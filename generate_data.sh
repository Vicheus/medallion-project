#!/usr/bin/env bash
# =============================================================================
# generate_data.sh
# Generates realistic synthetic datasets for all 8 Medallion sources:
# - Mode 'sample' (~1,500 rows per source, ~6 MB total for fast testing)
# - Mode 'full' (~45,000 rows per source, ~100-300 MB total for scale validation)
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR_SCRIPT="${SCRIPT_DIR}/gcp_migration/generator/generate_synthetic_data.py"

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
      echo "Usage: ./generate_data.sh [--mode sample|full] [--date YYYY-MM-DD]"
      exit 1
      ;;
  esac
done

echo "==============================================================================="
echo " Generating Synthetic Data for GCP Medallion Pipeline"
echo " Mode:            ${MODE}"
echo " Ingestion Date:  ${INGEST_DATE}"
echo " Generator:       ${GENERATOR_SCRIPT}"
echo "==============================================================================="

PYTHON_BIN="${SCRIPT_DIR}/.venv/bin/python"
if [ ! -f "${PYTHON_BIN}" ]; then
  PYTHON_BIN="python3"
fi

"${PYTHON_BIN}" "${GENERATOR_SCRIPT}" --mode "${MODE}" --date "${INGEST_DATE}"

echo ""
echo "Data generation complete. Output located in: data/synthetic/${MODE}/"
