# Forces Dataset Processing

This repository contains scripts to process the forces dataset.

## Setup

### 1. Mapping File

Before running the parser, you need to set up a **mapping file**.  
See the example: [`forces_mappings_example.json`](forces_mappings_example.json)

> **Note:**  
> If you have multiple fields for a single result property (e.g., `passport` and `inn`), separate them with a comma:

```json
"documents.serial": "passport_field,inn_field"

This configuration will create two entries in the documents array field in the results.

### 2. Running the Parser

Use the following command to run the main_forces.py script:

uv run python3 main_forces.py \
    --input_filepath <input_file_path> \
    --mapping_filepath <mapping_file_path> \
    --delimiter <delimiter> \
    --date_format <date_format> \
    --props_to_group_by <group_by_properties> \
    --props_to_aggregate <aggregate_properties>

| Parameter              | Description                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------- |
| `--input_filepath`     | Path to the input file                                                                 |
| `--mapping_filepath`   | Path to the mapping file created in Step 1                                             |
| `--delimiter`          | Delimiter used in the input file                                                       |
| `--date_format`        | Formats of dates in input file                                                         |
| `--props_to_group_by`  | Comma-separated list of properties to group results by (e.g., `names,birth_date`)      |
| `--props_to_aggregate` | Comma-separated list of properties to aggregate after grouping (e.g., `phones,emails`) |


**Example**

uv run python3 main_forces.py \
    --input_filepath data/forces_input.csv \
    --mapping_filepath config/forces_mappings.json \
    --delimiter "," \
    --date_format "%m/%d/%Y" \
    --props_to_group_by "names,birth_date" \
    --props_to_aggregate "phones,emails"

This command will produce a grouped and aggregated dataset according to your configuration.