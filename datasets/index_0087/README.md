# Parsetron results

## About row data

> - Code name: index_0087
> - File path: volgofarm_users_preprocessed.csv
> - Total rows: 10

### Schema
```
root
 |-- id_user: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)
 |-- work_place: string (nullable = true)

```

### Data sample
```
|   id_user | name                             | email                      | phone   | login         | password       | work_place   |
|----------:|:---------------------------------|:---------------------------|:--------|:--------------|:---------------|:-------------|
|       431 | Зенина Наталия Владимировна      | zenina0859@mail.ru         |         | zenina0859    | mark2510       |              |
|       339 | Лобасова Светлана Никаноровна    | apteka44@volgofarm.ru      |         | lobasovasn    | apteka44       |              |
|       254 | Третьякова Марина Александровна  | apteka34@volgofarm.ru      |         | apt34         | apt34vf        |              |
|       276 | Олейникова Виктория Владимировна | 20-fanta-80@mail.ru        |         | fanta         | fanta-20       |              |
|       473 | Хомкина Вера Георгиевна          | apteka102@volgofarm.ru     |         | volgofarm2018 | volgofarm2018  |              |
|       127 | Баженова Екатерина Михайловна    | anirekat@mail.ru           |         | anirekat      | katerina623725 |              |
|       424 | Хараман Кристина Сергеевна       | haraman@narod.ru           |         | apteka694     | 692018         |              |
|       429 | Понамарчук Марина Антоновна      | ponamarchuk-m@mail.ru      |         | apteka695     | 692018         |              |
|        95 | Федорова Марина Валерьевна       | fedorovamari2011@yandex.ru |         | agf625        | agf625         |              |
|       170 | Ярцева Марина Владимировна       | apteka42@volgofarm.ru      |         | marina18      | 950188         |              |
```

> - Code name: index_0087
> - File path: Заказы.csv
> - Total rows: 218629

### Schema
```
root
 |-- id: string (nullable = true)
 |-- id_user: double (nullable = true)
 |-- id_order: integer (nullable = true)
 |-- time: integer (nullable = true)
 |-- date: string (nullable = true)
 |-- apteka: string (nullable = true)
 |-- name_user: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- comment: string (nullable = true)
 |-- summa: double (nullable = true)
 |-- status: integer (nullable = true)
 |-- type_order: integer (nullable = true)
 |-- regids1: string (nullable = true)
 |-- kols1: string (nullable = true)
 |-- sum1: string (nullable = true)
 |-- regids2: string (nullable = true)
 |-- kols2: string (nullable = true)
 |-- sum2: string (nullable = true)
 |-- dostavka: integer (nullable = true)
 |-- oplata: integer (nullable = true)

```

### Data sample
```
|    id |   id_user |   id_order |       time | date       |   apteka | name_user                   | email                 | phone              | comment   |   summa |   status |   type_order | regids1                     | kols1                    | sum1    | regids2       | kols2     | sum2   |   dostavka |   oplata |
|------:|----------:|-----------:|-----------:|:-----------|---------:|:----------------------------|:----------------------|:-------------------|:----------|--------:|---------:|-------------:|:----------------------------|:-------------------------|:--------|:--------------|:----------|:-------|-----------:|---------:|
| 72202 |         0 |     203329 | 1574230052 | 20.11.2019 |       51 | Иванова Римма Александровна | rim-max@yandex.ru     | +7 (905) 339-20-58 |           |       0 |        0 |            0 | 702844                      | 5700.6                   | 1       |               |           |        |          0 |        0 |
| 72203 |         0 |     203330 | 1574230094 | 20.11.2019 |       42 | Светлана                    |                       | +7 (904) 401-28-90 |           |       0 |        0 |            0 | 731386                      | 690.3                    | 1       |               |           |        |          0 |        0 |
| 72204 |         0 |     203331 | 1574230103 | 20.11.2019 |       51 | Аноним                      |                       | +7 (905) 334-24-77 |           |       0 |        0 |            0 | 332843                      | 27.9                     | 1       |               |           |        |          0 |        0 |
| 72205 |         0 |     203333 | 1574230291 | 20.11.2019 |       51 | Юлия                        | yulya.sid@mail.ru     | +7 (961) 073-70-70 |           |       0 |        0 |            0 | 18072                       | 383.4                    | 1       |               |           |        |          0 |        0 |
| 72206 |         0 |     203335 | 1574230363 | 20.11.2019 |       32 | Анна                        |                       | +7 (909) 390-54-90 |           |       0 |        0 |            0 | 115226                      | 316.8                    | 1       |               |           |        |          0 |        0 |
| 72207 |         0 |     203336 | 1574230436 | 20.11.2019 |       42 | Светлана                    |                       | +7 (904) 401-28-90 |           |       0 |        0 |            0 | 8434                        | 164.7                    | 1       |               |           |        |          0 |        0 |
| 72208 |         0 |     203337 | 1574230440 | 20.11.2019 |       34 | Екатерина                   |                       | +7 (937) 711-82-91 |           |       0 |        0 |            0 | 485076                      | 206.1                    | 1       |               |           |        |          0 |        0 |
| 72209 |         0 |     203340 | 1574230581 | 20.11.2019 |      120 | Дудина                      |                       | +7 (960) 896-31-05 |           |       0 |        0 |            0 | 122987                      | 139.5                    | 1       |               |           |        |          0 |        0 |
| 72212 |         0 |     203342 | 1574230613 | 20.11.2019 |      137 | Татьяна                     | tany_22_81@mail.ru    | +7 (929) 787-91-57 |           |       0 |        0 |            0 | 159477                      | 421.2                    | 1       |               |           |        |          0 |        0 |
| 72213 |         0 |     203343 | 1574230618 | 20.11.2019 |       32 | сергей                      | mitrich2704@gmail.com | +7 (902) 311-16-93 |           |       0 |        0 |            0 | 366510                      | 774                      | 1       |               |           |        |          0 |        0 |
| 72214 |         0 |     203344 | 1574230667 | 20.11.2019 |       80 | Юрий Александрович Пыльнев  | u.pilnev@fsga.ru      | +7 (927) 500-34-08 |           |       0 |        0 |            0 | 427566                      | 534.6                    | 1       |               |           |        |          0 |        0 |
| 72215 |         0 |     203346 | 1574230776 | 20.11.2019 |      120 | Дудина                      |                       | +7 (960) 896-31-05 |           |       0 |        0 |            0 | 395                         | 578.7                    | 1       |               |           |        |          0 |        0 |
| 72216 |         0 |     203347 | 1574230790 | 20.11.2019 |      121 | Екатерина                   |                       | +7 (937) 711-82-91 |           |       0 |        0 |            0 | 21399                       | 500.4                    | 1       |               |           |        |          0 |        0 |
| 72217 |         0 |     203348 | 1574230815 | 20.11.2019 |      124 | Александр                   | alekslopat2@gmail.com | +7 (902) 389-04-83 |           |       0 |        0 |            0 | 483849                      | 1197                     | 1       |               |           |        |          0 |        0 |
| 72218 |         0 |     203349 | 1574230906 | 20.11.2019 |      235 |                             |                       | +7 (969) 658-19-26 |           |       0 |        0 |            0 | 237703,427023,427279,648352 | 2063.7,573.3,751.5,231.3 | 1,1,1,1 |               |           |        |          0 |        0 |
| 72219 |         0 |     203350 | 1574230976 | 20.11.2019 |       78 | Михаил                      | nikulin-56@list.ru    | +7 (903) 316-85-75 |           |       0 |        0 |            0 | 1806                        | 282.6                    | 1       |               |           |        |          0 |        0 |
| 72220 |         0 |     203353 | 1574231167 | 20.11.2019 |       68 | Анна                        | an8500@yandex.ru      | +7 (917) 837-85-00 |           |       0 |        0 |            0 | 2226,2226,4914              | 2.97,2.97,27             | 3,22,1  |               |           |        |          0 |        0 |
| 72221 |         0 |     203354 | 1574231239 | 20.11.2019 |       97 | Анна                        | nutikl@mail.ru        | +7 (905) 396-84-25 |           |       0 |        0 |            0 | 226886                      | 0.9                      | 1       |               |           |        |          0 |        0 |
| 72222 |         0 |     203354 | 1574231241 | 20.11.2019 |       97 | Анна                        | nutikl@mail.ru        | +7 (905) 396-84-25 |           |       0 |        0 |            0 |                             |                          |         | 376686,673160 | 621,593.1 | 1,1    |          0 |        0 |
| 72225 |         0 |     203359 | 1574231371 | 20.11.2019 |        3 | Виктория Полякова           | naitusa@yandex.ru     | +7 (960) 886-47-76 |           |       0 |        0 |            0 | 173304                      | 6016.5                   | 1       |               |           |        |          0 |        0 |
```


## About final data
> - Total rows: 204112

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- id: string (nullable = true)
 |    |    |-- password: string (nullable = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- actuality: string (nullable = true)
 |-- raw_metadata: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 73.45% |
| Phones | 99.97% |
| Accounts | 0.00% |
| Works | 0.00% |
| Actuality | 100.00% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                                | emails                         | phones          | accounts                                                                                                                | works   | actuality   | raw_metadata                      |
|:-------------------------------------|:-------------------------------|:----------------|:------------------------------------------------------------------------------------------------------------------------|:--------|:------------|:----------------------------------|
| ['Зенина Наталия Владимировна']      | ['zenina0859@mail.ru']         |                 | [Row(title='Аптека Волгофарм', link='https://volgofarm.ru', login='zenina0859', id='431', password='mark2510')]         |         |             |                                   |
| ['Лобасова Светлана Никаноровна']    | ['apteka44@volgofarm.ru']      |                 | [Row(title='Аптека Волгофарм', link='https://volgofarm.ru', login='lobasovasn', id='339', password='apteka44')]         |         |             |                                   |
| ['Третьякова Марина Александровна']  | ['apteka34@volgofarm.ru']      |                 | [Row(title='Аптека Волгофарм', link='https://volgofarm.ru', login='apt34', id='254', password='apt34vf')]               |         |             |                                   |
| ['Олейникова Виктория Владимировна'] | ['20-fanta-80@mail.ru']        |                 | [Row(title='Аптека Волгофарм', link='https://volgofarm.ru', login='fanta', id='276', password='fanta-20')]              |         |             |                                   |
| ['Хомкина Вера Георгиевна']          | ['apteka102@volgofarm.ru']     |                 | [Row(title='Аптека Волгофарм', link='https://volgofarm.ru', login='volgofarm2018', id='473', password='volgofarm2018')] |         |             |                                   |
| ['Баженова Екатерина Михайловна']    | ['anirekat@mail.ru']           |                 | [Row(title='Аптека Волгофарм', link='https://volgofarm.ru', login='anirekat', id='127', password='katerina623725')]     |         |             |                                   |
| ['Хараман Кристина Сергеевна']       | ['haraman@narod.ru']           |                 | [Row(title='Аптека Волгофарм', link='https://volgofarm.ru', login='apteka694', id='424', password='692018')]            |         |             |                                   |
| ['Понамарчук Марина Антоновна']      | ['ponamarchuk-m@mail.ru']      |                 | [Row(title='Аптека Волгофарм', link='https://volgofarm.ru', login='apteka695', id='429', password='692018')]            |         |             |                                   |
| ['Федорова Марина Валерьевна']       | ['fedorovamari2011@yandex.ru'] |                 | [Row(title='Аптека Волгофарм', link='https://volgofarm.ru', login='agf625', id='95', password='agf625')]                |         |             |                                   |
| ['Ярцева Марина Владимировна']       | ['apteka42@volgofarm.ru']      |                 | [Row(title='Аптека Волгофарм', link='https://volgofarm.ru', login='marina18', id='170', password='950188')]             |         |             |                                   |
| ['Иванова Римма Александровна']      | ['rim-max@yandex.ru']          | ['79053392058'] |                                                                                                                         |         | 20.11.2019  | {"apteka": "51", "summa": "0.0"}  |
| ['Светлана']                         |                                | ['79044012890'] |                                                                                                                         |         | 20.11.2019  | {"apteka": "42", "summa": "0.0"}  |
| ['Аноним']                           |                                | ['79053342477'] |                                                                                                                         |         | 20.11.2019  | {"apteka": "51", "summa": "0.0"}  |
| ['Юлия']                             | ['yulya.sid@mail.ru']          | ['79610737070'] |                                                                                                                         |         | 20.11.2019  | {"apteka": "51", "summa": "0.0"}  |
| ['Светлана']                         |                                | ['79044012890'] |                                                                                                                         |         | 20.11.2019  | {"apteka": "42", "summa": "0.0"}  |
| ['Екатерина']                        |                                | ['79377118291'] |                                                                                                                         |         | 20.11.2019  | {"apteka": "34", "summa": "0.0"}  |
| ['Дудина']                           |                                | ['79608963105'] |                                                                                                                         |         | 20.11.2019  | {"apteka": "120", "summa": "0.0"} |
| ['Татьяна']                          | ['tany_22_81@mail.ru']         | ['79297879157'] |                                                                                                                         |         | 20.11.2019  | {"apteka": "137", "summa": "0.0"} |
| ['Сергей']                           | ['mitrich2704@gmail.com']      | ['79023111693'] |                                                                                                                         |         | 20.11.2019  | {"apteka": "32", "summa": "0.0"}  |
| ['Юрий Александрович Пыльнев']       | ['u.pilnev@fsga.ru']           | ['79275003408'] |                                                                                                                         |         | 20.11.2019  | {"apteka": "80", "summa": "0.0"}  |
```