#!/usr/bin/env bash
# =============================================================================
# deploy.sh
# Provisions GCP Infrastructure for Medallion Architecture:
# - GCS raw staging bucket with 7-day auto-delete lifecycle
# - BigQuery datasets: bronze, silver, gold, ops_monitoring (europe-west1)
# - Persistent UDFs, Bronze, Silver, Gold, and Monitoring Tables & Routines
# - Dataset-level IAM binding for ai-agent-reader on gold
# - Daily BigQuery Scheduled Query orchestration
# =============================================================================

set -euo pipefail

# Environment & Python setup
export CLOUDSDK_PYTHON="${CLOUDSDK_PYTHON:-/opt/homebrew/bin/python3.13}"
PROJECT_ID="medallion-project-512608"
LOCATION="europe-west1"
BUCKET_NAME="medallion-project-512608-raw-data"
SA_EMAIL="ai-agent-reader@${PROJECT_ID}.iam.gserviceaccount.com"

echo "==============================================================================="
echo " Starting GCP Medallion Infrastructure Deployment"
echo " Project:  ${PROJECT_ID}"
echo " Location: ${LOCATION}"
echo " Bucket:   gs://${BUCKET_NAME}"
echo " Consumer: ${SA_EMAIL}"
echo "==============================================================================="

# -----------------------------------------------------------------------------
# 1. GCS Bucket Provisioning
# -----------------------------------------------------------------------------
echo ""
echo "[1/5] Checking Google Cloud Storage bucket..."
if gcloud storage buckets describe "gs://${BUCKET_NAME}" --project="${PROJECT_ID}" &>/dev/null; then
  echo "  Bucket gs://${BUCKET_NAME} already exists."
else
  echo "  Creating bucket gs://${BUCKET_NAME} in ${LOCATION}..."
  gcloud storage buckets create "gs://${BUCKET_NAME}" \
    --project="${PROJECT_ID}" \
    --location="${LOCATION}" \
    --uniform-bucket-level-access
fi

# Configure 7-day auto-delete lifecycle rule to guarantee near-zero storage costs
LIFECYCLE_TMP=$(mktemp)
cat <<EOF > "${LIFECYCLE_TMP}"
{
  "rule": [
    {
      "action": {"type": "Delete"},
      "condition": {"age": 7}
    }
  ]
}
EOF
echo "  Applying 7-day auto-deletion lifecycle policy..."
gcloud storage buckets update "gs://${BUCKET_NAME}" --lifecycle-file="${LIFECYCLE_TMP}" &>/dev/null
rm -f "${LIFECYCLE_TMP}"
echo "  Bucket configured with 7-day lifecycle retention."

# -----------------------------------------------------------------------------
# 2. BigQuery Datasets Provisioning
# -----------------------------------------------------------------------------
echo ""
echo "[2/5] Provisioning BigQuery Datasets in ${LOCATION}..."

DATASETS=("bronze" "silver" "gold" "ops_monitoring")
DESCRIPTIONS=(
  "Bronze layer: raw ingested data from all sources partitioned by ingest date"
  "Silver layer: cleaned, validated and normalized entity tables and UDFs"
  "Gold layer: semantic LLM-ready identity profiles, fact tables, and metadata dictionary"
  "Operational monitoring: audit logs, discrepancy checks, and pipeline runs"
)

for i in "${!DATASETS[@]}"; do
  DS="${DATASETS[$i]}"
  DESC="${DESCRIPTIONS[$i]}"
  if bq show --project_id="${PROJECT_ID}" "${PROJECT_ID}:${DS}" &>/dev/null; then
    echo "  Dataset ${PROJECT_ID}:${DS} already exists."
  else
    echo "  Creating dataset ${PROJECT_ID}:${DS}..."
    bq mk --project_id="${PROJECT_ID}" \
      --location="${LOCATION}" \
      --dataset \
      --description="${DESC}" \
      --label="layer:${DS}" \
      --label="project:medallion" \
      "${PROJECT_ID}:${DS}"
  fi
done

# -----------------------------------------------------------------------------
# 3. Deploy SQL Assets (UDFs, Tables, Stored Procedures)
# -----------------------------------------------------------------------------
echo ""
echo "[3/5] Deploying SQL DDL, Persistent UDFs, and Stored Procedures..."

SQL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/gcp_migration/sql"

run_sql_file() {
  local file_name="$1"
  local file_path="${SQL_DIR}/${file_name}"
  echo "  Executing ${file_name}..."
  bq query \
    --project_id="${PROJECT_ID}" \
    --location="${LOCATION}" \
    --use_legacy_sql=false \
    < "${file_path}"
}

run_sql_file "01_schemas_and_udfs.sql"
run_sql_file "02_bronze_tables.sql"
run_sql_file "03_silver_tables_and_sp.sql"
run_sql_file "04_gold_tables_and_sp.sql"
run_sql_file "05_monitoring_and_audit.sql"
run_sql_file "06_dynamic_silver_engine.sql"
echo "  All SQL schemas, UDFs, and stored procedures deployed successfully."

# -----------------------------------------------------------------------------
# 4. Synchronize Source Metadata Catalog
# -----------------------------------------------------------------------------
echo ""
echo "[4/7] Synchronizing Source Metadata Catalog (ops_monitoring.source_catalog)..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${SCRIPT_DIR}/.venv/bin/python"
if [ ! -f "${PYTHON_BIN}" ]; then
  PYTHON_BIN="python3"
fi
"${PYTHON_BIN}" "${SCRIPT_DIR}/gcp_migration/metadata/sync_catalog.py"

# -----------------------------------------------------------------------------
# 5. Dataset IAM Permissions for ai-agent-reader
# -----------------------------------------------------------------------------
echo ""
echo "[5/7] Configuring Least-Privilege IAM on Gold Dataset for ${SA_EMAIL}..."

# Grant roles/bigquery.dataViewer strictly on the gold dataset
# (User already has roles/bigquery.jobUser at the project level to execute queries)
TEMP_POLICY=$(mktemp)
bq show --format=prettyjson "${PROJECT_ID}:gold" > "${TEMP_POLICY}"

# Check if access already exists in dataset policy
if grep -q "${SA_EMAIL}" "${TEMP_POLICY}"; then
  echo "  IAM binding on gold dataset already configured for ${SA_EMAIL}."
else
  echo "  Granting roles/bigquery.dataViewer on gold dataset..."
  # Add access block using Python helper
  python3 - <<PYEOF
import json

with open("${TEMP_POLICY}", "r") as f:
    data = json.load(f)

access_list = data.get("access", [])
new_entry = {
    "role": "READER",
    "userByEmail": "${SA_EMAIL}"
}
if not any(entry.get("userByEmail") == "${SA_EMAIL}" for entry in access_list):
    access_list.append(new_entry)
    data["access"] = access_list

with open("${TEMP_POLICY}", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
  bq update --project_id="${PROJECT_ID}" --source="${TEMP_POLICY}" "${PROJECT_ID}:gold" &>/dev/null
  echo "  Dataset IAM binding applied successfully."
fi
rm -f "${TEMP_POLICY}"

# -----------------------------------------------------------------------------
# 6. BigQuery Scheduled Query Provisioning
# -----------------------------------------------------------------------------
echo ""
echo "[6/7] Checking BigQuery Scheduled Query orchestration..."

TRANSFER_CONFIG_NAME="Medallion Daily Pipeline"
EXISTING_CONFIG=$(bq ls --transfer_config --transfer_location="${LOCATION}" --project_id="${PROJECT_ID}" --format=prettyjson 2>/dev/null | grep "${TRANSFER_CONFIG_NAME}" || true)

if [ -n "${EXISTING_CONFIG}" ]; then
  echo "  Scheduled Query '${TRANSFER_CONFIG_NAME}' already exists."
else
  echo "  Creating Scheduled Query '${TRANSFER_CONFIG_NAME}' (every 24 hours)..."
  bq mk \
    --transfer_config \
    --project_id="${PROJECT_ID}" \
    --transfer_location="${LOCATION}" \
    --target_dataset="ops_monitoring" \
    --display_name="${TRANSFER_CONFIG_NAME}" \
    --schedule="every 24 hours" \
    --data_source=scheduled_query \
    --params='{"query":"CALL ops_monitoring.sp_run_medallion_pipeline();"}' &>/dev/null || {
      echo "  Note: Scheduled Query creation skipped or requires manual transfer permissions."
    }
fi

# -----------------------------------------------------------------------------
# 7. Autonomous Serverless Ingestion Trigger
# -----------------------------------------------------------------------------
echo ""
echo "[7/7] Autonomous Ingestion Trigger (Eventarc + Cloud Run Functions):"
echo "  Deploying/Verifying gcs-bronze-ingest-trigger..."
bash "${SCRIPT_DIR}/gcp_migration/cloud_functions/gcs_ingest_trigger/deploy_function.sh"

echo ""
echo "==============================================================================="
echo " Infrastructure Deployment Complete!"
echo " - Datasets: bronze, silver, gold, ops_monitoring (europe-west1)"
echo " - Staging Bucket: gs://${BUCKET_NAME} (7-day lifecycle retention)"
echo " - Bronze Tables: Refactored to generic bronze.raw_index_XXXX format"
echo " - Catalog: ops_monitoring.source_catalog synced (8 sources active)"
echo " - Dynamic Engine: silver.sp_transform_metadata_source & silver.sp_transform_all_metadata_sources"
echo " - Manifest: ops_monitoring.ingestion_manifest (idempotent reload preservation)"
echo " - Eventarc Trigger: gcs_ingest_trigger deployed under Cloud Run Functions"
echo " - IAM: ${SA_EMAIL} granted dataViewer on gold only"
echo " - Next step: Run ./run_pipeline.sh to execute pipeline"
echo "==============================================================================="
