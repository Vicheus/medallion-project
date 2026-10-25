# Parsetron results

## About row data

> - Code name: index_0454
> - File path: customers.csv
> - Total rows: 52252

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- user_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- password: string (nullable = true)
 |-- facebook_id: long (nullable = true)
 |-- odnoklassniki_id: long (nullable = true)
 |-- vkontakte_id: integer (nullable = true)
 |-- created_at: timestamp (nullable = true)
 |-- updated_at: timestamp (nullable = true)

```

### Data sample
```
|   id | first_name   | last_name     | user_name                 | email                     | password                                                     |   facebook_id |   odnoklassniki_id |   vkontakte_id | created_at          | updated_at          |
|-----:|:-------------|:--------------|:--------------------------|:--------------------------|:-------------------------------------------------------------|--------------:|-------------------:|---------------:|:--------------------|:--------------------|
|  284 | Маргарита    | Игельник      | marg0sha@mail.ru          | marg0sha@mail.ru          | $2y$13$wrRNeN6uhWmCcM3ex9.fWOOifRFVAW1iCVN34LDR/OxIvYw1npYKW |   1.02113e+16 |      nan           |  nan           | 2017-09-24 03:52:17 | 2017-12-23 02:44:25 |
|  287 | Test         | Test          | test@test.com             | test@test.com             | $2y$13$obVLmQ1sGxmTWsQF6SDqie/w6f5/LirjPieA9Xw/vv4XC2V.rPtmO | nan           |      nan           |  nan           | 2017-10-15 18:34:58 | 2017-10-15 18:34:58 |
|  288 | Имяdfgdfg    | Фамилияdfgdfg | dfgdfg@dfgdfg.vom         | dfgdfg@dfgdfg.vom         | $2y$13$SKmSmhdkPvmcyXqDaYh3IeWK8.y6Lr/nCoypVdQ8sRI1OftE7kA0W | nan           |      nan           |  nan           | 2017-10-16 09:47:47 | 2017-10-16 09:47:47 |
|  289 | Сергей       | Романков      | jdjd@sjsu.sjdj            | jdjd@sjsu.sjdj            | $2y$13$FP8GyLO3DYLYJ0h.s2rc/OEZSiKkR35O9Zxz.OUBtDW8oTtRiD0KS | nan           |      nan           |    4.82541e+07 | 2017-10-18 12:47:12 | 2017-10-18 12:47:12 |
|  293 | Екатерина    | Дроздова      | mukhin@bk.ru              | mukhin@bk.ru              | $2y$13$YY366h.KmgcdJVu6f3wWnOY6i8ctSGzfhifpvg4yPnOHWshVxRglC | nan           |      nan           |    3.98377e+06 | 2017-11-06 00:06:05 | 2017-11-22 10:22:34 |
|  296 | Sveta        | Sveta         | svetlanafilina@yandex.ru  | svetlanafilina@yandex.ru  | $2y$13$nxG6FYNDCOWlLAGBQeE4HuFM.Z9Obu.gscYcGV5H8Wh/ZwKdNXifq |   1.86828e+15 |        5.59578e+11 |  nan           | 2017-11-10 17:13:39 | 2017-11-22 11:13:24 |
|  304 | Cheburek     | Cheburek      | nexus_j@list.tu           | nexus_j@list.tu           | $2y$13$qU.zZxN7xl5hgiuVJsUJsuqCbTadi6IpkTu774jV2Ee7f2Z6zxJP2 |   1.04781e+14 |      nan           |  nan           | 2017-11-30 19:51:07 | 2017-11-30 19:51:07 |
|  306 | Test         | Test          | test111@gmail.com         | test111@gmail.com         | $2y$13$sjLs/1goV3Xan501ebytduNd0IvgSdOSm.34JbuUSVmbVyYZsgEiG | nan           |      nan           |  nan           | 2017-12-07 13:30:37 | 2017-12-07 13:30:37 |
|  307 | Пррр         | Пррр          | iphonemini@p33.org        | iphonemini@p33.org        | $2y$13$lCBcE4n/Z578c3dAdKMt4OnS//mQaFmA1E6Lilur4mvWRvRGsCbW. | nan           |      nan           |  nan           | 2017-12-08 13:55:33 | 2017-12-08 13:55:33 |
|  322 | Marianna     | Nasheva       | nasheva99@inbox.ru        | nasheva99@inbox.ru        | $2y$13$St7u1Phg95R6KbSeAXp1teyvNdHuRG2OzOM/Kh2rvF0ItqtfgNQs2 | nan           |      nan           |  nan           | 2018-01-13 00:20:27 | 2018-02-25 22:35:58 |
|  310 | John         | John          | flyflyerson4@gmail.com    | flyflyerson4@gmail.com    | $2y$13$GxDLjlCmCPWRDBr.DgJckOSMnH9b6vJVRHCYJVEkOx8ggkUi6m9EK |   7.25944e+14 |      nan           |  nan           | 2017-12-22 19:45:03 | 2017-12-22 19:45:03 |
|  314 | Настя        | Волкова       | nastyshavolkova@gmail.com | nastyshavolkova@gmail.com | $2y$13$4vMjbgZo7FnTmToGdkQgue6RfSq.047NnpZYMaFF6FfDSN0fL9q1G | nan           |      nan           |    8.60085e+06 | 2018-01-04 13:49:16 | 2018-01-04 13:49:16 |
|  315 | Li           | Li            | lolitka66@gmail.com       | lolitka66@gmail.com       | $2y$13$7fxnFtu86UIhktPRuXV0oO.Bp/X2HpYcw89dFbyYab9yc80nAn.FS |   1.55994e+15 |      nan           |  nan           | 2018-01-05 12:52:18 | 2018-01-05 12:52:18 |
|  316 | Елена        | Маринина      | daev25@mail.ru            | daev25@mail.ru            | $2y$13$9D9iTXQMyUyNLIitBJu61./WPTJX9OnjV3Q2AIr8G/vpKFuv8KY1. | nan           |      nan           |  nan           | 2018-01-06 02:56:25 | 2018-01-06 02:56:25 |
|  317 | Настя        | Шевякова      | ntyrnov00@mail.ru         | ntyrnov00@mail.ru         | $2y$13$5cFZI9VpSvRtkaVWTRXqLuC4z.CBiOERlEOs1PM24.PVpLtRS8uMS | nan           |      nan           |    2.8298e+08  | 2018-01-07 13:15:41 | 2018-01-07 13:15:41 |
|  320 | Олллл        | Проо          | tttt@gh.vhh               | tttt@gh.vhh               | $2y$13$/1/LiiCiOjJbIhGX7wKF2OuN4ChHsOIYY865.UUOfEhpWmAYNrpl6 | nan           |      nan           |  nan           | 2018-01-12 17:13:15 | 2018-01-12 17:13:15 |
|  321 | Диана        | Мелкумова     | dmelkumova@inbox.ru       | dmelkumova@inbox.ru       | $2y$13$0PQh4eHyxPFg1iw.ZzjmtuXrCvLlwMS9H2.wc3OiPGD5203sFb2gO | nan           |      nan           |    1.08862e+08 | 2018-01-12 23:02:35 | 2018-01-12 23:02:35 |
|  323 | Kristi       | Kristi        | taranets13@gmail.com      | taranets13@gmail.com      | $2y$13$VzUV6.rBZHn3Zj2N3Px0SOEC65HbRiAv/7nrWN08Mmi6GUJDDG76K |   1.56593e+15 |      nan           |  nan           | 2018-01-15 07:50:56 | 2018-01-15 07:50:56 |
|  324 | Иван         | Белобородов   | mail@beliv.net            | mail@beliv.net            | $2y$13$wfhXm8Z5rIBMrXI5H9KuKuuhkX9zFHKwkg5UIzqduM/YewclpZExO | nan           |      nan           |  nan           | 2018-01-15 20:39:13 | 2018-09-17 23:26:28 |
|  292 | Leonid       | Leonid        | sotnikovl@mail.ru         | sotnikovl@mail.ru         | $2y$13$n8SCkLxziZ3IAhEsghKeMOIgjV1Dzns7gxGIzkpwKiWWvqqtDKxwS |   1.29509e+15 |      nan           |    7.64932e+07 | 2017-11-05 20:25:27 | 2018-02-15 19:44:16 |
```

> - Code name: index_0454
> - File path: customers_address.csv
> - Total rows: 28409

### Schema
```
root
 |-- customer_id: integer (nullable = true)
 |-- id: integer (nullable = true)
 |-- city_id: integer (nullable = true)
 |-- order_id: integer (nullable = true)
 |-- street: string (nullable = true)
 |-- customer_first_name: string (nullable = true)
 |-- customer_last_name: string (nullable = true)
 |-- customer_phone_number: string (nullable = true)
 |-- house: string (nullable = true)
 |-- flat: string (nullable = true)
 |-- pvz_сode: string (nullable = true)
 |-- delivery_dispatch_number: integer (nullable = true)
 |-- delivery_start_date: timestamp (nullable = true)
 |-- delivery_status_id: integer (nullable = true)
 |-- delivery_status_date: timestamp (nullable = true)
 |-- delivery_status_city: string (nullable = true)
 |-- delivery_status_description: string (nullable = true)
 |-- delivery_substatus_id: integer (nullable = true)
 |-- delivery_substatus_date: timestamp (nullable = true)
 |-- delivery_substatus_description: string (nullable = true)
 |-- cash_on_delivery_fact: double (nullable = true)
 |-- delivery_price: double (nullable = true)
 |-- free_shipping: string (nullable = true)
 |-- post_code: string (nullable = true)
 |-- delivery_tariff_id: integer (nullable = true)
 |-- skip_delivery_price_calculation: string (nullable = true)
 |-- id_suffix: string (nullable = true)

```

### Data sample
```
|   customer_id |   id |   city_id |   order_id | street                       | customer_first_name   | customer_last_name   | customer_phone_number   | house               | flat        | pvz_сode   |   delivery_dispatch_number | delivery_start_date   |   delivery_status_id | delivery_status_date   | delivery_status_city   | delivery_status_description   |   delivery_substatus_id | delivery_substatus_date   | delivery_substatus_description   |   cash_on_delivery_fact |   delivery_price | free_shipping   |   post_code |   delivery_tariff_id | skip_delivery_price_calculation   | id_suffix   |
|--------------:|-----:|----------:|-----------:|:-----------------------------|:----------------------|:---------------------|:------------------------|:--------------------|:------------|:-----------|---------------------------:|:----------------------|---------------------:|:-----------------------|:-----------------------|:------------------------------|------------------------:|:--------------------------|:---------------------------------|------------------------:|-----------------:|:----------------|------------:|---------------------:|:----------------------------------|:------------|
|           322 |  737 |      3959 |        706 | Эдуардовна                   | Марианна              | Нашева               | 7 (928) 657-50-42       | Переулок Крылова 18 | Частный дом |            |                1.07054e+09 | 2018-01-15 10:22:40   |                    4 | 2018-01-22 10:59:56    | Черкесск               | Вручен                        |                     nan | 2018-01-22 14:00:03       |                                  |                 1327.42 |           337.42 | f               |      369000 |                  137 |                                   |             |
|           326 |  739 |      6190 |        708 | 1-ая ватутинская             | Ирина                 | Глушкова             | 7 (916) 312-69-98       | 6                   | 86          |            |                1.07129e+09 | 2018-01-21 13:45:37   |                    4 | 2018-01-23 09:08:28    | Троицк, Москов. обл.   | Вручен                        |                     nan | 2018-01-23 12:10:02       |                                  |                  288.02 |           288.02 | f               |      108818 |                  137 |                                   |             |
|           292 |  678 |      6190 |        650 | Якорная улица                | Леонид                | Сотников             | 7 (963) 687-19-30       | 9                   | 124         |            |              nan           | NaT                   |                  nan | NaT                    |                        |                               |                     nan | NaT                       |                                  |                    0    |           268.68 | f               |      115407 |                  137 |                                   |             |
|           356 |  750 |      6190 |        718 | Новочеремушкинская           | Евгения               | Аверьянова           | 7 (906) 766-93-00       | 9                   | 70          |            |                1.07258e+09 | 2018-02-01 11:58:55   |                    1 | 2018-02-01 09:01:43    | Москва                 | Создан                        |                     nan | 2018-02-03 21:50:02       |                                  |                    0    |           281.23 | f               |      117447 |                  137 |                                   |             |
|           425 |  788 |      6190 |        756 | Капотня 5-й квартал          | Василиса              | Сартакова            | 7 (926) 569-42-11       | 17                  | 83          |            |                1.07367e+09 | 2018-02-15 11:09:37   |                    1 | 2018-02-15 08:09:36    | Москва                 | Создан                        |                     nan | 2018-02-15 12:05:01       |                                  |                    0    |           266.81 | f               |      109649 |                  137 |                                   |             |
|           331 |  741 |      6190 |        710 | ул. Профсоюзная              | Евгения               | Тарасова             | 7 (915) 094-50-50       | 128, корп. 3        | Самовывоз   | MSK98      |                1.07167e+09 | 2018-01-24 11:45:25   |                    1 | 2018-01-24 10:24:46    | Москва                 | Создан                        |                     nan | 2018-01-29 10:20:04       |                                  |                    0    |           162.49 | f               |             |                  136 |                                   |             |
|           292 |  679 |      6190 |        651 | Якорная улица                | Леонид                | Сотников             | 7 (963) 687-19-30       | 9                   | 124         |            |                1.06243e+09 | 2017-11-05 21:27:45   |                    1 | 2017-11-05 18:27:44    | Москва                 | Создан                        |                     nan | 2017-11-06 16:04:40       |                                  |                    0    |           268.68 | f               |      115407 |                  137 |                                   |             |
|           286 |  658 |      6190 |        630 | Краснобогатырская улица      | Илья                  | Кайнов               | 7 (926) 178-03-07       | 9                   | 99          |            |                1.0604e+09  | 2017-10-15 20:46:24   |                    5 | NaT                    |                        |                               |                     nan | NaT                       |                                  |                    0    |           285    | f               |      107564 |                  137 |                                   |             |
|           286 |  659 |      7387 |        631 | Гагарина                     | Маргарита             | Игельник             | 7 (926) 178-03-08       | 40                  | 394         |            |                1.06099e+09 | 2017-10-20 18:11:08   |                    5 | NaT                    |                        |                               |                     nan | NaT                       |                                  |                    0    |           285    | f               |      143996 |                  137 |                                   |             |
|           423 |  790 |      6190 |        758 | Боровая                      | Айгуль                | Бедретдинова         | 7 (903) 534-88-34       | 16                  | 64          |            |                1.07375e+09 | 2018-02-16 10:03:01   |                    1 | 2018-02-16 07:03:01    | Москва                 | Создан                        |                     nan | 2018-02-16 12:40:03       |                                  |                    0    |           287.35 | f               |      111020 |                  137 |                                   |             |
|           291 |  669 |      6190 |        641 | Хамовнический Вал улица      | Алексей               | Юдин                 | 7 (903) 748-47-27       | 36                  | 88          |            |                1.06278e+09 | 2017-11-09 11:46:08   |                    4 | 2017-11-13 16:06:43    | Москва                 | Вручен                        |                     nan | 2017-11-14 19:56:25       |                                  |                  296.33 |           278.43 | f               |      119048 |                  137 |                                   |             |
|           296 |  703 |      6190 |        675 | Садовническая улица          | Света                 | Филина               | 7 (925) 490-49-54       | 72 строение 1       | Офис 3      |            |              nan           | NaT                   |                  nan | NaT                    |                        |                               |                     nan | NaT                       |                                  |                    0    |           270.93 | f               |      115035 |                  137 |                                   |             |
|           296 |  704 |      6190 |        675 | Краснопресненская набережная | Маша                  | Истомина             | 7 (967) 130-11-14       | 12                  | Офис 1104   |            |              nan           | NaT                   |                  nan | NaT                    |                        |                               |                     nan | NaT                       |                                  |                    0    |           270.93 | f               |      123610 |                  137 |                                   |             |
|           322 |  748 |      3959 |        716 | Переулок Крылова 18          | Марианна              | Нашева               | 7 (928) 657-50-42       | Частный             | Нет         |            |                1.07178e+09 | 2018-01-25 10:45:01   |                    4 | 2018-01-31 11:49:50    | Черкесск               | Вручен                        |                     nan | 2018-01-31 14:50:02       |                                  |                  757.37 |           333.67 | f               |      369000 |                  137 |                                   |             |
|           286 |  660 |      7387 |        632 | Гагарина                     | Маргарита             | Игельник             | 7 (926) 178-03-08       | 40                  | 394         |            |                1.06127e+09 | 2017-10-24 12:00:16   |                    4 | 2017-10-30 16:18:09    | Реутов                 | Вручен                        |                     nan | 2017-10-31 11:27:20       |                                  |                  308    |           285    | f               |      143996 |                  137 |                                   |             |
|           286 |  661 |      7387 |        633 | Гагарина                     | Маргарита             | Игельник             | 7 (926) 178-03-08       | 40                  | 394         |            |                1.06234e+09 | 2017-11-03 17:40:44   |                  nan | NaT                    |                        |                               |                     nan | NaT                       |                                  |                    0    |           306.75 | f               |      143996 |                  137 |                                   |             |
|           296 |  699 |      6190 |        671 | Садовническая улица          | Света                 | Филина               | 7 (925) 490-49-54       | 72 строение 1       | Офис 3      |            |                1.06488e+09 | 2017-11-24 11:04:36   |                    4 | 2017-11-28 13:05:12    | Москва                 | Вручен                        |                     nan | 2017-11-28 16:10:03       |                                  |                  278.83 |           270.93 | f               |      115035 |                  137 |                                   |             |
|           286 |  693 |      6190 |        665 | Ленинский проспект           | Илья                  | Кайнов               | 7 (926) 178-03-07       | 6 строение 20       | Офис Айлав  |            |                1.06359e+09 | 2017-11-15 20:32:09   |                    4 | 2017-11-29 11:39:20    | Москва                 | Вручен                        |                     nan | 2017-11-29 14:40:02       |                                  |                    0    |           270.93 | f               |      119049 |                  137 |                                   |             |
|           322 |  758 |      3959 |        726 | Переулок Крылова 18          | Марианна              | Нашева               | 7 (928) 657-50-42       | Частный             | Нет         |            |                1.07286e+09 | 2018-02-05 13:04:50   |                    4 | 2018-02-09 09:06:13    | Черкесск               | Вручен                        |                     nan | 2018-02-09 12:10:02       |                                  |                 1114.81 |           336    | f               |      369000 |                  137 |                                   |             |
|           296 |  701 |      9664 |        673 | Заречная улица               | Лилия                 | Аношкина             | 7 (925) 711-21-00       | 11к4                | 260         |            |                1.06488e+09 | 2017-11-24 11:05:21   |                    4 | 2017-12-02 13:04:06    | Санкт-Петербург        | Вручен                        |                     nan | 2017-12-02 16:05:02       |                                  |                    0    |           298.68 | f               |      194356 |                  137 |                                   |             |
```


## About final data
> - Total rows: 64740

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
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
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 20.17% |
| Emails | 79.83% |
| Address | 20.07% |
| Socials | 23.62% |
| Accounts | 79.83% |
| Raw_metadata | 20.17% |
| Actuality | 79.83% |



### Data sample
```
| names                     | phones   | emails                         | address   | socials                                                                 | accounts                                                                                                                                                                                                        | raw_metadata   | actuality   |
|:--------------------------|:---------|:-------------------------------|:----------|:------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:------------|
| ['Akhmadeeva Mila']       |          | ['miliaahma29@mail.ru']        |           |                                                                         | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='miliaahma29@mail.ru', password_hash='$2y$13$MK0bstmg2.e2badrh1sBS.iyTESbfgLQKyUx.kNZEdBG/NWUe4Ot6')]        |                | 26.07.2020  |
| ['Alipov Ali']            |          | ['alikatimka23@gmail.com']     |           | [Row(title='Vk', id='490375194', link=None, comment=None)]              | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='alikatimka23@gmail.com', password_hash='$2y$13$GzKoBmKOvyBRAsVzC6KqE.T11GXFMjVcG4P4EzHk5cThsPwcSum5u')]     |                | 18.08.2018  |
| ['Borodin Andrey']        |          | ['bortihu@gmail.com']          |           | [Row(title='Vk', id='341099622', link=None, comment=None)]              | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='bortihu@gmail.com', password_hash='$2y$13$dsiAyz09NKYHBImGdXsZFunfZBtmzX2qoUe9z5bc0AYO1cVuNGeBC')]          |                | 31.08.2021  |
| ['Gridina Yulia']         |          | ['gridina20021408@mail.ru']    |           |                                                                         | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='gridina20021408@mail.ru', password_hash='$2y$13$xV2yKqNVw5684xMoCAxyGOoXLsumwDUL9ozcTkTWaFG0ca0qh520q')]    |                | 09.06.2020  |
| ['Ilarionova Juliia']     |          | ['pri4ina21@gmail.com']        |           |                                                                         | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='pri4ina21@gmail.com', password_hash='$2y$13$TFOVMThfRrgNZyZ6dvFWyecZmLDmzxlg9nnCps2PWn97mWoT5NxA2')]        |                | 12.10.2019  |
| ['Julia Julia']           |          | ['karlfrazetty@gmail.com']     |           | [Row(title='Facebook', id='2586457854959628', link=None, comment=None)] | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='karlfrazetty@gmail.com', password_hash='$2y$13$m1uHrsnK9u9Itl6rKNj6yOFErq9RgARq9DIXPdhv9E9oDurmo4YmO')]     |                | 14.03.2020  |
| ['Karasev Roman']         |          | ['a6sent@gmail.com']           |           |                                                                         | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='a6sent@gmail.com', password_hash='$2y$13$r.DEnM2Pk7VQNO6IA2FiMO9Ur.jj7.Wi74El8ZeoVfHKI/zH6S/w2')]           |                | 09.06.2021  |
| ['Kardanova Amina']       |          | ['kardanovaamina0@gmail.com']  |           | [Row(title='Vk', id='474724438', link=None, comment=None)]              | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='kardanovaamina0@gmail.com', password_hash='$2y$13$Sm.3lClvp2Ssgk2svHR9be4tQZfOWDzzSr1GYOTFoqVg2h1AALgf6')]  |                | 29.03.2019  |
| ['Kolpakov Egor']         |          | ['kolpakov_eg@inbox.ru']       |           |                                                                         | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='kolpakov_eg@inbox.ru', password_hash='$2y$13$irMEI2sqsW2R8bRvAqJfU.KBmos.5IISK7PfoxVAmFXEh/9Q.RhbO')]       |                | 22.01.2021  |
| ['Ksenia Ksenia']         |          | ['kladygina@gmail.com']        |           | [Row(title='Facebook', id='1870678236334900', link=None, comment=None)] | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='kladygina@gmail.com', password_hash='$2y$13$tTZs9dk1GUT8VpdgtAI6E.3YMZ.KqK5bgeQiJf2Khut3Qe30/G02q')]        |                | 31.08.2018  |
| ['Life Thug-Bbiiiiiiiii'] |          | ['ladohka1999@icloud.com']     |           | [Row(title='Vk', id='453421631', link=None, comment=None)]              | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='ladohka1999@icloud.com', password_hash='$2y$13$P/1IvcgxX6TGaKq2WKPtnu3j0FAdfm08B49H5Tuv/pwR94r7r0HuK')]     |                | 25.06.2021  |
| ['Manukyan Marianna']     |          | ['mary_manuk@icloud.com']      |           | [Row(title='Vk', id='320690604', link=None, comment=None)]              | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='mary_manuk@icloud.com', password_hash='$2y$13$/Ti5Bo3ud0dKMAiV.V3iBeozNf6c5gEhCy9tPu0hBUN3uz9KUN692')]      |                | 04.09.2018  |
| ['Mila Mila']             |          | ['mila.falyush@gmail.com']     |           | [Row(title='Facebook', id='2468016980143445', link=None, comment=None)] | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='mila.falyush@gmail.com', password_hash='$2y$13$qkwG3yDMqB9qVSE6k/oiFeRJV0v0kka2v1Av1gGelD19p2MkXGqVe')]     |                | 08.08.2019  |
| ['Natalia Natalia']       |          | ['blackberry.elf@yandex.ru']   |           | [Row(title='Facebook', id='2708260202732758', link=None, comment=None)] | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='blackberry.elf@yandex.ru', password_hash='$2y$13$bvr55QMwM1RHB1P7Ncd81.9Vev0KzSEWTsC6gTSCNkpS1400uXzS.')]   |                | 26.09.2018  |
| ['Rusakova Diana']        |          | ['dianarusakova48@gmail.com']  |           | [Row(title='Vk', id='380740622', link=None, comment=None)]              | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='dianarusakova48@gmail.com', password_hash='$2y$13$T528euwCZ3T1Znf9IZ/iJeufRWd/F7Ctw8Ijp/CyM668SjH/e8jkC')]  |                | 28.03.2020  |
| ['S.V. S.V.']             |          | ['glta6wjlaztw@mail.ru']       |           |                                                                         | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='glta6wjlaztw@mail.ru', password_hash='$2y$13$BfWRojfv8sLQwEjSCetiAevCarb1JBXBGKzMlMtT8DxfXdjgWbU82')]       |                | 02.07.2020  |
| ['Sasha Sasha']           |          | ['jm007vik@gmail.com']         |           | [Row(title='Facebook', id='978733675893666', link=None, comment=None)]  | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='jm007vik@gmail.com', password_hash='$2y$13$SV0DJ8ol8mBD/eg6pIQ4hu9V/ErW2DFFYTIUkdgsCoLdRP9Rp7fYK')]         |                | 22.06.2020  |
| ['Shm Enny']              |          | ['ennyshmurina2000@mail.ru']   |           |                                                                         | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='ennyshmurina2000@mail.ru', password_hash='$2y$13$pyjBY1U1JuxI3/YGhfnn0.NeC6XVqC1f/dYCPei8aiAkKNIinXS/y')]   |                | 13.10.2019  |
| ['Valeri Valeri']         |          | ['valeri.gor102002@gmail.com'] |           | [Row(title='Facebook', id='728608794206493', link=None, comment=None)]  | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='valeri.gor102002@gmail.com', password_hash='$2y$13$IOPycK4Jh.5VA2iJQ0smueaRxY4dDN7v2tb1qcEBzgpfFMfHdbAjG')] |                | 01.03.2019  |
| ['Zimina Polina']         |          | ['zimorodok2000@mail.ru']      |           | [Row(title='Vk', id='122102488', link=None, comment=None)]              | [Row(title='Mimigram - лучшее приложение для печати фотографий', link='https://mimigram.ru', login='zimorodok2000@mail.ru', password_hash='$2y$13$y8cHg7Vvz5dhv2xzF7KcmuLVvoDnyx7EzrCIpOUXqCHeGmM/zrSBK')]      |                | 29.07.2018  |
```