# Parsetron results

## About row data

> - Code name: index_0037
> - File path: profiles.csv
> - Total rows: 7840297

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- user_id: integer (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- email: string (nullable = true)
 |-- created_at: timestamp (nullable = true)
 |-- updated_at: timestamp (nullable = true)

```

### Data sample
```
|   id |   user_id | first_name     | last_name   | middle_name   |        phone | email                        | created_at          | updated_at          |
|-----:|----------:|:---------------|:------------|:--------------|-------------:|:-----------------------------|:--------------------|:--------------------|
|    1 |         1 | Стефан         | Овчинников  | Борисович     | +72604760062 | super-admin@auchan-ecom.ru   | 2020-04-13 21:12:12 | 2020-04-13 21:12:12 |
|    2 |         2 | Тит            | Мишин       | Максимович    | +73362217443 | admin@auchan-ecom.ru         | 2020-04-13 21:12:12 | 2020-04-13 21:12:12 |
|    3 |         4 | Покупатель     | Покупатель  | Покупатель    | +79111111112 | customer@test.ru             | 2020-04-17 21:35:10 | 2020-04-17 21:35:10 |
|    4 |         5 | Покупатель     | Покупатель  | Покупатель    | +79777777777 | customer2@test.ru            | 2020-04-20 10:02:32 | 2020-04-20 10:02:32 |
|    9 |        12 | Тест           | Тестовый    | Тестович      | +79999999999 | testshop@auchan-ecom.ru      | 2020-04-22 21:33:16 | 2020-04-22 21:33:16 |
|   35 |        45 | Тест           | Тест        | NULL          |      +978712 | maxxique@gmail.com           | 2020-05-07 09:35:29 | 2021-02-13 04:38:22 |
|   36 |        46 | Татьяна        | Елина       | NULL          | +79032065090 | t.elina@auchan.ru            | 2020-05-07 10:40:03 | 2022-07-23 19:41:52 |
|   37 |        47 | Павел          | Ситкин      | NULL          | +79261814486 | one.dev.null@gmail.com       | 2020-05-07 11:36:55 | 2020-05-07 11:36:55 |
|   45 |        60 | Михаил         | Новоселов   | NULL          | +79636214745 | m.novoselov@auchan.ru        | 2020-05-07 19:50:00 | 2021-02-13 04:38:22 |
|   46 |        61 | Собака сутулая | Собакевич   | NULL          | +79211627025 | tplmxmbsmruceltjup@awdrt.org | 2020-05-08 09:47:34 | 2020-05-08 09:47:34 |
|   52 |        67 | Сергей         | Порохня     | NULL          | +79037865579 | sergporohnya@yandex.ru       | 2020-05-08 13:54:12 | 2021-02-13 04:38:22 |
|   53 |        68 | Мария          | Созонтова   | NULL          | +79998264347 | mashagalka@yandex.ru         | 2020-05-08 14:38:36 | 2021-09-08 18:31:44 |
|   54 |        69 | Илья           | Васильев    | NULL          | +79859588800 | ilushka911@inbox.ru          | 2020-05-08 14:57:51 | 2020-05-08 14:57:51 |
|   60 |        75 | Наталья        | Рычкова     | NULL          | +79036651306 | Na.rychkova@auchan.ru        | 2020-05-08 16:42:55 | 2020-05-08 16:42:55 |
|   61 |        76 | Никита         | Ящук        | NULL          | +79175520880 | nikyashchuk@mail.ru          | 2020-05-08 16:49:00 | 2020-05-08 16:49:00 |
|   62 |        77 | Николай        | Марков      | NULL          | +79260440504 | n.markov@auchan.ru           | 2020-05-08 17:21:05 | 2022-08-11 13:29:07 |
|   63 |        78 | Екатерина      | Маркова     | NULL          | +79160731338 | ek.markova@auchan.ru         | 2020-05-08 17:36:42 | 2021-03-25 12:16:13 |
|   64 |        79 | Катя           | Лысенко     | NULL          | +79686641811 | eka.lysenko@auchan.ru        | 2020-05-08 17:42:46 | 2021-05-12 17:28:10 |
|   65 |        80 | Александра     | Гагарина    | Гагарина      | +79106983514 | sasha.gagarina94@mail.ru     | 2020-05-08 18:14:09 | 2021-06-04 19:41:55 |
|   66 |        81 | Анна           | Щетина      | NULL          | +79035595824 | shchetina@mail.ru            | 2020-05-08 20:16:02 | 2020-05-08 20:16:02 |
```

> - Code name: index_0037
> - File path: customers.csv
> - Total rows: 7856407

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- user_id: integer (nullable = true)
 |-- status: integer (nullable = true)
 |-- comment_internal: string (nullable = true)
 |-- manager_id: string (nullable = true)
 |-- avatar: string (nullable = true)
 |-- birthday: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- created_at: timestamp (nullable = true)
 |-- updated_at: timestamp (nullable = true)
 |-- comment_status: string (nullable = true)
 |-- referrer_id: string (nullable = true)
 |-- referral_code: string (nullable = true)
 |-- referral_code_default: string (nullable = true)
 |-- referral_level_id: string (nullable = true)
 |-- legal_info_company_name: string (nullable = true)
 |-- legal_info_company_address: string (nullable = true)
 |-- legal_info_inn: string (nullable = true)
 |-- legal_info_payment_account: string (nullable = true)
 |-- legal_info_bik: string (nullable = true)
 |-- legal_info_bank: string (nullable = true)
 |-- legal_info_bank_correspondent_account: string (nullable = true)
 |-- promo_page_name: string (nullable = true)
 |-- referral_bill: string (nullable = true)
 |-- city: string (nullable = true)
 |-- current_merchant_id: string (nullable = true)
 |-- is_adult: integer (nullable = true)
 |-- current_delivery_method: string (nullable = true)
 |-- in_loyalty: integer (nullable = true)
 |-- loyalty_number: string (nullable = true)

```

### Data sample
```
|   id |   user_id |   status | comment_internal   | manager_id   | avatar   | birthday   | gender   | created_at          | updated_at          | comment_status   | referrer_id   | referral_code   | referral_code_default   | referral_level_id   | legal_info_company_name   | legal_info_company_address   | legal_info_inn   | legal_info_payment_account   | legal_info_bik   | legal_info_bank   | legal_info_bank_correspondent_account   | promo_page_name   | referral_bill   | city   |   current_merchant_id |   is_adult | current_delivery_method   |   in_loyalty | loyalty_number   |
|-----:|----------:|---------:|:-------------------|:-------------|:---------|:-----------|:---------|:--------------------|:--------------------|:-----------------|:--------------|:----------------|:------------------------|:--------------------|:--------------------------|:-----------------------------|:-----------------|:-----------------------------|:-----------------|:------------------|:----------------------------------------|:------------------|:----------------|:-------|----------------------:|-----------:|:--------------------------|-------------:|:-----------------|
|    1 |         5 |        5 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-04-20 10:02:33 | 2020-04-20 10:02:33 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | NULL                      |            0 | NULL             |
|    2 |         7 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-04-21 18:27:35 | 2020-04-21 18:27:35 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | NULL                      |            0 | NULL             |
|    5 |        14 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-04-23 11:09:49 | 2020-04-23 11:09:49 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | NULL                      |            0 | NULL             |
|    9 |        24 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-04-29 21:13:20 | 2020-04-29 21:13:20 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | NULL                      |            0 | NULL             |
|   29 |        45 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-07 09:35:29 | 2020-08-07 15:53:37 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | NULL                      |            0 | NULL             |
|   30 |        46 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-07 10:40:03 | 2023-05-17 14:06:12 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | 2                         |            1 | 2010000000557    |
|   31 |        47 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-07 11:36:55 | 2023-04-22 12:41:00 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    23 |          0 | 1                         |            0 | NULL             |
|   39 |        60 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-07 19:50:00 | 2022-06-27 09:43:58 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    14 |          0 | 2                         |            0 | NULL             |
|   40 |        61 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 09:47:34 | 2020-05-08 09:47:34 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | NULL                      |            0 | NULL             |
|   46 |        67 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 13:54:13 | 2020-05-08 13:54:13 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | NULL                      |            0 | NULL             |
|   47 |        68 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 14:38:36 | 2022-11-11 14:41:04 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    23 |          0 | 2                         |            0 | NULL             |
|   48 |        69 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 14:57:52 | 2020-05-08 14:57:52 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | NULL                      |            0 | NULL             |
|   54 |        75 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 16:42:56 | 2021-01-10 10:08:43 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | 1                         |            0 | NULL             |
|   55 |        76 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 16:49:00 | 2020-05-08 16:49:00 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | NULL                      |            0 | NULL             |
|   56 |        77 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 17:21:05 | 2023-05-06 09:39:30 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                     2 |          0 | 2                         |            1 | 2020000101581    |
|   57 |        78 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 17:36:42 | 2021-04-30 16:05:36 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    12 |          0 | 1                         |            0 | NULL             |
|   58 |        79 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 17:42:46 | 2023-02-04 13:06:15 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                     8 |          0 | 2                         |            0 | NULL             |
|   59 |        80 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 18:14:09 | 2022-09-20 11:57:12 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    24 |          0 | 2                         |            1 | NULL             |
|   60 |        81 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-08 20:16:02 | 2023-03-16 09:40:54 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    22 |          0 | 1                         |            0 | 2020017893707    |
|   61 |        82 |        1 | NULL               | NULL         | NULL     | NULL       | NULL     | 2020-05-09 08:05:53 | 2022-09-01 17:44:10 | NULL             | NULL          | NULL            | NULL                    | NULL                | NULL                      | NULL                         | NULL             | NULL                         | NULL             | NULL              | NULL                                    | NULL              | NULL            | NULL   |                    94 |          0 | 1                         |            0 | NULL             |
```

> - Code name: index_0037
> - File path: customer_addresses.csv
> - Total rows: 1234642

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- customer_id: integer (nullable = true)
 |-- created_at: timestamp (nullable = true)
 |-- updated_at: timestamp (nullable = true)
 |-- address: string (nullable = true)
 |-- default: integer (nullable = true)

```

### Data sample
```
|   id |   customer_id | created_at          | updated_at          | address                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |   default |
|-----:|--------------:|:--------------------|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------:|
| 5011 |            29 | 2020-05-10 15:08:36 | 2020-08-07 16:59:10 | {"area": "", "city": "г Балашиха", "flat": "", "block": "", "floor": "", "house": "д 22", "porch": "", "region": "Московская обл", "street": "ул Черняховского", "comment": "", "geo_lat": "55.7618385", "geo_lon": "37.9342178", "intercom": "", "area_guid": "", "city_guid": "27c5bc66-61bf-4a17-b0cd-ca0eb64192d6", "post_index": "143930", "region_guid": "29251dcf-00a1-4e34-98d4-5c47484a36d4", "country_code": "RU", "address_string": "Московская обл, г Балашиха, мкр Салтыковка, ул Черняховского, д 22"}                                              |         1 |
| 5071 |           303 | 2020-05-15 08:49:39 | 2020-05-19 19:39:17 | {"area": "", "city": "г Москва", "flat": "", "block": "", "floor": "", "house": "д 10", "porch": "", "region": "г Москва", "street": "ул Красносельская Верхн.", "comment": "", "geo_lat": "55.7841365", "geo_lon": "37.6610439", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "107140", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Красносельская Верхн., д 10, кв 117"}                                                                |         1 |
| 5090 |            57 | 2020-05-16 18:33:12 | 2021-05-11 16:44:12 | {"area": "", "city": "Москва", "flat": "", "block": "", "floor": "", "house": "3А", "porch": "", "region": "Москва", "street": "Верхняя Красносельская", "comment": "", "geo_lat": "55.78567", "geo_lon": "37.66531", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Верхняя Красносельская, д 3А"}                                                                                         |         1 |
| 5101 |           518 | 2020-05-17 10:11:13 | 2023-05-04 09:12:31 | {"area": "", "city": "г Москва", "flat": "82", "block": "", "floor": "12", "house": "д 4", "porch": "1", "region": "г Москва", "street": "ул Гастелло", "comment": "", "geo_lat": "55.78654", "geo_lon": "37.68149", "intercom": "82", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "107014", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Гастелло, д 4"}                                                                                                 |         1 |
| 5107 |           543 | 2020-05-17 14:51:25 | 2020-06-30 19:20:28 | {"area": "", "city": "г Москва", "flat": "", "block": "к 1", "floor": "", "house": "д 3", "porch": "", "region": "г Москва", "street": "ул Рябиновая", "comment": "", "geo_lat": "", "geo_lon": "", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "121471", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Рябиновая, д 3"}                                                                                                                   |         1 |
| 5158 |           568 | 2020-05-17 19:32:42 | 2020-06-30 19:20:28 | {"area": "", "city": "г Москва", "flat": "", "block": "к 1", "floor": "", "house": "д 32/36", "porch": "", "region": "г Москва", "street": "ул Бакунинская", "comment": "", "geo_lat": "55.7752445", "geo_lon": "37.686286", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "105082", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Бакунинская, д 32/36"}                                                                                    |         1 |
| 5203 |            74 | 2020-05-19 09:57:06 | 2020-12-15 16:30:18 | {"area": "", "city": "г Москва", "flat": "", "block": "", "floor": "", "house": "д 5", "porch": "", "region": "г Москва", "street": "ул Красносельская Нижн.", "comment": "", "geo_lat": "", "geo_lon": "", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Красносельская Нижн., д 5"}                                                                                                      |         1 |
| 5217 |           333 | 2020-05-19 18:25:57 | 2020-08-22 12:42:44 | {"area": "", "city": "г Москва", "flat": "", "block": "стр 6", "floor": "", "house": "д 11А", "porch": "", "region": "г Москва", "street": "ул Красносельская Верхн.", "comment": "", "geo_lat": "55.78434", "geo_lon": "37.66179", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "107140", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Красносельская Верхн., д 11А стр 6"}                                                               |         1 |
| 5223 |           702 | 2020-05-19 22:54:08 | 2020-08-19 00:00:21 | {"area": "", "city": "г Москва", "flat": "", "block": "", "floor": "", "house": "д 55", "porch": "", "region": "г Москва", "street": "ул Трифоновская", "comment": "", "geo_lat": "55.7895586", "geo_lon": "37.6302962", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "129272", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Трифоновская, д 55, кв 32"}                                                                                   |         1 |
| 5253 |           405 | 2020-05-21 10:39:57 | 2022-09-12 20:56:23 | {"area": "", "city": "Москва", "flat": "", "block": "", "floor": "", "house": "6", "porch": "", "region": "Москва", "street": "Тайнинская", "comment": "", "geo_lat": "55.87799", "geo_lon": "37.68286", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Тайнинская, д 6"}                                                                                                                   |         1 |
| 5254 |           790 | 2020-05-21 11:05:32 | 2023-02-18 19:20:15 | {"area": "", "city": "г Москва", "flat": "384", "block": "к 2", "floor": "12", "house": "д 8", "porch": "7", "region": "г Москва", "street": "ул Верхняя Красносельская", "comment": "", "geo_lat": "55.78398", "geo_lon": "37.659084", "intercom": "384к1414", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "107140", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Верхняя Красносельская, д 8 к 2, кв 384"}                                              |         1 |
| 5261 |           772 | 2020-05-21 15:01:43 | 2020-06-30 19:20:30 | {"area": "", "city": "г Москва", "flat": "", "block": "", "floor": "", "house": "д 3", "porch": "", "region": "г Москва", "street": "ул Годовикова", "comment": "", "geo_lat": "", "geo_lon": "", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "129085", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Годовикова, д 3"}                                                                                                                    |         1 |
| 5267 |           826 | 2020-05-21 19:20:02 | 2022-03-07 14:45:31 | {"area": "Сосенское", "city": "Москва", "flat": "", "block": "2", "floor": "", "house": "92", "porch": "", "region": "Москва", "street": "Александры Монаховой", "comment": "", "geo_lat": "55.54267", "geo_lon": "37.48662", "intercom": "", "area_guid": "90648b5c-d6e7-4bb0-9782-7908808325cf", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, поселение Сосенское, ул Александры Монаховой, д 92 к 2"}                      |         1 |
| 5269 |           833 | 2020-05-21 21:17:43 | 2021-04-04 16:03:40 | {"area": "", "city": "г Красногорск", "flat": "", "block": "", "floor": "", "house": "д 3", "porch": "", "region": "Московская обл", "street": "ул Пришвина", "comment": "", "geo_lat": "55.813597", "geo_lon": "37.245319", "intercom": "", "area_guid": "", "city_guid": "63fcf18a-365e-451f-baee-8d09ac50b773", "post_index": "143444", "region_guid": "29251dcf-00a1-4e34-98d4-5c47484a36d4", "country_code": "RU", "address_string": "Московская обл, г Красногорск, мкр Опалиха, ул Пришвина, д 3"}                                                         |         1 |
| 5275 |           846 | 2020-05-22 09:41:56 | 2020-06-30 19:20:31 | {"area": "", "city": "г Москва", "flat": "", "block": "", "floor": "", "house": "д 61", "porch": "", "region": "г Москва", "street": "ул Красных Зорь", "comment": "", "geo_lat": "55.7247622", "geo_lon": "37.4269169", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "121471", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Красных Зорь, д 61"}                                                                                          |         1 |
| 5297 |           911 | 2020-05-23 13:48:25 | 2022-09-09 15:16:26 | {"area": "", "city": "г Москва", "flat": "9", "block": "", "floor": "4", "house": "д 49", "porch": "1", "region": "г Москва", "street": "ул Трифоновская", "comment": "", "geo_lat": "55.789082", "geo_lon": "37.627795", "intercom": "4798", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "129272", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Трифоновская, д 49"}                                                                                     |         1 |
| 5314 |           606 | 2020-05-24 14:14:38 | 2023-05-01 15:17:39 | {"area": "г Одинцово", "city": "г Одинцово", "flat": "", "block": "", "floor": "", "house": "д 53А", "porch": "", "region": "Московская обл", "street": "", "comment": "", "geo_lat": "55.7056", "geo_lon": "37.38634", "intercom": "", "area_guid": "6ae8ad9e-aa6c-4849-92d8-8e637059c9b0", "city_guid": "6ae8ad9e-aa6c-4849-92d8-8e637059c9b0", "post_index": "143026", "region_guid": "29251dcf-00a1-4e34-98d4-5c47484a36d4", "country_code": "RU", "address_string": "Московская обл, г Одинцово, деревня Марфино, д 53А"}                                    |         1 |
| 5318 |           966 | 2020-05-24 17:28:38 | 2023-02-04 11:55:48 | {"area": "", "city": "г Москва", "flat": "", "block": "", "floor": "", "house": "д 10", "porch": "", "region": "г Москва", "street": "ул Сокольническая Слободка", "comment": "", "geo_lat": "", "geo_lon": "", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "107113", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Сокольническая Слободка, д 10"}                                                                                        |         1 |
| 5320 |           967 | 2020-05-24 17:32:23 | 2021-04-11 18:42:15 | {"area": "г Одинцово", "city": "г Одинцово", "flat": "", "block": "", "floor": "", "house": "д 52", "porch": "", "region": "Московская обл", "street": "Можайское шоссе", "comment": "", "geo_lat": "55.711939", "geo_lon": "37.375926", "intercom": "", "area_guid": "6ae8ad9e-aa6c-4849-92d8-8e637059c9b0", "city_guid": "6ae8ad9e-aa6c-4849-92d8-8e637059c9b0", "post_index": "143026", "region_guid": "29251dcf-00a1-4e34-98d4-5c47484a36d4", "country_code": "RU", "address_string": "Московская обл, г Одинцово, рп Новоивановское, Можайское шоссе, д 52"} |         1 |
| 5328 |           191 | 2020-05-25 09:46:48 | 2020-08-18 13:46:30 | {"area": "", "city": "г Москва", "flat": "", "block": "", "floor": "", "house": "д 1", "porch": "", "region": "г Москва", "street": "ул Арбат", "comment": "", "geo_lat": "55.751812", "geo_lon": "37.599292", "intercom": "", "area_guid": "", "city_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "post_index": "119019", "region_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5", "country_code": "RU", "address_string": "г Москва, ул Арбат, д 1"}                                                                                                            |         1 |
```


## About final data
> - Total rows: 121242

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- client_card_number: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 86.67% |
| Phones | 99.84% |
| Sex | 0.00% |
| Birth_date | 0.00% |
| Address | 20.57% |
| Accounts | 100.00% |
| Actuality | 100.00% |



### Data sample
```
| names                               | emails                          | phones          |   sex | birth_date   | address                                                                | accounts                                                                                            | actuality   |
|:------------------------------------|:--------------------------------|:----------------|------:|:-------------|:-----------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|:------------|
| ['Павловна Оболенская Оболенская']  | ['vera061957@yandex.ru']        | ['79057716702'] |   nan |              |                                                                        |                                                                                                     | 12.02.2021  |
| ['Сергеевна Дарья Гончаренко']      | ['alice.gerl15@gmail.com']      | ['79872490308'] |   nan |              |                                                                        |                                                                                                     | 12.02.2021  |
| ['Борисович Стефан Овчинников']     | ['super-admin@auchan-ecom.ru']  |                 |   nan |              |                                                                        |                                                                                                     | 13.04.2020  |
| ['Александровна Анастасия Маркова'] | ['markova-spb@list.ru']         | ['79266386711'] |   nan |              |                                                                        |                                                                                                     | 12.02.2021  |
| ['Минигалеевич Дмитрий Сафиуллин']  | ['dmitrijsafiullin8@gmail.com'] | ['79174419025'] |   nan |              |                                                                        |                                                                                                     | 12.02.2021  |
| ['Максимович Тит Мишин']            | ['admin@auchan-ecom.ru']        |                 |   nan |              |                                                                        |                                                                                                     | 13.04.2020  |
| ['Игоревич Сергей Однодворцев']     | ['cybarco@bk.ru']               | ['79129813744'] |   nan |              |                                                                        | [Row(title='Ашан', link='https://www.auchan.ru', id='1002990', client_card_number=None)]            | 13.10.2022  |
| ['Евгеньевич Игорь Мельник']        | ['igormelnike@gmail.com']       | ['79999939412'] |   nan |              |                                                                        | [Row(title='Ашан', link='https://www.auchan.ru', id='1003320', client_card_number=None)]            | 29.06.2021  |
| ['Юлия Юлия Митина']                |                                 | ['79085507261'] |   nan |              |                                                                        | [Row(title='Ашан', link='https://www.auchan.ru', id='1007340', client_card_number=None)]            | 05.09.2022  |
| ['Дмитриевна Галина Логашина']      | ['gala27147@gmail.com']         | ['79262347524'] |   nan |              | ['г Москва пер Басманный 1-й д 520 стр 2']                             | [Row(title='Ашан', link='https://www.auchan.ru', id='1008', client_card_number=None)]               | 13.02.2021  |
| ['Рахматуловна Роза Мурзина']       | ['r9090885936@gmail.com']       | ['79823448167'] |   nan |              |                                                                        | [Row(title='Ашан', link='https://www.auchan.ru', id='1008238', client_card_number='2010006716025')] | 22.10.2022  |
| ['Владимирович Игорь Павлов']       | ['igorpl69@yandex.ru']          | ['79997350196'] |   nan |              |                                                                        | [Row(title='Ашан', link='https://www.auchan.ru', id='1008343', client_card_number=None)]            | 30.07.2021  |
| ['Анатольевна Любовь Белокопытова'] | ['alopecurus72@rambler.ru']     | ['79651843101'] |   nan |              |                                                                        | [Row(title='Ашан', link='https://www.auchan.ru', id='1008646', client_card_number=None)]            | 26.07.2021  |
| ['Юрьевич Михаил Павленко']         | ['torg.krasnodar@gmail.com']    | ['79184406606'] |   nan |              |                                                                        | [Row(title='Ашан', link='https://www.auchan.ru', id='1010621', client_card_number=None)]            | 20.03.2022  |
| ['Сергеевна Арина Андриевская']     | ['andrievskaya1414@gmail.com']  | ['79023087547'] |   nan |              | ['Нижегородская обл Кстовский р-н деревня Анкудиновка ул Русская д 5'] | [Row(title='Ашан', link='https://www.auchan.ru', id='1010946', client_card_number=None)]            | 06.08.2021  |
| ['Голомозюк Татьяна Голомозюк']     | ['golomozyuktp@gmail.com']      | ['79290409940'] |   nan |              |                                                                        | [Row(title='Ашан', link='https://www.auchan.ru', id='1011392', client_card_number=None)]            | 26.02.2021  |
| ['Сергеевна Алиса Макаренко']       |                                 | ['79523318170'] |   nan |              |                                                                        | [Row(title='Ашан', link='https://www.auchan.ru', id='1011940', client_card_number=None)]            | 09.07.2022  |
| ['Давыдович Борис Давидович']       | ['davi.boris1945@gmail.com']    | ['79276923051'] |   nan |              | ['г Самара ул Степана Разина д 44 кв 19']                              | [Row(title='Ашан', link='https://www.auchan.ru', id='1015245', client_card_number='2010030938394')] | 26.05.2022  |
| ['Александровна Анна Хоптинская']   | ['anna_dorofeeva@bk.ru']        | ['79262496847'] |   nan |              | ['г Москва ул Воронцовские Пруды д 7']                                 | [Row(title='Ашан', link='https://www.auchan.ru', id='1016862', client_card_number=None)]            | 06.05.2022  |
| ['Андреевич Павел Грюкалов']        | ['pavel.zmey.1977@yandex.ru']   | ['79518524839'] |   nan |              |                                                                        | [Row(title='Ашан', link='https://www.auchan.ru', id='1018009', client_card_number=None)]            | 11.04.2022  |
```