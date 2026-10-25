# Pipeline Functions

## Overview

This document defines the functions available within the pipeline engine. These functions are applied exclusively to
the **Silver** and **Gold** layers to facilitate data parsing, transformation, and enrichment.

Functions may contain nested structures and can be found in the [Function Registry](../engine/registry/functions).

## Data Primitives

When defining arguments in YAML, use the following primitives:

| Primitive     | Description                                         | Example                       |
|:--------------|:----------------------------------------------------|:------------------------------|
| `string`      | A standard column name or string literal.           | `"user_id"`                   |
| `literal`     | A value treated as a constant.                      | `lit: 10` or `lit: "active"`  |
| `instruction` | A nested function call containing an `fn` key.      | `fn: "upper", column: "name"` |
| `list`        | A collection of strings, literals, or instructions. | `- "col1"`, `- lit: 5`        |

---

## Table of Contents

- [Conditions](#conditions)
- [Modifiers](#modifiers)
- [Complex Functions](#complex-functions)
- [User Defined Functions (UDFs)](#user-defined-functions)

## Conditions

[Placing location](../engine/registry/functions/conditions.py) (Spark operations only)

### Logical AND

Checks if multiple conditions are all true

**YAML Configuration**

```yaml
fn: "and"
# Type: list of strings and/or literals and/or instructions
columns:
  - "col1"
  - "col2"
```

**PySpark Implementation**

```python
(col("col1")) & (col("col2"))
```

### Logical OR

Checks if any of the provided conditions are true

**YAML Configuration**

```yaml
fn: "or"
# Type: list of strings and/or literals and/or instructions
columns:
  - "col1"
  - "col2"
```

**PySpark Implementation**

```python
(col("col1")) | (col("col2"))
```

### Logical NOT

Negates a single condition (e.g., `NOT (condition)`)

**YAML Configuration**

```yaml
fn: "not"
# Type: string, literal, instruction
column: "condition"
```

**PySpark Implementation**

```python
~(col("condition"))
```

### Comparison Operators

| Operator | Description                                                | YAML Key    |
|:---------|:-----------------------------------------------------------|:------------|
| `eq`     | Checks for equality (`==`).                                | `fn: "eq"`  |
| `ne`     | Checks for inequality (`!=`).                              | `fn: "ne"`  |
| `gt`     | Checks if column value is greater than (`>`).              | `fn: "gt"`  |
| `gte`    | Checks if column value is greater than or equal to (`>=`). | `fn: "gte"` |
| `lt`     | Checks if column value is less than (`<`).                 | `fn: "lt"`  |
| `lte`    | Checks if column value is less than or equal to (`<=`).    | `fn: "lte"` |

**Common Structure for Comparison Operators:**
(Applies to `eq`, `ne`, `gt`, `gte`, `lt`, `lte`)

**YAML Configuration**

```yaml
# Replace with specific fn
fn: "eq"
# Type: string, literal, instruction
column: "number"
# Type: literal
value:
  lit: 10
```

**PySpark Implementation**

```python
col("number") == lit(10)
```

### Between

Checks if a column's value falls within a specified inclusive range (`lower ≤ X ≤ upper`)

**YAML Configuration**

```yaml
fn: "between"
# Type: string, literal, instruction
column: "id"
# Type: string, literal, instruction
lower:
  lit: 10
# Type: string, literal, instruction
upper:
  lit: 100
```

**PySpark Implementation**

```python
col("id").between(lit(10), lit(100))
```

### Contains

Checks if a column's value contains the specified substring

**YAML Configuration**

```yaml
fn: "contains"
# Type: string, literal, instruction
column: "text"
# Type: string, literal, instruction
value:
  lit: "word"
```

**PySpark Implementation**

```python
col("text").contains(lit("word"))
```

### Endswith

Checks if a column's value ends with the specified suffix

**YAML Configuration**

```yaml
fn: "endswith"
# Type: string, literal, instruction
column: "word"
# Type: string, literal, instruction
value:
  lit: "suffix"
```

**PySpark Implementation**

```python
col("word").endswith(lit("suffix"))
```

### Startswith

Checks if a column's value starts with the specified prefix

**YAML Configuration**

```yaml
fn: "startswith"
# Type: string, literal, instruction
column: "word"
# Type: string, literal, instruction
value:
  lit: "prefix"
```

**PySpark Implementation**

```python
col("word").startswith(lit("prefix"))
```

### IsNull

Checks if the specified column value is null

**YAML Configuration**

```yaml
fn: "isNull"
# Type: string, literal, instruction
column: "data"
```

**PySpark Implementation**

```python
col("data").isNull()
```

### IsNotNull

Checks if the specified column value is not null

**YAML Configuration**

```yaml
fn: "isNotNull"
# Type: string, literal, instruction
column: "data"
```

**PySpark Implementation**

```python
col("data").isNotNull()
```

### Isin

Checks if the specified column value is present within a list of values

**YAML Configuration**

```yaml
fn: "isin"
# Type: string, literal, instruction
column: "symbol"
# Type: list of strings and/or literals and/or instructions
values:
  - lit: "a"
  - lit: "b"
```

**PySpark Implementation**

```python
col("symbol").isin(lit("a"), lit("b"))
```

### Like

Checks if the column value matches a specified pattern using SQL wildcard matching (`%`, `_`)

**YAML Configuration**

```yaml
fn: "like"
# Type: string, literal, instruction
column: "example"
# Type: literal
value:
  lit: "test%"
```

**PySpark Implementation**

```python
col("example").like("test%")
```

### RLike

Checks if the column value matches a specified regular expression pattern

**YAML Configuration**

```yaml
fn: "rlike"
# Type: string, literal, instruction
column: "word"
# Type: literal
value:
  lit: "^[A-Z]+$"
```

**PySpark Implementation**

```python
col("word").rlike("^[A-Z]+$")
```

## Modifiers

[Placing location](../engine/registry/functions/modifiers.py) (Spark operations only)

### Array

Creates an array from a specified list of columns

**YAML Configuration**

```yaml
fn: "array"
# Type: string, literal, instruction, list of instructions
columns:
  - "col1"
  - lit: "word"
```

**PySpark Implementation**

```python
array(col("col1"), lit("word"))
```

### ArrayCompact

Removes null values from the specified array

**YAML Configuration**

```yaml
fn: "array_compact"
# Type: string, literal, instruction
column: "data"
```

**PySpark Implementation**

```python
array_compact(col("data"))
```

### ArrayDistinct

Returns an array containing only the distinct values from the input array

**YAML Configuration**

```yaml
fn: "array_distinct"
# Type: string, literal, instruction
column: "data"
```

**PySpark Implementation**

```python
array_distinct(col("data"))
```

### Coalesce

Returns the first non-null value among the specified columns

**YAML Configuration**

```yaml
fn: "coalesce"
# Type: string, literal, instruction, list of instructions
columns:
  - "col1"
  - "col2"
  - lit: "default"
```

**PySpark Implementation**

```python
coalesce(col("col1"), col("col2"), lit("default"))
```

### Concat

Concatenates the specified columns into a single value

**YAML Configuration**

```yaml
fn: "concat"
# Type: string, literal, instruction, list of instructions
columns:
  - "first_name"
  - "last_name"
```

**PySpark Implementation**

```python
concat(col("first_name"), col("last_name"))
```

### ConcatWs

Concatenates the specified columns into a single string using a specified separator

**YAML Configuration**

```yaml
fn: "concat_ws"
# Type: string, literal, instruction, list of instructions
columns:
  - "item1"
  - "item2"
# Type: literal
# Default: ` `
sep:
  lit: ", "
```

**PySpark Implementation**

```python
concat_ws(", ", col("item1"), col("item2"))
```

### Explode

Explodes an array column into multiple rows, creating one row for each element

**YAML Configuration**

```yaml
fn: "explode"
# Type: string, literal, instruction
column: "values"
```

**PySpark Implementation**

```python
explode(col("values"))
```

### Greatest

Returns the greatest value among the specified columns

**YAML Configuration**

```yaml
fn: "greatest"
# Type: string, literal, instruction, list of instructions
columns:
  - "score1"
  - "score2"
```

**PySpark Implementation**

```python
greatest(col("score1"), col("score2"))
```

### Length

Returns the length of the string in the specified column

**YAML Configuration**

```yaml
fn: "length"
# Type: string, literal, instruction
column: "example_string"
```

**PySpark Implementation**

```python
length(col("example_string"))
```

### Lower

Converts the specified column to lowercase

**YAML Configuration**

```yaml
fn: "lower"
# Type: string, literal, instruction
column: "example_string"
```

**PySpark Implementation**

```python
lower(col("example_string"))
```

### Replace

Replaces all occurrences of a specified substring with a replacement string in a column

**YAML Configuration**

```yaml
fn: "replace"
# Type: string, literal, instruction
column: "original_string"
# Type: string, literal, instruction
pattern:
  lit: "old_word"
# (optional) 
# Type: string, literal, instruction
# Default: `None`
replacement:
  lit: "new_word"
```

**PySpark Implementation**

```python
col("original_string").replace(lit("old_word"), lit("new_word"))
```

### RegexpReplace

Replaces substrings that match a specified regular expression pattern

**YAML Configuration**

```yaml
fn: "regexp_replace"
# Type: string, literal, instruction
column: "email"
# Type: string, literal, instruction
pattern:
  lit: "[^@]+@[^@]+\\.[^@]+$"
# Type: string, literal, instruction
replacement:
  lit: "valid_email"
```

**PySpark Implementation**

```python
regexp_replace(col("email"), lit("[^@]+@[^@]+\\.[^@]+$"), lit("valid_email"))
```

### Size

Returns the size of the specified column (e.g., the number of elements in an array)

**YAML Configuration**

```yaml
fn: "size"
# Type: string, literal, instruction
column: "example_array"
```

**PySpark Implementation**

```python
size(col("example_array"))
```

### Split

Splits the specified column value into a list of strings based on a pattern (delimiter)

**YAML Configuration**

```yaml
fn: "split"
# Type: string, literal, instruction
column: "csv_line"
# Type: string, literal, instruction
pattern:
  lit: ","
# (optional)
# Type: string, literal, instruction
# Default: `-1`
limit:
  lit: 3
```

**PySpark Implementation**

```python
split(col("csv_line"), lit(","), 3)
```

### Trim

Trims leading and trailing whitespace from the specified column

**YAML Configuration**

```yaml
fn: "trim"
# Type: string, literal, instruction
column: "whitespace_string"
```

**PySpark Implementation**

```python
col("whitespace_string").trim()
```

### Upper

Converts the specified column to uppercase

**YAML Configuration**

```yaml
fn: "upper"
# Type: string, literal, instruction
column: "example_string"
```

**PySpark Implementation**

```python
upper(col("example_string"))
```

### Struct (Named Structure Creation)

Creates a structured object (struct) by grouping related columns or literals into a single field

**YAML Configuration**

```yaml
fn: "struct"
# Defines key-value pairs for the struct fields.
# Type: string, literal, instruction
values:
  user_id: "id"
  status:
    lit: "active"
  join_date: "joined"
```

**PySpark Implementation**

```python
struct(
    col("id").alias("user_id"),
    lit("active").alias("status"),
    col("joined").alias("join_date"),
)
```

### Left Padding

Prepends the specified symbol to the value up to the specified length

**YAML Configuration**

```yaml
fn: "lpad"
# Type: string, literal, instruction
column: "value"
# Type: literal
len:
  lit: 5
# Type: literal
pad:
  lit: 0
```

**PySpark Implementation**

```python
lpad(col("value"), lit(5), lit(0))
```

### From Unix Time

Converts the number of seconds to a string representing timestamp

**YAML Configuration**

```yaml
fn: "from_unixtime"
# Type: string, literal, instruction
column: "value"
# (optional)
# Type: literal
# Default: `yyyy-MM-dd HH:mm:ss`
date_format:
  lit: "yyyy-MM-dd HH:mm:ss"
```

**PySpark Implementation**

```python
from_unixtime(col("value"), lit("yyyy-MM-dd HH:mm:ss"))
```

### From JSON

Parses the specified value from JSON type into the specified one

**YAML Configuration**

```yaml
fn: "from_json"
# Type: string, literal, instruction
column: "value"
# Type: literal
schema:
  lit: "array<string>"
```

**PySpark Implementation**

```python
from_json(col("value"), "array<string>")
```

### Translate

Translates the specified symbol sequence to the corresponding one

**YAML Configuration**

```yaml
fn: "translate"
# Type: string, literal, instruction
column: "value"
# Type: literal
matching:
  lit: "abc"
# Type: literal
replace:
  lit: "def"
```

**PySpark Implementation**

```python
translate(col("value"), lit("abc"), lit("def"))
```

### Array Join

Joins values inside array by the specified delimiter

**YAML Configuration**

```yaml
fn: "array_join"
# Type: string, literal, instruction
column: "data"
# (optional)
# Type: literal
# Default: ` `
delimiter:
  lit: " "
```

**PySpark Implementation**

```python
array_join(col("data"), lit(" "))
```

### Capitalize

Capitalizes the first letter of each word

**YAML Configuration**

```yaml
fn: "initcap"
# Type: string, literal, instruction
column: "name"
```

**PySpark Implementation**

```python
initcap(col("name"))
```

### Substring

Substrings value starting from the specified index (1 is the first) up to the specified length

**YAML Configuration**

```yaml
fn: "substring"
# Type: string, literal, instruction
column: "sentence"
# (optional)
# Type: literal
# Default: `1`
pos:
  lit: 1
# Type: literal
len:
  lit: 3
```

**PySpark Implementation**

```python
substring(col("sentence"), lit(1), lit(3))
```

## Complex Functions

[Placing location](../engine/registry/functions/custom.py) (Spark operations only)

### Single When (Conditional Logic)

Evaluates a single `when`

**YAML Configuration**

```yaml
fn: "case"
condition:
  fn: "gt"
  # Type: string, literal, instruction
  column: "number"
  # Type: string, literal, instruction
  value:
    lit: 10
# Type: string, literal, instruction
value:
  lit: "Passed"
```

**PySpark Implementation**

```python
when(col("number") > 10, lit("Passed"))
```

### When (Conditional Logic)

Evaluates expressions sequentially. The first condition that evaluates to true determines the resulting value. If no
conditions match, an optional `otherwise` value is returned

**YAML Configuration**

```yaml
fn: "when"
# Defines the primary condition/case
# Type: case, list of cases
cases:
  # Type: string, literal, instruction
  - condition:
      fn: "gt"
      column: "number"
      value:
        lit: 10
    value:
      lit: "High"
  - condition:
      fn: "lt"
      column: "number"
      value:
        lit: 0
    value:
      lit: "Low"
# (optional)
# Type: string, literal, instruction
otherwise:
  lit: "Unknown"
```

**PySpark Implementation**

```python
when(col("number") > 10, lit("High")).when(col("number") < 0, lit("Low")).otherwise(lit("Unknown"))
```

### Is Not Null and Not Equal to (Conditional Logic)

Checks if the specified column value is not null and not equal to the specified value

**YAML Configuration**

```yaml
fn: "isNotNull_ne"
# Type: string, literal, instruction
column: "word"
# Type: string, literal, instruction
# Default: ``
value:
  lit: ""
```

**PySpark Implementation**

```python
col("word").isNotNull() & (col("word") != lit(""))
```

### Translate Map

Maps values from a column to new values using a dictionary-like lookup

**YAML Configuration**

```yaml
fn: "translate_map"
# Type: string, literal, instruction
column: "status"
# Defines the mapping of old values to new values
# Type: dict[string, string]
values:
  "1": "Active"
  "0": "Inactive"
# (optional)
# Type: string, literal, instruction
otherwise:
  lit: "Unknown"
```

**PySpark Implementation**

```python
coalesce(create_map(lit("1"), lit("Active"), lit("0"), lit("Inactive"))[col("status")], lit("Unknown"))
```

### Regexp Extract

Extracts a substring from a column based on a regular expression and a specific capture group index

**YAML Configuration**

```yaml
fn: "regexp_extract"
# Type: string, literal, instruction
column: "text"
# Type: literal
pattern:
  lit: "(\\d+)"
# Type: literal
index:
  lit: 1
```

**PySpark Implementation**

```python
regexp_extract(col("text"), lit("(\\d+)"), 1)
```

### Regexp Extract All

Extracts all substrings that match a regular expression pattern into an array

**YAML Configuration**

```yaml
fn: "regexp_extract_all"
# Type: string, literal, instruction
column: "text"
# Type: literal
pattern:
  lit: "[a-z]+"
# (optional)
# Type: literal
index:
  lit: 1
```

**PySpark Implementation**

```python
regexp_extract_all(col("text"), lit("[a-z]+"), 1)
```

## User Defined Functions

### Actuality

Parses a value according to pattern and turning it into the date type

**YAML Configuration**

```yaml
fn: "actuality_date_udf"
# Type: string, literal, instruction
column: "date"
# (optional) Date pattern to retrieve
# Type: literal
# Default: `%Y-%m-%d %H:%M:%S`
date_format:
  lit: "%Y-%m-%d %H:%M:%S"
```

**PySpark Implementation**

```python
actuality_date_udf(col("date"), lit("%Y-%m-%d %H:%M:%S"))
```

### Latest Actuality

Parses values according to pattern and turning them into the date type to select the maximum (latest) one

**YAML Configuration**

```yaml
fn: "latest_actuality_date_udf"
# Type: string, literal, instruction
columns:
  - "first_date"
  - "second_date"
# (optional) Date pattern to retrieve
# Type: literal
# Default: `%Y-%m-%d %H:%M:%S`
date_format:
  lit: "%Y-%m-%d %H:%M:%S"
```

**PySpark Implementation**

```python
latest_actuality_date_udf(col("first_date"), col("second_date"), lit("%Y-%m-%d %H:%M:%S"))
```

### Name Parts Ordered

Retrieves a name from the given parts in passed order joined by space

**YAML Configuration**

```yaml
fn: "name_parts_ordered_udf"
# Type: string, literal, instruction
columns:
  - "firstname"
  - "lastname"
```

**PySpark Implementation**

```python
name_parts_ordered_udf(col("lastname"), col("firstname"))
```

### Names

Retrieves names from the given array

**YAML Configuration**

```yaml
fn: "names_udf"
# Type: string, literal, instruction (that holds an array)
column: "names"
```

**PySpark Implementation**

```python
names_udf(col("names"))
```

### Name

**YAML Configuration**

```yaml
fn: "name_udf"
# Type: string, literal, instruction
column: "name"
```

**PySpark Implementation**

```python
name_udf(col("name"))
```

### Birth Date

Parses a value according to pattern

**YAML Configuration**

```yaml
fn: "birth_date_udf"
# Type: string, literal, instruction
column: "dob"
# (optional) Date pattern to retrieve
# Type: literal
# Default: `%Y-%m-%d`
date_format:
  lit: "%d.%m.%Y"
```

### Death Date

**YAML Configuration**

```yaml
fn: "death_date_udf"
# Type: string, literal, instruction
column: "dod"
# (optional) Date pattern to retrieve
# Type: literal
# Default: `%Y-%m-%d`
date_format:
  lit: "%d.%m.%Y"
```

**PySpark Implementation**

```python
death_date_udf(col("dod"), lit("%d.%m.%Y"))
```

### Sex

**YAML Configuration**

```yaml
fn: "sex_udf"
# Type: string, literal, instruction
column: "sex"
```

**PySpark Implementation**

```python
sex_udf(col("sex"))
```

### Phones

**YAML Configuration**

```yaml
fn: "phones_udf"
# Type: string, literal, instruction (that holds an array)
column: "phones"
# (optional) Overrides config root `countryCode` if present (specified)
# Type: literal
# Accepted values: `RU`, `BY`, `KZ`
# Default: `RU`
countryCode:
  lit: "RU"
```

**PySpark Implementation**

```python
phones_udf(col("phones"))
```

### Phone

**YAML Configuration**

```yaml
fn: "phone_udf"
# Type: string, literal, instruction
column: "phone"
# (optional) Overrides config root `countryCode` if present (specified)
# Type: literal
# Accepted values: `RU`, `BY`, `KZ`
# Default: `RU`
countryCode:
  lit: "RU"
```

**PySpark Implementation**

```python
phone_udf(col("phone"))
```

### Emails

**YAML Configuration**

```yaml
fn: "emails_udf"
# Type: string, literal, instruction (that holds an array)
column: "emails"
```

**PySpark Implementation**

```python
emails_udf(col("emails"))
```

### Email

**YAML Configuration**

```yaml
fn: "email_udf"
# Type: string, literal, instruction
column: "email"
```

**PySpark Implementation**

```python
email_udf(col("email"))
```

### IP Address

**YAML Configuration**

```yaml
fn: "ip_address_udf"
# Type: string, literal, instruction
column: "ip_address"
```

**PySpark Implementation**

```python
ip_address_udf(col("ip_address"))
```

### Work

**YAML Configuration**

```yaml
fn: "work_udf"
# (optional)
# Type: string, literal, instruction
post: "profession"
# (optional)
# Type: string, literal, instruction
date_start: "start"
# (optional)
# Type: string, literal, instruction
date_end: "end"
# (optional)
# Type: string, literal, instruction
company: "company_title"
# (optional)
# Type: string, literal, instruction
company_address: "company_address_value"
# (optional)
# Type: string, literal, instruction
comment: "comment_value"
```

**PySpark Implementation**

```python
work_udf(
    col("profession"),
    col("start"),
    col("end"),
    col("company_title"),
    col("company_address_value"),
    col("comment_value"),
)
```

### Document

**YAML Configuration**

```yaml
fn: "document_udf"
# Type: string, literal, instruction
type: "doc_type"
# Type: string, literal, instruction
serial: "doc_number"
# (optional)
# Type: string, literal, instruction
date_issue: "issue_date"
# (optional)
# Type: string, literal, instruction
date_expire: "expire_date"
# (optional)
# Type: string, literal, instruction
authority: "doc_authority"
# (optional)
# Type: string, literal, instruction
authority_code: "doc_authority_code"
# (optional)
# Type: literal
# Default: `%Y-%m-%d`
date_format:
  lit: "%Y-%m-%d"
# (optional) Overrides config root `countryCode` if present (specified)
# Type: literal
# Accepted values: `RU`, `BY`, `KZ`
# Default: `RU`
countryCode:
  lit: "RU"
```

**PySpark Implementation**

```python
document_udf(
    document_type=col("doc_type"),
    serial=col("doc_number"),
    date_issue=col("issue_date"),
    date_expire=col("expire_date"),
    authority=col("doc_authority"),
    authority_code=col("doc_authority_code"),
    date_format=lit("%Y-%m-%d"),
    country_code=lit("RU"),
)
```

### Forces

**YAML Configuration**

```yaml
fn: "forces_udf"
# Type: string, literal, instruction
tag_number: "tag"
# Type: string, literal, instruction
unit_code: "code"
# (optional)
# Type: string, literal, instruction
unit_name: "title"
# (optional)
# Type: string, literal, instruction
callsign: "callsign"
# (optional)
# Type: string, literal, instruction
rank: "rank"
# (optional)
# Type: string, literal, instruction
position: "position"
# (optional)
# Type: string, literal, instruction
mos_code: "mos_code"
# (optional)
# Type: string, literal, instruction
category: "category"
# (optional)
# Type: string, literal, instruction
date_start: "date_start"
# (optional)
# Type: string, literal, instruction
date_end: "date_end"
# (optional)
# Type: string, literal, instruction
comment: "comment"
# (optional)
# Type: literal
# Default: `%Y-%m-%d`
date_format:
  lit: "%Y-%m-%d"
```

**PySpark Implementation**

```python
forces_udf(
    tag_number=col("tag"),
    unit_code=col("code"),
    unit_name=col("title"),
    callsign=col("callsign"),
    rank=col("rank"),
    position=col("position"),
    mos_code=col("mos_code"),
    category=col("category"),
    date_start=col("date_start"),
    date_end=col("date_end"),
    comment=col("comment"),
    date_format=lit("%Y-%m-%d"),
)
```

### Education

**YAML Configuration**

```yaml
fn: "education_udf"
# Type: string, literal, instruction
title: "title"
# Type: string, literal, instruction
level: "level"
# Type: string, literal, instruction
country: "country"
# Type: string, literal, instruction
date_start: "date_start"
# Type: string, literal, instruction
date_end: "date_end"
# Type: string, literal, instruction
comment: "comment"
# (optional)
# Type: literal
# Default: `%Y-%m-%d`
date_format:
  lit: "%Y-%m-%d"
```

**PySpark Implementation**

```python
education_udf(
    title=col("title"),
    level=col("level"),
    country=col("country"),
    date_start=col("date_start"),
    date_end=col("date_end"),
    comment=col("comment"),
    date_format=lit("%Y-%m-%d"),
)
```

### Raw Metadata

**YAML Configuration**

```yaml
fn: "raw_metadata_udf"
# Defines key-value pairs for the struct fields
# Type: string, literal, instruction
values:
  user_id: "id"
  status:
    lit: "active"
  join_date: "joined"
```

**PySpark Implementation**

```python
raw_metadata_udf(
    lit("user_id"),
    col("id"),
    lit("status"),
    lit("active"),
    lit("join_date"),
    col("joined"),
)
```

### Address with Type

**YAML Configuration**

```yaml
fn: "address_with_type_udf"
# Type: string, literal, instruction
column: "address"
# Type: string, literal, instruction (value must be integer)
type:
  lit: 1
```

**PySpark Implementation**

```python
address_with_type_udf(col("address"), lit(1))
```

### Normalize Address Batch

**YAML Configuration**

```yaml
fn: "normalize_address_batch_udf"
# Type: string, literal, instruction
column: "address"
```

**PySpark Implementation**

```python
normalize_address_batch_udf(col("address"))
```

### Children

**YAML Configuration**

```yaml
fn: "children_udf"
# Type: string, literal, instruction
column: "has_children"
```

**PySpark Implementation**

```python
children_udf(col("has_children"))
```

### Device Date

**YAML Configuration**

```yaml
fn: "device_date_udf"
# Type: string, literal, instruction
column: "dd"
# (optional) Date pattern to retrieve
# Type: literal
# Default: `%Y-%m-%d`
date_format:
  lit: "%d.%m.%Y"
```

**PySpark Implementation**

```python
device_date_udf(col("dd"), lit("%d.%m.%Y"))
```

### Multiple Date Formats

Parses a date with the first matching date pattern

**YAML Configuration**

```yaml
fn: "multiple_date_formats_udf"
# Type: string, literal, instruction
column: "date"
# (optional) Date patterns to retrieve
# Type: literal, list of literals
# Default: `%Y-%m-%d`
date_formats:
  - lit: "%Y-%m-%d"
  - lit: "%d-%m-%Y"
# (optional) Min allowed year to return, calculation is based on the current year
# Type: literal, list of literals
# Default: `50`
max_years_from:
  lit: 50
# (optional) Max allowed year to return, calculation is based on the current year
# Type: literal, list of literals
# Default: `0`
max_years_to:
  lit: 0
# (optional) Parsed date pattern to receive
# Type: literal
# Default: `%d.%m.%Y`
result_date_format:
  lit: "%d.%m.%Y"
```

**PySpark Implementation**

```python
multiple_date_formats_udf(
    value=col("date"),
    date_formats=array(lit("%Y-%m-%d"), lit("%d-%m-%Y")),
    max_years_from=lit(50),
    max_years_to=lit(0),
    result_date_format=lit("%d.%m.%Y"),
)
```

### Relationship

**YAML Configuration**

```yaml
fn: "relationship_udf"
# Type: string, literal, instruction
column: "relationship"
```

**PySpark Implementation**

```python
relationship_udf(col("relationship"))
```

### Relations

**YAML Configuration**

```yaml
fn: "relationship_udf"
# Type: string, literal, instruction
column: "relations"
```

**PySpark Implementation**

```python
relations_udf(col("relations"))
```

### Address

Cleans a raw string as address

**YAML Configuration**

```yaml
fn: "address_udf"
# Type: string, literal, instruction
column: "raw_address"
```

**PySpark Implementation**

```python
address_udf(col("raw_address"))
```

### Social

Parses social media profile information

**YAML Configuration**

```yaml
fn: "social_udf"
# (optional)
# Type: string, literal, instruction
title: "social_title"
# (optional)
# Type: string, literal, instruction
id: "user_id"
# (optional)
# Type: string, literal, instruction
link: "profile_url"
# (optional)
# Type: string, literal, instruction
comment: "additional_notes"
```

**PySpark Implementation**

```python
social_udf(
    title=col("social_title"),
    id=col("user_id"),
    link=col("profile_url"),
    comment=col("additional_notes")
)
```

