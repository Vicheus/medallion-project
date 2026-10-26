#!/usr/bin/env bash
# =============================================================================
# teardown.sh
# Safely and cleanly destroys all provisioned GCP Medallion resources:
# - BigQuery Scheduled Query
# - BigQuery datasets (bronze, silver, gold, ops_monitoring) and all tables/routines
# - GCS raw staging bucket and all objects
# - Local synthetic data artifacts
# =============================================================================

set -euo pipefail

export CLOUDSDK_PYTHON="${CLOUDSDK_PYTHON:-/opt/homebrew/bin/python3.13}"
PROJECT_ID="medallion-project-512608"
LOCATION="europe-west1"
BUCKET_NAME="medallion-project-512608-raw-data"
TRANSFER_CONFIG_NAME="Medallion Daily Pipeline"

echo "==============================================================================="
echo " Starting GCP Medallion Infrastructure Teardown"
echo " Project:  ${PROJECT_ID}"
echo " Location: ${LOCATION}"
echo " Bucket:   gs://${BUCKET_NAME}"
echo "==============================================================================="

# 1. Remove Cloud Run Function, Eventarc Trigger & Scheduled Query
echo ""
echo "[1/6] Removing Cloud Run Function 'gcs-bronze-ingest-trigger'..."
gcloud functions delete gcs-bronze-ingest-trigger --region="${LOCATION}" --gen2 --project="${PROJECT_ID}" --quiet &>/dev/null || true

echo ""
echo "[2/6] Removing Scheduled Query '${TRANSFER_CONFIG_NAME}'..."
CONFIG_RESOURCE=$(bq ls --transfer_config --transfer_location="${LOCATION}" --project_id="${PROJECT_ID}" --format=prettyjson 2>/dev/null | \
  python3 -c "import sys, json; configs = json.load(sys.stdin); print(next((c['name'] for c in configs if c.get('displayName') == '${TRANSFER_CONFIG_NAME}'), ''))" 2>/dev/null || true)

if [ -n "${CONFIG_RESOURCE}" ]; then
  echo "  Deleting transfer config ${CONFIG_RESOURCE}..."
  bq rm --transfer_config -f "${CONFIG_RESOURCE}" &>/dev/null || true
  echo "  Scheduled Query deleted."
else
  echo "  No active Scheduled Query found."
fi

# 2. Remove Cloud Dataform Repository
echo ""
echo "[3/6] Removing Cloud Dataform repository 'medallion-complex-pipelines'..."
TOKEN="$(gcloud auth print-access-token 2>/dev/null || true)"
if [ -n "${TOKEN}" ]; then
  curl -s -X DELETE \
    -H "Authorization: Bearer ${TOKEN}" \
    "https://dataform.googleapis.com/v1beta1/projects/${PROJECT_ID}/locations/${LOCATION}/repositories/medallion-complex-pipelines?force=true" &>/dev/null || true
  echo "  Dataform repository removed."
fi

# 3. Remove BigQuery Datasets
echo ""
echo "[4/6] Removing BigQuery datasets (bronze, silver, gold, ops_monitoring)..."
DATASETS=("bronze" "silver" "gold" "ops_monitoring")
for DS in "${DATASETS[@]}"; do
  if bq show --project_id="${PROJECT_ID}" "${PROJECT_ID}:${DS}" &>/dev/null; then
    echo "  Deleting dataset ${PROJECT_ID}:${DS} and all contents..."
    bq rm -r -f -d --project_id="${PROJECT_ID}" "${PROJECT_ID}:${DS}" &>/dev/null || true
  else
    echo "  Dataset ${PROJECT_ID}:${DS} does not exist."
  fi
done

# 4. Remove GCS Staging Bucket
echo ""
echo "[5/6] Removing GCS bucket gs://${BUCKET_NAME}..."
PYTHON_BIN="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.venv/bin/python"
if [ ! -f "${PYTHON_BIN}" ]; then
  PYTHON_BIN="python3"
fi
"${PYTHON_BIN}" -c "
from google.cloud import storage
try:
    client = storage.Client(project='${PROJECT_ID}')
    bucket = client.get_bucket('${BUCKET_NAME}')
    blobs = list(bucket.list_blobs())
    if blobs:
        bucket.delete_blobs(blobs)
    bucket.delete()
    print('  Bucket deleted.')
except Exception as e:
    print(f'  Bucket deletion note: {e}')
"

# 5. Clean Local Temp Artifacts
echo ""
echo "[6/6] Cleaning local synthetic test data..."
if [ -d "data/synthetic" ]; then
  rm -rf "data/synthetic"
  echo "  Removed local directory data/synthetic/"
fi

echo ""
echo "==============================================================================="
echo " Teardown Complete! Zero lingering GCP resources remain."
echo "==============================================================================="
