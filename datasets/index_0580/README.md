# Parsetron results

## About row data

> - Code name: index_0580
> - File path: Chang Family ЦO.csv
> - Total rows: 55455

### Schema
```
root
 |-- PhoneNumber: long (nullable = true)
 |-- Name: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- MagnetCards: string (nullable = true)
 |-- Comment: string (nullable = true)
 |-- WhenCreated: string (nullable = true)
 |-- _c6: string (nullable = true)

```

### Data sample
```
|   PhoneNumber | Name   | Email   |   MagnetCards | Comment   | WhenCreated         | _c6   |
|--------------:|:-------|:--------|--------------:|:----------|:--------------------|:------|
|   7.98191e+10 |        |         |   79819101099 |           | 16.01.2026 20:28:02 |       |
|   7.93124e+10 |        |         |   79312388338 |           | 09.12.2025 22:36:01 |       |
|   7.91833e+10 |        |         |               |           | 06.12.2025 18:12:30 |       |
|   7.90456e+10 |        |         |   79045555743 |           | 25.10.2025 17:27:01 |       |
|   7.91172e+10 |        |         |   79117246632 |           | 18.01.2026 16:39:01 |       |
|   7.91111e+10 |        |         |   79111118129 |           | 16.12.2025 22:09:01 |       |
|   7.91117e+10 |        |         |               |           | 06.12.2024 15:39:03 |       |
| nan           |        |         |        970001 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |        970002 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |        970003 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |        970004 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |        970005 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |        970006 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |        970007 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |        970008 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |        970009 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |        970010 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |        970011 |           | 19.01.2024 15:06:59 |       |
| nan           |        |         |       9700129 |           | 15.12.2022 21:52:52 |       |
| nan           |        |         |        970012 |           | 30.11.2022 22:30:14 |       |
```


## About final data
> - Total rows: 20924

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
| Emails | 4.66% |
| Phones | 99.87% |
| Actuality | 87.17% |
| Raw_metadata | 27.78% |



### Data sample
```
| names                     | emails                          | phones          | actuality   | raw_metadata                       |
|:--------------------------|:--------------------------------|:----------------|:------------|:-----------------------------------|
| ['Alexander Serebryakov'] | ['serebryakov.all@gmail.com']   |                 | 09.06.2025  |                                    |
| ['Daria Sidorova']        | ['darsid@yandex.ru']            | ['79213193609'] | 31.05.2024  |                                    |
| ['Irina Gabi']            | ['irinagaby@icloud.com']        | ['79111215406'] | 18.08.2024  |                                    |
| ['Kristina G V']          | ['kristinagregory89@gmail.com'] | ['79818712107'] | 12.07.2025  |                                    |
| ['Luda']                  | ['blg80@yandex.ru']             | ['79152160008'] | 14.07.2024  |                                    |
| ['Mariia Plygun']         | ['termi89@gmail.com']           | ['79219765356'] | 09.06.2025  |                                    |
| ['Radik']                 | ['ronnikkip@mail.ru']           | ['79674627621'] | 09.08.2025  | ['{"MagnetCards": "79674627621"}'] |
| ['Sergey Gridnev']        | ['chycoff@gmail.com']           | ['79166314576'] | 10.09.2025  |                                    |
| ['Tanya Shatokhina']      | ['shato.ha@gmail.com']          | ['79117902427'] | 06.09.2024  |                                    |
| ['Vera']                  | ['v.polushkina@gmail.com']      | ['79006532295'] | 03.09.2022  |                                    |
| ['Vladimir']              | ['cat.007@mail.ru']             | ['79117622407'] | 04.05.2024  |                                    |
| ['Алексан']               | ['neo36ru@mail.ru']             | ['79092123452'] | 13.06.2025  |                                    |
| ['Александр']             | ['zendaun@mail.ru']             | ['79819661315'] | 09.06.2025  |                                    |
| ['Александр']             | ['antonenko96@list.ru']         | ['79803749727'] | 15.07.2024  |                                    |
| ['Александр']             | ['alexmangt540@gmail.com']      | ['79643744162'] | 09.06.2025  |                                    |
| ['Александр']             | ['xtrimal@bk.ru']               | ['79609107040'] | 02.08.2025  |                                    |
| ['Александр']             | ['bubnov_ay@icloud.com']        | ['79219538927'] | 29.05.2024  |                                    |
| ['Александр']             | ['perikl@yandex.ru']            | ['79215786773'] | 14.07.2024  |                                    |
| ['Александр']             | ['frax-infium@yandex.ru']       | ['79215653324'] | 04.07.2024  | ['{"MagnetCards": "79215653324"}'] |
| ['Александр']             | ['sauromusic@gmail.com']        | ['79213468376'] | 03.08.2024  |                                    |
```