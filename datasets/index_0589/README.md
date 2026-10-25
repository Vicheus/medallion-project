# Parsetron results

## About row data

> - Code name: index_0589
> - File path: kustanas.com.csv
> - Total rows: 38876

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
|   PhoneNumber | Name            | Email                           |   MagnetCards | Comment   | WhenCreated         |
|--------------:|:----------------|:--------------------------------|--------------:|:----------|:--------------------|
|  +99999999999 | Гггш            |                                 |               |           | 01.11.2022 23:14:29 |
| +959456085468 | Тимур Осипов    |                                 |  699554681322 |           | 24.08.2025 21:48:42 |
|  +91240340530 | анна            |                                 |               |           | 09.12.2023 20:37:27 |
|  +90935374930 | розалия         |                                 |               |           | 09.12.2023 9:09:21  |
|  +89997642818 | гульдария       |                                 |               |           | 03.11.2023 11:00:52 |
|  +89997424071 | раиль           |                                 |               |           | 02.12.2023 15:23:42 |
|  +89997247342 | ильгам          |                                 |               |           | 21.12.2023 14:57:45 |
| +899966230734 | Рина            |                                 |               |           | 20.10.2022 10:16:00 |
|  +89996236865 | Рената          |                                 |               |           | 14.11.2023 12:05:22 |
|  +89996235906 | Альфия альфия   | alfiyaasadullina1993@gmail. com |               |           | 09.12.2023 14:06:33 |
|  +89996231724 | Дмитрий дмитрий | beshkarevdimas@gmail.com        |               |           | 08.11.2023 13:13:26 |
|  +89996230703 | н               |                                 |               |           | 08.04.2025 18:28:52 |
|  +89996223093 | эльмира         |                                 |               |           | 19.10.2023 14:08:30 |
|  +89995893046 | елена           |                                 |               |           | 09.12.2023 13:35:12 |
|  +89995884497 | татьяна         |                                 |               |           | 26.11.2023 17:54:50 |
|  +89995881668 | Гулия           |                                 |               |           | 21.10.2023 19:47:10 |
|  +89995836481 | андрей          |                                 |               |           | 04.11.2023 13:22:38 |
|  +89995829870 | Юлия Юлия       | burangulova2301@gmail.com       |               |           | 04.12.2023 18:22:11 |
|  +89995708701 | алексей         |                                 |               |           | 19.11.2023 8:03:50  |
|  +89991764157 | АЙЛИНА          |                                 |               |           | 26.10.2023 17:25:41 |
```


## About final data
> - Total rows: 28894

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
| Emails | 21.22% |
| Phones | 99.87% |
| Actuality | 100.00% |
| Raw_metadata | 13.05% |



### Data sample
```
| names                 | emails                              | phones   | actuality   | raw_metadata   |
|:----------------------|:------------------------------------|:---------|:------------|:---------------|
| ['Дмитрий Дмитрий']   | ['beshkarevdimas@gmail.com']        |          | 08.11.2023  |                |
| ['Юлия Юлия']         | ['burangulova2301@gmail.com']       |          | 04.12.2023  |                |
| ['Регина Регина']     | ['reginaarmuhametova941@gmail.com'] |          | 09.12.2023  |                |
| ['Дарья Дарья']       | ['darya.trofimova.2002@bk.ru']      |          | 02.12.2023  |                |
| ['Карина Карина']     | ['deduseva98@bk.ru']                |          | 02.12.2023  |                |
| ['Салия Салия']       | ['shamsika17@gmail.com']            |          | 20.10.2023  |                |
| ['Регина Регина']     | ['nazarovaregina27@gmail.com']      |          | 03.12.2023  |                |
| ['Ольга Ольга']       | ['olga.stats@mail.ru']              |          | 11.11.2023  |                |
| ['Айдар Айдар']       | ['aidar.davle@gmail.com']           |          | 11.11.2023  |                |
| ['Азалия Азалия']     | ['azaliea26@mail.ru']               |          | 26.10.2023  |                |
| ['Карта Азалия']      | ['marchenko481@gmail.com']          |          | 17.12.2023  |                |
| ['Элизабет Элизабет'] | ['elizabet.yunusbaeva@mail.ru']     |          | 18.12.2023  |                |
| ['Гульназ Гульназ']   | ['gulnazocka@icloud.com']           |          | 26.11.2023  |                |
| ['Валеева Лиана']     | ['lvaleeva662@gmail.com']           |          | 10.04.2025  |                |
| ['Лиза Лиза']         | ['lizapaskidova@mail.ru']           |          | 14.12.2023  |                |
| ['Наталья']           | ['hamatalina06@mail.ru']            |          | 26.07.2024  |                |
| ['Зульфия Зульфия']   | ['zymasheva@gmail.com']             |          | 16.11.2023  |                |
| ['Фания Фания']       | ['faniya.barmakova@mail.ru']        |          | 09.12.2023  |                |
| ['Лиана Лиана']       | ['yulanova.liana@mail.ru']          |          | 02.12.2023  |                |
| ['Розалия Розалия']   | ['timerbaeva_rozaliya@mail.ru']     |          | 03.12.2023  |                |
```