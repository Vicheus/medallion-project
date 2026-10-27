-- =============================================================================
-- 05_monitoring_and_audit.sql
-- GCP Medallion Architecture: Observability, Discrepancy Checks, and Orchestration
-- Project: medallion-project-512608 | Location: europe-west1
-- =============================================================================

-- 0. Table: Ingestion File Manifest & Idempotent Audit Registry
CREATE TABLE IF NOT EXISTS `ops_monitoring.ingestion_manifest` (
  file_path STRING NOT NULL OPTIONS(description="Full GCS URI of the ingested file (e.g. gs://bucket/raw/index_0001/file.csv)"),
  file_name STRING NOT NULL OPTIONS(description="Base file name"),
  source_id STRING NOT NULL OPTIONS(description="Source identifier (e.g. index_0001)"),
  file_hash_sha256 STRING OPTIONS(description="SHA-256 or MD5 hash of file content for change detection"),
  first_ingest_timestamp TIMESTAMP NOT NULL OPTIONS(description="Immutable timestamp of the initial ingestion"),
  first_ingest_date DATE NOT NULL OPTIONS(description="Immutable partition date of the initial ingestion"),
  last_reupload_timestamp TIMESTAMP NOT NULL OPTIONS(description="Timestamp of the most recent re-upload"),
  reupload_count INT64 NOT NULL OPTIONS(description="Number of re-uploads (0 on initial load)"),
  record_count INT64 OPTIONS(description="Number of records loaded from this file"),
  status STRING NOT NULL OPTIONS(description="'PENDING', 'COMPLETED', 'FAILED', 'REPLACED'"),
  error_message STRING OPTIONS(description="Error message if ingestion failed"),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY first_ingest_date
CLUSTER BY source_id, file_name, status;

-- 1. Table: Pipeline Run Audit Logs
CREATE TABLE IF NOT EXISTS `ops_monitoring.pipeline_runs` (
  run_id STRING NOT NULL,
  pipeline_name STRING NOT NULL,
  ingest_date DATE NOT NULL,
  started_at TIMESTAMP NOT NULL,
  completed_at TIMESTAMP,
  status STRING NOT NULL OPTIONS(description="'STARTED', 'SUCCESS', 'FAILED'"),
  total_bronze_rows INT64,
  total_silver_rows INT64,
  total_gold_rows INT64,
  quarantined_rows INT64,
  error_message STRING
)
PARTITION BY ingest_date
CLUSTER BY status, pipeline_name;

-- 2. Table: Quarantined Records (Filtered out during validation)
CREATE TABLE IF NOT EXISTS `ops_monitoring.quarantined_records` (
  quarantine_id STRING NOT NULL,
  source_id STRING NOT NULL,
  source_entity_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  reason STRING NOT NULL,
  raw_payload STRING,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY source_id, reason;

-- 3. Table: Layer Discrepancy & Integrity Log
CREATE TABLE IF NOT EXISTS `ops_monitoring.layer_discrepancy_log` (
  log_id STRING NOT NULL,
  check_name STRING NOT NULL,
  check_category STRING NOT NULL,
  layer_from STRING,
  layer_to STRING,
  expected_count INT64,
  actual_count INT64,
  discrepancy_count INT64,
  status STRING NOT NULL OPTIONS(description="'PASS', 'WARNING', 'FAIL'"),
  details STRING,
  ingest_date DATE NOT NULL,
  check_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY status, check_category;

-- 4. Table: Source SLA Freshness Configuration
CREATE TABLE IF NOT EXISTS `ops_monitoring.source_sla_config` (
  source_id STRING NOT NULL,
  update_frequency STRING DEFAULT 'STATIC',
  max_staleness_hours INT64,
  min_expected_rows INT64 NOT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- Ensure schema evolution for existing tables
ALTER TABLE `ops_monitoring.source_sla_config`
ADD COLUMN IF NOT EXISTS update_frequency STRING;

ALTER TABLE `ops_monitoring.source_sla_config`
ALTER COLUMN update_frequency SET DEFAULT 'STATIC';

UPDATE `ops_monitoring.source_sla_config`
SET update_frequency = 'STATIC'
WHERE update_frequency IS NULL;

-- 5. Freshness Monitoring View (Dynamically resolves across source_catalog)
CREATE OR REPLACE VIEW `ops_monitoring.v_source_freshness` AS
WITH source_history AS (
  SELECT
    source_id,
    MAX(ingest_timestamp) AS last_ingest_ts,
    COUNTIF(ingest_date = CURRENT_DATE()) AS row_count_today,
    COUNT(*) AS total_rows_all_time
  FROM `bronze.raw_records_unified`
  GROUP BY source_id
)
SELECT
  c.source_id,
  c.source_name,
  COALESCE(s.update_frequency, 'STATIC') AS update_frequency,
  h.last_ingest_ts AS last_ingest_timestamp,
  CASE
    WHEN h.last_ingest_ts IS NOT NULL THEN TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), h.last_ingest_ts, HOUR)
    ELSE NULL
  END AS hours_since_last_ingest,
  COALESCE(h.row_count_today, 0) AS rows_ingested_today,
  COALESCE(h.total_rows_all_time, 0) AS total_rows_all_time,
  COALESCE(s.min_expected_rows, 50) AS min_expected_rows,
  s.max_staleness_hours,
  CASE
    -- 1. No data has ever been loaded for this active source
    WHEN h.last_ingest_ts IS NULL THEN 'CRITICAL_NO_DATA'
    -- 2. Low volume check against minimum expected rows
    WHEN COALESCE(h.total_rows_all_time, 0) < COALESCE(s.min_expected_rows, 50) THEN 'LOW_VOLUME_WARNING'
    -- 3. Static / one-off leak dump: Once loaded, permanently HEALTHY!
    WHEN COALESCE(s.update_frequency, 'STATIC') = 'STATIC' OR s.max_staleness_hours IS NULL THEN 'HEALTHY'
    -- 4. Recurring feed: evaluate staleness
    WHEN TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), h.last_ingest_ts, HOUR) > s.max_staleness_hours THEN 'STALE'
    ELSE 'HEALTHY'
  END AS freshness_status
FROM `ops_monitoring.source_catalog` c
LEFT JOIN `ops_monitoring.source_sla_config` s ON c.source_id = s.source_id
LEFT JOIN source_history h ON c.source_id = h.source_id
WHERE c.is_active = TRUE;

-- 6. Audit View: AI Agent Query Activity & Error Observability
CREATE OR REPLACE VIEW `ops_monitoring.v_ai_agent_query_audit` AS
SELECT
  job_id,
  creation_time,
  start_time,
  end_time,
  user_email,
  query,
  state,
  error_result.message AS error_message,
  total_bytes_billed,
  total_slot_ms,
  referenced_tables
FROM `region-europe-west1.INFORMATION_SCHEMA.JOBS_BY_PROJECT`
WHERE user_email = 'ai-agent-reader@medallion-project-512608.iam.gserviceaccount.com'
ORDER BY creation_time DESC;

-- =============================================================================
-- Stored Procedure: sp_register_and_get_ingest_metadata
-- Implements idempotent manifest lookup: preserves original ingest date on re-uploads
-- =============================================================================
CREATE OR REPLACE PROCEDURE `ops_monitoring.sp_register_and_get_ingest_metadata`(
  IN p_file_path STRING,
  IN p_file_name STRING,
  IN p_source_id STRING,
  IN p_file_hash STRING,
  IN p_record_count INT64,
  OUT out_ingest_date DATE,
  OUT out_ingest_timestamp TIMESTAMP,
  OUT out_is_reupload BOOLEAN,
  OUT out_reupload_count INT64
)
BEGIN
  DECLARE v_row STRUCT<first_ingest_date DATE, first_ingest_timestamp TIMESTAMP, reupload_count INT64>;

  -- 1. Check if file already exists in manifest
  SET v_row = (
    SELECT AS STRUCT first_ingest_date, first_ingest_timestamp, reupload_count
    FROM `ops_monitoring.ingestion_manifest`
    WHERE file_path = p_file_path OR (source_id = p_source_id AND file_name = p_file_name)
    ORDER BY first_ingest_timestamp ASC
    LIMIT 1
  );

  IF v_row.first_ingest_date IS NOT NULL THEN
    -- Case: Re-upload of an existing file (Idempotent replay)
    SET out_ingest_date = v_row.first_ingest_date;
    SET out_ingest_timestamp = v_row.first_ingest_timestamp;
    SET out_is_reupload = TRUE;
    SET out_reupload_count = v_row.reupload_count + 1;

    UPDATE `ops_monitoring.ingestion_manifest`
    SET
      last_reupload_timestamp = CURRENT_TIMESTAMP(),
      reupload_count = v_row.reupload_count + 1,
      record_count = p_record_count,
      file_hash_sha256 = COALESCE(p_file_hash, file_hash_sha256),
      status = 'COMPLETED',
      error_message = NULL
    WHERE file_path = p_file_path OR (source_id = p_source_id AND file_name = p_file_name);
  ELSE
    -- Case: New file initial upload
    SET out_ingest_date = CURRENT_DATE();
    SET out_ingest_timestamp = CURRENT_TIMESTAMP();
    SET out_is_reupload = FALSE;
    SET out_reupload_count = 0;

    INSERT INTO `ops_monitoring.ingestion_manifest` (
      file_path, file_name, source_id, file_hash_sha256,
      first_ingest_timestamp, first_ingest_date,
      last_reupload_timestamp, reupload_count,
      record_count, status
    ) VALUES (
      p_file_path, p_file_name, p_source_id, p_file_hash,
      out_ingest_timestamp, out_ingest_date,
      out_ingest_timestamp, 0,
      p_record_count, 'COMPLETED'
    );
  END IF;
END;

-- =============================================================================
-- Stored Procedure: sp_purge_file_records
-- Removes previously loaded records for a file before idempotent reload
-- =============================================================================
CREATE OR REPLACE PROCEDURE `ops_monitoring.sp_purge_file_records`(
  IN p_table_name STRING,
  IN p_file_name STRING,
  IN p_ingest_date DATE
)
BEGIN
  EXECUTE IMMEDIATE FORMAT(
    "DELETE FROM `bronze.%s` WHERE file_name = @fn AND ingest_date = @idate",
    p_table_name
  ) USING p_file_name AS fn, p_ingest_date AS idate;
END;

-- =============================================================================
-- Stored Procedure: sp_run_discrepancy_checks
-- =============================================================================
CREATE OR REPLACE PROCEDURE `ops_monitoring.sp_run_discrepancy_checks`(p_ingest_date DATE)
OPTIONS(strict_mode=false)
BEGIN
  DECLARE v_date DATE DEFAULT COALESCE(p_ingest_date, CURRENT_DATE());
  DECLARE v_bronze_count INT64;
  DECLARE v_silver_count INT64;
  DECLARE v_gold_count INT64;
  DECLARE v_unmatched_ids INT64;
  DECLARE v_supernode_count INT64;
  DECLARE v_suspect_details STRING DEFAULT '';
  DECLARE v_hash_collisions INT64;

  -- Clean today's check logs
  DELETE FROM `ops_monitoring.layer_discrepancy_log` WHERE ingest_date = v_date;

  -- Count rows across layers
  SET v_bronze_count = (SELECT COUNT(*) FROM `bronze.raw_records_unified` WHERE ingest_date = v_date);
  SET v_silver_count = (
    SELECT COUNT(DISTINCT source_entity_id) FROM (
      SELECT source_entity_id FROM `silver.persons` WHERE ingest_date = v_date
      UNION DISTINCT
      SELECT source_entity_id FROM `silver.vehicles` WHERE ingest_date = v_date
      UNION DISTINCT
      SELECT source_entity_id FROM `silver.movements` WHERE ingest_date = v_date
    )
  );
  SET v_gold_count = (SELECT COUNT(*) FROM `gold.person_profiles_master` WHERE ingest_date = v_date);

  -- ---------------------------------------------------------------------------
  -- Check 1: Bronze -> Silver Reconciliation (LEFT_ANTI Check)
  -- ---------------------------------------------------------------------------
  -- Count how many raw records were filtered out during Silver extraction across all domain entities
  SET v_unmatched_ids = (
    SELECT COUNT(*)
    FROM `bronze.raw_records_unified` b
    WHERE b.ingest_date = v_date
      AND NOT EXISTS (
        SELECT 1 FROM `silver.persons` s WHERE s.source_entity_id = b.source_entity_id AND s.ingest_date = v_date
      )
      AND NOT EXISTS (
        SELECT 1 FROM `silver.vehicles` v WHERE v.source_entity_id = b.source_entity_id AND v.ingest_date = v_date
      )
      AND NOT EXISTS (
        SELECT 1 FROM `silver.movements` m WHERE m.source_entity_id = b.source_entity_id AND m.ingest_date = v_date
      )
  );

  INSERT INTO `ops_monitoring.layer_discrepancy_log` (
    log_id, check_name, check_category, layer_from, layer_to, expected_count, actual_count, discrepancy_count, status, details, ingest_date
  ) VALUES (
    GENERATE_UUID(),
    'bronze_to_silver_drop_rate',
    'RECONCILIATION',
    'bronze',
    'silver',
    v_bronze_count,
    v_silver_count,
    v_unmatched_ids,
    CASE WHEN v_bronze_count > 0 AND (v_unmatched_ids / v_bronze_count) > 0.35 THEN 'WARNING' ELSE 'PASS' END,
    FORMAT('Bronze rows: %d, Silver rows: %d, Filtered invalid rows: %d (%.2f%% drop rate)',
      v_bronze_count, v_silver_count, v_unmatched_ids,
      IF(v_bronze_count > 0, (v_unmatched_ids / v_bronze_count) * 100.0, 0.0)),
    v_date
  );

  -- ---------------------------------------------------------------------------
  -- Check 2: Silver -> Gold Identity Conservation
  -- ---------------------------------------------------------------------------
  -- Asserts that every valid person in Silver with a non-null name is mapped into Gold
  SET v_unmatched_ids = (
    SELECT COUNT(DISTINCT s.source_entity_id)
    FROM `silver.persons` s
    WHERE s.ingest_date = v_date AND s.full_name IS NOT NULL
      AND NOT EXISTS (
        SELECT 1 FROM `gold.person_profiles_master` g, UNNEST(g.source_entity_ids) AS eid
        WHERE eid = s.source_entity_id AND g.ingest_date = v_date
      )
  );

  INSERT INTO `ops_monitoring.layer_discrepancy_log` (
    log_id, check_name, check_category, layer_from, layer_to, expected_count, actual_count, discrepancy_count, status, details, ingest_date
  ) VALUES (
    GENERATE_UUID(),
    'silver_to_gold_conservation',
    'COMPLETENESS',
    'silver',
    'gold',
    v_silver_count,
    v_gold_count,
    v_unmatched_ids,
    CASE WHEN v_unmatched_ids = 0 THEN 'PASS' ELSE 'FAIL' END,
    FORMAT('Unmapped Silver entity IDs in Gold: %d (expected 0 unexplained loss)', v_unmatched_ids),
    v_date
  );

  -- ---------------------------------------------------------------------------
  -- Check 3: Gold Entity Anomaly & Suspicious Cluster Check
  -- ---------------------------------------------------------------------------
  -- Flags any resolved person entity marked as suspicious (super-nodes, anomalous age, dummy contacts, timeline conflicts, etc.)
  SET (v_supernode_count, v_suspect_details) = (
    SELECT AS STRUCT
      COUNT(*),
      CASE
        WHEN COUNT(*) > 0 THEN
          FORMAT('Suspicious profiles: %d. Sources: [%s]. Top suspect: "%s" (Reason: %s, source: %s)',
            COUNT(*),
            COALESCE(ARRAY_TO_STRING(ARRAY_AGG(DISTINCT s_id IGNORE NULLS), ', '), 'UNKNOWN'),
            COALESCE(ANY_VALUE(primary_full_name), 'UNKNOWN'),
            COALESCE(ANY_VALUE(suspicious_reason), 'UNKNOWN'),
            COALESCE(ARRAY_TO_STRING(ANY_VALUE(source_ids), ', '), 'UNKNOWN')
          )
        ELSE 'Pass: 0 suspicious profiles detected.'
      END
    FROM `gold.person_profiles_master` g
    LEFT JOIN UNNEST(g.source_ids) AS s_id
    WHERE g.ingest_date = v_date AND g.is_suspicious_cluster = TRUE
  );

  INSERT INTO `ops_monitoring.layer_discrepancy_log` (
    log_id, check_name, check_category, layer_from, layer_to, expected_count, actual_count, discrepancy_count, status, details, ingest_date
  ) VALUES (
    GENERATE_UUID(),
    'gold_suspicious_cluster_check',
    'ANOMALY',
    'silver',
    'gold',
    0,
    v_supernode_count,
    v_supernode_count,
    CASE WHEN v_supernode_count = 0 THEN 'PASS' ELSE 'WARNING' END,
    v_suspect_details,
    v_date
  );

  -- ---------------------------------------------------------------------------
  -- Check 4: Hash Collision Check
  -- ---------------------------------------------------------------------------
  -- Asserts COUNT(*) = COUNT(DISTINCT person_id) in Gold
  SET v_hash_collisions = (
    SELECT (COUNT(*) - COUNT(DISTINCT person_id))
    FROM `gold.person_profiles_master`
    WHERE ingest_date = v_date
  );

  INSERT INTO `ops_monitoring.layer_discrepancy_log` (
    log_id, check_name, check_category, layer_from, layer_to, expected_count, actual_count, discrepancy_count, status, details, ingest_date
  ) VALUES (
    GENERATE_UUID(),
    'gold_hash_collision_check',
    'INTEGRITY',
    'gold',
    'gold',
    0,
    v_hash_collisions,
    v_hash_collisions,
    CASE WHEN v_hash_collisions = 0 THEN 'PASS' ELSE 'FAIL' END,
    FORMAT('Duplicate person_id hash collisions detected: %d', v_hash_collisions),
    v_date
  );

END;

-- =============================================================================
-- Master Orchestration Stored Procedure: sp_run_medallion_pipeline
-- =============================================================================
CREATE OR REPLACE PROCEDURE `ops_monitoring.sp_run_medallion_pipeline`()
OPTIONS(strict_mode=false)
BEGIN
  DECLARE v_run_id STRING DEFAULT GENERATE_UUID();
  DECLARE v_date DATE DEFAULT CURRENT_DATE();
  DECLARE v_b_count INT64 DEFAULT 0;
  DECLARE v_s_count INT64 DEFAULT 0;
  DECLARE v_g_count INT64 DEFAULT 0;

  -- 1. Log Run Start
  INSERT INTO `ops_monitoring.pipeline_runs` (
    run_id, pipeline_name, ingest_date, started_at, status
  ) VALUES (
    v_run_id, 'medallion_daily_pipeline', v_date, CURRENT_TIMESTAMP(), 'STARTED'
  );

  BEGIN
    -- 2. Execute Bronze -> Silver Entity Extraction
    CALL `silver.sp_transform_to_silver`(v_date);

    -- 3. Execute Silver -> Gold Identity Resolution & Fact Build
    CALL `gold.sp_build_gold`(v_date);

    -- 4. Execute Automated Discrepancy & Health Checks
    CALL `ops_monitoring.sp_run_discrepancy_checks`(v_date);

    -- 5. Count final metrics
    SET v_b_count = (SELECT COUNT(*) FROM `bronze.raw_records_unified` WHERE ingest_date = v_date);
    SET v_s_count = (SELECT COUNT(*) FROM `silver.persons` WHERE ingest_date = v_date);
    SET v_g_count = (SELECT COUNT(*) FROM `gold.person_profiles_master` WHERE ingest_date = v_date);

    -- 6. Log Run Success
    UPDATE `ops_monitoring.pipeline_runs`
    SET
      completed_at = CURRENT_TIMESTAMP(),
      status = 'SUCCESS',
      total_bronze_rows = v_b_count,
      total_silver_rows = v_s_count,
      total_gold_rows = v_g_count
    WHERE run_id = v_run_id;

  EXCEPTION WHEN ERROR THEN
    -- Log Run Failure
    UPDATE `ops_monitoring.pipeline_runs`
    SET
      completed_at = CURRENT_TIMESTAMP(),
      status = 'FAILED',
      error_message = @@error.message
    WHERE run_id = v_run_id;

    -- Re-raise error for BigQuery Scheduled Query monitoring
    RAISE USING MESSAGE = CONCAT('MEDALLION_PIPELINE_ERROR: ', @@error.message);
  END;

END;
