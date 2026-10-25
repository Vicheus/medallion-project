# Parsetron results

## About row data
{% for schema in schema_raw %}
> - Code name: {{ schema.code_name }}
> - File path: {{ schema.path.split('/')[-1] }}
> - Total rows: {{ schema.total }}

### Schema
```
{{ schema.schema }}
```

### Data sample
```
{{ schema.data_sample }}
```
{% endfor %}

## About final data
> - Total rows: {{ schema_final.total }}

### Schema
```
{{ schema_final.schema }}
```

{% if schema_final.columns_completeness %}
### Columns completeness

| Column   | Completeness |
|----------|--------------|
{% for column, completeness in schema_final.columns_completeness.items() -%}
| {{ column | capitalize }} | {{ "%.2f" % completeness }}% |
{% endfor %}
{% endif %}

### Data sample
```
{{ schema_final.data_sample }}
```
