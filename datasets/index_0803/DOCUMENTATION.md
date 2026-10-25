# Parsetron results

## About row data

> - File path: topbilet_clean.csv
> - Total rows: 449569

### Schema
```
root
 |-- ticket_id: string (nullable = true)
 |-- order_id: string (nullable = true)
 |-- timetable_id: string (nullable = true)
 |-- section: string (nullable = true)
 |-- pricecat: string (nullable = true)
 |-- row: string (nullable = true)
 |-- seat: string (nullable = true)
 |-- price0: string (nullable = true)
 |-- discount: string (nullable = true)
 |-- price: string (nullable = true)
 |-- fee1: string (nullable = true)
 |-- fee2: string (nullable = true)
 |-- price_after: string (nullable = true)
 |-- promocode: string (nullable = true)
 |-- promo_discount: string (nullable = true)
 |-- sum_after: string (nullable = true)
 |-- final_price: string (nullable = true)
 |-- invite_fee: string (nullable = true)
 |-- barcode: string (nullable = true)
 |-- email: string (nullable = true)
 |-- name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- buyer_email: string (nullable = true)
 |-- buyer_name: string (nullable = true)
 |-- buyer_phone: string (nullable = true)
 |-- order_date: string (nullable = true)
 |-- sale_type: string (nullable = true)
 |-- platform: string (nullable = true)
 |-- comment: string (nullable = true)

```

### Data sample
```
|   ticket_id |   order_id |   timetable_id | section   | pricecat       | row   | seat   |   price0 |   discount |   price |   fee1 |   fee2 |   price_after |   promocode |   promo_discount |   sum_after | final_price   |   invite_fee |      barcode | email                        | name               |       phone | buyer_email   | buyer_name   | buyer_phone   | order_date          | sale_type   | platform   |      comment |
|------------:|-----------:|---------------:|:----------|:---------------|:------|:-------|---------:|-----------:|--------:|-------:|-------:|--------------:|------------:|-----------------:|------------:|:--------------|-------------:|-------------:|:-----------------------------|:-------------------|------------:|:--------------|:-------------|:--------------|:--------------------|:------------|:-----------|-------------:|
|     1170962 |   10548982 |           4485 | Входной   | Взрослый билет | -     | -      |     3000 |          0 |    3000 |    150 |      0 |          3150 |           0 |             3000 |        3150 |               |            0 |  13053152865 | maksimv980@gmail.com         | Максим             | 77786381244 |               |              |               | 2026-10-05 02:04:51 | kaspi       | topbilet   | 700811400587 |
|     1170932 |   10548967 |           4443 | Партер    |                | 5     | 18     |     5000 |          0 |    5000 |      0 |      0 |          5000 |           0 |             5000 |        5000 |               |            0 | 117093254799 | raiyan12127@gmail.com        | Арайлым            | 77757769300 |               |              |               | 2026-10-05 01:21:26 | tiptop      | topbilet   | 930307301368 |
|     1170933 |   10548967 |           4443 | Партер    |                | 5     | 19     |     5000 |          0 |    5000 |      0 |      0 |          5000 |           0 |             5000 |        5000 |               |            0 | 117093346779 | raiyan12127@gmail.com        | Арайлым            | 77757769300 |               |              |               | 2026-10-05 01:21:26 | tiptop      | topbilet   | 930307301368 |
|     1170934 |   10548967 |           4443 | Партер    |                | 5     | 20     |     5000 |          0 |    5000 |      0 |      0 |          5000 |           0 |             5000 |        5000 |               |            0 | 117093472421 | raiyan12127@gmail.com        | Арайлым            | 77757769300 |               |              |               | 2026-10-05 01:21:26 | tiptop      | topbilet   | 930307301368 |
|     1170935 |   10548967 |           4443 | Партер    |                | 5     | 21     |     5000 |          0 |    5000 |      0 |      0 |          5000 |           0 |             5000 |        5000 |               |            0 | 117093597006 | raiyan12127@gmail.com        | Арайлым            | 77757769300 |               |              |               | 2026-10-05 01:21:26 | tiptop      | topbilet   | 930307301368 |
|     1170923 |   10548962 |           4475 | Партер    |                | 1     | 13     |     6000 |          0 |    6000 |      0 |      0 |          6000 |           0 |             6000 |        6000 |               |            0 | 117092322772 | abdizhapparbalnur@icloud.com | Balnur Abdizhappar | 77022120707 |               |              |               | 2026-10-05 01:15:03 | kaspi       | topbilet   |              |
|     1170924 |   10548962 |           4475 | Партер    |                | 1     | 12     |     6000 |          0 |    6000 |      0 |      0 |          6000 |           0 |             6000 |        6000 |               |            0 | 117092417230 | abdizhapparbalnur@icloud.com | Balnur Abdizhappar | 77022120707 |               |              |               | 2026-10-05 01:15:03 | kaspi       | topbilet   |              |
|     1170925 |   10548962 |           4475 | Партер    |                | 1     | 11     |     6000 |          0 |    6000 |      0 |      0 |          6000 |           0 |             6000 |        6000 |               |            0 | 117092560812 | abdizhapparbalnur@icloud.com | Balnur Abdizhappar | 77022120707 |               |              |               | 2026-10-05 01:15:03 | kaspi       | topbilet   |              |
|     1170926 |   10548962 |           4475 | Партер    |                | 1     | 10     |     6000 |          0 |    6000 |      0 |      0 |          6000 |           0 |             6000 |        6000 |               |            0 | 117092656419 | abdizhapparbalnur@icloud.com | Balnur Abdizhappar | 77022120707 |               |              |               | 2026-10-05 01:15:03 | kaspi       | topbilet   |              |
|     1170918 |   10548960 |           4416 | Сектор Б  |                | 4     | 15     |     8000 |          0 |    8000 |      0 |      0 |          8000 |           0 |             8000 |        8000 |               |            0 | 117091855516 | abdizhapparbalnur@icloud.com | Balnur Abdizhappar | 77022120707 |               |              |               | 2026-10-05 01:08:33 | kaspi       | topbilet   |              |
|     1170919 |   10548960 |           4416 | Сектор Б  |                | 4     | 14     |     8000 |          0 |    8000 |      0 |      0 |          8000 |           0 |             8000 |        8000 |               |            0 | 117091938525 | abdizhapparbalnur@icloud.com | Balnur Abdizhappar | 77022120707 |               |              |               | 2026-10-05 01:08:33 | kaspi       | topbilet   |              |
|     1170917 |   10548959 |           4439 | Партер    |                | 2     | 18     |     8000 |          0 |    8000 |      0 |      0 |          8000 |           0 |             8000 |        8000 |               |            0 | 117091725268 | kurmanova_shugyla@mail.ru    | Шұғыла             | 77473250438 |               |              |               | 2026-10-05 01:07:44 | kaspi       | topbilet   |  40615650165 |
|     1170897 |   10548947 |           4434 | Партер    |                | 1     | 18     |     6500 |          0 |    6500 |      0 |      0 |          6500 |           0 |             6500 |        6500 |               |            0 | 117089739314 | www.janaika.kz88@mail.ru     | Айгерим            | 77056371188 |               |              |               | 2026-10-05 00:37:01 | kaspi       | topbilet   | 880927400966 |
|     1170881 |   10548938 |           4416 | Сектор Г  |                | 3     | 25     |     8000 |          0 |    8000 |      0 |      0 |          8000 |           0 |             8000 |        8000 |               |            0 | 117088128864 | kapaldin@mail.ru             | Dinara             | 77017688247 |               |              |               | 2026-10-05 00:25:19 | kaspi       | topbilet   | 850927402485 |
|     1170882 |   10548938 |           4416 | Сектор Г  |                | 3     | 26     |     8000 |          0 |    8000 |      0 |      0 |          8000 |           0 |             8000 |        8000 |               |            0 | 117088227371 | kapaldin@mail.ru             | Dinara             | 77017688247 |               |              |               | 2026-10-05 00:25:19 | kaspi       | topbilet   | 850927402485 |
|     1170883 |   10548938 |           4416 | Сектор Г  |                | 3     | 27     |     8000 |          0 |    8000 |      0 |      0 |          8000 |           0 |             8000 |        8000 |               |            0 | 117088316515 | kapaldin@mail.ru             | Dinara             | 77017688247 |               |              |               | 2026-10-05 00:25:19 | kaspi       | topbilet   | 850927402485 |
|     1170878 |   10548936 |           4471 | Сектор А  |                | 24    | 3      |    40000 |          0 |   40000 |   2000 |      0 |         42000 |           0 |            40000 |       42000 |               |            0 |  13050360014 | sssayat@mail.ru              | Молдир             | 77770060673 |               |              |               | 2026-10-05 00:24:20 | tiptop      | topbilet   | 860411450729 |
|     1170879 |   10548936 |           4471 | Сектор А  |                | 24    | 4      |    40000 |          0 |   40000 |   2000 |      0 |         42000 |           0 |            40000 |       42000 |               |            0 |  13050441068 | sssayat@mail.ru              | Молдир             | 77770060673 |               |              |               | 2026-10-05 00:24:20 | tiptop      | topbilet   | 860411450729 |
|     1170860 |   10548926 |           4434 | Партер    |                | 5     | 23     |     6500 |          0 |    6500 |      0 |      0 |          6500 |           0 |             6500 |        6500 |               |            0 | 117086053905 | baytimur77@mail.ru           | Тимур              | 77057043749 |               |              |               | 2026-10-05 00:16:19 | kaspi       | topbilet   | 770507300263 |
|     1170861 |   10548926 |           4434 | Партер    |                | 5     | 22     |     6500 |          0 |    6500 |      0 |      0 |          6500 |           0 |             6500 |        6500 |               |            0 | 117086115660 | baytimur77@mail.ru           | Тимур              | 77057043749 |               |              |               | 2026-10-05 00:16:19 | kaspi       | topbilet   | 770507300263 |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- actuality: date (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 98.00% |
| Emails | 99.95% |
| Actuality | 100.00% |
| Raw_metadata | 0.00% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                   | phones          | emails                           | actuality   | raw_metadata   | source_entity_id                                         |
|:------------------------|:----------------|:---------------------------------|:------------|:---------------|:---------------------------------------------------------|
| ['Abakumova Alexandra'] | ['77016789065'] | ['abakumova_sasha@mail.ru']      | 08.09.2023  |                | c5c981c3f048f49341bd7121b5880edae18036db06f8fd89ad93b842 |
| ['Abdikarim']           | ['77779064466'] | ['ibrasheva_akbike@mail.ru']     | 29.03.2023  |                | a71d38b62ff9b56f7e6dc1f91d2aa57087e481ac15dbbff41fc6ac36 |
| ['Adiya']               | ['77073884864'] | ['rahimovaadia1@gmail.com']      | 27.11.2025  |                | 19b8b050c7a7d9e33f0ab02b91a493a63915fe5d89815ba5fabc7403 |
| ['Aibolat']             | ['77753603673'] | ['aibolat.kulatay@gmail.com']    | 16.09.2023  |                | 1223dc666497f9eb344f6985b82fcd9ee5556625b5278d66cba31716 |
| ['Aida Azhikhan']       | ['77768886488'] | ['azhikhan.ayda@mail.ru']        | 10.03.2024  |                | 7aaee4edd9156b921c77070b52759da962d45d8b01c580a7a5420560 |
| ['Aigerim']             | ['77017547545'] | ['aizhaks@gmail.com']            | 07.02.2025  |                | e977a48e523447c0c95b673c1085f762fea215b492d759e41dadbd93 |
| ['Aigerim']             | ['77472947399'] | ['kenesbekovaai@mail.ru']        | 06.03.2024  |                | 250ad0efff6209286c7d6f523e4b2f302fb7df6db7477be648278746 |
| ['Aigerim Kulshygash']  | ['77718943959'] | ['ajgerimkulsygas758@gmail.com'] | 17.01.2024  |                | 6c136bb34bcf29f94c260bfb4fe35b7a8cca5a37542b8f71261050b4 |
| ['Aigul']               | ['77777834621'] | ['aigul_aaa77@mail.ru']          | 17.10.2024  |                | f68f3810ae8d236015020bb1ea4c60eea17527accc2df7ac29a153d9 |
| ['Aiman']               | ['77013098033'] | ['shugyla.tolenova@bk.ru']       | 01.10.2026  |                | 35efc61a7fd2ed2f0c6ea09ca9f61710a991e73fe74ec5192464dc04 |
| ['Aina Aknazarova']     | ['77014662231'] | ['gulaina.aidun@yahoo.com']      | 06.04.2024  |                | 4a0626147ae6bb042d64fc17fd3fbea47b94ecf087f4a7c2e3f69620 |
| ['Ainur Baimeshova']    | ['77472208374'] | ['ainurbaimeshova@gmail.com']    | 13.10.2023  |                | 6fc8ad41e3a7dc7875985626ea0cc67a211bb37f8432169851d17e48 |
| ['Aiym']                |                 | ['aiym.doss@mail.ru']            | 03.12.2025  |                | f96f948d4e7af7d7c07a210d1e65c77c29f1158b50429e058e4ced16 |
| ['Akaisha']             | ['77781888808'] | ['airisbekova@bk.ru']            | 04.09.2023  |                | 3d6e2c3ae8835cc5eda9af5782446fb0909817ba1749bd40de29f256 |
| ['Akmaral']             | ['77750007991'] | ['akonya21@gmail.com']           | 26.08.2023  |                | a7ac5e1de69408f15301f32205a2dbd7f781982cccaaa5c24e8f603c |
| ['Akylbej']             | ['77758833003'] | ['akilbek_pr@mail.ru']           | 24.03.2023  |                | ffb0e9018988c80554f49fd8fa675fb4cf2dc375fc970ab0381bb52e |
| ['Albina']              | ['77056588959'] | ['albina030409@icloud.com']      | 20.11.2025  |                | f127234a0cb1dc0df37088913d830372c67750eadebed42a22b96b83 |
| ['Albina']              | ['77006302300'] | ['kydyrali00@bk.ru']             | 21.11.2024  |                | 67a7a93cf26619c0640395addd1d2a56d830c4021252e0a76a6104ca |
| ['Aleksandra Zhulina']  | ['77778691944'] | ['alexazum14@gmail.com']         | 09.11.2025  |                | cf15d06d3c867f3df08034a424da01a403f482a3099597afe98e9af0 |
| ['Alexandra Koshman']   |                 | ['alexandra.koshman1@gmail.com'] | 05.06.2026  |                | 782d440e2f68c14019ea21fe18bb35411194eb8899503f1a8ff58e0c |
```
