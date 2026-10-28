"""
GCS to BigQuery Eventarc Trigger Function (Cloud Run Functions / 2nd gen).
Autonomous, Event-Driven Medallion Pipeline Ingestion ("Drop CSV -> Gold").

Listens for: google.cloud.storage.object.v1.finalized
Target Path: gs://<bucket>/raw/<source_id>/<any_filename>.csv
Bronze Table: bronze.raw_<source_id>
Manifest: ops_monitoring.ingestion_manifest
Catalog: ops_monitoring.source_catalog
Dynamic Silver Engine: silver.sp_transform_metadata_source / silver.sp_transform_to_silver
Gold Engine: gold.sp_build_gold
Discrepancy Checks: ops_monitoring.sp_run_discrepancy_checks
"""

import os
import re
import csv
import io
import json
import uuid
import logging
from datetime import datetime, date, timezone
from typing import Dict, Any, Tuple, Optional

import functions_framework
from cloudevents.http import CloudEvent
from google.cloud import bigquery
from google.cloud import storage
from google.cloud import dataform_v1

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("gcs_ingest_trigger")

PROJECT_ID = os.environ.get("PROJECT_ID", "medallion-project-512608")
LOCATION = os.environ.get("LOCATION", "europe-west1")
DATASET_BRONZE = "bronze"
DATASET_SILVER = "silver"
DATASET_GOLD = "gold"
DATASET_OPS = "ops_monitoring"

# Regex pattern to match raw uploads:
# Matches: raw/index_0001/file.csv, raw/index_0042/orders.csv, raw/index_0500/dump.csv
RAW_PATH_REGEX = re.compile(r"^raw/([^/]+)/(.+)$")


def get_bigquery_client() -> bigquery.Client:
    return bigquery.Client(project=PROJECT_ID, location=LOCATION)


def parse_gcs_path(gcs_path: str) -> Optional[Tuple[str, str]]:
    """
    Extracts (source_id, file_name) from GCS object path.
    Example: raw/index_0001/subfolder/data.csv -> ("index_0001", "data.csv")
    """
    match = RAW_PATH_REGEX.match(gcs_path)
    if not match:
        return None
    source_id = match.group(1)
    file_name = os.path.basename(match.group(2))
    return source_id, file_name


def check_and_update_manifest(
    bq_client: bigquery.Client,
    file_path: str,
    file_name: str,
    source_id: str,
    file_hash: Optional[str] = None
) -> Tuple[date, datetime, bool, int]:
    """
    Queries ops_monitoring.ingestion_manifest to guarantee idempotent reloads:
    - If file was already loaded in history: returns original ingest date & timestamp,
      increments reupload_count.
    - If new: creates manifest entry with current timestamp and reupload_count=0.
    """
    manifest_table = f"`{PROJECT_ID}.{DATASET_OPS}.ingestion_manifest`"

    lookup_query = f"""
    SELECT
        first_ingest_date,
        first_ingest_timestamp,
        reupload_count
    FROM {manifest_table}
    WHERE file_path = @file_path OR (source_id = @source_id AND file_name = @file_name)
    ORDER BY first_ingest_timestamp ASC
    LIMIT 1
    """

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("file_path", "STRING", file_path),
            bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
            bigquery.ScalarQueryParameter("file_name", "STRING", file_name),
        ]
    )

    query_job = bq_client.query(lookup_query, job_config=job_config)
    results = list(query_job.result())

    if results:
        row = results[0]
        first_date = row.first_ingest_date
        first_ts = row.first_ingest_timestamp
        reupload_count = row.reupload_count + 1
        is_reupload = True

        logger.info(
            f"[IDEMPOTENCY] Existing file detected for {file_path}. "
            f"Preserving original ingest_date={first_date}, reupload_count={reupload_count}"
        )

        update_query = f"""
        UPDATE {manifest_table}
        SET
            last_reupload_timestamp = CURRENT_TIMESTAMP(),
            reupload_count = @reupload_count,
            file_hash_sha256 = COALESCE(@file_hash, file_hash_sha256),
            status = 'PROCESSING',
            error_message = NULL
        WHERE file_path = @file_path OR (source_id = @source_id AND file_name = @file_name)
        """
        update_job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("reupload_count", "INT64", reupload_count),
                bigquery.ScalarQueryParameter("file_hash", "STRING", file_hash or ""),
                bigquery.ScalarQueryParameter("file_path", "STRING", file_path),
                bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
                bigquery.ScalarQueryParameter("file_name", "STRING", file_name),
            ]
        )
        bq_client.query(update_query, job_config=update_job_config).result()
        return first_date, first_ts, is_reupload, reupload_count

    else:
        now_ts = datetime.now(timezone.utc)
        today_date = now_ts.date()
        is_reupload = False
        reupload_count = 0

        logger.info(f"[MANIFEST] Registering new file: {file_path} with ingest_date={today_date}")

        insert_query = f"""
        INSERT INTO {manifest_table} (
            file_path, file_name, source_id, file_hash_sha256,
            first_ingest_timestamp, first_ingest_date,
            last_reupload_timestamp, reupload_count,
            record_count, status
        ) VALUES (
            @file_path, @file_name, @source_id, @file_hash,
            @first_ts, @first_date,
            @first_ts, 0,
            0, 'PROCESSING'
        )
        """
        insert_job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("file_path", "STRING", file_path),
                bigquery.ScalarQueryParameter("file_name", "STRING", file_name),
                bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
                bigquery.ScalarQueryParameter("file_hash", "STRING", file_hash or ""),
                bigquery.ScalarQueryParameter("first_ts", "TIMESTAMP", now_ts),
                bigquery.ScalarQueryParameter("first_date", "DATE", today_date),
            ]
        )
        bq_client.query(insert_query, job_config=insert_job_config).result()
        return today_date, now_ts, is_reupload, reupload_count


def purge_old_file_records(
    bq_client: bigquery.Client,
    table_id: str,
    file_name: str,
    ingest_date: date
) -> int:
    """
    Purges any previous records for this file from the Bronze table
    to guarantee zero duplicates on re-upload.
    """
    try:
        bq_client.get_table(table_id)
    except Exception:
        logger.info(f"Table {table_id} does not exist yet. Skipping purge.")
        return 0

    purge_sql = f"""
    DELETE FROM `{table_id}`
    WHERE file_name = @file_name AND ingest_date = @ingest_date
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("file_name", "STRING", file_name),
            bigquery.ScalarQueryParameter("ingest_date", "DATE", ingest_date),
        ]
    )
    res = bq_client.query(purge_sql, job_config=job_config).result()
    deleted_rows = res.num_dml_affected_rows or 0
    logger.info(f"[IDEMPOTENCY] Purged {deleted_rows} previous records for {file_name} from {table_id}")
    return deleted_rows


def extract_csv_headers_from_gcs(gcs_uri: str) -> list:
    """
    Downloads the first chunk (up to 64KB) of a CSV from GCS and parses the header row.
    Returns cleaned BigQuery-compatible column names (lowercase, alphanumeric).
    """
    try:
        storage_client = storage.Client(project=PROJECT_ID)
        bucket_name, blob_name = gcs_uri.replace("gs://", "").split("/", 1)
        blob = storage_client.bucket(bucket_name).blob(blob_name)

        # Download first 64KB (sufficient for wide tables with dozens of columns)
        chunk = blob.download_as_bytes(start=0, end=65536)
        text = chunk.decode("utf-8", errors="replace")
        lines = text.splitlines()
        if not lines:
            return []

        reader = csv.reader(io.StringIO(lines[0]))
        raw_headers = next(reader, [])

        clean_headers = []
        seen = set()
        for idx, h in enumerate(raw_headers):
            clean_name = h.lstrip("\ufeff").strip()
            clean_name = re.sub(r"[^a-zA-Z0-9_]", "_", clean_name)
            if not clean_name or clean_name[0].isdigit():
                clean_name = f"col_{clean_name}"
            clean_name = clean_name.lower()
            if clean_name in seen:
                clean_name = f"{clean_name}_{idx}"
            seen.add(clean_name)
            clean_headers.append(clean_name)

        return clean_headers
    except Exception as exc:
        logger.warning(f"Could not extract headers from {gcs_uri}: {exc}")
        return []


def load_file_into_bronze(
    bq_client: bigquery.Client,
    gcs_uri: str,
    source_id: str,
    file_name: str,
    ingest_date: date,
    ingest_timestamp: datetime
) -> int:
    """
    Loads raw CSV into Bronze table using resilient All-String schema architecture.
    Guarantees:
    1. Table is initialized with all business columns as STRING (zero type-mismatch crashes).
    2. New columns are detected and added dynamically via ALTER TABLE ... ADD COLUMN ... STRING.
    3. Metadata fields (ingest_date, ingest_timestamp, file_name, source_id, source_entity_id) are enforced.
    """
    table_id = f"{PROJECT_ID}.{DATASET_BRONZE}.raw_{source_id}"
    clean_headers = extract_csv_headers_from_gcs(gcs_uri)

    try:
        table = bq_client.get_table(table_id)
        table_exists = True
    except Exception:
        table_exists = False
        table = None

    if not table_exists:
        if clean_headers:
            # Build schema: all business fields are STRING, while partitioning/timestamp fields maintain exact temporal types
            schema = []
            seen = set()
            for col in clean_headers:
                if col == "ingest_date":
                    schema.append(bigquery.SchemaField("ingest_date", "DATE", mode="NULLABLE"))
                elif col == "ingest_timestamp":
                    schema.append(bigquery.SchemaField("ingest_timestamp", "TIMESTAMP", mode="NULLABLE"))
                else:
                    schema.append(bigquery.SchemaField(col, "STRING", mode="NULLABLE"))
                seen.add(col)

            # Ensure standard medallion metadata columns
            if "ingest_date" not in seen:
                schema.append(bigquery.SchemaField("ingest_date", "DATE", mode="NULLABLE"))
            if "ingest_timestamp" not in seen:
                schema.append(bigquery.SchemaField("ingest_timestamp", "TIMESTAMP", mode="NULLABLE"))
            if "file_name" not in seen:
                schema.append(bigquery.SchemaField("file_name", "STRING", mode="NULLABLE"))
            if "source_id" not in seen:
                schema.append(bigquery.SchemaField("source_id", "STRING", mode="NULLABLE"))
            if "source_entity_id" not in seen:
                schema.append(bigquery.SchemaField("source_entity_id", "STRING", mode="NULLABLE"))

            new_table = bigquery.Table(table_id, schema=schema)
            new_table.time_partitioning = bigquery.TimePartitioning(
                type_=bigquery.TimePartitioningType.DAY,
                field="ingest_date"
            )
            bq_client.create_table(new_table)
            logger.info(f"[BRONZE_INIT] Created new Bronze table {table_id} with {len(schema)} columns (partitioned by ingest_date DATE).")
            table = bq_client.get_table(table_id)
        else:
            logger.info(f"Table {table_id} does not exist and headers empty. Will rely on LoadJob autodetection.")
    else:
        # Check if new columns exist in incoming CSV and alter table on the fly
        if clean_headers:
            existing_cols = {f.name.lower() for f in table.schema}
            new_cols = [c for c in clean_headers if c not in existing_cols]
            if new_cols:
                alter_clauses = []
                for c in new_cols:
                    if c == "ingest_date":
                        alter_clauses.append("ADD COLUMN IF NOT EXISTS `ingest_date` DATE")
                    elif c == "ingest_timestamp":
                        alter_clauses.append("ADD COLUMN IF NOT EXISTS `ingest_timestamp` TIMESTAMP")
                    else:
                        alter_clauses.append(f"ADD COLUMN IF NOT EXISTS `{c}` STRING")
                alter_sql = f"ALTER TABLE `{table_id}` " + ", ".join(alter_clauses) + ";"
                logger.info(f"[SCHEMA_EVOLUTION] Adding {len(new_cols)} new column(s) to {table_id}: {new_cols}")
                bq_client.query(alter_sql).result()
                table = bq_client.get_table(table_id)

    # Load raw CSV into Bronze table
    # When table exists with predefined STRING schema, autodetect must be False
    # to prevent BigQuery from guessing INTEGER and conflicting with STRING schema.
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=False if table else True,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        allow_quoted_newlines=True,
        ignore_unknown_values=True
    )
    if not table:
        job_config.schema_update_options = [bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION]

    logger.info(f"[INGEST] Starting LoadJob: {gcs_uri} -> {table_id} (autodetect={job_config.autodetect})")
    load_job = bq_client.load_table_from_uri(gcs_uri, table_id, job_config=job_config)
    load_job.result()  # Wait for job completion
    loaded_rows = load_job.output_rows or 0
    logger.info(f"[INGEST] Successfully loaded {loaded_rows} rows into {table_id}")

    # 2. Ensure all standard Medallion metadata columns exist
    alter_sql = f"""
    ALTER TABLE `{table_id}`
    ADD COLUMN IF NOT EXISTS ingest_date DATE,
    ADD COLUMN IF NOT EXISTS ingest_timestamp TIMESTAMP,
    ADD COLUMN IF NOT EXISTS file_name STRING,
    ADD COLUMN IF NOT EXISTS source_id STRING,
    ADD COLUMN IF NOT EXISTS source_entity_id STRING;
    """
    try:
        bq_client.query(alter_sql).result()
    except Exception as exc:
        logger.warning(f"Metadata column check note on {table_id}: {exc}")

    # 3. Populate missing metadata columns on new records
    update_metadata_sql = f"""
    UPDATE `{table_id}`
    SET
        ingest_date = COALESCE(ingest_date, @ingest_date),
        ingest_timestamp = COALESCE(ingest_timestamp, @ingest_ts),
        file_name = COALESCE(file_name, @file_name),
        source_id = COALESCE(source_id, @source_id),
        source_entity_id = COALESCE(source_entity_id, GENERATE_UUID())
    WHERE ingest_date IS NULL OR file_name IS NULL OR source_id IS NULL OR source_entity_id IS NULL;
    """
    update_job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("ingest_date", "DATE", ingest_date),
            bigquery.ScalarQueryParameter("ingest_ts", "TIMESTAMP", ingest_timestamp),
            bigquery.ScalarQueryParameter("file_name", "STRING", file_name),
            bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
        ]
    )
    bq_client.query(update_metadata_sql, job_config=update_job_config).result()

    # 4. Refresh bronze unified view so new tables are automatically discoverable
    try:
        bq_client.query(f"CALL `{PROJECT_ID}.{DATASET_BRONZE}.sp_refresh_raw_records_unified`()").result()
    except Exception as exc:
        logger.warning(f"Could not refresh raw_records_unified view: {exc}")

    return loaded_rows


def trigger_downstream_pipeline(
    bq_client: bigquery.Client,
    source_id: str,
    ingest_date: date,
    started_at: datetime,
    file_name: str = ""
) -> Dict[str, Any]:
    """
    Autonomous orchestration of Silver entity extraction and Gold identity resolution:
    1. Checks ops_monitoring.source_catalog for pipeline_type (METADATA_DRIVEN vs DATAFORM_DAG).
    2. Runs silver extraction (sp_transform_metadata_source or sp_transform_to_silver).
    3. Runs gold consolidation (gold.sp_build_gold).
    4. Runs discrepancy checks (ops_monitoring.sp_run_discrepancy_checks).
    5. Records run metrics in ops_monitoring.pipeline_runs.
    """
    run_id = str(uuid.uuid4())
    catalog_table = f"`{PROJECT_ID}.{DATASET_OPS}.source_catalog`"
    catalog_query = f"""
    SELECT pipeline_type, is_active
    FROM {catalog_table}
    WHERE source_id = @source_id
    LIMIT 1
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("source_id", "STRING", source_id)
        ]
    )
    results = list(bq_client.query(catalog_query, job_config=job_config).result())

    if not results:
        logger.warning(
            f"[CATALOG] Source '{source_id}' is not yet registered in {catalog_table}. "
            "Bronze data loaded successfully. Register source YAML to enable automatic Silver extraction."
        )
        return {"status": "SKIPPED_UNREGISTERED", "reason": "source_not_in_catalog"}

    pipeline_type = results[0].pipeline_type
    is_active = results[0].is_active

    if not is_active:
        logger.info(f"[CATALOG] Source '{source_id}' is marked inactive. Skipping Silver extraction.")
        return {"status": "SKIPPED_INACTIVE"}

    logger.info(f"[PIPELINE] Executing Silver extraction for {source_id} (type: {pipeline_type}, run_id: {run_id})...")

    try:
        # Step 2: Silver Transformation
        if pipeline_type == "METADATA_DRIVEN":
            silver_call = f"CALL `{PROJECT_ID}.{DATASET_SILVER}.sp_transform_metadata_source`(@source_id, @ingest_date)"
            silver_job_config = bigquery.QueryJobConfig(
                query_parameters=[
                    bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
                    bigquery.ScalarQueryParameter("ingest_date", "DATE", ingest_date),
                ]
            )
            bq_client.query(silver_call, job_config=silver_job_config).result()
        else:
            # DATAFORM_DAG: Autonomous tag-driven Dataform execution
            try:
                import time
                df_client = dataform_v1.DataformClient()
                repo_path = df_client.repository_path(PROJECT_ID, LOCATION, "medallion-complex-pipelines")
                ws_name = f"{repo_path}/workspaces/prod-workspace"

                # 1. Compile Dataform models from workspace
                comp_req = dataform_v1.CreateCompilationResultRequest(
                    parent=repo_path,
                    compilation_result=dataform_v1.CompilationResult(workspace=ws_name)
                )
                comp_res = df_client.create_compilation_result(request=comp_req)

                # 2. Invoke workflow invocation filtered purely by source_id tag
                inv_req = dataform_v1.CreateWorkflowInvocationRequest(
                    parent=repo_path,
                    workflow_invocation=dataform_v1.WorkflowInvocation(
                        compilation_result=comp_res.name,
                        invocation_config=dataform_v1.InvocationConfig(
                            included_tags=[source_id],
                            transitive_dependencies_included=True
                        )
                    )
                )
                inv_res = df_client.create_workflow_invocation(request=inv_req)
                logger.info(f"[DATAFORM] Triggered Dataform workflow {inv_res.name} for tag: {source_id}")

                # 3. Wait for Dataform workflow execution to succeed before Gold layer runs
                for _ in range(30):
                    time.sleep(2)
                    inv = df_client.get_workflow_invocation(name=inv_res.name)
                    if inv.state.name == "SUCCEEDED":
                        logger.info(f"[DATAFORM] Workflow for tag {source_id} SUCCEEDED.")
                        break
                    elif inv.state.name in ("FAILED", "CANCELLED"):
                        raise RuntimeError(f"Dataform workflow invocation {inv_res.name} failed with state {inv.state.name}")
            except Exception as df_err:
                logger.error(f"[DATAFORM] Execution error for {source_id}: {df_err}")
                raise df_err

        # Step 2.5: Quarantine Invalid / Defective Records (Row-level defects)
        logger.info(f"[PIPELINE] Running quarantine isolation for source={source_id}, ingest_date={ingest_date}...")
        quarantine_call = f"CALL `{PROJECT_ID}.{DATASET_OPS}.sp_quarantine_invalid_records`(@ingest_date, @source_id)"
        quarantine_job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("ingest_date", "DATE", ingest_date),
                bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
            ]
        )
        bq_client.query(quarantine_call, job_config=quarantine_job_config).result()

        # Step 3: Gold Identity Resolution & Consolidation
        logger.info(f"[PIPELINE] Executing Gold layer consolidation for ingest_date={ingest_date}...")
        gold_call = f"CALL `{PROJECT_ID}.{DATASET_GOLD}.sp_build_gold`(@ingest_date)"
        gold_job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("ingest_date", "DATE", ingest_date),
            ]
        )
        bq_client.query(gold_call, job_config=gold_job_config).result()

        # Step 4: Discrepancy & Integrity Checks (Scoped by source_id and run_id)
        logger.info(f"[PIPELINE] Running automated discrepancy checks for source={source_id}, ingest_date={ingest_date}...")
        disc_call = f"CALL `{PROJECT_ID}.{DATASET_OPS}.sp_run_discrepancy_checks`(@ingest_date, @source_id, @run_id)"
        disc_job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("ingest_date", "DATE", ingest_date),
                bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
                bigquery.ScalarQueryParameter("run_id", "STRING", run_id),
            ]
        )
        bq_client.query(disc_call, job_config=disc_job_config).result()

        # Query discrepancy log for this run to emit structured alerts and determine run health
        disc_summary_sql = f"""
        SELECT check_name, check_category, source_id, status, details
        FROM `{PROJECT_ID}.{DATASET_OPS}.layer_discrepancy_log`
        WHERE run_id = @run_id AND status IN ('WARNING', 'FAIL')
        """
        has_fail = False
        has_warning = False
        anomaly_messages = []
        try:
            disc_q_config = bigquery.QueryJobConfig(
                query_parameters=[
                    bigquery.ScalarQueryParameter("run_id", "STRING", run_id),
                ]
            )
            for disc_row in bq_client.query(disc_summary_sql, job_config=disc_q_config).result():
                src_tag = f"source={disc_row.source_id or source_id} file={file_name} run_id={run_id}"
                msg = f"{disc_row.check_name} ({disc_row.check_category}): {disc_row.details}"
                anomaly_messages.append(f"[{disc_row.source_id or source_id}] {msg}")
                if disc_row.status == "FAIL":
                    has_fail = True
                    logger.error(f"[INTEGRITY_FAIL] [{src_tag}] {msg}")
                else:
                    has_warning = True
                    logger.warning(f"[ANOMALY] [{src_tag}] {msg}")
        except Exception as disc_err:
            logger.warning(f"Note: Could not query discrepancy summary: {disc_err}")

        # Check for quarantined records in this run
        quarantine_count_sql = f"""
        SELECT COUNT(*) AS q_cnt, STRING_AGG(DISTINCT reason, ', ' LIMIT 3) AS q_reasons
        FROM `{PROJECT_ID}.{DATASET_OPS}.quarantined_records`
        WHERE source_id = @source_id AND ingest_date = @ingest_date
        """
        quarantined_rows = 0
        try:
            q_res = list(bq_client.query(
                quarantine_count_sql,
                job_config=bigquery.QueryJobConfig(
                    query_parameters=[
                        bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
                        bigquery.ScalarQueryParameter("ingest_date", "DATE", ingest_date),
                    ]
                )
            ).result())
            if q_res and hasattr(q_res[0], "q_cnt"):
                try:
                    q_val = int(q_res[0].q_cnt)
                except (ValueError, TypeError):
                    q_val = 0
                if q_val > 0:
                    quarantined_rows = q_val
                    q_reasons = getattr(q_res[0], "q_reasons", None) or "validation_defects"
                    has_warning = True
                    q_note = f"Quarantined {quarantined_rows} invalid record(s) ({q_reasons})"
                    anomaly_messages.append(f"[{source_id}] {q_note}")
                    logger.warning(f"[ANOMALY] [source={source_id} file={file_name} run_id={run_id}] {q_note}")
        except Exception as q_err:
            logger.warning(f"Note: Could not check quarantined records count: {q_err}")

        # Step 5: Record execution in ops_monitoring.pipeline_runs
        silver_count_expr = f"(SELECT COUNT(*) FROM `{PROJECT_ID}.{DATASET_SILVER}.persons` WHERE source_id = @source_id AND ingest_date = @ingest_date)"
        if source_id == "index_0020":
            silver_count_expr = f"(SELECT COUNT(*) FROM `{PROJECT_ID}.{DATASET_SILVER}.movements` WHERE source_id = @source_id AND ingest_date = @ingest_date)"
        elif source_id == "index_0500":
            silver_count_expr = f"(SELECT COUNT(*) FROM `{PROJECT_ID}.{DATASET_SILVER}.vehicles` WHERE source_id = @source_id AND ingest_date = @ingest_date)"

        if has_fail:
            final_status = "FAILED"
        elif has_warning:
            final_status = "WARNING"
        else:
            final_status = "SUCCESS"

        combined_error = "; ".join(anomaly_messages) if anomaly_messages else None

        log_run_sql = f"""
        INSERT INTO `{PROJECT_ID}.{DATASET_OPS}.pipeline_runs` (
            run_id, pipeline_name, ingest_date, started_at, completed_at, status,
            total_bronze_rows, total_silver_rows, total_gold_rows, quarantined_rows, error_message
        ) VALUES (
            @run_id,
            CONCAT('eventarc_autonomous_', @source_id),
            @ingest_date,
            @started_at,
            CURRENT_TIMESTAMP(),
            @status,
            (SELECT COUNT(*) FROM `{PROJECT_ID}.{DATASET_BRONZE}.raw_{source_id}` WHERE ingest_date = @ingest_date),
            {silver_count_expr},
            (SELECT COUNT(*) FROM `{PROJECT_ID}.{DATASET_GOLD}.person_profiles_master` WHERE ingest_date = @ingest_date AND @source_id IN UNNEST(source_ids)),
            @quarantined_rows,
            @error_message
        );
        """
        log_job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("run_id", "STRING", run_id),
                bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
                bigquery.ScalarQueryParameter("ingest_date", "DATE", ingest_date),
                bigquery.ScalarQueryParameter("started_at", "TIMESTAMP", started_at),
                bigquery.ScalarQueryParameter("status", "STRING", final_status),
                bigquery.ScalarQueryParameter("quarantined_rows", "INT64", quarantined_rows),
                bigquery.ScalarQueryParameter("error_message", "STRING", combined_error),
            ]
        )
        bq_client.query(log_run_sql, job_config=log_job_config).result()

        logger.info(f"[PIPELINE] Complete Medallion cycle for {source_id} finished with status={final_status} (run_id: {run_id}).")
        return {"status": final_status, "pipeline_type": pipeline_type, "run_id": run_id, "anomalies": anomaly_messages}

    except Exception as exc:
        err_msg = f"Pipeline execution failed for source={source_id} file={file_name}: {exc}"
        logger.error(f"[ERROR] [source={source_id} file={file_name} run_id={run_id}] {err_msg}")
        try:
            fail_sql = f"""
            INSERT INTO `{PROJECT_ID}.{DATASET_OPS}.pipeline_runs` (
                run_id, pipeline_name, ingest_date, started_at, completed_at, status,
                total_bronze_rows, total_silver_rows, total_gold_rows, error_message
            ) VALUES (
                @run_id,
                CONCAT('eventarc_autonomous_', @source_id),
                @ingest_date,
                @started_at,
                CURRENT_TIMESTAMP(),
                'FAILED',
                (SELECT COUNT(*) FROM `{PROJECT_ID}.{DATASET_BRONZE}.raw_{source_id}` WHERE ingest_date = @ingest_date),
                0,
                0,
                @error_message
            );
            """
            bq_client.query(
                fail_sql,
                job_config=bigquery.QueryJobConfig(
                    query_parameters=[
                        bigquery.ScalarQueryParameter("run_id", "STRING", run_id),
                        bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
                        bigquery.ScalarQueryParameter("ingest_date", "DATE", ingest_date),
                        bigquery.ScalarQueryParameter("started_at", "TIMESTAMP", started_at),
                        bigquery.ScalarQueryParameter("error_message", "STRING", str(exc)),
                    ]
                )
            ).result()
        except Exception as log_err:
            logger.warning(f"Failed to record FAILED run in pipeline_runs: {log_err}")
        raise exc


def update_manifest_status(
    bq_client: bigquery.Client,
    file_path: str,
    status: str,
    record_count: int,
    error_message: Optional[str] = None
):
    manifest_table = f"`{PROJECT_ID}.{DATASET_OPS}.ingestion_manifest`"
    sql = f"""
    UPDATE {manifest_table}
    SET
        status = @status,
        record_count = @record_count,
        error_message = @error_message,
        last_reupload_timestamp = CURRENT_TIMESTAMP()
    WHERE file_path = @file_path
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("status", "STRING", status),
            bigquery.ScalarQueryParameter("record_count", "INT64", record_count),
            bigquery.ScalarQueryParameter("error_message", "STRING", error_message or ""),
            bigquery.ScalarQueryParameter("file_path", "STRING", file_path),
        ]
    )
    bq_client.query(sql, job_config=job_config).result()


@functions_framework.cloud_event
def on_gcs_object_finalized(cloud_event: CloudEvent) -> Dict[str, Any]:
    """
    Eventarc entrypoint for GCS Object Finalized events.
    Triggered when any investigator or automated crawler drops a file into:
    gs://<bucket>/raw/<source_id>/<filename>.csv

    Executes:
    1. Path validation & parsing
    2. Idempotent re-upload verification via ops_monitoring.ingestion_manifest
    3. Old record purging (if re-upload)
    4. Bronze ingestion & metadata column augmentation
    5. Silver entity extraction (dynamic YAML or Dataform staging)
    6. Gold identity resolution & graph build
    7. Automated quality & discrepancy auditing
    """
    data = cloud_event.data
    bucket = data.get("bucket")
    name = data.get("name")
    size = data.get("size")
    md5_hash = data.get("md5Hash")

    if not bucket or not name:
        logger.warning(f"Ignored invalid CloudEvent missing bucket or name: {data}")
        return {"status": "SKIPPED", "reason": "missing_bucket_or_name"}

    gcs_uri = f"gs://{bucket}/{name}"
    logger.info(f"Incoming GCS event: {gcs_uri} (size: {size} bytes)")

    # 1. Filter only files under raw/
    parsed = parse_gcs_path(name)
    if not parsed:
        logger.info(f"Ignored non-raw file path: {name}")
        return {"status": "SKIPPED", "reason": "not_in_raw_folder"}

    source_id, file_name = parsed
    target_table_id = f"{PROJECT_ID}.{DATASET_BRONZE}.raw_{source_id}"

    bq_client = get_bigquery_client()

    try:
        # 2. Check & Update Idempotent Manifest
        ingest_date, ingest_ts, is_reupload, reupload_count = check_and_update_manifest(
            bq_client=bq_client,
            file_path=gcs_uri,
            file_name=file_name,
            source_id=source_id,
            file_hash=md5_hash
        )

        # 3. If re-upload: purge previous records for this file to ensure zero duplicates
        if is_reupload:
            purge_old_file_records(bq_client, target_table_id, file_name, ingest_date)

        # 4. Ingest records into Bronze table and augment metadata
        row_count = load_file_into_bronze(
            bq_client=bq_client,
            gcs_uri=gcs_uri,
            source_id=source_id,
            file_name=file_name,
            ingest_date=ingest_date,
            ingest_timestamp=ingest_ts
        )

        # 5. Trigger Autonomous Downstream Medallion Pipeline (Silver -> Gold -> Quality Audit)
        downstream_result = trigger_downstream_pipeline(
            bq_client=bq_client,
            source_id=source_id,
            ingest_date=ingest_date,
            started_at=ingest_ts,
            file_name=file_name
        )

        # 6. Finalize manifest status
        update_manifest_status(
            bq_client=bq_client,
            file_path=gcs_uri,
            status="COMPLETED",
            record_count=row_count
        )

        response = {
            "status": "SUCCESS",
            "gcs_uri": gcs_uri,
            "source_id": source_id,
            "target_table": target_table_id,
            "ingest_date": str(ingest_date),
            "ingest_timestamp": ingest_ts.isoformat(),
            "is_reupload": is_reupload,
            "reupload_count": reupload_count,
            "rows_loaded": row_count,
            "downstream": downstream_result
        }
        logger.info(f"End-to-end ingestion pipeline completed successfully: {json.dumps(response)}")
        return response

    except Exception as exc:
        logger.exception(f"Ingestion failed for {gcs_uri}: {str(exc)}")
        update_manifest_status(
            bq_client=bq_client,
            file_path=gcs_uri,
            status="FAILED",
            record_count=0,
            error_message=str(exc)
        )
        raise exc
