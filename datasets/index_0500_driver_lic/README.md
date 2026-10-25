# Parsetron results

## About row data

> - Code name: index_0500_driver_lic
> - File path: Водительское_удостоверение_2024_@StormBaseAdapter.csv
> - Total rows: 58413

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- seria: long (nullable = true)
 |-- nomber: long (nullable = true)
 |-- data_birth: date (nullable = true)
 |-- date_issuance: date (nullable = true)
 |-- date_action: date (nullable = true)
 |-- category: string (nullable = true)

```

### Data sample
```
|   id |      seria |     nomber | data_birth   | date_issuance   | date_action   | category                   |
|-----:|-----------:|-----------:|:-------------|:----------------|:--------------|:---------------------------|
|    1 | 9935088309 | 9935088309 | 1992-07-17   | 2024-04-09      | 2034-04-09    | B,B1,BE,C,C1,C1E,CE,D,D1,M |
|    2 | 9932079709 | 9932079709 | 1964-01-30   | 2024-03-09      | 2034-03-09    | B,B1,M                     |
|    3 | 9933191217 | 9933191217 | 1983-06-17   | 2024-03-16      | 2034-03-16    | B,B1,M                     |
|    4 | 9935088310 | 9935088310 | 1976-12-04   | 2024-04-09      | 2034-04-09    | B,B1,C,C1,D,D1,M           |
|    5 | 9933191218 | 9933191218 | 1975-12-12   | 2024-03-16      | 2034-03-16    | B,B1                       |
|    6 | 9933191219 | 9933191219 | 1987-09-23   | 2024-03-16      | 2034-03-16    | A,A1,B,B1,M                |
|    7 | 9935088311 | 9935088311 | 1983-11-26   | 2024-04-09      | 2034-04-09    | B,B1,M                     |
|    8 | 9933191220 | 9933191220 | 1983-01-08   | 2024-03-16      | 2031-11-13    | B,B1,M                     |
|    9 | 9932079710 | 9932079710 | 1989-01-09   | 2024-03-09      | 2034-03-09    | B,B1,C,C1,M                |
|   10 | 9933191221 | 9933191221 | 2006-03-05   | 2024-03-16      | 2034-03-16    | B,B1                       |
|   11 | 9935088312 | 9935088312 | 1996-10-03   | 2024-04-09      | 2034-04-09    | B,B1,M                     |
|   12 | 9932079711 | 9932079711 | 1987-07-23   | 2024-03-09      | 2034-03-09    | B,B1,M                     |
|   13 | 9935088313 | 9935088313 | 1962-11-17   | 2024-04-09      | 2034-04-09    | A,A1,B,B1,C,C1,M           |
|   14 | 9935088306 | 9935088306 | 1985-01-02   | 2024-04-09      | 2034-04-09    | A,A1,B,B1,C,C1,M           |
|   15 | 9932079706 | 9932079706 | 2002-01-02   | 2024-03-09      | 2034-03-09    | B,B1,M                     |
|   16 | 9923778157 | 9923778157 | 2001-12-10   | 2024-04-03      | 2034-04-03    | B,B1,M                     |
|   17 | 9938084211 | 9938084211 | 1969-07-15   | 2024-01-23      | 2034-01-23    | B,B1,C,C1,C1E,CE,M         |
|   18 | 9935088307 | 9935088307 | 1960-03-10   | 2024-04-09      | 2034-04-09    | B,B1,M                     |
|   19 | 9936055845 | 9936055845 | 1994-03-23   | 2024-02-14      | 2034-02-14    | B,B1,C,C1,M                |
|   20 | 9923779000 | 9923779000 | 1984-08-04   | 2024-07-04      | 2034-07-04    | A,A1,B,B1,M                |
```


## About final data
> - Total rows: 58393

### Schema
```
root
 |-- birth_date: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)

```



### Data sample
```
| birth_date   | documents                                                                                                                 |
|:-------------|:--------------------------------------------------------------------------------------------------------------------------|
| 17.07.1992   | [Row(type=3, serial='9935088309', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 30.01.1964   | [Row(type=3, serial='9932079709', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 17.06.1983   | [Row(type=3, serial='9933191217', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 04.12.1976   | [Row(type=3, serial='9935088310', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 12.12.1975   | [Row(type=3, serial='9933191218', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 23.09.1987   | [Row(type=3, serial='9933191219', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 26.11.1983   | [Row(type=3, serial='9935088311', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 08.01.1983   | [Row(type=3, serial='9933191220', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 09.01.1989   | [Row(type=3, serial='9932079710', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 05.03.2006   | [Row(type=3, serial='9933191221', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 03.10.1996   | [Row(type=3, serial='9935088312', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 23.07.1987   | [Row(type=3, serial='9932079711', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 17.11.1962   | [Row(type=3, serial='9935088313', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 02.01.1985   | [Row(type=3, serial='9935088306', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 02.01.2002   | [Row(type=3, serial='9932079706', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 10.12.2001   | [Row(type=3, serial='9923778157', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 15.07.1969   | [Row(type=3, serial='9938084211', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 10.03.1960   | [Row(type=3, serial='9935088307', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 23.03.1994   | [Row(type=3, serial='9936055845', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| 04.08.1984   | [Row(type=3, serial='9923779000', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
```