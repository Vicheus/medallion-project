# Parsetron results

## About row data

> - File path: contact_emails_preprocessed.csv
> - Total rows: 87178

### Schema
```
root
 |-- email: string (nullable = true)
 |-- contact_id: integer (nullable = true)

```

### Data sample
```
| email                          |   contact_id |
|:-------------------------------|-------------:|
| katrin_o@mail.ru               |            2 |
| kaluzhnaja.ekaterina@otr.ru    |            3 |
| kat6ka@yandex.ru               |            4 |
| ali-potapova@yandex.ru         |            5 |
| rozzi70@mail.ru                |            6 |
| katrinn171@list.ru             |            7 |
| taneksh@rambler.ru             |            8 |
| my2shy@mail.ru                 |            9 |
| nyh2006@yandex.ru              |           10 |
| alev965n@yandex.ru             |           11 |
| elena_11074@mail.ru            |           12 |
| barykina@bank.rs.ru            |           13 |
| als69@yandex.ru                |           14 |
| als19692008@rambler.ru         |           15 |
| pakostnitza@gmail.com          |           16 |
| onabynarada@gmail.com          |           17 |
| karpovaai@gmail.com            |           18 |
| dina.bolshakova@missioneco.org |           19 |
| bin21@mail.ru                  |           20 |
| romantika79@rambler.ru         |           21 |
```

> - File path: registered_contact_emails_names_from_messages_preprocessed.csv
> - Total rows: 35539

### Schema
```
root
 |-- email: string (nullable = true)
 |-- name: string (nullable = true)
 |-- contact_id: integer (nullable = true)

```

### Data sample
```
| email                      | name                          |   contact_id |
|:---------------------------|:------------------------------|-------------:|
| ok@trestgm.ru              | ok                            |        67836 |
| olesik_v@mail.ru           | Гоголева Олеся Владимировна   |        67842 |
| elen-alekc@yandex.ru       | elen-alekc                    |        67833 |
| olichka1987@meta.ua        | olichka1987                   |        67829 |
| lyba591@yandex.ru          | lyba591                       |        67799 |
| Ilona_gavrilenko@mail.ru   | Гавриленко Илона Владимировна |        67823 |
| yulya.t.1978@mail.ru       | Трухина Юлия Александровна    |        67764 |
| nadezhda231096@mail.ru     | Маркова Надежда Михайловна    |        67765 |
| mammaeva_9607@mail.ru      | mammaeva_9607                 |        67756 |
| ya.aleshinaelena@yandex.ru | ya.aleshinaelena              |        67748 |
| Nati-00@mail.ru            | Бойко Наталия Сергеевна       |        67729 |
| cargo.exp@bk.ru            | cargo.exp                     |        67743 |
| vsenn@mail.ru              | В Наталья Н                   |        67648 |
| Bobrink@yandex.ru          | Bobrink                       |        67671 |
| viktorirazin@mail.ru       | Разина Виктори Анатольевна    |        67621 |
| reymichel1@centurylink.net | reymichel1                    |        67587 |
| badyvrana@mail.ru          | Бады Урана Шоомбуловна        |        67616 |
| ogtix@mail.ru              | ogtix                         |        67572 |
| mitinatania@mail.ru        | mitinatania                   |        67573 |
| Lara0214@yandex.ru         | Пилецкая Лариса Владимировна  |        67536 |
```

> - File path: contacts_info_preprocessed.csv
> - Total rows: 89654

### Schema
```
root
 |-- contact_id: string (nullable = true)
 |-- address: string (nullable = true)
 |-- address_city: string (nullable = true)
 |-- address_country: string (nullable = true)
 |-- address_dom: string (nullable = true)
 |-- address_etazh: string (nullable = true)
 |-- address_kvartira: string (nullable = true)
 |-- address_lat: string (nullable = true)
 |-- address_lng: string (nullable = true)
 |-- address_region: string (nullable = true)
 |-- address_street: string (nullable = true)
 |-- address_ulitsa: string (nullable = true)
 |-- address_zip: string (nullable = true)
 |-- create_ip: string (nullable = true)
 |-- create_user_agent: string (nullable = true)
 |-- facebook_id: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- phone_confirmed: string (nullable = true)
 |-- socialnetwork: long (nullable = true)
 |-- vkontakte_id: long (nullable = true)
 |-- yandex_id: long (nullable = true)

```

### Data sample
```
| contact_id                                | address   | address_city   | address_country   |   address_dom |   address_etazh | address_kvartira   |   address_lat | address_lng   |   address_region | address_street                                          | address_ulitsa   |   address_zip | create_ip   | create_user_agent   |     facebook_id | first_name   | phone           | phone_confirmed   |   socialnetwork |   vkontakte_id |   yandex_id |
|:------------------------------------------|:----------|:---------------|:------------------|--------------:|----------------:|:-------------------|--------------:|:--------------|-----------------:|:--------------------------------------------------------|:-----------------|--------------:|:------------|:--------------------|----------------:|:-------------|:----------------|:------------------|----------------:|---------------:|------------:|
| 1                                         |           | Москва         | rus               |               |                 |                    |               |               |               77 | пр-кт Андропова, д 22                                   |                  |        115533 |             |                     | 984584764933704 |              | 79037241370     |                   |             nan |            nan |         nan |
| 2                                         |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 9265755187      |                   |             nan |            nan |         nan |
| 3                                         |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 9265755187      |                   |             nan |            nan |         nan |
| 4                                         |           |                |                   |               |                 |                    |               |               |                  | Дмитровское шоссе д.60А                                 |                  |               |             |                     |                 |              |                 |                   |             nan |            nan |         nan |
| (Здание бизнес центра с вывеской ""Плане" |           |                |                   |               |                 |                    |    9265755187 |               |                  |                                                         |                  |               |             |                     |                 |              |                 |                   |             nan |            nan |         nan |
| 5                                         |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 84956549212     |                   |             nan |            nan |         nan |
| 6                                         |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 89263698430     |                   |             nan |            nan |         nan |
| 7                                         |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 89859909383     |                   |             nan |            nan |         nan |
| 8                                         |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 84985532917     |                   |             nan |            nan |         nan |
| 9                                         |           |                |                   |               |                 |                    |               |               |                  | 4-ый Лесной пер., 4, 547 офис, Москва                   |                  |               |             |                     |                 |              | 89067954472     |                   |             nan |            nan |         nan |
| 10                                        |           |                | rus               |               |                 |                    |               |               |               50 | ул.олимпийский проспект д5 стр.1                        |                  |               |             |                     |                 |              | 89261834525     |                   |             nan |            nan |         nan |
| 11                                        |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 89165780640     |                   |             nan |            nan |         nan |
| 12                                        |           | Москва         | rus               |               |                 |                    |               |               |               77 |                                                         |                  |        117638 |             |                     |                 |              | 89035001934     |                   |             nan |            nan |         nan |
| 13                                        |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 89263252524     |                   |             nan |            nan |         nan |
| 14                                        |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 9168003660      |                   |             nan |            nan |         nan |
| 15                                        |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 9168003660      |                   |             nan |            nan |         nan |
| 16                                        |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 4996176987      |                   |             nan |            nan |         nan |
| 17                                        |           | Москва г       | rus               |            45 |               1 |                    |               |               |               50 | ул. Судостроительная, дом 45, кв. 39, код 39 ключ 9301. | Судостроительная |        115407 |             |                     |                 |              | 89031247409     |                   |             nan |            nan |         nan |
| 18                                        |           |                |                   |               |                 |                    |               |               |                  |                                                         |                  |               |             |                     |                 |              | 89031247409     |                   |             nan |            nan |         nan |
| 19                                        |           |                |                   |               |                 |                    |               |               |                  | РФ.Москва. ул Большая Якиманка. дом 45                  |                  |               |             |                     |                 |              | 8.903.100.60.94 |                   |             nan |            nan |         nan |
```

> - File path: contacts1_preprocessed.csv
> - Total rows: 19

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- firstname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- title: string (nullable = true)
 |-- company: string (nullable = true)
 |-- jobtitle: string (nullable = true)
 |-- company_contact_id: integer (nullable = true)
 |-- is_company: integer (nullable = true)
 |-- is_user: integer (nullable = true)
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)
 |-- last_datetime: timestamp (nullable = true)
 |-- sex: string (nullable = true)
 |-- about: string (nullable = true)
 |-- photo: integer (nullable = true)
 |-- create_datetime: timestamp (nullable = true)
 |-- create_app_id: string (nullable = true)
 |-- create_method: string (nullable = true)
 |-- create_contact_id: integer (nullable = true)
 |-- locale: string (nullable = true)
 |-- timezone: string (nullable = true)
 |-- birth_day: integer (nullable = true)
 |-- birth_month: integer (nullable = true)
 |-- birth_year: integer (nullable = true)

```

### Data sample
```
|    id | name                           | firstname   | middlename   | lastname    | title   | company   | jobtitle   |   company_contact_id |   is_company |   is_user | login   | password                         | last_datetime       | sex   | about   |      photo | create_datetime     | create_app_id   | create_method   |   create_contact_id | locale   | timezone   |   birth_day |   birth_month |   birth_year |
|------:|:-------------------------------|:------------|:-------------|:------------|:--------|:----------|:-----------|---------------------:|-------------:|----------:|:--------|:---------------------------------|:--------------------|:------|:--------|-----------:|:--------------------|:----------------|:----------------|--------------------:|:---------|:-----------|------------:|--------------:|-------------:|
|  2335 | Драчева Алина                  | Алина       |              | Драчева     |         |           |            |                    0 |            0 |         0 |         | 337acb44118dce66c45b211547c7d40f | 2016-07-23 10:55:20 |       |         |          0 | 2009-07-05 21:25:43 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|  2971 | 2971                           |             |              |             |         |           |            |                    0 |            0 |         0 |         | a28b775d99cf6bafad2e0470649e51cf | 2020-11-15 17:28:28 |       |         |          0 | 2009-09-09 23:02:47 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|  8757 | Чернова Ирина Васильевна       | Ирина       | Васильевна   | Чернова     |         |           |            |                    0 |            0 |         0 |         | c77ddd50be4d5088c4ac2384c152e7e1 | 2020-11-05 19:09:57 |       |         |          0 | 2011-03-27 22:02:39 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
| 15550 | Зайцева Юлия                   | Юлия        |              | Зайцева     |         |           |            |                    0 |            0 |         0 |         | 21b95a0f90138767b0fd324e6be3457b | NaT                 |       |         |          0 | 2012-11-14 19:54:05 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
| 16536 | Orlova Julia                   | Julia       |              | Orlova      |         |           |            |                    0 |            0 |         0 |         |                                  | NaT                 |       |         |          0 | 2013-01-20 17:21:31 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
| 19340 | Зайцева Юлия                   | Юлия        |              | Зайцева     |         |           |            |                    0 |            0 |         0 |         |                                  | NaT                 |       |         |          0 | 2013-09-13 19:38:03 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
| 24682 | Ирина                          | Ирина       |              |             |         |           |            |                    0 |            0 |         0 |         |                                  | NaT                 |       |         |          0 | 2014-12-29 13:16:04 | shop            |                 |                   0 |          |            |         nan |           nan |          nan |
| 27590 | Иващенко Елизавета             | Елизавета   |              | Иващенко    |         |           |            |                    0 |            0 |         0 |         | 8df0ed56b9ce7305c4b240ce0f4e2cf6 | NaT                 |       |         |          0 | 2015-07-13 12:52:06 | shop            |                 |                   0 |          |            |           4 |             5 |         1988 |
| 35406 | Кузнецов Сергей Владимирович   | Сергей      | Владимирович | Кузнецов    |         |           |            |                    0 |            0 |         0 |         | 5b9bb6543459b4b4af74a3980494c44a | 2020-06-22 12:41:46 |       |         |          0 | 2016-12-21 17:51:31 | shop            | signup          |                   0 |          |            |         nan |           nan |          nan |
| 38284 | Фомина Оксана Николаевна       | Оксана      | Николаевна   | Фомина      |         |           |            |                    0 |            0 |         0 |         | 79d9b09acc2fafba9ad3841ed23b0ed6 | 2020-06-29 19:31:43 |       |         |          0 | 2017-06-06 12:18:05 | shop            |                 |                   0 |          |            |         nan |           nan |          nan |
| 62561 | Генералов Николай Игоревич     | Николай     | Игоревич     | Генералов   |         |           |            |                    0 |            0 |         0 |         | 8ac87c54738af0cff0b8d1e2b7995f3c | 2019-07-17 16:37:21 | m     |         |          0 | 2019-04-10 19:15:26 | shop            | signup          |                   0 |          |            |         nan |           nan |          nan |
| 42653 | sergo300878                    |             |              |             |         |           |            |                    0 |            0 |         0 |         |                                  | 2017-12-14 21:13:53 |       |         |          0 | 2017-12-14 21:13:53 | mailer          |                 |                   0 |          |            |         nan |           nan |          nan |
| 50946 | 50946                          |             |              |             |         |           |            |                    0 |            0 |         0 |         | 4fee5ee0437353aab609855b4c8b982b | 2020-11-16 17:01:00 |       |         |          0 | 2018-08-07 13:58:29 | shop            |                 |                   0 |          |            |         nan |           nan |          nan |
| 51416 | Вискалов Алексей Алексеевич    | Алексей     | Алексеевич   | Вискалов    |         |           |            |                    0 |            0 |         0 |         | 04ca1d9629b09f97024c028cfa62623d | 2019-07-10 23:01:43 |       |         |          0 | 2018-08-25 13:49:38 | shop            |                 |                   0 |          |            |         nan |           nan |          nan |
| 60122 | Кондратьева Раиса Владимировна | Раиса       | Владимировна | Кондратьева |         |           |            |                    0 |            0 |         0 |         |                                  | 2019-03-04 09:39:23 |       |         |          0 | 2019-03-04 09:39:23 | mailer          |                 |                   0 |          |            |         nan |           nan |          nan |
| 65262 | Клочкова Татьяна Владимировна  | Татьяна     | Владимировна | Клочкова    |         |           |            |                    0 |            0 |         0 |         | 5c8a714ddacf4c829ff05dc7f1bb7946 | 2020-10-30 21:28:09 |       |         |          0 | 2019-09-17 22:52:43 | shop            |                 |                   0 |          |            |         nan |           nan |          nan |
| 69107 | Генералов Николай              | Николай     |              | Генералов   |         |           |            |                    0 |            0 |         0 |         | 5ead9b11fc19e770029f0aaa6fe324c  | 2020-04-11 13:24:57 |       |         | 1128160760 | 2020-04-11 13:05:38 | shop            | facebook        |                   0 |          |            |         nan |           nan |          nan |
| 70855 | Сафиуллина Алия Гумеровна      | Алия        | Гумеровна    | Сафиуллина  |         |           |            |                    0 |            0 |         0 |         | 029afa8b516152fa34f1b2fbe50f1eab | 2020-05-27 14:34:54 |       |         |          0 | 2020-05-27 13:34:51 | shop            |                 |                   0 |          |            |         nan |           nan |          nan |
| 71777 | Генералов Николай              | Николай     |              | Генералов   |         |           |            |                    0 |            0 |         0 |         | 2113945ea87643839eea0b4edcf7303  | 2020-10-12 12:56:55 | m     |         |  548447264 | 2020-07-10 13:27:37 | shop            | vkontakte       |                   0 |          |            |          12 |             8 |         1988 |
```

> - File path: contacts2_preprocessed.csv
> - Total rows: 88822

### Schema
```
root
 |-- id: string (nullable = true)
 |-- name: string (nullable = true)
 |-- firstname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- title: integer (nullable = true)
 |-- company: string (nullable = true)
 |-- jobtitle: string (nullable = true)
 |-- company_contact_id: integer (nullable = true)
 |-- is_company: string (nullable = true)
 |-- is_user: string (nullable = true)
 |-- is_staff: integer (nullable = true)
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)
 |-- last_datetime: string (nullable = true)
 |-- sex: string (nullable = true)
 |-- about: string (nullable = true)
 |-- photo: integer (nullable = true)
 |-- create_datetime: string (nullable = true)
 |-- create_app_id: string (nullable = true)
 |-- create_method: string (nullable = true)
 |-- create_contact_id: integer (nullable = true)
 |-- locale: string (nullable = true)
 |-- timezone: string (nullable = true)
 |-- birth_day: integer (nullable = true)
 |-- birth_month: integer (nullable = true)
 |-- birth_year: integer (nullable = true)

```

### Data sample
```
|    id | name                         | firstname   | middlename    | lastname   |   title | company   | jobtitle      |   company_contact_id |   is_company |   is_user |   is_staff | login         | password                         | last_datetime       | sex   | about   |      photo | create_datetime     | create_app_id   | create_method   |   create_contact_id | locale   | timezone   |   birth_day |   birth_month |   birth_year |
|------:|:-----------------------------|:------------|:--------------|:-----------|--------:|:----------|:--------------|---------------------:|-------------:|----------:|-----------:|:--------------|:---------------------------------|:--------------------|:------|:--------|-----------:|:--------------------|:----------------|:----------------|--------------------:|:---------|:-----------|------------:|--------------:|-------------:|
|     1 | KORA Косметика Натуральная   | Косметика   | Натуральная   | KORA       |     nan |           | Администратор |                    0 |            0 |         1 |          1 | administrator | 329fd85b143f96cad66fe783e1af6e8a | 2023-08-17 18:12:09 |       |         | 1140276111 | 2014-07-30 00:54:41 | webasyst        | install         |                   0 | ru_RU    |            |          18 |             2 |         1984 |
| 68440 | Ишпахтина Эля Вячеславовна   | Эля         | Вячеславовна  | Ишпахтина  |     nan |           |               |                    0 |            0 |         0 |          0 |               | b54cbe3422c130de8d727b5b875252c4 | 2020-03-24 15:15:38 | f     |         |          0 | 2020-03-20 20:52:59 | shop            | signup          |                   0 |          |            |         nan |           nan |          nan |
| 47476 | Зимова Юлия Александровна    | Юлия        | Александровна | Зимова     |     nan |           |               |                    0 |            0 |         0 |          0 |               |                                  |                     |       |         |          0 | 2018-03-21 10:39:29 | shop            |                 |                   0 |          |            |         nan |           nan |          nan |
|     2 | КАЛЮЖНАЯ ЕКАТЕРИНА           | ЕКАТЕРИНА   |               | КАЛЮЖНАЯ   |     nan |           |               |                    0 |            0 |         0 |          0 |               | eace85f150e2e85986972ffb2a02f3fd |                     |       |         |          0 | 2008-11-28 00:53:31 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|     3 | КАЛЮЖНАЯ ЕКАТЕРИНА           | ЕКАТЕРИНА   |               | КАЛЮЖНАЯ   |     nan |           |               |                    0 |            0 |         0 |          0 |               | eace85f150e2e85986972ffb2a02f3fd |                     |       |         |          0 | 2008-11-28 00:55:37 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|     4 | Калюжная ЕКАТЕРИНА           | ЕКАТЕРИНА   |               | Калюжная   |     nan |           |               |                    0 |            0 |         0 |          0 |               | 215ac8956d2aba8da4cbebd920460a5f |                     |       |         |          0 | 2008-11-28 01:11:27 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|     5 | Потапова Алия                | Алия        |               | Потапова   |     nan |           |               |                    0 |            0 |         0 |          0 |               | 2085ab10ed575362bb48a8eb798d1dc8 |                     |       |         |          0 | 2008-11-28 01:46:49 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|     6 | Розенберг Вячеслав           | Вячеслав    |               | Розенберг  |     nan |           |               |                    0 |            0 |         0 |          0 |               | 8ac5b08dd6292beffce44a4bc9b12b4d |                     |       |         |          0 | 2008-11-28 12:48:37 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|     7 | Тимохина Екатерина           | Екатерина   |               | Тимохина   |     nan |           |               |                    0 |            0 |         0 |          0 |               | b0072872dd4da4ae291509869225abc5 | 2016-12-10 09:45:39 |       |         |          0 | 2008-11-28 15:25:15 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|     8 | Шевелина Татьяна             | Татьяна     |               | Шевелина   |     nan |           |               |                    0 |            0 |         0 |          0 |               | 6e3b97e14ced7cb97db50acc4d05fd45 | 2014-12-29 10:34:47 |       |         |          0 | 2008-11-28 15:37:43 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|     9 | Рубан Мария                  | Мария       |               | Рубан      |     nan |           |               |                    0 |            0 |         0 |          0 |               | c15d6ce6ff90066b048c0188aa4b7c83 |                     |       |         |          0 | 2008-11-28 15:45:51 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|    10 | Соловьева Анна               | Анна        |               | Соловьева  |     nan |           |               |                    0 |            0 |         0 |          0 |               | 47c5e17bebf23486cff3a0512c32dbae |                     |       |         |          0 | 2008-11-28 16:44:03 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|    11 | Смирнова Анастасия           | Анастасия   |               | Смирнова   |     nan |           |               |                    0 |            0 |         0 |          0 |               | 629c3592c016bc71989faee11ed2b828 |                     |       |         |          0 | 2008-11-28 19:21:45 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|    12 | Соколова Елена Александровна | Елена       | Александровна | Соколова   |     nan |           |               |                    0 |            0 |         0 |          0 |               | 8f1c89411f5d0d63563e06912190a2dc | 2021-04-20 20:27:14 |       |         |          0 | 2008-11-28 19:30:14 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|    13 | Барыкина Ксения              | Ксения      |               | Барыкина   |     nan |           |               |                    0 |            0 |         0 |          0 |               | bcb9ed10a1e8fadb5e71a89fb7129575 |                     |       |         |          0 | 2008-11-28 21:05:34 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|    14 | Стельмах Людмила             | Людмила     |               | Стельмах   |     nan |           |               |                    0 |            0 |         0 |          0 |               | fcea920f7412b5da7be0cf42b8c93759 |                     |       |         |          0 | 2008-11-29 12:08:58 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|    15 | Стельмах Людмила             | Людмила     |               | Стельмах   |     nan |           |               |                    0 |            0 |         0 |          0 |               | fcea920f7412b5da7be0cf42b8c93759 |                     |       |         |          0 | 2008-11-29 12:12:41 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|    16 | Карпова Анна                 | Анна        |               | Карпова    |     nan |           |               |                    0 |            0 |         0 |          0 |               | f10718e59f760291ee8930fb63cab9a9 |                     |       |         |          0 | 2008-11-29 15:28:36 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|    17 | Карпова Анна Игоревна        | Анна        | Игоревна      | Карпова    |     nan |           |               |                    0 |            0 |         0 |          0 |               | 039101b3540c4aab7a5f59a856b97042 | 2019-08-17 13:58:31 |       |         |          0 | 2008-11-29 15:34:14 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
|    18 | Карпова Анна                 | Анна        |               | Карпова    |     nan |           |               |                    0 |            0 |         0 |          0 |               | f10718e59f760291ee8930fb63cab9a9 |                     |       |         |          0 | 2008-11-29 15:38:38 | shop            |                 |                   1 |          |            |         nan |           nan |          nan |
```

> - File path: not_registered_contact_emails_names_from_messages_preprocessed.csv
> - Total rows: 114

### Schema
```
root
 |-- email: string (nullable = true)
 |-- name: string (nullable = true)

```

### Data sample
```
| email                          | name                       |
|:-------------------------------|:---------------------------|
|                                | 67807                      |
| alexandrova_anastacia@inbox.ru | alexandrova_anastacia      |
| 5008888@rambler.ru             | 5008888                    |
| abonchuk@yandex.ru             | abonchuk                   |
| alena_kapkova@mail.ru          | alena_kapkova              |
| adiallo23@student.cscc.edu     | adiallo23                  |
| almasth_allad@mail.ru          | almasth_allad              |
| 444444455544@mail.ru           | 444444455544               |
| alga60@mail.ru                 | alga60                     |
| generalov.nickolay@yandex.ru   | Генералов Николай Игоревич |
| 5594310@mail.ru                | 5594310                    |
| accessclosed@yandex.ru         | accessclosed               |
| alin.shashina@yandex.ru        | alin.shashina              |
| alladin68@list.ru              | alladin68                  |
| alena_dyachkova@mail.ru        | alena_dyachkova            |
| al.nosochencko@yandex.ru       | al.nosochencko             |
| alena69kot@gmail.com           | alena69kot                 |
| alex.sajan11@mail.ru           | alex.sajan11               |
| a.anokhina@absolutleasing.ru   | a.anokhina                 |
| aisedora.85@mail.ru            | aisedora.85                |
```

> - File path: shop_order_params_preprocessed.csv
> - Total rows: 114276

### Schema
```
root
 |-- order_id: string (nullable = true)
 |-- billing_address_city: string (nullable = true)
 |-- billing_address_country: string (nullable = true)
 |-- billing_address_dom: string (nullable = true)
 |-- billing_address_etazh: string (nullable = true)
 |-- billing_address_kvartira: string (nullable = true)
 |-- billing_address_lat: string (nullable = true)
 |-- billing_address_lng: string (nullable = true)
 |-- billing_address_region: string (nullable = true)
 |-- billing_address_street: string (nullable = true)
 |-- billing_address_ulitsa: string (nullable = true)
 |-- billing_address_zip: string (nullable = true)
 |-- billing_contact_name: string (nullable = true)
 |-- contact_email: string (nullable = true)
 |-- contact_name: string (nullable = true)
 |-- contact_phone: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- sdekint_city_country_name: string (nullable = true)
 |-- sdekint_city_name: string (nullable = true)
 |-- sdekint_city_region_name: string (nullable = true)
 |-- sdekint_country: string (nullable = true)
 |-- sdekint_dom: string (nullable = true)
 |-- sdekint_flat: string (nullable = true)
 |-- sdekint_house: string (nullable = true)
 |-- sdekint_kvartira: string (nullable = true)
 |-- sdekint_lat: string (nullable = true)
 |-- sdekint_lng: string (nullable = true)
 |-- sdekint_region: string (nullable = true)
 |-- sdekint_street: string (nullable = true)
 |-- sdekint_ulitsa: string (nullable = true)
 |-- sdekint_zip: string (nullable = true)
 |-- sdekint_contact_email: string (nullable = true)
 |-- sdekint_contact_name: string (nullable = true)
 |-- sdekint_contact_phone: string (nullable = true)
 |-- sdekint_contact_phones_0: string (nullable = true)
 |-- sdekint_contact_phones_1: string (nullable = true)
 |-- sdekint_contact_phones_2: string (nullable = true)
 |-- sdekint_contact_phones_3: string (nullable = true)
 |-- shipping_address_city: string (nullable = true)
 |-- shipping_address_country: string (nullable = true)
 |-- shipping_address_dom: string (nullable = true)
 |-- shipping_address_etazh: string (nullable = true)
 |-- shipping_address_kvartira: string (nullable = true)
 |-- shipping_address_lat: string (nullable = true)
 |-- shipping_address_lng: string (nullable = true)
 |-- shipping_address_region: string (nullable = true)
 |-- shipping_address_street: string (nullable = true)
 |-- shipping_address_ulitsa: string (nullable = true)
 |-- shipping_address_zip: string (nullable = true)
 |-- shipping_contact_name: string (nullable = true)
 |-- shipping_name: string (nullable = true)
 |-- user_agent: string (nullable = true)

```

### Data sample
```
| order_id                                  | billing_address_city   | billing_address_country   | billing_address_dom   | billing_address_etazh   | billing_address_kvartira   | billing_address_lat   | billing_address_lng   | billing_address_region   | billing_address_street                            | billing_address_ulitsa   | billing_address_zip   | billing_contact_name   | contact_email                  | contact_name     | contact_phone   | ip              | sdekint_city_country_name   | sdekint_city_name   | sdekint_city_region_name   | sdekint_country   | sdekint_dom   | sdekint_flat   | sdekint_house   | sdekint_kvartira   | sdekint_lat   | sdekint_lng   | sdekint_region   | sdekint_street   | sdekint_ulitsa   | sdekint_zip   | sdekint_contact_email   | sdekint_contact_name   | sdekint_contact_phone   | sdekint_contact_phones_0   | sdekint_contact_phones_1   | sdekint_contact_phones_2   | sdekint_contact_phones_3   | shipping_address_city   | shipping_address_country   | shipping_address_dom   | shipping_address_etazh   | shipping_address_kvartira   | shipping_address_lat   | shipping_address_lng   | shipping_address_region   | shipping_address_street                           | shipping_address_ulitsa   | shipping_address_zip   | shipping_contact_name   | shipping_name   | user_agent   |
|:------------------------------------------|:-----------------------|:--------------------------|:----------------------|:------------------------|:---------------------------|:----------------------|:----------------------|:-------------------------|:--------------------------------------------------|:-------------------------|:----------------------|:-----------------------|:-------------------------------|:-----------------|:----------------|:----------------|:----------------------------|:--------------------|:---------------------------|:------------------|:--------------|:---------------|:----------------|:-------------------|:--------------|:--------------|:-----------------|:-----------------|:-----------------|:--------------|:------------------------|:-----------------------|:------------------------|:---------------------------|:---------------------------|:---------------------------|:---------------------------|:------------------------|:---------------------------|:-----------------------|:-------------------------|:----------------------------|:-----------------------|:-----------------------|:--------------------------|:--------------------------------------------------|:--------------------------|:-----------------------|:------------------------|:----------------|:-------------|
| 1                                         |                        | rus                       |                       |                         |                            |                       |                       | Московская область       | Трофимова                                         |                          |                       | max bur                | bur-max@yandex.ru              | max bur          |                 | 93.80.101.182   |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | rus                        |                        |                          |                             |                        |                        | Московская область        | Трофимова                                         |                           |                        | max bur                 | Курьер          |              |
| 2                                         |                        | rus                       |                       |                         |                            |                       |                       | Московская область       | Трофимова                                         |                          |                       | max bur                | bur-max@yandex.ru              | max bur          |                 | 78.106.111.33   |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | rus                        |                        |                          |                             |                        |                        | Московская область        | Трофимова                                         |                           |                        | max bur                 | Курьер          |              |
| 3                                         |                        | rus                       |                       |                         |                            |                       |                       | Московская область       | Трофимова                                         |                          |                       | max bur                | bur-max@yandex.ru              | max bur          |                 | 78.106.111.33   |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | rus                        |                        |                          |                             |                        |                        | Московская область        | Трофимова                                         |                           |                        | max bur                 | Самовывоз       |              |
| 4                                         |                        | rus                       |                       |                         |                            |                       |                       | Московская область       | Трофимова                                         |                          |                       | max bur                | bur-max@yandex.ru              | max bur          |                 | 78.106.111.33   |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | rus                        |                        |                          |                             |                        |                        | Московская область        | Трофимова                                         |                           |                        | max bur                 | Курьер          |              |
| 5                                         |                        | rus                       |                       |                         |                            |                       |                       | Московская область       | Трофимова                                         |                          |                       | max bur                | bur-max@yandex.ru              | max bur          |                 | 78.106.111.33   |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | rus                        |                        |                          |                             |                        |                        | Московская область        | Трофимова                                         |                           |                        | max bur                 | Курьер          |              |
| 6                                         |                        | rus                       |                       |                         |                            |                       |                       | Московская область       | Трофимова                                         |                          |                       | max bur                | bur-max@yandex.ru              | max bur          |                 | 81.211.65.66    |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | rus                        |                        |                          |                             |                        |                        | Московская область        | Трофимова                                         |                           |                        | max bur                 | Курьер          |              |
| 7                                         |                        | rus                       |                       |                         |                            |                       |                       | Московская область       | Трофимова                                         |                          |                       | max bur                | bur-max@yandex.ru              | max bur          |                 | 81.211.65.66    |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | rus                        |                        |                          |                             |                        |                        | Московская область        | Трофимова                                         |                           |                        | max bur                 | Курьер          |              |
| 8                                         |                        | Габон                     |                       |                         |                            |                       |                       |                          | Дмитровское шоссе д.60А                           |                          |                       |                        |                                |                  |                 |                 |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         |                            |                        |                          |                             |                        |                        |                           |                                                   |                           |                        |                         |                 |              |
| (Здание бизнес центра с вывеской ""Плане" |                        |                           | ЕКАТЕРИНА Калюжная    | kat6ka@yandex.ru        | ЕКАТЕРИНА Калюжная         |                       | 85.202.113.43         |                          |                                                   |                          |                       |                        |                                |                  |                 |                 |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  | Габон         |                         |                        |                         |                            |                            |                            | Дмитровское шоссе д.60А    |                         |                            |                        |                          |                             |                        |                        |                           |                                                   |                           |                        |                         |                 |              |
| (Здание бизнес центра с вывеской ""Плане" |                        |                           | ЕКАТЕРИНА Калюжная    | Курьер                  |                            |                       |                       |                          |                                                   |                          |                       |                        |                                |                  |                 |                 |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         |                            |                        |                          |                             |                        |                        |                           |                                                   |                           |                        |                         |                 |              |
| 9                                         |                        | Суринам                   |                       |                         |                            |                       |                       |                          | 4-ый Лесной пер., 4, 547 офис, Москва             |                          |                       | Мария Рубан            | my2shy@mail.ru                 | Мария Рубан      |                 | 213.152.248.150 |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | Суринам                    |                        |                          |                             |                        |                        |                           | 4-ый Лесной пер., 4, 547 офис, Москва             |                           |                        | Мария Рубан             | Курьер          |              |
| 10                                        |                        | Суринам                   |                       |                         |                            |                       |                       |                          | 4-ый Лесной пер., 4, 547 офис, Москва             |                          |                       | Мария Рубан            | my2shy@mail.ru                 | Мария Рубан      |                 | 213.152.248.150 |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | Суринам                    |                        |                          |                             |                        |                        |                           | 4-ый Лесной пер., 4, 547 офис, Москва             |                           |                        | Мария Рубан             | Курьер          |              |
| 11                                        |                        |                           |                       |                         |                            |                       |                       |                          |                                                   |                          |                       |                        | als19692008@rambler.ru         | Людмила Стельмах |                 | 194.186.53.101  |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         |                            |                        |                          |                             |                        |                        |                           |                                                   |                           |                        |                         | Курьер          |              |
| 12                                        |                        |                           |                       |                         |                            |                       |                       |                          |                                                   |                          |                       |                        | als19692008@rambler.ru         | Людмила Стельмах |                 | 194.186.53.101  |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         |                            |                        |                          |                             |                        |                        |                           |                                                   |                           |                        |                         | Курьер          |              |
| 13                                        |                        |                           |                       |                         |                            |                       |                       |                          |                                                   |                          |                       |                        | njusja.k@gmail.com             | Анна Карпова     |                 | 78.106.93.52    |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         |                            |                        |                          |                             |                        |                        |                           |                                                   |                           |                        |                         | Курьер          |              |
| 14                                        |                        | Парагвай                  |                       |                         |                            |                       |                       |                          | РФ.Москва. ул Большая Якиманка. дом 45            |                          |                       | Дина Большакова        | dina.bolshakova@missioneco.org | Дина Большакова  |                 | 85.140.185.200  |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | Парагвай                   |                        |                          |                             |                        |                        |                           | РФ.Москва. ул Большая Якиманка. дом 45            |                           |                        | Дина Большакова         | Курьер          |              |
| 15                                        |                        | Сан-Томе и Принсипи       |                       |                         |                            |                       |                       |                          | г. Москва, ул. Молодежная, д.5, подъезд 6, кв.137 |                          |                       | ольга маркович         | bin21@mail.ru                  | ольга маркович   |                 | 217.117.127.22  |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | Сан-Томе и Принсипи        |                        |                          |                             |                        |                        |                           | г. Москва, ул. Молодежная, д.5, подъезд 6, кв.137 |                           |                        | ольга маркович          | Курьер          |              |
| 16                                        |                        | Сан-Томе и Принсипи       |                       |                         |                            |                       |                       |                          | г. Москва, ул. Молодежная, д.5, подъезд 6, кв.137 |                          |                       | ольга маркович         | bin21@mail.ru                  | ольга маркович   |                 | 217.117.127.22  |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | Сан-Томе и Принсипи        |                        |                          |                             |                        |                        |                           | г. Москва, ул. Молодежная, д.5, подъезд 6, кв.137 |                           |                        | ольга маркович          | Курьер          |              |
| 17                                        |                        | Сан-Томе и Принсипи       |                       |                         |                            |                       |                       |                          | г. Москва, ул. Молодежная, д.5, подъезд 6, кв.137 |                          |                       | ольга маркович         | bin21@mail.ru                  | ольга маркович   |                 | 217.117.127.22  |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | Сан-Томе и Принсипи        |                        |                          |                             |                        |                        |                           | г. Москва, ул. Молодежная, д.5, подъезд 6, кв.137 |                           |                        | ольга маркович          | Курьер          |              |
| 18                                        |                        | Сан-Томе и Принсипи       |                       |                         |                            |                       |                       |                          | г. Москва, ул. Молодежная, д.5, подъезд 6, кв.137 |                          |                       | ольга маркович         | bin21@mail.ru                  | ольга маркович   |                 | 217.117.127.22  |                             |                     |                            |                   |               |                |                 |                    |               |               |                  |                  |                  |               |                         |                        |                         |                            |                            |                            |                            |                         | Сан-Томе и Принсипи        |                        |                          |                             |                        |                        |                           | г. Москва, ул. Молодежная, д.5, подъезд 6, кв.137 |                           |                        | ольга маркович          | Курьер          |              |
```


## About final data

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
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- devices: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- user_agent: string (nullable = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.23% |
| Phones | 73.33% |
| Address | 65.93% |
| Sex | 9.56% |
| Birth_date | 5.13% |
| Socials | 4.65% |
| Devices | 33.43% |
| Ips | 46.59% |
| Actuality | 83.31% |



### Data sample
```
| names                                                           | emails                                                 | phones          | address                                                          |   sex | birth_date   | socials   | devices                                                                                                                                                                                                                                                                                                                                            | ips                         | actuality   |
|:----------------------------------------------------------------|:-------------------------------------------------------|:----------------|:-----------------------------------------------------------------|------:|:-------------|:----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|:------------|
| ['------- Елена']                                               | ['elena_ivonteva@mail.ru']                             | ['79037441095'] |                                                                  |   nan |              |           |                                                                                                                                                                                                                                                                                                                                                    |                             | 18.10.2011  |
| ['Amador Elvira']                                               | ['ellia112003@mail.ru']                                | ['79161561778'] | ['Москва Соймоновский проезд д.7 крпус 1 подъезд около троллей'] |   nan |              |           |                                                                                                                                                                                                                                                                                                                                                    |                             | 04.03.2009  |
| ['Andrewcon Andrewcon Andrewcon']                               | ['andrey03082017@gmail.com']                           |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144')]                                                                                                                                                                              | [Row(ip='93.72.51.208')]    | 29.11.2017  |
| ['Antonsmnv']                                                   | ['koptevandrey88@gmail.com']                           |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36')]                                                                                                                                                                                     | [Row(ip='176.36.21.189')]   |             |
| ['Arambathelvink Arambathelvink Arambathelvink']                | ['sat3187@yahoo.com']                                  |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 7.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0')]                                                                                                                                                                                                                              | [Row(ip='216.120.254.25')]  | 01.02.2018  |
| ['Arkadiirox Arkadiirox Arkadiirox']                            | ['ermakovdaniell@gmail.com']                           | ['78425787972'] |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]                                                                                                                                                                                                 | [Row(ip='213.21.30.95')]    | 12.10.2017  |
| ['Arthurgum Arthurgum Arthurgum']                               | ['katya.soleikina@yandex.ru']                          |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')]                                                                                                                                                                                    | [Row(ip='87.117.191.16')]   | 31.01.2019  |
| ['Arzu Gashimova']                                              | ['iulitas@yandex.ru']                                  |                 | ['Московская область МоскваГоловинское шоссе дом 8кор2 ком704']  |   nan |              |           |                                                                                                                                                                                                                                                                                                                                                    | [Row(ip='178.178.219.190')] |             |
| ['Backtemgaspig Backtemgaspig Backtemgaspig']                   | ['backtemga@mail.ru']                                  |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')]                                                                                                                                                                                                | [Row(ip='31.185.12.47')]    | 27.09.2018  |
| ['Bingoboomwrova Bingoboomwrova Bingoboomwrova']                | ['bingoboom23@mail.ru']                                |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144')]                                                                                                                                                                 | [Row(ip='109.172.78.221')]  | 05.03.2018  |
| ['Bladebringerhelvink Bladebringerhelvink Bladebringerhelvink'] | ['farrelldane@yahoo.com', 'danielle.lenson@gmail.com'] |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 7.1; Win64; rv:43.1) Gecko/20100101 Firefox/43.1'), Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 10.1; rv:40.1) Gecko/20100101 Firefox/40.1')]                                                                                                               | [Row(ip='216.120.254.25')]  | 30.01.2018  |
| ['Brettfub Brettfub Brettfub']                                  | ['hweint1@sslsmtp.win', 'emikoabe@sgdfhghtj5.work']    | ['74154711651'] |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'), Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.840 Yowser/2.5 Safari/537.36')] | [Row(ip='46.161.9.20')]     | 31.08.2017  |
| ['Burtonnic Burtonnic Burtonnic']                               | ['ldmila51dobrev@mail.ru']                             |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36')]                                                                                                                                                                                    | [Row(ip='184.147.17.163')]  | 14.12.2018  |
| ['Ceciliajak Ceciliajak Ceciliajak']                            | ['sllnghqqy@pilazzo.ru']                               | ['79344888249'] |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]                                                                                                                                                                                   | [Row(ip='46.161.9.68')]     | 22.03.2018  |
| ['Chrisval Chrisval Chrisval']                                  | ['auted140817@i.ua']                                   |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]                                                                                                                                                                                     | [Row(ip='93.188.37.224')]   | 24.09.2017  |
| ['Corneliusfuh Corneliusfuh Corneliusfuh']                      | ['sbezukladochnaya@inbox.ru']                          |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')]                                                                                                                                                                                    | [Row(ip='46.173.211.148')]  | 18.01.2019  |
| ['Creasimesspig Creasimesspig Creasimesspig']                   | ['creasimes@mail.ru']                                  |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')]                                                                                                                                                                                    | [Row(ip='31.185.9.60')]     | 22.09.2018  |
| ['Cветлана Соловьева']                                          | ['sv_sol@list.ru']                                     |                 | ['Московская область Москва ул.Туристкая.д10 кв.86']             |   nan |              |           |                                                                                                                                                                                                                                                                                                                                                    | [Row(ip='217.10.38.185')]   |             |
| ['Dustinjomma Dustinjomma Dustinjomma']                         | ['kostik.plotichkin@bk.ru']                            |                 |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36 Kinza/4.8.2')]                                                                                                                                                                                     | [Row(ip='46.173.211.148')]  | 20.02.2019  |
| ['Eugenearida Eugenearida Eugenearida']                         | ['pershicz.ivan@bk.ru']                                | ['79897133257'] |                                                                  |   nan |              |           | [Row(title='https://kora.ru', user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.54')]                                                                                                                                                                    | [Row(ip='46.173.211.148')]  | 03.01.2019  |
```