# Parsetron results

## About row data

> - Code name: index_0072
> - File path: infoflot_preprocessed.csv
> - Total rows: 2029073

### Schema
```
root
 |-- passenger_id: string (nullable = true)
 |-- user_id: integer (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- birthday: integer (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- address_legal: string (nullable = true)
 |-- address_home: string (nullable = true)
 |-- passport_series: string (nullable = true)
 |-- passport_number: string (nullable = true)
 |-- passenger_data: string (nullable = true)
 |-- passenger_children: string (nullable = true)
 |-- passenger_parent_data: string (nullable = true)
 |-- passenger_files: string (nullable = true)
 |-- passenger_bonus_card: string (nullable = true)

```

### Data sample
```
|   passenger_id |   user_id | first_name   | last_name   | middle_name   |      birthday | email   | phone   | address_legal   | address_home   | passport_series   |   passport_number | passenger_data                                                                                                                                                                                                                                                                                                                                                                                              | passenger_children                                                                                | passenger_parent_data                                                                                   | passenger_files                                                                                                            |   passenger_bonus_card |
|---------------:|----------:|:-------------|:------------|:--------------|--------------:|:--------|:--------|:----------------|:---------------|:------------------|------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|-----------------------:|
|          38834 |         0 |              | тест        |               | nan           |         |         |                 |                |                   |                   | a:6:{s:10:\"first_name\";s:0:\"\";s:11:\"middle_name\";s:0:\"\";s:9:\"last_name\";s:8:\"тест\";s:15:\"passport_series\";s:0:\"\";s:15:\"passport_number\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                                                                                                                                                                                                              | a:3:{s:4:\"name\";s:0:\"\";s:8:\"document\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                  |                                                                                                         |                                                                                                                            |                        |
|          38835 |         0 |              |             |               | nan           |         |         |                 |                |                   |                   | a:6:{s:10:\"first_name\";s:0:\"\";s:11:\"middle_name\";s:0:\"\";s:9:\"last_name\";s:0:\"\";s:15:\"passport_series\";s:0:\"\";s:15:\"passport_number\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                                                                                                                                                                                                                  | a:3:{s:4:\"name\";s:0:\"\";s:8:\"document\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                  |                                                                                                         |                                                                                                                            |                        |
|          38991 |         0 | Сергей       | Дунаев      | Петрович      | nan           |         |         |                 |                | 4606              |            491007 | a:6:{s:10:\"first_name\";s:12:\"Сергей\";s:11:\"middle_name\";s:16:\"Петрович\";s:9:\"last_name\";s:12:\"Дунаев\";s:15:\"passport_series\";s:4:\"4606\";s:15:\"passport_number\";s:6:\"491007\";s:8:\"birthday\";s:8:\"24.12.58\";}                                                                                                                                                                         | a:3:{s:4:\"name\";s:0:\"\";s:8:\"document\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                  | a:3:{s:10:\"cabin_name\";s:3:\"202\";s:9:\"type_name\";s:3:\"А2\";s:9:\"deck_name\";s:14:\"Средняя\";}  |                                                                                                                            |                        |
|          38992 |         0 | Наталья      | Дунаева     | Николаевна    |   2.45624e+08 |         |         |                 |                | 9400              |            120404 | a:11:{s:10:\"first_name\";s:14:\"Наталья\";s:11:\"middle_name\";s:20:\"Николаевна\";s:9:\"last_name\";s:14:\"Дунаева\";s:15:\"passport_series\";s:4:\"9400\";s:15:\"passport_number\";s:6:\"120404\";s:15:\"passport_issued\";s:0:\"\";s:20:\"passport_issued_date\";s:0:\"\";s:17:\"passport_end_date\";s:0:\"\";s:11:\"citizenship\";s:0:\"\";s:6:\"gender\";s:0:\"\";s:8:\"birthday\";s:8:\"14.10.77\";} | a:4:{s:4:\"name\";s:0:\"\";s:8:\"document\";s:0:\"\";s:8:\"birthday\";s:0:\"\";s:4:\"meal\";i:0;} | a:3:{s:10:\"cabin_name\";s:0:\"\";s:9:\"type_name\";s:0:\"\";s:9:\"deck_name\";s:0:\"\";}               | a:1:{s:12:\"confirmation\";a:4:{s:4:\"name\";s:0:\"\";s:4:\"path\";s:0:\"\";s:4:\"type\";s:0:\"\";s:4:\"size\";s:0:\"\";}} |                 000000 |
|          38995 |         0 | Надежда      | Фисун       | Аркадьевна    | nan           |         |         |                 |                | 9405              |            639656 | a:6:{s:10:\"first_name\";s:14:\"Надежда\";s:11:\"middle_name\";s:20:\"Аркадьевна\";s:9:\"last_name\";s:10:\"Фисун\";s:15:\"passport_series\";s:4:\"9405\";s:15:\"passport_number\";s:6:\"639656\";s:8:\"birthday\";s:8:\"11.07.55\";}                                                                                                                                                                       | a:3:{s:4:\"name\";s:0:\"\";s:8:\"document\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                  | a:3:{s:10:\"cabin_name\";s:3:\"233\";s:9:\"type_name\";s:5:\"Б2к\";s:9:\"deck_name\";s:14:\"Средняя\";} |                                                                                                                            |                        |
|          38996 |         0 | Тимур        | Дунаев      | Сергеевич     | nan           |         |         |                 |                | IИК               |            757433 | a:6:{s:10:\"first_name\";s:10:\"Тимур\";s:11:\"middle_name\";s:18:\"Сергеевич\";s:9:\"last_name\";s:12:\"Дунаев\";s:15:\"passport_series\";s:5:\"IИК\";s:15:\"passport_number\";s:6:\"757433\";s:8:\"birthday\";s:8:\"13.02.03\";}                                                                                                                                                                          | a:3:{s:4:\"name\";s:0:\"\";s:8:\"document\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                  |                                                                                                         |                                                                                                                            |                        |
|          39017 |    107379 | Владимир     | Петровицкий | Александрович | nan           |         |         |                 |                | 4508              |            814380 | a:6:{s:10:\"first_name\";s:16:\"Владимир\";s:11:\"middle_name\";s:26:\"Александрович\";s:9:\"last_name\";s:22:\"Петровицкий\";s:15:\"passport_series\";s:4:\"4508\";s:15:\"passport_number\";s:6:\"814380\";s:8:\"birthday\";s:0:\"\";}                                                                                                                                                                     | a:3:{s:4:\"name\";s:0:\"\";s:8:\"document\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                  |                                                                                                         |                                                                                                                            |                 079798 |
|          39018 |    107380 | Людмила      | Петровицкая | Ивановна      | nan           |         |         |                 |                | 4508              |            814388 | a:6:{s:10:\"first_name\";s:14:\"Людмила\";s:11:\"middle_name\";s:16:\"Ивановна\";s:9:\"last_name\";s:22:\"Петровицкая\";s:15:\"passport_series\";s:4:\"4508\";s:15:\"passport_number\";s:6:\"814388\";s:8:\"birthday\";s:0:\"\";}                                                                                                                                                                           | a:3:{s:4:\"name\";s:0:\"\";s:8:\"document\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                  |                                                                                                         |                                                                                                                            |                 079799 |
|          39021 |     53773 | Ирина        | Кондрацкая  | Владимировна  | nan           |         |         |                 |                | 4504              |            508442 | a:6:{s:10:\"first_name\";s:10:\"Ирина\";s:11:\"middle_name\";s:24:\"Владимировна\";s:9:\"last_name\";s:20:\"Кондрацкая\";s:15:\"passport_series\";s:4:\"4504\";s:15:\"passport_number\";s:6:\"508442\";s:8:\"birthday\";s:0:\"\";}                                                                                                                                                                          | a:3:{s:4:\"name\";s:0:\"\";s:8:\"document\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                  |                                                                                                         |                                                                                                                            |                 053634 |
|          39022 |         0 | Нина         | Тарасова    | Георгиевна    | nan           |         |         |                 |                | 4601              |            110321 | a:6:{s:10:\"first_name\";s:8:\"Нина\";s:11:\"middle_name\";s:20:\"Георгиевна\";s:9:\"last_name\";s:16:\"Тарасова\";s:15:\"passport_series\";s:4:\"4601\";s:15:\"passport_number\";s:6:\"110321\";s:8:\"birthday\";s:0:\"\";}                                                                                                                                                                                | a:3:{s:4:\"name\";s:0:\"\";s:8:\"document\";s:0:\"\";s:8:\"birthday\";s:0:\"\";}                  |                                                                                                         |                                                                                                                            |                        |
```


## About final data
> - Total rows: 968499

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Data sample
```
| names                                  | address   | emails   | phones   | birth_date   | documents                                                                                                                 | accounts   |
|:---------------------------------------|:----------|:---------|:---------|:-------------|:--------------------------------------------------------------------------------------------------------------------------|:-----------|
| ['Дунаев Сергей Петрович']             |           |          |          |              | [Row(type=0, serial='4606491007', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |            |
| ['Дунаева Наталья Николаевна']         |           |          |          | 13.10.1977   | [Row(type=0, serial='9400120404', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |            |
| ['Фисун Надежда Аркадьевна']           |           |          |          |              | [Row(type=0, serial='9405639656', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |            |
| ['Дунаев Тимур Сергеевич']             |           |          |          |              | [Row(type=5, serial='IИК757433', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]  |            |
| ['Петровицкий Владимир Александрович'] |           |          |          |              | [Row(type=0, serial='4508814380', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |            |
| ['Петровицкая Людмила Ивановна']       |           |          |          |              | [Row(type=0, serial='4508814388', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |            |
| ['Кондрацкая Ирина Владимировна']      |           |          |          |              | [Row(type=0, serial='4504508442', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |            |
| ['Тарасова Нина Георгиевна']           |           |          |          |              | [Row(type=0, serial='4601110321', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |            |
| ['Михеева Кристина Дмитриевна']        |           |          |          |              | [Row(type=0, serial='4608380192', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |            |
| ['Садкова Еленаниколаевна']            |           |          |          |              | [Row(type=0, serial='4504968919', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |            |
```