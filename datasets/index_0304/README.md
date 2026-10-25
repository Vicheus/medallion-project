# Parsetron results

## About row data

> - Code name: index_0304
> - File path: modx_a_order.csv
> - Total rows: 932

### Schema
```
root
 |-- order_id: string (nullable = true)
 |-- order_created: string (nullable = true)
 |-- order_status: integer (nullable = true)
 |-- order_status_pay: string (nullable = true)
 |-- order_client: string (nullable = true)
 |-- order_manager: string (nullable = true)
 |-- order_delivery: string (nullable = true)
 |-- order_delivery_cost: string (nullable = true)
 |-- order_cost: string (nullable = true)
 |-- order_comment: string (nullable = true)
 |-- order_code: integer (nullable = true)
 |-- order_pay: string (nullable = true)
 |-- user_fullname: string (nullable = true)
 |-- user_email: string (nullable = true)
 |-- user_phone: string (nullable = true)
 |-- order_verify: string (nullable = true)

```

### Data sample
```
|   order_id | order_created       |   order_status |   order_status_pay |   order_client |   order_manager | order_delivery                                                                                                                                                             | order_delivery_cost   |   order_cost | order_comment                                                       |   order_code |   order_pay | user_fullname     | user_email           |            user_phone |   order_verify |
|-----------:|:--------------------|---------------:|-------------------:|---------------:|----------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|-------------:|:--------------------------------------------------------------------|-------------:|------------:|:------------------|:---------------------|----------------------:|---------------:|
|          1 | 2015-06-23 16:24:21 |              1 |                  0 |             47 |               0 | """1"""                                                                                                                                                                    |                       |            0 |                                                                     |            0 |           0 |                   |                      |                       |              1 |
|          2 | 2015-06-23 16:30:48 |              1 |                  0 |             47 |               0 | """1"""                                                                                                                                                                    |                       |        84000 |                                                                     |            0 |           2 |                   |                      |                       |              1 |
|          3 | 2015-06-23 16:36:10 |              1 |                  0 |             47 |               1 | "{""city"":""\u0425\u0430\u0440\u044c\u043a\u043e\u0432"",""street"":""\u0413\u0430\u043d\u043d\u044b"",""house"":""20\u0430"",""kv"":""1""}"                              |                       |        84000 | fdsfdsf                                                             |            0 |           0 |                   |                      |                       |              1 |
|          4 | 2015-06-23 17:08:08 |              1 |                  0 |             47 |               1 | "{""city"":""\u0425\u0430\u0440\u044c\u043a\u043e\u0432"",""street"":""\u0413\u0430\u043d\u043d\u044b"",""house"":""20\u0430"",""kv"":""1""}"                              |                       |        84000 | commet                                                              |            0 |           0 | sancho            | sanchovostok@mail.ru |          123123123123 |              1 |
|          5 | 2015-06-23 17:28:27 |              1 |                  0 |             48 |               1 | "{""city"":"""",""street"":"""",""house"":"""",""kv"":""""}"                                                                                                               |                       |       168000 | Voluptas quis error laudantium, facilis irure et et sed aliqua.     |            0 |           0 | Isadora Mcpherson | pyrylydavu@gmail.com |         2222222222222 |              1 |
|          7 | 2015-06-24 11:56:12 |              3 |                  0 |              0 |               1 | "{""city"":"""",""street"":"""",""house"":"""",""kv"":""""}"                                                                                                               |                       |        65000 |                                                                     |            0 |           0 | sanchovostok      |                      |          159357258456 |              1 |
|          8 | 2015-06-24 11:57:57 |              3 |                  0 |              0 |               1 | "{""city"":"""",""street"":"""",""house"":"""",""kv"":""""}"                                                                                                               |                       |       200000 |                                                                     |            0 |           0 | sanchovostok2     |                      |          123456789123 |              1 |
|          6 | 2015-06-24 11:38:13 |              6 |                  0 |              0 |               1 | "{""city"":"""",""street"":"""",""house"":"""",""kv"":""""}"                                                                                                               |                       |       100000 |                                                                     |            0 |           0 | sancho            |                      |    777888899996665547 |              1 |
|          9 | 2015-06-24 12:20:53 |              6 |                  0 |             47 |               0 |                                                                                                                                                                            |                       |        84000 |                                                                     |            0 |           0 | sancho            |                      |          123123123123 |              1 |
|         10 | 2015-06-24 12:21:30 |              6 |                  0 |             47 |               0 |                                                                                                                                                                            |                       |       318000 |                                                                     |            0 |           0 | sancho            |                      |          123123123123 |              1 |
|         11 | 2015-06-24 12:39:11 |              1 |                  0 |             47 |               0 | "{""city"":""\u0425\u0430\u0440\u044c\u043a\u043e\u0432"",""street"":""\u0413\u0430\u043d\u043d\u044b"",""house"":""20\u0430"",""kv"":""1""}"                              |                       |        65000 |                                                                     |            0 |           1 | sancho            | sanchovostok@mail.ru |          123123123123 |              1 |
|         12 | 2015-06-25 10:45:26 |              6 |                  0 |              0 |               0 |                                                                                                                                                                            |                       |        84000 |                                                                     |            0 |           0 | sancho1           |                      |          123456789123 |              1 |
|         13 | 2015-06-25 10:46:05 |              6 |                  0 |              0 |               0 |                                                                                                                                                                            |                       |       414000 |                                                                     |            0 |           0 | sancho2           |                      |          123123123123 |              1 |
|         14 | 2015-06-25 10:48:05 |              1 |                  0 |             49 |               0 | "{""city"":""Deserunt fugiat voluptate qui anim exercitation ut veniam"",""street"":""Duis sit do enim velit iste est"",""house"":""157"",""kv"":""10""}"                  |                       |       149000 | Perspiciatis, illo totam occaecat a ratione quis est in nulla vero. |            0 |           1 | Brenden Hall      | cizuz@gmail.com      | 987879879879879879878 |              1 |
|         15 | 2015-06-25 11:40:51 |              1 |                  0 |             49 |               0 | "{""city"":""Deserunt fugiat voluptate qui anim exercitation ut veniam"",""street"":""Duis sit do enim velit iste est"",""house"":""157"",""kv"":""10""}"                  |                       |       149000 |                                                                     |            0 |           1 | Brenden Hall      | cizuz@gmail.com      | 987879879879879879878 |              1 |
|         16 | 2015-06-25 11:46:10 |              6 |                  0 |             49 |               0 |                                                                                                                                                                            |                       |       186650 |                                                                     |            0 |           0 | Brenden Hall      |                      | 987879879879879879878 |              1 |
|         17 | 2015-06-25 11:47:01 |              6 |                  0 |             49 |               0 |                                                                                                                                                                            |                       |       596400 |                                                                     |            0 |           0 | Brenden Hall      |                      | 987879879879879879878 |              1 |
|         18 | 2015-06-25 18:02:10 |              3 |                  0 |              0 |               1 | "{""city"":"""",""street"":"""",""house"":"""",""kv"":""""}"                                                                                                               |                       |        58000 |                                                                     |            0 |           0 | test              |                      |      1541640684068460 |              1 |
|         19 | 2015-06-25 18:04:06 |              6 |                  0 |              0 |               0 |                                                                                                                                                                            |                       |       128650 |                                                                     |            0 |           0 | HEHETH            |                      |         1156556665464 |              1 |
|         20 | 2015-06-25 18:20:04 |              1 |                  0 |             51 |               0 | "{""city"":""43534534534534"",""street"":""543453453454"",""house"":""\u0443\u043a\u043d\u0443\u043a\u043d\u0443"",""kv"":""\u043d\u0443\u0443\u043d\u043a\u043d\u0443""}" |                       |      3450650 | 45345345345534534                                                   |            0 |           4 | укпукпук          | tarrest_9@mail.ru    |           04165464646 |              1 |
```


## About final data
> - Total rows: 510

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
 |-- actuality: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 79.80% |
| Phones | 94.12% |
| Address | 0.00% |
| Actuality | 100.00% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                | emails                          | phones          | address   | actuality   | raw_metadata                                                                                                                                               |
|:---------------------|:--------------------------------|:----------------|:----------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Диана']            | ['disk905@mail.ru']             | ['79787054168'] |           | 27.10.2022  | ['{"order_id": "904", "order_manager": "0", "order_cost": "8990", "order_code": "0", "order_pay": "1"}']                                                   |
| ['Наталья']          | ['marchenco.2016@mail.ru']      | ['79788223929'] |           | 30.12.2020  | ['{"order_id": "724", "order_manager": "1", "order_cost": "350", "order_code": "0", "order_pay": "2"}']                                                    |
| ['Никита Друшляк']   | ['nikitasss20022002@mail.ru']   | ['79781228531'] |           | 22.07.2016  | ['{"order_id": "194", "order_manager": "1", "order_cost": "1150", "order_code": "0", "order_pay": "2"}']                                                   |
| ['Moeller']          | ['artjokerqa@gmail.com']        |                 |           | 08.07.2015  | ['{"order_id": "52", "order_manager": "0", "order_cost": "172380", "order_comment": "tgtgtgtgb btbtbt tbbb", "order_code": "0", "order_pay": "1"}']        |
| ['Максим']           |                                 | ['79787689738'] |           | 03.07.2018  | ['{"order_id": "359", "order_manager": "1", "order_cost": "60", "order_code": "0", "order_pay": "1"}']                                                     |
| ['Александр']        | ['drumers@inbox.ru']            | ['79141574510'] |           | 19.12.2018  | ['{"order_id": "419", "order_manager": "0", "order_cost": "10510", "order_comment": "Прошу Вас перезвонить мне...", "order_code": "0", "order_pay": "5"}'] |
| ['Ангелина']         |                                 | ['79029021176'] |           | 20.09.2022  | ['{"order_id": "895", "order_manager": "0", "order_cost": "14990", "order_code": "0", "order_pay": "0"}']                                                  |
| ['Кристина Левчук']  | ['kristinalevchuk17@gmail.com'] | ['79782616012'] |           | 27.05.2018  | ['{"order_id": "348", "order_manager": "1", "order_cost": "1760", "order_code": "0", "order_pay": "1"}']                                                   |
| ['Татьяна']          | ['zz.75@mail.ru']               | ['79780701925'] |           | 23.09.2019  | ['{"order_id": "506", "order_manager": "0", "order_cost": "1660", "order_code": "0", "order_pay": "1"}']                                                   |
| ['Алексей']          | ['lafax82@gmail.com']           | ['79889435520'] |           | 02.09.2020  | ['{"order_id": "653", "order_manager": "1", "order_cost": "74990", "order_code": "0", "order_pay": "1"}']                                                  |
| ['Дмитрий Мейсигов'] | ['meis2000@mail.ru']            | ['79105073780'] |           | 04.06.2020  | ['{"order_id": "618", "order_manager": "1", "order_cost": "8990", "order_code": "0", "order_pay": "5"}']                                                   |
| ['Алина']            | ['alianavahonina@yandex.ru']    | ['79780353914'] |           | 18.09.2020  | ['{"order_id": "663", "order_manager": "1", "order_cost": "230", "order_code": "0", "order_pay": "1"}']                                                    |
| ['Бронислав']        | ['armor.sbv@gmail.com']         | ['79787425936'] |           | 06.02.2016  | ['{"order_id": "186", "order_manager": "1", "order_cost": "35800", "order_comment": "1й подъезд, домофон", "order_code": "0", "order_pay": "2"}']          |
| ['Андрей']           | ['djanky1986@gmail.com']        | ['79789007797'] |           | 03.10.2019  | ['{"order_id": "515", "order_manager": "1", "order_cost": "2100", "order_code": "0", "order_pay": "2"}']                                                   |
| ['Евгений']          | ['aeterna84@yandex.ru']         | ['79788823782'] |           | 31.12.2020  | ['{"order_id": "725", "order_manager": "1", "order_cost": "6680", "order_code": "0", "order_pay": "1"}']                                                   |
| ['Николай']          |                                 | ['79788922394'] |           | 15.11.2016  | ['{"order_id": "203", "order_manager": "0", "order_cost": "8400", "order_code": "0", "order_pay": "0"}']                                                   |
| ['Валентин']         | ['bajiek1994@mail.ru']          | ['79186201151'] |           | 14.11.2020  | ['{"order_id": "705", "order_manager": "0", "order_cost": "9370", "order_code": "0", "order_pay": "1"}']                                                   |
| ['Мамедова Амина']   | ['ammyma1272@gmail.com']        | ['79782702817'] |           | 26.12.2018  | ['{"order_id": "424", "order_manager": "0", "order_cost": "1320", "order_code": "0", "order_pay": "1"}']                                                   |
| ['Семён']            | ['posohov.semen@mail.ru']       | ['79788583754'] |           | 10.08.2020  | ['{"order_id": "645", "order_manager": "1", "order_cost": "22000", "order_comment": "Проверка сайта.", "order_code": "0", "order_pay": "3"}']              |
| ['Алексей']          |                                 | ['79788320984'] |           | 13.08.2020  | ['{"order_id": "647", "order_manager": "1", "order_cost": "6450", "order_code": "0", "order_pay": "1"}']                                                   |
```