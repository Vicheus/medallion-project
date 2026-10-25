# Parsetron results

## About row data

> - File path: mydocuments36.ru.csv
> - Total rows: 25905

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- otep: string (nullable = true)
 |-- block: integer (nullable = true)
 |-- email: string (nullable = true)
 |-- otpKey: string (nullable = true)
 |-- params: string (nullable = true)
 |-- password: string (nullable = true)
 |-- username: string (nullable = true)
 |-- sendEmail: integer (nullable = true)
 |-- activation: string (nullable = true)
 |-- resetCount: integer (nullable = true)
 |-- registerDate: timestamp (nullable = true)
 |-- requireReset: integer (nullable = true)
 |-- lastResetTime: string (nullable = true)
 |-- lastvisitDate: timestamp (nullable = true)

```

### Data sample
```
|    id | name                           | otep   |   block | email                                           | otpKey   | params                                                                                                                             | password                                                     | username                              |   sendEmail | activation   |   resetCount | registerDate        |   requireReset | lastResetTime       | lastvisitDate       |
|------:|:-------------------------------|:-------|--------:|:------------------------------------------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|:--------------------------------------|------------:|:-------------|-------------:|:--------------------|---------------:|:--------------------|:--------------------|
| 13000 | Русина Светлана Ивановна       |        |       0 | svetlanayu-mfc@rambler.ru                       |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":""}                                       | $2y$10$9pCVOILtt3ocMXHkxZwAyu2DLpUlpAOSC37tSw2z8S5NLOuy2UNN6 | esia_c5c279b86bf89b329adf570855d7585c |           0 |              |            0 | 2016-10-06 07:44:45 |              0 | 0000-00-00 00:00:00 | 2022-04-08 09:38:29 |
| 13002 | Кочетов Илья Владимирович      |        |       0 | ilya.kochetov@gmail.com                         |          | {"queue":"","admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":""}                            | $2y$10$5MpAfOamLDOJpFs0//mUGuJkh.FRK5U912yt9at6JQL7YO3yCFCZC | esia_41a4abd45e4d3db0e9fb624ea96c8349 |           0 |              |            0 | 2016-10-06 07:48:55 |              0 | 0000-00-00 00:00:00 | 2022-02-21 07:44:28 |
| 13041 | Меркулов Игорь Николаевич      |        |       0 | igor.merculov7315@yandex.ru                     |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":"","queue":""}                            | $2y$10$Wzkn8SN44vi7/CU.IErh9uRQTpVJcmwNwndksHOW6Mu86m/DBGgHe | esia_c8b6e257dfc99551a4e9d3278ded873f |           0 |              |            0 | 2016-10-07 04:48:51 |              0 | 0000-00-00 00:00:00 | 2022-04-12 04:54:59 |
| 13066 | Колесников Василий Петрович    |        |       0 | kolesnikov-mfc@mail.ru                          |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":"","queue":""}                            | $2y$10$4MYlr7On.2aILjmEVL7yze1b/FnhiWKToj7zMCU6CgX38IJ6zsdbW | esia_83b258641f12a8fe8390624bc6362e6d |           0 |              |            0 | 2016-10-07 11:23:05 |              0 | 0000-00-00 00:00:00 | 2022-05-06 05:44:43 |
| 13067 | ШУЛЬЖЕНКО ИРИНА ГЕННАДЬЕВНА    |        |       0 | shulzhenko-i@mail.ru                            |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":""}                                       | $2y$10$KhWrRtao/17ZAnKKkccT7OBJiBgrLaHXTlaSAiUbs/SVejx51b3mS | esia_387b1a8396065e9026dbad6a34614ac5 |           0 |              |            0 | 2016-10-07 11:59:43 |              0 | 0000-00-00 00:00:00 | 2022-05-06 11:47:54 |
| 13071 | Меснянкина Светлана Сергеевна  |        |       0 | pchela-sv@list.ru                               |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":""}                                       | $2y$10$yuz4242xf5cHdawX1f0e/eMMn8sh1Nf9da30WvRg8X7mRMfhZrgaK | esia_c85d77cdceb339448bf2753e3fc175a4 |           0 |              |            0 | 2016-10-07 13:43:31 |              0 | 0000-00-00 00:00:00 | 2022-04-07 06:11:19 |
| 13074 | Меснянкина Светлана            |        |       0 | smesnyankina@govvrn.ru                          |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":"Europe\\/Moscow","jckuicolor":"#FFFFFF"} | $2y$10$Nb5eK./KFEHor52g.3XuWuSvliRGlwqBsRab2feTSxCRXZlfRoSmK | Smesnyankina                          |           0 |              |            0 | 2016-10-07 14:04:37 |              0 | 0000-00-00 00:00:00 | 2022-05-06 11:50:08 |
| 13079 | Богдалова Майя Камильевна      |        |       0 | mkbog@mail.ru                                   |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":"","queue":""}                            | $2y$10$AD9n2mtl2w/I2zqC.OL.OO0wqQrOXKMU5g9PNL9ztvA21P/6XNa4G | esia_bb412ed94f79a53c9d1738e5515c2beb |           0 |              |            0 | 2016-10-07 16:50:31 |              0 | 0000-00-00 00:00:00 | 2022-04-28 11:07:52 |
| 13118 | Сидоренко Ирина Владимировна   |        |       0 | b25b47728f31b3840894e6b700cf2ccb@madeup.esia.ru |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":"","queue":""}                            | $2y$10$eTe0sNwISap5Ozq8a3PWIO36P31TZsBRGA5aruxEnh2uyP4bgZe0a | esia_b25b47728f31b3840894e6b700cf2ccb |           0 |              |            0 | 2016-10-10 10:13:35 |              0 | 0000-00-00 00:00:00 | 2022-03-02 06:24:45 |
| 13121 | РОДЧЕНКОВ АНДРЕЙ НИКОЛАЕВИЧ    |        |       0 | rodandrvrn@yandex.ru                            |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":"","queue":""}                            | $2y$10$vB6N9dDwFl7xGnZHvZRGzOceYnPP9FIFFKjAZii9bdElSx58X0UJS | esia_66de2dc67ed1122baa8555f796033c88 |           0 |              |            0 | 2016-10-10 11:40:14 |              0 | 0000-00-00 00:00:00 | 2022-05-06 13:02:18 |
| 13157 | Машин Андрей Владимирович      |        |       0 | rembrande@hotmail.com                           |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":"","queue":""}                            | $2y$10$v5SwN7mMFTGQYfV/Aw0IBulP3XVbkxS1w1qFxz4jErs8HZP3flNIC | esia_b4a383c89891bd744a1a66e498e6ef4e |           0 |              |            0 | 2016-10-11 06:37:10 |              0 | 0000-00-00 00:00:00 | 2022-04-29 13:38:19 |
| 13164 | Шидловская Анна Владимировна   |        |       0 | A.shidlovskaya@govvrn.ru                        |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":"","queue":""}                            | $2y$10$Sm7EvRlIVdXdbhImgMG.dOlu3z0sAsGqPe/2Tb4vRSyx7mSB0g5m2 | esia_c7d5d2dafca4cc0613c77c19cf3b31f7 |           0 |              |            0 | 2016-10-11 07:44:35 |              0 | 0000-00-00 00:00:00 | 2022-05-07 11:04:54 |
| 13186 | ПИГАРЕВА ИРИНА ЕВГЕНЬЕВНА      |        |       0 | presh@mail.ru                                   |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":"","queue":""}                            | $2y$10$8VA1k4EfimrGaia16/53iOQc1otM0EzMcY92VUgRgxFIAk77cyqL. | esia_3283a2316f112e0f5e2f3da69845ca82 |           0 |              |            0 | 2016-10-11 11:50:00 |              0 | 0000-00-00 00:00:00 | 2022-03-25 10:49:10 |
| 13188 | СЕРГИЕНКО АНТОНИНА ГЕННАДЬЕВНА |        |       0 | antonina.s75@mail.ru                            |          | {"queue":""}                                                                                                                       | $2y$10$omHOMsMfwOOWwQKmdIiWUepmVREWLHI.r0ReU9uvIu7jrsJSjacv2 | esia_5a168a2189017bfe2f889ad671ef63a4 |           0 |              |            0 | 2016-10-11 12:14:58 |              0 | 0000-00-00 00:00:00 | 2022-04-27 13:44:29 |
| 13198 | Спирин Алексей Михайлович      |        |       0 | spirin-mfc@mail.ru                              |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":"","queue":""}                            | $2y$10$WBJVlA3RayxxS0meBOhNXu2B04SBWfZJhtILjiNNxPRew4p0yGn5S | esia_5298d402308e7d41c9fc69617a724f2a |           0 |              |            0 | 2016-10-11 15:17:07 |              0 | 0000-00-00 00:00:00 | 2022-05-05 15:45:04 |
| 13199 | Анисимова Светлана Сергеевна   |        |       0 | 250381@mail.ru                                  |          | {"queue":""}                                                                                                                       | $2y$10$3HW7E/HdR0uvHxhbxx0YR.jhUvYaCxOapaJuwaa201yAtIAuA5PTy | esia_fdc04bcf9416ad843bda1067e21ef600 |           0 |              |            0 | 2016-10-11 16:16:25 |              0 | 0000-00-00 00:00:00 | 2022-03-21 08:56:41 |
| 13213 | Собкалов Юрий Алексеевич       |        |       0 | sob071177@yandex.ru                             |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":""}                                       | $2y$10$p5pgyITt4rVdBKVplVkrGe.qtnNlpi24r5bPx7jqO4u5WHLu6Y8KC | esia_8aa9ceb1ad8d1d4bf9486f39a118b2d0 |           0 |              |            0 | 2016-10-12 06:30:42 |              0 | 0000-00-00 00:00:00 | 2022-04-25 08:02:57 |
| 13229 | Колесникова Ольга Ивановна     |        |       0 | 3cfbf08738e9e09a092de2aa6dd2dee5@madeup.esia.ru |          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":""}                                       | $2y$10$kmRfpUY3HSuMde2sy7LqSOcuChgrniZsp75Dhd7xm5iKAaiO6hq9C | esia_3cfbf08738e9e09a092de2aa6dd2dee5 |           0 |              |            0 | 2016-10-12 08:50:48 |              0 | 0000-00-00 00:00:00 | 2022-02-14 10:41:31 |
| 13240 | Плохих Ольга Николаевна        |        |       0 | o.plohih@yandex.ru                              |          | {"queue":""}                                                                                                                       | $2y$10$Fhe0EigdDXtyHYiX7N65pujC.hDlz0Iqjw.5XFBXhkY8SHynvxKFC | esia_9315c30209c3fb94f28b21e06197ad18 |           0 |              |            0 | 2016-10-12 12:23:49 |              0 | 0000-00-00 00:00:00 | 2022-05-06 08:08:07 |
| 13241 | Кабанцов Олег Иванович         |        |       0 | olegvrn@yandex.ru                               |          | {"queue":""}                                                                                                                       | $2y$10$UtQRmNj9R.GI/fUjoxUxs.PQzMn.9q1gPg/2fdkryiqGbkHazXjJ6 | esia_3417d2da5e9198b63a164f510378a24b |           0 |              |            0 | 2016-10-12 12:54:56 |              0 | 0000-00-00 00:00:00 | 2022-02-04 08:11:45 |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- actuality: date (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |
| Accounts | 100.00% |
| Actuality | 100.00% |



### Data sample
```
| names                              | emails                                              | accounts                                                                                                                                                                                      | actuality   |
|:-----------------------------------|:----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Русина Светлана Ивановна']       | ['svetlanayu-mfc@rambler.ru']                       | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_c5c279b86bf89b329adf570855d7585c', password_hash='$2y$10$9pCVOILtt3ocMXHkxZwAyu2DLpUlpAOSC37tSw2z8S5NLOuy2UNN6')] | 08.04.2022  |
| ['Кочетов Илья Владимирович']      | ['ilya.kochetov@gmail.com']                         | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_41a4abd45e4d3db0e9fb624ea96c8349', password_hash='$2y$10$5MpAfOamLDOJpFs0//mUGuJkh.FRK5U912yt9at6JQL7YO3yCFCZC')] | 21.02.2022  |
| ['Меркулов Игорь Николаевич']      | ['igor.merculov7315@yandex.ru']                     | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_c8b6e257dfc99551a4e9d3278ded873f', password_hash='$2y$10$Wzkn8SN44vi7/CU.IErh9uRQTpVJcmwNwndksHOW6Mu86m/DBGgHe')] | 12.04.2022  |
| ['Колесников Василий Петрович']    | ['kolesnikov-mfc@mail.ru']                          | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_83b258641f12a8fe8390624bc6362e6d', password_hash='$2y$10$4MYlr7On.2aILjmEVL7yze1b/FnhiWKToj7zMCU6CgX38IJ6zsdbW')] | 06.05.2022  |
| ['Шульженко Ирина Геннадьевна']    | ['shulzhenko-i@mail.ru']                            | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_387b1a8396065e9026dbad6a34614ac5', password_hash='$2y$10$KhWrRtao/17ZAnKKkccT7OBJiBgrLaHXTlaSAiUbs/SVejx51b3mS')] | 06.05.2022  |
| ['Меснянкина Светлана Сергеевна']  | ['pchela-sv@list.ru']                               | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_c85d77cdceb339448bf2753e3fc175a4', password_hash='$2y$10$yuz4242xf5cHdawX1f0e/eMMn8sh1Nf9da30WvRg8X7mRMfhZrgaK')] | 07.04.2022  |
| ['Меснянкина Светлана']            | ['smesnyankina@govvrn.ru']                          | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='Smesnyankina', password_hash='$2y$10$Nb5eK./KFEHor52g.3XuWuSvliRGlwqBsRab2feTSxCRXZlfRoSmK')]                          | 06.05.2022  |
| ['Богдалова Майя Камильевна']      | ['mkbog@mail.ru']                                   | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_bb412ed94f79a53c9d1738e5515c2beb', password_hash='$2y$10$AD9n2mtl2w/I2zqC.OL.OO0wqQrOXKMU5g9PNL9ztvA21P/6XNa4G')] | 28.04.2022  |
| ['Сидоренко Ирина Владимировна']   | ['b25b47728f31b3840894e6b700cf2ccb@madeup.esia.ru'] | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_b25b47728f31b3840894e6b700cf2ccb', password_hash='$2y$10$eTe0sNwISap5Ozq8a3PWIO36P31TZsBRGA5aruxEnh2uyP4bgZe0a')] | 02.03.2022  |
| ['Родченков Андрей Николаевич']    | ['rodandrvrn@yandex.ru']                            | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_66de2dc67ed1122baa8555f796033c88', password_hash='$2y$10$vB6N9dDwFl7xGnZHvZRGzOceYnPP9FIFFKjAZii9bdElSx58X0UJS')] | 06.05.2022  |
| ['Машин Андрей Владимирович']      | ['rembrande@hotmail.com']                           | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_b4a383c89891bd744a1a66e498e6ef4e', password_hash='$2y$10$v5SwN7mMFTGQYfV/Aw0IBulP3XVbkxS1w1qFxz4jErs8HZP3flNIC')] | 29.04.2022  |
| ['Шидловская Анна Владимировна']   | ['a.shidlovskaya@govvrn.ru']                        | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_c7d5d2dafca4cc0613c77c19cf3b31f7', password_hash='$2y$10$Sm7EvRlIVdXdbhImgMG.dOlu3z0sAsGqPe/2Tb4vRSyx7mSB0g5m2')] | 07.05.2022  |
| ['Пигарева Ирина Евгеньевна']      | ['presh@mail.ru']                                   | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_3283a2316f112e0f5e2f3da69845ca82', password_hash='$2y$10$8VA1k4EfimrGaia16/53iOQc1otM0EzMcY92VUgRgxFIAk77cyqL.')] | 25.03.2022  |
| ['Сергиенко Антонина Геннадьевна'] | ['antonina.s75@mail.ru']                            | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_5a168a2189017bfe2f889ad671ef63a4', password_hash='$2y$10$omHOMsMfwOOWwQKmdIiWUepmVREWLHI.r0ReU9uvIu7jrsJSjacv2')] | 27.04.2022  |
| ['Спирин Алексей Михайлович']      | ['spirin-mfc@mail.ru']                              | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_5298d402308e7d41c9fc69617a724f2a', password_hash='$2y$10$WBJVlA3RayxxS0meBOhNXu2B04SBWfZJhtILjiNNxPRew4p0yGn5S')] | 05.05.2022  |
| ['Анисимова Светлана Сергеевна']   | ['250381@mail.ru']                                  | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_fdc04bcf9416ad843bda1067e21ef600', password_hash='$2y$10$3HW7E/HdR0uvHxhbxx0YR.jhUvYaCxOapaJuwaa201yAtIAuA5PTy')] | 21.03.2022  |
| ['Собкалов Юрий Алексеевич']       | ['sob071177@yandex.ru']                             | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_8aa9ceb1ad8d1d4bf9486f39a118b2d0', password_hash='$2y$10$p5pgyITt4rVdBKVplVkrGe.qtnNlpi24r5bPx7jqO4u5WHLu6Y8KC')] | 25.04.2022  |
| ['Колесникова Ольга Ивановна']     | ['3cfbf08738e9e09a092de2aa6dd2dee5@madeup.esia.ru'] | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_3cfbf08738e9e09a092de2aa6dd2dee5', password_hash='$2y$10$kmRfpUY3HSuMde2sy7LqSOcuChgrniZsp75Dhd7xm5iKAaiO6hq9C')] | 14.02.2022  |
| ['Плохих Ольга Николаевна']        | ['o.plohih@yandex.ru']                              | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_9315c30209c3fb94f28b21e06197ad18', password_hash='$2y$10$Fhe0EigdDXtyHYiX7N65pujC.hDlz0Iqjw.5XFBXhkY8SHynvxKFC')] | 06.05.2022  |
| ['Кабанцов Олег Иванович']         | ['olegvrn@yandex.ru']                               | [Row(title='mydocuments36.ru', link='https://mydocuments36.ru', login='esia_3417d2da5e9198b63a164f510378a24b', password_hash='$2y$10$UtQRmNj9R.GI/fUjoxUxs.PQzMn.9q1gPg/2fdkryiqGbkHazXjJ6')] | 04.02.2022  |
```