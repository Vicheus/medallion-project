# Parsetron results

## About row data

> - File path: grnhs.ru.csv
> - Total rows: 231895

### Schema
```
root
 |-- PhoneNumber: long (nullable = true)
 |-- Name: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- MagnetCards: string (nullable = true)
 |-- Comment: string (nullable = true)
 |-- WhenCreated: string (nullable = true)

```

### Data sample
```
|   PhoneNumber | Name              | Email                        | MagnetCards   | Comment   | WhenCreated         |
|--------------:|:------------------|:-----------------------------|:--------------|:----------|:--------------------|
|   99964297573 | Сергей            |                              |               |           | 17.08.2022 5:09:36  |
|  998993820928 | Алина             | alinatahirova769@gmail.ru    |               |           | 26.12.2020 8:25:45  |
|  998933440369 | Jovid             | Djanik2002@mail.tu           |               |           | 29.03.2023 15:40:08 |
|  998914450647 | Манзура           | manzuraboltaeva059@gmail.com |               |           | 26.07.2022 5:40:29  |
|  998913378826 | FUCKTHEPOPULATION | ftpengrus@gmail.com          |               |           | 05.12.2022 15:14:07 |
|   99888898898 | Мартышкина Ариша  |                              |               |           | 27.10.2024 11:41:10 |
|  996555585281 | Таника            | ktanika@mail.ru              |               |           | 25.04.2021 19:47:54 |
|  996550028808 | Dzhaparova        | Particular-09@mail.ru        |               |           | 27.09.2021 7:01:58  |
|  996224246624 | Seiilka           | Seil8686@mail.ru             |               |           | 15.07.2022 14:29:36 |
|   99620768551 | Ирина             |                              |               |           | 26.06.2023 14:06:36 |
|   99605520572 | Марчела           |                              |               |           | 11.06.2023 15:24:26 |
|   98935043512 | Ольга             |                              |               |           | 23.07.2022 7:42:57  |
|  989130520598 | Екатерина         |                              |               |           | 01.03.2020 7:39:47  |
|   98588544043 | Дарья             |                              |               |           | 16.05.2022 18:25:16 |
|  983300623506 | Ларья             |                              |               |           | 24.08.2020 13:37:27 |
|   98264504656 | Софья             |                              |               |           | 26.09.2021 16:29:37 |
|  972587030616 | Наталия           | Yermakova-NB@yandex.ru       |               |           | 10.08.2022 15:44:46 |
|  972539215838 | NATALIA           | enje231@yandex.ru            |               |           | 31.05.2023 6:00:24  |
|  972538270999 | Vitalina          | rashvita13@gmail.com         |               |           | 21.10.2021 11:21:37 |
|  971529320905 | Sahsa             | apolyubez@gmail.com          |               |           | 21.06.2021 10:58:49 |
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
| Emails | 14.70% |
| Phones | 99.86% |
| Actuality | 100.00% |
| Raw_metadata | 5.24% |



### Data sample
```
| names                 | emails                           | phones          | actuality   | raw_metadata   |
|:----------------------|:---------------------------------|:----------------|:------------|:---------------|
| ['Алина']             | ['alinatahirova769@gmail.ru']    |                 | 26.12.2020  |                |
| ['Jovid']             | ['djanik2002@mail.tu']           |                 | 29.03.2023  |                |
| ['Манзура']           | ['manzuraboltaeva059@gmail.com'] |                 | 26.07.2022  |                |
| ['Fuckthepopulation'] | ['ftpengrus@gmail.com']          |                 | 05.12.2022  |                |
| ['Таника']            | ['ktanika@mail.ru']              |                 | 25.04.2021  |                |
| ['Dzhaparova']        | ['particular-09@mail.ru']        |                 | 27.09.2021  |                |
| ['Seiilka']           | ['seil8686@mail.ru']             |                 | 15.07.2022  |                |
| ['Наталия']           | ['yermakova-nb@yandex.ru']       |                 | 10.08.2022  |                |
| ['Natalia']           | ['enje231@yandex.ru']            |                 | 31.05.2023  |                |
| ['Vitalina']          | ['rashvita13@gmail.com']         |                 | 21.10.2021  |                |
| ['Sahsa']             | ['apolyubez@gmail.com']          |                 | 21.06.2021  |                |
| ['Иван']              | ['vanbka13@yandex.ru']           |                 | 05.02.2020  |                |
| ['Ademchivy']         | ['ademchivy1983@gmail.con']      |                 | 07.04.2023  |                |
| ['Aleksandra']        | ['aleksandra.luneva@gmail.com']  |                 | 11.02.2021  |                |
| ['Tati']              | ['t.o.petukhova@gmail.com']      |                 | 16.03.2022  |                |
| ['Никита']            |                                  | ['79874233797'] | 04.08.2021  |                |
| ['Ирина']             |                                  | ['79836189799'] | 17.09.2019  |                |
| ['Марина']            |                                  | ['79833643061'] | 24.06.2019  |                |
| ['Ходакова Алиса']    |                                  | ['79832988824'] | 06.07.2019  |                |
| ['Алена']             |                                  | ['79832026478'] | 22.10.2020  |                |
```