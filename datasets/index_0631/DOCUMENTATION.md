# Parsetron results

## About row data

> - File path: agents_data*.csv
> - Total rows: 5036

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- Пользователь: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Агентство Недвижимости: string (nullable = true)
 |-- Роль: string (nullable = true)

```

### Data sample
```
|    id |   Пользователь | ФИО                             | Почта                         | Агентство Недвижимости       | Роль   |
|------:|---------------:|:--------------------------------|:------------------------------|:-----------------------------|:-------|
| 24542 |    79585874971 | Новиков Алексей Михайлович      | 5115701@mail.ru               | ИП Новиков А.М.              |        |
| 24540 |    79643608916 | Ильина Анастасия Евгеньевна     | ilinaae@mirkv.com             | ООО АК Мир Квартир           |        |
| 24778 |    79992250374 | Фадеева Екатерина Владимировна  | fadeevakatya95@mail.ru        | АН Ювикол                    |        |
| 25690 |    79657840154 | Абрамян Эрик Санвелович         | er.abramian@gmail.com         | АН Надежда                   |        |
| 25714 |    73213158932 | Ельницкая Ольга                 | elnickaya@rfn.spb.ru          | Русский Фонд Недвижимости    |        |
| 25364 |    79219832235 | Брой-Каррэ Оксана               | broyka@bk.ru                  | АН Ювикол                    |        |
| 23984 |    79622107646 | Штатнова Мария Дмитриевна       | shtatnova.mari@mail.ru        | АН Адмирал                   |        |
| 23836 |    79110016556 | Иванова Наталья Ивановна        | 89110016556@yandex.ru         | Эрмитаж Галерея Недвижимости |        |
| 25320 |    79111415909 | Подаваева Вера Николаевна       | vera.amosova2017@yandex.ru    | @Victor.Realty               |        |
| 23862 |    79312988955 | Пузанов Илья Витальевич         | ilia.rop@outlook.com          | North Star                   |        |
| 21112 |    79500073315 | Майорова Екатерина Степановна   | mayor_1994@inbox.ru           | Дом                          |        |
|  9494 |    79219707264 | Юлия Иванова                    | ivulya1081@yandex.ru          | НЕВА Недвижимость            |        |
| 24622 |    79526246243 | Мальцева Юлия Алексеевна        | yulia-lend@yandex.ru          | ПЛАН                         |        |
| 24962 |    79119854185 | Екатерина Литвинчук             | litvinchuk_eo@bk.ru           | АН Романа Чиковани           |        |
| 24588 |    79219494798 | Михайлова Людмила Дмитриевна    | 9494798@mail.ru               | ИП Шишкин Алексей Валерьевич |        |
| 27006 |    79310006010 | фролова инна романовна          | astana_ui@mail.ru             | smart realtor                |        |
| 24570 |    79602962488 | Кузнецова Светлана Геннадьевна  | evstisveta@mail.ru            | Marinova Estate              |        |
| 24658 |    79650510225 | Ботвич Артём Михайлович         | 89650510225@perspektiva24.com | АН Перспектива24-Приморский  |        |
| 25168 |    79584983889 | Замыслова Анна Николаевна       | a.prosuvorova@yandex.ru       | АН Адмирал                   |        |
| 25502 |    79119484873 | Мильковский Вячеслав Викторович | vm@anwh.ru                    | Белый Дом                    |        |
```

> - File path: contacts.csv
> - Total rows: 433

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- Фотография: string (nullable = true)
 |-- Обращение: string (nullable = true)
 |-- Имя: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Отчество: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Должность: string (nullable = true)
 |-- Компания: string (nullable = true)
 |-- Тип контакта: string (nullable = true)
 |-- Ответственный: string (nullable = true)
 |-- Рабочий телефон: string (nullable = true)
 |-- Мобильный телефон: string (nullable = true)
 |-- Рабочий e-mail: string (nullable = true)
 |-- Источник: string (nullable = true)
 |-- Дополнительно об источнике: string (nullable = true)
 |-- Экспорт: string (nullable = true)
 |-- Кем создан: string (nullable = true)
 |-- Дата создания: string (nullable = true)
 |-- Кем изменен: string (nullable = true)
 |-- Дата изменения: string (nullable = true)

```

### Data sample
```
|   ID | Фотография   | Обращение   | Имя                 | Фамилия            | Отчество   | Дата рождения   | Должность    | Компания                                    | Тип контакта    | Ответственный       |   Рабочий телефон | Мобильный телефон   | Рабочий e-mail                 | Источник       | Дополнительно об источнике   | Экспорт   | Кем создан          | Дата создания       | Кем изменен   | Дата изменения      |
|-----:|:-------------|:------------|:--------------------|:-------------------|:-----------|:----------------|:-------------|:--------------------------------------------|:----------------|:--------------------|------------------:|:--------------------|:-------------------------------|:---------------|:-----------------------------|:----------|:--------------------|:--------------------|:--------------|:--------------------|
| 3152 |              |             | Москвина            | Яна                |            |                 |              | АН Аста                                     | Агент           | Мерген Лиджиев      |       79291769357 |                     | yam@asta-an.ru                 |                |                              | да        | Мерген Лиджиев      | 27.08.2021 12:10:01 | Герман Ющенко | 04.10.2021 16:30:52 |
| 5440 |              |             | Наталья             | Яковлева           |            |                 | Менеджер     | Созвездие недвижимости                      | Агент           | Анна Епифанова      |       79215883086 |                     | yakovleva@szvdom.ru            |                |                              | да        | Анна Епифанова      | 27.09.2021 17:30:42 | Герман Ющенко | 04.10.2021 16:30:58 |
| 4356 |              |             | Анциферов           | Юрий Владимирович  |            |                 |              | ИП Анциферов Ю. В.                          | Агент           | Мерген Лиджиев      |       79219647163 |                     | an9647163@yandex.ru            |                |                              | да        | Мерген Лиджиев      | 10.09.2021 11:23:26 | Герман Ющенко | 04.10.2021 16:30:55 |
|  810 |              |             | Марышев             | Юрий Александрович |            |                 |              | АН Петербург недвижимость / ИП Марышев Ю.А. | Руководитель АН | Мерген Лиджиев      |       79312262380 |                     | 89319708502@mail.ru            |                |                              | да        | Мерген Лиджиев      | 06.08.2021 11:20:34 | Герман Ющенко | 04.10.2021 16:30:49 |
| 3380 |              |             | Заморина            | Юлия Леонидовна    |            |                 |              | АН Первый дом                               | Агент           | Мерген Лиджиев      |       89111603519 |                     | dom1.zamorina@gmail.com        |                |                              | да        | Мерген Лиджиев      | 30.08.2021 14:32:19 | Герман Ющенко | 04.10.2021 16:30:53 |
|  476 |              |             | Петина              | Юлия Викторовна    |            |                 |              | ООО Деловые Технологии                      | Руководитель АН | Мерген Лиджиев      |       89118191619 |                     | asoty@inbox.ru                 |                |                              | да        | Мерген Лиджиев      | 02.08.2021 15:36:17 | Герман Ющенко | 04.10.2021 16:30:48 |
| 4184 |              |             | Лошкарёва           | Юлия Алексеевна    |            |                 |              | АН CITY.com / ИП Лошкарёва Ю.А.             | Руководитель АН | Мерген Лиджиев      |       79143361711 |                     | yulia_loshkareva191288@mail.ru |                |                              | да        | Мерген Лиджиев      | 08.09.2021 12:05:52 | Герман Ющенко | 04.10.2021 16:30:55 |
| 5522 |              |             | Боженова            | Юлия Александровна |            |                 |              | ИП Боженова Ю.А.                            | Агент           | Мерген Лиджиев      |       79522360303 |                     | u.bozhenova@mail.ru            |                |                              | да        | Мерген Лиджиев      | 28.09.2021 16:11:52 | Герман Ющенко | 04.10.2021 16:30:59 |
| 4724 |              |             | Анастасия           | Этажи              |            |                 |              |                                             | Агент           | Хайран Пржевальский |       89219956517 |                     |                                |                |                              | да        | Хайран Пржевальский | 16.09.2021 18:45:15 | Герман Ющенко | 04.10.2021 16:30:56 |
| 1692 |              |             | Файзуллин           | Эрик Уралович      |            |                 |              | ООО ЭкспертКом                              | Агент           | Мерген Лиджиев      |       89117860640 |                     | 3@expertcom-spb.ru             |                |                              | да        | Мерген Лиджиев      | 12.08.2021 14:28:56 | Герман Ющенко | 04.10.2021 16:30:50 |
| 5030 |              |             | Регина              | Эдилерская         |            |                 | Менеджер     | 100 квадратов                               | Агент           | Анна Епифанова      |       79117824373 |                     | rishechka1@yandex.ru           |                |                              | да        | Анна Епифанова      | 22.09.2021 17:58:15 | Герман Ющенко | 04.10.2021 16:30:57 |
|  468 |              |             | Елена               | Щербакова          |            |                 |              | АН Диалог                                   | Агент           | Мерген Лиджиев      |       79219051277 |                     | 9051277@mail.ru                |                |                              | да        | Мерген Лиджиев      | 02.08.2021 14:54:34 | Герман Ющенко | 04.10.2021 16:30:48 |
| 5892 |              |             | Евдокия Васильевна  | Ширяева            |            |                 | Руководитель | ИП Ширяева Евдокия Васильевна               | Руководитель АН | Анна Епифанова      |       79062730418 |                     | shirevd@list.ru                |                |                              | да        | Анна Епифанова      | 04.10.2021 11:45:05 | Герман Ющенко | 04.10.2021 16:31:02 |
| 4708 |              |             | Наталья             | Шимохина           |            |                 |              | ООО Вторая Парадная / АН Вторая парадная    | Агент           | Мерген Лиджиев      |       79995159112 |                     | shimohina.realty@yandex.ru     |                |                              | да        | Мерген Лиджиев      | 16.09.2021 16:14:29 | Герман Ющенко | 04.10.2021 16:30:56 |
| 5414 |              |             | Полина Романовна    | Шалаева            |            |                 | Менеджер     | Созвездие недвижимости                      | Агент           | Анна Епифанова      |       79217629676 |                     | shalaeva@szvdom.ru             |                |                              | да        | Анна Епифанова      | 27.09.2021 16:52:14 | Герман Ющенко | 04.10.2021 16:30:58 |
| 4662 |              |             | Михаил              | Черноусенко        |            |                 | Менеджер     | Легион Недвижимость                         | Агент           | Анна Епифанова      |       79217980621 |                     | litt-670@mail.ru               |                |                              | да        | Анна Епифанова      | 16.09.2021 12:22:31 | Герман Ющенко | 04.10.2021 16:30:56 |
| 2076 |              |             | Мария               | Чернова            |            |                 |              | АН Панорама                                 | Агент           | Мерген Лиджиев      |       89819528250 |                     |                                | Переуступки.РФ |                              | да        | Дмитрий Шкляр       | 16.08.2021 12:38:45 | Герман Ющенко | 04.10.2021 16:30:51 |
|  498 |              |             | Анастасия           | Черниченко         |            |                 | ГД           | АН Черника / ИП Черниченко Анастасия        | Агент           | Анастасия Коршунова |       89110747125 |                     | chernika.flat@bk.ru            | Переуступки.РФ |                              | да        | Дмитрий Шкляр       | 03.08.2021 09:36:40 | Герман Ющенко | 04.10.2021 16:30:49 |
| 5898 |              |             | Екатерина Сергеевна | Цебоева            |            |                 | Руководитель | Твоя Квартира                               | Руководитель АН | Мерген Лиджиев      |       79215874945 |                     | 9215874945@mail.ru             |                |                              | да        | Мерген Лиджиев      | 04.10.2021 12:11:06 | Герман Ющенко | 04.10.2021 16:31:02 |
| 5666 |              |             | Дмитрий Николаевич  | Харьковский        |            |                 | Руководитель | ИП Смирнова Г.А.                            | Агент           | Анна Епифанова      |       79119234262 |                     | kharkovskii.estate@ya.ru       |                |                              | да        | Анна Епифанова      | 29.09.2021 17:47:19 | Герман Ющенко | 04.10.2021 16:31:00 |
```

> - File path: users_from_eci.csv
> - Total rows: 1373

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)
 |-- email: string (nullable = true)
 |-- photo                               : string (nullable = true)
 |-- phone: string (nullable = true)
 |-- agency: string (nullable = true)
 |-- dateOfBirth: string (nullable = true)
 |-- name: string (nullable = true)
 |-- lastName: string (nullable = true)
 |-- refreshToken                                                                                                                                                 : string (nullable = true)
 |-- createdAt: timestamp (nullable = true)
 |-- updatedAt: timestamp (nullable = true)
 |-- roleId: integer (nullable = true)

```

### Data sample
```
|   id | login       | password                                                     | email                     | photo                                  | phone       | agency               | dateOfBirth   | name             | lastName   | refreshToken                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | createdAt                  | updatedAt                  |   roleId |
|-----:|:------------|:-------------------------------------------------------------|:--------------------------|:---------------------------------------|:------------|:---------------------|:--------------|:-----------------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------|:---------------------------|---------:|
| 1030 | 79818023921 | $2b$10$HeyznXHOS0jnfJI7arVUjOi8n.kbK9eVOZHjGiXrAvz6qt/zozgaO | kotuwko@yandex.ru         |                                        | 79818023921 | Кит-квартира         |               | Ржевская         | Екатерина  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 2023-01-16 18:47:29.955000 | 2023-01-16 18:47:29.955000 |        2 |
| 1104 | 79208408505 | $2b$10$qQcWzQ3dFpX4nxLXISONtOGhs98Awg5emwDSM5CfRvk1S0xeqLT7q | chikova@adresat.spb.ru    |                                        | 79208408505 | Адресат              |               | Чикова           | Ирина      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 2023-02-03 14:03:42.368000 | 2023-02-03 14:03:42.368000 |        2 |
|    7 | 79042621201 | $2b$10$gw8neRdkgftEdOpBZmRuYOS6HbIoYIsd.zFh1gBx.0QAMVFAc66z2 | antonanton@gmail.com      |                                        | 79042621201 | Agent                | 2022-09-30    | Антон            | Антон      | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjcsInJvbGVJZCI6MiwiaWF0IjoxNjY2NTIwMDYxLCJleHAiOjE2NjkxMTIwNjF9.R1cqFc0PNJc3a5gU7B0rMs-I5SwjXRXAPnFjnNCwZTCmO0XnJRcPt9uJK5gnHbFootVlSCep3p5k_la37pi6WqP7F8hOGH0tUJ7mgPEgvIo_vtoiiyHhJ5DjmVeUkpOIzP8Q16vVyetv44PtKxLWOWFiNjdPxCAr4yk2gZZWyYlg_tewHo4okNx3MrPuGsAtDvKToblimXibNZ7uETOXCam1okWoeo4o-VLtWKrcceexPHten_M555j5VRCGgpdmlJn-tM5KOuSnB3cgDhgJXcn62dKBkL_X1WOZrQ6qPQg2Hgs2khuwbEO12TMwy-zw4Lp3BGJRDptnKQRLaG3lfQ     | 2022-09-01 18:56:53.661000 | 2022-10-23 13:14:21.561000 |        2 |
|  288 | 79643608785 | $2b$10$iS2gt1hdXZWFPUxjB6K0wOMaZ3KjExM4.3dSJOMxzB52LzkIKZEI2 | berezneva.vika@mail.ru    |                                        | 79643608785 | Макромир             |               | Березнева        | Виктория   | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI4OCwicm9sZUlkIjoyLCJpYXQiOjE2Njc5MTk4NTQsImV4cCI6MTY3MDUxMTg1NH0.avTKlcBAbXGRC0wSfmHI68VL16LJmAWtQct9jrJbx4NrLJ9FKJEiYkihWJwILlWijEWxiO_3BFpoqSZTIHo0kfVtHMt9UVMFZbJzJP8ZxqQLYI6BZBDsRYB_hESQ2qnkGYKXoMovfi8_hJQwEz4cCWIwu2DLcYNpK0RU3_cMYjoOYlcA7VBD3umAAMM2q_miHdIdMecUOzooi5dbnxQzEdGmU-98DMrViKqX2ONE8pCXY2-EPAGvFs0izHrinRsFZptvb1U4s118T9SjMVC-LNOmNU4BWDGjzHmOne1z3J3AnTLkoBSuQo4AlASVaMgYtprlOB_G1eXhsGYoQonM3w  | 2022-11-07 10:24:58.407000 | 2022-11-08 17:04:14.959000 |        2 |
|  868 | 79052193452 | $2b$10$CdM14i1z3Q7FNTDGg6h.UuahNlOp75hqi3OWC7NO0RI8LbtJr4xMm | mirskaya.valeri@mail.ru   |                                        | 79052193452 | ООО "Империя"        |               | Мирская          | Валерия    | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjg2OCwicm9sZUlkIjoyLCJpYXQiOjE2NzA0MjAwNDQsImV4cCI6MTY3MzAxMjA0NH0.fkCw96zEP9h58fvZy4iRiVnj-vinjG2uvgh3RUQuCmDJ45_ueh70qnp5PBhd9Q4ahUh2QT7qM4I7dJCrG8e4lpNvoQXSN9NjdW5O6HlnQfETXP4PmnQEBMjzvFnhiGI-2w-Gu8bR1-m_uBz63jR6D655hv9ycU3rlUro-bR1aTr50jk9g52JtOP_bTx5FWVq9xLCsrUfsBDvhwxGyVnLq0KiwrMZ8PEyLqwGmxfoxCCfQfhv2wQ9uLiWgyE6V0tcPslqbAlXELDZuGjGvzVlMgafITVLm3bbvlkchqeiPaVIqrgWW0dAv01TSxaF3gGyg-UM3j1z6fy6FoJ88POojA  | 2022-12-07 15:33:40.221000 | 2022-12-07 15:34:04.539000 |        2 |
|   26 | sdgasd      | $2b$10$CxLlZAPfP1jdF7/RCgln4e32LICYHXEYzQRlYTpACmBzqjnm3kUVe | asdasd@asdads.ru          |                                        | 244fssfsf   |                      |               | asdasd           | asdasd     | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI2LCJyb2xlSWQiOjEsImlhdCI6MTY2NTkzNTk3MiwiZXhwIjoxNjY4NTI3OTcyfQ.ZhPFmlF-5uVx_GVcrOIkGjxZx5xur0U4rHmj_Ysi-GGyS70L8EOH2Ym5erkugb3JRT1GpAKCGnTD0AyMKF2DCR73I4AvbX8VKglVIJL9uk5PoxJPHGOUwTdYnScKzIC2d_HXOZFhcdBIS4z_-0xilGc-jWv1CBm-MU7_CcPxtOzwnAG8A4zGAZKAimB5eJeSxCrJU_HAnaaG06Iz_jMFcIlvsNvRk6oyITKysMG7O-2yBRN86szg2oNLCPuqf_hd1vW5oeRVYC9tqkVfe1acGFI2TMmIOOSjVng7LeWjdym1Giyhk0wzspRxgFqlyD58Wqjvt6AivIs_2JYGiDznKw   | 2022-09-16 14:44:47.952000 | 2022-10-16 18:59:32.432000 |        1 |
|   19 | backd       | $2b$10$XMygGARoRwBZz.PDmu09IO3hmih8e2b.vE0GQ32/EDrxCiO/3R4fq | bacdkf@back.ru            |                                        | 79999999992 |                      |               | asdasd           | asdasd     | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjE5LCJyb2xlSWQiOjEsImlhdCI6MTY2MzY2NDM3NSwiZXhwIjoxNjY2MjU2Mzc1fQ.WwcZTBsUVCewfpbGIZSeGtgE7ELAu3c8FSaBR_3jW1EN_gD5Rmo-aMmlJdgVziOcpiHFgXLsm_mKgvgNF0OpoGEwHzlPnUVof1CVawN0-6OynA4C1LflIbHTZP1U1--sxhrbyhwnxsDSe_ig6fLKQ3IcP3afhyWtTxzUfNSmHErL4QIChX3aWCwlRCY1VmifAphpJQLUrqleds3hp4qV9vfgeFOaE_sCVyOje9YTeQelwLU0FcaAYwgk4WyznFOl34pZeDqGBivG4gCibZEU9nlPTKKaFTjMPc48we7gLBl8DEVd9xgiQA7IC_mFlk2-i1PYRLd2kw0lmk62RSomMA   | 2022-09-14 18:24:39.318000 | 2022-09-20 11:59:35.143000 |        1 |
|   12 | sdasd       | $2b$10$SiWa5kfQ.2fyGeZiq4DwmuIRGbJwOs4GDkLy2Sz63odi98A7PNSjS | back@back.ru              |                                        | 1           |                      |               | asdasd           | asdasd     | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEyLCJyb2xlSWQiOjEsImlhdCI6MTY2NDAxODk4OCwiZXhwIjoxNjY2NjEwOTg4fQ.LK_X7sgH10U7JeQqFHDxae3KmWVHlqPaftZEWqGPBsHUYM1LC8Z7UtqD6UEUDwtsRl5Efz464nm77qcps83sztQsvOcEJ5DmtCjJHckZqcxv3lt7b4K-1ebGNZ3OZRNMUBivnrZQ3LbyHT_uV07AVwLFl7tRtbIRJ-lBKG6nL465Vhaj7kAgD1N9Rlqx37s_bN_kQbA5zlbImoi-mUMlqWDvSZYKFBdfQP1hrRTevkeBDdGoOjOUpGf86YIHXjYrOJbUYod5Im55wxyghTVH4FnKZSYeRjAjzGh7EgTGgEPu58TUXYGVqacW3IcwjhRZoE0Y6EB1UlUcuEaYrvi_WA   | 2022-09-14 18:14:50.102000 | 2022-09-24 14:29:48.101000 |        1 |
|  530 | 79123323974 | $2b$10$.tdrK74j8tWD0m8xl36Qb.BkEUxNSTa1Es1wH0DAx/zCYVPPG4N4O | apriori.78@yandex.ru      |                                        | 79123323974 | Макромир             |               | Громова          | Ольга      | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjUzMCwicm9sZUlkIjoyLCJpYXQiOjE2Njk4ODAwNDUsImV4cCI6MTY3MjQ3MjA0NX0.lMifrV-IJTmsBa9bhVcJleK4NCkx0AcF4DE4LKwoQGaKfBrwgoqNA1ac6ccSznko8yEG3-CQJSPbmAsYCjb9ae-PHzf2u0_hRAZJ-4QDInaKPYaIcOPmpCclV0-AbQBC2fT-Pp9fhmT2F_wahulVzTtieeTS5Pa8GkZFSV0Bowr71JHyb5FoiLVB_P97IKbfYEpn0DoZKRjq5NdXNGnQwtaPKqfGK3czEqk8TJpmBqRfyxxwrT8s2B4L7Irh20mZe_ofgnIPQjaLmMQKtP09q7n4PWHFKLLNPNu4rnxtr3iyLbCjr15pw_U4rVEXyS8RtOS0Ve5Y9L0kHFEje6vv5A  | 2022-11-07 15:48:10.137000 | 2022-12-01 09:34:05.686000 |        2 |
|  332 | 79117403575 | $2b$10$VsgRwTCtH5YN0NBI1cjxDuigbXtT6cUp78WJZ7a2oLjBd7PHf//nq | gal777@inbox.ru           |                                        | 79117403575 | Макромир             |               | Дильдина         | Галина     | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjMzMiwicm9sZUlkIjoyLCJpYXQiOjE2Njg0MjM0NjQsImV4cCI6MTY3MTAxNTQ2NH0.W64Cc-v315otRT-35lPU-GAMwjnaP6rj4TH5jvszG_CP2o04uzN5xh-tkjiTTl5pZFNS0Em892KNCQccq1JY6JL3KZAS-P9bHHXHXjvTqElPk8XuHdSrkviV75_Ob-MnOIOE5BjHPqLLSZdG6UV4rnWg_N9-2fTnsamzSJZ_fJZdxYwA1gT_taRTqk1nGZt4rO5SGjIvOl0kd09LdBg5gaUlVhb9pseNSIIQC_hCU7pZjOrF_mj9NDunnQIzqwC0sq4s3p0WMvd1mmoXL5OxuVqQIoIJXZrmqj62Zq7DTTkusmgNpOZSj89_5Apa-Vt2_4CohGPchs2vS6-IH1wWRg  | 2022-11-07 11:36:20.946000 | 2022-11-14 12:57:44.083000 |        2 |
|  292 | 79214173787 | $2b$10$1SrYo8XENpOltX3VjxAnDO7YatgDFTDiINEdwrWHRyvOPxP2P3ozS | t89214173787@gmail.com    |                                        | 79214173787 | Макромир             |               | Валько           | Татьяна    | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI5Miwicm9sZUlkIjoyLCJpYXQiOjE2NjkxMTA1MTMsImV4cCI6MTY3MTcwMjUxM30.Ri7FSWxuoNskcR3lokPOGKk2K0f40dRSLoW9DpH_SCSdGJcUaku9FUPLIORbxfEqfhLkRMHlH8HYTpn3Rw6XKbfHup-x6ig3eOBlcAS_08CPPA5reJS-qISlgOuyZMvIN_jiUViFR1Qy-LDiraDtn6ib3888oJNmLVE8Xm5ffcBcfFnFvvOc_ZEeeIBDwC7xb4yIjT8hbg4bwImlaNx8TCZL06EEo18mqX0jeVxLOpv4sorRkGo30lHNE06xOH3yndzDcDoTOF_HLdFgPmzCFLNbN8egXsg-lXnVFBuwDYYdnKYZH4O_ZFwQm1ftYSrdMqjjMkFceF0YzXnK2YBWYA  | 2022-11-07 10:26:50.074000 | 2022-11-22 11:48:33.771000 |        2 |
|   44 | 79184150415 | $2b$10$NS.k/zrMFN/oa7FUEzlAhOnUT7jVW6FSGD9LRlpHGeOCAjnhpl/Cm | itsfamwely@mwail.ru       |                                        | 79184150415 | Тестовая компания на |               | Грригорий тесттт |            | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjQ0LCJyb2xlSWQiOjIsImlhdCI6MTY2NjUzMDA5MywiZXhwIjoxNjY5MTIyMDkzfQ.jvhLnhtqx-ZMm3yvioEX72UyMKnbs_uR4MIYvOPu_1JueopmJ58ZR7sGikpsxeD-uHW0j3sXajRm32kbK2fuz4CIofAUU6pZUJplKAuejjcjvluvOf7efEZP7NgfDAnJ2ssvnsPA7ve3IQIq-7d3y2-Hbx7lN3KA8Hs9VRGY-AgyFrScHnzNqD8gxzK8kkkcWjZpeuj6QsauemRnwATPpDkRwI_gY3I1qovl8H6cOf6XzoXFb2Le4fyNbv0Gu2AEHo1E74JXrmedGlu7MK8APQKwBjkp3EVlnW2PSheEZdBjAyXBlznsiKOVScLNmNPaTTZoq4MJ4vvhz8nyutE64w   | 2022-10-23 15:03:51.606000 | 2022-10-23 16:01:33.342000 |        2 |
|  742 | 79956296790 | $2b$10$lGuG6gyYm3bBMJ5vgVNcGu/YZKUZGbTyGdbBWAeZPCqTUcYIQXsCq | pd888242@yandex.ru        |                                        | 79956296790 | самозанятая          | 1971-03-22    | Киселева         | Марина     | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjc0Miwicm9sZUlkIjoyLCJpYXQiOjE2NjkxMjE1MTgsImV4cCI6MTY3MTcxMzUxOH0.cdp1rMxw9Wuw1WXzYmG9kOkQFdtbsCJJNKmnlY6YtL7LORrt-4rbNIKGyD6BTgBptJSPHjRird7VALjjWucNgScrQR0LbTDVyysKmv6DePtkUzAV_s4uJWRDl2l6p-x-WRByFCsTXcprUfcYkaopOhAWVAN0W4656kszB39JRnMBVaGILzf_4UXpoRPSvn6gBuxwNyOS_jsAAttFBYO_GlUsetnExMttOGG1byxNNIcwGLVHePuOChvAEIHkuTD_sxwtJHfgC8of07LAwm7_fQMSOZ5PJka-cSOi1f_9ISMBrAVBZ5wi3FWUBx1PFKP7Tq101LM9ff3tE5KTY1ROXg  | 2022-11-22 12:35:57.812000 | 2022-11-22 14:51:58.822000 |        2 |
| 1779 | 79213299468 | $2b$10$tXAVA3rE4QnpCAponP7fG.bvM0k.miKvyzPlah8l0bDSYaX9X8eci | nadkathegreat@gmail.com   |                                        | 79213299468 | ИП Брызгалова ОА     |               | Фролова          | Надежда    | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjE3NzksInJvbGVJZCI6MiwiaWF0IjoxNjg1NDMzNTU0LCJleHAiOjE2ODgwMjU1NTR9.MqmiTAdhbooAJv-i-DT03iL24GbUScTSxrF3-UbOykDkIsC2Nxo6au_nJHDy-3nwg7HcgqwQcG7WxoNZY3AOxNZSDBm2WR3uuNqgOkYzFx6dr3PDpG6wQKec9PIvc-ie6bK-q5brNeqBQA1RyI6abeMUCm8_cSV6Y2-dIRwVJcUnAFEcClZmRlOyTm1hMTZpXaTvp0Bd0tBf0TyTn4ZXm3GSZRupsYAG0GX-pCIB_n3gVNPnN_FN-WoKafTTNs2VXm24EzLX8Phm4pzyTWFR1znll-N3x6OFVg10eRj2XsP8SvG0sqrCNGlvzDU-PGlMgTTcr2dnxNLOk8oFLUuLdw | 2023-05-30 10:45:56.767000 | 2023-05-30 10:59:14.451000 |        2 |
|   29 | login       | $2b$10$mJ.Q9TC17MqH3XPPN1tMBuZ9BKgun6DJK31MAv53Ka2Q3VZC.jx2G | mail@mail.ru              |                                        | 71231231231 |                      |               | Imya             | Familiya   | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI5LCJyb2xlSWQiOjEsImlhdCI6MTY2NjA0MzYxMCwiZXhwIjoxNjY4NjM1NjEwfQ.V-IXyVbVukZ4Q7Tm20dixdbx_13Iettfo8VOzaFi2cDolf8wcWZoP3c4kz0qQKR3hbJBm5mLqWSflIAxB6FynvfRFfdzy-n3LseX2LsL-T_eem71HVpjyZInBB5JxQrw_IZyfPs5W3ZpRQnXdRctW51F-XdAPjaVeN7cU8iB_yJD0Fsq4liCS2QpSOf8AtRu0VeFzXNQXwdaZ-UV5ehj1lGVjByn1jO3blTT2sIt2_Ie5I40LErBsFoIyM4aUjQ97-YWkR-mroiGVwCDaZRx6ipSXKU-Oh0QwkHjv7PHC_bmi53-9TT05zdJTg4UyixyQOVDN7OvJaWhZbTMBIhQzA   | 2022-09-29 11:04:04.971000 | 2022-10-18 00:53:30.430000 |        1 |
|  632 | 79829333434 | $2b$10$HqMIwPlf4eCZgde4T2TIDujQX2A7wc7bVqe8q3XSZWPlZsogTky7. | dombrovskyi@tochkadom.com | Сжатая1675467826218.jpg                | 79829333434 | ТОЧКАДОМ             | 1982-10-10    | Домбровский      | Денис      | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjYzMiwicm9sZUlkIjoyLCJpYXQiOjE2ODIwNjA1NDksImV4cCI6MTY4NDY1MjU0OX0.AUp8xbzeYLjD_Ej2o-TiGwdzMQro2DAWcHHJ31S6njB2D2mqF1iFCo-eeMdAGTavxCr_UN8wdoc7DaIJZtDhd7CF250sYdmsys3aIyZ0SRri6Qv1gZPaL4BZgNgKKQ-orA62sM7D9itfEh_PtFrbAifhidq6LJGwL0GEJvv6VB-sHjKfvYwLYbqkIYHzRPfIbIU9jlv41Sjhkz-vXccbSevPkxXKbUzB85snZdd_liZZZvUH8etFUt1c8mDEPRFeVLZfMlFxZHw2a9k3WubCljKEzfnpCPmUKxzh0sIjG8ERvBzlAeCz-eVHp331nGdGU5QH02eqRbJkj1nvivYp2w  | 2022-11-11 14:12:44.985000 | 2023-04-21 10:02:29.421000 |        2 |
| 1086 | 79959975214 | $2b$10$Kou.Ywbw/i45lmUTKPZr0.JX0HF6pFWABxMVPDrBL6OrbYTDCeIOe | romanova@adresat.spb.ru   |                                        | 79959975214 | Адресат              |               | Воробьева        | Лариса     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 2023-02-03 12:36:47.194000 | 2023-02-03 12:36:47.194000 |        2 |
|   52 | timur       | $2b$10$3v1zVMETNpHACNLDxdrKVO42bbBOWOEm1eoGIpzfcgVZDIjZq0u/y | agrrent@mail.com          |                                        | 79925016214 |                      |               | timur            | manager    | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjUyLCJyb2xlSWQiOjEsImlhdCI6MTY2Njg0NDUzMCwiZXhwIjoxNjY5NDM2NTMwfQ.AMnIWHw0YURCUSCdWOg_EV7D3NSpJdC67BE66LGtd3sudKvzBMHI691qSW6znxrtgooB_6IRuki1nnCBObMM3zz9rCQy3pmegVjUF63VwIMFkqxYhR3xwHgOQB5Amzd78df18-mTm0dnGravTxp6tEgCsDZAuVz33ACa6tjGyY-Ex3e57GS1H0eQhKOggPqlnGDe5_4GtUthtb8pCZ-TnVZ1-ThvRpdstUPjR3rXJ03iWKqFceeXEtdGkTIBvGxWPw0bzFTolBITINoKZW7ffhzJmPRUIaSkhhiBiQddVWldjk6ur0-Mu-t5jL1TVGZalv891oygrfSnyx38ORaBxQ   | 2022-10-24 16:30:54.750000 | 2022-10-27 07:22:10.581000 |        1 |
|  694 | 79219494131 | $2b$10$105rugwm/EZVpvAUIRQNu.PKVdzI2FOV5iOL2eNTZlOKu08Rvygli | Tolkachev@kvadratspb.ru   |                                        | 79219494131 | Квадрат Estate       |               | Толкачёв         | Александр  | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjY5NCwicm9sZUlkIjoyLCJpYXQiOjE2ODMwMzUxNDIsImV4cCI6MTY4NTYyNzE0Mn0.FqWtXdQYlQ8xwAA1mXPY5jBIW2S3WULfrrht0vsMbeHpud9-coHk3UATmpDcpJusMk-gFnXXBHN_5Y8XWMSEbQxgo-K3LchqbbqLmDbaL5jUDFqgfxdHv9dw0clwmRT_z3xWI5nMF8DhK69qf8KRhOajQt18HeaFhrVdtnOjzN4AvGVH4Ynp1-aMkduD2mf3DMK6nxC9zNACN4koCsVcBcOs0FMa5fCYq3GIh5q-XwpAnUjqJURt2RGIrbY6Wtjx1u0YUd6WZp9OpC3NBdVyVS6xPC-ylNziSYm2REdvt6mldi6AI-TZN_PelUO_bpnZWMNsuu6f2bKb0U2xD05lTw  | 2022-11-16 15:11:28.318000 | 2023-05-02 16:45:42.287000 |        2 |
| 1106 | 79098312060 | $2b$10$/Ml4XY7ou6NeuYXueSFUDe4J.SZnbUm7dsSZ9m7VGmMSsry3ELz5G | isaeva@adresat.spb.ru     |                                        | 79098312060 | Адресат              |               | Исаева           | Надежда    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 2023-02-03 14:05:24.846000 | 2023-02-03 14:05:24.846000 |        2 |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- actuality: date (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 0.04% |
| Phones | 99.66% |
| Emails | 86.10% |
| Works | 71.95% |
| Actuality | 6.25% |
| Accounts | 20.12% |
| Raw_metadata | 19.83% |



### Data sample
```
| names                                 | birth_date   | phones          | emails                              | works                                                                                                                | actuality   | accounts   | raw_metadata   |
|:--------------------------------------|:-------------|:----------------|:------------------------------------|:---------------------------------------------------------------------------------------------------------------------|:------------|:-----------|:---------------|
| ['Андрей Панов']                      |              | ['79992144940'] | ['a.panov@advise.ru']               | [Row(post=None, date_start=None, date_end=None, company='Advise', address=None, comment=None)]                       |             |            |                |
| ['Баранович Денис Леонидович']        |              | ['79119087309'] | ['d.pro-realt@yandex.ru']           | [Row(post=None, date_start=None, date_end=None, company='Счастливый город', address=None, comment=None)]             |             |            |                |
| ['Баянов Владимир Алексеевич']        |              | ['79627293333'] | ['7293333@mail.ru']                 | [Row(post=None, date_start=None, date_end=None, company='ИП Баянов В.А.', address=None, comment=None)]               |             |            |                |
| ['Бирюкова Ирина Валерьевна']         |              | ['79650510145'] | ['89650510145@perspektiva24.com']   | [Row(post=None, date_start=None, date_end=None, company='Перспектива24-Приморский', address=None, comment=None)]     |             |            |                |
| ['Бронникова Антонина Александровна'] |              | ['79112232221'] | ['antonina@agn178.ru']              | [Row(post=None, date_start=None, date_end=None, company='Недвижимость 178', address=None, comment=None)]             |             |            |                |
| ['Ващенко Максим Игоревич']           |              | ['79214012316'] | ['vmi@flatvspb.ru']                 | [Row(post=None, date_start=None, date_end=None, company='АН Флэт в СПб flat v spb', address=None, comment=None)]     |             |            |                |
| ['Вера']                              |              | ['79673410171'] |                                     | [Row(post=None, date_start=None, date_end=None, company='Октава', address=None, comment=None)]                       |             |            |                |
| ['Власова Елена Алексеевна']          |              | ['79052125117'] | ['dania59@list.ru']                 | [Row(post=None, date_start=None, date_end=None, company='АН Макромир', address=None, comment=None)]                  |             |            |                |
| ['Ирина']                             |              | ['79052257046'] | ['alen2255.64@yandex.ru']           | [Row(post=None, date_start=None, date_end=None, company='АН Недвижимость в Петербурге', address=None, comment=None)] |             |            |                |
| ['Ковалева Ольга Валерьевна']         |              | ['79319935051'] | ['935051@mail.ru']                  | [Row(post=None, date_start=None, date_end=None, company='НЕВА Недвижимость', address=None, comment=None)]            |             |            |                |
| ['Ковалевич Елена Викторовна']        |              | ['79062251327'] | ['kovaleviche@mail.ru']             | [Row(post=None, date_start=None, date_end=None, company='ООО ВВС-Брокер', address=None, comment=None)]               |             |            |                |
| ['Кондратьева Маргарита Николаевна']  |              | ['79062735820'] | ['kondrateva@mirndv.ru']            | [Row(post=None, date_start=None, date_end=None, company='ООО МН Групп', address=None, comment=None)]                 |             |            |                |
| ['Личутина Ольга Александровна']      |              | ['79516806809'] | ['lichutichu@gmail.com']            | [Row(post=None, date_start=None, date_end=None, company='ИП Горбачевский О.Н.', address=None, comment=None)]         |             |            |                |
| ['Максимова Марина']                  |              | ['79052227096'] | ['mmv@petropol.ru']                 | [Row(post=None, date_start=None, date_end=None, company='АН Петрополь', address=None, comment=None)]                 |             |            |                |
| ['Никешина Марина Анатольевна']       |              | ['79650803581'] | ['mnikeshina@bk.ru']                | [Row(post=None, date_start=None, date_end=None, company='АН Арго-Недвижимость', address=None, comment=None)]         |             |            |                |
| ['Павлова Александра Петровна']       |              | ['79657940115'] | ['alexandra.pavlova@langesmith.ru'] | [Row(post=None, date_start=None, date_end=None, company='LangeSmith', address=None, comment=None)]                   |             |            |                |
| ['Ревягин Сергей Вячеславович']       |              | ['79523704444'] | ['s3704444@yandex.ru']              | [Row(post=None, date_start=None, date_end=None, company='Мой риэлтор', address=None, comment=None)]                  |             |            |                |
| ['Сабина Комарова']                   |              | ['79110180555'] | ['komarova@metrika72.ru']           | [Row(post=None, date_start=None, date_end=None, company='АН Метрика Недвижимость', address=None, comment=None)]      |             |            |                |
| ['Светлова Камилла Абдуловна']        |              | ['79213256739'] | ['svetlova@szvdom.ru']              | [Row(post=None, date_start=None, date_end=None, company='АН Созвездие Недвижимости', address=None, comment=None)]    |             |            |                |
| ['Сивакова Елена']                    |              | ['79213770304'] | ['es.sivakova@gmail.com']           | [Row(post=None, date_start=None, date_end=None, company='DOMINION', address=None, comment=None)]                     |             |            |                |
```