# Parsetron results

## About row data

> - Code name: index_0273
> - File path: /media/user/SAMSUNG/Databases/index_0273/raw/romantino.ru/preprocessed/customers_preprocessed.csv
> - Total rows: 8626

### Schema
```
root
 |-- customer_id: integer (nullable = true)
 |-- firstname: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- email: string (nullable = true)
 |-- telephone: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- date_added: timestamp (nullable = true)
 |-- password: string (nullable = true)

```

### Data sample
```
|   customer_id | firstname    | lastname   | email                             |    telephone | ip              | date_added          | password                                 |
|--------------:|:-------------|:-----------|:----------------------------------|-------------:|:----------------|:--------------------|:-----------------------------------------|
|          6889 | Александра   |            | pansion.2019@yandex.ru            |  79859142091 | 162.158.183.208 | 2021-07-13 13:44:34 | 532294c946f05b4fa120da75a0aa89f2073f71a4 |
|          6886 | Инна         |            | tim-inna@yandex.ru                |  89117008710 | 178.252.66.11   | 2021-07-12 17:42:47 | ccc2d9010f4f9da37f7b89fbb6da6ab8d37f72d9 |
|          6887 | Светлана     |            | derkachdas89@gmail.com            |              | 162.158.183.214 | 2021-07-12 20:01:28 | 186ca64072f7ca0da031f20205c006f78032a826 |
|          6888 | Борис        |            | prolima@mail.ru                   |              | 162.158.92.6    | 2021-07-13 07:55:41 | 124cf81883085942f482f6dcd1b0b68c27ef1153 |
|          6885 | Анастасия    |            | pasynkova_94@mail.ru              |  89780063144 | 172.68.10.205   | 2021-07-12 11:02:37 | 0ebeb970c90deaeafe791b32dcfa7e79a9161ea6 |
|          6884 | Громова      | Викторовна | gromova-mis11@mail.ru             | +79032935481 | 162.158.183.158 | 2021-07-11 13:07:41 | bf3a539231e4e236973f0efd56c989bdea825194 |
|          6883 | Бэлла        |            | umar191116@mail.ru                |              | 162.158.89.226  | 2021-07-11 00:06:48 | 6bf0d5258831ff8b02a965428a42403ece7353e4 |
|          6882 | Дина         |            | ddziova@inbox.ru                  |              | 172.68.11.94    | 2021-07-10 13:27:05 | beca77021b9f5a4c9490040c4899228130a777f9 |
|          6881 | Чулков Роман |            | Roman0189@yandex.ru               | +79224520790 | 176.59.192.106  | 2021-07-10 11:48:18 | 10bd9bfac4e40aff8c3f660c556e6e645a47bf41 |
|          6880 | Дарья        |            | mrsnapoleon@mail.ru               |  89160064965 | 162.158.183.198 | 2021-07-09 01:13:06 | 4b749473a03f74fd27c98db49b25bf9e1c5d526e |
|          6879 | Татьяна      | Гудкова    | Tatyana.kalashnikova.1993@mail.ru |  89155626631 | 104.28.198.245  | 2021-07-08 14:52:26 | 1fe556413bda3682aaeaa3c7f2069ac1f841f11e |
|          6877 | Ольга        |            | nanova@mail.ru                    |  89104662789 | 172.68.245.200  | 2021-07-07 13:14:29 | 657fc09c02be23b8318a80cecf4c11bb1e46b865 |
|          6878 | Elena        |            | sternchen@mail.ru                 |  79218690654 | 172.68.246.219  | 2021-07-07 20:04:08 | f3431715d1e0cdd8fbf5b28c616b50c08bff30ca |
|          6876 | Ирина        |            | ib25061987@mail.ru                |              | 162.158.90.24   | 2021-07-07 11:40:25 | 48f968d7ab8086205d593a202892337c16d84f13 |
|          6875 | ольга        |            | olga.bobrovq2015@gmail.com        |              | 162.158.111.176 | 2021-07-06 13:57:12 | 843e2cbc4f6ea9a90ef1f7c380e20b67169a4a0f |
|          6872 | Влад         |            | korol23062000@gmail.com           |              | 162.158.183.214 | 2021-07-06 07:31:40 | 562019ab554b24b743608a7b0a9aebf4acb28a0a |
|          6873 |              |            | federal.8@yandex.ru               |              | 162.158.183.197 | 2021-07-06 07:51:58 | 68d61f9b02cb03e90f2fedadbbd6f6976b838d64 |
|          6874 | Ольга        |            | ov@centerir.ru                    |              | 172.68.10.107   | 2021-07-06 08:17:28 | cfbec53a765c415d5aec50e5e80eab4d7edf0e22 |
|          6871 | Виталий      |            | gehutz@yandex.ru                  |              | 141.101.104.187 | 2021-07-05 22:33:36 | 10b4adca0673d10d846110fc6065c76d5ac869a2 |
|          6870 | Елена        |            | em5171175@gmail.com               |              | 172.68.246.62   | 2021-07-05 21:44:32 | 63e010774886e271ef0ba9316c731e9bcd36ad29 |
```

> - Code name: index_0273
> - File path: /media/user/SAMSUNG/Databases/index_0273/raw/romantino.ru/preprocessed/customers_address_preprocessed.csv
> - Total rows: 1014

### Schema
```
root
 |-- customer_id: integer (nullable = true)
 |-- address_1: string (nullable = true)
 |-- city: string (nullable = true)
 |-- postcode: double (nullable = true)

```

### Data sample
```
|   customer_id | address_1                                                                                  | city                 |   postcode |
|--------------:|:-------------------------------------------------------------------------------------------|:---------------------|-----------:|
|          2524 | Родионова 189/24 кв. 224                                                                   | Нижний Новгород      |     603163 |
|          2520 | Пушкина ул., д. 9                                                                          | Тула                 |     300903 |
|          2518 | г. Тольятти, ул. Л.Чайкиной 52-97                                                          | г Тольятти           |     445008 |
|          2514 | Революционная ул., д. 52 А                                                                 | Тольятти             |     445028 |
|          2513 | ул Ленина д.117, кв.25                                                                     | г Нижняя Тура        |     624220 |
|          2512 | Кропоткинский пер, д 23 стр 1                                                              | г Москва             |        nan |
|          2509 | ул Белорусская, д 87 к 2 , кв.111                                                          | г Самара             |     443042 |
|          2506 | ул Крупской, д 61, кв 15                                                                   | г Пермь              |     614070 |
|          2503 | ул Шевченко, д 19 кв.30                                                                    | г Рыбинск            |     152909 |
|          2284 | тест 123                                                                                   | деревня Тестово      |        nan |
|          2277 | г Москва, ул Почтовая Б., д 1/33 стр 1 кв44                                                | г Москва             |        nan |
|          2275 | Калининградская область, Полесский район, поселок Тургенево, ул. Калининградская 2, дом 14 | Калининград          |     238646 |
|          2273 | ул.Аникина 19а                                                                             | Усолье Пермский край |     618460 |
|          2271 | ул Бунинская Аллея                                                                         | г Москва             |        nan |
|          2270 | Вологодская обл. г. Череповец пр. Московский 36-54                                         | Череповец            |     162602 |
|          2268 | ул. 60 лет ВЛКСМ 94\1                                                                      | Белореченск          |     352630 |
|          2266 | Пр-т К.Маркса, д. 159, кв. 97                                                              | Магнитогорск         |     455045 |
|          2265 | ул Артиллерийская, д 63, кв 45                                                             | г Калининград        |     236038 |
|          2264 | ул. Комсомольская, д.47, кв.12                                                             | г Лихославль         |     171210 |
|          2263 | ул Ленина ,дом 13                                                                          | рп Тума              |     391001 |
```

> - Code name: index_0273
> - File path: /media/user/SAMSUNG/Databases/index_0273/raw/romantino.ru/preprocessed/registered_customers_from_orders_preprocessed.csv
> - Total rows: 4319

### Schema
```
root
 |-- customer_id: integer (nullable = true)
 |-- firstname: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- email: string (nullable = true)
 |-- telephone: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- date_added: timestamp (nullable = true)
 |-- address: string (nullable = true)

```

### Data sample
```
|   customer_id | firstname            | lastname       | email                       | telephone       | ip             | date_added          | address                                               |
|--------------:|:---------------------|:---------------|:----------------------------|:----------------|:---------------|:--------------------|:------------------------------------------------------|
|             5 | Наталья              | Пушкина        | mi4664@yandex.ru            | +79104526301    | 86.62.106.177  | 2015-03-30 14:24:04 | Москва Дубининская, 65к2, кв.14                       |
|             6 | ИИММЯЯ               | ФФААММИИЛЛИИЯЯ | g1017056@trbvm.com          | 987456321       | 176.109.27.135 | 2015-04-04 01:56:04 | Саранск АДРЕССС                                       |
|             7 | Ната                 | Пуш            | mi4664@ya.ru                | 34234           | 86.62.106.177  | 2015-04-04 17:34:40 | Москва 123                                            |
|             8 | Дмитрий              | Потапенко      | dm.potapenko@gmail.com      | 89629389801     | 86.62.106.177  | 2016-08-17 12:51:05 | Москва ул Дубининская, д 65 к 2                       |
|            10 | Ольга                |                | olgawww2013@yandex.ru       | 89500952059     | 91.219.139.192 | 2015-04-13 15:24:29 | Усть-Илимск Энгельса д.15 кв. 229                     |
|            11 | Ольга                |                | ambal@aviel.ru              | +79269098512    | 93.185.192.65  | 2015-04-14 06:33:18 | Раменское Г. Раменское, ул. Михалевича, д.18, к1, кв7 |
|            15 | Роман                |                | roman_inozemcev@mail.ru     | 8-916-719-25-81 | 217.26.0.99    | 2015-04-16 21:01:57 |                                                       |
|            16 | таня                 |                | tan51071571@mail.ru         | 89608479448     | 31.28.61.66    | 2015-04-17 15:43:56 | тольятти Степана-Разина д79 кв80                      |
|            18 | ИЛЬМИРА              |                | ELKA525@MAIL.RU             | +79050198313    | 178.163.102.38 | 2015-04-17 21:43:55 | Тольятти ДЗЕРЖИНСКОГО                                 |
|            27 | Елена                |                | Solorados@yandex.ru         | 89094480573     | 128.74.174.231 | 2015-04-19 18:54:31 | Краснодар Атарбекова д1/1 постамат 2301-003:          |
|            30 | Ильгам               |                | ilgam-musical@yandex.ru     | 89173456067     | 77.94.119.46   | 2015-04-21 10:33:25 | Уфа ул.Гагарина 10/2-186                              |
|            31 | ольга                | ---            | volihina.olya@yandex.ru     | 89605237369     | 82.145.217.222 | 2015-06-03 15:07:29 | ----- -----                                           |
|            33 | Ольга                |                | iamlelik@yandex.ru          | 89096435596     | 193.46.207.100 | 2015-04-22 11:29:46 | Москва проспект Академика Сахарова, д. 18             |
|            37 | Инна                 |                | innashor@mail.ru            | 8(925)5526009   | 87.226.160.251 | 2015-04-23 12:11:14 | Москва Дмитровское шоссе, д.55, к.1, кв.75            |
|            39 | Надежда Владимировна |                | nadeniakalebedeva@yandex.ru | +79056345542    | 85.91.121.90   | 2015-04-24 10:50:14 |                                                       |
|            41 | олег                 |                | ovtribuno@mail.ru           | 89136602248     | 46.241.119.98  | 2015-04-24 22:02:13 |                                                       |
|            42 | Екатерина            | Шишкина        | shishkinakatie@yandex.ru    | 89146759823     | 80.83.239.29   | 2016-09-25 07:52:42 | Владивосток ул. Карбышева, д. 44, кв. 35              |
|            44 | татьяна              |                | tatyno@mail.ru              | 89069748373     | 93.159.240.178 | 2015-04-26 08:12:31 |                                                       |
|            47 | Михаил               | ---            | andreevm1@yandex.ru         | 89040311877     | 37.29.75.31    | 2016-03-22 15:05:44 | ----- -----                                           |
|            51 | Владимир             | ---            | Chigaryov777@mail.ru        | 89533200060     | 95.31.48.217   | 2016-03-21 12:04:48 | ----- -----                                           |
```

> - Code name: index_0273
> - File path: /media/user/SAMSUNG/Databases/index_0273/raw/romantino.ru/preprocessed/not_registered_customers_from_orders_preprocessed.csv
> - Total rows: 34193

### Schema
```
root
 |-- firstname: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- email: string (nullable = true)
 |-- telephone: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- date_added: timestamp (nullable = true)
 |-- address: string (nullable = true)

```

### Data sample
```
| firstname   | lastname    | email                        | telephone        | ip             | date_added          | address                                              |
|:------------|:------------|:-----------------------------|:-----------------|:---------------|:--------------------|:-----------------------------------------------------|
| Дмитрий     | Потапенко   | dm.potapenko@gmail.com       | +7 925 974 40 71 | 86.62.106.177  | 2015-02-01 18:07:41 | Москва Дуб 65                                        |
| Дарья       | Бабикова    | kotodo@mail.ru               | 89680302451      | 81.1.137.29    | 2015-04-28 21:01:09 |                                                      |
| Ткач        | Евгений     | evgeniy.tkach.73@mail.ru     | 89883471991      | 82.145.208.130 | 2015-04-28 22:08:01 |                                                      |
| Марина      | Рычкова     | maugros@yandex.ru            | 9183434332       | 46.158.240.175 | 2015-04-29 09:45:44 |                                                      |
| Татьяна     | Тиганова    | hramtzova.olga2010@yandex.ru | 89103171241      | 91.240.209.201 | 2015-04-29 10:17:58 | Курск проспект Дружбы, дом 2, кв 182                 |
| Дмитрий     | Аникин      | anakinr1@mail.ru             | 896-101-77-555   | 78.25.121.164  | 2015-04-29 22:17:10 | Тверь -----                                          |
| Наталия     | Цвигун      | cvigun_natalia@rambler.ru    | +79140149488     | 188.168.17.223 | 2015-04-30 05:25:47 | Усолье-Сибирское пр-т Красных Партизан, д.22, кв.119 |
| Денис       | Зуев        | denis.a.zuev@gmail.com       | 89037432983      | 91.220.93.136  | 2015-04-30 11:30:23 | Москва ул маши порываевой д.34 стр.1                 |
| Серкова     | Татьяна     | komp-du@mail.ru              | 9057776970       | 95.220.62.60   | 2015-04-30 12:14:04 | Дубна Понтекорво 8-25                                |
| Андрей      | ---         | andreyzem@list.ru            | 925 517-73-93    | 77.232.15.231  | 2015-04-30 22:33:13 | ----- -----                                          |
| игорь       | зайцев      | egor023@list.ru              | 89141955981      | 85.26.241.87   | 2015-05-01 08:05:24 | бикин хабаровский край матронина 7 кв 79             |
| Татьяна     | Колодий     | tatyanakolodiichik@mail.ru   | +79780090309     | 195.3.246.87   | 2015-05-01 10:07:49 | Черноморское ул.Комсомольская, д.1 кв.13             |
| РАИСА       | МИХАЙЛОВА   | risa.ru68@mail.ru            | 89062065369      | 94.143.240.220 | 2015-05-01 14:03:49 | ----- -----                                          |
| Алексей     | Копин       | kopin007@mail.ru             | +79005629434     | 95.52.69.54    | 2015-05-01 18:30:42 | ----- -----                                          |
| Наталья     | Марцинкевич | barselona7707@inbox.ru       | 89268235600      | 94.45.195.226  | 2015-05-02 11:24:55 | ----- -----                                          |
| Надежда     | Емельянова  | nadia4292@ya.ru              | 89222604292      | 212.96.202.82  | 2015-05-02 21:48:01 | Березово ХМАО Тюменской обл.                         |
| Сергей      | ---         | kabucha85@yandex.ru          | 89251893721      | 188.35.130.131 | 2015-05-02 22:37:25 | Москва Алтуфьевское шоссе д.86, к.1                  |
| Шаповалова  | Ириина      | shapovalova-yanulya@mail.ru  | 89515065511      | 95.153.160.61  | 2015-05-03 18:37:56 | Таганрог Сквозной 21                                 |
| Евгения     | Лысенко     | lysenkoef@yandex.ru          | 89817460526      | 188.187.12.112 | 2015-05-04 00:20:58 | ----- -----                                          |
| Николай     | Кузнецов    | rebusper@yandex.ru           | +7 9296820174    | 62.141.68.78   | 2015-05-04 09:55:05 | Москва Москва                                        |
```


## About final data
> - Total rows: 34481

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- actuality: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```

### Columns completeness
```
{
    "names": 100.0,
    "emails": 97.8,
    "phones": 87.65,
    "ips": 84.19,
    "actuality": 100.0,
    "address": 64.0,
    "accounts": 22.57
}
```

### Data sample
```
| names                              | emails                                | phones          | ips                                                                                          | actuality   | address                                                                     | accounts                                                                                                                                                                                    |
|:-----------------------------------|:--------------------------------------|:----------------|:---------------------------------------------------------------------------------------------|:------------|:----------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Александра']                     | ['pansion.2019@yandex.ru']            | ['79859142091'] | [Row(ip='162.158.183.208', date='13.07.2021'), Row(ip='162.158.183.158', date='13.07.2021')] | 13.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='pansion.2019@yandex.ru', password_hash='532294c946f05b4fa120da75a0aa89f2073f71a4')]            |
| ['Инна']                           | ['tim-inna@yandex.ru']                | ['79117008710'] | [Row(ip='178.252.66.11', date='12.07.2021'), Row(ip='172.68.11.94', date='13.07.2021')]      | 13.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='tim-inna@yandex.ru', password_hash='ccc2d9010f4f9da37f7b89fbb6da6ab8d37f72d9')]                |
| ['Светлана']                       | ['derkachdas89@gmail.com']            |                 |                                                                                              | 12.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='derkachdas89@gmail.com', password_hash='186ca64072f7ca0da031f20205c006f78032a826')]            |
| ['Борис']                          | ['prolima@mail.ru']                   |                 |                                                                                              | 13.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='prolima@mail.ru', password_hash='124cf81883085942f482f6dcd1b0b68c27ef1153')]                   |
| ['Анастасия']                      | ['pasynkova_94@mail.ru']              | ['79780063144'] | [Row(ip='172.68.10.205', date='12.07.2021')]                                                 | 12.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='pasynkova_94@mail.ru', password_hash='0ebeb970c90deaeafe791b32dcfa7e79a9161ea6')]              |
| ['Викторовна Громова']             | ['gromova-mis11@mail.ru']             | ['79032935481'] |                                                                                              | 11.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='gromova-mis11@mail.ru', password_hash='bf3a539231e4e236973f0efd56c989bdea825194')]             |
| ['Бэлла']                          | ['umar191116@mail.ru']                |                 |                                                                                              | 11.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='umar191116@mail.ru', password_hash='6bf0d5258831ff8b02a965428a42403ece7353e4')]                |
| ['Дина']                           | ['ddziova@inbox.ru']                  |                 |                                                                                              | 10.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='ddziova@inbox.ru', password_hash='beca77021b9f5a4c9490040c4899228130a777f9')]                  |
| ['Чулков Роман', 'Ирина Чулкова']  | ['roman0189@yandex.ru']               | ['79224520790'] | [Row(ip='176.59.192.106', date='10.07.2021'), Row(ip='37.79.36.224', date='18.07.2022')]     | 18.07.2022  | ['153035.0 Иваново Лежневская ул. д. 117', 'Иваново Лежневская ул. д. 117'] | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='Roman0189@yandex.ru', password_hash='10bd9bfac4e40aff8c3f660c556e6e645a47bf41')]               |
| ['Дарья']                          | ['mrsnapoleon@mail.ru']               | ['79160064965'] | [Row(ip='162.158.183.198', date='09.07.2021'), Row(ip='172.68.246.63', date='09.07.2021')]   | 09.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='mrsnapoleon@mail.ru', password_hash='4b749473a03f74fd27c98db49b25bf9e1c5d526e')]               |
| ['Гудкова Татьяна']                | ['tatyana.kalashnikova.1993@mail.ru'] | ['79155626631'] |                                                                                              | 08.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='Tatyana.kalashnikova.1993@mail.ru', password_hash='1fe556413bda3682aaeaa3c7f2069ac1f841f11e')] |
| ['Ольга']                          | ['nanova@mail.ru']                    | ['79104662789'] | [Row(ip='172.68.245.200', date='07.07.2021'), Row(ip='172.68.11.94', date='07.07.2021')]     | 07.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='nanova@mail.ru', password_hash='657fc09c02be23b8318a80cecf4c11bb1e46b865')]                    |
| ['Elena']                          | ['sternchen@mail.ru']                 | ['79218690654'] | [Row(ip='172.68.246.219', date='07.07.2021'), Row(ip='172.68.10.117', date='07.07.2021')]    | 07.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='sternchen@mail.ru', password_hash='f3431715d1e0cdd8fbf5b28c616b50c08bff30ca')]                 |
| ['Ирина']                          | ['ib25061987@mail.ru']                |                 |                                                                                              | 07.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='ib25061987@mail.ru', password_hash='48f968d7ab8086205d593a202892337c16d84f13')]                |
| ['Ольга']                          | ['olga.bobrovq2015@gmail.com']        |                 |                                                                                              | 06.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='olga.bobrovq2015@gmail.com', password_hash='843e2cbc4f6ea9a90ef1f7c380e20b67169a4a0f')]        |
| ['Влад']                           | ['korol23062000@gmail.com']           |                 |                                                                                              | 06.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='korol23062000@gmail.com', password_hash='562019ab554b24b743608a7b0a9aebf4acb28a0a')]           |
| ['Ольга']                          | ['ov@centerir.ru']                    |                 |                                                                                              | 06.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='ov@centerir.ru', password_hash='cfbec53a765c415d5aec50e5e80eab4d7edf0e22')]                    |
| ['Виталий']                        | ['gehutz@yandex.ru']                  |                 |                                                                                              | 05.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='gehutz@yandex.ru', password_hash='10b4adca0673d10d846110fc6065c76d5ac869a2')]                  |
| ['Елена']                          | ['em5171175@gmail.com']               |                 |                                                                                              | 05.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='em5171175@gmail.com', password_hash='63e010774886e271ef0ba9316c731e9bcd36ad29')]               |
| ['Миронова Анна', 'Анна Миронова'] | ['ask8080@rambler.ru']                | ['79261601410'] | [Row(ip='172.70.35.34', date='05.07.2021'), Row(ip='162.158.183.214', date='05.07.2021')]    | 05.07.2021  |                                                                             | [Row(title='Romantino.ru – интернет-магазин парфюмерии', link='https://romantino.ru', login='ask8080@rambler.ru', password_hash='a29751fabc67ee9ffe6cc0bc932af6d4c00f2bac')]                |
```