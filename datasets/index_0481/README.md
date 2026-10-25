# Parsetron results

## About row data

> - Code name: index_0481
> - File path: *.json
> - Total rows: 2148

### Schema
```
root
 |-- data: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- C_BASE: string (nullable = true)
 |    |    |-- C_BLOCKED_SHOW: string (nullable = true)
 |    |    |-- C_CLFIS: string (nullable = true)
 |    |    |-- C_DATE_LAST: string (nullable = true)
 |    |    |-- C_DATE_OPEN: string (nullable = true)
 |    |    |-- C_NAME: string (nullable = true)
 |    |    |-- C_PAY_CODE: string (nullable = true)
 |    |    |-- C_SALDO: double (nullable = true)
 |    |    |-- C_TYPE_ACC: string (nullable = true)
 |    |    |-- ID: long (nullable = true)
 |    |    |-- ID_BASE: long (nullable = true)
 |    |    |-- ID_ORGANIZATION: long (nullable = true)
 |-- sql: string (nullable = true)

```

### Data sample
```
| data   | sql   |
|--------|-------|
```


## About final data
> - Total rows: 13138080

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- actuality: string (nullable = true)

```



### Data sample
```
| names   | phones   | raw_metadata   | actuality   |
|---------|----------|----------------|-------------|
```