#!/usr/bin/env python3
"""
validate_catalog.py
Validates YAML source definition files in gcp_migration/metadata/sources/.
Ensures mandatory fields, valid types, and correct entity structures.
Used in GitHub Actions CI to gate pull requests.
"""

import sys
from pathlib import Path
import yaml

REQUIRED_FIELDS = ["source_id", "name", "pipeline_type", "target_entities"]
VALID_PIPELINE_TYPES = ["METADATA_DRIVEN", "DATAFORM_DAG"]
VALID_ENTITIES = [
    "persons", "contacts", "addresses", "documents",
    "works", "digital_footprint", "movements", "vehicles"
]
VALID_CONTACT_TYPES = ["PHONE", "EMAIL"]
VALID_FOOTPRINT_TYPES = ["IP", "TELEGRAM", "USER_AGENT"]


def validate_file(file_path: Path) -> list[str]:
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as exc:
        return [f"Failed to parse YAML: {exc}"]

    if not isinstance(data, dict):
        return ["Top-level element must be a dictionary/mapping"]

    # Validate optional SLA config if present
    if "sla" in data:
        sla = data["sla"]
        if not isinstance(sla, dict):
            errors.append("'sla' must be a dictionary/mapping")
        else:
            if "update_frequency" in sla and sla["update_frequency"] not in ["STATIC", "RECURRING"]:
                errors.append("'sla.update_frequency' must be 'STATIC' or 'RECURRING'")
            if "is_static" in sla and not isinstance(sla["is_static"], bool):
                errors.append("'sla.is_static' must be a boolean")
            if "max_staleness_hours" in sla and sla["max_staleness_hours"] is not None and not isinstance(sla["max_staleness_hours"], int):
                errors.append("'sla.max_staleness_hours' must be an integer or null")
            if "min_expected_rows" in sla and not isinstance(sla["min_expected_rows"], int):
                errors.append("'sla.min_expected_rows' must be an integer")

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")

    source_id = data.get("source_id", "")
    if not source_id.startswith("index_"):
        errors.append(f"source_id '{source_id}' must follow pattern 'index_XXXX'")

    pipeline_type = data.get("pipeline_type")
    if pipeline_type not in VALID_PIPELINE_TYPES:
        errors.append(f"Invalid pipeline_type '{pipeline_type}'. Must be one of {VALID_PIPELINE_TYPES}")

    target_entities = data.get("target_entities")
    if pipeline_type == "DATAFORM_DAG":
        if not isinstance(target_entities, list) and not isinstance(target_entities, dict):
            errors.append("'target_entities' in DATAFORM_DAG must be a list of target tables or mapping")
        if "dataform" not in data or not isinstance(data["dataform"], dict):
            errors.append("DATAFORM_DAG sources must define a 'dataform' mapping with models")
        return errors

    if not isinstance(target_entities, dict):
        errors.append("'target_entities' must be a dictionary/mapping")
        return errors

    # Check that at least one entity is defined
    defined_entities = [k for k in target_entities.keys() if k in VALID_ENTITIES]
    if not defined_entities:
        errors.append(f"At least one valid target entity must be defined from {VALID_ENTITIES}")

    # Validate contacts if present
    if "contacts" in target_entities:
        contacts = target_entities["contacts"]
        if not isinstance(contacts, list):
            errors.append("'target_entities.contacts' must be a list of contact definitions")
        else:
            for i, c in enumerate(contacts):
                if not isinstance(c, dict):
                    errors.append(f"Contact item #{i} must be a dictionary")
                    continue
                if "contact_type" not in c or "value_col" not in c:
                    errors.append(f"Contact item #{i} missing 'contact_type' or 'value_col'")
                elif c["contact_type"] not in VALID_CONTACT_TYPES:
                    errors.append(f"Contact item #{i} invalid contact_type '{c['contact_type']}'")

    # Validate digital footprint if present
    if "digital_footprint" in target_entities:
        footprint = target_entities["digital_footprint"]
        if not isinstance(footprint, list):
            errors.append("'target_entities.digital_footprint' must be a list")
        else:
            for i, fp in enumerate(footprint):
                if not isinstance(fp, dict):
                    errors.append(f"Digital footprint item #{i} must be a dictionary")
                    continue
                if "channel_type" not in fp or "value_col" not in fp:
                    errors.append(f"Digital footprint item #{i} missing 'channel_type' or 'value_col'")

    return errors


def main():
    sources_dir = Path(__file__).resolve().parent / "sources"
    yaml_files = sorted(list(sources_dir.glob("*.yaml")) + list(sources_dir.glob("*.yml")))

    if not yaml_files:
        print(f"ERROR: No YAML files found in {sources_dir}")
        sys.exit(1)

    print(f"Validating {len(yaml_files)} source specification files...")
    total_errors = 0

    for yf in yaml_files:
        errs = validate_file(yf)
        if errs:
            print(f"❌ {yf.name}:")
            for err in errs:
                print(f"   - {err}")
            total_errors += len(errs)
        else:
            print(f"✅ {yf.name} (Valid)")

    if total_errors > 0:
        print(f"\nValidation failed with {total_errors} errors.")
        sys.exit(1)
    else:
        print(f"\nAll {len(yaml_files)} source specification files are strictly valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()
