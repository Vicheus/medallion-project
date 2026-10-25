# Parsetron results

## About row data

> - Code name: index_0003
> - File path: sportmaster-part1.txt
> - Total rows: 99908778

### Schema
```
root
 |-- CODE: string (nullable = true)
 |-- CLIENT_REG_CODE: string (nullable = true)
 |-- TYPE: string (nullable = true)
 |-- STATE: string (nullable = true)
 |-- BARCODE: string (nullable = true)
 |-- DAT: string (nullable = true)
 |-- ANKETA_TYPE: string (nullable = true)
 |-- PLACE_TYPE: string (nullable = true)
 |-- PLACE_SHOP: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- FIRST_NAME: string (nullable = true)
 |-- MIDDLE_NAME: string (nullable = true)
 |-- SEX: string (nullable = true)
 |-- BIRTHDAY: string (nullable = true)
 |-- MOBILE_PHONE: string (nullable = true)
 |-- HOME_PHONE: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- NICKNAME: string (nullable = true)
 |-- ADDR_INDEX: string (nullable = true)
 |-- ADDR_OBL: string (nullable = true)
 |-- ADDR_RON: string (nullable = true)
 |-- ADDR_CITY: string (nullable = true)
 |-- ADDR_STREET: string (nullable = true)
 |-- ADDR_HOUSE: string (nullable = true)
 |-- ADDR_KORP: string (nullable = true)
 |-- ADDR_STROEN: string (nullable = true)
 |-- ADDR_KV: string (nullable = true)
 |-- ADDR_OTHER: string (nullable = true)
 |-- SMPERS_ID: string (nullable = true)
 |-- STAFF_DAT_IN: timestamp (nullable = true)
 |-- STAFF_DAT_OUT: timestamp (nullable = true)
 |-- WANT_RECEIVE_INFO: integer (nullable = true)
 |-- WO_SMS: integer (nullable = true)
 |-- WO_EMAIL: integer (nullable = true)
 |-- DAT_RECOGNIZE: timestamp (nullable = true)
 |-- DAT_PROCESS: timestamp (nullable = true)
 |-- INSERTED: timestamp (nullable = true)
 |-- UPDATED: timestamp (nullable = true)
 |-- REMARKS: string (nullable = true)
 |-- LANG_CODE: string (nullable = true)
 |-- CASHIER: string (nullable = true)
 |-- HAS_SIGN: integer (nullable = true)
 |-- HAVE_KIDS: integer (nullable = true)
 |-- HAVE_SPOUSE: string (nullable = true)
 |-- SPOUSE_BIRTHDAY: string (nullable = true)
 |-- METRO_STATION: string (nullable = true)
 |-- ADDRESS_NAME: string (nullable = true)
 |-- TRANSACTION_CODE: long (nullable = true)
 |-- ID_CITY: long (nullable = true)
 |-- ID_STREET: string (nullable = true)
 |-- ID_HOUSE: string (nullable = true)
 |-- ID_METRO: string (nullable = true)
 |-- FAST_DELIVERY_CODE: string (nullable = true)
 |-- PERS_AGREEMENT: integer (nullable = true)
 |-- AGGR_PROCESSED: integer (nullable = true)
 |-- COMM_AGREEMENT: string (nullable = true)

```

### Data sample
```
|               CODE |    CLIENT_REG_CODE |   TYPE |   STATE |       BARCODE | DAT                     |   ANKETA_TYPE |   PLACE_TYPE |   PLACE_SHOP | LAST_NAME   | FIRST_NAME   | MIDDLE_NAME   |   SEX | BIRTHDAY                | MOBILE_PHONE   | HOME_PHONE   | EMAIL                     | NICKNAME   |   ADDR_INDEX | ADDR_OBL   | ADDR_RON   | ADDR_CITY      | ADDR_STREET   |   ADDR_HOUSE | ADDR_KORP   | ADDR_STROEN   |   ADDR_KV | ADDR_OTHER   | SMPERS_ID   | STAFF_DAT_IN   | STAFF_DAT_OUT   |   WANT_RECEIVE_INFO |   WO_SMS |   WO_EMAIL | DAT_RECOGNIZE   | DAT_PROCESS   | INSERTED            | UPDATED             | REMARKS   | LANG_CODE   | CASHIER   |   HAS_SIGN |   HAVE_KIDS | HAVE_SPOUSE   | SPOUSE_BIRTHDAY   | METRO_STATION   | ADDRESS_NAME   |   TRANSACTION_CODE |   ID_CITY | ID_STREET   | ID_HOUSE   | ID_METRO   | FAST_DELIVERY_CODE   |   PERS_AGREEMENT |   AGGR_PROCESSED | COMM_AGREEMENT   |
|-------------------:|-------------------:|-------:|--------:|--------------:|:------------------------|--------------:|-------------:|-------------:|:------------|:-------------|:--------------|------:|:------------------------|:---------------|:-------------|:--------------------------|:-----------|-------------:|:-----------|:-----------|:---------------|:--------------|-------------:|:------------|:--------------|----------:|:-------------|:------------|:---------------|:----------------|--------------------:|---------:|-----------:|:----------------|:--------------|:--------------------|:--------------------|:----------|:------------|:----------|-----------:|------------:|:--------------|:------------------|:----------------|:---------------|-------------------:|----------:|:------------|:-----------|:-----------|:---------------------|-----------------:|-----------------:|:-----------------|
| 992000000090559583 | 992000000049534146 |      0 |       1 | 2012017331266 | 2012-09-15 00:00:00.000 |            11 |            0 |         5253 | Кошуняева   | Юлия         |               |     0 |                         | 79021913388    |              |                           |            |            0 |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559584 | 992000000062783670 |      0 |       1 | 2012079616738 | 2013-06-20 00:00:00.000 |            11 |            0 |          975 |             | Ильнара      |               |     0 | 1989-03-04 00:00:00.000 | 79503180713    |              |                           |            |            0 |            |            | Казань         | Салимжанова   |           17 |             |               |        13 |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559585 | 992000000035071128 |      0 |       1 | 2012043978794 | 2013-06-15 00:00:00.000 |            11 |            0 |         5199 |             | Владимир     |               |     1 | 1990-08-17 00:00:00.000 | 79222525132    |              | semenov_vladimir@inbox.ru |            |            0 |            |            | Краснотурьинск |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559586 | 992000000045432740 |      0 |       1 | 2012077291272 | 2013-07-21 00:00:00.000 |            11 |            0 |         5032 |             | Анна         |               |     0 | 1984-04-29 00:00:00.000 | 79208361179    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559587 | 992000000035994080 |      0 |       1 | 2012077291418 | 2013-07-21 00:00:00.000 |            11 |            0 |         5032 |             | Анна         |               |     0 | 1990-08-01 00:00:00.000 | 79803011798    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559588 | 992000000039695240 |      0 |       1 | 2012077329067 | 2013-07-20 00:00:00.000 |            11 |            0 |          212 |             | Юлия         |               |     0 | 1989-10-18 00:00:00.000 | 79038104886    |              |                           |            |            0 |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559589 | 992000000036899256 |      0 |       1 | 2012064310863 | 2013-07-20 00:00:00.000 |            11 |            0 |          835 |             | Наталья      |               |     0 | 1969-10-18 00:00:00.000 | 79059641346    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559590 | 992000000057702739 |      0 |       1 | 2012068263974 | 2013-07-20 00:00:00.000 |            11 |            0 |         5609 |             |              |               |       |                         |                |              |                           |            |            0 |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559591 | 992000000052842705 |      0 |       1 | 2012034040646 | 2013-07-20 00:00:00.000 |            11 |            0 |         5517 |             | Татьяна      |               |     0 | 1969-09-29 00:00:00.000 | 79825991885    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559592 | 992000000055658650 |      0 |       1 | 2014000486908 | 2013-07-20 00:00:00.000 |             4 |            0 |          743 |             | ***          |               |     1 | 1988-09-21 00:00:00.000 | ***            |              | ***                       |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |        nan |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559593 | 992000000042771050 |      0 |       1 | 2012067065340 | 2013-07-21 00:00:00.000 |            11 |            0 |          938 |             | Ольга        |               |     0 | 1979-09-11 00:00:00.000 | 79222686336    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559594 | 992000000057830721 |      0 |       1 | 2012078733290 | 2013-07-21 00:00:00.000 |            11 |            0 |          805 |             | Александр    |               |     1 | 1957-06-24 00:00:00.000 | 79644792451    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559595 | 992000000050445300 |      0 |       1 | 2012048429857 | 2013-07-21 00:00:00.000 |            11 |            0 |         5429 |             | Екатерина    |               |     0 | 1979-08-04 00:00:00.000 | 79200224637    |              | katrin-hor@mail.ru        |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559596 | 992000000035969422 |      0 |       1 | 2012004356883 | 2013-07-21 00:00:00.000 |            11 |            0 |          146 |             | Ульяна       |               |     0 | 1974-01-20 00:00:00.000 | 79055772919    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000090559597 | 992000000062582861 |      0 |       1 | 2012072318523 | 2013-07-21 00:00:00.000 |            11 |            0 |          813 |             | Александр    |               |     1 | 1984-04-29 00:00:00.000 | 79130278057    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |          1 |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000092819301 | 992000000046296607 |      0 |       1 | 2006079516464 | 2010-07-13 00:00:00.000 |            11 |            0 |          973 | Петрухина   | Светлана     |               |     0 | 1984-05-02 00:00:00.000 | 79209718070    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |        nan |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000092819302 | 992000000062077067 |      0 |       1 | 2006079400060 | 2010-07-10 00:00:00.000 |            11 |            0 |          266 | Паничев     | Андрей       |               |     1 | 1982-03-06 00:00:00.000 | 79043460855    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |        nan |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000092819303 | 992000000053979603 |      0 |       1 | 2006075200749 | 2010-07-10 00:00:00.000 |            11 |            0 |          266 | Зацепина    | Яна          | Юрьевна       |     0 | 1991-01-15 00:00:00.000 | 79518497016    |              | yanchik1501@gmail.com     |            |       344048 |            |            | Ростов-на-Дону | Равенства     |           12 |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |        nan |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000092819304 | 992000000065662942 |      0 |       1 | 2006079400930 | 2010-07-10 00:00:00.000 |            11 |            0 |          266 | Сахно       | Виталий      |               |     1 | 1979-03-20 00:00:00.000 | 79286059307    |              |                           |            |              |            |            | Ростов-на-Дону |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |        nan |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
| 992000000092819305 | 992000000046476340 |      0 |       1 | 2006085336377 | 2010-07-12 00:00:00.000 |            11 |            0 |          264 | Мухин       | Алексей      |               |     1 | 1975-03-10 00:00:00.000 | 79202541250    |              |                           |            |              |            |            |                |               |              |             |               |           |              |             | NaT            | NaT             |                   1 |        0 |          0 | NaT             | NaT           | 2013-10-28 00:06:37 | 2013-10-28 00:06:37 |           |             |           |        nan |         nan |               |                   |                 |                |                nan |       nan |             |            |            |                      |              nan |              nan |                  |
```


## About final data
> - Total rows: 55104541

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- children: boolean (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |-- actuality: string (nullable = true)

```



### Data sample
```
| names                                      | phones          | emails                            | address                                           | birth_date   |   sex | children   | accounts                                                | actuality   |
|:-------------------------------------------|:----------------|:----------------------------------|:--------------------------------------------------|:-------------|------:|:-----------|:--------------------------------------------------------|:------------|
| ['Суконникова Галина']                     |                 | ['kisca_galunka-@mail.ru']        |                                                   |              |     0 |            | [Row(title='sportmaster app', id='100000000171454306')] |             |
| ['Кирилл']                                 | ['79825463718'] | ['crimes@mail.ru']                |                                                   |              |     1 |            | [Row(title='sportmaster app', id='100000000308839273')] |             |
| ['Утлик']                                  |                 | ['lehaytlik@mail.ru']             |                                                   |              |     1 |            | [Row(title='sportmaster app', id='100000000313782739')] |             |
| ['Мария']                                  | ['79098010009'] | ['mashaant1997@mail.ru']          | ['Хабаровск']                                     |              |   nan |            | [Row(title='sportmaster app', id='100000000326789116')] |             |
| ['Мария']                                  | ['79681885277'] | ['marya94_94@mail.ru']            |                                                   |              |     0 |            | [Row(title='sportmaster app', id='100000000340945133')] |             |
| ['Константин']                             | ['79092492986'] | ['super.coss@yandex.ru']          |                                                   |              |     1 |            | [Row(title='sportmaster app', id='100000000372363626')] |             |
| ['Анастасия']                              | ['79675953417'] | ['irissska2017@icloud.com']       | ['Санкт Петербург Ударников проспект д. 191']     |              |     0 |            | [Row(title='sportmaster app', id='100000000383293789')] |             |
| ['Мария']                                  | ['79177605571'] | ['mariya.petrova.8383@gmail.com'] | ['Уфа Менделеева д. 1732']                        |              |     0 |            | [Row(title='sportmaster app', id='100000000445531566')] |             |
| ['Елизавета']                              | ['79056371020'] | ['lisya.05@mail.ru']              | ['Ярославль Строителей д. 19']                    |              |     0 |            | [Row(title='sportmaster app', id='100000000451815276')] |             |
| ['Канаева Валерия Валерьевна']             | ['79181198819'] |                                   |                                                   |              |     0 |            | [Row(title='sportmaster app', id='110000000000972561')] |             |
| ['Соколов Артур Александр Константинович'] | ['79522098529'] |                                   |                                                   |              |     1 |            | [Row(title='sportmaster app', id='110000003156648971')] |             |
| ['Андрей']                                 | ['79246867711'] |                                   | ['Петропавловск-Камчатский Олега Кошевого д. 10'] |              |     1 |            | [Row(title='sportmaster app', id='121000000001665484')] | 11.11.2013  |
| ['Александр']                              | ['79051901968'] |                                   | ['Саров Ленина д. 26']                            |              |     1 |            | [Row(title='sportmaster app', id='121000000006769304')] | 22.11.2013  |
| ['Михаил']                                 | ['79104314555'] |                                   |                                                   |              |     1 |            | [Row(title='sportmaster app', id='121000000010850074')] | 25.11.2013  |
| ['Надежда']                                | ['79656811993'] |                                   | ['Чебоксары Энтузиастов д. 9']                    |              |     0 |            | [Row(title='sportmaster app', id='121000000012935530')] | 13.11.2013  |
| ['Алексей']                                | ['79511142101'] |                                   | ['Магнитогорск Гагарина д. 41']                   |              |     1 |            | [Row(title='sportmaster app', id='121000000020869484')] | 13.11.2013  |
| ['Владислав']                              | ['79307816070'] |                                   | ['Рязань Либкнехта д. 3']                         |              |     1 |            | [Row(title='sportmaster app', id='121000000024508436')] | 20.11.2013  |
| ['Александр']                              | ['79046204419'] |                                   | ['Уссурийск Тургенева д. 7 кв. 513']              |              |     1 |            | [Row(title='sportmaster app', id='121000000040708891')] | 10.12.2013  |
| ['Константин']                             | ['79021907842'] | ['krenev-1974@mail.ru']           | ['Северодвинск Морской д. 8']                     |              |     1 |            | [Row(title='sportmaster app', id='121000000042613241')] | 28.11.2013  |
| ['Лариса']                                 | ['74959180484'] |                                   | ['Москва Цюрупы']                                 |              |     0 |            | [Row(title='sportmaster app', id='121000000044499880')] | 28.11.2013  |
```