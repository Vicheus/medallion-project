# Parsetron results

## About row data

> - File path: superkopilka.csv
> - Total rows: 299275

### Schema
```
root
 |-- LastName: string (nullable = true)
 |-- FirstName: string (nullable = true)
 |-- Phone: string (nullable = true)
 |-- City: string (nullable = true)
 |-- BirthDate: string (nullable = true)
 |-- Hash: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- Sex: string (nullable = true)
 |-- C0: string (nullable = true)

```

### Data sample
```
| LastName   | FirstName   |       Phone | City            | BirthDate   | Hash                                     | Email                          | Sex   | C0   |
|:-----------|:------------|------------:|:----------------|:------------|:-----------------------------------------|:-------------------------------|:------|:-----|
| Кривцова   | Наталья     | 79092077066 | Белгород        | 07.09.1984  | fd113124e718eced7f4e94b25c852da26c6fb1a3 | n.a.t.a.l.i.a.84@mail.ru       | F     | NULL |
| Авлохова   | Алана       | 79992454413 | Владикавказ     | 18.10.1998  | 947913f982f230a3e45bee92378040955b135bdc | avlohova98@mail.ru             | F     | NULL |
| Сабанская  | Ольга       | 79940223573 | Лесозаводск     | 20.10.1969  | c60d2314d6659f758bdec5e3b19675362c61d316 | Sabanskay_10@mail.ru           | F     | NULL |
| Белякова   | Татьяна     | 79832744840 | Абакан          | 18.10.1998  | ca70f7619e386c603b841e16d4c52e566129729f | tatanabelakova8697@gmail.com   |       | NULL |
| Гатауллина | Резеда      | 79503134315 | Казань          | 06.06.1988  | 8bf3f42f74fe9a693a0803197c2375bf27477f26 | rezedushka2008@mail.ru         | F     | NULL |
| Сидоров    | Александр   | 79157530438 | Одинцово        | 30.08.1983  | d5403155c259adc446385b5854cca415bff75e02 | alekssidorov.83@list.ru        |       | NULL |
| Теткина    | Ольга       | 79628015828 | Абакан          | 21.06.1986  | 8e6c04790a939c45aa0296e71daf973e93b06d08 | Sagalakova.o.s@mail.ru         |       | NULL |
| Тупоногова | Олеся       | 79374738963 | Уфа             | 03.03.1998  | 227c4aa3fd6777e731a1213d8db22738508f53e2 | ilesya200794@gmail.com         | F     | NULL |
| Калова     | Алита       | 79964135902 | Москва          | 18.01.1999  | 245f71da69a2991b32e46e3eaf4e5649ba7c0d85 | kaldarashiraliev794@gmail.com  | F     | NULL |
| Брыксин    | Александр   | 79164032599 | Электросталь    | 09.02.1989  | cb5f2acffd397608357c2a79ba0aac927c47ac09 | Bryksinsan@mail.ru             |       | NULL |
| Нагаева    | Анастасия   | 79193220448 | Челябинск       | 24.06.1991  | 6974ddde2608a56dbe873506eea3864ca4000bfb | sorokina-nastya@inbox.ru       |       | NULL |
| Инапшба    | Бажена      | 79409342330 | Сухум           | 07.08.1995  | e6040ba290f5a9fd8fc052484bb15667c3d94c88 | Bazhena.inapshba.nanba@mail.ru |       | NULL |
| Султанов   | Азамат      | 79050055358 | Уфа             | 02.02.1989  | ec067978d62b7b25647a6e74e8313ad0d428bb82 | Zultan89@mail.ru               | M     | NULL |
| Проглядова | Наталья     | 79111600646 | Санкт-Петербург | 14.01.1988  | 56bdbc4a8b273bc465781d7f417b429bf6ee7624 | chentoriczkaya@mail.ru         | F     | NULL |
| Рустамова  | Елена       | 79806530911 | Рыково          | 02.05.1977  | 555943d3c21ed8c0d31e16af9b02c95e4cea421b | Aliena.77@mail.ru              |       | NULL |
| Ульянчева  | Наталья     | 79028580876 | Нижневартовск   | 17.10.1984  | a2a12bc3af6ef95a35659c86df9fd8b0eae5c711 | chikisheva86nata@mail.ru       |       | NULL |
| Кузикова   | Татьяна     | 79145986630 | Свободный       | 03.06.1991  | ccb73d3db4c22dcdcc263c9c4cf31222213c1bdb | kuzikova_t@bk.ru               |       | NULL |
| Усенбаева  | Айгуль      | 77018626080 | Атырау          | 20.02.1986  | 277f42208cd521b06f8c5acaa3acdf98cf64f5a5 | azinok@list.ru                 | F     | NULL |
| Лалетина   | Наталья     | 79635549420 | Киров           | 12.05.1980  | a17bc8f893cf6dc54a9205e448b4834c50c6d292 | Natali3015@mail.ru             | F     | NULL |
| Беда       | Денис       | 79385288200 | Тихорецк        | 16.10.1991  | 60bb0ed900ecaa1f94a46bde7abc88f8c2871a32 | bvb1997@bk.ru                  | M     | NULL |
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
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 94.22% |
| Phones | 63.13% |
| Address | 99.83% |
| Sex | 84.53% |
| Birth_date | 97.58% |



### Data sample
```
| names                  | emails                             | phones          | address             |   sex | birth_date   |
|:-----------------------|:-----------------------------------|:----------------|:--------------------|------:|:-------------|
| ['Кривцова Наталья']   | ['n.a.t.a.l.i.a.84@mail.ru']       | ['79092077066'] | ['Белгород']        |     0 | 07.09.1984   |
| ['Авлохова Алана']     | ['avlohova98@mail.ru']             | ['79992454413'] | ['Владикавказ']     |     0 | 18.10.1998   |
| ['Сабанская Ольга']    | ['sabanskay_10@mail.ru']           | ['79940223573'] | ['Лесозаводск']     |     0 | 20.10.1969   |
| ['Белякова Татьяна']   | ['tatanabelakova8697@gmail.com']   | ['79832744840'] | ['Абакан']          |   nan | 18.10.1998   |
| ['Гатауллина Резеда']  | ['rezedushka2008@mail.ru']         | ['79503134315'] | ['Казань']          |     0 | 06.06.1988   |
| ['Сидоров Александр']  | ['alekssidorov.83@list.ru']        | ['79157530438'] | ['Одинцово']        |   nan | 30.08.1983   |
| ['Теткина Ольга']      | ['sagalakova.o.s@mail.ru']         | ['79628015828'] | ['Абакан']          |   nan | 21.06.1986   |
| ['Тупоногова Олеся']   | ['ilesya200794@gmail.com']         | ['79374738963'] | ['Уфа']             |     0 | 03.03.1998   |
| ['Калова Алита']       | ['kaldarashiraliev794@gmail.com']  | ['79964135902'] | ['Москва']          |     0 | 18.01.1999   |
| ['Брыксин Александр']  | ['bryksinsan@mail.ru']             | ['79164032599'] | ['Электросталь']    |   nan | 09.02.1989   |
| ['Нагаева Анастасия']  | ['sorokina-nastya@inbox.ru']       | ['79193220448'] | ['Челябинск']       |   nan | 24.06.1991   |
| ['Инапшба Бажена']     | ['bazhena.inapshba.nanba@mail.ru'] | ['79409342330'] | ['Сухум']           |   nan | 07.08.1995   |
| ['Султанов Азамат']    | ['zultan89@mail.ru']               | ['79050055358'] | ['Уфа']             |     1 | 02.02.1989   |
| ['Проглядова Наталья'] | ['chentoriczkaya@mail.ru']         | ['79111600646'] | ['Санкт-Петербург'] |     0 | 14.01.1988   |
| ['Рустамова Елена']    | ['aliena.77@mail.ru']              | ['79806530911'] | ['Рыково']          |   nan | 02.05.1977   |
| ['Ульянчева Наталья']  | ['chikisheva86nata@mail.ru']       | ['79028580876'] | ['Нижневартовск']   |   nan | 17.10.1984   |
| ['Кузикова Татьяна']   | ['kuzikova_t@bk.ru']               | ['79145986630'] | ['Свободный']       |   nan | 03.06.1991   |
| ['Усенбаева Айгуль']   | ['azinok@list.ru']                 |                 | ['Атырау']          |     0 | 20.02.1986   |
| ['Лалетина Наталья']   | ['natali3015@mail.ru']             | ['79635549420'] | ['Киров']           |     0 | 12.05.1980   |
| ['Беда Денис']         | ['bvb1997@bk.ru']                  | ['79385288200'] | ['Тихорецк']        |     1 | 16.10.1991   |
```