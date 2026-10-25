# Parsetron results

## About row data

> - Code name: index_0388
> - File path: users_preprocessed.csv
> - Total rows: 37326

### Schema
```
root
 |-- name: string (nullable = true)
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)
 |-- email1: string (nullable = true)
 |-- regdate: string (nullable = true)
 |-- logdate: timestamp (nullable = true)
 |-- last_ip: string (nullable = true)
 |-- discont_card: long (nullable = true)
 |-- customer_phone: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- address: string (nullable = true)

```

### Data sample
```
| name                            | login                    | password                         | email1                   | regdate             | logdate             | last_ip         |   discont_card | customer_phone      | email2                   | address                                                             |
|:--------------------------------|:-------------------------|:---------------------------------|:-------------------------|:--------------------|:--------------------|:----------------|---------------:|:--------------------|:-------------------------|:--------------------------------------------------------------------|
| Черепанов Василий Витальевич    | stiletsale@gmail.com     | 2a3f5eed35b323f7f2d28216613f585c | stiletsale@gmail.com     | 0000-00-00 00:00:00 | 2023-09-29 13:37:39 | 81.222.188.250  |  1820002417427 |                     | stiletsale@gmail.com     | 420034 Казань 2-я Юго-Западная д.28 кв.61                           |
| Харин Михаил Георгиевич         | kharin-mikhail@yandex.ru | 0aefa2e65e532f1183a38f3f12e20a63 | kharin-mikhail@yandex.ru | 0000-00-00 00:00:00 | 2023-04-08 17:55:04 | 176.52.106.214  |  1810120008546 |                     | kharin-mikhail@yandex.ru | 0                                                                   |
| Золотов Денис Сергеевич         | zooldenis@yandex.ru      | 03076fd64f5525ef67297dfa8a60c4f9 | zooldenis@yandex.ru      | 0000-00-00 00:00:00 | 2023-07-10 14:46:25 | 84.47.153.5     |  1820002444829 |                     | zooldenis@yandex.ru      | 170000 Тверь улица Советская д.7 кв.14                              |
| Филиппов Алексей Сергеевич      | lexx.paul@gmail.com      | 8dcde4cd40f78e8aee54543af7c937e6 | lexx.paul@gmail.com      | 0000-00-00 00:00:00 | 2023-02-14 12:08:13 | 91.244.253.167  |  1313133506042 |                     | lexx.paul@gmail.com      | 0                                                                   |
| конов алексей михайлович        | k-konov2012@yandex.ru    | d62a13ad793dcc53958748a208c555e9 | k-konov2012@yandex.ru    | 0000-00-00 00:00:00 | 2022-06-27 17:28:02 | 85.249.30.168   |  1313133804148 |                     | k-konov2012@yandex.ru    | 422526 зеленодольский р-он пос.октябрьский ул.железнодорожная26.кв1 |
| Морозов Виталий Вадимович       | a.aschotov@yandex.ru     | e7775c7f3a89accd3a19deee0225f728 | morozow.ya94@yandex.ru   | 2015-03-04 12:06:47 | 2024-01-23 19:33:25 | 178.204.200.96  |  7777777232738 | +7 (904) 760-17-32  | morozow.ya94@yandex.ru   | 420087 Казань ул. Карбышева 46-22                                   |
| Киямов Айрат Хаматгалиевич      | skoro_airat@mail.ru      | 8de0e387ffeeaaffba8ca3520df70b7a | skoro_airat@mail.ru      | 0000-00-00 00:00:00 | 2022-12-17 09:18:39 | 5.101.23.208    |          15967 |                     | skoro_airat@mail.ru      | 0                                                                   |
| Владимир                        | twinkerzz.what@mail.ru   | 5f53324c674028537edf7c3af0640fc9 | twinkerzz.what@mail.ru   | 2018-12-17 01:09:11 | 2022-07-02 02:47:40 | 46.187.34.53    |  1820026474987 | +7 (996) 949-83-36  | twinkerzz.what@mail.ru   | 0                                                                   |
| Алексей                         | marales16@mail.ru        | 236f0415ea426ab2ecb266dd43b07e58 | marales16@mail.ru        | 2019-03-06 12:01:02 | 2022-10-20 15:21:55 | 85.140.2.52     |  1820026489998 | +7 (890) 338-84-144 | marales16@mail.ru        | 0                                                                   |
| Артур                           | nadezhdindin@gmail.com   | 1c14c22a9f153450488aa6033ca00ac7 | nadezhdindin@gmail.com   | 2019-07-05 18:21:12 | 2023-06-09 12:53:08 | 85.249.27.141   |  1820026511026 | +7 (903) 341-33-91  | nadezhdindin@gmail.com   | 0                                                                   |
| Мальцев Эдуард Иванович         | malllya@mail.ru          | 98511ee588d2ebeec32bf22908f6bc76 | malllya@mail.ru          | 0000-00-00 00:00:00 | 2020-03-27 15:10:44 | 92.51.25.66     |  1820002412422 |                     | malllya@mail.ru          | 617123 Верещагино Карла Маркса, 138-10                              |
| Каргин Станислав Викторович     | danfield@list.ru         | 4ad77ea88f1476f89ac1d90221d922df | danfield@list.ru         | 0000-00-00 00:00:00 | 2021-09-23 22:11:18 | 176.59.125.25   |  7777777132090 |                     | danfield@list.ru         | 420087 Казань Гвардейская  д65 кв14                                 |
| Артем                           | kpfox@list.ru            | e768a61d5b28a69b3765160e7d6199ce | kpfox@list.ru            | 0000-00-00 00:00:00 | 2020-04-21 20:06:55 | 85.140.1.1      |  1820002437975 |                     | kpfox@list.ru            | 420000 казань ул.Галии кайбицкой д.12 кв.21                         |
| Хабибов Арсен Аюбович           | bony2226699@mail.ru      | fa06492e255c4b88beceaeb1548bbda0 | bony2226699@mail.ru      | 0000-00-00 00:00:00 | 2021-03-19 11:32:30 | 85.249.166.33   |  1820002446243 |                     | bony2226699@mail.ru      | 0                                                                   |
| Пржевальский Сергей Геннадьевич | vtts2529@gmail.com       | 127be07a05c5b9bb5306bed23eb4ca68 | vtts2529@gmail.com       | 0000-00-00 00:00:00 | 2020-06-22 09:08:38 | 176.59.99.251   |  1820002448506 |                     | vtts2529@gmail.com       | 426034 Ижевск Коммунаров 218-37                                     |
| семин алексей викторович        | alisa.semina@bk.ru       | a7f67fe0ef7844d5d4fd3db1ea2fadf3 | alisa.semina@bk.ru       | 0000-00-00 00:00:00 | 2021-05-05 20:42:46 | 87.117.185.183  |  1820002450691 |                     | alisa.semina@bk.ru       | 420033 казань ул. Батыршина 38 корпус 2 второй подьезд кв 23        |
| Грановский Андрей               | andersonya@mail.ru       | 3e3acb6ba598c1fb66cd79d485f60d64 | andersonya@mail.ru       | 0000-00-00 00:00:00 | 2021-03-08 15:53:53 | 188.225.107.125 |  1820002453395 |                     | andersonya@mail.ru       | 420054 казань В.Кулагина дом 6 кв 69                                |
| Юрасов Алексей Алексеевич       | hsz@yandex.ru            | 13d7c0c273d72db09c66310b942b70ee | hsz@yandex.ru            | 0000-00-00 00:00:00 | 2020-04-28 07:23:49 | 80.83.234.242   |  1820002460003 |                     | hsz@yandex.ru            | 0                                                                   |
| Артур                           | 502000@mail.ru           | 6b97a6c76e455af9d11a78fe906c184a | subarukzn@yandex.ru      | 0000-00-00 00:00:00 | 2020-04-28 20:26:06 | 94.180.139.102  |  1820002460997 |                     | subarukzn@yandex.ru      | 0                                                                   |
| Хайруллин Булат Тахирович       | vip_hajrullin@list.ru    | e2d6dcc41a94f8ea67c62ac846ee1cdc | vip_hajrullin@list.ru    | 0000-00-00 00:00:00 | 2021-11-06 11:03:51 | 176.52.100.57   |  1820002463257 |                     | vip_hajrullin@list.ru    | 0                                                                   |
```


## About final data
> - Total rows: 9968

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |    |    |-- client_card_number: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Ips | 100.00% |
| Emails | 100.00% |
| Phones | 98.18% |
| Address | 67.32% |
| Accounts | 100.00% |
| Actuality | 100.00% |



### Data sample
```
| names                               | ips                                            | emails                       | phones          | address                                                                 | accounts                                                                                                                                                                  | actuality   |
|:------------------------------------|:-----------------------------------------------|:-----------------------------|:----------------|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Черепанов Василий Витальевич']    | [Row(ip='81.222.188.250', date='29.09.2023')]  | ['stiletsale@gmail.com']     |                 | ['420034 Казань 2-я Юго-Западная д.28 кв.61']                           | [Row(title='Эролайф', link='https://erolaif.ru', login='stiletsale@gmail.com', password_hash='2a3f5eed35b323f7f2d28216613f585c', client_card_number='1820002417427')]     | 29.09.2023  |
| ['Харин Михаил Георгиевич']         | [Row(ip='176.52.106.214', date='08.04.2023')]  | ['kharin-mikhail@yandex.ru'] |                 |                                                                         | [Row(title='Эролайф', link='https://erolaif.ru', login='kharin-mikhail@yandex.ru', password_hash='0aefa2e65e532f1183a38f3f12e20a63', client_card_number='1810120008546')] | 08.04.2023  |
| ['Золотов Денис Сергеевич']         | [Row(ip='84.47.153.5', date='10.07.2023')]     | ['zooldenis@yandex.ru']      |                 | ['170000 Тверь улица Советская д.7 кв.14']                              | [Row(title='Эролайф', link='https://erolaif.ru', login='zooldenis@yandex.ru', password_hash='03076fd64f5525ef67297dfa8a60c4f9', client_card_number='1820002444829')]      | 10.07.2023  |
| ['Филиппов Алексей Сергеевич']      | [Row(ip='91.244.253.167', date='14.02.2023')]  | ['lexx.paul@gmail.com']      |                 |                                                                         | [Row(title='Эролайф', link='https://erolaif.ru', login='lexx.paul@gmail.com', password_hash='8dcde4cd40f78e8aee54543af7c937e6', client_card_number='1313133506042')]      | 14.02.2023  |
| ['Конов Алексей Михайлович']        | [Row(ip='85.249.30.168', date='27.06.2022')]   | ['k-konov2012@yandex.ru']    |                 | ['422526 Зеленодольский Р-Он Пос.Октябрьский Ул.Железнодорожная26.Кв1'] | [Row(title='Эролайф', link='https://erolaif.ru', login='k-konov2012@yandex.ru', password_hash='d62a13ad793dcc53958748a208c555e9', client_card_number='1313133804148')]    | 27.06.2022  |
| ['Морозов Виталий Вадимович']       | [Row(ip='178.204.200.96', date='23.01.2024')]  | ['morozow.ya94@yandex.ru']   | ['79047601732'] | ['420087 Казань ул. Карбышева 46-22']                                   | [Row(title='Эролайф', link='https://erolaif.ru', login='a.aschotov@yandex.ru', password_hash='e7775c7f3a89accd3a19deee0225f728', client_card_number='7777777232738')]     | 23.01.2024  |
| ['Киямов Айрат Хаматгалиевич']      | [Row(ip='5.101.23.208', date='17.12.2022')]    | ['skoro_airat@mail.ru']      |                 |                                                                         | [Row(title='Эролайф', link='https://erolaif.ru', login='skoro_airat@mail.ru', password_hash='8de0e387ffeeaaffba8ca3520df70b7a', client_card_number='15967')]              | 17.12.2022  |
| ['Владимир']                        | [Row(ip='46.187.34.53', date='02.07.2022')]    | ['twinkerzz.what@mail.ru']   | ['79969498336'] |                                                                         | [Row(title='Эролайф', link='https://erolaif.ru', login='twinkerzz.what@mail.ru', password_hash='5f53324c674028537edf7c3af0640fc9', client_card_number='1820026474987')]   | 02.07.2022  |
| ['Алексей']                         | [Row(ip='85.140.2.52', date='20.10.2022')]     | ['marales16@mail.ru']        | ['79033884144'] |                                                                         | [Row(title='Эролайф', link='https://erolaif.ru', login='marales16@mail.ru', password_hash='236f0415ea426ab2ecb266dd43b07e58', client_card_number='1820026489998')]        | 20.10.2022  |
| ['Артур']                           | [Row(ip='85.249.27.141', date='09.06.2023')]   | ['nadezhdindin@gmail.com']   | ['79033413391'] |                                                                         | [Row(title='Эролайф', link='https://erolaif.ru', login='nadezhdindin@gmail.com', password_hash='1c14c22a9f153450488aa6033ca00ac7', client_card_number='1820026511026')]   | 09.06.2023  |
| ['Мальцев Эдуард Иванович']         | [Row(ip='92.51.25.66', date='27.03.2020')]     | ['malllya@mail.ru']          |                 | ['617123 Верещагино Карла Маркса 138-10']                               | [Row(title='Эролайф', link='https://erolaif.ru', login='malllya@mail.ru', password_hash='98511ee588d2ebeec32bf22908f6bc76', client_card_number='1820002412422')]          | 27.03.2020  |
| ['Каргин Станислав Викторович']     | [Row(ip='176.59.125.25', date='23.09.2021')]   | ['danfield@list.ru']         |                 | ['420087 Казань Гвардейская д65 кв14']                                  | [Row(title='Эролайф', link='https://erolaif.ru', login='danfield@list.ru', password_hash='4ad77ea88f1476f89ac1d90221d922df', client_card_number='7777777132090')]         | 23.09.2021  |
| ['Артем']                           | [Row(ip='85.140.1.1', date='21.04.2020')]      | ['kpfox@list.ru']            |                 | ['420000 казань ул.Галии кайбицкой д.12 кв.21']                         | [Row(title='Эролайф', link='https://erolaif.ru', login='kpfox@list.ru', password_hash='e768a61d5b28a69b3765160e7d6199ce', client_card_number='1820002437975')]            | 21.04.2020  |
| ['Хабибов Арсен Аюбович']           | [Row(ip='85.249.166.33', date='19.03.2021')]   | ['bony2226699@mail.ru']      |                 |                                                                         | [Row(title='Эролайф', link='https://erolaif.ru', login='bony2226699@mail.ru', password_hash='fa06492e255c4b88beceaeb1548bbda0', client_card_number='1820002446243')]      | 19.03.2021  |
| ['Пржевальский Сергей Геннадьевич'] | [Row(ip='176.59.99.251', date='22.06.2020')]   | ['vtts2529@gmail.com']       |                 | ['426034 Ижевск Коммунаров 218-37']                                     | [Row(title='Эролайф', link='https://erolaif.ru', login='vtts2529@gmail.com', password_hash='127be07a05c5b9bb5306bed23eb4ca68', client_card_number='1820002448506')]       | 22.06.2020  |
| ['Семин Алексей Викторович']        | [Row(ip='87.117.185.183', date='05.05.2021')]  | ['alisa.semina@bk.ru']       |                 | ['420033 казань ул. Батыршина 38 корпус 2 второй подьезд кв 23']        | [Row(title='Эролайф', link='https://erolaif.ru', login='alisa.semina@bk.ru', password_hash='a7f67fe0ef7844d5d4fd3db1ea2fadf3', client_card_number='1820002450691')]       | 05.05.2021  |
| ['Грановский Андрей']               | [Row(ip='188.225.107.125', date='08.03.2021')] | ['andersonya@mail.ru']       |                 | ['420054 казань В.Кулагина дом 6 кв 69']                                | [Row(title='Эролайф', link='https://erolaif.ru', login='andersonya@mail.ru', password_hash='3e3acb6ba598c1fb66cd79d485f60d64', client_card_number='1820002453395')]       | 08.03.2021  |
| ['Юрасов Алексей Алексеевич']       | [Row(ip='80.83.234.242', date='28.04.2020')]   | ['hsz@yandex.ru']            |                 |                                                                         | [Row(title='Эролайф', link='https://erolaif.ru', login='hsz@yandex.ru', password_hash='13d7c0c273d72db09c66310b942b70ee', client_card_number='1820002460003')]            | 28.04.2020  |
| ['Артур']                           | [Row(ip='94.180.139.102', date='28.04.2020')]  | ['subarukzn@yandex.ru']      |                 |                                                                         | [Row(title='Эролайф', link='https://erolaif.ru', login='502000@mail.ru', password_hash='6b97a6c76e455af9d11a78fe906c184a', client_card_number='1820002460997')]           | 28.04.2020  |
| ['Хайруллин Булат Тахирович']       | [Row(ip='176.52.100.57', date='06.11.2021')]   | ['vip_hajrullin@list.ru']    |                 |                                                                         | [Row(title='Эролайф', link='https://erolaif.ru', login='vip_hajrullin@list.ru', password_hash='e2d6dcc41a94f8ea67c62ac846ee1cdc', client_card_number='1820002463257')]    | 06.11.2021  |
```