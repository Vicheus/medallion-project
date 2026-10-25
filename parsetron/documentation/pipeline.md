# YAML Data Processing

## Overview


## YAML Config
```yaml
# TODO: There is no entity and column validations. Add required entity and column validations
# Index associated with the processing data
sourceId: "index_0000"
# (optional) Identifies the origin of `phones` and `documents` to parse
# Accepted values: `RU`, `BY`, `KZ`
# Default: `RU`
countryCode: "RU"
# (optional) Specifies `source_entity_id` generation type. ID generation happens on pre-processed
# (`bronze.read.trimValues,replaceWithNone,replaceRegexWithNone`) columns specified in `entities`
# Accepted values: `stable_int` (1..n ID, stable), `unstable_int` (1..n ID, unstable per runs), `hash_int` (hashed
# integer ID, stable), `hash_sha224` (hashed letter and integer based ID, stable)
# Default: `hash_sha224`
sourceEntityIdHashType: "hash_sha224"
# Data pre-processing level that only takes required fields, adds associated record id `source_entity_id` without
# additional processing
# Type: object, list of objects
bronze:
  # (optional if a single object, required if a list of objects) Associated with the input data
  id: ""
  # Specifies reading parameters
  # Type: object
  read:
    # (optional) Data reading format
    # Allowed values: `csv`
    # Default: `csv`
    format: "csv"
    # (optional) Partial path to the file (without its name). Takes place when `path` is not absolute
    basePath: ""
    # Path to the file to read
    path: "path/to/data.csv"
    # (optional) Defines header (each column becomes string)
    # Type: list of strings
    header:
    # (optional) Specific parameters while reading the data according to Spark
    # Type: dictionary (object)
    options:
      # There are several parameters specified with default values:
      # (optional) Reads all data as string type if `false`, otherwise is trying to determine type (can lead to partial
      # data loss)
      # Type: boolean
      # Default: `true`
      inferSchema: true
      # (optional) Accepts the first row as a header if `true`
      # Type: boolean
      # Default: `true`
      header: true
      # (optional, default: ,) Field delimiter
      # Default: `,`
      sep: ","
      # (optional) File encoding
      # Default: `UTF-8`
      encoding: "UTF-8"
      # (optional) Defines the character used to escape special characters within a field
      # default: `"`
      escape: '"'
      # (optional) Defines the behavior when encountering records that do not match the expected schema or format
      # Accepted values: `PERMISSIVE` (default by Spark), `DROPMALFORMED`, `FAILFAST`
      # Default: `FAILFAST`
      mode: "FAILFAST"
    # (optional) Removes trailing whitespaces (specified symbols if string). Does not convert empty value into None.
    # Can be replaced with `replaceRegexWithNone`
    # Type: boolean, string
    # Default: `false`
    trimValues: false
    # (optional) Defines values to replace with None
    # Type: string, list of strings
    replaceWithNone: ""
    # (optional) Defines regular expressions to replace matched values with None
    # Type: string, list of strings
    replaceRegexWithNone: "^\\s*NULL\\s*$"
    # (optional) Data to append (Union) or join
    # Type: Union, Join, list of combined Union and/or Join
    append:
      # Specifies reading parameters, the same type as the root read, including nested `append`
      - read:
          path: "path/to/data/join.csv"
        # Lists IDs to join 2 datasets, the second key is always related to the second (joined) data. If only one ID is
        # provided, then it is used on both
        # Type: string, list of strings (max 2)
        ids:
          - "id"
          - "second_id"
        # (optional) Specifies join type
        # Allowed values: `inner`, `left`, `right`, `outer`, `left_anti`
        # Default: `left`
        type: "left"
        # (optional) Specifies suffix to append to the joined data columns except join ID, to prevent ambiguous naming
        renameSuffix: "_join"
      # Specifies reading parameters, the same type as the root read, including nested `append`
      - read:
          path: "path/to/data/union.csv"
        # (optional) Appends the data by column names
        # Type: boolean
        # Default: `false`
        allowMissingColumns: false
  # (optional) Specifies instructions to apply on the dataset after read
  afterRead:
    # (optional) Drops duplicates based on the entities required columns. Applying before `source_entity_id` generation
    # Type: boolean
    # Default: `true`
    distinct: true
    # (optional) Cashes the read data to speed up `entities` processing that prevents duplicating read, ID generation,
    # distinct steps. Applying after `source_entity_id` generation
    # Type: boolean
    # Default: `true`
    cache: true
  # Specifies entities and their fields to select and save
  entities:
    # Entities to save. Must match with the Silver layer
    # Type: object
    persons:
      # (optional) Defines write parameters
      io:
        write:
          # (optional) Writing type
          # Allowed values: `repartition`, `coalesce`, `coalesce_size`
          # Default: repartition
          type: "repartition"
          # (optional) Files count, or size of data chunk in MB to split if `type` is `coalesce_size`
          # Type: integer
          # Default: `4`
          count: 4
      # Columns to hold within the entity
      columns:
        # Destination column
        # Type: string, object
        name:
          # Source column to take
          source: "fio"
          # (optional) Spark type to cast processing column. Throws an error if cast is not possible due to data format
          # Allowed values: `string`, `timestamp`, `integer`, `double`
          # Default: `string`
          type: "string"
        # Key-value definition automatically casts column to string type
        birth_date: "date_of_birth"
# Data processing level which parses, transforms and enriches the data
# Type: object, list of objects
silver:
  # (optional if a single object, required if a list of objects) Associated with the input data (bronze)
  id: ""
  # Specifies entities and their fields to select, transform, enrich, and save
  # Type: object
  entities:
    # Entities to save. Must match with the Bronze layer
    persons:
      # (optional) Reads and joins (outer) specified entities from Bronze as a source. By default, takes only the
      # specified above entity name as a source
      # Type: string, list of strings
      entities: [ "persons", "common" ]
      # (optional) Defines write parameters
      io:
        write:
          # (optional) Writing type
          # Allowed values: `repartition`, `coalesce`, `coalesce_size`
          # Default: repartition
          type: "repartition"
          # (optional) Files count, or size of data chunk in MB to split if `type` is `coalesce_size`
          # Type: integer
          # Default: `3`
          count: 4
      columns:
        # Destination column. Columns start with `__` will not be added to the final entity
        __processed_name:
          # (required, type: string, literal object, instruction object) Source to process with the instructions
          source:
            # Instruction to apply on the column
            fn: "name_udf"
            # (required, type: type: string, literal object, instruction object) Column to process within the
            # instruction
            column: "name"
          # (optional) If `True` filters out values equal None
          # Type: boolean, instruction object (fn)
          # Default: `false`
          filter: true
        names:
          source: "__processed_name"
        birth_date:
          source:
            fn: "birth_date_udf"
            column: "birth_date"
            date_format: "%Y-%m-%d"
# Data post-processing level which groups and clears the data
# Type: object, list of objects
gold:
  # (optional, required if Bronze and Silver holds 2+ IDs) Associated with the input data (bronze, silver). Datasets are
  # combined using union by name with allowed missing columns
  ids:
    - id: "id1"
      # (optional) Performs listed operations on the dataset
      # Type: transformation object (op), list of transformation objects
      transformations:
    - id: "id2"
      transformations:
  # (optional) Defines write parameters
  io:
    write:
      # (optional) Writing type
      # Allowed values: `repartition`, `coalesce`, `coalesce_size`
      # Default: repartition
      type: "coalesce"
      # (optional) Files count, or size of data chunk in MB to split if `type` is `coalesce_size`
      # Type: integer
      # Default: `1`
      count: 1
  # (optional) Performs listed operations on the dataset
  # Type: transformation object (op), list of transformation objects 
  transformations:
    op: "groupBy"
    columns:
      - "names"
      - "emails"
  # Keeps the only records that meet condition
  # Type: string (names & string), list of strings (names & (string1 | ... | stringn)), instruction object (fn)
  remain: "emails"
```
