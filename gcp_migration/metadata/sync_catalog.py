#!/usr/bin/env python3
"""
sync_catalog.py
Synchronizes YAML source configurations from gcp_migration/metadata/sources/
into BigQuery ops_monitoring.source_catalog.
"""

import os
import sys
import json
import glob
from pathlib import Path
import yaml
from google.cloud import bigquery

PROJECT_ID = os.environ.get("PROJECT_ID", "medallion-project-512608")
LOCATION = os.environ.get("LOCATION", "europe-west1")
DATASET_OPS = "ops_monitoring"
CATALOG_TABLE = "source_catalog"
SLA_TABLE = "source_sla_config"

DDL_CREATE_CATALOG = f"""
CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET_OPS}.{CATALOG_TABLE}` (
  source_id STRING NOT NULL OPTIONS(description="Unique source index identifier (e.g. index_0001)"),
  source_name STRING NOT NULL OPTIONS(description="Human-readable dataset label"),
  pipeline_type STRING NOT NULL OPTIONS(description="'METADATA_DRIVEN' or 'DATAFORM_DAG'"),
  raw_table_name STRING NOT NULL OPTIONS(description="Corresponding table in bronze dataset"),
  is_active BOOLEAN DEFAULT TRUE OPTIONS(description="Active ingestion status"),
  description STRING,
  mapping_spec JSON OPTIONS(description="Compiled JSON representation of YAML column mapping and rules"),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
CLUSTER BY pipeline_type, source_id
OPTIONS(
  description="Central Medallion Source Catalog distinguishing Tier-1 Standard Metadata sources from Complex Dataform DAG sources."
);
"""

DDL_CREATE_SLA = f"""
CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET_OPS}.{SLA_TABLE}` (
  source_id STRING NOT NULL,
  max_staleness_hours INT64 NOT NULL,
  min_expected_rows INT64 NOT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
OPTIONS(
  description="Source SLA Freshness Configuration dynamically managed from YAML catalog"
);
"""

MERGE_SQL = f"""
MERGE `{PROJECT_ID}.{DATASET_OPS}.{CATALOG_TABLE}` T
USING (
  SELECT
    @source_id AS source_id,
    @source_name AS source_name,
    @pipeline_type AS pipeline_type,
    @raw_table_name AS raw_table_name,
    @is_active AS is_active,
    @description AS description,
    PARSE_JSON(@mapping_spec_json) AS mapping_spec
) S
ON T.source_id = S.source_id
WHEN MATCHED THEN
  UPDATE SET
    source_name = S.source_name,
    pipeline_type = S.pipeline_type,
    raw_table_name = S.raw_table_name,
    is_active = S.is_active,
    description = S.description,
    mapping_spec = S.mapping_spec,
    updated_at = CURRENT_TIMESTAMP()
WHEN NOT MATCHED THEN
  INSERT (
    source_id, source_name, pipeline_type, raw_table_name,
    is_active, description, mapping_spec, created_at, updated_at
  )
  VALUES (
    S.source_id, S.source_name, S.pipeline_type, S.raw_table_name,
    S.is_active, S.description, S.mapping_spec, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()
  );
"""

MERGE_SLA_SQL = f"""
MERGE `{PROJECT_ID}.{DATASET_OPS}.{SLA_TABLE}` T
USING (
  SELECT
    @source_id AS source_id,
    @max_staleness_hours AS max_staleness_hours,
    @min_expected_rows AS min_expected_rows,
    @is_active AS is_active
) S
ON T.source_id = S.source_id
WHEN MATCHED THEN
  UPDATE SET
    max_staleness_hours = S.max_staleness_hours,
    min_expected_rows = S.min_expected_rows,
    is_active = S.is_active,
    updated_at = CURRENT_TIMESTAMP()
WHEN NOT MATCHED THEN
  INSERT (source_id, max_staleness_hours, min_expected_rows, is_active, updated_at)
  VALUES (S.source_id, S.max_staleness_hours, S.min_expected_rows, S.is_active, CURRENT_TIMESTAMP());
"""


def sync_sources():
    sources_dir = Path(__file__).resolve().parent / "sources"
    yaml_files = sorted(list(sources_dir.glob("*.yaml")) + list(sources_dir.glob("*.yml")))

    if not yaml_files:
        print(f"No source YAML files found in {sources_dir}")
        sys.exit(1)

    print(f"Connecting to BigQuery project={PROJECT_ID}, location={LOCATION}...")
    client = bigquery.Client(project=PROJECT_ID, location=LOCATION)

    print(f"Ensuring {PROJECT_ID}.{DATASET_OPS}.{CATALOG_TABLE} & {SLA_TABLE} exist...")
    client.query(DDL_CREATE_CATALOG).result()
    client.query(DDL_CREATE_SLA).result()

    synced_count = 0
    print(f"Found {len(yaml_files)} source specification files. Syncing to catalog & SLA config...")

    for yf in yaml_files:
        with open(yf, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        source_id = data.get("source_id")
        source_name = data.get("name", source_id)
        pipeline_type = data.get("pipeline_type", "METADATA_DRIVEN")
        description = data.get("description", "")
        raw_table_name = f"raw_{source_id}"

        if not source_id:
            print(f"Skipping {yf.name}: missing 'source_id'")
            continue

        spec_json = json.dumps(data, ensure_ascii=False)

        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
                bigquery.ScalarQueryParameter("source_name", "STRING", source_name),
                bigquery.ScalarQueryParameter("pipeline_type", "STRING", pipeline_type),
                bigquery.ScalarQueryParameter("raw_table_name", "STRING", raw_table_name),
                bigquery.ScalarQueryParameter("is_active", "BOOL", True),
                bigquery.ScalarQueryParameter("description", "STRING", description),
                bigquery.ScalarQueryParameter("mapping_spec_json", "STRING", spec_json),
            ]
        )

        client.query(MERGE_SQL, job_config=job_config).result()

        # Sync SLA configuration (custom or default 24h / 50 rows)
        sla_cfg = data.get("sla", {})
        max_staleness = sla_cfg.get("max_staleness_hours", 24)
        min_rows = sla_cfg.get("min_expected_rows", 50)

        sla_job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("source_id", "STRING", source_id),
                bigquery.ScalarQueryParameter("max_staleness_hours", "INT64", max_staleness),
                bigquery.ScalarQueryParameter("min_expected_rows", "INT64", min_rows),
                bigquery.ScalarQueryParameter("is_active", "BOOL", True),
            ]
        )
        client.query(MERGE_SLA_SQL, job_config=sla_job_config).result()

        print(f"  [OK] Synced {source_id} ({pipeline_type}): {source_name} [SLA: max {max_staleness}h, min {min_rows} rows]")
        synced_count += 1

    print(f"\nSuccessfully synchronized {synced_count} sources to {DATASET_OPS}.{CATALOG_TABLE}.")

    print("Refreshing bronze.raw_records_unified view...")
    try:
        client.query(f"CALL `{PROJECT_ID}.bronze.sp_refresh_raw_records_unified`()").result()
        print("  [OK] Unified raw records view updated.")
    except Exception as exc:
        print(f"  [WARN] Could not refresh unified view: {exc}")

    sync_dataform_workspace()


def sync_dataform_workspace():
    """
    Synchronizes local/repo Dataform files (SQLX, settings) into Cloud Dataform prod-workspace.
    Ensures Cloud Dataform always has the latest DAG definitions without manual git linking.
    """
    dataform_dir = Path(__file__).resolve().parent.parent / "dataform"
    if not dataform_dir.exists():
        return

    print("Checking Cloud Dataform workspace synchronization...")
    try:
        from google.cloud import dataform_v1
        client = dataform_v1.DataformClient()
        repo_path = client.repository_path(PROJECT_ID, LOCATION, "medallion-complex-pipelines")
        ws_name = f"{repo_path}/workspaces/prod-workspace"

        try:
            client.get_workspace(name=ws_name)
        except Exception:
            client.create_workspace(parent=repo_path, workspace_id="prod-workspace")
            print("  [OK] Created Cloud Dataform workspace 'prod-workspace'.")

        synced_files = 0
        for fpath in dataform_dir.rglob("*"):
            if fpath.is_file() and not fpath.name.startswith("."):
                rel_path = str(fpath.relative_to(dataform_dir))
                content = fpath.read_bytes()
                req = dataform_v1.WriteFileRequest(workspace=ws_name, path=rel_path, contents=content)
                client.write_file(request=req)
                synced_files += 1

        print(f"  [OK] Successfully synchronized {synced_files} Dataform definitions to Cloud Dataform workspace.")
    except Exception as exc:
        print(f"  [WARN] Cloud Dataform workspace sync note: {exc}")


if __name__ == "__main__":
    sync_sources()
