# Parsetron results

## About row data

> - Code name: index_0086
> - File path: Westwing.ru/Email_Westwing.ru_11.2019_1,5M.txt
> - Total rows: 1573099

### Schema
```
root
 |-- id_customer: string (nullable = true)
 |-- email: string (nullable = true)
 |-- facebook_id: long (nullable = true)
 |-- facebook_id_new: long (nullable = true)
 |-- google_plus_id: decimal(21,0) (nullable = true)
 |-- Имя: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Пол: string (nullable = true)
 |-- hash: string (nullable = true)
 |-- confirmation_key: string (nullable = true)
 |-- payment_reference_key: string (nullable = true)
 |-- created_at: string (nullable = true)
 |-- updated_at: string (nullable = true)

```

### Data sample
```
|   id_customer | email                                 |   facebook_id |   facebook_id_new | google_plus_id   | Имя     | Фамилия    | Пол    | hash                                                         | confirmation_key                 | payment_reference_key   | created_at          | updated_at          |
|--------------:|:--------------------------------------|--------------:|------------------:|:-----------------|:--------|:-----------|:-------|:-------------------------------------------------------------|:---------------------------------|:------------------------|:--------------------|:--------------------|
|             1 | martin.l.bayer@gmail.com              | nan           |               nan |                  | test    | test       | female | 802f2f7be032ff375963ff2ec9b858a4                             | 05d6ab54f4c1f5b781f4230c871a5c63 |                         | 2011-11-30 18:57:10 | 2016-03-09 18:18:42 |
|             3 | dinara.sharlapaeva@gmail.com          |   1.01545e+16 |               nan |                  | Динара  | Шарлапаева | female | $2y$13$OtGee9QX3rWNkPH.cqZZgebCZDCF2FUFoY2YtdpBxHxEBP2P9vBQK | 29110767d467219c7d3e69fbe2179623 |                         | 2011-12-01 11:27:40 | 2019-03-12 17:38:16 |
|             8 | alan.p.oensgen@gmail.com              | nan           |               nan |                  | alan    | poensgen   | female | 1b18739407706e9d47c978410c68fa15                             | 3c327f1fe0a5e33bcc3baf4093d65be3 |                         | 2011-12-06 17:37:03 | 2019-10-25 09:38:06 |
|            10 | e.killikh@mail.ru                     |   1.34878e+15 |               nan |                  | Евгения | Киллих     | female | 69f126c57e806dacadec92c6728b3e1c                             | bf8eb0a5b26879c0fba1cda5b6064474 |                         | 2011-12-06 18:21:46 | 2018-10-14 21:38:14 |
|            11 | alanpoensgen@gmail.com                | nan           |               nan |                  | Alan    | poensgen   | female | 368f201d9549ebc7ceaf12bf4f07f958                             | d497ce147b3c29da7b27937660faa6cc |                         | 2011-12-06 18:22:48 | 2013-10-28 18:55:44 |
|            17 | fedorinova.tatiana@gmail.com          | nan           |               nan |                  | Татьяна | Федоринова | female | 741512f9b9a977895d1b98672aea89ea                             | 76c554263494e06835fa5c0e65a186ec |                         | 2011-12-07 12:01:08 | 2014-07-02 18:16:45 |
|            20 | d.vasiliev7@gmail.com                 | nan           |               nan |                  | Denis   | Vasiliev   | male   | 8f459520b7d8506e473e383d7d782306                             | ea94a7f5a8339fe074a5298ec475464f |                         | 2011-12-07 16:28:47 | 2019-10-07 10:57:31 |
|            21 | manuela.stoll@mebelrama.ru            | nan           |               nan |                  | Manuela | Stoll      | female | 6f9c2c4784ddde9b68902370368b84de                             | b062159fb64a56201d9b63deefdaaf0e |                         | 2011-12-07 16:29:25 | 2019-10-07 10:58:00 |
|            22 | martell.hardenberg@rocket-internet.de | nan           |               nan |                  | Martell | Hardenberg | male   | 5fba6aa332e348884c3301a63a91df9e                             | 0d8d080a397a4be8a0f3b0f4584b004a |                         | 2011-12-07 16:31:44 | 2019-09-25 18:04:14 |
|            23 | y.turovtseva@gmail.com                | nan           |               nan |                  | Юлианна | Соколова   | female | $2y$13$yoVcjt/8eDK6yQzqpQcRKe9A8AI4uO45X8BQihD5JXD/IourXBnh6 | a26a61eb4520363edf9e1171139e6171 |                         | 2011-12-07 16:37:00 | 2019-11-11 00:18:45 |
```

> - Code name: index_0086
> - File path: Westwing.ru/Phone_Westwing.ru_11.2019_346k.txt
> - Total rows: 346219

### Schema
```
root
 |-- id_customer_address: integer (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- address1: string (nullable = true)
 |-- address2: string (nullable = true)
 |-- city: string (nullable = true)
 |-- postcode: string (nullable = true)
 |-- phone: string (nullable = true)

```

### Data sample
```
|   id_customer_address | first_name   | last_name   | gender   | address1                        | address2   | city                     |   postcode |              phone |
|----------------------:|:-------------|:------------|:---------|:--------------------------------|:-----------|:-------------------------|-----------:|-------------------:|
|                     1 | test         | test name   | male     | asdasda                         |            | muncih                   |      12345 |               4654 |
|                     3 | Динара       | Шарлапаева  | female   | Славянский бульвар, д 3 кв 21.  |            | Москва                   |     121352 |        79152451705 |
|                     8 | Test         | Test        | male     | lkdsflka                        |            | afdfadsfads              |  213810928 | 091239811234809834 |
|                    10 | Татьяна      | Федоринова  | female   | Варшавское ш., д. 9,            |            | Москва                   |     117623 |        79161890294 |
|                    11 | Елена        | Васильева   | female   | Краснобогатырская 79, 640       |            | Москва                   |     107076 |        79055390231 |
|                    17 | Анна         | Каверина    | female   | Новгородская улица, 5к1, 6      |            | Москва                   |     127576 |        79265557334 |
|                    20 | Анна         | Пахомова    | female   | ул. Бочкова д.5 кв. 38          |            | Москва                   |     129085 |        79057171412 |
|                    21 | Oksana       | Pak         | female   | Большой Козихинский пер, дом 8  | кв. 8      | Москва (в пределах МКАД) |      23104 |        79060960168 |
|                    22 | Виктория     | Голубова    | female   | Зоологическая ул 28 стр 2       | Кв 103     | Москва                   |     123056 |        79857771899 |
|                    23 | Mария        | Разумова    | female   | ул.Живописная д.17корп.2 кв.177 |            | Москва                   |     123103 |        79163203623 |
```


## About final data
> - Total rows: 60172

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
 |-- sex: integer (nullable = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```

### Data sample
```
| names                     | phones          | emails   | address                                                                                                                                                                |   sex | socials   |
|:--------------------------|:----------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------:|:----------|
| ['Филина Irina']          | ['74957696026'] |          | ['Москва в пределах МКАД ул. Ясный проезд д. 5 кв.76']                                                                                                                 |   nan |           |
| ['Булгакова Надя']        | ['74992606194'] |          | ['Москва в пределах МКАД Аргуновская 12-500']                                                                                                                          |   nan |           |
| ['Томилло Ирина']         | ['78125761532'] |          | ['Санкт-Петербург ул зодчего Росси дом 13 каб.507', 'санкт-петербург ул зодчего Россидом13 каб.507']                                                                   |   nan |           |
| ['Аседуллаева Екатерина'] | ['79002122249'] |          | ['Екатеринбург Свердловская область Проспект Космонавтов 52 204']                                                                                                      |   nan |           |
| ['Джаджиева Анна']        | ['79028195585'] |          | ['Ханты-Мансийск Ханты-Мансийский Автономный округ - Югра Ханты-Мансийск ул. Свободы д. 61 кв. 86']                                                                    |   nan |           |
| ['Наумчук Елена']         | ['79028567111'] |          | ['Нягань Ханты-Мансийский Автономный округ - Югра 6 мкр. дом 3 кв. 32']                                                                                                |   nan |           |
| ['Бабинова Елена']        | ['79028764118'] |          | ['Екатеринбург Свердловская область ул. Куйбишева д. 76 кв. 46', 'Екатеринбург Свердловская область ул. Куйбишева д. 76 кв. 46 Екатеринбург']                          |   nan |           |
| ['Сушкевич Наталья']      | ['79029906088'] |          | ['Красноярск Красноярский край Молокова 37']                                                                                                                           |   nan |           |
| ['Шиманова Зинаида']      | ['79030159552'] |          | ['Москва за пределами МКАД Московская обл.Люберецкий р-н КрасковоФедянинад.1кв.35', 'Москва за пределами МКАД Московская обл.Раменский р-н Капустиноул.Ромашковаяд.5'] |   nan |           |
| ['Флерова Наталия']       | ['79031098092'] |          | ['Москва в пределах МКАД Красноказарменная 16-б кВ.47']                                                                                                                |   nan |           |
```