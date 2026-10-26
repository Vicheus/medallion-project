#!/usr/bin/env bash
# =============================================================================
# run_pipeline.sh
# End-to-end execution of the GCP Medallion Pipeline:
# 1. Uploads synthetic CSVs to GCS (raw/{source_id}/ingest_date=YYYY-MM-DD/)
# 2. Loads raw data into BigQuery Bronze partitioned tables
# 3. Invokes master transformation routine (Bronze -> Silver -> Gold + Quality Checks)
# 4. Prints validation metrics, discrepancy reports, and sample resolved entities
# =============================================================================

set -euo pipefail

export CLOUDSDK_PYTHON="${CLOUDSDK_PYTHON:-/opt/homebrew/bin/python3.13}"
PROJECT_ID="medallion-project-512608"
LOCATION="europe-west1"
BUCKET_NAME="medallion-project-512608-raw-data"

MODE="sample"
INGEST_DATE="$(date +%Y-%m-%d)"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      MODE="$2"
      shift 2
      ;;
    --full)
      MODE="full"
      shift
      ;;
    --sample)
      MODE="sample"
      shift
      ;;
    --date)
      INGEST_DATE="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1"
      echo "Usage: ./run_pipeline.sh [--mode sample|full] [--date YYYY-MM-DD]"
      exit 1
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="${SCRIPT_DIR}/data/synthetic/${MODE}"

echo "==============================================================================="
echo " Executing GCP Medallion Pipeline"
echo " Project:       ${PROJECT_ID}"
echo " Mode:          ${MODE}"
echo " Ingest Date:   ${INGEST_DATE}"
echo " Staging Dir:   ${DATA_DIR}"
echo " GCS Target:    gs://${BUCKET_NAME}/raw/"
echo "==============================================================================="

# -----------------------------------------------------------------------------
# 1. Verify / Generate Synthetic Data
# -----------------------------------------------------------------------------
echo ""
echo "[1/4] Checking local synthetic data..."
if [ ! -d "${DATA_DIR}" ] || [ -z "$(ls -A "${DATA_DIR}"/*.csv 2>/dev/null)" ]; then
  echo "  No data found in ${DATA_DIR}. Generating synthetic data..."
  "${SCRIPT_DIR}/generate_data.sh" --mode "${MODE}" --date "${INGEST_DATE}"
else
  echo "  Found existing CSV data in ${DATA_DIR}."
fi

# -----------------------------------------------------------------------------
# 2. Upload Data to GCS Staging Bucket (Triggers Eventarc Cloud Run Function)
# -----------------------------------------------------------------------------
echo ""
echo "[2/4] Uploading raw data to Google Cloud Storage (gs://${BUCKET_NAME}/raw/)..."

PYTHON_BIN="${SCRIPT_DIR}/.venv/bin/python"
if [ ! -f "${PYTHON_BIN}" ]; then
  PYTHON_BIN="python3"
fi

upload_to_gcs() {
  local file_name="$1"
  local source_id="$2"
  local local_file="${DATA_DIR}/${file_name}"
  local gcs_dest="raw/${source_id}/${file_name}"

  if [ -f "${local_file}" ]; then
    echo "  Uploading ${file_name} -> gs://${BUCKET_NAME}/${gcs_dest}..."
    "${PYTHON_BIN}" -c "
import sys
from google.cloud import storage
try:
    client = storage.Client(project='${PROJECT_ID}')
    bucket = client.bucket('${BUCKET_NAME}')
    blob = bucket.blob('${gcs_dest}')
    blob.upload_from_filename('${local_file}')
except Exception as e:
    print(f'Error uploading ${local_file}: {e}', file=sys.stderr)
    sys.exit(1)
"
  else
    echo "  Warning: Local file ${local_file} not found, skipping."
  fi
}

upload_to_gcs "index_0001_zoloto585_crm.csv" "index_0001"
upload_to_gcs "index_0696_dozarplati_loans.csv" "index_0696"
upload_to_gcs "index_0800_duhirf_ecommerce.csv" "index_0800"
upload_to_gcs "index_0801_skb_techno_clients.csv" "index_0801"
upload_to_gcs "index_0020_sirena.csv" "index_0020"
upload_to_gcs "index_0500_vehicles.csv" "index_0500"
upload_to_gcs "index_0080_gaming_profiles.csv" "index_0080"
upload_to_gcs "index_0042_delivery_orders.csv" "index_0042"
echo "  All 8 source datasets uploaded to GCS (Eventarc triggers initiated)."

# -----------------------------------------------------------------------------
# 3. Synchronize Ingestion & Run Master Pipeline
# -----------------------------------------------------------------------------
echo ""
echo "[3/4] Executing Master Medallion Stored Procedure (ops_monitoring.sp_run_medallion_pipeline)..."
echo "  Waiting 5s for Eventarc processing to settle..."
sleep 5

bq query \
  --project_id="${PROJECT_ID}" \
  --location="${LOCATION}" \
  --use_legacy_sql=false \
  "CALL ops_monitoring.sp_run_medallion_pipeline();" &>/dev/null

echo "  Medallion pipeline executed successfully!"

# -----------------------------------------------------------------------------
# 5. Verification & Metrics Display
# -----------------------------------------------------------------------------
echo ""
echo "==============================================================================="
echo " PIPELINE RUN AUDIT SUMMARY"
echo "==============================================================================="
bq query \
  --project_id="${PROJECT_ID}" \
  --location="${LOCATION}" \
  --use_legacy_sql=false \
  --format=pretty \
  "SELECT run_id, pipeline_name, status, total_bronze_rows, total_silver_rows, total_gold_rows, completed_at
   FROM ops_monitoring.pipeline_runs
   ORDER BY started_at DESC LIMIT 1;"

echo ""
echo "==============================================================================="
echo " LAYER DISCREPANCY & RECONCILIATION CHECKS"
echo "==============================================================================="
bq query \
  --project_id="${PROJECT_ID}" \
  --location="${LOCATION}" \
  --use_legacy_sql=false \
  --format=pretty \
  "SELECT check_name, status, expected_count, actual_count, discrepancy_count, details
   FROM ops_monitoring.layer_discrepancy_log
   WHERE ingest_date = DATE('${INGEST_DATE}');"

echo ""
echo "==============================================================================="
echo " SAMPLE RESOLVED 360° PROFILE IN GOLD MASTER"
echo "==============================================================================="
bq query \
  --project_id="${PROJECT_ID}" \
  --location="${LOCATION}" \
  --use_legacy_sql=false \
  --format=pretty \
  "SELECT
     primary_full_name,
     primary_phone,
     primary_email,
     birth_date,
     ARRAY_LENGTH(phones) AS total_phones,
     ARRAY_LENGTH(documents) AS total_docs,
     ARRAY_LENGTH(vehicles) AS total_cars,
     ARRAY_LENGTH(source_ids) AS cross_source_count,
     source_ids
   FROM gold.person_profiles_master
   WHERE ARRAY_LENGTH(source_ids) > 1
   LIMIT 3;"

echo ""
echo "==============================================================================="
echo " Medallion Pipeline Execution Complete!"
echo "==============================================================================="
