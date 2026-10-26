-- =============================================================================
-- 02_bronze_tables.sql
-- GCP Medallion Architecture: Bronze Dynamic Procedures & Unified View Refresher
-- Project: medallion-project-512608 | Location: europe-west1
--
-- NOTE: Bronze raw ingestion tables (bronze.raw_index_XXXX) are NOT created
-- statically. They are created completely AUTONOMOUSLY and ON-THE-FLY by the
-- Eventarc Cloud Run Function (main.py) with BigQuery LoadJob autodetection
-- whenever a new CSV/JSON file is uploaded to gs://<bucket>/raw/index_XXXX/*
-- =============================================================================

-- Dynamic Stored Procedure: Rebuilds bronze.raw_records_unified across all active Bronze tables
CREATE OR REPLACE PROCEDURE `bronze.sp_refresh_raw_records_unified`()
BEGIN
  DECLARE v_tables ARRAY<STRING>;
  DECLARE v_sql STRING DEFAULT '';
  DECLARE i INT64 DEFAULT 0;

  -- 1. Discover all existing physical bronze tables in INFORMATION_SCHEMA
  SET v_tables = (
    SELECT ARRAY_AGG(table_name ORDER BY table_name)
    FROM `medallion-project-512608.bronze.INFORMATION_SCHEMA.TABLES`
    WHERE table_name LIKE 'raw_index_%'
  );

  -- If no bronze tables have been ingested yet, create an empty placeholder view
  IF COALESCE(ARRAY_LENGTH(v_tables), 0) = 0 THEN
    EXECUTE IMMEDIATE """
      CREATE OR REPLACE VIEW `bronze.raw_records_unified` AS
      SELECT
        CAST(NULL AS STRING) AS source_id,
        CAST(NULL AS STRING) AS source_entity_id,
        CAST(NULL AS DATE) AS ingest_date,
        CAST(NULL AS TIMESTAMP) AS ingest_timestamp,
        CAST(NULL AS STRING) AS file_name,
        CAST(NULL AS STRING) AS raw_payload_json
      LIMIT 0
    """;
    RETURN;
  END IF;

  -- 2. Dynamically construct UNION ALL across all discovered raw_index_* tables
  WHILE i < ARRAY_LENGTH(v_tables) DO
    IF i > 0 THEN
      SET v_sql = CONCAT(v_sql, ' UNION ALL ');
    END IF;
    SET v_sql = CONCAT(
      v_sql,
      FORMAT('SELECT CAST(source_id AS STRING) AS source_id, CAST(source_entity_id AS STRING) AS source_entity_id, CAST(ingest_date AS DATE) AS ingest_date, CAST(ingest_timestamp AS TIMESTAMP) AS ingest_timestamp, CAST(file_name AS STRING) AS file_name, TO_JSON_STRING(t) AS raw_payload_json FROM `medallion-project-512608.bronze.%s` t', v_tables[OFFSET(i)])
    );
    SET i = i + 1;
  END WHILE;

  -- 3. Replace unified view on-the-fly
  EXECUTE IMMEDIATE CONCAT('CREATE OR REPLACE VIEW `medallion-project-512608.bronze.raw_records_unified` AS ', v_sql);
END;

-- Initialize the unified view (placeholder if zero tables exist yet)
CALL `bronze.sp_refresh_raw_records_unified`();
