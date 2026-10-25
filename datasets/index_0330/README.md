# Parsetron results

## About row data

> - Code name: index_0330
> - File path: kuking.net.csv
> - Total rows: 132204

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- salt: string (nullable = true)
 |-- site: string (nullable = true)
 |-- about: string (nullable = true)
 |-- email: string (nullable = true)
 |-- avatar: string (nullable = true)
 |-- gender: integer (nullable = true)
 |-- status: integer (nullable = true)
 |-- location: string (nullable = true)
 |-- password: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- nick_name: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_visit: timestamp (nullable = true)
 |-- user_forum: integer (nullable = true)
 |-- user_posts: integer (nullable = true)
 |-- change_date: timestamp (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- user_themes: integer (nullable = true)
 |-- access_level: integer (nullable = true)
 |-- activate_key: string (nullable = true)
 |-- use_gravatar: integer (nullable = true)
 |-- activation_ip: string (nullable = true)
 |-- creation_date: timestamp (nullable = true)
 |-- email_confirm: integer (nullable = true)
 |-- online_status: string (nullable = true)
 |-- registration_ip: string (nullable = true)
 |-- registration_date: timestamp (nullable = true)
 |-- registration_date_forum: string (nullable = true)

```

### Data sample
```
|     id | salt                             | site    | about   | email                    | avatar                                       |   gender |   status | location   | password                         | last_name   | nick_name     | birth_date   | first_name   | last_visit          |   user_forum |   user_posts | change_date         | middle_name   |   user_themes |   access_level | activate_key                     |   use_gravatar | activation_ip   | creation_date       |   email_confirm | online_status   | registration_ip   | registration_date   | registration_date_forum   |
|-------:|:---------------------------------|:--------|:--------|:-------------------------|:---------------------------------------------|---------:|---------:|:-----------|:---------------------------------|:------------|:--------------|:-------------|:-------------|:--------------------|-------------:|-------------:|:--------------------|:--------------|--------------:|---------------:|:---------------------------------|---------------:|:----------------|:--------------------|----------------:|:----------------|:------------------|:--------------------|:--------------------------|
|      1 | 87b18d8c04b3768dfad9fc9bd191fa07 | <blank> | <blank> | root@kuking.net          | NULL                                         |        0 |        1 | <blank>    | b864ea12ac7af1e9deaccb487228c6c7 | <blank>     | root          | NULL         | <blank>      | 2020-03-19 11:51:37 |            0 |            0 | 2014-10-16 05:25:20 | <blank>       |             0 |              1 | 4689b157bcca0f658c57c5f7df5fa6b6 |              0 | 88.208.45.9     | 2013-09-18 11:59:35 |               1 | <blank>         | 88.208.45.9       | 2013-09-18 11:59:35 | 0000-00-00 00:00:00       |
| 124480 | ebacaa833727967e31aaf8ce10bd1cbc | <blank> | <blank> | test@gmail.com           | /my/images/avatars/769eb4fd55b1af5db9b24.gif |        0 |        1 | <blank>    | ebacaa833727967e31aaf8ce10bd1cbc | <blank>     | admin         | NULL         | <blank>      | 2017-06-28 04:06:17 |            2 |          710 | 2017-07-13 03:35:01 | <blank>       |            49 |              0 | ebacaa833727967e31aaf8ce10bd1cbc |              0 | 195.92.38.5     | 2014-04-01 12:43:43 |               1 | <blank>         | 195.92.38.5       | 2002-05-10 21:24:04 | 2002-05-10 21:24:04       |
| 124481 | 4a65071285f88b9a1cf40693a64a209e | <blank> | <blank> | denis@kuking.net         | /my/images/avatars/AAvatars/ummm.gif         |        0 |        1 | <blank>    | 4a65071285f88b9a1cf40693a64a209e | <blank>     | denis         | NULL         | <blank>      | 2021-12-21 11:57:56 |            3 |           60 | 2021-12-21 14:15:01 | <blank>       |             6 |              0 | 4a65071285f88b9a1cf40693a64a209e |              0 | 195.92.70.130   | 2014-04-01 12:43:43 |               1 | <blank>         | 195.92.70.130     | 2001-11-20 23:43:17 | 2001-11-20 23:43:17       |
| 124482 | b3269a2e2ba82d4e8b89ab0001f5df86 | <blank> | <blank> | maria@kuking.net         | /my/images/avatars/57c2b4e94784e2672aee8.jpg |        0 |        1 | <blank>    | b3269a2e2ba82d4e8b89ab0001f5df86 | <blank>     | Maria         | NULL         | <blank>      | 2015-07-24 02:12:20 |            4 |         4282 | 2015-07-24 03:25:01 | <blank>       |           409 |              0 | b3269a2e2ba82d4e8b89ab0001f5df86 |              0 | 195.92.38.4     | 2014-04-01 12:43:43 |               1 | <blank>         | 195.92.38.4       | 2001-11-21 19:55:00 | 2001-11-21 19:55:00       |
| 124483 | e0018d7058c93fbb70da83e4ec7b1976 | <blank> | <blank> | trushin@ufanet.ru        | /my/images/avatars/General/linux.gif         |        0 |        1 | <blank>    | e0018d7058c93fbb70da83e4ec7b1976 | <blank>     | Dina          | NULL         | <blank>      | 2009-04-13 08:11:57 |            5 |          126 | 2014-04-03 07:53:22 | <blank>       |            21 |              0 | e0018d7058c93fbb70da83e4ec7b1976 |              0 | 81.30.207.166   | 2014-04-01 12:43:43 |               1 | <blank>         | 81.30.207.166     | 2001-11-22 07:17:00 | 2001-11-22 07:17:00       |
| 124484 | e0018d7058c93fbb70da83e4ec7b1976 | <blank> | <blank> | vigi5@bezeqint.net       | NULL                                         |        0 |        1 | <blank>    | e0018d7058c93fbb70da83e4ec7b1976 | <blank>     | Anna          | NULL         | <blank>      | 2012-01-18 16:16:22 |            7 |          774 | 2014-04-03 07:53:22 | <blank>       |            21 |              0 | e0018d7058c93fbb70da83e4ec7b1976 |              0 | 212.179.204.211 | 2014-04-01 12:43:43 |               1 | <blank>         | 212.179.204.211   | 2001-11-22 19:39:41 | 2001-11-22 19:39:41       |
| 124485 | e0018d7058c93fbb70da83e4ec7b1976 | <blank> | <blank> | Yuri_Podolsky@mail.ru    | NULL                                         |        0 |        1 | <blank>    | e0018d7058c93fbb70da83e4ec7b1976 | <blank>     | Yuri_Podolsky | NULL         | <blank>      | 1970-01-01 04:00:00 |            8 |            1 | 2014-04-03 07:53:22 | <blank>       |             0 |              0 | e0018d7058c93fbb70da83e4ec7b1976 |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2001-11-23 00:49:20 | 2001-11-23 00:49:20       |
| 124486 | e0018d7058c93fbb70da83e4ec7b1976 | <blank> | <blank> | genuaria_lav2001@mail.ru | NULL                                         |        0 |        1 | <blank>    | e0018d7058c93fbb70da83e4ec7b1976 | <blank>     | geka          | NULL         | <blank>      | 2002-05-24 11:05:28 |            9 |           11 | 2014-04-03 07:53:22 | <blank>       |             1 |              0 | e0018d7058c93fbb70da83e4ec7b1976 |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2001-11-23 16:12:53 | 2001-11-23 16:12:53       |
| 124487 | e0018d7058c93fbb70da83e4ec7b1976 | <blank> | <blank> | jjullia@hotmail.com      | NULL                                         |        0 |        1 | <blank>    | e0018d7058c93fbb70da83e4ec7b1976 | <blank>     | Jul           | NULL         | <blank>      | 2008-06-26 23:32:07 |           12 |          160 | 2014-04-03 07:53:22 | <blank>       |             4 |              0 | e0018d7058c93fbb70da83e4ec7b1976 |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2001-11-27 05:21:45 | 2001-11-27 05:21:45       |
| 124488 | e0018d7058c93fbb70da83e4ec7b1976 | <blank> | <blank> | laur_anja@hotmail.com    | /my/images/avatars/Fantasy/apollo.gif        |        0 |        1 | <blank>    | e0018d7058c93fbb70da83e4ec7b1976 | <blank>     | Dascha        | NULL         | <blank>      | 2011-01-03 16:43:13 |           17 |          765 | 2014-04-03 07:53:22 | <blank>       |            43 |              0 | e0018d7058c93fbb70da83e4ec7b1976 |              0 | 194.118.89.218  | 2014-04-01 12:43:43 |               1 | <blank>         | 194.118.89.218    | 2001-12-03 18:46:06 | 2001-12-03 18:46:06       |
| 124489 | e0018d7058c93fbb70da83e4ec7b1976 | <blank> | <blank> | lissa@r66.ru             | NULL                                         |        0 |        1 | <blank>    | e0018d7058c93fbb70da83e4ec7b1976 | <blank>     | LISSA         | NULL         | <blank>      | 1970-01-01 04:00:00 |           18 |            1 | 2014-04-03 07:53:22 | <blank>       |             1 |              0 | e0018d7058c93fbb70da83e4ec7b1976 |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2001-12-03 23:04:55 | 2001-12-03 23:04:55       |
| 124490 | 256e8dbd04f161b7a1369612e397f2f2 | <blank> | <blank> | igorus@at-travel.ru      | NULL                                         |        0 |        1 | <blank>    | 256e8dbd04f161b7a1369612e397f2f2 | <blank>     | Igorus        | NULL         | <blank>      | 2015-11-16 13:06:00 |           22 |            2 | 2015-11-17 03:35:01 | <blank>       |             0 |              0 | 256e8dbd04f161b7a1369612e397f2f2 |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2001-12-10 12:34:24 | 2001-12-10 12:34:24       |
| 124491 | e0018d7058c93fbb70da83e4ec7b1976 | <blank> | <blank> | olgas99@hotmail.com      | NULL                                         |        0 |        1 | <blank>    | e0018d7058c93fbb70da83e4ec7b1976 | <blank>     | olga          | NULL         | <blank>      | 2008-06-27 15:30:51 |           25 |            1 | 2014-04-03 07:53:23 | <blank>       |             0 |              0 | e0018d7058c93fbb70da83e4ec7b1976 |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2001-12-12 23:07:09 | 2001-12-12 23:07:09       |
| 124492 | 81ef06d0baa6c5f180b099693577c0be | <blank> | <blank> | dewi@mail.ru             | NULL                                         |        0 |        1 | <blank>    | 81ef06d0baa6c5f180b099693577c0be | <blank>     | dewi          | NULL         | <blank>      | 1970-01-01 04:00:00 |           34 |            1 | 2014-04-03 07:53:23 | <blank>       |             1 |              0 | 81ef06d0baa6c5f180b099693577c0be |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2001-12-21 15:15:37 | 2001-12-21 15:15:37       |
| 124493 | 81ef06d0baa6c5f180b099693577c0be | <blank> | <blank> | oksanulia@chat.ru        | NULL                                         |        0 |        1 | <blank>    | 81ef06d0baa6c5f180b099693577c0be | <blank>     | Oksana        | NULL         | <blank>      | 1970-01-01 04:00:00 |           36 |            1 | 2014-04-03 07:53:23 | <blank>       |             1 |              0 | 81ef06d0baa6c5f180b099693577c0be |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2001-12-23 12:32:03 | 2001-12-23 12:32:03       |
| 124494 | 81ef06d0baa6c5f180b099693577c0be | <blank> | <blank> | Nexorosho@yahoo.com      | NULL                                         |        0 |        1 | <blank>    | 81ef06d0baa6c5f180b099693577c0be | <blank>     | Sasha         | NULL         | <blank>      | 1970-01-01 04:00:00 |           39 |            2 | 2014-04-03 07:53:23 | <blank>       |             2 |              0 | 81ef06d0baa6c5f180b099693577c0be |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2001-12-27 20:42:33 | 2001-12-27 20:42:33       |
| 124495 | 81ef06d0baa6c5f180b099693577c0be | <blank> | <blank> | vlatamir@list.ru         | /my/images/avatars/d555a87342b279373fafc.jpg |        0 |        1 | <blank>    | 81ef06d0baa6c5f180b099693577c0be | <blank>     | impraimis     | NULL         | <blank>      | 2006-07-09 22:58:54 |           45 |          122 | 2014-04-03 07:53:23 | <blank>       |            21 |              0 | 81ef06d0baa6c5f180b099693577c0be |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2002-01-10 18:00:02 | 2002-01-10 18:00:02       |
| 124496 | 81ef06d0baa6c5f180b099693577c0be | <blank> | <blank> | kruge@mailru.com         | /my/images/avatars/General/baby.gif          |        0 |        1 | <blank>    | 81ef06d0baa6c5f180b099693577c0be | <blank>     | Lesha_Kruge   | NULL         | <blank>      | 2003-01-14 00:09:21 |           47 |           12 | 2014-04-03 07:53:23 | <blank>       |             3 |              0 | 81ef06d0baa6c5f180b099693577c0be |              0 | 213.33.245.182  | 2014-04-01 12:43:43 |               1 | <blank>         | 213.33.245.182    | 2002-01-12 23:08:19 | 2002-01-12 23:08:19       |
| 124497 | 4f74a90344dcd90f1b4ee1daf4dd661f | <blank> | <blank> | ufik9@yandex.ru          | /my/images/avatars/5abe8a134767fe6a644b6.gif |        0 |        1 | <blank>    | 4f74a90344dcd90f1b4ee1daf4dd661f | <blank>     | ufik          | NULL         | <blank>      | 2014-07-31 11:48:38 |           51 |          128 | 2015-08-05 12:25:01 | <blank>       |            17 |              0 | 4f74a90344dcd90f1b4ee1daf4dd661f |              0 | 213.219.91.156  | 2014-04-01 12:43:43 |               1 | <blank>         | 213.219.91.156    | 2002-01-23 10:05:44 | 2002-01-23 10:05:44       |
| 124498 | 81ef06d0baa6c5f180b099693577c0be | <blank> | <blank> | IraPak@mail.ru           | NULL                                         |        0 |        1 | <blank>    | 81ef06d0baa6c5f180b099693577c0be | <blank>     | ira           | NULL         | <blank>      | 1970-01-01 04:00:00 |           53 |            1 | 2014-04-03 07:53:23 | <blank>       |             0 |              0 | 81ef06d0baa6c5f180b099693577c0be |              0 | <blank>         | 2014-04-01 12:43:43 |               1 | <blank>         | <blank>           | 2002-01-25 08:27:51 | 2002-01-25 08:27:51       |
```


## About final data
> - Total rows: 100649

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |    |    |-- id: string (nullable = true)
 |-- actuality: string (nullable = true)

```

### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |
| Ips | 0.66% |
| Accounts | 100.00% |
| Actuality | 100.00% |


### Data sample
```
| names            | emails                       | ips                                                                                          | accounts                                                                                                                                   | actuality   |
|:-----------------|:-----------------------------|:---------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Root']         | ['root@kuking.net']          | [Row(ip='88.208.45.9', date='18.09.2013')]                                                   | [Row(title='Kuking.net', link='https://kuking.net', login='root', password_hash='b864ea12ac7af1e9deaccb487228c6c7', id='1')]               | 19.03.2020  |
| ['Denis']        | ['denis@kuking.net']         | [Row(ip='195.92.70.130', date='01.04.2014'), Row(ip='195.92.70.130', date='20.11.2001')]     | [Row(title='Kuking.net', link='https://kuking.net', login='denis', password_hash='4a65071285f88b9a1cf40693a64a209e', id='124481')]         | 21.12.2021  |
| ['Maria']        | ['maria@kuking.net']         | [Row(ip='195.92.38.4', date='01.04.2014'), Row(ip='195.92.38.4', date='21.11.2001')]         | [Row(title='Kuking.net', link='https://kuking.net', login='Maria', password_hash='b3269a2e2ba82d4e8b89ab0001f5df86', id='124482')]         | 24.07.2015  |
| ['Dina']         | ['trushin@ufanet.ru']        | [Row(ip='81.30.207.166', date='01.04.2014'), Row(ip='81.30.207.166', date='22.11.2001')]     | [Row(title='Kuking.net', link='https://kuking.net', login='Dina', password_hash='e0018d7058c93fbb70da83e4ec7b1976', id='124483')]          | 03.04.2014  |
| ['Anna']         | ['vigi5@bezeqint.net']       | [Row(ip='212.179.204.211', date='01.04.2014'), Row(ip='212.179.204.211', date='22.11.2001')] | [Row(title='Kuking.net', link='https://kuking.net', login='Anna', password_hash='e0018d7058c93fbb70da83e4ec7b1976', id='124484')]          | 03.04.2014  |
| ['Yuripodolsky'] | ['yuri_podolsky@mail.ru']    |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='Yuri_Podolsky', password_hash='e0018d7058c93fbb70da83e4ec7b1976', id='124485')] | 03.04.2014  |
| ['Geka']         | ['genuaria_lav2001@mail.ru'] |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='geka', password_hash='e0018d7058c93fbb70da83e4ec7b1976', id='124486')]          | 03.04.2014  |
| ['Jul']          | ['jjullia@hotmail.com']      |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='Jul', password_hash='e0018d7058c93fbb70da83e4ec7b1976', id='124487')]           | 03.04.2014  |
| ['Dascha']       | ['laur_anja@hotmail.com']    | [Row(ip='194.118.89.218', date='01.04.2014'), Row(ip='194.118.89.218', date='03.12.2001')]   | [Row(title='Kuking.net', link='https://kuking.net', login='Dascha', password_hash='e0018d7058c93fbb70da83e4ec7b1976', id='124488')]        | 03.04.2014  |
| ['Lissa']        | ['lissa@r66.ru']             |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='LISSA', password_hash='e0018d7058c93fbb70da83e4ec7b1976', id='124489')]         | 03.04.2014  |
| ['Igorus']       | ['igorus@at-travel.ru']      |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='Igorus', password_hash='256e8dbd04f161b7a1369612e397f2f2', id='124490')]        | 17.11.2015  |
| ['Olga']         | ['olgas99@hotmail.com']      |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='olga', password_hash='e0018d7058c93fbb70da83e4ec7b1976', id='124491')]          | 03.04.2014  |
| ['Dewi']         | ['dewi@mail.ru']             |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='dewi', password_hash='81ef06d0baa6c5f180b099693577c0be', id='124492')]          | 03.04.2014  |
| ['Oksana']       | ['oksanulia@chat.ru']        |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='Oksana', password_hash='81ef06d0baa6c5f180b099693577c0be', id='124493')]        | 03.04.2014  |
| ['Sasha']        | ['nexorosho@yahoo.com']      |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='Sasha', password_hash='81ef06d0baa6c5f180b099693577c0be', id='124494')]         | 03.04.2014  |
| ['Impraimis']    | ['vlatamir@list.ru']         |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='impraimis', password_hash='81ef06d0baa6c5f180b099693577c0be', id='124495')]     | 03.04.2014  |
| ['Leshakruge']   | ['kruge@mailru.com']         | [Row(ip='213.33.245.182', date='01.04.2014'), Row(ip='213.33.245.182', date='12.01.2002')]   | [Row(title='Kuking.net', link='https://kuking.net', login='Lesha_Kruge', password_hash='81ef06d0baa6c5f180b099693577c0be', id='124496')]   | 03.04.2014  |
| ['Ufik']         | ['ufik9@yandex.ru']          | [Row(ip='213.219.91.156', date='01.04.2014'), Row(ip='213.219.91.156', date='23.01.2002')]   | [Row(title='Kuking.net', link='https://kuking.net', login='ufik', password_hash='4f74a90344dcd90f1b4ee1daf4dd661f', id='124497')]          | 05.08.2015  |
| ['Ira']          | ['irapak@mail.ru']           |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='ira', password_hash='81ef06d0baa6c5f180b099693577c0be', id='124498')]           | 03.04.2014  |
| ['Milk']         | ['milk@sochi.ru']            |                                                                                              | [Row(title='Kuking.net', link='https://kuking.net', login='milk', password_hash='81ef06d0baa6c5f180b099693577c0be', id='124500')]          | 03.04.2014  |
```