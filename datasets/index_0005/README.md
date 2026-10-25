# Parsetron results

## About row data

> - Code name: index_0005
> - File path: /home/user/Documents/data/index_0005/raw/adengi.ru_23.02.2024_6,8M/clients_adengi.ru.csv
> - Total rows: 6697527

### Schema
```
root
 |-- user_id: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- password_hash: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- address: string (nullable = true)
 |-- source: string (nullable = true)
 |-- not_identified_column_1: string (nullable = true)
 |-- metric: string (nullable = true)
 |-- not_identified_column_2: string (nullable = true)
 |-- not_identified_column_3: string (nullable = true)
 |-- created_at: string (nullable = true)
 |-- updated_at: string (nullable = true)

```

### Data sample
```
|   user_id | first_name   | last_name   | middle_name   | email                         |       phone | password_hash                                                | gender   | birth_date   | address                                                                    | source    | not_identified_column_1   |      metric | not_identified_column_2   | not_identified_column_3   | created_at          | updated_at          |
|----------:|:-------------|:------------|:--------------|:------------------------------|------------:|:-------------------------------------------------------------|:---------|:-------------|:---------------------------------------------------------------------------|:----------|:--------------------------|------------:|:--------------------------|:--------------------------|:--------------------|:--------------------|
|   5100082 | Алексей      | Русаков     | Германович    | aleksey.rusakov.92@yandex.rus | 79827266769 | $2y$10$XbSKC4i8/m1bKVBMKJfWgOdlcXVQqCQ.Ne7GNp/hM228yWLGMu1uG | male     | 1992-03-11   | Кировоград                                                                 | site      |                           | 1.8052e+09  | f                         |                           | 2023-10-06 07:03:07 | 2023-10-06 07:05:35 |
|   5994445 | Дмитрий      | Барилко     | Борисович     | DMITRIJBARILKO1@GMAIL.COM     | 79089088696 | $2y$10$uDxTsGwKfgDzvCp1ccTYnutCJO8jKBOH7UW6q1FPeUd8pvH9yjzQC | male     | 1969-07-03   | ГОР. СВЕРДЛОВСК                                                            | selfiedsa |                           |             | f                         |                           | 2023-12-20 11:53:30 | 2023-12-20 11:53:30 |
|      2810 | Никита       | Кульков     | Алекс         | nik.kulkov00@bk.ru            | 79270989335 | $2y$10$ZOTMKl3uSS/QQZDcj15fK.ISmpmQkO8DuuCepdE2t4KSyll4hYFiG | male     | 2000-08-24   | Г ПЕНЗА                                                                    | alfa      |                           | 2.01567e+09 | f                         |                           | 2022-04-21 19:14:46 | 2024-02-12 01:21:15 |
|   1774313 | Максим       | Клопов      | Андреевич     | questionable1@mail.ru         | 79170257327 | $2y$10$NWDPTD7yyOvK6evlI8OZiu6KU9rZ0qHKgyzHj5ehKEAE/kw.0qN32 | male     | 2001-11-15   | ГОР ПУГАЧЕВ САРАТОВСКОЙ ОБЛ                                                | alfa      |                           |             | f                         |                           | 2022-12-30 11:00:02 | 2022-12-30 11:00:02 |
|      1401 | Семён        | Сотников    | Александрович | miragebeyond@mail.ru          | 79180021549 | $2y$10$JLCT/EkaS044JGHbaggOGujDhvX4tTSx9QwDm22FFMkv6KOphWw5G | male     | 1993-08-06   | СТАНИЦА РОМАНОВСКАЯ ВОЛГОДОНСКОГО Р-НА РОСТОВСКОЙ ОБЛ                      | alfa      |                           |             | f                         |                           | 2022-04-21 14:37:25 | 2022-04-21 14:37:25 |
|   6614058 | Олег         | Яптунэ      | Олегович      | qwertynet99@gmail.com         | 79951744793 | $2y$10$4KPEwiQJluZxOZmgd4hrsuyjcd59jSrrsmMp/PnPWM5fip/sBebE6 | male     | 2003-09-05   | Дудинка                                                                    | site      |                           | 9.77381e+08 | f                         |                           | 2024-02-15 13:10:49 | 2024-02-15 13:12:03 |
|    350343 | Елена        | Кушнир      | Павловна      | elenacushnir65@gmail.com      | 79998835951 | $2y$10$kXUeDLNPaAyXrCBFLkM6levPUW6SAhhneJG06yTblGn7FwIAdbRBG | female   | 1990-10-16   | МОСКОВСКАЯ ОБЛАСТЬ Г.ЧЕХОВ                                                 | alfa      |                           |             | f                         |                           | 2022-07-11 07:36:14 | 2023-07-28 21:00:17 |
|   5359201 | Денис        | Довженко    | Викторович    | dangerden39@gmail.com         | 79953399643 | $2y$10$vzvKBt.Azy80TWZtTq7yKOrMJR3KMVj99H94Htjzc7ucrle5NWnS6 |          |              |                                                                            | site      |                           | 1.59043e+09 | f                         |                           | 2023-10-29 01:15:24 | 2023-10-29 01:15:24 |
|   4666126 | Олеся        | Гусейнова   | Анатольевна   | 79665555455@yandex.ru         | 79665555455 | $2y$10$EuSxi8u9lD2F8H7jytKkyeXAyhq0gHRdIPNAjtBxitTIjJ/UGG//e | female   | 1982-12-26   | МОСКВА                                                                     | alfa      |                           |             | f                         |                           | 2023-09-03 21:33:11 | 2023-09-03 21:33:11 |
|      1406 | Владимир     | Хитриков    | Юрьевич       | hitrikovvladimir@mail.ru      | 79828347783 | $2y$10$Y/EJmajH093rFE2d9.7ggeo7tWjxHwY/NHuGVzWKEYJzXt8tFzXWS | male     | 1972-03-10   | Г. ИЖЕВСК УАССР                                                            | alfa      |                           |             | f                         |                           | 2022-04-21 14:38:11 | 2022-04-21 14:38:11 |
|   5811704 | Мария        | Тимофеева   | Александровна | mariya192030@yandex.ru        | 79814302755 | $2y$10$zUHRn7p/ELDWDukY/.HGTuso/9dv5Oz6oL1lcZKQK13r9WteGFPfO | female   | 1985-06-19   | ГОР.ЧЕРЕПОВЕЦ ВОЛОГОДСКОЙ ОБЛ.                                             | alfa      |                           |             | f                         |                           | 2023-12-05 14:31:30 | 2023-12-05 14:32:07 |
|      1408 | Николай      | Ильченко    | Николаевич    | nik-ilch3121989@yandex.ru     | 79124368330 | $2y$10$MVAcE8QagiNzTLHNy2FkEO2x6RnxiIjmhNdo8Ke.ls7twWXoHWAPK | male     | 1989-12-03   | СЕЛО ЛЕНИНСКОЕ ЛЕНИНСКОГО РАЙОНА КУСТАНАЙСКОЙ ОБЛАСТИ РЕСПУБЛИКА КАЗАХСТАН | alfa      |                           |             | f                         |                           | 2022-04-21 14:38:31 | 2022-04-21 14:38:31 |
|      1409 | Мансурбек    | Нышанов     | Айтбекович    | dildorakambaralieva@yandex.ru | 79170395533 | $2y$10$6fe.LR6oH.iMZBEjlSJQouWJVJ4mvOjZUVLVWzCmE9MlUHDkebxYG | male     | 1983-11-01   | КЫРГЫЗСТАН                                                                 | alfa      |                           |             | f                         |                           | 2022-04-21 14:38:34 | 2022-04-21 14:38:34 |
|   3433355 | Наталья      | Петренко    | Михайловна    | petrenkonatali944@mail.com    | 79050521255 | $2y$10$LcNDayySDxkY8hjszKzQsetLz0TZXy5gK2AU5gpVF.irJRUhSdLnS |          |              |                                                                            | site      |                           | 6.48436e+08 | f                         |                           | 2023-05-24 10:05:50 | 2023-05-24 10:05:50 |
|      1411 | Олёг         | Молчанов    | Иванович      | molchanovlegrand@gmail.com    | 79006506163 | $2y$10$FYBWJQLexdOy8aov53OJj.HQW3cXIZeigm1Q33JgIIM1sy8ZLFpHC | male     | 1992-11-16   | ГОР. ИНТАРЕСПУБЛИКА КОМИ                                                   | alfa      |                           |             | f                         |                           | 2022-04-21 14:38:48 | 2022-04-21 14:38:48 |
|      1412 | Александра   | Моисеева    | Емилияновна   | gililova1988@mail.ru          | 79165176520 | $2y$10$AWjYK/C8v87QxkpwuGthi.ENk0ODrSMfA0K1hgLOtjxWHQGI2W/eq | female   | 1988-11-27   | Г. ЛОБНЯ МОСКОВСКОЙ ОБЛ                                                    | alfa      |                           |             | f                         |                           | 2022-04-21 14:38:50 | 2022-04-21 14:38:50 |
|   3163656 | Сергей       | Тюхалкин    | Александрович | 79043942603@mail.ru           | 79043942603 | $2y$10$N6GvpqLuqpc7QvqVUdD3VewWkWGpN2wUIOKzBJCZRxpXFCI8.xFoG | male     | 1981-03-23   | НИЖНИЙ НОВГОРОД                                                            | alfa      |                           |             | f                         |                           | 2023-05-01 12:19:20 | 2023-05-01 12:19:20 |
|      1414 | Дмитрий      | Кузнецов    | Евгеньевич    | avansier6@gmail.com           | 79137440476 | $2y$10$5Ha1SETGD2MbDKkUxcwfd.ujophBOfyEWg4uQe1nZrUfDsaFM.YYG | male     | 1992-01-05   | ГОР.НОВОСИБИРСК                                                            | alfa      |                           |             | f                         |                           | 2022-04-21 14:39:00 | 2022-04-21 14:39:00 |
|      1415 | Тимур        | Абакаров    | Камилович     | timurchik66@icloud.com        | 79522079981 | $2y$10$vi8ujifB4VLwGPn4mC4ugOr6uKKNmNQ94JM4YFWm1FivvParxq1V6 | male     | 1984-06-06   | ГОРОД ХАСАВЮРТ РЕСПУБЛИКА ДАГЕСТАН                                         | alfa      |                           |             | f                         |                           | 2022-04-21 14:39:12 | 2022-04-21 14:39:12 |
|   5100731 | Александр    | Хавренко    | Дмитриевич    | 79000635316@mail.ru           | 79000635316 | $2y$10$c8yANDeWxiayPWDHTbkeZeHu8hT/Mb/sBBYPaXAaxJhISZEzJs6aW | male     | 1987-01-15   | ЧЕЛЯБИНСК                                                                  | alfa      |                           | 2.14431e+08 | f                         |                           | 2023-10-06 08:43:46 | 2023-10-06 08:45:24 |
```

> - Code name: index_0005
> - File path: /home/user/Documents/data/index_0005/raw/adengi.ru_23.02.2024_6,8M/clients_inn_adengi.ru.csv
> - Total rows: 3755426

### Schema
```
root
 |-- id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- inn: string (nullable = true)
 |-- response_code: string (nullable = true)
 |-- response_inn: string (nullable = true)
 |-- captcha_required: string (nullable = true)
 |-- error_details: string (nullable = true)
 |-- created_at: string (nullable = true)
 |-- updated_at: string (nullable = true)

```

### Data sample
```
|     id |   user_id |          inn | response_code   | response_inn      | captcha_required                                                 | error_details               | created_at                                              | updated_at          |
|-------:|----------:|-------------:|:----------------|:------------------|:-----------------------------------------------------------------|:----------------------------|:--------------------------------------------------------|:--------------------|
| 310311 |   1623486 | 280116407867 | found           | "{'"code'":1      | '"inn'":'"280116407867'"                                         | '"captchaRequired'":false}" |                                                         | 2022-12-14 09:04:52 |
| 310312 |   1622370 |              | not_found       | "{'"code'":0      | '"captchaRequired'":false}"                                      |                             | 2022-12-14 09:05:00                                     | 2022-12-14 09:05:00 |
| 310313 |   1622384 |              | not_found       | "{'"code'":0      | '"captchaRequired'":false}"                                      |                             | 2022-12-14 09:05:06                                     | 2022-12-14 09:05:06 |
| 310314 |    932438 | 220701052502 | found           | "{'"code'":1      | '"inn'":'"220701052502'"                                         | '"captchaRequired'":false}" |                                                         | 2022-12-14 09:05:07 |
| 310315 |   1627404 | 560202791910 | found           | "{'"code'":1      | '"inn'":'"560202791910'"                                         | '"captchaRequired'":false}" |                                                         | 2022-12-14 09:05:11 |
| 310316 |   1623375 | 741109614573 | found           | "{'"code'":1      | '"inn'":'"741109614573'"                                         | '"captchaRequired'":false}" |                                                         | 2022-12-14 09:05:19 |
| 310317 |   1623157 | 462502938072 | found           | "{'"code'":1      | '"inn'":'"462502938072'"                                         | '"captchaRequired'":true}"  |                                                         | 2022-12-14 09:05:28 |
| 310318 |   1624926 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:05:32 |
| 310319 |   1624292 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:05:34 |
| 310320 |   1624200 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:05:38 |
| 310321 |   1622664 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:05:40 |
| 310322 |   1622857 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:05:44 |
| 310323 |   1625434 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:05:55 |
| 310324 |    481469 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:05:57 |
| 310325 |    573118 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:05:57 |
| 310326 |   1453114 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:06:07 |
| 310327 |   1627405 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:06:08 |
| 310328 |   1624122 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:06:12 |
| 310329 |   1623404 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:06:12 |
| 310330 |   1622674 |              | error           | "{'"ERROR'":'"-'" | '"ERRORS'":{'"captcha'":['"Требуется ввести цифры с картинки'"]} | '"STATUS'":400}"            | "{'"captcha'":['"Требуется ввести цифры с картинки'"]}" | 2022-12-14 09:06:18 |
```

> - Code name: index_0005
> - File path: /home/user/Documents/data/index_0005/raw/adengi.ru_23.02.2024_6,8M/clients_passports_adengi.ru.csv
> - Total rows: 6677818

### Schema
```
root
 |-- id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- serial: string (nullable = true)
 |-- number: string (nullable = true)
 |-- date_issue: string (nullable = true)
 |-- authority: string (nullable = true)
 |-- authority_code: string (nullable = true)
 |-- date_expire: string (nullable = true)
 |-- created_at: string (nullable = true)
 |-- updated_at: string (nullable = true)

```

### Data sample
```
|   id |   user_id |   serial |   number | date_issue   | authority                                                                                     |   authority_code | date_expire   | created_at          | updated_at          |
|-----:|----------:|---------:|---------:|:-------------|:----------------------------------------------------------------------------------------------|-----------------:|:--------------|:--------------------|:--------------------|
|    1 |         2 |     3344 |   123459 | 2018-01-02   | УВД г. Москва                                                                                 |           555444 | 2045-01-02    | 2022-04-07 14:34:05 | 2022-04-07 14:34:05 |
|    2 |         3 |     5009 |   606223 | 2009-12-08   | ОТДЕЛЕНИЕМ УФМС РОССИИ ПО НОВОСИБИРСКОЙ ОБЛ. В ОКТЯБРЬСКОМ РАЙОНЕ Г. НОВОСИБИРСКА             |           540008 | 2033-11-14    | 2022-04-13 09:13:28 | 2022-04-13 09:13:28 |
|    3 |         4 |     3219 |    84457 | 2019-08-26   | ГУ МВД РОССИИ ПО КЕМЕРОВСКОЙ ОБЛасти                                                          |           420003 | 2039-06-16    | 2022-04-14 13:50:15 | 2022-04-14 13:50:15 |
|    4 |         5 |     4620 |   848193 | 2020-09-03   | ГУ МВД РОССИИ ПО МОСКОВСКОЙ ОБЛ.                                                              |           500034 | 2075-08-10    | 2022-04-15 08:52:51 | 2022-04-15 08:52:51 |
|    5 |         6 |     3915 |   119756 | 2017-04-06   | ОТДЕЛЕНИЕМ УФМС РОССИИ ПО МОСКОВСКОЙ ОБЛ. В Г. ЛОБНЕ                                          |           500067 | 2027-09-11    | 2022-04-18 22:04:21 | 2022-04-18 22:04:21 |
|    6 |         7 |      109 |   400744 | 2009-08-18   | ОТДЕЛЕНИЕМ УФМС РОССИИ ПО АЛТАЙСКОМУ КРАЮ ПО Г. СЛАВГОРОДУ И СЛАВГОРОДСКОМУ РАЙОНУ            |           220046 | 2030-01-13    | 2022-04-19 09:52:10 | 2022-04-19 09:52:10 |
|    7 |         8 |     3214 |   493821 | 2014-12-17   | ОТДЕЛОМ УФМС РОССИИ ПО КЕМЕРОВСКОЙ ОБЛ. В ЦЕНТРАЛЬНОМ РАЙОНЕ Г. КЕМЕРОВО                      |           420002 | 2039-12-01    | 2022-04-19 15:20:37 | 2022-04-19 15:20:37 |
|    8 |        10 |        0 |        0 | 2022-04-21   | ВЫАЫЫВЫА                                                                                      |           123456 | 2045-04-21    | 2022-04-21 08:57:19 | 2022-04-21 08:57:19 |
|    9 |        11 |     6605 |   208840 | 2006-08-22   | ГАГАРИНСКИМ ГОВД СМОЛЕНСКОЙ ОБЛ.                                                              |           672007 | 2031-04-30    | 2022-04-21 09:25:09 | 2022-04-21 09:25:09 |
|   10 |        12 |     6012 |    15079 | 2011-07-09   | ОТДЕЛЕНИЕМ УФМС РОССИИ ПО РОСТОВСКОЙ ОБЛ. В ПЕРВОМАЙСКОМ РАЙОНЕ Г. РОСТОВА-НА-ДОНУ            |           610014 | 2036-06-03    | 2022-04-21 10:20:19 | 2022-04-21 10:20:19 |
|   11 |        13 |     4608 |   351692 | 2008-08-27   | ОТДЕЛОМ УФМС РОССИИ ПО МОСКОВСКОЙ ОБЛ. В КЛИНСКОМ РАЙОНЕ                                      |           500046 | 2033-02-19    | 2022-04-21 10:20:44 | 2022-04-21 10:20:44 |
|   12 |        14 |     3818 |   181073 | 2018-05-16   | УМВД РОССИИ ПО КУРСКОЙ ОБЛАСТИ                                                                |           460006 | 2043-04-05    | 2022-04-21 10:23:10 | 2022-04-21 10:23:10 |
|   13 |        15 |     5220 |   982377 | 2020-11-14   | УМВД РОССИИ ПО ОМСКОЙ ОБЛАСТИ                                                                 |           550001 | 2045-11-08    | 2022-04-21 10:23:38 | 2022-04-21 10:23:38 |
|   14 |        16 |     1115 |    91479 | 2016-04-05   | ОТДЕЛОМ УФМС РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛАСТИ И НЕНЕЦКОМУ АВТОНОМНОМУ ОКРУГУ В ВЕЛЬСКОМ РАЙОНЕ |           290007 | 2047-03-29    | 2022-04-21 10:24:03 | 2022-04-21 10:24:03 |
|   15 |        17 |     1806 |   931216 | 2007-02-20   | ЧЕРНЫШКОВСКИМ РОВД ВОЛГОГРАДСКОЙ ОБЛ.                                                         |           342043 | 2031-06-10    | 2022-04-21 10:24:16 | 2022-04-21 10:24:16 |
|   16 |        18 |     3315 |   372773 | 2016-06-20   | МИГРАЦИОННЫМ ПУНКТОМ УФМС РОССИИ ПО КИРОВСКОЙ ОБЛАСТИ В ФАЛЕНСКОМ РАЙОНЕ                      |           430036 | 2041-06-11    | 2022-04-21 10:24:43 | 2022-04-21 10:24:43 |
|   17 |        19 |     1118 |   226661 | 2018-08-10   | УМВД РОССИИ ПО АРХАНГЕЛЬСКОЙ ОБЛ.                                                             |           290013 | 2037-04-06    | 2022-04-21 10:26:21 | 2022-04-21 10:26:21 |
|   18 |        20 |     7320 |   401860 | 2020-12-10   | ОТДЕЛОМ УФМС  РОССИИ ПО УЛЬЯНОВСКОЙ ОБЛАСТИ В ЗАВОЛЖСКОМ РАЙОНЕ ГОРОДА УЛЬЯНОВСКА             |           730003 | 2072-01-02    | 2022-04-21 10:26:37 | 2022-04-21 10:26:37 |
|   19 |        21 |     6915 |   675695 | 2015-11-25   | ОТДЕЛОМ УФМС РОССИИ ПО ТОМСКОЙ ОБЛАСТИ В ГОР. КОЛПАШЕВО                                       |           700023 | 2029-05-02    | 2022-04-21 10:27:42 | 2022-04-21 10:27:42 |
|   20 |        22 |     1714 |   381285 | 2014-10-07   | МРО УФМС ПО ВЛАДИМИРСКОЙ ОБЛАСТИ В ГОРОДЕ ВЯЗНИКИ                                             |           028330 | 2038-11-03    | 2022-04-21 10:27:43 | 2022-04-21 10:27:43 |
```


## About final data
> - Total rows: 6694675

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- addresses: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- raw: string (nullable = false)
 |    |    |-- address: string (nullable = true)
 |    |    |-- location: struct (nullable = true)
 |    |    |    |-- region_type: string (nullable = true)
 |    |    |    |-- region_value: string (nullable = true)
 |    |    |    |-- settlement_region_type: string (nullable = true)
 |    |    |    |-- settlement_region_value: string (nullable = true)
 |    |    |    |-- settlement_type: string (nullable = true)
 |    |    |    |-- settlement_value: string (nullable = true)
 |    |    |    |-- street_type: string (nullable = true)
 |    |    |    |-- street_value: string (nullable = true)
 |    |    |    |-- house: string (nullable = true)
 |    |    |    |-- flat: string (nullable = true)
 |    |    |    |-- floor: string (nullable = true)
 |    |    |    |-- office: string (nullable = true)
 |    |    |    |-- corpus: string (nullable = true)
 |    |    |    |-- coordinates: array (nullable = true)
 |    |    |    |    |-- element: double (containsNull = true)
 |    |    |    |-- coord_detalization_lvl: integer (nullable = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = false)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- id: integer (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)

```

### Data sample
```
| names                                    | address                                              | addresses                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | emails                                 | phones          | accounts                                                                                                                                   | documents                                                                                                                   |   sex | birth_date   |
|:-----------------------------------------|:-----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|------:|:-------------|
| ['Александр Козлов Александрович']       | ['Город Горький']                                    | [Row(type=1, raw='ГОРОД ГОРЬКИЙ', address='город Горький', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Горький', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=[47.1818468973098, 56.14882870825013], coord_detalization_lvl=1))]                                                                                 |                                        | ['79991215222'] | [Row(title='adengi', link='https://adengi.ru/', id=1956267, password_hash='$2y$10$4OacwBFDD3Km/VKj5dJ/HuZmxQ/ajmRm1CeZsNjlO7/RDLvlG2i2G')] | [Row(type=1, serial='526321883130', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     1 | 22.01.1987   |
| ['Александр Брусянин Алексеевич']        |                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ['az08.cerb@gmail.com']                | ['79923071148'] | [Row(title='adengi', link='https://adengi.ru/', id=6419694, password_hash='$2y$10$4ke/CX9L5pbKuN9e6sSmWOmfE5hNeFAcDl/r8jlk9c.PMwYdxs9hO')] |                                                                                                                             |   nan |              |
| ['Амнат Дадалова Вахидсолтовна']         | ['Шалинский р он']                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ['amnatdadalova@gmail.com']            | ['79637066037'] | [Row(title='adengi', link='https://adengi.ru/', id=2423833, password_hash='$2y$10$HhGrmsOJuV9kkkddHHjaUu6ZRpqEx.V7Jl6XlGD/q8X9KFvoRrshW')] | []                                                                                                                          |     1 | 04.03.1979   |
| ['Анастасия Беляева Вячеславовна']       |                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ['nastyabelaeva01@yandex.ru']          | ['79524725064'] | [Row(title='adengi', link='https://adengi.ru/', id=1844912, password_hash='$2y$10$/gN9ks9dhWueU/Mrn2hod.pfaauPHsEfJqm44NBdhv41rwm3ReLw2')] |                                                                                                                             |   nan |              |
| ['Анастасия Зарифуллина Амировна']       | ['Пос. Ильинский Пермская обл.']                     | [Row(type=1, raw='Пос. Ильинский Пермская обл.', address='область Пермская', location=Row(region_type='область', region_value='Пермская', settlement_region_type=None, settlement_region_value=None, settlement_type='поселок', settlement_value='Ильинский', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=[30.4704284, 59.9648648], coord_detalization_lvl=1))]                                                             | ['anastasij08092013@mail.com']         | ['79519367027'] | [Row(title='adengi', link='https://adengi.ru/', id=3622869, password_hash='$2y$10$w7ce3sdzxa.fxvPY7/bDHeL1jIJJ6p/TohXlvmM6IJzhRPgBlxwYu')] | []                                                                                                                          |     0 | 19.03.1984   |
| ['Анастасия Дында Сергеевна']            | ['Севастополь']                                      | [Row(type=1, raw='Севастополь', address='город Севастополь', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Севастополь', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=[49.17803660153933, 55.750044946350386], coord_detalization_lvl=1))]                                                                         | ['anastasiya.dynda88@gmail.com']       | ['79505381355'] | [Row(title='adengi', link='https://adengi.ru/', id=4969198, password_hash='$2y$10$3uIUQn6TTAB.dik28SZXou7WDYAeZWFmZ1GFE0Iz5xkOQSrlfg4RC')] | []                                                                                                                          |     0 | 24.07.1988   |
| ['Анастасия Кузнецова Сергеевна']        | ['РП.Саргатское Саргатский район Омская область']    | [Row(type=1, raw='РП.Саргатское Саргатский район Омская область', address='область Омская район Саргатский', location=Row(region_type='область', region_value='Омская', settlement_region_type='район', settlement_region_value='Саргатский', settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=1))]                                                    | ['kuznecovaanastasia017@gmail.com']    | ['79012626146'] | [Row(title='adengi', link='https://adengi.ru/', id=1232075, password_hash='$2y$10$EXR0hLbSQJ35R7OHQc3vr.PjeT0nnH6iDB5Kll3wi0hRU1hqti7ba')] | [Row(type=1, serial='553200737219', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 22.07.2000   |
| ['Аанастасия Шиханина Юрьевна']          | ['Город Краснотурьинск.']                            | [Row(type=1, raw='ГОРОД КРАСНОТУРЬИНСК.', address='город Краснотурьинск', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Краснотурьинск', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=[60.20121531784691, 59.78635421204361], coord_detalization_lvl=1))]                                                          | ['ashikhanina@bk.ru']                  | ['79022577517'] | [Row(title='adengi', link='https://adengi.ru/', id=2802951, password_hash='$2y$10$3wk08m2gDt10tkmgJSTzTeLg7UWVAC2z2AGD.MDZUbEPOsT8y2sle')] | []                                                                                                                          |     0 | 03.08.2001   |
| ['Аандрей Худинов Васильевич']           | ['Архангельск']                                      | [Row(type=1, raw='АРХАНГЕЛЬСК', address='город Архангельск', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Архангельск', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=[39.26572147335222, 57.06447559699346], coord_detalization_lvl=1))]                                                                          | ['andrejhudinov32@gmail.com']          | ['79268775409'] | [Row(title='adengi', link='https://adengi.ru/', id=1067553, password_hash='$2y$10$R6OXKnqV0dNq350mwQLMN.U0Y4lHlEIFvM2M0NZA70B3VahyQTnEq')] | []                                                                                                                          |     1 | 26.09.1987   |
| ['Абакаргаджи Абакаргаджиев Алиевич']    | ['С.Чирката Гумбетовский Район Республики Дагестан'] | [Row(type=1, raw='С.ЧИРКАТА ГУМБЕТОВСКИЙ РАЙОН РЕСПУБЛИКИ ДАГЕСТАН', address='республика Дагестан село Чирката район Гумбетовский', location=Row(region_type='республика', region_value='Дагестан', settlement_region_type='район', settlement_region_value='Гумбетовский', settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=1))]                      | ['abakargadziabakargadziev@gmail.com'] | ['79285857011'] | [Row(title='adengi', link='https://adengi.ru/', id=324390, password_hash='$2y$10$AITL.ELsVngB1osLI/Y5yuKYs9QiJNowR9oCwnBuPLdYm2CTiBneS')]  | []                                                                                                                          |     1 | 10.08.1982   |
| ['Абдалкасим Магомедмансуров Исрапович'] | ['С Гуни']                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ['qwerty48@gmail.com']                 | ['79894506913'] | [Row(title='adengi', link='https://adengi.ru/', id=5646209, password_hash='$2y$10$lw5ZxW5YUWiYWychqJWFzOikTnGVAw6czaVKDnp6eh8R14GXj4ali')] | []                                                                                                                          |     1 | 03.08.2004   |
| ['Абделрахман Абделмагид Абделнаим']     |                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ['bashabebo058@mail.com']              | ['79956391214'] | [Row(title='adengi', link='https://adengi.ru/', id=3396453, password_hash='$2y$10$jdMthjqCjI6m2n5vxY6AZekbnxvygps4F1FukU3fjJKIn/iYOtMNq')] |                                                                                                                             |   nan |              |
| ['Абдрахман Кумкаков Бисекович']         | ['С Суетиновка Волгоградской Обл']                   | [Row(type=1, raw='С СУЕТИНОВКА ВОЛГОГРАДСКОЙ ОБЛ', address='область Волгоградская село Суетиновка', location=Row(region_type='область', region_value='Волгоградская', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=1))]                                                                 |                                        | ['79275427494'] | [Row(title='adengi', link='https://adengi.ru/', id=1845638, password_hash='$2y$10$NEwVs2xQHsQGkSh1RhiVKe/yblkN0JA/d2t6EnqWtCamw7DoeOqmy')] | []                                                                                                                          |     1 | 14.04.1962   |
| ['Абдузият Магомедов Гаджиевич']         | ['П. Нарын-Худук Черноземельского Р-На Калм. Асср']  | [Row(type=1, raw='П. НАРЫН-ХУДУК ЧЕРНОЗЕМЕЛЬСКОГО Р-НА КАЛМ. АССР', address='посёлок Нарын-Худук район Калм', location=Row(region_type=None, region_value=None, settlement_region_type='район', settlement_region_value='Калм', settlement_type='посёлок', settlement_value='Нарын-Худук', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=1))]                                                    | ['abdulmagomebov593@gmail.com']        | ['79968885444'] | [Row(title='adengi', link='https://adengi.ru/', id=2745655, password_hash='$2y$10$FObIIt7x4nI5vDUeCrhzSOW/GXPzuP4SuebRkwAkLL5Qi0XSp1286')] | []                                                                                                                          |     1 | 14.06.1985   |
| ['Абдул Рамазанов Магомедович']          |                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ['abdulramazanov141@gmail.com']        | ['79285028726'] | [Row(title='adengi', link='https://adengi.ru/', id=6380317, password_hash='$2y$10$spto2pDvKt1kGokBqhxYG.nd.orOyptD3WT0T//1cSPkIJbyXsYca')] |                                                                                                                             |   nan |              |
| ['Абдул Шахмандаров Баширович']          | ['Астрахань']                                        | [Row(type=1, raw='АСТРАХАНЬ', address='город Астрахань', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Астрахань', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=[48.07051409537934, 46.451998566945086], coord_detalization_lvl=1))]                                                                               | ['sahmandarovabdul696@gmail.com']      | ['79880614391'] | [Row(title='adengi', link='https://adengi.ru/', id=4711728, password_hash='$2y$10$0SWfjRWVaZvDdjdqyUhMFe9Z0NagQ2ELYSQ.i3yRHqDUWoq8UBRAq')] | []                                                                                                                          |     1 | 19.07.1999   |
| ['Абдул-Кадыр Албогачиев Мухматович']    | ['Назрань Республика Ингушетия']                     | [Row(type=1, raw='НАЗРАНЬ РЕСПУБЛИКА ИНГУШЕТИЯ', address='республика Ингушетия город Назрань', location=Row(region_type='республика', region_value='Ингушетия', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Назрань', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=1))]                                                               | ['aakm93@mail.ru']                     | ['79235346660'] | [Row(title='adengi', link='https://adengi.ru/', id=6219385, password_hash='$2y$10$YnLlSxQ0xJ155sDRjQ3eWu7bWHQqRP3vgpOwt3TxMhE8BkxnVPyXy')] | []                                                                                                                          |     1 | 19.09.1993   |
| ['Абдул-Малик Кагиров Зелимханович']     | ['Назрань']                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | ['ghjjhbb@gmail.com']                  | ['79386666316'] | [Row(title='adengi', link='https://adengi.ru/', id=3389982, password_hash='$2y$10$0wilGJuKodTob3TizZiXkujnXM4uMYY6ePPMbPgeFP.LrXhu2fqRu')] | []                                                                                                                          |     1 | 19.04.2005   |
| ['Абдул-Малик Темиров Аптиевич']         | ['Г Шали Шалинский Район Чеченская Республика']      | [Row(type=1, raw='Г ШАЛИ ШАЛИНСКИЙ РАЙОН ЧЕЧЕНСКАЯ РЕСПУБЛИКА', address='республика Чечня город Шали район Шалинский', location=Row(region_type='республика', region_value='Чечня', settlement_region_type='район', settlement_region_value='Шалинский', settlement_type='город', settlement_value='Шали', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=[45.891194911484234, 43.24511021744261], coord_detalization_lvl=1))] | ['online2017tem@gmail.com']            | ['79661988889'] | [Row(title='adengi', link='https://adengi.ru/', id=5123565, password_hash='$2y$10$/bbaIdI7b/1l5/igpq.lKulstmwCUVkIrllesmVeaijQrSZmbuU3u')] | [Row(type=1, serial='201212201700', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     1 | 24.05.2004   |
| ['Абдул-Муталиб Тимаров Анзорович']      | ['Гор. Грозный Чеченской Республики']                | [Row(type=1, raw='ГОР. ГРОЗНЫЙ ЧЕЧЕНСКОЙ РЕСПУБЛИКИ', address='республика Чечня город Грозный', location=Row(region_type='республика', region_value='Чечня', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Грозный', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=[40.162092417941096, 47.702072847578144], coord_detalization_lvl=1))]                              | ['tisharovabdul@icloud.com']           | ['79271331731'] | [Row(title='adengi', link='https://adengi.ru/', id=4480948, password_hash='$2y$10$sHyu0.2Ni/TBhFZVGZJ2OOjExfoqPrbcEppSgvK9DBoQ2p25bgGC2')] | []                                                                                                                          |     1 | 06.04.1997   |
```