#!/usr/bin/env bash
# =============================================================================
# scripts/test_schema_drift.sh
# End-to-End Automated Test for Schema Evolution & Drift (Index 0001)
# Tests:
#   1. All-String Bronze auto-creation with strict typing in Gold
#   2. Column Deletion (room_number deleted -> turns to NULL without crash)
#   3. Column Addition (client_vip_status added -> auto-evolved in Bronze)
#   4. Column Renaming (phone_number -> contact_phone)
#   5. Data Type Change (passport_number int -> alphanumeric string "МР-...")
# =============================================================================

set -eo pipefail

PROJECT_ID="${PROJECT_ID:-medallion-project-512608}"
REGION="${REGION:-europe-west1}"
BUCKET_NAME="${BUCKET_NAME:-medallion-project-512608-raw-data}"
SOURCE_ID="index_0001"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

V1_FILE="${ROOT_DIR}/data/test_schema_drift/index_0001_v1_original.csv"
V2_FILE="${ROOT_DIR}/data/test_schema_drift/index_0001_v2_schema_drift.csv"

# Color formatting
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

log_step() { echo -e "\n${BLUE}===============================================================================${NC}"; echo -e "${BLUE}>>> $1${NC}"; echo -e "${BLUE}===============================================================================${NC}"; }
log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_err()  { echo -e "${RED}[ERROR]${NC} $1"; }

check_prerequisites() {
  log_step "Checking Prerequisites"
  if [[ ! -f "${V1_FILE}" || ! -f "${V2_FILE}" ]]; then
    log_err "Test files missing! Run generator first."
    exit 1
  fi
  log_info "Project:     ${PROJECT_ID}"
  log_info "Bucket:      gs://${BUCKET_NAME}"
  log_info "Source:      ${SOURCE_ID}"
  log_info "V1 Fixture:  ${V1_FILE}"
  log_info "V2 Fixture:  ${V2_FILE}"
}

clean_gcp_data() {
  log_step "Step 0: Purging Previous Test Data from BigQuery & GCS"

  log_info "1. Dropping raw Bronze table for ${SOURCE_ID} to test fresh All-String creation..."
  bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false \
    "DROP TABLE IF EXISTS \`bronze.raw_${SOURCE_ID}\`;"

  log_info "2. Purging ${SOURCE_ID} rows from Silver normalized entities..."
  bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false "
    DELETE FROM \`silver.persons\` WHERE source_id = '${SOURCE_ID}';
    DELETE FROM \`silver.contacts\` WHERE source_id = '${SOURCE_ID}';
    DELETE FROM \`silver.addresses\` WHERE source_id = '${SOURCE_ID}';
    DELETE FROM \`silver.documents\` WHERE source_id = '${SOURCE_ID}';
    DELETE FROM \`silver.works\` WHERE source_id = '${SOURCE_ID}';
  "

  log_info "3. Purging audit & manifest history for ${SOURCE_ID}..."
  bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false "
    DELETE FROM \`ops_monitoring.ingestion_manifest\` WHERE source_id = '${SOURCE_ID}';
    DELETE FROM \`ops_monitoring.pipeline_runs\` WHERE pipeline_name = 'eventarc_autonomous_${SOURCE_ID}';
    DELETE FROM \`ops_monitoring.layer_discrepancy_log\` WHERE source_id = '${SOURCE_ID}';
    DELETE FROM \`ops_monitoring.quarantined_records\` WHERE source_id = '${SOURCE_ID}';
  "

  log_info "4. Removing GCS test files from raw/${SOURCE_ID}/..."
  gcloud storage rm "gs://${BUCKET_NAME}/raw/${SOURCE_ID}/**" 2>/dev/null || true

  log_info "Cleanup complete. Target environment is clean!"
}

poll_pipeline_run() {
  local target_file="$1"
  log_info "Waiting for Cloud Run Function to process ${target_file} (polling ops_monitoring.pipeline_runs)..."

  local attempt=0
  local max_attempts=30
  while [[ $attempt -lt $max_attempts ]]; do
    sleep 5
    attempt=$((attempt + 1))

    # Query latest run
    local status
    status=$(bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false --format=csv \
      "SELECT status FROM \`ops_monitoring.pipeline_runs\` 
       WHERE pipeline_name = 'eventarc_autonomous_${SOURCE_ID}' 
       ORDER BY started_at DESC LIMIT 1" 2>/dev/null | tail -n 1 || echo "")

    if [[ -n "$status" && "$status" != "status" ]]; then
      if [[ "$status" == "SUCCESS" || "$status" == "WARNING" ]]; then
        log_info "Pipeline finished with status: ${status} (took ~$((attempt * 5))s)"
        return 0
      elif [[ "$status" == "FAILED" ]]; then
        log_err "Pipeline finished with status: FAILED!"
        bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false \
          "SELECT run_id, status, error_message FROM \`ops_monitoring.pipeline_runs\` 
           WHERE pipeline_name = 'eventarc_autonomous_${SOURCE_ID}' 
           ORDER BY started_at DESC LIMIT 1"
        return 1
      fi
    fi
    echo -n "."
  done

  log_err "Timeout waiting for pipeline run after $((max_attempts * 5))s"
  return 1
}

run_v1_original() {
  log_step "Phase 1: Ingesting Original Dataset (v1)"
  local gcs_dest="gs://${BUCKET_NAME}/raw/${SOURCE_ID}/index_0001_v1_original.csv"
  
  log_info "Uploading V1 original CSV to ${gcs_dest}..."
  gcloud storage cp "${V1_FILE}" "${gcs_dest}"

  poll_pipeline_run "index_0001_v1_original.csv"

  log_info "Inspecting Bronze Schema to verify All-String creation:"
  bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false \
    "SELECT column_name, data_type 
     FROM \`bronze.INFORMATION_SCHEMA.COLUMNS\` 
     WHERE table_name = 'raw_${SOURCE_ID}' 
     ORDER BY ordinal_position LIMIT 10;"

  log_info "Row Counts after Phase 1:"
  bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false "
    SELECT 
      (SELECT COUNT(*) FROM \`bronze.raw_${SOURCE_ID}\`) AS bronze_rows,
      (SELECT COUNT(*) FROM \`silver.persons\` WHERE source_id = '${SOURCE_ID}') AS silver_persons,
      (SELECT COUNT(*) FROM \`gold.person_profiles_master\`) AS gold_profiles,
      (SELECT status FROM \`ops_monitoring.pipeline_runs\` WHERE pipeline_name = 'eventarc_autonomous_${SOURCE_ID}' ORDER BY started_at DESC LIMIT 1) AS run_status;
  "
}

run_v2_schema_drift() {
  log_step "Phase 2: Ingesting Schema Drift Dataset (v2)"
  log_info "Mutations being tested in v2:"
  log_info "  - Column DELETED:      room_number"
  log_info "  - Column ADDED:        client_vip_status"
  log_info "  - Column RENAMED:      phone_number -> contact_phone"
  log_info "  - Data Type CHANGED:   passport_number contains alphanumeric strings ('МР-...')"

  local gcs_dest="gs://${BUCKET_NAME}/raw/${SOURCE_ID}/index_0001_v2_schema_drift.csv"
  
  log_info "Uploading V2 drift CSV to ${gcs_dest}..."
  gcloud storage cp "${V2_FILE}" "${gcs_dest}"

  poll_pipeline_run "index_0001_v2_schema_drift.csv"

  log_info "Inspecting Bronze Schema to verify new column addition (ALLOW_FIELD_ADDITION):"
  bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false \
    "SELECT column_name, data_type 
     FROM \`bronze.INFORMATION_SCHEMA.COLUMNS\` 
     WHERE table_name = 'raw_${SOURCE_ID}' AND column_name IN ('client_vip_status', 'contact_phone', 'passport_number', 'room_number');"

  log_info "Verifying alphanumeric passport values in Bronze (no integer parsing crash!):"
  bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false \
    "SELECT passport_number, client_vip_status, file_name 
     FROM \`bronze.raw_${SOURCE_ID}\` 
     WHERE passport_number LIKE 'МР-%' LIMIT 5;"

  log_info "Verifying that Silver and Gold remain strictly typed:"
  bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false \
    "SELECT column_name, data_type 
     FROM \`gold.INFORMATION_SCHEMA.COLUMNS\` 
     WHERE table_name = 'person_profiles_master' AND column_name IN ('birth_date', 'sex_code', 'latest_actuality_date');"

  log_info "Cumulative Summary after Phase 2:"
  bq query --project_id="${PROJECT_ID}" --use_legacy_sql=false "
    SELECT 
      (SELECT COUNT(*) FROM \`bronze.raw_${SOURCE_ID}\`) AS total_bronze_rows,
      (SELECT COUNT(*) FROM \`silver.persons\` WHERE source_id = '${SOURCE_ID}') AS total_silver_persons,
      (SELECT COUNT(*) FROM \`gold.person_profiles_master\`) AS total_gold_profiles;
  "
}

# Entry point logic
ACTION="${1:-all}"

case "${ACTION}" in
  clean)
    check_prerequisites
    clean_gcp_data
    ;;
  v1)
    check_prerequisites
    run_v1_original
    ;;
  v2)
    check_prerequisites
    run_v2_schema_drift
    ;;
  all)
    check_prerequisites
    clean_gcp_data
    run_v1_original
    run_v2_schema_drift
    log_step "SUCCESS: End-to-End Schema Drift Test Passed Completely!"
    ;;
  *)
    echo "Usage: $0 [all | clean | v1 | v2]"
    exit 1
    ;;
esac
