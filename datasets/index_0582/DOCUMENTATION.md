# Parsetron results

## About row data

> - File path: Del Mar.csv
> - Total rows: 48540

### Schema
```
root
 |-- PhoneNumber: string (nullable = true)
 |-- Name: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- MagnetCards: string (nullable = true)
 |-- Comment: string (nullable = true)
 |-- WhenCreated: string (nullable = true)

```

### Data sample
```
|   PhoneNumber | Name                           | Email                   |   MagnetCards | Comment   | WhenCreated         |
|--------------:|:-------------------------------|:------------------------|--------------:|:----------|:--------------------|
|   79851785563 | Владимир                       |                         |               |           | 29.05.2023 22:09:47 |
|   79183013046 | Кокоева Елена Алексеевна       |                         |               |           | 10.09.2024 17:27:49 |
|   79267370480 | Наталья                        | Umniza2005@yandex.ru    |        101584 |           | 12.09.2020 13:36:09 |
|   79051111222 | СВЕТЛАНА                       |                         |               |           | 22.03.2021 17:07:50 |
|   79853895276 | Сергей                         | dsergi332@gmail.com     |          1655 |           | 11.04.2022 10:35:49 |
|   79890907070 | Лика                           | lika89.08@mail.ru       |        400034 |           | 21.03.2020 12:49:03 |
|               | Наталья Шарабарина             |                         |          2051 |           | 25.06.2023 10:58:57 |
|   79057925755 | СВЕТЛАНА                       |                         |          3014 |           | 09.08.2022 10:57:13 |
|   79035935268 | СТАНИСЛАВ                      |                         |          3048 |           | 31.07.2022 17:23:57 |
|   79147312955 | Малиновская елена              | Lena-Nasonova@yandex.ru |       1005594 |           | 10.12.2021 18:03:23 |
|   79111993370 | Abakumova Marina Александровна |                         |               |           | 12.01.2023 14:25:44 |
|   79881845225 | ABDRAKHMANOV RATMIR            | ratmir.atc@gmail.com    |        102317 |           | 17.11.2020 13:16:04 |
|   79282344278 | Abramova Natali                |                         |               |           | 30.10.2022 17:26:11 |
|   79625010008 | Afanasyeva Natalia             |                         |      30002016 |           | 13.09.2021 12:18:31 |
|   79182002029 | afonkina Alisa                 |                         |          4483 |           | 17.12.2019 18:17:23 |
|   79857890973 | Afonskaya Evgeniya             |                         |               |           | 09.03.2025 17:36:52 |
|   79263555758 | Agapov Sergey                  | agapovs@mail.ru         |       1009294 |           | 28.10.2022 19:07:57 |
|   79175540777 | Ageeva Inga                    | eternity116@gmail.com   |       1002132 |           | 08.05.2021 14:05:13 |
|   79172990755 | Akberov Tin                    |                         |               |           | 07.01.2024 10:23:15 |
|   79610727528 | Akhanova Anastasiya            | Aahanova@gmail.com      |       4002348 |           | 16.09.2021 12:36:13 |
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
 |-- actuality: date (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 50.19% |
| Phones | 99.77% |
| Actuality | 100.00% |
| Raw_metadata | 56.61% |



### Data sample
```
| names                              | emails                           | phones          | actuality   | raw_metadata                    |
|:-----------------------------------|:---------------------------------|:----------------|:------------|:--------------------------------|
| ['Полозов Александр']              | ['aleksandr_polozov@rambler.ru'] | ['79000000026'] | 17.08.2022  | ['{"MagnetCards": "4004145"}']  |
| ['Кулиева Ева']                    | ['kulieva19987@gmail.com']       | ['79006251897'] | 12.12.2021  | ['{"MagnetCards": "1005636"}']  |
| ['Лапшина Наталья']                |                                  | ['79025149782'] | 11.05.2021  |                                 |
| ['Фотина Ольга']                   | ['olg3326747@yandex.ru']         | ['79027951612'] | 29.07.2021  | ['{"MagnetCards": "1003830"}']  |
| ['Селезнев Николай Анатольевич']   |                                  | ['79030794966'] | 12.02.2024  |                                 |
| ['Кузьмин Антон']                  | ['kuzmin-36@yandex.ru']          | ['79031300999'] | 17.07.2020  | ['{"MagnetCards": "300724"}']   |
| ['Михайлова Анас']                 | ['cherry158@yandex.ru']          | ['79032106244'] | 07.08.2021  | ['{"MagnetCards": "1004018"}']  |
| ['Уваров Юрий']                    |                                  | ['79033216332'] | 12.09.2025  |                                 |
| ['Алёшкина Ирина']                 |                                  | ['79033857940'] | 13.09.2024  |                                 |
| ['Сидоров Станислав']              | ['styles@mail.ru']               | ['79035736898'] | 14.03.2021  | ['{"MagnetCards": "1001068"}']  |
| ['Сырецких Александр']             |                                  | ['79035847489'] | 17.12.2019  | ['{"MagnetCards": "899"}']      |
| ['Голос Светлана']                 | ['kmglazkov@yandex.ru']          | ['79037915026'] | 19.07.2021  | ['{"MagnetCards": "1003677"}']  |
| ['Казаров Артем']                  |                                  | ['79043696969'] | 21.06.2022  | ['{"MagnetCards": "1007471"}']  |
| ['Стрельцова Татьяна Стрельцова']  |                                  | ['79044839111'] | 03.07.2021  | ['{"MagnetCards": "30001607"}'] |
| ['Елауркина Евгения']              | ['komarik336@yandex.ru']         | ['79045768263'] | 20.03.2020  | ['{"MagnetCards": "400031"}']   |
| ['Морозов Дмитрий']                |                                  | ['79046116209'] | 07.06.2024  |                                 |
| ['Ребрин Виталий']                 | ['vtrebtin@gmail.com']           | ['79050649410'] | 19.08.2021  | ['{"MagnetCards": "4002097"}']  |
| ['Мамина Елена']                   | ['emoiseeva84@mail.ru']          | ['79055333340'] | 01.01.2021  | ['{"MagnetCards": "1000060"}']  |
| ['Меньшакова Светлана Николаевна'] |                                  | ['79055804419'] | 13.02.2024  |                                 |
| ['Морозова Анна']                  | ['agavve@yandex.ru']             | ['79055884425'] | 30.05.2022  | ['{"MagnetCards": "1007222"}']  |
```