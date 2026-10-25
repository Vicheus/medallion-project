# Parsetron results

## About row data

> - File path: users_b_form_result.csv
> - Total rows: 29882

### Schema
```
root
 |-- RESULT_ID: string (nullable = true)
 |-- name: string (nullable = true)
 |-- email_1: string (nullable = true)

```

### Data sample
```
|   RESULT_ID | name             | email_1                    |
|------------:|:-----------------|:---------------------------|
|         177 | Ксения           | Voskresenskayak@mail.ru    |
|         299 | Вячеслав         | bordo2006@yandex.ru        |
|         442 | Смыслова Елена   |                            |
|         642 | Мила             | velimirovna@gmail.com      |
|         739 | Екатерина        | Lola_sterina@mail.ru       |
|         741 | Шишляева Наталья | Shishlyaeva@mail.ru        |
|         744 | Раиса            | rgshakirova@ya.ru          |
|         829 | Алексей          | Zarudnev976@mail.ru        |
|         872 | ольга            | okabaeva@mail.ru           |
|        1026 | Наталья          | tesh-dem@mail.ru           |
|        1085 | Майя             | ama3@bk.ru                 |
|        1121 | Марина           | myhappychance@ya.ru        |
|        1130 | Алёна            | makeeva-alena@rsmbler.ru   |
|        1131 | Алёна            | makeeva-alena@rambler.ru   |
|        1171 | сысова оксана    | sysova.kdl@yandex.ru       |
|        1211 | Ольга            | la-plus-belle@yandex.ru    |
|        1423 | Юлия             | Pashinyan.Yuliya@yandex.ru |
|        1589 | Алексей          | andreev_a@mail.ru          |
|        1642 | Андрон           | andron.yann@yandex.ru      |
|        1648 | Мария            | konopitskaya@gmail.com     |
```

> - File path: users_b_sale_order_props.csv
> - Total rows: 30000

### Schema
```
root
 |-- ORDER_ID: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- address: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)

```

### Data sample
```
|   ORDER_ID | name      | lastname   | address                                                   | email                                | phone              |
|-----------:|:----------|:-----------|:----------------------------------------------------------|:-------------------------------------|:-------------------|
|        587 | Алена     | Парамонова | Москва,  Остоженка, д. 40                                 | alena@paramonova.com                 | 89263873483        |
|        757 | Анна      | Шитова     | Москва,  Новый Арбат, д. 19                               | asheetova@gmail.com                  | +7 (985) 410-31-97 |
|        759 | Артем     | К          | Свердловская обл, г. Екатеринбург,  Гагарина, д. 35       | Koscheevartem@gmail.com              | +79220255777       |
|        775 | Александр | Харунжа    | Новый Арбат, д. 19                                        | rolland@alterego.biz.ua              | +7 (123) 345-34-53 |
|        780 | Александр | Харунжа    | Новый Арбат, д. 19                                        | rolland@alterego.biz.ua              | +7 (123) 345-34-53 |
|        781 | Елена     |            | Москва,  Милютинский, д. 9, кв. оф 101                    | 89166499632-1432635467@bosco.ru      | 89166499632        |
|        788 | Иван      | Машканцев  |                                                           | depechemodefan@alterego.biz.ua       | 1234567            |
|        790 | Иван      | Машканцев  |                                                           | depechemodefan@alterego.biz.ua       | 1234567            |
|        803 | Дина      | Калугина   | Москва,  Пенягинская, д. 16, кв. 6                        | dkalugina@yandex.ru                  | +7 (985) 233-67-44 |
|        809 | Юлия      | Немерюк    | Москва,  Беговая, д. 3 корпус 1/1                         | yulianem@mail.ru                     | +7 (985) 762-02-44 |
|        811 | Людмила   |            | Москва,  Академика Сахарова, д. 9                         | +79859912935-1432806141@www.bosco.ru | +7 (985) 991-29-35 |
|        812 | Елена     | Валеева    | Калининградская обл, г. Озерск,  Пушкина, д. 3, кв. 4     | valeeva-lena@yandex.ru               | +7 (922) 237-40-24 |
|        821 | Елена     | Смыслова   | Саратовская обл, г. Саратов,  Пугачевский-1 пос.б, д. 44Б | cits@overta.ru                       | +7 (927) 223-65-56 |
|        835 | Елена     | Шнейдер    | Москва,  Ленинградский проспект, д. 31А/1, кв. 17 этаж    | e.shneider@ftc.ru                    | 89164343935        |
|        836 | Ирина     | Тамадаева  | Москва,  Пугачевская 2-я, д. 10/2, кв. 80                 | zara.tamadaeva@yandex.ru             | +7 (926) 484-48-68 |
|        884 | Иван      | Машканцев  |                                                           | depechemodefan@alterego.biz.ua       | 1234567            |
|        888 | Ирина     | Автономова | Москва,  Крылатская, д. 45/3, кв. 51                      | iri-load@yandex.ru                   | 89251212211        |
|        945 | Александр | Харунжа    | Москва,  Бориса Галушкина, д. 123                         | rolland@alterego.biz.ua              | +7 (123) 345-34-53 |
|        946 | Елена     | Ягодкина   | Москва,  Осенний, д. 7/2                                  | emy70@mail.ru                        | 89197737347        |
|        947 | Артем     | К          | Свердловская обл, г. Екатеринбург,  Гагарина, д. 35/А     | Koscheevartem@gmail.com              | +79220255777       |
```

> - File path: users_b_user.csv
> - Total rows: 516859

### Schema
```
root
 |-- ID: string (nullable = true)
 |-- TIMESTAMP_X: string (nullable = true)
 |-- LOGIN: string (nullable = true)
 |-- PASSWORD: string (nullable = true)
 |-- CHECKWORD: string (nullable = true)
 |-- ACTIVE: string (nullable = true)
 |-- NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- LAST_LOGIN: timestamp (nullable = true)
 |-- DATE_REGISTER: string (nullable = true)
 |-- LID: string (nullable = true)
 |-- PERSONAL_PROFESSION: string (nullable = true)
 |-- PERSONAL_WWW: string (nullable = true)
 |-- PERSONAL_ICQ: string (nullable = true)
 |-- PERSONAL_GENDER: string (nullable = true)
 |-- PERSONAL_BIRTHDATE: string (nullable = true)
 |-- PERSONAL_PHOTO: integer (nullable = true)
 |-- PERSONAL_PHONE: decimal(20,0) (nullable = true)
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
 |-- WORK_COUNTRY: string (nullable = true)
 |-- WORK_PROFILE: timestamp (nullable = true)
 |-- WORK_LOGO: timestamp (nullable = true)
 |-- WORK_NOTES: string (nullable = true)
 |-- ADMIN_NOTES: integer (nullable = true)
 |-- STORED_HASH: integer (nullable = true)
 |-- XML_ID: string (nullable = true)
 |-- PERSONAL_BIRTHDAY: date (nullable = true)
 |-- EXTERNAL_AUTH_ID: string (nullable = true)
 |-- CHECKWORD_TIME: string (nullable = true)
 |-- SECOND_NAME: string (nullable = true)
 |-- CONFIRM_CODE: string (nullable = true)
 |-- LOGIN_ATTEMPTS: string (nullable = true)
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
|   ID | TIMESTAMP_X         | LOGIN                                              | PASSWORD                                 | CHECKWORD                                | ACTIVE   | NAME        | LAST_NAME         | EMAIL                                              | LAST_LOGIN          | DATE_REGISTER       | LID   | PERSONAL_PROFESSION   | PERSONAL_WWW   | PERSONAL_ICQ   | PERSONAL_GENDER   | PERSONAL_BIRTHDATE   |   PERSONAL_PHOTO |   PERSONAL_PHONE | PERSONAL_FAX   | PERSONAL_MOBILE   | PERSONAL_PAGER   | PERSONAL_STREET   | PERSONAL_MAILBOX   | PERSONAL_CITY   | PERSONAL_STATE   | PERSONAL_ZIP   |   PERSONAL_COUNTRY | PERSONAL_NOTES   | WORK_COMPANY   | WORK_DEPARTMENT   | WORK_POSITION   | WORK_WWW   |   WORK_PHONE | WORK_FAX   | WORK_PAGER   | WORK_STREET   | WORK_MAILBOX   | WORK_CITY   | WORK_STATE   | WORK_ZIP   |   WORK_COUNTRY | WORK_PROFILE   | WORK_LOGO   | WORK_NOTES   |   ADMIN_NOTES |   STORED_HASH | XML_ID   | PERSONAL_BIRTHDAY   | EXTERNAL_AUTH_ID   | CHECKWORD_TIME      | SECOND_NAME   | CONFIRM_CODE   |   LOGIN_ATTEMPTS | LAST_ACTIVITY_DATE   | AUTO_TIME_ZONE   | TIME_ZONE   | TIME_ZONE_OFFSET   | TITLE   | BX_USER_ID                       | LANGUAGE_ID   |
|-----:|:--------------------|:---------------------------------------------------|:-----------------------------------------|:-----------------------------------------|:---------|:------------|:------------------|:---------------------------------------------------|:--------------------|:--------------------|:------|:----------------------|:---------------|:---------------|:------------------|:---------------------|-----------------:|-----------------:|:---------------|:------------------|:-----------------|:------------------|:-------------------|:----------------|:-----------------|:---------------|-------------------:|:-----------------|:---------------|:------------------|:----------------|:-----------|-------------:|:-----------|:-------------|:--------------|:---------------|:------------|:-------------|:-----------|---------------:|:---------------|:------------|:-------------|--------------:|--------------:|:---------|:--------------------|:-------------------|:--------------------|:--------------|:---------------|-----------------:|:---------------------|:-----------------|:------------|:-------------------|:--------|:---------------------------------|:--------------|
|    1 | 2023-08-29 10:55:07 | lena@paramonova.com                                | }6uE|Yk96010b424813b8d43e3849021cfe92b81 | FmtU9C7p89f97c3ad3fb468dd7b97e65316446a6 | Y        | Admin       | 1                 | lena@paramonova.com                                | 2024-08-26 12:52:18 | 2014-11-07 15:25:08 | s5    |                       |                |                | F                 |                      |              nan |      7.12312e+10 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          | 2016-09-05          |                    | 2022-09-01 17:15:42 |               |                |                0 | 0000-00-00 00:00:00  |                  |             |                    |         | 215b96f639b5b7b49a7131c4aebb30fa |               |
|    3 | 2023-12-19 21:12:46 | alena@paramonova.com                               | f)9L4;Gdca8c821cd10fcf8b6e4545077f3c9c26 | AaIzTEUWa93392f11b2c5d8a8ab52d1d1c588b10 | Y        | Алена       | Парамонова        | alena@paramonova.com                               | 2024-02-16 21:51:18 | 2014-11-22 21:45:15 | s5    |                       |                |                | F                 |                      |              nan |      7.92639e+10 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |  89263873483 |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          | 1984-07-05          |                    | 2023-12-19 21:12:46 | Александровна |                |                0 | 0000-00-00 00:00:00  |                  |             |                    |         | 6c121ae1d8579913b8307df1335ab229 |               |
|    4 | 2017-11-20 09:55:08 | bx_crm_import_user_xccoe@gisele.alterego-russia.ru | 4As<^Lm19fbe37c668eff7fbde4bdd11f0da8547 | Ksnau2e112848076b2cbafc877bccfca5b7d37bf | Y        | CRM         | IMPORT            | bx_crm_import_user_xccoe@gisele.alterego-russia.ru | 2024-02-16 12:14:15 | 2014-12-05 18:15:13 | s1    |                       |                |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2015-04-27 23:37:10 |               |                |                0 | 2016-11-11 00:26:05  |                  |             |                    |         | 69163920f9b5d81d1cf7a81276dcda6d |               |
|    5 | 2018-09-05 18:32:53 | divoy@yandex.ru                                    | $If9D*6d18369e69a18e136791eb52cd41d18fc1 | JW1jxSGX7a910be61140303c247c1ac72c219106 | N        | Дмитрий     | Войтович          | divoy@yandex.ru                                    | 2015-05-22 21:06:55 | 2014-12-08 12:43:17 | s1    |                       |                |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2018-09-05 18:32:53 |               |                |                0 |                      |                  |             |                    |         | f8bb46ab196ae22f5fcb645cce41c92b |               |
|    6 | 2022-10-20 09:38:53 | depechemodefan@alterego.biz.ua                     | /Pf7]H0s4c5017bf0966ea2598b6b968684a25f3 | rMc7nNcq64e5f734d27a7b8154acd88b5a6e5c10 | N        | Иван        | Машканцев         | depechemodefan@alterego.biz.ua                     | 2022-03-07 18:05:19 | 2014-12-18 19:12:16 | 13    |                       |                |                | F                 |                      |              nan |      3.80503e+11 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          | 1991-07-05          |                    | 2022-10-20 09:38:53 | Александрович |                |                0 | 0000-00-00 00:00:00  |                  |             |                    |         | 0aa789226006ace09720993186a9552e |               |
|    7 | 2023-08-28 16:37:38 | 1cadmin@berezkaonline.ru                           | d4/H0T!v2e1069f0ffdf177b5a42927c2d463bf6 | hxllq01V14a90474990506e8efb522711c614f9f | Y        |             |                   | 1cadmin@berezkaonline.ru                           | 2024-04-27 22:35:01 | 2014-12-31 13:26:32 | s1    |                       |                |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2023-08-28 16:37:38 |               |                |                0 | 2016-11-11 00:24:30  |                  |             |                    |         | eef180a257bf9263351521f128ed31ad |               |
|    8 | 2019-02-18 17:22:43 | den@alterego.biz.ua                                | j5S#tX-64d82bc6a71354c50af887e1ae82d94d9 | fegNRYzG9105caa0651cf2630753ba686c069e57 | Y        | Denys       | Vas               | den@alterego.biz.ua                                | 2016-06-27 17:33:55 | 2015-01-14 18:10:03 | s1    |                       |                |                |                   |                      |              nan |      7.925e+10   |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2018-09-05 18:27:57 |               |                |                0 | 2016-06-27 17:36:52  |                  |             |                    |         | d882bdc1cfcbf3eaa7653075c2d42fc7 |               |
|   20 | 2022-09-01 15:00:35 | zavgorodny@alterego.biz.ua                         | |i2N%3Hyf42ce4d0f6dc4ddac0eecbca7da102e6 | SekMLULhd9c84ba9501ab003f9bd77f475334ecb | N        | Денис       | Завгородний       | zavgorodny@alterego.biz.ua                         | 2019-06-17 23:51:25 | 2015-01-31 19:57:33 | s9    |                       |                |                | M                 |                      |              nan |      7.12321e+10 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          | 2003-05-05          |                    | 2022-09-01 15:00:35 |               |                |                1 | 0000-00-00 00:00:00  |                  |             |                    |         | da0bde97b6a9cb5bd2fa91710c9d97fe |               |
|   67 | 2018-10-17 18:01:15 | denis.zavgorodny@mail.com                          | Y1JUVQfd2a1342c8bb938a8ba11dd2fe5b6da81a | uSc264Vy57f217af29842256d079399037b769a2 | Y        | Иванов      | Петр              | denis.zavgorodny@mail.com                          | 2015-02-09 14:43:51 | 2015-02-09 14:43:51 | s2    |                       |                |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |                | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2015-02-09 14:43:51 |               |                |                0 |                      |                  |             |                    |         |                                  |               |
|   77 | 2022-07-22 15:53:33 | e.stativa@alterego.biz.ua                          | Gy0{R8/t39f4227781b7d4182b74ecf650e143b0 | a5M5I5gO224d0a02f252e0ddadc1f56b4888f4ec | N        | Елена       | Редина            | e.stativa@alterego.biz.ua                          | 2021-11-14 00:09:04 | 2015-02-16 14:56:26 | s1    |                       |                |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2022-07-22 15:53:33 |               |                |                0 | 0000-00-00 00:00:00  |                  |             |                    |         | 78094df1f485f45e603bb8f8a149143e |               |
|   78 | 2023-03-15 09:36:10 | half-admin@berezka.alterego-russia.ru              | 0Dd!3Hj,7f643b9d2e05e0df5c9e5462b6562969 | xSqSW6eOdd66436afb2f2837bd2d44ca61a9d230 | N        |             | Полуадминистратор | half-admin@berezka.alterego-russia.ru              | 2015-05-27 01:43:51 | 2015-02-16 20:42:56 | s1    |                       |                |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2023-03-15 09:36:10 |               |                |                0 |                      |                  |             |                    |         | 98fa75ebbf054f933d41eb727b217af3 |               |
|   85 | 2018-09-05 18:29:42 | carinatus@alterego.biz.ua                          | m9lztKWK7508f2ddfda25ebe2e820f0061a63a35 | 2OSyytVU1300591a6070881ba5bb9d63a8081f3c | Y        | Зинаида     | Седых             | carinatus@alterego.biz.ua                          | 2017-05-25 15:44:22 | 2015-02-25 16:06:25 | s1    |                       |                |                |                   |                      |              nan |      7.00011e+10 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2018-09-05 18:29:42 |               |                |                4 | 2016-11-09 17:25:16  |                  |             |                    |         | d7135ca6a83230ef839505b53c620299 |               |
|  178 | 2022-07-22 15:29:32 | denis.zavgorodny                                   | 1Cf!\6cTc22143903130e46b3ae1c659674c8129 | W4jBvU4lf11e8321464753dacb29f1e9dfe104fc | N        | Zavgorodny1 | Denis             | denis.zavgorodny@gmail.com                         | 2022-02-18 17:40:56 | 2015-02-25 22:07:50 | s2    |                       |                |                |                   |                      |              nan |      7.00089e+10 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2022-07-22 15:29:32 |               |                |                0 | 2016-05-04 18:09:20  |                  |             |                    |         | 96e116464895d1d7e836578a35033bd5 |               |
|  418 | 2017-11-23 00:15:12 | copywriter@berezka.alterego-russia.ru              | O9-s:P6x4c859af12a7fc2f94eee787877a069b9 | LbIFYu7Se4d56ca7238caceeb5cbbfeca30eef5c | Y        |             | Копирайтер        | copywriter@berezka.alterego-russia.ru              | 2016-09-30 11:47:46 | 2015-03-13 14:07:45 | s1    |                       |                |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2015-03-13 14:11:34 |               |                |                0 | 2016-09-30 11:48:28  |                  |             |                    |         | 86d1d27fcd0dfe007f67056771ed8f0d |               |
|  419 | 2017-12-12 17:47:33 | designer@berezka.alterego-russia.ru                | 3Fj^0l[A8ab0c5f059a5a2df7840d37f4cd0a041 | qfvaunaC65b8abfb079ff309e5f22d865816a76d | N        | Тест        | Дизайнер          | designer@berezka.alterego-russia.ru                | 2015-11-09 17:03:40 | 2015-03-13 14:09:19 | s1    |                       |                |                |                   |                      |              nan |      7.91517e+10 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2015-11-10 14:49:04 |               |                |                0 | 2015-11-09 18:06:36  |                  |             |                    |         | 49e4c5e94021d5609a559692017bdeb0 |               |
|  420 | 2022-10-20 09:44:01 | marketer@berezka.alterego-russia.ru                | f\Z9jW.13425d3a9ef5c638faa576a518c39f560 | YaXfzHX4e1ed99f7c42401e009e3aafda0eeb4fd | N        |             |                   | marketer@berezka.alterego-russia.ru                | 2015-05-22 16:37:40 | 2015-03-13 14:09:51 | s1    |                       |                |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2022-10-20 09:44:01 |               |                |                0 |                      |                  |             |                    |         | 48c0eda6f3f01842bc15d39e15b11cb8 |               |
|  435 | 2023-09-17 18:24:26 | bytkevi4@gmail.com                                 | 9,rJ8Cm3160b8a8ba9031f92067975e75953278  | V8Br8DyJ01eb7f3229235c0ca99f47f476db0fe6 | N        | Антон       | Буткевич          | bytkevi4@gmail.com                                 | 2018-02-26 18:32:03 | 2015-03-23 19:24:25 | s5    |                       |                |                |                   |                      |              nan |      7.92657e+10 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2020-11-16 14:45:12 |               |                |            18252 | 0000-00-00 00:00:00  |                  |             |                    |         | 9698b8b57fad22918cc5737ba936b998 |               |
|  437 | 2019-02-18 17:24:23 | popuk@list.ru                                      | 9p%EAw>0a3dfb08c5b9bcf7dc8efc5fa6393a7ee | lKI6L51s923763bcdc12080ac2c15661b8529275 | Y        |             |                   | popuk@list.ru                                      | 2020-12-21 23:52:15 | 2015-03-24 15:52:13 | s8    |                       |                |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          |                     |                    | 2018-09-04 21:34:38 |               |                |                0 | 2016-11-09 23:38:50  |                  |             |                    |         | 1e1b4eaad40b7d937a57a9d033594bbf |               |
|  446 | 2023-08-29 10:54:53 | k.melnychuk@alterego-russia.ru                     | W}l24Zu^a23f945ba8c0b1023c7dac8d0a7ca50a | Owh0tRNe0248889c81185e2575379a26d6472931 | Y        | Кирилл1     | Мельничук         | k.melnychuk@alterego-russia.ru                     | 2019-10-04 17:40:06 | 2015-03-26 20:01:13 | s8    |                       |                |                |                   |                      |              nan |      7.92501e+10 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          | 1988-09-05          |                    | 2018-09-04 21:41:48 |               |                |                0 | 2016-11-11 00:27:14  |                  |             |                    |         | 0c507f2fe79df5e6801b90b52c4a24c6 |               |
|  448 | 2023-11-23 00:20:53 | igor@kazakov.com                                   | 8rZ)%Dq0897666940830ff704817c41f66c70980 | XKMWAVYoa49067267599ec22201679662f76690c | Y        | Игорь       | Казаков           | igor@kazakov.com                                   | 2024-02-14 11:24:28 | 2015-03-26 21:29:28 | s5    |                       |                |                | M                 |                      |              nan |      7.90396e+10 |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 | NaT            | NaT         |              |           nan |           nan |          | 1980-10-17          |                    | 2022-02-10 12:35:05 |               |                |                0 | 0000-00-00 00:00:00  |                  |             |                    |         | 9a3120c035a9a440288222a55713fb93 |               |
```

> - File path: users_b_uts_fuser.csv
> - Total rows: 136159

### Schema
```
root
 |-- VALUE_ID: integer (nullable = true)
 |-- UF_NAME: string (nullable = true)
 |-- UF_EMAIL: string (nullable = true)
 |-- UF_PHONE: string (nullable = true)
 |-- UF_USER_ID: integer (nullable = true)
 |-- UF_THIRD_STEP_TIME: integer (nullable = true)
 |-- UF_DATE: timestamp (nullable = true)
 |-- UF_DATE_UPDATE: timestamp (nullable = true)
 |-- UF_SITE_ID: string (nullable = true)

```

### Data sample
```
|   VALUE_ID | UF_NAME   | UF_EMAIL                    |     UF_PHONE |   UF_USER_ID |   UF_THIRD_STEP_TIME | UF_DATE             | UF_DATE_UPDATE      | UF_SITE_ID   |
|-----------:|:----------|:----------------------------|-------------:|-------------:|---------------------:|:--------------------|:--------------------|:-------------|
|          1 | Светлана  | svetik8819@mail.ru          | +79651362957 |        82067 |                   60 | 2016-10-26 14:00:44 | 2016-10-26 14:00:45 | s5           |
|          2 | Валентина | valya.mudzhikova.84@mail.ru | +89615470638 |        84871 |                  330 | 2016-11-22 11:11:30 | 2016-11-22 11:12:30 | s6           |
|          3 | Виктория  | viktorialicate@mail.ru      | +79167414203 |        55045 |                  180 | 2019-01-31 00:11:25 | 2019-01-31 00:12:59 | s2           |
|          4 | Ксения    | Ksenia94@yandex.ru          |  89037373780 |          nan |                  690 | 2016-06-15 13:34:41 | 2016-06-15 13:37:11 | s5           |
|          5 | Елена     | bura-09@mail.ru             |  79166836241 |          nan |                   60 | 2016-09-27 10:58:13 | 2016-09-27 10:58:13 | s2           |
|          6 | Наталья   | natal-kulik@yandex.ru       | +79301649366 |        50005 |                 1050 | 2016-09-02 23:59:28 | 2016-09-03 00:02:13 | s5           |
|          7 | Юлия      | julia0052@yandex.ru         | +79039617465 |        50677 |                38460 | 2016-09-08 14:15:40 | 2016-09-08 15:47:28 | s2           |
|          8 | марина    | alekseeva_mv@solidar.ru     | +79104556515 |        60487 |                 1290 | 2016-09-29 10:59:15 | 2016-09-29 11:02:33 | s5           |
|          9 | впачу     | dw@ww.aa                    |  +5522002233 |        45751 |                   30 | 2017-08-03 15:20:16 | 2017-08-03 15:20:16 | s9           |
|         10 | ВЛАДИМИР  | dastin1972@mail.ru          | +79661863212 |       366427 |                  480 | 2019-10-26 12:38:02 | 2019-10-26 12:39:46 | s5           |
|         11 | Дмитрий   | salo46@yandex.ru            | +79508724405 |          nan |                  630 | 2017-06-07 22:17:19 | 2017-06-07 22:23:19 | s8           |
|         14 | Елена     | sambalina@mail.ru           |  89164445788 |          nan |                  180 | 2016-06-07 21:53:59 | 2016-06-07 21:54:35 | s2           |
|         16 | Анастасия | a.lardem@gmail.com          | +79150760656 |          nan |                  240 | 2016-07-22 12:56:02 | 2016-07-22 12:57:03 | s2           |
|         17 | Татьяна   | tatsweetfed@gmail.com       | +79107291109 |          nan |                  540 | 2017-03-11 14:31:46 | 2017-03-11 14:34:04 | s6           |
|         18 | Елена     | e.v.dubrovina@yandex.ru     |  89036830373 |          nan |                 1110 | 2016-06-22 09:38:52 | 2016-06-22 09:42:56 | s2           |
|         19 | Анна      | valova.tofa@mail.ru         | +79175691550 |          nan |                  480 | 2016-07-30 20:03:42 | 2016-07-30 20:04:14 | s5           |
|         20 | Елена     | plena@fromru.com            | +79173410622 |        79523 |                 1380 | 2016-10-17 08:47:45 | 2016-10-17 08:51:49 | s5           |
|         21 | Давид     | daveti500@pm.me             | +79853009191 |       785865 |                  120 | 2020-12-15 21:51:54 | 2020-12-15 21:52:56 | s5           |
|         28 | Елена     | konoplevaeg@mail.ru         | +79145228242 |          nan |                  150 | 2016-07-28 07:50:10 | 2016-07-28 07:50:41 | s2           |
|         35 | Фатима    | fatima-bersanova@mail.ru    | +79215795959 |        72515 |                  750 | 2016-09-16 21:25:14 | 2016-09-16 21:27:26 | s5           |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = false)
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- addresses: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- raw: string (nullable = false)
 |    |    |-- address: string (nullable = true)
 |    |    |-- location: struct (nullable = true)
 |    |    |    |-- region_type: string (nullable = true)
 |    |    |    |-- region_value: string (nullable = true)
 |    |    |    |-- settlement_region_type: string (nullable = true)
 |    |    |    |-- settlement_region_value: string (nullable = true)
 |    |    |    |-- settlement_type: string (nullable = true)
 |    |    |    |-- settlement_value: string (nullable = true)
 |    |    |    |-- street_type: string (nullable = true)
 |    |    |    |-- street_value: string (nullable = true)
 |    |    |    |-- house: string (nullable = true)
 |    |    |    |-- flat: string (nullable = true)
 |    |    |    |-- floor: string (nullable = true)
 |    |    |    |-- office: string (nullable = true)
 |    |    |    |-- corpus: string (nullable = true)
 |    |    |    |-- coordinates: array (nullable = true)
 |    |    |    |    |-- element: double (containsNull = true)
 |    |    |    |-- coord_detalization_lvl: integer (nullable = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- actuality: string (nullable = true)

```



### Data sample
```
| names                           |   sex | birth_date   | phones          | emails                                  | address   | addresses   | socials   | accounts                                                                                                                                                                        | actuality   |
|:--------------------------------|------:|:-------------|:----------------|:----------------------------------------|:----------|:------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Росс Александра']             |     0 |              | ['79151900880'] | ['0030104@gmail.com']                   |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='+79151900880', password_hash='qNr6kDk8a1b6d41688c7f14d85d7917db84bff5c')]             | 29.10.2023  |
| ['Коржов Василий']              |     1 |              | ['79166889664'] | ['0597@mail.ru']                        |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='0597@mail.ru', password_hash='}0Ft9!Lq62611b6106ac7778fe9c3f73d70390e8')]             | 24.04.2023  |
| ['Сливина Юлия Борисовна']      |     1 | 25.12.1985   | ['79660708000'] | ['0708000s@mail.ru']                    |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='0708000s@mail.ru', password_hash='JcmR9sR721cd4e5f3f596656d12049c830814a88')]         | 19.07.2022  |
| ['Гордиевская Алла']            |   nan |              | ['79036647412'] | ['100hit@ya.ru']                        |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='+79036647412', password_hash='9|Fx5At_fd5306b3bab8fabe786b3e2142c76300')]             | 15.11.2019  |
| ['Жукова Лариса Викторовна']    |     0 |              |                 | ['1305.zhoukova@gmail.com']             |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='1305.zhoukova@gmail.com', password_hash='elwglNjn02a7e41a5276a0fd0b5a2b01f1759b1f')]  | 14.08.2021  |
| ['Наталья']                     |   nan |              | ['79153341724'] | ['1371255@rambler.ru']                  |           |             |           |                                                                                                                                                                                 |             |
| ['Айдинян Руслан']              |     1 |              | ['79991111109'] | ['1789964@mail.ru']                     |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='1789964@mail.ru', password_hash='=2Dvh3]B16d6481dd3129d46a691b74cebe29296')]          | 19.01.2024  |
| ['Салимон Михаил']              |     1 |              | ['79881888109'] | ['19-30@mail.ru']                       |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='19-30@mail.ru', password_hash='*2uQ1?bDbf0e4640cf4b2cc0e5b4d7051773d4c4')]            | 07.10.2021  |
| ['Ольга']                       |   nan |              |                 | ['1961235@gmail.com']                   |           |             |           |                                                                                                                                                                                 |             |
| ['Воробьев Андрей Николаевич']  |     1 | 23.10.1969   | ['79069867070'] | ['196969@inboxx.ru', '196969@inbox.ru'] |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='196969@inboxx.ru', password_hash='s[0S2?Yu3b7e3e54d99311ddf3b14fbe919e0282')]         | 21.07.2019  |
| ['Шархун Андрей']               |     1 |              | ['79031412501'] | ['1975shark@rambler.ru']                |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='1975shark@rambler.ru', password_hash='{3Fk!7Tv8d71161f12a1042989047499787072dc')]     | 04.12.2023  |
| ['Фиалковский Роман']           |   nan |              | ['79112571683'] | ['19frv71@mail.ru']                     |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='19frv71@mail.ru', password_hash='VHhjJKzg124e6ff674a62f99be1670fb8846d40a')]          | 16.12.2020  |
| ['Барабанщиков Вадим']          |     0 |              | ['79067456160'] | ['19vadim86@mail.ru']                   |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='19vadim86@mail.ru', password_hash='Td_89D^zf3c817826c2906d0e1f77da185443555')]        | 05.07.2020  |
| ['Королева Диана']              |     0 |              | ['79166283194'] | ['1diana101@mail.ru']                   |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='+79166283194', password_hash='9kR,8:mPaf25d980f532b891e50b3088bda81c98')]             | 21.11.2019  |
| ['Шведун Ксения Александровна'] |     0 | 03.01.1993   | ['79144655050'] | ['1famous.mouse1@gmail.com']            |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='1famous.mouse1@gmail.com', password_hash='0WGpkh54cf6d28d0d92fc999e2b76b72b09c8b7d')] | 18.05.2019  |
| ['Сулейманов Даниял']           |     1 |              | ['79264727221'] | ['1sdm@mail.ru']                        |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='1sdm@mail.ru', password_hash='Xz_71)Yj9a7df4eb1ca94f16d26e83caf72167b0')]             | 08.08.2022  |
| ['Масюк Наталия']               |     0 |              | ['79803000870'] | ['2003masyk@gmail.com']                 |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='2003masyk', password_hash='2NZhwqHD67f0b55abff7fa0177165345669aa40f')]                | 08.11.2022  |
| ['Андреев Дмитрий']             |     0 |              | ['79687312042'] | ['2130242@mail.ru']                     |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='2130242@mail.ru', password_hash='iHLKS4ir7e88c39f87901ad0a8588570ba3bc156')]          | 10.02.2024  |
| ['Данил']                       |   nan |              |                 | ['220975@bk.ru']                        |           |             |           |                                                                                                                                                                                 |             |
| ['Фомин Евгений Павлович']      |     1 |              | ['79127797773'] | ['23-12-65@mail.ru']                    |           |             |           | [Row(title='Bosco.ru – группа компаний Bosco di Ciliegi', link='https://bosco.ru', login='23-12-65@mail.ru', password_hash='ywJgPS2Qc8d1c9ab86d2831d1c44825e94eac599')]         | 08.11.2022  |
```