# Parsetron results

## About row data

> - Code name: index_0108
> - File path: Sessions.csv
> - Total rows: 2767133

### Schema
```
root
 |-- Id: string (nullable = true)
 |-- ChangeDate: string (nullable = true)
 |-- CreateDate: string (nullable = true)
 |-- FirstName: string (nullable = true)
 |-- Inn: long (nullable = true)
 |-- LastName: string (nullable = true)
 |-- PassportNumber: integer (nullable = true)
 |-- PassportSeries: integer (nullable = true)
 |-- Patronymic: string (nullable = true)
 |-- Phone: long (nullable = true)
 |-- SmsCode: integer (nullable = true)
 |-- SmsMessageId: string (nullable = true)
 |-- Snils: long (nullable = true)
 |-- UpridCheckId: integer (nullable = true)
 |-- CheckOnlyPhone: boolean (nullable = true)
 |-- PersonVerified: boolean (nullable = true)
 |-- PhoneVerified: boolean (nullable = true)
 |-- PersonVerificationFinished: boolean (nullable = true)
 |-- PhoneVerificationFinished: boolean (nullable = true)
 |-- ClientId: string (nullable = true)
 |-- UpridError: string (nullable = true)
 |-- CallbackFinished: string (nullable = true)
 |-- CallbackUrl: string (nullable = true)
 |-- AttemptsToCheckSms: string (nullable = true)

```

### Data sample
```
| Id                                   | ChangeDate                    | CreateDate                    | FirstName   |   Inn | LastName       |   PassportNumber |   PassportSeries | Patronymic    |       Phone |   SmsCode |       SmsMessageId |       Snils |   UpridCheckId | CheckOnlyPhone   | PersonVerified   | PhoneVerified   | PersonVerificationFinished   | PhoneVerificationFinished   |   ClientId | UpridError   | CallbackFinished   | CallbackUrl   |   AttemptsToCheckSms |
|:-------------------------------------|:------------------------------|:------------------------------|:------------|------:|:---------------|-----------------:|-----------------:|:--------------|------------:|----------:|-------------------:|------------:|---------------:|:-----------------|:-----------------|:----------------|:-----------------------------|:----------------------------|-----------:|:-------------|:-------------------|:--------------|---------------------:|
| 7e4a37a1-0427-400b-a017-ff13994e3d5e | 2020-11-06 12:42:26.928 +0300 | 2020-11-06 12:42:19.356 +0300 | Ольга       |   nan | Мисурагина     |           768929 |             6513 | Сергеевна     | 79193922966 |      1993 | 870826392604901460 | 15199484203 |         875534 | False            | True             | True            | True                         | True                        |     018462 |              | false              |               |                    0 |
| 397722a3-b3d5-4c1d-8c87-209bcb2d0697 | 2020-11-06 12:37:46.829 +0300 | 2020-11-06 12:37:19.700 +0300 | Дмитрий     |   nan | Плиско         |           150668 |             2707 | Михайлович    | 79097794543 |      4209 | 870825750507290645 | 14192438759 |         875468 | False            | True             | True            | True                         | True                        |     001399 |              | false              |               |                    0 |
| a109f8c7-f7ff-439d-bef8-4b5321e96640 | 2020-11-06 12:39:57.095 +0300 | 2020-11-06 12:37:17.908 +0300 | Дмитрий     |   nan | Судоргин       |           552756 |             3713 | Олегович      | 79080092007 |      5971 | 870825746212323384 | 14973870416 |         875467 | False            | True             | True            | True                         | True                        |     018779 |              | false              |               |                    0 |
| 571caa81-0577-414e-a0bb-14855dd9148c | 2020-11-06 12:32:55.631 +0300 | 2020-11-06 12:30:34.850 +0300 | Лидия       |   nan | Харченко       |           471337 |             6500 | Александровна | 79022593325 |      2927 | 870824880776413236 |   872591662 |         875417 | False            | True             | True            | True                         | True                        |     001399 |              | false              |               |                    0 |
| 8ec8576b-4f14-40bb-ae94-5cc5d5e71224 | 2020-11-06 12:32:58.129 +0300 | 2020-11-06 12:32:37.184 +0300 | Алексей     |   nan | Анохин         |           295427 |             7011 | Владимирович  | 79534280515 |      3566 | 870825142769418272 | 10799102872 |         875435 | False            | True             | True            | True                         | True                        |     018779 |              | false              |               |                    0 |
| de4a2893-2801-420f-b10b-aca2b90af1f9 | 2020-11-06 12:28:59.646 +0300 | 2020-11-06 12:28:50.133 +0300 | Рена        |   nan | Исмайлова      |           934288 |             4620 | Фархадкызы    | 79778998151 |      6507 | 870824655290630201 | 19971182627 |         875406 | False            | False            | True            | True                         | True                        |     018462 |              | false              |               |                    0 |
| 3b969e86-91a2-42c9-98cf-e55c023e01ea | 2020-11-06 12:31:20.210 +0300 | 2020-11-06 12:31:08.740 +0300 | Маргарита   |   nan | Тайгунова      |           532330 |             8011 | Каримовна     | 79631371939 |      2360 | 870824953790857232 | 15103185513 |         875421 | False            | True             | True            | True                         | True                        |     018462 |              | false              |               |                    0 |
| cb094543-ae34-4cd3-8db2-ab3f5ca8e6e0 | 2020-11-06 12:38:01.514 +0300 | 2020-11-06 12:37:49.166 +0300 | Теймур      |   nan | Самыгин        |           343490 |             9212 | Александрович | 79520484759 |      9217 | 870825812784316471 | 14603938967 |         875473 | False            | True             | True            | True                         | True                        |     018462 |              | false              |               |                    0 |
| 3d60f1e6-21cc-4650-8aaa-3f9c70beb370 | 2020-11-06 12:29:24.938 +0300 | 2020-11-06 12:26:49.545 +0300 | Дмитрий     |   nan | Ковган         |           403881 |             4515 | Викторович    | 79997737801 |      9406 | 870824397592592385 | 13843477684 |         875388 | False            | True             | True            | True                         | True                        |     001399 |              | false              |               |                    0 |
| 26a30824-ad34-47d1-a037-d7679a4833d4 | 2020-11-06 12:35:26.123 +0300 | 2020-11-06 12:32:49.185 +0300 | Ренат       |   nan | Кисмаев        |           343648 |             5708 | Ростемович    | 79125924533 |      3000 | 870825168539222062 | 13696971925 |         875436 | False            | False            | True            | True                         | True                        |     001399 |              | false              |               |                    0 |
| 16fa96a4-080b-4b09-a32a-1e6ba2e51c9c | 2020-11-06 12:29:33.710 +0300 | 2020-11-06 12:29:13.274 +0300 | Алексей     |   nan | Терентьев      |            69052 |             6012 | Михайлович    | 79287631201 |      3958 | 870824704682754101 | 10184396943 |         875408 | False            | True             | True            | True                         | True                        |     018779 |              | false              |               |                    0 |
| 7b12d83c-798d-4403-b273-94d34bd0526c | 2020-11-06 12:29:53.924 +0300 | 2020-11-06 12:29:26.968 +0300 | Татьяна     |   nan | Зеленова       |           888523 |             8013 | Геннадьевна   | 79876270009 |      9569 | 870824734747525140 | 13772811272 |         875409 | False            | True             | True            | True                         | True                        |     018779 |              | false              |               |                    0 |
| 2a303b49-8dea-4951-94d8-663f7833a5f2 | 2020-11-06 12:36:28.892 +0300 | 2020-11-06 12:36:23.559 +0300 | Татьяна     |   nan | Баймуратова    |           940414 |             7112 | Борисовна     | 79123936839 |      7858 | 870825630248206337 |  7872536104 |         875463 | False            | True             |                 | True                         | False                       |     018779 |              | false              |               |                    5 |
| 5b85d947-7ba7-4a17-9c5b-411b05b64d08 | 2020-11-06 12:32:10.464 +0300 | 2020-11-06 12:30:56.082 +0300 | Станислав   |   nan | Белоцерковский |           980225 |             7020 | Викторови     | 79807297215 |       538 | 870824925873569831 | 18822802086 |         875420 | False            | False            | True            | True                         | True                        |     018779 |              | false              |               |                    0 |
| dca05774-d5e8-4b52-bf02-149dc562ec7c | 2020-11-06 12:46:58.582 +0300 | 2020-11-06 12:44:38.837 +0300 | Галина      |   nan | Шулаева        |           142682 |             2204 | Петровна      | 79503406323 |      9847 | 870826693252612128 |  2917218551 |         875554 | False            | True             | True            | True                         | True                        |     018462 |              | false              |               |                    0 |
| a0faa9ce-b541-489a-8601-2a7a12f5a8fe | 2020-11-06 12:32:24.048 +0300 | 2020-11-06 12:32:03.701 +0300 | Татьяна     |   nan | Зеленова       |           888523 |             8013 | Геннадьевна   | 79876270009 |      4209 | 870825071902457880 | 13772811272 |         875427 | False            | True             | True            | True                         | True                        |     018779 |              | false              |               |                    0 |
| 51c9bbc9-19be-4dee-a8bb-0c64ab022861 | 2020-11-06 12:30:55.275 +0300 | 2020-11-06 12:29:47.024 +0300 | Ильяс       |   nan | Алиев          |           609898 |             8713 | ИльясОглы     | 79042321124 |      7584 | 870824777697198131 | 15092860870 |         875410 | False            | False            | True            | True                         | True                        |     018779 |              | false              |               |                    0 |
| 4b3e6a4e-6cfc-465b-bbf8-263715d88274 | 2020-11-06 12:32:26.157 +0300 | 2020-11-06 12:32:01.758 +0300 | Анжела      |   nan | Кривошеина     |           317908 |             8619 | Сергеевна     | 79114062434 |      2991 | 870825067607490589 | 16426056861 |         875426 | False            | True             | True            | True                         | True                        |     001399 |              | false              |               |                    0 |
| fbd05017-bfd0-4ab2-ac36-5b58c2aee3c5 | 2020-11-06 12:43:01.705 +0300 | 2020-11-06 12:41:34.826 +0300 | Евгений     |   nan | Богдан         |           664307 |              820 | Михайлович    | 79141566253 |    784665 | 870826298115620893 |  5476170367 |         875523 | False            | True             | True            | True                         | True                        |     016445 |              | false              |               |                    0 |
| f8527e8b-ac31-4298-99f7-3508c3b128cd | 2020-11-06 12:38:44.822 +0300 | 2020-11-06 12:38:15.985 +0300 | Дмитрий     |   nan | Лаврухин       |           271449 |             1919 | Олегович      | 79517374868 |      7555 | 870825870766374970 |  7880535199 |         875479 | False            | True             | True            | True                         | True                        |     018462 |              | false              |               |                    0 |
```


## About final data
> - Total rows: 2710686

### Schema
```
root
 |-- names: array (nullable = true)
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
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 99.78% |
| Documents | 99.86% |
| Accounts | 99.76% |
| Actuality | 100.00% |



### Data sample
```
| names                                  | phones          | documents                                                                                                                                                                                                                                           | accounts                                                           | actuality   |
|:---------------------------------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|:------------|
| ['Мисурагина Ольга Сергеевна']         | ['79193922966'] | [Row(type=2, serial='15199484203', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='6513768929', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018462')] | 06.11.2020  |
| ['Плиско Дмитрий Михайлович']          | ['79097794543'] | [Row(type=2, serial='14192438759', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='2707150668', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='001399')] | 06.11.2020  |
| ['Судоргин Дмитрий Олегович']          | ['79080092007'] | [Row(type=2, serial='14973870416', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='3713552756', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018779')] | 06.11.2020  |
| ['Харченко Лидия Александровна']       | ['79022593325'] | [Row(type=2, serial='00872591662', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='6500471337', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='001399')] | 06.11.2020  |
| ['Анохин Алексей Владимирович']        | ['79534280515'] | [Row(type=2, serial='10799102872', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='7011295427', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018779')] | 06.11.2020  |
| ['Исмайлова Рена Фархадкызы']          | ['79778998151'] | [Row(type=2, serial='19971182627', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='4620934288', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018462')] | 06.11.2020  |
| ['Тайгунова Маргарита Каримовна']      | ['79631371939'] | [Row(type=2, serial='15103185513', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='8011532330', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018462')] | 06.11.2020  |
| ['Самыгин Теймур Александрович']       | ['79520484759'] | [Row(type=2, serial='14603938967', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='9212343490', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018462')] | 06.11.2020  |
| ['Ковган Дмитрий Викторович']          | ['79997737801'] | [Row(type=2, serial='13843477684', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='4515403881', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='001399')] | 06.11.2020  |
| ['Кисмаев Ренат Ростемович']           | ['79125924533'] | [Row(type=2, serial='13696971925', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='5708343648', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='001399')] | 06.11.2020  |
| ['Терентьев Алексей Михайлович']       | ['79287631201'] | [Row(type=2, serial='10184396943', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                          | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018779')] | 06.11.2020  |
| ['Зеленова Татьяна Геннадьевна']       | ['79876270009'] | [Row(type=2, serial='13772811272', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='8013888523', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018779')] | 06.11.2020  |
| ['Баймуратова Татьяна Борисовна']      | ['79123936839'] | [Row(type=2, serial='07872536104', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='7112940414', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018779')] | 06.11.2020  |
| ['Белоцерковский Станислав Викторови'] | ['79807297215'] | [Row(type=2, serial='18822802086', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='7020980225', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018779')] | 06.11.2020  |
| ['Шулаева Галина Петровна']            | ['79503406323'] | [Row(type=2, serial='02917218551', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='2204142682', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018462')] | 06.11.2020  |
| ['Зеленова Татьяна Геннадьевна']       | ['79876270009'] | [Row(type=2, serial='13772811272', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='8013888523', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018779')] | 06.11.2020  |
| ['Алиев Ильяс Ильясоглы']              | ['79042321124'] | [Row(type=2, serial='15092860870', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='8713609898', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018779')] | 06.11.2020  |
| ['Кривошеина Анжела Сергеевна']        | ['79114062434'] | [Row(type=2, serial='16426056861', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='8619317908', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='001399')] | 06.11.2020  |
| ['Богдан Евгений Михайлович']          | ['79141566253'] | [Row(type=2, serial='05476170367', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                          | [Row(title='Мандарин', link='http://mandarin.io.ru', id='016445')] | 06.11.2020  |
| ['Лаврухин Дмитрий Олегович']          | ['79517374868'] | [Row(type=2, serial='07880535199', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='1919271449', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(title='Мандарин', link='http://mandarin.io.ru', id='018462')] | 06.11.2020  |
```