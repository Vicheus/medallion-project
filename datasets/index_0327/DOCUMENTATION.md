# Parsetron results

## About row data

> - File path: EGRUL_2022_2024.txt
> - Total rows: 33824086

### Schema
```
root
 |-- inn: long (nullable = true)
 |-- last_name: string (nullable = true)
 |-- name: string (nullable = true)
 |-- patronymic: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- ogrnip: long (nullable = true)
 |-- reg_date: string (nullable = true)
 |-- updated_at_num: integer (nullable = true)
 |-- status: integer (nullable = true)
 |-- end_date: string (nullable = true)
 |-- okved_id: integer (nullable = true)
 |-- tax_office_id: integer (nullable = true)
 |-- email: string (nullable = true)
 |-- pfr: long (nullable = true)
 |-- fss: long (nullable = true)
 |-- citizenship_type: integer (nullable = true)
 |-- country_code: integer (nullable = true)

```

### Data sample
```
|         inn | last_name   | name                 | patronymic    |   sex |          ogrnip | reg_date   |   updated_at_num |   status | end_date   |   okved_id |   tax_office_id | email                  |         pfr |   fss |   citizenship_type |   country_code |
|------------:|:------------|:---------------------|:--------------|------:|----------------:|:-----------|-----------------:|---------:|:-----------|-----------:|----------------:|:-----------------------|------------:|------:|-------------------:|---------------:|
|           0 | Токтаров    | Мадияр               |               |     1 | 322774600175399 | 2022-03-15 |            11375 |        0 | 0000-00-00 |       4547 |            7746 |                        |           0 |     0 |                  2 |            398 |
| 10000021695 | Тарраф      | Хедер Имад           |               |     1 | 321010000002435 | 2021-11-23 |            11299 |        0 | 0000-00-00 |       3634 |             100 | KHEDER@INTERNET.RU     |  1001091666 |     0 |                  2 |            760 |
| 10000057878 | Зарифи      | Аджмир               |               |     1 | 321010000002825 | 2021-11-25 |            11298 |        0 | 0000-00-00 |       3771 |             100 |                        |  1005058645 |     0 |                  2 |              4 |
| 10000077384 | ШАРМАТ      | НААЛА                | ЗАБЕЕВНА      |     2 |               0 | 0000-00-00 |                0 |        0 | 0000-00-00 |          0 |               0 |                        |           0 |     0 |                  0 |              0 |
| 10000077521 | Гейтс       | Лиза Тайе            |               |     0 |               0 | 0000-00-00 |                0 |        0 | 0000-00-00 |          0 |               0 |                        |           0 |     0 |                  0 |              0 |
| 10000081535 | Парфенова   | Вера                 | Викторовна    |     2 | 304450836500040 | 2004-12-30 |            11297 |      201 | 2005-02-04 |        226 |            4508 |                        | 55121001380 |     0 |                  1 |              0 |
| 10000096796 | Королев     | Валерий              | Алексеевич    |     1 | 305682711000271 | 2005-04-20 |            11300 |      501 | 2005-01-01 |          0 |            6820 |                        |           0 |     0 |                  1 |              0 |
| 10000125126 | ИШБЕКОВ     | ЗАФАР                | ИСКАНДАРОВИЧ  |     1 |               0 | 0000-00-00 |                0 |        0 | 0000-00-00 |          0 |               0 |                        |           0 |     0 |                  0 |              0 |
| 10000133303 | Раздорская  | Нина                 | Борисовна     |     2 | 305682713100105 | 2005-05-11 |            11300 |      501 | 2005-01-01 |          0 |            6820 |                        |           0 |     0 |                  1 |              0 |
| 10000143975 | Торчуа      | Диана                | Одиковна      |     2 |               0 | 0000-00-00 |                0 |        0 | 0000-00-00 |          0 |               0 |                        |           0 |     0 |                  0 |              0 |
| 10000144070 | Фролова     | Светлана             | Викторовна    |     2 |               0 | 0000-00-00 |                0 |        0 | 0000-00-00 |          0 |               0 |                        |           0 |     0 |                  0 |              0 |
| 10000145595 | Чамагуа     | Лаура                | Амерановна    |     2 |               0 | 0000-00-00 |                0 |        0 | 0000-00-00 |          0 |               0 |                        |           0 |     0 |                  0 |              0 |
| 10000151750 | Плиев       | Феликс               | Александрович |     1 | 322010000002050 | 2022-01-26 |            11322 |        0 | 0000-00-00 |       3804 |             100 | PLIEVKFAF@YANDEX.RU    |  1006066829 |     0 |                  1 |              0 |
| 10000220203 | Юрцова      | Татьяна Владимировна |               |     2 | 322010000003327 | 2022-02-07 |            11335 |        0 | 0000-00-00 |       4509 |             100 | LIDERLIDEROV@GMAIL.COM |           0 |     0 |                  2 |            112 |
| 10060101578 | ТРАХОВ      | АСЛАН                | МАХМУДОВИЧ    |     1 |               0 | 0000-00-00 |                0 |        0 | 0000-00-00 |          0 |               0 |                        |           0 |     0 |                  0 |              0 |
| 10100000265 | Мазовка     | Наталья              | Васильевна    |     2 | 304010125000076 | 2004-09-06 |            11298 |      201 | 2010-04-22 |       1241 |             100 |                        |           0 |     0 |                  1 |              0 |
| 10100000339 | Симоненко   | Виталий              | Васильевич    |     1 | 305010128300020 | 2005-10-10 |            11298 |      201 | 2006-03-23 |       1324 |             100 |                        |           0 |     0 |                  1 |              0 |
| 10100000586 | Крылова     | Надежда              | Пантелеевна   |     2 | 304010130600280 | 2004-11-01 |            11298 |      201 | 2007-01-28 |       1319 |             100 |                        |           0 |     0 |                  1 |              0 |
| 10100000650 | Комисарова  | Светлана             | Николаевна    |     2 | 305010100105686 | 2005-01-01 |            11298 |      501 | 2005-01-01 |          0 |             100 |                        |           0 |     0 |                  1 |              0 |
| 10100001075 | Масцеев     | Сергей               | Юрьевич       |     1 | 306233921400030 | 2006-08-02 |            11167 |      201 | 2015-10-28 |       1056 |            2375 |                        | 33041014915 |     0 |                  1 |              0 |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- actuality: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```



### Data sample
```
| names                              |   sex | emails                     | documents                                                                                                                   | actuality   | raw_metadata                                                                                                                                                                      |
|:-----------------------------------|------:|:---------------------------|:----------------------------------------------------------------------------------------------------------------------------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Тарраф Хедер Имад']              |     1 | ['kheder@internet.ru']     | [Row(type=1, serial='010000021695', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             | ['{"reg_date": "2021-11-23", "status": "0", "end_date": "0000-00-00", "okved_id": "3634", "tax_office_id": "100", "pfr": "1001091666", "fss": "0", "citizenship_type": "2"}']     |
| ['Зарифи Аджмир']                  |     1 |                            | [Row(type=1, serial='010000057878', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             | ['{"reg_date": "2021-11-25", "status": "0", "end_date": "0000-00-00", "okved_id": "3771", "tax_office_id": "100", "pfr": "1005058645", "fss": "0", "citizenship_type": "2"}']     |
| ['Шармат Наала Забеевна']          |   nan |                            | [Row(type=1, serial='010000077384', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             | ['{"reg_date": "0000-00-00", "status": "0", "end_date": "0000-00-00", "okved_id": "0", "tax_office_id": "0", "pfr": "0", "fss": "0", "citizenship_type": "0"}']                   |
| ['Гейтс Лиза Тайе']                |     0 |                            | [Row(type=1, serial='010000077521', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             | ['{"reg_date": "0000-00-00", "status": "0", "end_date": "0000-00-00", "okved_id": "0", "tax_office_id": "0", "pfr": "0", "fss": "0", "citizenship_type": "0"}']                   |
| ['Парфенова Вера Викторовна']      |   nan |                            | [Row(type=1, serial='010000081535', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | 04.02.2005  | ['{"reg_date": "2004-12-30", "status": "201", "end_date": "2005-02-04", "okved_id": "226", "tax_office_id": "4508", "pfr": "55121001380", "fss": "0", "citizenship_type": "1"}']  |
| ['Королев Валерий Алексеевич']     |     1 |                            | [Row(type=1, serial='010000096796', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | 01.01.2005  | ['{"reg_date": "2005-04-20", "status": "501", "end_date": "2005-01-01", "okved_id": "0", "tax_office_id": "6820", "pfr": "0", "fss": "0", "citizenship_type": "1"}']              |
| ['Ишбеков Зафар Искандарович']     |     1 |                            | [Row(type=1, serial='010000125126', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             | ['{"reg_date": "0000-00-00", "status": "0", "end_date": "0000-00-00", "okved_id": "0", "tax_office_id": "0", "pfr": "0", "fss": "0", "citizenship_type": "0"}']                   |
| ['Раздорская Нина Борисовна']      |   nan |                            | [Row(type=1, serial='010000133303', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | 01.01.2005  | ['{"reg_date": "2005-05-11", "status": "501", "end_date": "2005-01-01", "okved_id": "0", "tax_office_id": "6820", "pfr": "0", "fss": "0", "citizenship_type": "1"}']              |
| ['Торчуа Диана Одиковна']          |   nan |                            | [Row(type=1, serial='010000143975', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             | ['{"reg_date": "0000-00-00", "status": "0", "end_date": "0000-00-00", "okved_id": "0", "tax_office_id": "0", "pfr": "0", "fss": "0", "citizenship_type": "0"}']                   |
| ['Фролова Светлана Викторовна']    |   nan |                            | [Row(type=1, serial='010000144070', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             | ['{"reg_date": "0000-00-00", "status": "0", "end_date": "0000-00-00", "okved_id": "0", "tax_office_id": "0", "pfr": "0", "fss": "0", "citizenship_type": "0"}']                   |
| ['Чамагуа Лаура Амерановна']       |   nan |                            | [Row(type=1, serial='010000145595', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             | ['{"reg_date": "0000-00-00", "status": "0", "end_date": "0000-00-00", "okved_id": "0", "tax_office_id": "0", "pfr": "0", "fss": "0", "citizenship_type": "0"}']                   |
| ['Плиев Феликс Александрович']     |     1 | ['plievkfaf@yandex.ru']    | [Row(type=1, serial='010000151750', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             | ['{"reg_date": "2022-01-26", "status": "0", "end_date": "0000-00-00", "okved_id": "3804", "tax_office_id": "100", "pfr": "1006066829", "fss": "0", "citizenship_type": "1"}']     |
| ['Юрцова Татьяна Владимировна']    |   nan | ['liderliderov@gmail.com'] | [Row(type=1, serial='010000220203', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             | ['{"reg_date": "2022-02-07", "status": "0", "end_date": "0000-00-00", "okved_id": "4509", "tax_office_id": "100", "pfr": "0", "fss": "0", "citizenship_type": "2"}']              |
| ['Мазовка Наталья Васильевна']     |   nan |                            | [Row(type=1, serial='010100000265', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | 22.04.2010  | ['{"reg_date": "2004-09-06", "status": "201", "end_date": "2010-04-22", "okved_id": "1241", "tax_office_id": "100", "pfr": "0", "fss": "0", "citizenship_type": "1"}']            |
| ['Симоненко Виталий Васильевич']   |     1 |                            | [Row(type=1, serial='010100000339', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | 23.03.2006  | ['{"reg_date": "2005-10-10", "status": "201", "end_date": "2006-03-23", "okved_id": "1324", "tax_office_id": "100", "pfr": "0", "fss": "0", "citizenship_type": "1"}']            |
| ['Крылова Надежда Пантелеевна']    |   nan |                            | [Row(type=1, serial='010100000586', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | 28.01.2007  | ['{"reg_date": "2004-11-01", "status": "201", "end_date": "2007-01-28", "okved_id": "1319", "tax_office_id": "100", "pfr": "0", "fss": "0", "citizenship_type": "1"}']            |
| ['Комисарова Светлана Николаевна'] |   nan |                            | [Row(type=1, serial='010100000650', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | 01.01.2005  | ['{"reg_date": "2005-01-01", "status": "501", "end_date": "2005-01-01", "okved_id": "0", "tax_office_id": "100", "pfr": "0", "fss": "0", "citizenship_type": "1"}']               |
| ['Масцеев Сергей Юрьевич']         |     1 |                            | [Row(type=1, serial='010100001075', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | 28.10.2015  | ['{"reg_date": "2006-08-02", "status": "201", "end_date": "2015-10-28", "okved_id": "1056", "tax_office_id": "2375", "pfr": "33041014915", "fss": "0", "citizenship_type": "1"}'] |
| ['Тютюнькова Тамара Ивановна']     |   nan |                            | [Row(type=1, serial='010100001212', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | 29.05.2014  | ['{"reg_date": "2004-06-25", "status": "201", "end_date": "2014-05-29", "okved_id": "1285", "tax_office_id": "100", "pfr": "0", "fss": "0", "citizenship_type": "1"}']            |
| ['Асманова Зоя Николаевна']        |   nan |                            | [Row(type=1, serial='010100001607', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | 12.12.2018  | ['{"reg_date": "2016-02-20", "status": "201", "end_date": "2018-12-12", "okved_id": "3760", "tax_office_id": "2375", "pfr": "33016109349", "fss": "0", "citizenship_type": "1"}'] |
```