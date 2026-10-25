# Parsetron results

## About row data

> - Code name: index_0144
> - File path: naftusia_preprocessed_2.csv
> - Total rows: 1293

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- TIMESTAMP_X: timestamp (nullable = true)
 |-- LOGIN: string (nullable = true)
 |-- PASSWORD: string (nullable = true)
 |-- CHECKWORD: string (nullable = true)
 |-- ACTIVE: string (nullable = true)
 |-- NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- LAST_LOGIN: timestamp (nullable = true)
 |-- DATE_REGISTER: timestamp (nullable = true)
 |-- LID: string (nullable = true)
 |-- PERSONAL_PROFESSION: string (nullable = true)
 |-- PERSONAL_WWW: string (nullable = true)
 |-- PERSONAL_ICQ: string (nullable = true)
 |-- PERSONAL_GENDER: string (nullable = true)
 |-- PERSONAL_BIRTHDATE: string (nullable = true)
 |-- PERSONAL_PHOTO: integer (nullable = true)
 |-- PERSONAL_PHONE: string (nullable = true)
 |-- PERSONAL_FAX: string (nullable = true)
 |-- PERSONAL_MOBILE: string (nullable = true)
 |-- PERSONAL_PAGER: string (nullable = true)
 |-- PERSONAL_STREET: string (nullable = true)
 |-- PERSONAL_MAILBOX: string (nullable = true)
 |-- PERSONAL_CITY: string (nullable = true)
 |-- PERSONAL_STATE: string (nullable = true)
 |-- PERSONAL_ZIP: string (nullable = true)
 |-- PERSONAL_COUNTRY: integer (nullable = true)
 |-- PERSONAL_NOTES: string (nullable = true)
 |-- WORK_COMPANY: string (nullable = true)
 |-- WORK_DEPARTMENT: string (nullable = true)
 |-- WORK_POSITION: string (nullable = true)
 |-- WORK_WWW: string (nullable = true)
 |-- WORK_PHONE: string (nullable = true)
 |-- WORK_FAX: string (nullable = true)
 |-- WORK_PAGER: string (nullable = true)
 |-- WORK_STREET: string (nullable = true)
 |-- WORK_MAILBOX: string (nullable = true)
 |-- WORK_CITY: string (nullable = true)
 |-- WORK_STATE: string (nullable = true)
 |-- WORK_ZIP: string (nullable = true)
 |-- WORK_COUNTRY: integer (nullable = true)
 |-- WORK_PROFILE: string (nullable = true)
 |-- WORK_LOGO: string (nullable = true)
 |-- WORK_NOTES: string (nullable = true)
 |-- ADMIN_NOTES: string (nullable = true)
 |-- STORED_HASH: string (nullable = true)
 |-- XML_ID: string (nullable = true)
 |-- PERSONAL_BIRTHDAY: date (nullable = true)
 |-- EXTERNAL_AUTH_ID: string (nullable = true)
 |-- CHECKWORD_TIME: timestamp (nullable = true)
 |-- SECOND_NAME: string (nullable = true)
 |-- CONFIRM_CODE: string (nullable = true)
 |-- LOGIN_ATTEMPTS: integer (nullable = true)
 |-- LAST_ACTIVITY_DATE: timestamp (nullable = true)
 |-- AUTO_TIME_ZONE: string (nullable = true)
 |-- TIME_ZONE: string (nullable = true)
 |-- TIME_ZONE_OFFSET: string (nullable = true)
 |-- TITLE: string (nullable = true)
 |-- BX_USER_ID: string (nullable = true)
 |-- LANGUAGE_ID: string (nullable = true)

```

### Data sample
```
|   ID | TIMESTAMP_X         | LOGIN                            | PASSWORD                                 | CHECKWORD                                | ACTIVE   | NAME      | LAST_NAME   | EMAIL                     | LAST_LOGIN          | DATE_REGISTER       | LID   | PERSONAL_PROFESSION   | PERSONAL_WWW                            | PERSONAL_ICQ   | PERSONAL_GENDER   | PERSONAL_BIRTHDATE   |   PERSONAL_PHOTO | PERSONAL_PHONE   | PERSONAL_FAX   | PERSONAL_MOBILE   | PERSONAL_PAGER   | PERSONAL_STREET   | PERSONAL_MAILBOX   | PERSONAL_CITY   | PERSONAL_STATE   | PERSONAL_ZIP   |   PERSONAL_COUNTRY | PERSONAL_NOTES   | WORK_COMPANY   | WORK_DEPARTMENT   | WORK_POSITION   | WORK_WWW   | WORK_PHONE   | WORK_FAX   | WORK_PAGER   | WORK_STREET   | WORK_MAILBOX   | WORK_CITY   | WORK_STATE   | WORK_ZIP   |   WORK_COUNTRY | WORK_PROFILE   | WORK_LOGO   | WORK_NOTES   | ADMIN_NOTES   | STORED_HASH   | XML_ID                                  | PERSONAL_BIRTHDAY   | EXTERNAL_AUTH_ID   | CHECKWORD_TIME      | SECOND_NAME   | CONFIRM_CODE   |   LOGIN_ATTEMPTS | LAST_ACTIVITY_DATE   | AUTO_TIME_ZONE   | TIME_ZONE   | TIME_ZONE_OFFSET   | TITLE   | BX_USER_ID                       | LANGUAGE_ID   |
|-----:|:--------------------|:---------------------------------|:-----------------------------------------|:-----------------------------------------|:---------|:----------|:------------|:--------------------------|:--------------------|:--------------------|:------|:----------------------|:----------------------------------------|:---------------|:------------------|:---------------------|-----------------:|:-----------------|:---------------|:------------------|:-----------------|:------------------|:-------------------|:----------------|:-----------------|:---------------|-------------------:|:-----------------|:---------------|:------------------|:----------------|:-----------|:-------------|:-----------|:-------------|:--------------|:---------------|:------------|:-------------|:-----------|---------------:|:---------------|:------------|:-------------|:--------------|:--------------|:----------------------------------------|:--------------------|:-------------------|:--------------------|:--------------|:---------------|-----------------:|:---------------------|:-----------------|:------------|:-------------------|:--------|:---------------------------------|:--------------|
|    1 | 2018-01-02 22:39:24 | a.kozelski@ya.ru                 | 0l|GW~b51dec34df813cf374293444ebc592fc20 | 4IPdKTAr4e44c12f689f4aa875c41cf4589ee086 | Y        | Андрей    | Козельский  | schaos@yandex.ru          | 2023-05-02 11:03:08 | 2014-04-21 13:28:04 | s2    |                       |                                         |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |                                         |                     |                    | 2017-05-13 11:09:56 |               |                |                0 | 2014-04-25 15:18:09  |                  |             |                    |         |                                  |               |
|    2 | 2024-05-09 15:17:12 | siteadmin                        | Ho~4R[7o4246e1ba339694903a0bba973a8eb73a | EHhpzZsyee368a0111bd637207a8e2e103074655 | Y        |           |             | administrator@naftusia.ru | 2024-05-09 15:17:12 | 2014-04-28 13:12:00 | s2    |                       |                                         |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |                                         |                     |                    | 2023-11-09 11:15:18 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|    3 | 2024-05-15 12:38:17 | manager                          | jP?10D#v077b5499f2f0148eaa69a3cdb20e1f34 | q3nlrAXw8786fb3fdd6c1f7b0e8b1d7ed88f79b1 | Y        |           |             | manager@naftusya.tk       | 2024-05-13 23:05:48 | 2014-05-06 11:05:12 | s1    |                       |                                         |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |                                         |                     |                    | 2024-04-23 20:08:54 |               |                |                1 | NaT                  |                  |             |                    |         | 36af290a6e8608a72f7a104cb93a0a89 |               |
|    4 | 2015-11-17 16:37:19 | Andrew                           | wDU1ZDYy18620ef40a2f095173b91d225d27346f | 3RnWh5H344fcd87c1ea98334f43c6934a3f03edc | Y        |           |             | a.kozelski@ya.ru          | 2014-05-14 16:03:15 | 2014-05-14 16:03:15 | s2    |                       |                                         |                |                   |                      |              nan | 898800000001     |                |                   |                  |                   |                    | город мой       |                  |                |                 17 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-06-27 02:06:47 |               |                |                1 | NaT                  |                  |             |                    |         |                                  |               |
|    5 | 2014-06-10 22:54:45 | openid.mail.ru/mail/vploskodnjak | GTENZrpD59d3aa55b5d1bc8bd676ba9eb49518e9 | 9mHNkcIn8241153267d9e5fecf6d7ae42f4b0525 | Y        | Вера      | Плоскодняк  | vploskodnjak@mail.ru      | 2014-06-11 00:12:56 | 2014-06-10 23:54:45 | s1    |                       | http://openid.mail.ru/mail/vploskodnjak |                | F                 |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               | http://openid.mail.ru/mail/vploskodnjak |                     | socservices        | 2014-06-10 23:54:45 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|    6 | 2014-06-13 08:00:21 | rsamedov@mail.ru                 | 5DryeFvD1dd092eb34059123cf83df21938b0b57 | yhuBvgGr975e355a80d0542aaa83c4e204d69fba | Y        | Rashad    | Samadov     | rsamedov@mail.ru          | 2014-06-13 09:00:21 | 2014-06-13 09:00:21 | s2    |                       |                                         |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-06-13 09:00:21 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|    7 | 2014-06-16 09:38:32 | Faotina                          | eJjmI7aO8e02bfa4a7b52126ded35a87ed741c0a | X1pXz2ra6f48163c342a0a28392eae640c7b9cbc | Y        |           |             | faotinakirik54@mail.ru    | 2014-06-16 10:38:32 | 2014-06-16 10:38:32 | s2    |                       |                                         |                |                   |                      |              nan | 8-961-135-96-54  |                |                   |                  |                   |                    | Смоленск        |                  |                |                  1 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-06-16 10:38:32 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|    8 | 2014-06-16 13:07:40 | RyazancevG@yandex.ru             | R5wHoIOh36032a05874f8327153dcc422a4fca27 | RPXu4KYMa232b24f57feac99d119dd8119a45b56 | Y        | Олег      | Рязанцев    | ryazancevg@yandex.ru      | 2014-06-16 14:07:40 | 2014-06-16 14:07:40 | s2    |                       |                                         |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-06-16 14:07:40 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|    9 | 2014-06-16 13:57:26 | alexsandr_65@mail.ru             | 0LR3XspL41d3ff7f25594d73a21f3d36b799db7d | sawc6Q8y8acff0c3062bf89cd154a01038c26ef3 | Y        | Александр | Андриященко | alexsandr_65@mail.ru      | 2014-06-16 14:57:26 | 2014-06-16 14:57:26 | s2    |                       |                                         |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-06-16 14:57:26 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|   10 | 2024-01-13 04:30:54 | guest                            | DEy8htX128e95be3b6a1df62bde39d7489b58e2e | yzfRGLkN2586439c1d0aba40190f4aed2608a96c | Y        |           |             | guest@naftisua.ru         | NaT                 | 2014-06-21 17:45:37 | s2    |                       |                                         |                |                   |                      |              nan |                  |                |                   |                  |                   |                    |                 |                  |                |                  0 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |                                         |                     |                    | 2014-06-21 17:49:54 |               |                |              124 | NaT                  |                  |             |                    |         |                                  |               |
|   11 | 2014-06-27 22:27:48 | lootme                           | d1I%wX1^0520ee5b1ec92c105dcad9ff7603fb72 | OfpHqOps6a4839b6eca6f1dc967ff4ac0f87c2dc | Y        |           |             | a.kozelski@ya.ru          | 2014-06-30 11:30:57 | 2014-06-23 15:42:25 | s2    |                       |                                         |                |                   |                      |             5667 | 89885649475      |                |                   |                  |                   |                    | Ростов          |                  |                |                105 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |              0 |                |             |              |               |               |                                         |                     |                    | 2014-06-27 02:14:27 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|   12 | 2014-06-26 23:51:28 | VKuser7874889                    | eQh2ihWDed876f5d3f1840e89ae143e3e2e899f3 | 8qLkUedm24eca90091c48f677c1fc98d5861fb56 | Y        | Andrey    | Kozelski    |                           | 2014-06-27 13:06:30 | 2014-06-27 00:51:28 | s2    |                       | http://vk.com/id7874889                 |                | M                 |                      |             5455 |                  |                |                   |                  |                   |                    |                 |                  |                |                nan |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               | 7874889                                 | 1990-01-05          | socservices        | 2014-06-27 00:51:28 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|   13 | 2014-07-14 15:18:07 | platibit                         | FseXaRI124b8dec74b75e3ca6849f194e313f6f9 | 8J0Iyrrt23aea6e2253afbc690f51b1bcc5ddd20 | Y        |           |             | platimn@gmail.com         | 2014-07-14 16:18:07 | 2014-06-27 01:33:56 | s2    |                       |                                         |                |                   |                      |              nan | 123456           |                |                   |                  |                   |                    | Ndenga          |                  |                |                124 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-06-27 01:33:56 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|   14 | 2014-06-27 14:04:31 | rukawar                          | SE0uBfZb56e06aa87f3e470397732c7424f0e859 | nUmpOvO8eec225af80308c3aaeaaa0a98e93249e | Y        |           |             | odnorukiy@list.ru         | 2014-06-27 15:04:31 | 2014-06-27 15:04:30 | s2    |                       |                                         |                |                   |                      |              nan | 8(926)5938440    |                |                   |                  |                   |                    | Москва          |                  |                |                  1 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-06-27 15:04:30 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|   15 | 2014-07-07 02:59:00 | Williammupe                      | pgYyDD821632c44ae1337ed08eaacea9958847c0 | h9QDOcj25bb37fd19b79ceb1a1018c3d5ce3d8e5 | Y        |           |             | adam_asnyk@aol.com        | 2014-07-07 03:59:00 | 2014-07-07 03:58:55 | s2    |                       |                                         |                |                   |                      |              nan | 123456           |                |                   |                  |                   |                    | Sanaa           |                  |                |                 60 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-07-07 03:58:55 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|   16 | 2014-07-08 01:07:14 | VikaVirtbuh                      | C2zbq3Zga9dc1d84886d29c91579ca48992a0865 | MhYkVEec1655137b05bf2577f7449a0870c095ee | Y        |           |             | vikahotxxx@mail.ru        | 2014-07-08 02:07:14 | 2014-07-08 02:07:10 | s2    |                       |                                         |                |                   |                      |              nan | 123456           |                |                   |                  |                   |                    | Кувандык        |                  |                |                 25 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-07-08 02:07:10 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|   17 | 2014-07-10 16:02:43 | HorstmannWQ                      | syb2lxtA37c702f31e9fce47bb746dbfcf6b70b4 | VklwKye9dc3eeea54c62f06d0c8b5952a9ec8791 | Y        |           |             | mcfarlanrr@gmail.com      | 2014-07-10 17:02:43 | 2014-07-10 17:02:37 | s2    |                       |                                         |                |                   |                      |              nan | 123456           |                |                   |                  |                   |                    |                 |                  |                |                187 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-07-10 17:02:37 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|   18 | 2014-07-17 00:39:20 | MiguelReoF                       | RKyZJWbCb02d5da37e95d9640951c13d5a16834c | XBf5WGbR2f2400c464aa6942b41a96f68947d611 | Y        |           |             | miguelwani@outlook.com    | 2014-07-17 01:39:20 | 2014-07-17 01:39:13 | s2    |                       |                                         |                |                   |                      |              nan | 123456           |                |                   |                  |                   |                    | Parnu           |                  |                |                194 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-07-17 01:39:13 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|   19 | 2014-07-19 06:46:30 | Edmondpese                       | YysXWkY593a83f44b614cdcdf22fe4dacd2d6bb7 | wF3OahGTaca87d73c7f991e5d981d83e0efa3c80 | Y        |           |             | edmondhit2014@yandex.ru   | 2014-07-19 07:46:30 | 2014-07-19 07:46:22 | s2    |                       |                                         |                |                   |                      |              nan | 123456           |                |                   |                  |                   |                    | Gliwice         |                  |                |                 86 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-07-19 07:46:22 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
|   20 | 2014-07-22 20:00:34 | durestehort                      | IZnKZOtt2971a1a3e6085324aa8fe309b80dbde3 | eEmifvZO5978765b91905bf0c8ea3deef2f39d5f | Y        |           |             | marcinejohwad@gmail.com   | 2014-07-22 21:00:34 | 2014-07-22 21:00:32 | s2    |                       |                                         |                |                   |                      |              nan | 123456           |                |                   |                  |                   |                    | Paris           |                  |                |                  8 |                  |                |                   |                 |            |              |            |              |               |                |             |              |            |            nan |                |             |              |               |               |                                         |                     |                    | 2014-07-22 21:00:32 |               |                |                0 | NaT                  |                  |             |                    |         |                                  |               |
```

> - Code name: index_0144
> - File path: naftusia_preprocessed.csv
> - Total rows: 2316

### Schema
```
root
 |-- PHONE: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- FIO: string (nullable = true)
 |-- PERSONAL_COUNTRY: string (nullable = true)
 |-- PERSONAL_CITY: string (nullable = true)
 |-- RELATED_PERSON_1: string (nullable = true)
 |-- RELATED_PERSON_2: string (nullable = true)
 |-- RELATED_PERSON_3: string (nullable = true)
 |-- RELATED_PERSON_4: string (nullable = true)
 |-- RELATED_PERSON_5: string (nullable = true)

```

### Data sample
```
| PHONE                   | EMAIL                    | FIO                             | PERSONAL_COUNTRY   | PERSONAL_CITY       | RELATED_PERSON_1           | RELATED_PERSON_2   | RELATED_PERSON_3   | RELATED_PERSON_4   | RELATED_PERSON_5   |
|:------------------------|:-------------------------|:--------------------------------|:-------------------|:--------------------|:---------------------------|:-------------------|:-------------------|:-------------------|:-------------------|
| +79037683755            | ansti@rambler.ru         | Панасевич Лидия Петровна        | Россия             | Москва              | Панасевич Виктор Сергеевич |                    |                    |                    |                    |
| Страна: Россия          |                          |                                 |                    |                     |                            |                    |                    |                    |                    |
| Город: Москва           |                          |                                 |                    |                     |                            |                    |                    |                    |                    |
| Телефон:                |                          |                                 |                    |                     |                            |                    |                    |                    |                    |
| Email: ansti@rambler.ru |                          |                                 |                    |                     |                            |                    |                    |                    |                    |
| ,,,,                    |                          |                                 |                    |                     |                            |                    |                    |                    |                    |
| 8 962 948 24 37         | stenov1@yandex.ru        | Коровина Наталья Григорьевна    | Россия             | Ржев                |                            |                    |                    |                    |                    |
| 79165670066             | lvbnhb@mail.ru           | Полухин Дмитрий Леонидович      | Россия             | Москва              |                            |                    |                    |                    |                    |
| 8-906-787-70-71         | dudnikova@land.ru        | Дудникова Ирина Константиновна  | Россия             | Солнечногорский р-н |                            |                    |                    |                    |                    |
| 89204510520             |                          | Удодов Александр Николаевич     | россия             | воронеж             |                            |                    |                    |                    |                    |
| 89629925370             |                          | Есарева Юлия Владимировна       | Россия             | Москва              |                            |                    |                    |                    |                    |
| 8-916-195-91-43         | guselaleksandr@yandex.ru | Гусельников Александр Андреевич | Россия             | Москва              |                            |                    |                    |                    |                    |
| 89151423652             |                          | Сарычев Виталий Алексеевич      | Россия             | Москва              |                            |                    |                    |                    |                    |
| 8 9252287762            |                          | Дурягина Валентина Аркадьевна   | Россия             | Жуковский           |                            |                    |                    |                    |                    |
| 89262735870             |                          | Астапенко Валентина Петровна    | россия             | москва              |                            |                    |                    |                    |                    |
| +7 916 336 9451         |                          | Вадим Владимирович              | Россия             | Москва              |                            |                    |                    |                    |                    |
| 79166235344             | 210654@bk.ru             | Мищенко Виктор Юрьевич          | Россия             | Железнодорожный     | Мищенко Тамара Евгеньевна  |                    |                    |                    |                    |
| Страна: Россия          |                          |                                 |                    |                     |                            |                    |                    |                    |                    |
| Город: Железнодорожный  |                          |                                 |                    |                     |                            |                    |                    |                    |                    |
| Телефон: 79166235344    |                          |                                 |                    |                     |                            |                    |                    |                    |                    |
```


## About final data
> - Total rows: 1383

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
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |    |    |-- id: string (nullable = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- relations: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 74.69% |
| Phones | 97.90% |
| Sex | 0.29% |
| Birth_date | 0.00% |
| Address | 98.99% |
| Accounts | 0.72% |
| Works | 0.00% |
| Relations | 23.28% |
| Socials | 0.22% |
| Actuality | 0.72% |



### Data sample
```
| names                              | emails                          | phones          |   sex | birth_date   | address             | accounts                                                                                                                                                            | works   | relations                     | socials                                                    | actuality   |
|:-----------------------------------|:--------------------------------|:----------------|------:|:-------------|:--------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|:------------------------------|:-----------------------------------------------------------|:------------|
| ['Григорьева Елена']               | ['alena.grig@yandex.ru']        |                 |     0 |              |                     | [Row(title='НАФТУСЯ ТУР', link='https://naftusia.com', login='VKuser160010651', password_hash='DBwTMtJnc6697db943fb2d5b8194c21f87f8cd13', id='162')]                |         |                               | [Row(title='Vk', id='160010651', link=None, comment=None)] | 25.05.2015  |
| ['Auvarl Auvarl']                  | ['andreschestakov@yandex.ru']   |                 |   nan |              |                     | [Row(title='НАФТУСЯ ТУР', link='https://naftusia.com', login='andreschestakov@yandex.ru', password_hash='UcS1ZQRv3a746f951ff48ec89ad11b8a2afdfbe8', id='26')]       |         |                               |                                                            | 01.08.2014  |
| ['Козельский Андрей']              | ['schaos@yandex.ru']            |                 |   nan |              |                     | [Row(title='НАФТУСЯ ТУР', link='https://naftusia.com', login='a.kozelski@ya.ru', password_hash='0l|GW~b51dec34df813cf374293444ebc592fc20', id='1')]                 |         |                               |                                                            | 02.05.2023  |
| ['Николаевна Вера']                | ['wnw35@rambler.ru']            |                 |     0 |              |                     | [Row(title='НАФТУСЯ ТУР', link='https://naftusia.com', login='VKuser50438774', password_hash='GzrTNPJy6cbca62a9a98a45339a5b8564d243dae', id='185')]                 |         |                               | [Row(title='Vk', id='50438774', link=None, comment=None)]  | 08.07.2015  |
| ['Samadov Rashad']                 | ['rsamedov@mail.ru']            |                 |   nan |              |                     | [Row(title='НАФТУСЯ ТУР', link='https://naftusia.com', login='rsamedov@mail.ru', password_hash='5DryeFvD1dd092eb34059123cf83df21938b0b57', id='6')]                 |         |                               |                                                            | 13.06.2014  |
| ['Андриященко Александр']          | ['alexsandr_65@mail.ru']        |                 |   nan |              |                     | [Row(title='НАФТУСЯ ТУР', link='https://naftusia.com', login='alexsandr_65@mail.ru', password_hash='0LR3XspL41d3ff7f25594d73a21f3d36b799db7d', id='9')]             |         |                               |                                                            | 16.06.2014  |
| ['Пономарев Сергей']               | ['silwersky@gmail.com']         |                 |   nan |              |                     | [Row(title='НАФТУСЯ ТУР', link='https://naftusia.com', login='webmaster', password_hash='Y0.yMt3*95d6264f2b53851b7fca77f76e259fe6', id='134')]                      |         |                               |                                                            | 04.05.2017  |
| ['Плоскодняк Вера']                | ['vploskodnjak@mail.ru']        |                 |     0 |              |                     | [Row(title='НАФТУСЯ ТУР', link='https://naftusia.com', login='openid.mail.ru/mail/vploskodnjak', password_hash='GTENZrpD59d3aa55b5d1bc8bd676ba9eb49518e9', id='5')] |         |                               |                                                            | 11.06.2014  |
| ['Kozelski Andrey']                |                                 |                 |     1 |              |                     | [Row(title='НАФТУСЯ ТУР', link='https://naftusia.com', login='VKuser7874889', password_hash='eQh2ihWDed876f5d3f1840e89ae143e3e2e899f3', id='12')]                   |         |                               | [Row(title='Vk', id='7874889', link=None, comment=None)]   | 27.06.2014  |
| ['Рязанцев Олег']                  | ['ryazancevg@yandex.ru']        |                 |   nan |              |                     | [Row(title='НАФТУСЯ ТУР', link='https://naftusia.com', login='RyazancevG@yandex.ru', password_hash='R5wHoIOh36032a05874f8327153dcc422a4fca27', id='8')]             |         |                               |                                                            | 16.06.2014  |
| ['Бокова Наталья Александровна']   | ['bkvanat@rambler.ru']          | ['79035881955'] |   nan |              | ['Москва']          |                                                                                                                                                                     |         |                               |                                                            |             |
| ['Матюшина Елена Васильевна']      |                                 | ['79267632148'] |   nan |              | ['Москва']          |                                                                                                                                                                     |         |                               |                                                            |             |
| ['Халмурзаева Валентина Ивановна'] | ['malinochka-81@mail.ru']       | ['79217585125'] |   nan |              | ['Санкт-Петербург'] |                                                                                                                                                                     |         |                               |                                                            |             |
| ['Блиндер Елена Евгеньевна']       | ['elena-sazanovich@yanlex.ru']  | ['79175181544'] |   nan |              | ['Подольск']        |                                                                                                                                                                     |         | ['Блиндер Игорь Наумович']    |                                                            |             |
| ['Спивак Инна Васильевна']         | ['spivakinna@mail.ru']          | ['79202283510'] |   nan |              | ['Воронеж']         |                                                                                                                                                                     |         |                               |                                                            |             |
| ['Смирнова Елена Александровна']   | ['elena-smirnova-1969@mail.ru'] | ['79044752624'] |   nan |              | ['Лабытнанги']      |                                                                                                                                                                     |         |                               |                                                            |             |
| ['Анисов Дмитрий Павлович']        | ['lacrimosa192@mail.ru']        | ['79670946189'] |   nan |              | ['Москва']          |                                                                                                                                                                     |         |                               |                                                            |             |
| ['Голышкина Людмила Петровна']     | ['l.golyshkina@mail.ru']        | ['79629047141'] |   nan |              | ['Москва']          |                                                                                                                                                                     |         |                               |                                                            |             |
| ['Фомичева Прасковья Егоровна']    | ['79152604176@yandex.ru']       | ['79152604176'] |   nan |              | ['Москва']          |                                                                                                                                                                     |         | ['Балакина Лидия Николаевна'] |                                                            |             |
| ['Александрова Ольга Николаевна']  | ['alexand-olga@yandex.ru']      | ['79212213695'] |   nan |              | ['Петрозаводск']    |                                                                                                                                                                     |         |                               |                                                            |             |
```