# Parsetron results

## About row data

> - File path: users_1.csv
> - Total rows: 299821

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- TIMESTAMP_X: timestamp (nullable = true)
 |-- LOGIN: string (nullable = true)
 |-- PASSWORD: string (nullable = true)
 |-- CHECKWORD: string (nullable = true)
 |-- ACTIVE: string (nullable = true)
 |-- NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- LAST_LOGIN: timestamp (nullable = true)
 |-- DATE_REGISTER: timestamp (nullable = true)
 |-- LID: string (nullable = true)
 |-- PERSONAL_PROFESSION: string (nullable = true)
 |-- PERSONAL_WWW: string (nullable = true)
 |-- PERSONAL_ICQ: string (nullable = true)
 |-- PERSONAL_GENDER: string (nullable = true)
 |-- PERSONAL_BIRTHDATE: string (nullable = true)
 |-- PERSONAL_PHOTO: string (nullable = true)
 |-- PERSONAL_PHONE: long (nullable = true)
 |-- PERSONAL_FAX: string (nullable = true)
 |-- PERSONAL_MOBILE: long (nullable = true)
 |-- PERSONAL_PAGER: long (nullable = true)
 |-- PERSONAL_STREET: string (nullable = true)
 |-- PERSONAL_MAILBOX: string (nullable = true)
 |-- PERSONAL_CITY: string (nullable = true)
 |-- PERSONAL_STATE: string (nullable = true)
 |-- PERSONAL_ZIP: integer (nullable = true)
 |-- PERSONAL_COUNTRY: integer (nullable = true)
 |-- PERSONAL_NOTES: string (nullable = true)
 |-- WORK_COMPANY: string (nullable = true)
 |-- WORK_DEPARTMENT: string (nullable = true)
 |-- WORK_POSITION: string (nullable = true)
 |-- WORK_WWW: string (nullable = true)
 |-- WORK_PHONE: string (nullable = true)
 |-- WORK_FAX: string (nullable = true)
 |-- WORK_PAGER: string (nullable = true)
 |-- WORK_STREET: string (nullable = true)
 |-- WORK_MAILBOX: string (nullable = true)
 |-- WORK_CITY: string (nullable = true)
 |-- WORK_STATE: string (nullable = true)
 |-- WORK_ZIP: string (nullable = true)
 |-- WORK_COUNTRY: integer (nullable = true)
 |-- WORK_PROFILE: string (nullable = true)
 |-- WORK_LOGO: string (nullable = true)
 |-- WORK_NOTES: string (nullable = true)
 |-- ADMIN_NOTES: string (nullable = true)
 |-- STORED_HASH: string (nullable = true)
 |-- XML_ID: integer (nullable = true)
 |-- PERSONAL_BIRTHDAY: date (nullable = true)
 |-- EXTERNAL_AUTH_ID: string (nullable = true)
 |-- CHECKWORD_TIME: timestamp (nullable = true)
 |-- SECOND_NAME: string (nullable = true)
 |-- CONFIRM_CODE: string (nullable = true)
 |-- LOGIN_ATTEMPTS: integer (nullable = true)
 |-- LAST_ACTIVITY_DATE: timestamp (nullable = true)
 |-- AUTO_TIME_ZONE: string (nullable = true)
 |-- TIME_ZONE: string (nullable = true)
 |-- TIME_ZONE_OFFSET: string (nullable = true)
 |-- TITLE: string (nullable = true)
 |-- BX_USER_ID: string (nullable = true)
 |-- LANGUAGE_ID: string (nullable = true)

```

### Data sample
```
|   ID | TIMESTAMP_X         | LOGIN                         | PASSWORD                                 | CHECKWORD                                | ACTIVE   | NAME                 | LAST_NAME                         | EMAIL                         | LAST_LOGIN          | DATE_REGISTER       | LID   | PERSONAL_PROFESSION   | PERSONAL_WWW   | PERSONAL_ICQ   | PERSONAL_GENDER   | PERSONAL_BIRTHDATE   | PERSONAL_PHOTO   |   PERSONAL_PHONE | PERSONAL_FAX   |   PERSONAL_MOBILE |   PERSONAL_PAGER | PERSONAL_STREET     | PERSONAL_MAILBOX   | PERSONAL_CITY   | PERSONAL_STATE   |   PERSONAL_ZIP |   PERSONAL_COUNTRY | PERSONAL_NOTES   | WORK_COMPANY   | WORK_DEPARTMENT   | WORK_POSITION   | WORK_WWW   | WORK_PHONE   | WORK_FAX   | WORK_PAGER   | WORK_STREET   | WORK_MAILBOX   | WORK_CITY   | WORK_STATE   | WORK_ZIP   |   WORK_COUNTRY | WORK_PROFILE   | WORK_LOGO   | WORK_NOTES   | ADMIN_NOTES   | STORED_HASH   |   XML_ID | PERSONAL_BIRTHDAY   | EXTERNAL_AUTH_ID   | CHECKWORD_TIME      | SECOND_NAME                                        | CONFIRM_CODE   |   LOGIN_ATTEMPTS | LAST_ACTIVITY_DATE   | AUTO_TIME_ZONE   | TIME_ZONE   | TIME_ZONE_OFFSET   | TITLE   | BX_USER_ID                       | LANGUAGE_ID   |
|-----:|:--------------------|:------------------------------|:-----------------------------------------|:-----------------------------------------|:---------|:---------------------|:----------------------------------|:------------------------------|:--------------------|:--------------------|:------|:----------------------|:---------------|:---------------|:------------------|:---------------------|:-----------------|-----------------:|:---------------|------------------:|-----------------:|:--------------------|:-------------------|:----------------|:-----------------|---------------:|-------------------:|:-----------------|:---------------|:------------------|:----------------|:-----------|:-------------|:-----------|:-------------|:--------------|:---------------|:------------|:-------------|:-----------|---------------:|:---------------|:------------|:-------------|:--------------|:--------------|---------:|:--------------------|:-------------------|:--------------------|:---------------------------------------------------|:---------------|-----------------:|:---------------------|:-----------------|:------------|:-------------------|:--------|:---------------------------------|:--------------|
|    1 | 2024-06-19 10:47:51 | admin_new@kant.ru             | Ix-6[sX60cbe3049a901c1d4088572b61a159dab | OWLlKWiZe8d456e6570a6c396faed939f7565128 | Y        |                      |                                   | admin_new@kant.ru             | 2024-12-18 15:42:50 | 2014-08-27 19:18:58 | s1    |                       |                |                | M                 |                      |                  |      7e+10       |                |       7e+10       |              nan | ул. Варейкиса 45-54 |                    | Ульяновск       |                  |         432044 |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |      nan | 1990-05-18          |                    | 2024-06-19 10:47:51 |                                                    |                |                0 | 2024-05-02 13:00:59  |                  |             |                    |         | d31f80cc05bb5912cf75ffbd77fd33d7 |               |
|    2 | 2023-03-10 18:58:39 | vladimir.savritsky            | ~8JrtM2=fb22d5b7377235d93ff8eac66737cdba | 2mhkosnfb8c64bc529aeca7950b01525e84dd95d | Y        |                      | Саврик                            | vladimir.savritsky@gmail.com  | 2014-10-15 20:08:01 | 2014-10-15 20:08:01 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2020-06-25 21:26:05 |                                                    |                |             1133 | NaT                  |                  |             |                    |         |                                  |               |
|    3 | 2023-07-26 12:13:20 | vladimir.savritsky@gmail.com1 | glpPPglM122471b1c30f29d9597c4c4368b5c21a | UV4CJkh7e6656981e587d55b7f1ed1730f2da668 | Y        | 123                  |                                   | vladimir.savritsky@gmail.com1 | 2014-10-17 00:18:18 | 2014-10-17 00:18:18 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |      nan |                     |                    | 2014-10-20 17:39:37 |                                                    |                |              481 | NaT                  |                  |             |                    |         |                                  |               |
|    5 | 2020-05-04 17:25:17 | guest_5xfkff8leix@kant.ru     | 6CrfFKKRb3e75e143d3d6daac816d438f551e2c6 | RZqF29Db6c21af78d31083b61a0df9e9cdc7a706 | Y        | kirill               | 1                                 | guest_5xfkff8leix@kant.ru     | 2019-09-19 15:31:06 | 2014-10-17 00:38:41 | s1    |                       |                |                |                   |                      |                  |      8e+10       |                |       8e+10       |              nan |                     |                    | Подольск        |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2020-03-19 15:44:38 | 1                                                  |                |              523 | 2018-10-25 16:47:46  |                  |             |                    |         | e76a605dad8d1e49cdfe9c013938620f |               |
|    6 | 2023-02-20 20:03:14 | besedina@aeroidea.ru          | t8n4n0RW7d77b3fcd225cbf6a7afe4b4431eb4b3 | 93x4FfuC98bed68a3a90f8d9b0eb6dcd5fb517e1 | Y        | Fyut                 |                                   | besedina@aeroidea.ru          | 2014-10-20 12:50:55 | 2014-10-20 12:16:28 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-10-20 12:16:28 |                                                    |                |              448 | NaT                  |                  |             |                    |         |                                  |               |
|    7 | 2023-03-18 11:55:35 | 234@sdf.ru                    | qyaZ5bnH8f5aef98cd5c4118fa52b75be80da46e | 1QV2UsWy61ee6eee2e4a227e041804d904173862 | Y        | 123                  |                                   | 234@sdf.ru                    | 2014-10-20 12:21:45 | 2014-10-20 12:21:45 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-10-20 12:21:45 |                                                    |                |              746 | NaT                  |                  |             |                    |         |                                  |               |
|    8 | 2021-10-05 13:06:32 | flamieflamie@gmail.com        | k{7T1Ii^b97d03b4367a0ad59ce874f3fc2f872e | H1RuiRXNc5923206b8b782dce78a0d5841d4f18b | Y        | Ангелина             |                                   | flamieflamie@gmail.com        | 2021-04-07 16:16:46 | 2014-10-20 12:31:17 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-11-13 18:38:03 |                                                    |                |              230 | 2021-04-07 16:16:49  |                  |             |                    |         |                                  |               |
|    9 | 2022-09-23 14:21:51 | ruxica@walkmail.net           | 77yDctRE2ce440edf80b26afbf5a8207370580bc | AVqRpJGu393e20d47a9357f3737543b78070513e | Y        | Андрей               | Test                              | ruxica@walkmail.net           | 2023-01-15 16:20:28 | 2014-10-20 14:51:30 | s1    |                       |                |                |                   |                      |                  |      7.92599e+10 |                |       7.92599e+10 |              nan |                     |                    |                 |                  |            nan |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |      nan |                     |                    | 2014-10-20 14:58:36 | Вяч                                                |                |               13 | 2023-01-15 16:20:30  |                  |             |                    |         | 4d619002aeb23bf4500d61b42559c798 |               |
|   10 | 2022-12-27 11:20:20 | vladimir.savritsky@gmail.com2 | lR5=iS1[ee723d7012e7c42a4a262a01d39b83ff | wHA16USubb6a42213cf30f6439f4e310c3e7c616 | Y        | Владимир             |                                   | vladimir.savritsky@gmail.com2 | 2014-10-20 18:54:06 | 2014-10-20 17:39:56 | s1    |                       |                |                |                   |                      |                  |      7.92669e+10 |                |       7.92669e+10 |              nan |                     |                    |                 |                  |            nan |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |      nan |                     |                    | 2014-10-21 11:24:55 |                                                    |                |              104 | NaT                  |                  |             |                    |         |                                  |               |
|   12 | 2022-03-01 14:53:05 | vladimir.savritsky@gmail.com  | (wZ78,qF338430f0953e7730086057fd19c75fa3 | YQGef6cX42656987ea20194d97f0d4db4010c051 | Y        | Владимир             |                                   | vladimir.savritsky@gmail.com  | 2014-11-25 01:31:25 | 2014-10-21 11:32:25 | s1    |                       |                |                |                   |                      |                  |      7.92669e+10 |                |       7.92669e+10 |              nan |                     |                    |                 |                  |            nan |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |      nan |                     |                    | 2014-11-27 01:01:24 |                                                    |                |              158 | NaT                  |                  |             |                    |         |                                  |               |
|   13 | 2023-05-06 17:04:10 | andrey@aeroidea.ru            | uKKXxd2bd2812dee7b87d4a0c163702d6767a8ec | xqYqcAhB083716ce93748e212497af61a8c63b0f | Y        | Андрей Носов         |                                   | andrey@aeroidea.ru            | 2014-10-30 20:48:18 | 2014-10-30 20:48:17 | s1    |                       |                |                |                   |                      |                  |      7.92599e+10 |                |       7.92599e+10 |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-10-30 20:48:17 |                                                    |                |              269 | NaT                  |                  |             |                    |         |                                  |               |
|   14 | 2020-08-10 23:28:13 | agbv@rambler.ru               | NfvRGIZT07365d56f2d2582b1f61290c239eecef | cotiz2UV4bd2e69390f732796c9829a89d96896b | Y        | Angelina             |                                   | agbv@rambler.ru               | 2014-11-15 00:56:48 | 2014-10-31 01:47:16 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-10-31 01:47:16 |                                                    |                |               85 | NaT                  |                  |             |                    |         |                                  |               |
|   15 | 2022-04-18 21:45:59 | dfty@ghf.ru                   | Z0HahJb65548785c64bb1634608aa05bb54fbe0b | Yl8s3jYM17c88d58996d077f727fd716a06ab6a5 | Y        | Владимир             |                                   | dfty@ghf.ru                   | 2014-10-31 01:48:21 | 2014-10-31 01:48:21 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-10-31 01:48:21 |                                                    |                |               85 | NaT                  |                  |             |                    |         |                                  |               |
|   16 | 2023-02-21 01:40:23 | 123@sdfsdf.ru                 | woA7kQkp807b84df396d6724f3833913136ecf8f | KCfPAK3Tf48313e0e1e8e82bf103c6584b3928eb | Y        | 123                  |                                   | 123@sdfsdf.ru                 | 2014-10-31 01:54:51 | 2014-10-31 01:54:51 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-10-31 01:54:51 |                                                    |                |               62 | NaT                  |                  |             |                    |         |                                  |               |
|   17 | 2019-10-02 05:14:12 | 342@dfsdf.ru                  | xZiBYdWie37901120fd623f6f4c3b583e075dadf | dNK7mPfRc08d58b0d77c298f07cf5ed16e8ccbf4 | Y        | 123                  |                                   | 342@dfsdf.ru                  | 2014-10-31 01:55:47 | 2014-10-31 01:55:47 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-10-31 01:55:47 |                                                    |                |               75 | NaT                  |                  |             |                    |         |                                  |               |
|   18 | 2020-04-24 15:57:53 | gfj@gfht.ru                   | FIIxNWDN1a06c0cbba1cb8a91bbe697d8a33ae35 | DqOo6Taf552ea415d4a66c5bcedaa4ede4ae7c5f | Y        | 123                  |                                   | gfj@gfht.ru                   | 2014-10-31 01:56:55 | 2014-10-31 01:56:55 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-10-31 01:56:55 |                                                    |                |              110 | NaT                  |                  |             |                    |         |                                  |               |
|   19 | 2023-08-13 18:11:58 | tester.14@rambler.ru          | >Qm6;y9Vba1a2af672ae7c5f1dcbf7acabe1d8ad | Dk2mtYvpa6466ea7509316d6e22383a5a7bab24e | Y        | tester.14@rambler.ru | gfgfgfgfjgh пварпапрапраапапрарпа | tester.14@rambler.ru          | 2014-11-14 19:22:42 | 2014-10-31 17:29:26 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |      nan |                     |                    | 2014-11-03 18:32:55 | выпваыпвапавввпррооооооооооооооолллллгнешгнешненкш |                |              258 | NaT                  |                  |             |                    |         |                                  |               |
|   20 | 2019-10-02 05:14:13 | tester                        | xBxPEJ69a5edf92aa0fa3ef7ddac5ae35d2ec3ef | akdx0Yhs73ce1e83958ca39b696e31a887f8fc2e | Y        | tester.13            |                                   | tester.13@rambler.ru          | 2014-11-03 18:34:54 | 2014-11-03 18:34:53 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-11-03 18:34:53 |                                                    |                |              151 | NaT                  |                  |             |                    |         |                                  |               |
|   21 | 2019-10-02 05:14:13 | tester.13@rambler.ru          | zrsdtvLDb7bc37d594f25228b835ed01cdd8eb1f | W0EuhXux2beb7b4759535018082f6046e0f6b555 | Y        | hfgjhgjh             |                                   | tester.13@rambler.ru          | 2014-11-07 19:55:23 | 2014-11-03 18:37:48 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-11-03 18:37:48 |                                                    |                |              312 | NaT                  |                  |             |                    |         |                                  |               |
|   22 | 2022-01-01 16:27:20 | trytrytr@gfhg.yu              | esAW0fiJdf048a056068e31e512526e8deab473e | 5VdhYuvZ604a828351ce919107843e5965ccc57d | Y        | hghjg                |                                   | trytrytr@gfhg.yu              | 2021-03-30 13:09:48 | 2014-11-03 18:39:18 | s1    |                       |                |                |                   |                      |                  |    nan           |                |     nan           |              nan |                     |                    |                 |                  |            nan |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |      nan |                     |                    | 2014-11-03 18:39:18 |                                                    |                |               88 | 2021-03-30 13:09:53  |                  |             |                    |         |                                  |               |
```

> - File path: users_2.csv
> - Total rows: 12983

### Schema
```
root
 |-- name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- email: string (nullable = true)
 |-- comment: string (nullable = true)

```

### Data sample
```
| name                                                                                                                                                                                           | phone           | email                        | comment                                                                                                                                                                                            |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|:-----------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 345345                                                                                                                                                                                         | 345354          | 354345                       | 345345                                                                                                                                                                                             |
| 34533                                                                                                                                                                                          | 45345           | 345345                       | dfsfsf                                                                                                                                                                                             |
| 34533                                                                                                                                                                                          | 45345           | 345345                       | dfsfsf                                                                                                                                                                                             |
| 35                                                                                                                                                                                             | 345345345       | 345                          | dgdgdfg                                                                                                                                                                                            |
| Dkflbvbh                                                                                                                                                                                       | +79266881334    | vladimir.savritsky@gmail.com |                                                                                                                                                                                                    |
| Екатерина Вороничева                                                                                                                                                                           | 89629418250     | katarina_v@mail.ru           | Добрый день,                                                                                                                                                                                       |
| Хочу записать в горнолыжную школу свою дочь, 9 лет. Ни разу не стояла на горных лыжах. Спортивный опыт минимальный. Хотим начать занятия в группе для начинающих в это воскресенье 14 декабря. |                 |                              |                                                                                                                                                                                                    |
| спасибо."                                                                                                                                                                                      |                 |                              |                                                                                                                                                                                                    |
| Круглий Юлия                                                                                                                                                                                   | +79163500509    | moonstep@mail.ru             | занятия для школьника, 7 лет , начальный уровень, ни разу не стоял на лыжах. Хотели бы в четверг, 4 раза в месяц.                                                                                  |
| Гонт Ольга                                                                                                                                                                                     | 926-267-5650    | olga.gont@mail.ru            | двое детей: девочка / мальчик                                                                                                                                                                      |
| 9 лет / 3 года 10 мес                                                                                                                                                                          |                 |                              |                                                                                                                                                                                                    |
| лыжи / лыжи или сноуборд                                                                                                                                                                       |                 |                              |                                                                                                                                                                                                    |
| желательно в субботу не ранее 15:00                                                                                                                                                            |                 |                              |                                                                                                                                                                                                    |
| Буду ждать звонка."                                                                                                                                                                            |                 |                              |                                                                                                                                                                                                    |
| Круглий Юлия                                                                                                                                                                                   | +79163500509    | moonstep@mail.ru             | хотели бы записаться в группу обучению горным лыжам по четвергам в 1800-1930 у Антоновой Марии, ребенку 7 лет. Что нам необходимо для первого занятия? и когда можно начинать?                     |
| Селезнева Александра Владимировна                                                                                                                                                              | 8-915-076-00-61 | Doronina86@mail.ru           | Добрый день! Моему сыну 11 лет, он очень хочет научится кататься на сноуборде или на горных лыжах. Подскажите пожалуйста, возможно записаться сейчас в вашу школу?                                 |
| Дудышева Екатерина                                                                                                                                                                             | 89067896506     | Kate198402@ya.ru             | Ребенок 7 лет, обучение только в выходные                                                                                                                                                          |
| Сафронов Михаил Михайлович                                                                                                                                                                     | 89260135585     | michael.safronov@yandex.ru   |                                                                                                                                                                                                    |
| Берштейн Виктория Вениаминовна                                                                                                                                                                 | +79036772727    | bershteyn@rambler.ru         | Добрый день! Хочу записать 3-х детей(6 и 9 лет) на индивидуальное ЭКСПРЕСС-ОБУЧЕНИЕ к Лесовой Александре в воскресенье (13.12.2014) во второй половине дня. Как это сделать? С уважением Виктория. |
| Татьяна                                                                                                                                                                                        | 89162609176     | tmikhailenko2305@gmail.com   | хочу привезти сегодня сына на индивидуалку или группу, сыну 8 лет, катается третий год                                                                                                             |
```

> - File path: users_3.csv
> - Total rows: 48577

### Schema
```
root
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- index: string (nullable = true)
 |-- city: string (nullable = true)
 |-- street: string (nullable = true)
 |-- building: string (nullable = true)
 |-- flat: string (nullable = true)
 |-- comment: string (nullable = true)

```

### Data sample
```
| name                                                   | email                        | phone            |          index | city         | street                  | building               |             flat | comment    |
|:-------------------------------------------------------|:-----------------------------|:-----------------|---------------:|:-------------|:------------------------|:-----------------------|-----------------:|:-----------|
| Саврик                                                 | vladimir.savritsky@gmail.com | +79266881334     |         101000 |              |                         |                        |                  |            |
| Fyut                                                   | besedina@aeroidea.ru         | 123123123        |         101000 | Москва       |                         |                        |                  |            |
|                                                        |                              |                  |                |              |                         |                        |                  |            |
|                                                        |                              |                  |                |              |                         |                        |                  |            |
| ТЕСТ ТЕСТ ТЕСТ                                         | besedina@aeroidea.com        | 11111111111      |      123234234 | Москва213243 | Совесткая               | 1                      |                1 | тест       |
|                                                        |                              |                  |                |              |                         |                        |                  |            |
| tester.14@rambler.ru gfgfgfgfjgh пварпапрапраапапрарпа | tester.14@rambler.ru         | 879879870987098  |         101000 |              |                         |                        |                  |            |
| hfgjhgjh                                               | tester.13@rambler.ru         | 6797869797867869 |         101000 |              |                         |                        |                  |            |
| Angelina                                               | agbv@rambler.ru              | 123123           |         101000 |              | Ntcn                    | 1                      |                  | 123123     |
| Владимир ТЕСТ ТЕСТ ТЕСТ                                | vladimir.savritsky@gmail.com | +7(111)111-11-11 |            123 | Москва789    | 1                       | 2                      |                5 | 7899       |
| 123                                                    | 3@22.ru                      |                  |         101000 |              |                         |                        |                  |            |
| Ангелина                                               | flaminga.mail@yandex.ru      | 123123123        |         101000 |              |                         |                        |                  |            |
| alex                                                   | kydryav@mail.ru              |                  |         101000 |              |                         |                        |                  |            |
| Tester Тестер                                          | mailfortests2@gmail.com      | 123123           |         101000 |              | 12                      | 123                    |              123 | тест       |
| Tester Тестер                                          | mailfortests2@gmail.com      | 123  123         |         101000 |              | тест                    | тест                   |                  |            |
| test                                                   | kydryav@gmail.com            | 23452345         |         101000 |              | еееееееееееееееееееееее | 5444444444444444444444 | 2345444444444444 | ывапыва    |
| tester.14@rambler.ru gfgfgfgfjgh пварпапрапраапапрарпа | tester.14@rambler.ru         | 679867967        |         101000 |              | tuytghj                 | dfhfgdhfd              |               12 | ghkhgkghkg |
| фывфы                                                  | haha.artur@mail.ru           |                  |         101000 |              |                         |                        |                  |            |
| фывфы                                                  | haha.artur@mail.ru           |                  |         101000 |              |                         |                        |                  |            |
| ыфвыф                                                  | haha.artur1@mail.ru          |                  |         101000 |              |                         |                        |                  |            |
```

> - File path: cards.csv
> - Total rows: 99955

### Schema
```
root
 |-- number: string (nullable = true)
 |-- amount: double (nullable = true)
 |-- cardholder: string (nullable = true)
 |-- cardtype: string (nullable = true)
 |-- PAN: string (nullable = true)
 |-- datetime: timestamp (nullable = true)

```

### Data sample
```
| number   |   amount | cardholder          | cardtype   | PAN              | datetime            |
|:---------|---------:|:--------------------|:-----------|:-----------------|:--------------------|
| N382163  |      306 | SERGEY KOVTUN       | MASTERCARD | 510069******4391 | 2019-11-22 13:06:09 |
| N382163  |      306 |                     |            |                  | 2019-11-22 13:06:12 |
| N382193  |    15990 | I NOVOKRESHCHENOV   | MASTERCARD | 522598******4808 | 2019-11-22 14:41:28 |
| N382193  |    15990 |                     |            |                  | 2019-11-22 14:41:32 |
| N382199  |     8990 | IRINA BABUSHKINA    | MASTERCARD | 546942******3421 | 2019-11-22 15:17:19 |
| N382199  |     8990 |                     |            |                  | 2019-11-22 15:17:29 |
| N382171  |     2290 | ANATOLIY PAVLOV     | MASTERCARD | 553691******0107 | 2019-11-22 19:07:25 |
| N382219  |     1690 | YANA PIROZHKOVA     | MASTERCARD | 557057******0545 | 2019-11-22 20:24:25 |
| N382219  |     1690 |                     |            |                  | 2019-11-22 20:24:32 |
| N382211  |    25916 | IULIIA IVANOVA      | MIR        | 220024******4145 | 2019-11-23 01:33:33 |
| N382211  |    25916 |                     |            |                  | 2019-11-23 01:33:46 |
| N382203  |     2742 | ARTEM ALEKSEEV      | MIR        | 220220******4014 | 2019-11-23 09:46:10 |
| N382203  |     2742 |                     |            |                  | 2019-11-23 09:46:17 |
| N382317  |      940 | SERGEY ERSHOV       | VISA       | 427638******7958 | 2019-11-23 11:46:29 |
| N382319  |     9354 | CHELYSHEV ALEXEY    | VISA       | 447624******1229 | 2019-11-23 13:38:33 |
| N382319  |     9354 |                     |            |                  | 2019-11-23 13:38:43 |
| N382333  |    28851 | ALEKSANDR SAVELEV   | MASTERCARD | 548999******0361 | 2019-11-23 14:43:28 |
| N382333  |    28851 |                     |            |                  | 2019-11-23 14:43:33 |
| N382371  |     2250 | DMITRIY ZELENEVSKIY | VISA       | 426101******0622 | 2019-11-23 15:07:10 |
| N382371  |     2250 |                     |            |                  | 2019-11-23 15:07:17 |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- financials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- card_number: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Sex | 22.97% |
| Birth_date | 20.35% |
| Emails | 99.93% |
| Phones | 70.44% |
| Accounts | 95.36% |
| Address | 5.55% |
| Financials | 0.00% |
| Raw_metadata | 1.43% |
| Actuality | 92.90% |



### Data sample
```
| names                           |   sex | birth_date   | emails                                             | phones          | accounts                                                                                                                                                                              | address                | financials   | raw_metadata   | actuality   |
|:--------------------------------|------:|:-------------|:---------------------------------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|:-------------|:---------------|:------------|
| ['- Карина']                    |   nan |              | ['user_1481545522584e9732688e8@crm.com']           |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='user_1481545522584e9732688e8@crm.com', password_hash='eeK4bCCt596ec0cfc1cb826e1878697f43450277')]           |                        |              |                |             |
| ['- Роман']                     |   nan |              | ['user_1453222771569e6b739c33b@crm.com']           |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='user_1453222771569e6b739c33b@crm.com', password_hash='E586gnYyccfd63463cad5d0e4b51e05629112dd9')]           |                        |              |                |             |
| ['- Татьяна -']                 |   nan |              | ['user_15337446025b6b15da33246@crm.com']           | ['79263874059'] | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='user_15337446025b6b15da33246@crm.com', password_hash='KDZLqqmA55f53da25b49dfccff130b2024eb45f2')]           | ['кп Петровский Парк'] |              |                |             |
| ['-- Сергей']                   |   nan |              | ['user_148887931158be7ecfc18c3@crm.com']           |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='user_148887931158be7ecfc18c3@crm.com', password_hash='jcE7hB4a6e66a884ed4855d5ddfa03fb3d40b14b')]           |                        |              |                |             |
| ['---- Кирилл']                 |   nan |              | ['user_15136155045a37f09008d31@crm.com']           |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='user_15136155045a37f09008d31@crm.com', password_hash='jUoPjzRLff21ba81612d5d34345bdfa1d8c45e0d')]           |                        |              |                |             |
| ['Alexander']                   |   nan |              | ['mdvdvlxndr@gmail.com']                           | ['79859623199'] | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='mdvdvlxndr@gmail.com', password_hash='7RdiYTFN647da5b79efdebb2d35dafaa4be58fdc')]                           |                        |              |                | 10.06.2020  |
| ['Andrei P']                    |   nan |              | ['chino198787@list.ru']                            | ['79171668537'] | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='chino198787@list.ru', password_hash='10cQbTdM96f271c43d3b664b7bd006dbc84964dc')]                            |                        |              |                | 04.04.2015  |
| ['Andrewdealmfy Andrewdealm']   |   nan |              | ['nertyew@yandex.com']                             |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='AndrewDealm', password_hash='LsDPNwqs8f4904282d81a5dc04699e0f6f693c96')]                                    |                        |              |                | 30.12.2019  |
| ['Ansimawt Ansima']             |   nan |              | ['2303@info89.ru']                                 |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='Ansima', password_hash='Up09o4cf32fae6fe16e6428ec1c0c6cbc16f452e')]                                         |                        |              |                | 25.03.2020  |
| ['Anton Solovyov']              |   nan |              | ['a.solovyov81@mail.ru']                           |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='a.solovyov81@mail.ru', password_hash='L1j3kbPha8e8a69aada0d033e3159a4c71c5eb51')]                           |                        |              |                | 30.11.2019  |
| ['Artem']                       |   nan |              | ['artembaobab@gmail.com']                          | ['79151128879'] | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='Artembaobab@gmail.com', password_hash='67jR14vV5bcc6e61d23b40bc73711521a2aa7e7c')]                          |                        |              |                | 23.12.2014  |
| ['Arteminsagra Arteminsag']     |   nan |              | ['artem538@wemail.ru']                             |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='ArtemInsag', password_hash='RNQshc6le11d9bbdf3c92f03d5a99315627d9199')]                                     |                        |              |                | 04.06.2020  |
| ['Artyomyushkafr Agamaril']     |   nan |              | ['jotheluckystar@gmail.com']                       |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='Agamaril', password_hash='j73kyfGI1fdf0b116b0d497fc2a8a44ec85f5705')]                                       |                        |              |                | 16.04.2020  |
| ['Azagolymnxk Evdeniylymn']     |   nan |              | ['nicovarniere@orange.fr']                         |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='evdeniyLymn', password_hash='UlpBy28H67aaba18c453bbea3eb50762ab9e4616')]                                    |                        |              |                | 09.01.2020  |
| ['Bdfyiffr Anastasia']          |   nan |              | ['lsikand@sikand.com']                             |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='anastasia', password_hash='0OHA1fxX078e3d30b69e31f192165acc8d85def4')]                                      |                        |              |                | 28.05.2020  |
| ['Benniebeinsfl Benniebeins']   |   nan |              | ['temptest657429585@gmail.com']                    |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='Benniebeins', password_hash='sVmHPUij0be80f308b35404cb9603fcfb23a95b0')]                                    |                        |              |                | 02.05.2019  |
| ['Bjyffr Atlecz']               |   nan |              | ['ccohen23@me.com']                                |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='atlecz', password_hash='7ihviyuN8bd922468f1c6b6e68988388414c8452')]                                         |                        |              |                | 19.07.2020  |
| ['Chesn Ilya Serg']             |     1 | 01.04.1988   | ['guest_mr8va6dpavfbclzfkhjhy0y82ygpbmio@kant.ru'] | ['79068002282'] | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='guest_mr8va6dpavfbclzfkhjhy0y82ygpbmio@kant.ru', password_hash='HpOwaU38dd8254ca2e9766b979202dac6ea10704')] |                        |              |                | 05.06.2020  |
| ['Darrellhoadsfz Darrellhoads'] |   nan |              | ['malevtina704@gmail.com']                         |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='Darrellhoads', password_hash='bjpDoZBTa69ee9bfa2859ade2ed9425ed3909d23')]                                   |                        |              |                | 09.10.2019  |
| ['Davidchaicph Davidkib']       |   nan |              | ['srgplesh@yandex.by']                             |                 | [Row(title='Спортивные магазины КАНТ', link='https://www.kant.ru', login='Davidkib', password_hash='pI02wlDpb4521d56f290644b10433968ac7043dc')]                                       |                        |              |                | 04.07.2020  |
```