# Parsetron results

## About row data

> - Code name: index_0146
> - File path: rpn.gov.ru_28K.csv
> - Total rows: 28671

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- esia_oid: integer (nullable = true)
 |-- full_name: string (nullable = true)
 |-- surname: string (nullable = true)
 |-- name: string (nullable = true)
 |-- patronymic: string (nullable = true)
 |-- passport: long (nullable = true)
 |-- inn: long (nullable = true)
 |-- email: string (nullable = true)
 |-- email_verified_at: timestamp (nullable = true)
 |-- remember_token: string (nullable = true)
 |-- created_at: timestamp (nullable = true)
 |-- updated_at: timestamp (nullable = true)
 |-- deleted_at: string (nullable = true)
 |-- snils: string (nullable = true)
 |-- passport_issuer: string (nullable = true)
 |-- passport_issue_date: timestamp (nullable = true)
 |-- address_line: string (nullable = true)
 |-- address_index: string (nullable = true)
 |-- address_oktmo: integer (nullable = true)
 |-- tel: string (nullable = true)
 |-- fax: string (nullable = true)
 |-- is_esia_trusted: boolean (nullable = true)

```

### Data sample
```
|     id |         esia_oid | full_name                         | surname     | name                      | patronymic    |   passport |           inn | email                         | email_verified_at   | remember_token                                               | created_at          | updated_at          | deleted_at   |       snils | passport_issuer   | passport_issue_date   | address_line   | address_index   |   address_oktmo | tel   | fax   | is_esia_trusted   |
|-------:|-----------------:|:----------------------------------|:------------|:--------------------------|:--------------|-----------:|--------------:|:------------------------------|:--------------------|:-------------------------------------------------------------|:--------------------|:--------------------|:-------------|------------:|:------------------|:----------------------|:---------------|:----------------|----------------:|:------|:------|:------------------|
| 356725 |      1.03979e+09 | Тюлюкин Михаил Валерьевич         | Тюлюкин     | Михаил                    | Валерьевич    |        nan | nan           | autofanpenza@mail.ru          | NaT                 |                                                              | 2022-01-17 10:33:32 | 2023-01-18 09:34:39 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356702 |      1.0046e+09  | Калинина Ольга Александровна      | Калинина    | Ольга                     | Александровна |        nan | nan           | olya-kalinina@mail.ru         | NaT                 |                                                              | 2022-01-17 10:29:20 | 2022-12-26 11:41:59 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356714 |      1.08758e+09 | Васильев Анатолий Петрович        | Васильев    | Анатолий                  | Петрович      |        nan | nan           | dorohovoomz@mail.ru           | 2022-01-17 10:59:00 |                                                              | 2022-01-17 10:31:52 | 2022-01-17 10:59:00 |              |             |                   | NaT                   |                |                 |             nan |       |       | False             |
| 356700 |      1.02693e+09 | Юрасова Елена Вячеславовна        | Юрасова     | Елена                     | Вячеславовна  |        nan | nan           | yurasovaa@yandex.ru           | NaT                 |                                                              | 2022-01-17 10:29:02 | 2023-01-30 09:34:08 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356735 |      1.01696e+09 | ГРЕЧИШНИКОВ ВИКТОР НИКОЛАЕВИЧ     | ГРЕЧИШНИКОВ | ВИКТОР                    | НИКОЛАЕВИЧ    |        nan | nan           | tarlykov_aa@mail.ru           | 2022-01-17 10:38:19 |                                                              | 2022-01-17 10:35:17 | 2023-01-23 09:25:24 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356703 | 136377           | Литвиненков Максим Александрович  | Литвиненков | Максим                    | Александрович |        nan | nan           | lit_max@mail.ru               | NaT                 |                                                              | 2022-01-17 10:29:25 | 2022-01-17 10:29:25 |              |             |                   | NaT                   |                |                 |             nan |       |       | False             |
| 356724 |      2.46014e+08 | ЧЕКРЫШОВ ВЛАДИМИР АЛЕКСАНДРОВИЧ   | ЧЕКРЫШОВ    | ВЛАДИМИР                  | АЛЕКСАНДРОВИЧ |        nan | nan           | tchekrychov@rambler.ru        | NaT                 |                                                              | 2022-01-17 10:33:31 | 2024-01-16 15:10:21 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356713 |      1.06085e+09 | Корнилаева Татьяна Вячеславовна   | Корнилаева  | Татьяна                   | Вячеславовна  |        nan |   5.26102e+11 | school32-nnov@yandex.ru       | NaT                 |                                                              | 2022-01-17 10:31:41 | 2024-02-02 13:34:18 |              | 00648686368 |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356734 |      1.00276e+09 | Гизаткулов Камиль Инсафович       | Гизаткулов  | Камиль                    | Инсафович     |        nan | nan           | gizkamin@yandex.ru            | NaT                 |                                                              | 2022-01-17 10:35:17 | 2022-01-17 10:35:18 |              |             |                   | NaT                   |                |                 |             nan |       |       | False             |
| 356723 |    nan           | Пузакова Татьяна Александровна    | Пузакова    | Татьяна                   | Александровна |        nan | nan           | mdou215@yandex.ru             | 2022-01-17 10:34:20 | UNMysupFCQONqeELfWCYfQCvzAs2Bf53xMuO24XBkuYmMiECz7C6vSjPzmOA | 2022-01-17 10:33:31 | 2023-06-28 11:01:16 |              |             |                   | NaT                   |                |                 |             nan |       |       | False             |
| 356712 |      2.46694e+08 | Жабрева Людмила Васильевна        | Жабрева     | Людмила                   | Васильевна    |        nan | nan           | zhabrevalv@mail.ru            | NaT                 |                                                              | 2022-01-17 10:31:35 | 2022-01-17 10:31:35 |              |             |                   | NaT                   |                |                 |             nan |       |       | False             |
| 356733 |      1.12694e+09 | Голубков Илья Андреевич           | Голубков    | Илья                      | Андреевич     |        nan | nan           | igolubkov@kineshma.ru         | NaT                 |                                                              | 2022-01-17 10:35:07 | 2023-01-19 08:16:22 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356722 |    nan           | Ускова Татьяна Викторовна         |             | Ускова Татьяна Викторовна |               |        nan | nan           | apexdir@mail.ru               | NaT                 |                                                              | 2022-01-17 10:33:29 | 2022-01-17 10:33:29 |              |             |                   | NaT                   |                |                 |             nan |       |       | False             |
| 356711 | 199043           | Шилов Олег Александрович          | Шилов       | Олег                      | Александрович |        nan | nan           | olegkmz@mail.ru               | NaT                 |                                                              | 2022-01-17 10:31:18 | 2023-01-20 17:31:08 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356732 |      1.00823e+09 | Севастьянов Владимир Олегович     | Севастьянов | Владимир                  | Олегович      |        nan | nan           | krista.ahtubinsk@gmail.com    | 2022-01-17 10:35:42 |                                                              | 2022-01-17 10:34:36 | 2023-01-17 07:14:47 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356721 |      1.00972e+09 | Ведяшкин Игорь Владимирович       | Ведяшкин    | Игорь                     | Владимирович  |        nan | nan           | igorvedyashkin40@yandex.ru    | 2022-01-17 10:37:35 |                                                              | 2022-01-17 10:33:18 | 2022-12-26 15:05:59 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356710 |      1.04861e+09 | Двуглазова Алена Геннадьевна      | Двуглазова  | Алена                     | Геннадьевна   |        nan | nan           | dvuglazova.ddt@yandex.ru      | NaT                 |                                                              | 2022-01-17 10:31:18 | 2023-03-13 09:56:40 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356731 |    nan           | Алябьев Сергей Викторович         | Алябьев     | Сергей                    | Викторович    |        nan | nan           | alyabjev.serguei@yandex.ru    | 2022-01-17 10:35:23 |                                                              | 2022-01-17 10:34:32 | 2022-01-17 10:35:23 |              |             |                   | NaT                   |                |                 |             nan |       |       | False             |
| 356741 |      1.0173e+09  | ПШЕНИЧНИКОВ ЕВГЕНИЙ АЛЕКСАНДРОВИЧ | ПШЕНИЧНИКОВ | ЕВГЕНИЙ                   | АЛЕКСАНДРОВИЧ |        nan | nan           | pshenichnikov1987@internet.ru | NaT                 |                                                              | 2022-01-17 10:35:49 | 2024-01-19 13:01:40 |              |             |                   | NaT                   |                |                 |             nan |       |       | True              |
| 356720 |      1.00612e+09 | Маршавин Сергей Иванович          | Маршавин    | Сергей                    | Иванович      |        nan |   3.628e+11   | marshavin64@mail.ru           | NaT                 |                                                              | 2022-01-17 10:33:07 | 2023-01-25 10:12:14 |              | 07430347746 |                   | NaT                   |                |                 |             nan |       |       | True              |
```


## About final data
> - Total rows: 25758

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
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

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.50% |
| Address | 3.35% |
| Phones | 3.38% |
| Documents | 5.00% |



### Data sample
```
| names                                 | emails                            | address   | phones   | documents                                                                                                                                                                                                                                             |
|:--------------------------------------|:----------------------------------|:----------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Тюлюкин Михаил Валерьевич']         | ['autofanpenza@mail.ru']          |           |          |                                                                                                                                                                                                                                                       |
| ['Калинина Ольга Александровна']      | ['olya-kalinina@mail.ru']         |           |          |                                                                                                                                                                                                                                                       |
| ['Васильев Анатолий Петрович']        | ['dorohovoomz@mail.ru']           |           |          |                                                                                                                                                                                                                                                       |
| ['Юрасова Елена Вячеславовна']        | ['yurasovaa@yandex.ru']           |           |          |                                                                                                                                                                                                                                                       |
| ['Гречишников Виктор Николаевич']     | ['tarlykov_aa@mail.ru']           |           |          |                                                                                                                                                                                                                                                       |
| ['Литвиненков Максим Александрович']  | ['lit_max@mail.ru']               |           |          |                                                                                                                                                                                                                                                       |
| ['Чекрышов Владимир Александрович']   | ['tchekrychov@rambler.ru']        |           |          |                                                                                                                                                                                                                                                       |
| ['Корнилаева Татьяна Вячеславовна']   | ['school32-nnov@yandex.ru']       |           |          | [Row(type=1, serial='526102407924', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='00648686368', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| ['Гизаткулов Камиль Инсафович']       | ['gizkamin@yandex.ru']            |           |          |                                                                                                                                                                                                                                                       |
| ['Пузакова Татьяна Александровна']    | ['mdou215@yandex.ru']             |           |          |                                                                                                                                                                                                                                                       |
| ['Жабрева Людмила Васильевна']        | ['zhabrevalv@mail.ru']            |           |          |                                                                                                                                                                                                                                                       |
| ['Голубков Илья Андреевич']           | ['igolubkov@kineshma.ru']         |           |          |                                                                                                                                                                                                                                                       |
| ['Ускова Татьяна Викторовна']         | ['apexdir@mail.ru']               |           |          |                                                                                                                                                                                                                                                       |
| ['Шилов Олег Александрович']          | ['olegkmz@mail.ru']               |           |          |                                                                                                                                                                                                                                                       |
| ['Севастьянов Владимир Олегович']     | ['krista.ahtubinsk@gmail.com']    |           |          |                                                                                                                                                                                                                                                       |
| ['Ведяшкин Игорь Владимирович']       | ['igorvedyashkin40@yandex.ru']    |           |          |                                                                                                                                                                                                                                                       |
| ['Двуглазова Алена Геннадьевна']      | ['dvuglazova.ddt@yandex.ru']      |           |          |                                                                                                                                                                                                                                                       |
| ['Алябьев Сергей Викторович']         | ['alyabjev.serguei@yandex.ru']    |           |          |                                                                                                                                                                                                                                                       |
| ['Пшеничников Евгений Александрович'] | ['pshenichnikov1987@internet.ru'] |           |          |                                                                                                                                                                                                                                                       |
| ['Маршавин Сергей Иванович']          | ['marshavin64@mail.ru']           |           |          | [Row(type=1, serial='362800000257', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='07430347746', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
```