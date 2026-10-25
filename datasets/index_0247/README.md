# Parsetron results

## About row data

> - Code name: index_0247
> - File path: rusnod_users.csv
> - Total rows: 200319

### Schema
```
root
 |-- User_ID: string (nullable = true)
 |-- Password: string (nullable = true)
 |-- PermissionGroup_ID: string (nullable = true)
 |-- Checked: string (nullable = true)
 |-- Language: string (nullable = true)
 |-- Created: string (nullable = true)
 |-- LastUpdated: timestamp (nullable = true)
 |-- Email: string (nullable = true)
 |-- Confirmed: integer (nullable = true)
 |-- RegistrationCode: string (nullable = true)
 |-- Keyword: string (nullable = true)
 |-- Login: string (nullable = true)
 |-- Year: string (nullable = true)
 |-- Avatar: string (nullable = true)
 |-- Country: integer (nullable = true)
 |-- FullName: string (nullable = true)
 |-- Catalogue_ID: integer (nullable = true)
 |-- InsideAdminAccess: integer (nullable = true)
 |-- Auth_Hash: string (nullable = true)
 |-- UserType: string (nullable = true)
 |-- Region: integer (nullable = true)
 |-- ncAttemptAuth: integer (nullable = true)
 |-- City: integer (nullable = true)
 |-- Address: string (nullable = true)
 |-- Phone: string (nullable = true)
 |-- Skype: string (nullable = true)
 |-- Citizenship: string (nullable = true)
 |-- NickName: string (nullable = true)
 |-- Status: integer (nullable = true)
 |-- UserName: string (nullable = true)
 |-- EmailMess: integer (nullable = true)
 |-- SmsMess: integer (nullable = true)
 |-- VK: string (nullable = true)
 |-- FB: string (nullable = true)
 |-- TW: string (nullable = true)
 |-- LJ: string (nullable = true)
 |-- Site: string (nullable = true)
 |-- About: string (nullable = true)
 |-- Youth: string (nullable = true)
 |-- RegionAccess: string (nullable = true)
 |-- noPass: string (nullable = true)
 |-- newLogin: string (nullable = true)
 |-- extended: integer (nullable = true)

```

### Data sample
```
|   User_ID | Password                         |   PermissionGroup_ID |   Checked | Language   | Created             | LastUpdated         | Email                      |   Confirmed | RegistrationCode                 | Keyword   | Login                      | Year       | Avatar   |   Country | FullName                    |   Catalogue_ID |   InsideAdminAccess | Auth_Hash   | UserType   |   Region |   ncAttemptAuth |   City | Address                    |        Phone | Skype     | Citizenship   | NickName          |   Status | UserName                    |   EmailMess |   SmsMess | VK                         | FB   | TW              | LJ   | Site            | About                                    |   Youth | RegionAccess   |   noPass | newLogin   |   extended |
|----------:|:---------------------------------|---------------------:|----------:|:-----------|:--------------------|:--------------------|:---------------------------|------------:|:---------------------------------|:----------|:---------------------------|:-----------|:---------|----------:|:----------------------------|---------------:|--------------------:|:------------|:-----------|---------:|----------------:|-------:|:---------------------------|-------------:|:----------|:--------------|:------------------|---------:|:----------------------------|------------:|----------:|:---------------------------|:-----|:----------------|:-----|:----------------|:-----------------------------------------|--------:|:---------------|---------:|:-----------|-----------:|
|         1 | 2f23ef57dd5f11c2795d112d330f9a42 |                    1 |         1 | Russian    | 2014-09-29 15:02:22 | 2021-02-18 13:49:30 | roman@gcinfinity.ru        |           0 |                                  |           | adm_NODa                   | admin      |          |         1 | admin                       |              0 |                   1 |             | normal     |        1 |               0 |      1 |                            |              |           |               |                   |      nan | Зыков Роман                 |           1 |         0 |                            |      |                 |      |                 | 1111111111                               |       0 |                |        0 |            |          0 |
|         2 | 4efa7bb41f20342caf01e74332f0d582 |                    2 |         1 | Russian    | 2015-03-27 22:16:45 | 2015-05-13 10:30:07 | red@rusnod.ru              |           0 |                                  |           | red@rusnod.ru              | 11.8.1973  |          |         1 | РедНОД РедНОД РедНОД        |              1 |                   0 |             | normal     |        1 |               0 |      1 | Россия                     |              |           | Россия,       | РедНОД            |        7 | Крузенштерн Иван Федорович  |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|         3 | fafcd8fb37e9fe92e1fd04fded943c52 |                    2 |         1 | Russian    | 2015-03-27 22:16:44 | 2015-04-14 10:13:52 | rifzar76@gmail.com         |           0 |                                  |           | rifzar76@gmail.com         | 24.12.1976 |          |         0 | Зарипов Риф Флюрович        |              1 |                   0 |             | normal     |        8 |               0 |    412 | Россия                     |  79177709995 | rifzar76  | 0,            | Риф НОД           |        5 | Зарипов Риф Флюрович        |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|         5 | 6ef296d11a5f5419af30a53c25703006 |                    2 |         1 | Russian    | 2015-03-27 22:16:43 | 2015-05-13 10:30:07 | marishka3001@gmail.com     |           0 |                                  |           | marishka3001@gmail.com     |            |          |         1 | Марина Тимашова             |              1 |                   0 |             | normal     |        1 |               0 |      1 | Россия                     |              |           | Россия        | DiMare            |        2 | Марина Тимашова             |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|         6 | be6d6f9aced9e3619be1e1e114431740 |                    2 |         1 | Russian    | 2015-03-27 22:16:43 | 2015-04-14 10:13:52 | oksanasoloveva@mail.ru     |           0 |                                  |           | oksanasoloveva@mail.ru     |            |          |         0 | Оксана Соловьева            |              1 |                   0 |             | normal     |        0 |               0 |      0 | РФ                         |              |           | Россия        | Ксения            |        1 | Оксана Соловьева            |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|         9 | 2cad8dd94a33ece486820fe1e277d2cd |                    2 |         1 | Russian    | 2015-03-27 22:16:41 | 2022-01-05 07:14:08 | andrivanen@gmail.com       |           0 | 418aafde5182903a165c27e98cb2b96a |           | andrivanen@gmail.com       |            |          |         0 | Андрей Иваненко             |              1 |                   0 |             | normal     |        0 |               0 |      0 | Россия                     |              |           | Россия        | вместецелаястрана |        1 | Андрей Иваненко             |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        10 | 1fd9f866108ae2daf6e5a3722aa9f79d |                    2 |         1 | Russian    | 2015-03-27 22:16:40 | 2015-04-14 10:13:52 | mlkor3@mail.ru             |           0 |                                  |           | mlkor3@mail.ru             |            |          |         0 | Кирилл                      |              1 |                   0 |             | normal     |      456 |               0 |   8426 | Россия Воронежская Воронеж |              |           | Россия        | Кирилл            |        1 | Кирилл                      |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        11 | fa3bcfe0068508df8a97464728d45c7f |                    2 |         1 | Russian    | 2015-03-27 22:16:40 | 2015-04-14 10:13:52 | igor.smirnov.dev@gmail.com |           0 |                                  |           | igor.smirnov.dev@gmail.com |            |          |         0 | Igor Smirnov                |              1 |                   0 |             | normal     |      456 |               0 |   8426 | Israel                     |              |           |               | igor.smirnov      |        1 | Igor Smirnov                |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        12 | 4b221d996acf6751b82359b0e8ae0c8d |                    2 |         1 | Russian    | 2015-03-27 22:16:39 | 2015-04-14 10:13:52 | serjkrush@gmail.com        |           0 |                                  |           | serjkrush@gmail.com        |            |          |         0 | Serj Krush                  |              1 |                   0 |             | normal     |        0 |               0 |      0 | Ukraine                    |              |           |               | Qweb              |        1 | Serj Krush                  |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        15 | 0b56c6bfefec1d92f52efa64d373c347 |                    2 |         1 | Russian    | 2015-03-27 22:16:39 | 2015-05-13 10:30:07 | k.shukalov@yandex.ru       |           0 |                                  |           | k.shukalov@yandex.ru       |            |          |         1 | Константин Шукалов          |              1 |                   0 |             | normal     |        1 |               0 |      1 | Россия                     |              |           | Россия        | Constantine       |        1 | Константин Шукалов          |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        16 | 3f2c4f27e67651fc3b9826478dcfa96f |                    2 |         1 | Russian    | 2015-03-27 22:16:39 | 2015-04-14 10:13:52 | adminiv@list.ru            |           0 |                                  |           | adminiv@list.ru            |            |          |         0 | Андрей Рычихин              |              1 |                   0 |             | normal     |      456 |               0 |   8426 | Россия                     |              |           | Россия        | rezak             |        1 | Андрей Рычихин              |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        17 | 139987554f556697dc22be9ab1c6be5c |                    2 |         1 | Russian    | 2015-03-27 22:16:38 | 2015-04-14 10:13:52 | pavel.klimin@mail.ru       |           0 |                                  |           | pavel.klimin@mail.ru       |            |          |         0 | Павел Климин                |              1 |                   0 |             | normal     |        0 |               0 |      0 | Россия                     |              |           | Россия        | Павел             |        1 | Павел Климин                |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        18 | 0a46182be20ed1e1915a493676335342 |                    2 |         1 | Russian    | 2015-03-27 22:16:38 | 2015-04-14 10:13:52 | sashum123@yandex.ru        |           0 |                                  |           | sashum123@yandex.ru        |            |          |         0 | Николай Васильев            |              1 |                   0 |             | normal     |      456 |               0 |   8426 | Россия                     |              |           | Россия        | nikol             |        1 | Николай Васильев            |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        19 | de96876368fe9b04cf04d8de3df17835 |                    2 |         1 | Russian    | 2015-03-27 22:16:37 | 2016-04-06 14:29:00 | garnett18@mail.ru          |           0 |                                  |           | garnett18@mail.ru          | 1.10.1990  |          |         1 | Макашов Евгений Викторович  |              1 |                   0 |             | normal     |       39 |               0 |   1342 | Россия                     |  89519140237 | nodnnevm  | Россия,       | Евгений           |        5 | Макашов Евгений Викторович  |           0 |         1 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        20 | 7a4fb9a34f4131e0d7b62a396ea9069e |                    2 |         1 | Russian    | 2015-03-27 22:16:37 | 2015-04-14 10:13:52 | jegor.peredera@gmail.com   |           0 |                                  |           | jegor.peredera@gmail.com   |            |          |         0 | Передера Егор               |              1 |                   0 |             | normal     |      456 |               0 |   8426 | Нидерланды                 |              |           |               | jegor             |        1 | Передера Егор               |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        22 | 852de8fd4c3bbb9c004a86a3b6e2b040 |                    2 |         1 | Russian    | 2015-03-27 22:16:36 | 2015-04-14 10:13:52 | Fedotoff_DV@mail.ru        |           0 |                                  |           | Fedotoff_DV@mail.ru        |            |          |         0 | Дммтрий Федотов             |              1 |                   0 |             | normal     |        0 |               0 |      0 | РФ                         |              |           | Россия        | Fedotoff_DV       |        1 | Дммтрий Федотов             |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        23 | 3c0d019579ed6efe1ef57e28a4402c8c |                    2 |         1 | Russian    | 2015-03-27 22:16:35 | 2015-04-14 10:13:52 | ufamark@mail.ru            |           0 |                                  |           | ufamark@mail.ru            |            |          |         0 | Марат Андаржанов            |              1 |                   0 |             | normal     |      456 |               0 |   8426 | Башкортостан               |              |           |               | Марк              |        1 | Марат Андаржанов            |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        25 | 14a155c885662e4fb89ccdc9ae327898 |                    2 |         1 | Russian    | 2015-03-27 22:16:34 | 2015-05-07 17:28:29 | miron1360@gmail.com        |           0 | 4927536ea4083247d09d846c0dc12f5c |           | miron1360@gmail.com        | 06.06.1981 |          |         1 | Андреев Александр Андреевич |              1 |                   0 |             | normal     |       74 |               0 |   2488 | Россия                     |  89033222519 | miron1360 | Россия        | miron1360         |        5 | Андреев Александр Андреевич |           1 |         1 | http://vk.com/nodchuvashia |      | http://rusnod21 |      | http://nodch.ru | Координатор НОД по Чувашской республике. |       0 |                |        0 |            |          0 |
|        26 | 0734d24ef007439853037fd8b0a7c18e |                    2 |         1 | Russian    | 2015-03-27 22:16:34 | 2015-04-14 10:13:52 | sbayazitov@mail.ru         |           0 |                                  |           | sbayazitov@mail.ru         | 19.6.1993  |          |         0 | Самат Баязитов Гумарович    |              1 |                   0 |             | normal     |       60 |               0 |   2090 | Россия                     | +79600891667 |           | Россия,       | Gad123naq         |        1 | Самат Баязитов Гумарович    |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
|        28 | a08885a83ce8f55f9079be1811aec75a |                    2 |         1 | Russian    | 2015-03-27 22:16:33 | 2015-04-14 10:13:52 | EdwardGushchin@gmail.com   |           0 |                                  |           | EdwardGushchin@gmail.com   |            |          |         0 | Гущин Эдуард                |              1 |                   0 |             | normal     |        0 |               0 |      0 | Россия                     |              |           | Россия        | EduardGuschin     |        1 | Гущин Эдуард                |           0 |         0 |                            |      |                 |      |                 |                                          |       0 |                |        0 |            |          0 |
```


## About final data
> - Total rows: 144418

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- actuality: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.57% |
| Phones | 31.29% |
| Address | 33.19% |
| Socials | 6.19% |
| Accounts | 98.13% |
| Birth_date | 68.93% |
| Actuality | 100.00% |
| Raw_metadata | 0.66% |



### Data sample
```
| names                           | emails                         | phones          | address                        | socials                                                                                                             | accounts                                                                                                                        | birth_date   | actuality   | raw_metadata                                                                         |
|:--------------------------------|:-------------------------------|:----------------|:-------------------------------|:--------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|:-------------|:------------|:-------------------------------------------------------------------------------------|
| ['Admin']                       | ['roman@gcinfinity.ru']        |                 |                                |                                                                                                                     |                                                                                                                                 |              | 18.02.2021  | ['{"About": "1111111111"}']                                                          |
| ['Реднод Реднод Реднод']        | ['red@rusnod.ru']              |                 | ['Россия']                     |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='РедНОД', password_hash='4efa7bb41f20342caf01e74332f0d582')]            | 11.08.1973   | 13.05.2015  |                                                                                      |
| ['Зарипов Риф Флюрович']        | ['rifzar76@gmail.com']         | ['79177709995'] | ['Россия']                     | [Row(title='Skype', id='rifzar76', link=None)]                                                                      | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='Риф НОД', password_hash='fafcd8fb37e9fe92e1fd04fded943c52')]           | 24.12.1976   | 14.04.2015  |                                                                                      |
| ['Марина Тимашова']             | ['marishka3001@gmail.com']     |                 | ['Россия']                     |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='DiMare', password_hash='6ef296d11a5f5419af30a53c25703006')]            |              | 13.05.2015  |                                                                                      |
| ['Оксана Соловьева']            | ['oksanasoloveva@mail.ru']     |                 |                                |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='Ксения', password_hash='be6d6f9aced9e3619be1e1e114431740')]            |              | 14.04.2015  |                                                                                      |
| ['Андрей Иваненко']             | ['andrivanen@gmail.com']       |                 | ['Россия']                     |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='вместецелаястрана', password_hash='2cad8dd94a33ece486820fe1e277d2cd')] |              | 05.01.2022  |                                                                                      |
| ['Кирилл']                      | ['mlkor3@mail.ru']             |                 | ['Россия Воронежская Воронеж'] |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='Кирилл', password_hash='1fd9f866108ae2daf6e5a3722aa9f79d')]            |              | 14.04.2015  |                                                                                      |
| ['Igor Smirnov']                | ['igor.smirnov.dev@gmail.com'] |                 | ['Israel']                     |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='igor.smirnov', password_hash='fa3bcfe0068508df8a97464728d45c7f')]      |              | 14.04.2015  |                                                                                      |
| ['Serj Krush']                  | ['serjkrush@gmail.com']        |                 | ['Ukraine']                    |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='Qweb', password_hash='4b221d996acf6751b82359b0e8ae0c8d')]              |              | 14.04.2015  |                                                                                      |
| ['Константин Шукалов']          | ['k.shukalov@yandex.ru']       |                 | ['Россия']                     |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='Constantine', password_hash='0b56c6bfefec1d92f52efa64d373c347')]       |              | 13.05.2015  |                                                                                      |
| ['Андрей Рычихин']              | ['adminiv@list.ru']            |                 | ['Россия']                     |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='rezak', password_hash='3f2c4f27e67651fc3b9826478dcfa96f')]             |              | 14.04.2015  |                                                                                      |
| ['Павел Климин']                | ['pavel.klimin@mail.ru']       |                 | ['Россия']                     |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='Павел', password_hash='139987554f556697dc22be9ab1c6be5c')]             |              | 14.04.2015  |                                                                                      |
| ['Николай Васильев']            | ['sashum123@yandex.ru']        |                 | ['Россия']                     |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='nikol', password_hash='0a46182be20ed1e1915a493676335342')]             |              | 14.04.2015  |                                                                                      |
| ['Макашов Евгений Викторович']  | ['garnett18@mail.ru']          | ['79519140237'] | ['Россия']                     | [Row(title='Skype', id='nodnnevm', link=None)]                                                                      | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='Евгений', password_hash='de96876368fe9b04cf04d8de3df17835')]           | 01.10.1990   | 06.04.2016  |                                                                                      |
| ['Передера Егор']               | ['jegor.peredera@gmail.com']   |                 | ['Нидерланды']                 |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='jegor', password_hash='7a4fb9a34f4131e0d7b62a396ea9069e')]             |              | 14.04.2015  |                                                                                      |
| ['Дммтрий Федотов']             | ['fedotoff_dv@mail.ru']        |                 |                                |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='Fedotoff_DV', password_hash='852de8fd4c3bbb9c004a86a3b6e2b040')]       |              | 14.04.2015  |                                                                                      |
| ['Марат Андаржанов']            | ['ufamark@mail.ru']            |                 | ['Башкортостан']               |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='Марк', password_hash='3c0d019579ed6efe1ef57e28a4402c8c')]              |              | 14.04.2015  |                                                                                      |
| ['Андреев Александр Андреевич'] | ['miron1360@gmail.com']        | ['79033222519'] | ['Россия']                     | [Row(title='ВКонтакте', id=None, link='http://vk.com/nodchuvashia'), Row(title='Skype', id='miron1360', link=None)] | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='miron1360', password_hash='14a155c885662e4fb89ccdc9ae327898')]         | 06.06.1981   | 07.05.2015  | ['{"About": "Координатор НОД по Чувашской республике.", "Site": "http://nodch.ru"}'] |
| ['Самат Баязитов Гумарович']    | ['sbayazitov@mail.ru']         | ['79600891667'] | ['Россия']                     |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='Gad123naq', password_hash='0734d24ef007439853037fd8b0a7c18e')]         | 19.06.1993   | 14.04.2015  |                                                                                      |
| ['Гущин Эдуард']                | ['edwardgushchin@gmail.com']   |                 | ['Россия']                     |                                                                                                                     | [Row(title='Rusnod.ru', link='https://rusnod.ru', login='EduardGuschin', password_hash='a08885a83ce8f55f9079be1811aec75a')]     |              | 14.04.2015  |                                                                                      |
```