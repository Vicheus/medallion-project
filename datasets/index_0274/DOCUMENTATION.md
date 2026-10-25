# Parsetron results

## About row data

> - Code name: index_0274
> - File path: /media/user/SAMSUNG/Databases/index_0274/raw/vitaexpress.ru/preprocessed/users_preprocessed.csv
> - Total rows: 666944

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
 |-- PERSONAL_PROFESSION: long (nullable = true)
 |-- PERSONAL_WWW: string (nullable = true)
 |-- PERSONAL_ICQ: string (nullable = true)
 |-- PERSONAL_GENDER: string (nullable = true)
 |-- PERSONAL_BIRTHDATE: string (nullable = true)
 |-- PERSONAL_PHOTO: string (nullable = true)
 |-- PERSONAL_PHONE: double (nullable = true)
 |-- PERSONAL_FAX: string (nullable = true)
 |-- PERSONAL_MOBILE: string (nullable = true)
 |-- PERSONAL_PAGER: string (nullable = true)
 |-- PERSONAL_STREET: string (nullable = true)
 |-- PERSONAL_MAILBOX: string (nullable = true)
 |-- PERSONAL_CITY: string (nullable = true)
 |-- PERSONAL_STATE: string (nullable = true)
 |-- PERSONAL_ZIP: string (nullable = true)
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
 |-- XML_ID: string (nullable = true)
 |-- PERSONAL_BIRTHDAY: date (nullable = true)
 |-- EXTERNAL_AUTH_ID: string (nullable = true)
 |-- CHECKWORD_TIME: timestamp (nullable = true)
 |-- SECOND_NAME: string (nullable = true)
 |-- CONFIRM_CODE: string (nullable = true)
 |-- LOGIN_ATTEMPTS: integer (nullable = true)
 |-- LAST_ACTIVITY_DATE: string (nullable = true)
 |-- AUTO_TIME_ZONE: string (nullable = true)
 |-- TIME_ZONE: string (nullable = true)
 |-- TIME_ZONE_OFFSET: string (nullable = true)
 |-- TITLE: string (nullable = true)
 |-- BX_USER_ID: string (nullable = true)
 |-- LANGUAGE_ID: string (nullable = true)

```

### Data sample
```
|   ID | TIMESTAMP_X         | LOGIN                     | PASSWORD                                 | CHECKWORD                                | ACTIVE   | NAME                      | LAST_NAME   | EMAIL                         | LAST_LOGIN          | DATE_REGISTER       | LID   |   PERSONAL_PROFESSION | PERSONAL_WWW   | PERSONAL_ICQ   | PERSONAL_GENDER   | PERSONAL_BIRTHDATE   | PERSONAL_PHOTO   |   PERSONAL_PHONE | PERSONAL_FAX   | PERSONAL_MOBILE   | PERSONAL_PAGER   | PERSONAL_STREET   | PERSONAL_MAILBOX   | PERSONAL_CITY   | PERSONAL_STATE   | PERSONAL_ZIP   |   PERSONAL_COUNTRY | PERSONAL_NOTES   | WORK_COMPANY   | WORK_DEPARTMENT   | WORK_POSITION   | WORK_WWW   | WORK_PHONE   | WORK_FAX   | WORK_PAGER   | WORK_STREET   | WORK_MAILBOX   | WORK_CITY   | WORK_STATE   | WORK_ZIP   |   WORK_COUNTRY | WORK_PROFILE   | WORK_LOGO   | WORK_NOTES   | ADMIN_NOTES   | STORED_HASH   | XML_ID   | PERSONAL_BIRTHDAY   | EXTERNAL_AUTH_ID   | CHECKWORD_TIME      | SECOND_NAME   | CONFIRM_CODE   |   LOGIN_ATTEMPTS | LAST_ACTIVITY_DATE   | AUTO_TIME_ZONE   | TIME_ZONE   | TIME_ZONE_OFFSET   | TITLE   | BX_USER_ID                       | LANGUAGE_ID   |
|-----:|:--------------------|:--------------------------|:-----------------------------------------|:-----------------------------------------|:---------|:--------------------------|:------------|:------------------------------|:--------------------|:--------------------|:------|----------------------:|:---------------|:---------------|:------------------|:---------------------|:-----------------|-----------------:|:---------------|:------------------|:-----------------|:------------------|:-------------------|:----------------|:-----------------|:---------------|-------------------:|:-----------------|:---------------|:------------------|:----------------|:-----------|:-------------|:-----------|:-------------|:--------------|:---------------|:------------|:-------------|:-----------|---------------:|:---------------|:------------|:-------------|:--------------|:--------------|:---------|:--------------------|:-------------------|:--------------------|:--------------|:---------------|-----------------:|:---------------------|:-----------------|:------------|:-------------------|:--------|:---------------------------------|:--------------|
|    1 | 2023-04-20 01:02:48 | admin@vitaexpress.ru      | g8T=I2=n1ce392e425244060bf960ded68c54869 | RkZhWQQFe6d2fd9c8da444b18d587cfdc7b7972e | Y        | Администратор Сайта Сайта | Сайта       | admin@vitaexpress.ru          | 2023-04-20 05:02:41 | 2015-08-29 17:04:00 | s1    |                   nan |                |                |                   |                      |                  |      9.17013e+09 |                |                   |                  | ул. Тестовая 47   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2022-06-03 11:56:08 |               |                |                0 |                      |                  |             |                    |         | bdb908dc17983026088fec4c0cb95ca9 |               |
|    4 | 2022-07-12 09:17:05 | alikperova@vita-samara.ru | m5V+C0b?d1521d738b1de51d79d54d746f71ec0d | pODtNsZZ841e515d8fe0310324de553c92d1c460 | Y        | Евгения                   | А           | alikperova@vita-samara.ru     | 2022-07-12 13:16:44 | 2016-04-03 14:54:15 | s1    |                   nan |                |                |                   |                      |                  |    nan           |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2017-09-15 09:44:58 | Владимировна  |                |                0 |                      |                  |             |                    | Тест    | d37d91a6e71d3363e3745253b3ad15f6 |               |
|    7 | 2019-12-27 10:35:16 | osinads                   | [Di52fM%0c30b0c0df4a93f3d7b5766e93b08ce2 | zbYXKnGt0620e73018c31d9c57fab75db981df5a | Y        | Дарья                     |             | d.osina@inbox.ru              | 2016-06-22 14:28:12 | 2016-06-21 16:31:23 | s1    |                   nan |                |                |                   |                      |                  |    nan           |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2016-10-26 10:56:51 |               |                |                1 |                      |                  |             |                    |         | 8d7407b2c932fce1789590c5ff0aae4c |               |
|   21 | 2017-06-23 06:24:20 | Scherzo                   | 0M\pP*z75734e184a9e965d1d0a6e51df177f1a8 | ks8t2B8ie19e0823efe84e9ae2d6217edc3d310a | Y        | Scherzo                   |             | n.moiseenkova101@gmail.com    | 2016-07-13 16:42:50 | 2016-07-13 16:42:50 | s1    |                   nan |                |                |                   |                      |                  |    nan           |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2017-06-23 10:24:20 |               |                |                0 |                      |                  |             |                    |         | 0c32a28e72b3cad8a42fffcf50a22edf |               |
|   23 | 2021-06-21 12:39:01 | Boroviig                  | 5Qt{/iQ90fd5890f290fbd689553a33e5462544c | R2hLf5m334f29e49f7930112e3ef412d6ffaf5ab | Y        | Igor Borovikov            |             | igor.logistic@me.com          | 2021-06-21 16:39:01 | 2016-07-28 18:20:09 | s1    |                   nan |                |                |                   |                      |                  |      9.17943e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2020-08-17 20:41:27 |               |                |                0 |                      |                  |             |                    |         | a56c58d39959e3c0db7d9ee286899d2a |               |
|   24 | 2022-06-23 12:14:35 | Akramova                  | aYpBLNFV8b791f6ecd906a5026572008b4afef9d | U1ZdwSBF04518b5c292963a7231a300cda48e41b | Y        | Елена                     |             | panda990@mail.ru              | 2021-02-28 00:41:21 | 2016-08-01 15:35:12 | s1    |                   nan |                |                |                   |                      |                  |      9.17872e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2022-06-23 16:14:35 |               |                |                0 |                      |                  |             |                    |         | 0a549b3d3046e263d0de90f10e8afebc |               |
|   31 | 2019-12-27 10:34:08 | solomatov@vita-samara.ru  | qC)9O8y$ff5be07ac99436c9083beae98bd7e58f | Gl4KLGL51e95387c4e7cdf0a8b20fd77e4f9755f | Y        | Илья                      |             | solomatov@vita-samara.ru      | 2018-07-16 16:01:32 | 2016-08-19 10:52:34 | s1    |                   nan |                |                |                   |                      |                  |      9.27652e+09 |                |                   |                  |                   |                    |                 |                  |                |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |          |                     |                    | 2018-07-16 16:26:27 |               |                |                0 |                      |                  |             |                    |         | f10808fccd40b2f5bb369c9145f06fb4 |               |
|   37 | 2019-12-27 10:34:08 | test01                    | WXbdj3KF8c6ef6a5afca4ef8080f919616f83ad4 | Ibc7IU5q2d70b622455cc24877881266fc6094d6 | Y        | test                      |             | fedorov.vitaliy_163@mail.ru   | 2016-08-29 09:43:53 | 2016-08-29 09:43:53 | s1    |                   nan |                |                |                   |                      |                  |      9.27716e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2016-10-26 10:55:40 |               |                |                1 |                      |                  |             |                    |         |                                  |               |
|   38 | 2022-07-18 10:58:34 | alla.m44@mail.ru          | kR8~0cL=deca8f45dc1e664b3a96e5bd28c56ff1 | VBVGeFzB7556bb669897fd34a313b1fa79c7dc5b | Y        | Алла                      |             | alla.m44@mail.ru              | 2022-07-18 14:58:09 | 2016-08-31 10:55:20 | s1    |                   nan |                |                |                   |                      |                  |      9.64982e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2021-02-11 10:53:08 |               |                |                1 |                      |                  |             |                    |         | 3a65651e514f327199e339a3055efe07 |               |
|   39 | 2019-12-27 10:34:08 | ???                       | lXXiaTv766ae4b53ce8893a1f1c9d08bec8b486b | 6siUV7B85c1a42ef35e1d8d65d6c0ec2d239cd0b | Y        | евгений                   |             | evgeny.yankov@advacapital.com | 2016-09-28 05:34:37 | 2016-09-28 05:34:37 | s1    |                   nan |                |                |                   |                      |                  |      9.85227e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2016-10-26 10:03:40 |               |                |                0 |                      |                  |             |                    |         |                                  |               |
|   40 | 2016-11-01 13:04:47 | popova.sv                 | Th)5.aZ88e89601379e843d33c2371311f0c33d2 | zBI8QxnD9ecaad7e432f27253d89a83186947b39 | Y        | Светлана                  |             | popova.sv@vita-samara.ru      | 2016-11-02 09:31:12 | 2016-09-28 10:31:12 | s1    |                   nan |                |                |                   |                      |                  |    nan           |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2016-11-01 17:04:47 |               |                |             5761 |                      |                  |             |                    |         | 58f701ca1bcf79df827e229136362f0a |               |
|   41 | 2019-12-27 10:34:08 | sveta100779               | yEuht4I88a5265f03febcb2b74575822bb8f6f3c | isAqd317cf6d69c221df9ea8e3692ed752b8a716 | Y        | Любовь                    |             | sveta100779@mail.ru           | 2016-10-19 16:00:57 | 2016-10-19 16:00:57 | s1    |                   nan |                |                |                   |                      |                  |      9.06338e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2016-10-26 10:00:31 |               |                |                7 |                      |                  |             |                    |         | 050e78edfbd7201f20463412e7e2588d |               |
|   42 | 2017-01-08 10:02:47 | Анна                      | L9k<-Qe1f91267ab28ecef6cdf60625dc7755bfa | s4QXjfjC30458d740947b0fc0b7e3000f917d0d7 | Y        | Анна                      |             | werty-83@yandex.ru            | 2016-10-21 14:03:50 | 2016-10-20 08:02:54 | s1    |                   nan |                |                |                   |                      |                  |    nan           |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2017-01-08 14:02:47 |               |                |             2869 |                      |                  |             |                    |         | 39fd328e46a9686aff1753f651869a03 |               |
|   43 | 2019-12-27 10:34:08 | ellytob                   | %T3ycS[53e06abcc7b3ecbf0381e323fd7a3181e | wb1X9hFaffb8221dff87b8c0d3bd9a4df598b881 | Y        | Эльмира                   |             | ellytob@rambler.ru            | 2019-11-14 11:30:16 | 2016-10-20 10:40:12 | s1    |                   nan |                |                |                   |                      |                  |      9.17922e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2019-11-14 11:29:28 |               |                |                1 |                      |                  |             |                    |         | 623d3e2bfdae60640a955bf2d162a66c |               |
|   44 | 2019-12-27 10:34:08 | kolesnikowa               | k0WRDoLT1e4816af0ef14d16f18ce452e8e25e0a | UkYYswNkc7b2a1007d74194a86805105ad8320a2 | Y        | Альфия                    |             | a6@vita-samara.ru             | 2016-10-20 11:57:32 | 2016-10-20 11:57:32 | s1    |                   nan |                |                |                   |                      |                  |      9.03302e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2016-10-26 09:40:30 |               |                |                1 |                      |                  |             |                    |         | d1db9e076984b10e57a0e2cfe222d3ba |               |
|   45 | 2019-12-27 10:34:08 | liliya-ibatullin@mail.ru  | EaWID4IJd968d28d534e103751c16ed7cd3372ec | E0RrddJA2d553e4d64f61142b5e795670cf71fd9 | Y        | Лилия                     |             | liliya-ibatullin@mail.ru      | 2016-10-21 16:07:01 | 2016-10-20 12:04:45 | s1    |                   nan |                |                |                   |                      |                  |      9.03342e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2016-10-26 11:19:09 |               |                |                0 |                      |                  |             |                    |         | 194003ced929fcabfbee85c36833234e |               |
|   46 | 2019-12-27 10:34:08 | unc21@yandex.ru           | _M5x(3Dib13303bd564ef2ac7864dab7c139ee72 | trqLuGAaae1040a2fd25d48fd0260669a43b5505 | Y        | Малюгина Е.Н.             |             | unc21@yandex.ru               | 2017-06-25 17:09:41 | 2016-10-20 12:17:03 | s1    |                   nan |                |                |                   |                      |                  |      9.27902e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2017-06-21 13:00:13 |               |                |                0 |                      |                  |             |                    |         | 536f98872a50dcc5d40318b504e1843e |               |
|   47 | 2022-03-14 09:45:02 | almelion                  | _Qj9U6h!7d229ab046fb1d4a7d4890986ad8d668 | RWu7FP1V95ba6411b55385ed73aad8a328f7928b | Y        | Васисуалий                |             | almelion@rambler.ru           | 2022-03-14 13:32:20 | 2016-10-20 12:42:25 | s1    |                   nan |                |                |                   |                      |                  |      9.03308e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2022-03-08 21:07:51 |               |                |                0 |                      |                  |             |                    |         | d10ccec501599a129c2da89655061293 |               |
|   48 | 2019-12-27 10:34:07 | нина                      | 0ChORnO266683890070b922988955833c918d2e0 | eI11hIuydd7a05e01eb2be36ce4acaf8aae10341 | Y        | кутейкина                 |             | kutejkina.nina@yandex.ru      | 2016-10-20 12:46:56 | 2016-10-20 12:46:56 | s1    |                   nan |                |                |                   |                      |                  |      9.05331e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2016-10-26 10:02:02 |               |                |              429 |                      |                  |             |                    |         | e39a00a55b6670ec460e03a80274d72f |               |
|   49 | 2022-06-23 12:14:35 | Vita36                    | %2Rn4n&Kc69bfede993f8276cb551a17dbd4d72f | t4GVccry54e56fdafcda6cdcf13bc008fb5ded2e | Y        | Анна                      |             | annmuhacheva@mail.ru          | 2017-06-16 14:40:21 | 2016-10-20 12:56:46 | s1    |                   nan |                |                |                   |                      |                  |      9.08388e+09 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |          |                     |                    | 2022-06-23 16:14:35 |               |                |                0 |                      |                  |             |                    |         | 5a0b4ffcf088e03b3ad19b056962161f |               |
```

> - Code name: index_0274
> - File path: /media/user/SAMSUNG/Databases/index_0274/raw/vitaexpress.ru/preprocessed/*from_orders_preprocessed.csv
> - Total rows: 432490

### Schema
```
root
 |-- UF_CREATED_AT: string (nullable = true)
 |-- name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- email: string (nullable = true)
 |-- relation_name: string (nullable = true)
 |-- relation_phone: string (nullable = true)
 |-- city: string (nullable = true)
 |-- address: string (nullable = true)

```

### Data sample
```
| UF_CREATED_AT       | name                  |            phone | email                     | relation_name      | relation_phone   | city              | address                                                                            |
|:--------------------|:----------------------|-----------------:|:--------------------------|:-------------------|:-----------------|:------------------|:-----------------------------------------------------------------------------------|
| 2023-05-11 02:50:32 | testdummy             | 7846322223223322 | dummy@dummy.dum           | bno                | bpo              | c                 | string                                                                             |
| 2023-05-11 03:18:52 | testdummy             | 7846322223223322 | dummy@dummy.dum           | bno                | bpo              | c                 | string                                                                             |
| 2023-05-11 03:32:54 | Айрат Ayrat           |      89177355316 | yuliyaaprel34@gmail.com   |                    |                  | Уфа               | Россия, Республика Башкортостан, Уфа, улица Асхата Мирзагитова, 12                 |
| 2023-05-11 03:32:54 | Радмила  Азиатцева    |      79120209197 | azimilly1016@gmail.com    |                    |                  | Самара            | Россия, Самара, Запорожская улица, 43                                              |
| 2023-05-11 03:32:54 | Валентина Г.          |      79877911341 | MadSo@yandex.ru           |                    |                  | Оренбург          | Россия, Оренбург, микрорайон Форштадт, улица Потехина, 30                          |
| 2023-05-11 03:32:54 | Наталья Арапкина      |      79022678971 | nata.arapkina@mail.ru     |                    |                  | Екатеринбург      | Россия, Свердловская область, Екатеринбург, жилой район Уралмаш, улица Хмелева, 18 |
| 2023-05-11 03:32:54 | Валерия Бажанова      |      79171181259 | valkim993@gmail.com       |                    |                  | Самара            | Россия, Самара, Самарская улица, 268                                               |
| 2023-05-11 03:32:54 | Анна Колесникова      |      79119451964 | kolesnekova76@mail.ru     |                    |                  | Гатчина           | Россия, Ленинградская область, Гатчина, улица Достоевского, 12                     |
| 2023-05-11 03:32:55 | Антон Мельничников    |      79214088062 | melnichnikov1991@mail.ru  | Рита Шкя           | 79117390066      | Санкт-Петербург   | Россия, Санкт-Петербург, Арцеуловская аллея, 19                                    |
| 2023-05-11 03:32:55 | Юлия Рычкова          |      79385307137 | Julianafitness@yandex.ru  |                    |                  | Краснодар         | Россия, Краснодар, Бородинская улица, 150Бк1                                       |
| 2023-05-11 03:32:55 | Снежана Шабанова      |      79171421702 | sneghana000@mail.ru       | Сабина Тавакаловна | 79991556996      | Казань            | Россия, Республика Татарстан, Казань, Комсомольская улица, 2                       |
| 2023-05-11 03:32:55 | Андрей Никитин        |      79991719739 | Andreynikitin1998@mail.ru |                    |                  | Каменск-Уральский | Россия, Свердловская область, Каменск-Уральский, Каменская улица, 86               |
| 2023-05-11 03:32:55 | Эльмира Ахкамутдинова |      79196136729 | altafovna1970@yandex.ru   | Руфина Сагидуллина | 79872583369      | Екатеринбург      | Россия, Свердловская область, Екатеринбург, улица Очеретина, 3                     |
| 2023-05-11 03:32:55 | Наталия Шарапова      |      79171648614 | spiegel.merle@gmail.com   |                    |                  | Самара            | Россия, Самара, проспект Карла Маркса, 207                                         |
| 2023-05-11 03:32:55 | Михаил Востригин      |      79185433314 | wind.walk.v@gmail.com     |                    |                  | Москва            | Россия, Москва, Гвардейская улица, 14                                              |
| 2023-05-11 03:32:55 | Яна Бобина            |      79536461499 | JanaBobina@mail.ru        | Зоя  Верезуб       | 79201183222      | Ярославль         | Россия, Ярославль, Московский проспект, 108                                        |
| 2023-05-11 03:32:55 | Олеся  Стручкова      |      79213600115 | Olesya.red@mail.ru        |                    |                  | Санкт-Петербург   | Россия, Санкт-Петербург, улица Вадима Шефнера, 10к1                                |
| 2023-05-11 03:32:55 | Ильяс Зилидинов       |      79276988705 | scream2408@rambler.ru     | Алина Зилидинова   | 79277116115      | Самара            | Россия, Самара, улица Мяги, 7                                                      |
| 2023-05-11 03:32:55 | Александра  Ковалева  |      79962402204 | smm.kovaleva@gmail.com    |                    |                  | Ярославль         | Россия, Ярославль, Мануфактурная улица, 28                                         |
| 2023-05-11 03:32:55 | Анастасия  Красная    |      79639413257 | mayfau@mail.ru            |                    |                  | Санкт-Петербург   | Россия, Санкт-Петербург, бульвар Новаторов, 25                                     |
```


## About final data
> - Total rows: 647246

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- actuality: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- relations: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Columns completeness
```
{
    "names": 100.0,
    "phones": 11.0,
    "emails": 99.9,
    "sex": 72.32,
    "birth_date": 60.24,
    "actuality": 96.42,
    "accounts": 99.84,
    "relations": 0.03,
    "address": 0.15
}
```

### Data sample
```
| names          | phones          | emails                         |   sex | birth_date   | actuality   | accounts                                                                                                                                                | relations   | address   |
|:---------------|:----------------|:-------------------------------|------:|:-------------|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|:----------|
| ['Aleksandra'] |                 | ['alekom@list.ru']             |   nan |              | 17.11.2020  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='alekom@list.ru', password_hash='Gu3QpIyh6dca130d4522caafc8baca24fda53999')]             |             |           |
| ['Aleksandra'] |                 | ['alleksa_74@mail.ru']         |   nan |              | 09.08.2017  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='Alleksa_74', password_hash='kyolSjDM5c23a49e8d498e6ce545a47868037ee2')]                 |             |           |
| ['Anna']       | ['79050505219'] | ['anna.slyusar.83@mail.ru']    |   nan |              | 12.03.2020  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='anna.slyusar.83@mail.ru', password_hash='ddrIRJ7038b921d64b745e87e68ab1a6024ed493')]    |             |           |
| ['Aнна']       |                 | ['anna9-9494_2011@mail.ru']    |     0 |              | 02.04.2022  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='anna9-9494_2011@mail.ru', password_hash='5CuGsp7T8150c06df2088c326a0282a31f65018e')]    |             |           |
| ['Cергей']     |                 | ['viktorov.serj@mail.ru']      |     1 | 10.01.2002   | 08.01.2022  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='viktorov.serj@mail.ru', password_hash='dJUz83C6bae9f147f511f06ba969fa8ec6068cae')]      |             |           |
| ['Cофья']      | ['79776554469'] | ['ycinas@mail.ru']             |     0 | 19.02.1950   | 15.03.2021  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='ycinas@mail.ru', password_hash='D24SmrsX0bee7fbe19d25f171664ab3da7428542')]             |             |           |
| ['Inessa']     |                 | ['inessatimofeeva@yandex.ru']  |   nan |              | 15.11.2017  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='inessatimofeeva@yandex.ru', password_hash='kEgOqbMZc0ef45cfc1c4eea7dd33b9c747f29e97')]  |             |           |
| ['Khav']       |                 | ['khav79@mail.ru']             |   nan |              | 31.05.2019  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='khav79@mail.ru', password_hash='qfKy2K1N02a9e22915ba3cb9132742b86cc9f756')]             |             |           |
| ['Konstantin'] |                 | ['akv-reg@mail.ru']            |   nan |              | 11.03.2022  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='akv-reg@mail.ru', password_hash='LfqBosTR5406a517792ce3a4e465456eeb66bf4d')]            |             |           |
| ['Ksenia']     |                 | ['fedorovaoksana17@yandex.ru'] |   nan |              | 20.03.2019  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='fedorovaoksana17@yandex.ru', password_hash='kOzqMj3A4328bae6c0f7e1e3cf4c5c498320a912')] |             |           |
| ['Lera']       |                 | ['lera_1985_11@mail.ru']       |   nan |              | 21.09.2018  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='lera_1985_11@mail.ru', password_hash='uMy5YXhlba85eb62f946e80815635775432fef3e')]       |             |           |
| ['Lyudmila']   |                 | ['gordeeva_lisa@mail.ru']      |   nan |              | 05.02.2018  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='gordeeva_lisa@mail.ru', password_hash='54Rp8VdDd21b1ec18ddfbba1c188c635818b974a')]      |             |           |
| ['Natalia']    | ['79222918559'] | ['anatalie2@list.ru']          |   nan |              | 03.06.2019  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='anatalie2@list.ru', password_hash='IlhomgSn214ca129263d8c312d778fdba7908a6e')]          |             |           |
| ['Oksana']     |                 | ['arsakova@rambler.ru']        |   nan |              | 05.04.2019  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='Arsakova@rambler.ru', password_hash='4jZ?V8k.a91f7cbda0723dc5bf6fc11bf0cce7a0')]        |             |           |
| ['Olesya']     | ['79028774869'] | ['ovsvetlova@yandex.ru']       |   nan |              | 11.01.2022  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='Ovsvetlova@yandex.ru', password_hash='nBV1RPzI7d4e715d5b470aa74dac2de73edc46bd')]       |             |           |
| ['Olga']       |                 | ['111l@bk.ru']                 |   nan |              |             | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='111l@bk.ru', password_hash='eVEwkVxi7cf8f9cbe7c18ad1b42c7867d20e029a')]                 |             |           |
| ['Olga']       |                 | ['olga.zhaldybina@mail.ru']    |   nan |              | 01.12.2020  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='olga.zhaldybina@mail.ru', password_hash='AvbwvDLY498362b763e29f5f2d02305851770908')]    |             |           |
| ['Olga']       |                 | ['tigra-88@bk.ru']             |   nan |              | 13.05.2022  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='tigra-88@bk.ru', password_hash='birU2UDif54a2a4ed68c3cb4b6838b43147804f7')]             |             |           |
| ['Olga Gilm']  |                 | ['olgagilm@mail.ru']           |   nan |              | 02.08.2022  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='olgagilm@mail.ru', password_hash='|Dm0N4/v0653918fa9cddbcbe265ba78c2581a89')]           |             |           |
| ['Ruslan']     |                 | ['vitaexpress.ru@yandex.ru']   |   nan |              | 10.04.2018  | [Row(title='Аптека Вита', link='https://vitaexpress.ru', login='vitaexpress.ru@yandex.ru', password_hash='4AUOmcS880b229675fab1fadec996547bdc6e030')]   |             |           |
```