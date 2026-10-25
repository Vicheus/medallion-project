# Parsetron results

## About row data

> - File path: book24_ru.csv
> - Total rows: 4003787

### Schema
```
root
 |-- LOGIN: string (nullable = true)
 |-- PASSWORD: string (nullable = true)
 |-- CHECKWORD: string (nullable = true)
 |-- NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- LAST_LOGIN: string (nullable = true)
 |-- DATE_REGISTER: string (nullable = true)
 |-- PERSONAL_GENDER: string (nullable = true)
 |-- PERSONAL_PHONE: string (nullable = true)
 |-- PERSONAL_MOBILE: string (nullable = true)
 |-- PERSONAL_CITY: string (nullable = true)
 |-- ADMIN_NOTES: string (nullable = true)
 |-- PERSONAL_BIRTHDAY: string (nullable = true)
 |-- EXTERNAL_AUTH_ID: string (nullable = true)
 |-- CHECKWORD_TIME: string (nullable = true)
 |-- SECOND_NAME: string (nullable = true)
 |-- TITLE: string (nullable = true)

```

### Data sample
```
| LOGIN                                              | PASSWORD                                 | CHECKWORD                                | NAME      | LAST_NAME       | EMAIL                                                                                      | LAST_LOGIN          | DATE_REGISTER       | PERSONAL_GENDER   | PERSONAL_PHONE   | PERSONAL_MOBILE   | PERSONAL_CITY    | ADMIN_NOTES   | PERSONAL_BIRTHDAY   | EXTERNAL_AUTH_ID   | CHECKWORD_TIME      | SECOND_NAME   | TITLE                  |
|:---------------------------------------------------|:-----------------------------------------|:-----------------------------------------|:----------|:----------------|:-------------------------------------------------------------------------------------------|:--------------------|:--------------------|:------------------|:-----------------|:------------------|:-----------------|:--------------|:--------------------|:-------------------|:--------------------|:--------------|:-----------------------|
| fk-xkWx8qoqikrBoX-fk-zphxocnwwxvlvn-anonymous_5oth | x3rOoEjif2b9f7cd58e01b7dea067272df873370 | V6rKaeukf057b8f947b5445f19d0e91029af2bdd | null      | null            | fk-xkWx8qoqikrBoX-fk-zphxocnwwxvlvn-anonymous_5oth1s3jf@example.com                        | null                | 01.06.2016 14:30:46 |                   | null             | null              | null             | null          | null                | saleanonymous      | 27.12.2022 15:43:00 | null          | null                   |
| fk-8e2xYUKTZeRioe-fk-fkmqwkaveitudj-fk-cethjuzpc86 | O(v3m6Y{d3c94840b40954e3e973c5b2ae843f22 | O8h8fm0y2076432f328b7754614b01c83a8eabe8 | null      | null            | fk-8e2xYUKTZeRioe-fk-fkmqwkaveitudj-fk-cethjuzpc861mv-fk-mqxutbvtfbnf53-zvorun.av@eksmo.ru | 06.09.2017 10:05:12 | 02.06.2016 11:08:05 |                   | null             |                   | Москва           |               | null                | null               | 28.12.2022 9:42:28  | null          |                        |
| v.p.latyshev@yandex.ru                             | e9P\-m9V4ea9b6b39a707c91ea124f69de835a3c | Hiwpui06e62f371fdf90dde44ad6c4b05360597b | Василий   | Латышев         | v.p.latyshev@yandex.ru                                                                     | 26.05.2023 12:18:36 | 06.06.2016 17:18:46 | M                 | +7 916 820-58-98 |                   | Москва           |               | 25.01.2017          | null               | 30.12.2022 23:32:57 | Павлович      |                        |
| Zhuravleva.MV@bookcentre.ru                        | 5^jG2A.s2ed70b34c8ca502a7ea98fe0dea099b0 | gxHXvV9Ed8a7cf6b0b51b7a68aceef7ca933a6cf | Журавлева | Маргарита       | Zhuravleva.MV@bookcentre.ru                                                                | 18.05.2023 9:58:18  | 09.06.2016 15:01:45 | F                 | +7 903 261-01-51 |                   | Москва г, Россия |               | 09.10.1985          | null               | 22.03.2023 16:54:09 |               |                        |
| katerina_msk2007@mail.ru                           | l5;Z1eZ=9bb2d94f8a6f58ff89c40a6be1cf62d1 | L5CNwSOf5acfe3727a747e13408800a5005d2652 | Екатерина | Мосяга          | katerina_msk2007@mail.ru                                                                   | 25.01.2023 12:11:53 | 09.06.2016 16:03:23 | F                 | +7 916 438-79-06 |                   | Москва г         |               | 20.06.2017          | null               | 15.11.2021 13:54:57 | Юрьевна       |                        |
| kiro2100@yandex.ru                                 | 1wU:zD2{4cb09bea0eebff5bff8d9cb8eebc57dd | 06d9Aej93f98dc3b79a473156c08847ffe01642d | пас       | кирилл          | kiro2100@yandex.ru                                                                         | 27.02.2022 12:36:11 | 10.06.2016 0:35:46  | M                 | null             | null              | null             | null          | null                | null               | 20.01.2020 19:32:07 |               | null                   |
| fk-qxxXKwcPJqJzuZ-ivan@balvan.com                  | SMDYDNvPe639a0c22d72a8ade3b4c89603f8db95 | 3xNYANrD47e96d7e8f85f696b0ac27ba5d521cfb | null      | null            | fk-qxxXKwcPJqJzuZ-ivan@balvan.com                                                          | 16.12.2021 19:13:39 | 10.06.2016 11:35:57 |                   | null             | 89168205898       | null             | null          | null                | null               | 28.12.2022 1:33:50  | null          | null                   |
| t@tt.ru                                            | 6wtm9bSe6dd21f8de446c32dc94e5acfd64de5d4 | WYe5pRKnc289e14edd87bb9511444855b171e5cd | t         | t               | t@tt.ru                                                                                    | null                | 11.06.2016 16:13:14 |                   | null             | null              | null             | null          | null                | null               | 29.08.2016 12:50:12 | t             | null                   |
| urlico@petrushka.ru                                | PA1R9Dxzb0ba3d5377312e809a298fef49c2b575 | Yssso7lp796cfb28faf784338be2f972837e0d96 | Василий   | Латышев         | urlico@petrushka.ru                                                                        | 14.06.2016 10:49:43 | 14.06.2016 10:49:43 | M                 | null             | 89168205898       | null             | null          | null                | null               | 14.06.2016 10:49:43 |               | null                   |
| artem@luchnikov.ru                                 | 3(cBo>3G5ba5a7e9b356c0bcf5fd97f1628bd679 | FFz6KTudaa54f88bc99ad1e2b36949fa1187633d | Артём     | Лучников        | artem@luchnikov.ru                                                                         | 24.11.2022 16:06:54 | 15.06.2016 13:02:21 | M                 | +7 912 370-81-26 |                   | Москва           |               | 18.10.1986          | null               | 15.12.2020 10:53:35 |               |                        |
| svetshiman@gmail.com                               | LhyVqIMDb5d282b764681df42e7117ac77a03bf2 | DcNeFe9H912f4655289bd4d27765c760329e0693 |           |                 | svetshiman@gmail.com                                                                       | null                | 15.06.2016 18:12:47 |                   | null             |                   |                  |               | null                | null               | 02.03.2018 9:27:43  |               |                        |
| centos@centos.ru                                   | c5cELHlbde79cf3279dc0eda13c4fad3035d1608 | c6TwxgVMa39feb9068b44c04bcc2e8ecfdf837ff | TEST      | TEST            | centos@centos.ru                                                                           | 23.04.2018 22:10:19 | 16.06.2016 15:32:24 |                   | null             |                   |                  |               | null                | null               | 09.10.2018 7:22:57  | TEST          |                        |
| sterx@rl6.ru                                       | jF1+?Bi53c64c15b8db1c63dee36d98e27c9b392 | cYRgnz1ddcc5ed1705afd4177989d0f6c401fcad | Алексей   | Голобурдин      | sterx@rl6.ru                                                                               | 28.12.2021 9:32:25  | 16.06.2016 16:17:16 | M                 | +7 963 672-22-29 |                   | Москва           |               | null                | null               | 28.12.2021 9:32:05  | Анатольевич   |                        |
| di_07@inbox.ru                                     | KzORVeZge70e5bbc92169f4b4ffc69d486742c92 | SJIhmecB279f220ed9cbfa0a7b869fb580382ef4 | Диана     | Одинцова        | di_07@inbox.ru                                                                             | 16.06.2016 20:57:39 | 16.06.2016 20:57:39 | F                 | null             | null              | null             | null          | null                | null               | 16.06.2016 20:57:39 |               | null                   |
| kiro@hh.tt                                         | icmDvh16e86d4154f408b4ad9f23e9485f082dfc | bBm60ByA2b3b201d043ab4cb917d19f5e1849f19 | 2312      | 2321            | kiro@hh.tt                                                                                 | 16.06.2016 23:23:13 | 16.06.2016 23:23:13 |                   | null             | null              | null             | null          | null                | null               | 16.06.2016 23:23:13 | 213           | null                   |
| kirosan88@mail.ru                                  | 5fJUR7hH8bd4c1e5ac5c034d2461c0f58e2e722e | T92ff2Ak89cb467b0166f779ccd628dcdb766dea | 42        | 42342           | kirosan88@mail.ru                                                                          | 17.06.2016 14:21:22 | 16.06.2016 23:24:41 |                   | null             | null              | null             | null          | null                | null               | 16.06.2016 23:24:41 | 4234          | null                   |
| paucheok@yandex.ru                                 | S3MD0ogxca5f954248b88088032b7bdd90350880 | 7JyYrt8G356d059a2160607c28f13522bdd33882 | nev       | nev             | paucheok@yandex.ru                                                                         | 17.06.2016 10:33:15 | 17.06.2016 10:33:15 |                   | null             | null              | null             | null          | null                | null               | 17.06.2016 10:33:15 |               | null                   |
| svetshiman@mail.ru                                 | aVEjFBoxc079a08ece1d5c73ee15d7c4ed289fb8 | uIHFxycad9493a82c04080384140b333c612b6cf | Светлана  | Шиманская       | svetshiman@mail.ru                                                                         | 30.06.2016 16:06:48 | 17.06.2016 15:38:27 | F                 | null             | 89122827276       | null             | null          | null                | null               | 17.06.2016 15:38:27 | Олеговна      | null                   |
| a.sukhanov@yahoo.com                               | IP0ev3553319fb90533c374d61add2e101d6c0b8 | KM7DJm66165aabc91f5aeca7565423e786f5610c | 111111111 | 111111111111111 | a.sukhanov@yahoo.com                                                                       | 17.06.2016 16:49:15 | 17.06.2016 16:49:15 |                   | null             | null              | null             | null          | null                | null               | 17.06.2016 16:49:15 | 1111111111111 | null                   |
| Zhuravleva.MV@eksmo.ru                             | k#3Fn7A-c4be959b5db9d2db2a45b37050fc8073 | 7UELwM0T0f76593d8046cc85e14622ade07769e2 | Маргарита |                 | Zhuravleva.MV@eksmo.ru                                                                     | 30.11.2021 14:27:08 | 20.06.2016 10:13:09 | F                 | null             |                   |                  |               | null                | null               | 14.12.2022 16:33:46 |               | Zhuravleva.MV@eksmo.ru |
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
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.96% |
| Phones | 86.24% |
| Sex | 95.44% |
| Birth_date | 38.55% |
| Accounts | 100.00% |
| Actuality | 0.00% |



### Data sample
```
| names                              | emails                          | phones          |   sex | birth_date   | accounts                                                                                                                                  | actuality   |
|:-----------------------------------|:--------------------------------|:----------------|------:|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Латышев Василий Павлович']       | ['v.p.latyshev@yandex.ru']      | ['79168205898'] |     1 | 25.01.2017   | [Row(title='Book24', link='https://book24.ru', login='v.p.latyshev@yandex.ru', password='e9P\\-m9V4ea9b6b39a707c91ea124f69de835a3c')]     |             |
| ['Маргарита Журавлева']            | ['zhuravleva.mv@bookcentre.ru'] | ['79032610151'] |     0 | 09.10.1985   | [Row(title='Book24', link='https://book24.ru', login='Zhuravleva.MV@bookcentre.ru', password='5^jG2A.s2ed70b34c8ca502a7ea98fe0dea099b0')] |             |
| ['Мосяга Екатерина Юрьевна']       | ['katerina_msk2007@mail.ru']    | ['79164387906'] |     0 | 20.06.2017   | [Row(title='Book24', link='https://book24.ru', login='katerina_msk2007@mail.ru', password='l5;Z1eZ=9bb2d94f8a6f58ff89c40a6be1cf62d1')]    |             |
| ['Кирилл Пас']                     | ['kiro2100@yandex.ru']          |                 |     1 |              | [Row(title='Book24', link='https://book24.ru', login='kiro2100@yandex.ru', password='1wU:zD2{4cb09bea0eebff5bff8d9cb8eebc57dd')]          |             |
| ['T T T']                          | ['t@tt.ru']                     |                 |   nan |              | [Row(title='Book24', link='https://book24.ru', login='t@tt.ru', password='6wtm9bSe6dd21f8de446c32dc94e5acfd64de5d4')]                     |             |
| ['Латышев Василий']                | ['urlico@petrushka.ru']         | ['79168205898'] |     1 |              | [Row(title='Book24', link='https://book24.ru', login='urlico@petrushka.ru', password='PA1R9Dxzb0ba3d5377312e809a298fef49c2b575')]         |             |
| ['Лучников Артём']                 | ['artem@luchnikov.ru']          | ['79123708126'] |     1 | 18.10.1986   | [Row(title='Book24', link='https://book24.ru', login='artem@luchnikov.ru', password='3(cBo>3G5ba5a7e9b356c0bcf5fd97f1628bd679')]          |             |
| ['Голобурдин Алексей Анатольевич'] | ['sterx@rl6.ru']                | ['79636722229'] |     1 |              | [Row(title='Book24', link='https://book24.ru', login='sterx@rl6.ru', password='jF1+?Bi53c64c15b8db1c63dee36d98e27c9b392')]                |             |
| ['Одинцова Диана']                 | ['di_07@inbox.ru']              |                 |     0 |              | [Row(title='Book24', link='https://book24.ru', login='di_07@inbox.ru', password='KzORVeZge70e5bbc92169f4b4ffc69d486742c92')]              |             |
| ['Nev Nev']                        | ['paucheok@yandex.ru']          |                 |   nan |              | [Row(title='Book24', link='https://book24.ru', login='paucheok@yandex.ru', password='S3MD0ogxca5f954248b88088032b7bdd90350880')]          |             |
| ['Шиманская Светлана Олеговна']    | ['svetshiman@mail.ru']          | ['79122827276'] |     0 |              | [Row(title='Book24', link='https://book24.ru', login='svetshiman@mail.ru', password='aVEjFBoxc079a08ece1d5c73ee15d7c4ed289fb8')]          |             |
| ['Маргарита']                      | ['zhuravleva.mv@eksmo.ru']      |                 |     0 |              | [Row(title='Book24', link='https://book24.ru', login='Zhuravleva.MV@eksmo.ru', password='k#3Fn7A-c4be959b5db9d2db2a45b37050fc8073')]      |             |
| ['Б А В']                          | ['1@mail.ru']                   | ['79200000000'] |     0 | 12.02.1981   | [Row(title='Book24', link='https://book24.ru', login='1@mail.ru', password='eWYVQzsKfcb66d7732ada18f4fef0a7042836ef3')]                   |             |
| ['Иван Иван']                      | ['fkj@sdlkfjalkj.ur']           |                 |     1 |              | [Row(title='Book24', link='https://book24.ru', login='fkj@sdlkfjalkj.ur', password='pHrw6JpSac3c0e65a8ffe7421d63cdecea27c921')]           |             |
| ['Борисова Анжела Филатовна']      | ['pepokepaj@top1post.ru']       |                 |     0 |              | [Row(title='Book24', link='https://book24.ru', login='pepokepaj@top1post.ru', password='oFJeBqvCaf4c5df050298a37607227b7e15b8844')]       |             |
| ['Смирнова Алина Романовна']       | ['tigimadod@top1post.ru']       |                 |     0 |              | [Row(title='Book24', link='https://book24.ru', login='tigimadod@top1post.ru', password='Qvd82QBB4598ac0e9bac8e3322e9398f488a2048')]       |             |
| ['Карпова Татьяна Варламовна']     | ['jatep@top1post.ru']           |                 |     0 |              | [Row(title='Book24', link='https://book24.ru', login='jatep@top1post.ru', password='HG7y0RqF9b9e67eded4733733f167c308ef28355')]           |             |
| ['Ladnova Leyla']                  | ['mail.ladnova@gmail.com']      | ['79031235537'] |   nan |              | [Row(title='Book24', link='https://book24.ru', login='Mail.ladnova@gmail.com', password='cZEAsfqo9cb0897b097b7d4a630f62ace2c6c6c9')]      |             |
| ['Перейди Икота Нафедота']         | ['fedot@ikota.ru']              |                 |   nan |              | [Row(title='Book24', link='https://book24.ru', login='fedot@ikota.ru', password='5Tb77RLY8b1a248a36e8bce77ce16b4ca5301d98')]              |             |
| ['Титова Наина']                   | ['zasik@top1post.ru']           |                 |     0 |              | [Row(title='Book24', link='https://book24.ru', login='zasik@top1post.ru', password='jKEnogxdbff088ad658fa3da14d8255380007ab8')]           |             |
```