# Pipeline Transformations

## Overview

Transformations take place only on the **Gold** layer, transforming the data.

Transformations may contain nested structures and can be found in [the registry](../engine/registry/transformations).

### Group By

**YAML Configuration**

```yaml
op: "groupBy"
# Values to group by. Other columns in the dataset are related to aggregation
# Type: string, list of strings
columns:
  - "id"
  - "type"
# (optional) Accepts instruction to get rows to group by
positive:
  fn: "and"
  columns:
    fn: "isNotNull"
    column: "id"
# (optional) If boolean then inverts `positive` with the help of negation. If `false` then negation filter value will
# not be appended using `unionByName` to `positive` group result
# Type: boolean, instruction
# Default: `true`
negative: true
```

**PySpark Implementation**

```python
group_df = df.filter(positive)
unmatched_df = df.filter(negative)
agg_cols = [column for column in df.columns if column not in columns]
group_df.groupBy(columns).agg(agg_cols).unionByName(unmatched_df)
```

### Aggregation Group By

**YAML Configuration**

```yaml
op: "aggGroupBy"
# Values to aggregate. Other columns in the dataset are related to grouping
# Type: string, list of strings
columns:
  - "id"
  - "type"
# (optional) Accepts instruction to get rows to group by
positive:
  fn: "and"
  columns:
    fn: "isNotNull"
    column: "id"
# (optional) If boolean then inverts `positive` with the help of negation. If `false` then negation filter value will
# not be appended using `unionByName` to `positive` group result
# Type: boolean, instruction
# Default: `true`
negative: true
```

**PySpark Implementation**

```python
group_df = df.filter(positive)
unmatched_df = df.filter(negative)
group_cols = [column for column in df.columns if column not in columns]
group_df.groupBy(group_cols).agg(columns).unionByName(unmatched_df)
```

### Actuality Group By

Groups by all columns, except `actuality` and `source_entity_id` which are related to aggregation max value

**YAML Configuration**

```yaml
op: "actualityGroupBy"
```

**PySpark Implementation**

```python
group_cols = [
    column for column in df.columns if column not in {actuality, source_entity_id}
]
(
    group_df.groupBy(group_cols)
    .agg(max(struct(actuality, source_entity_id)).alias(struct))
    .select("*", "struct.*")
    .drop(struct)
)
```

### Filter

Filters out records do not meet condition

**YAML Configuration**

```yaml
op: "filter"
# Type: instruction (fn)
column:
  fn: "isNotNull"
  column: "id"
```

**PySpark Implementation**

```python
df.filter(col("id").isNotNull())
```

### Distinct

**YAML Configuration**

```yaml
op: "distinct"
# (optional) Drops duplicates by columns, if omitted then distinct across all
# Type: string, list of strings
columns:
  - "id"
  - "type"
```

**PySpark Implementation**

```python
df.drop_duplicates("id", "type")
```

Or (if columns missing)

```python
df.distinct()
```

### Drop Columns

**YAML Configuration**

```yaml
op: "dropColumns"
# Columns to drop
# Type: string, list of strings
columns:
  - "id"
  - "type"
```

**PySpark Implementation**

```python
df.drop("id", "type")
```
