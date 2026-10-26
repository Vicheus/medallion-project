#!/usr/bin/env bash
# =============================================================================
# deploy_function.sh
# Deploys Eventarc-triggered Cloud Run Function for autonomous Bronze ingestion.
# =============================================================================

set -euo pipefail

PROJECT_ID="${PROJECT_ID:-medallion-project-512608}"
REGION="${REGION:-europe-west1}"
BUCKET_NAME="${BUCKET_NAME:-medallion-project-512608-raw-data}"
FUNCTION_NAME="gcs-bronze-ingest-trigger"
SERVICE_ACCOUNT="medallion-pipeline@${PROJECT_ID}.iam.gserviceaccount.com"

echo "==============================================================================="
echo " Deploying Cloud Run Function: ${FUNCTION_NAME}"
echo " Project:         ${PROJECT_ID}"
echo " Region:          ${REGION}"
echo " Bucket Trigger:  gs://${BUCKET_NAME}"
echo " Service Account: ${SERVICE_ACCOUNT}"
echo "==============================================================================="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 1. Enable required APIs
echo "[1/4] Enabling required GCP APIs..."
gcloud services enable \
  eventarc.googleapis.com \
  run.googleapis.com \
  cloudfunctions.googleapis.com \
  cloudbuild.googleapis.com \
  storage.googleapis.com \
  bigquery.googleapis.com \
  --project="${PROJECT_ID}"

# 2. Grant GCS Service Agent pubsub.publisher role (required for GCS Eventarc triggers)
echo "[2/4] Configuring GCS Service Agent IAM permissions..."
GCS_SERVICE_ACCOUNT="$(gcloud storage service-agent --project="${PROJECT_ID}" 2>/dev/null | tr -d '[:space:]' || true)"
if [ -n "${GCS_SERVICE_ACCOUNT}" ]; then
  echo "  Granting pubsub.publisher to ${GCS_SERVICE_ACCOUNT}..."
  gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
    --member="serviceAccount:${GCS_SERVICE_ACCOUNT}" \
    --role="roles/pubsub.publisher" &>/dev/null || true
fi

# 3. Ensure Service Account exists and grant permissions
echo "[3/4] Ensuring pipeline Service Account permissions..."
if ! gcloud iam service-accounts describe "${SERVICE_ACCOUNT}" --project="${PROJECT_ID}" &>/dev/null; then
  echo "  Creating service account ${SERVICE_ACCOUNT}..."
  gcloud iam service-accounts create medallion-pipeline \
    --display-name="Medallion Pipeline Service Account" \
    --project="${PROJECT_ID}"
fi

PROJECT_NUMBER="$(gcloud projects describe "${PROJECT_ID}" --format='value(projectNumber)')"
COMPUTE_SA="${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"
echo "  Granting cloudbuild.builds.builder to compute SA ${COMPUTE_SA}..."
gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member="serviceAccount:${COMPUTE_SA}" \
  --role="roles/cloudbuild.builds.builder" &>/dev/null || true

gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member="serviceAccount:${SERVICE_ACCOUNT}" \
  --role="roles/bigquery.admin" &>/dev/null || true

gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member="serviceAccount:${SERVICE_ACCOUNT}" \
  --role="roles/storage.objectViewer" &>/dev/null || true

gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member="serviceAccount:${SERVICE_ACCOUNT}" \
  --role="roles/eventarc.eventReceiver" &>/dev/null || true

gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
  --member="serviceAccount:${SERVICE_ACCOUNT}" \
  --role="roles/run.invoker" &>/dev/null || true

# 4. Deploy 2nd Gen Cloud Function with Eventarc GCS Trigger
echo "[4/4] Deploying 2nd-gen Cloud Run Function with Eventarc trigger..."
gcloud functions deploy "${FUNCTION_NAME}" \
  --gen2 \
  --runtime="python311" \
  --region="${REGION}" \
  --source="${SCRIPT_DIR}" \
  --entry-point="on_gcs_object_finalized" \
  --trigger-event-filters="type=google.cloud.storage.object.v1.finalized" \
  --trigger-event-filters="bucket=${BUCKET_NAME}" \
  --service-account="${SERVICE_ACCOUNT}" \
  --set-env-vars="PROJECT_ID=${PROJECT_ID},LOCATION=${REGION}" \
  --memory="512Mi" \
  --timeout="300s" \
  --min-instances=0 \
  --max-instances=10 \
  --quiet \
  --project="${PROJECT_ID}"

echo ""
echo "==============================================================================="
echo " Cloud Run Function deployed successfully!"
echo " Trigger: Any file dropped into gs://${BUCKET_NAME}/raw/index_XXXX/*"
echo " Target:  Automatically loaded into BigQuery bronze.raw_index_XXXX"
echo "==============================================================================="
