# Parsetron results

## About row data

> - Code name: index_0519
> - File path: jivo.ru (2022).txt
> - Total rows: 154115

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- Почта: string (nullable = true)

```

### Data sample
```
| ФИО                            |   Номер телефона | Почта                       |
|:-------------------------------|-----------------:|:----------------------------|
| Владислав                      |      79038408681 | zubr-tula@bk.ru             |
| Владимир                       |      79630924299 | BRIGADIR.811@GMAIL.COM      |
| виталий                        |      79205758912 | shevchenko_8383@list.ru     |
| евгений                        |      79205070637 | evgesafro@mail.ru           |
| Арсений                        |      79199611692 | 5077390@mail.ru             |
| Марина                         |      79518603249 | mari70007@mail.ru           |
| Алексей                        |      79819769891 | 2605302@mail.ru             |
| Магомед                        |      79112440542 | mzmz62@mail.ru              |
| Александр                      |      79878229675 | Aleksandr.lomov64@yandex.ru |
| Александр Павлович             |      79507726485 | Aleks.startcev@yandex.ru    |
| Travis Melton                  |      79014275462 | travis.melton1@gmail.com    |
| Ryan                           |       6026634432 | rykenn19@yahoo.com          |
| Надежда Анатольевна Шельпякова |      79519955716 | schelpnadin@mail.ru         |
| Рифат                          |      77779010303 | dostik0774@mail.ru          |
| Sheldon                        |       7806030060 | schartrand@ymail.com        |
| Игорь Каширин                  |      79515406167 | Kashirin02.06.75@mail.ru    |
| Ирина                          |      79102825641 | ireniym1985@mail.ru         |
| Любовь                         |      79650245258 | ml@tdrusichi.ru             |
| Марина                         |      79531468877 | mar570@yandex.ru            |
| Биксалиев Асхать Нурислямович  |      79176986001 | sale1@scomposites.ru        |
```


## About final data
> - Total rows: 136819

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)

```



### Data sample
```
| names                              | phones          | emails                          |
|:-----------------------------------|:----------------|:--------------------------------|
| ['Владислав']                      | ['79038408681'] | ['zubr-tula@bk.ru']             |
| ['Владимир']                       | ['79630924299'] | ['brigadir.811@gmail.com']      |
| ['Виталий']                        | ['79205758912'] | ['shevchenko_8383@list.ru']     |
| ['Евгений']                        | ['79205070637'] | ['evgesafro@mail.ru']           |
| ['Арсений']                        | ['79199611692'] | ['5077390@mail.ru']             |
| ['Марина']                         | ['79518603249'] | ['mari70007@mail.ru']           |
| ['Алексей']                        | ['79819769891'] | ['2605302@mail.ru']             |
| ['Магомед']                        | ['79112440542'] | ['mzmz62@mail.ru']              |
| ['Александр']                      | ['79878229675'] | ['aleksandr.lomov64@yandex.ru'] |
| ['Александр Павлович']             | ['79507726485'] | ['aleks.startcev@yandex.ru']    |
| ['Travis Melton']                  | ['79014275462'] | ['travis.melton1@gmail.com']    |
| ['Ryan']                           |                 | ['rykenn19@yahoo.com']          |
| ['Надежда Анатольевна Шельпякова'] | ['79519955716'] | ['schelpnadin@mail.ru']         |
| ['Рифат']                          |                 | ['dostik0774@mail.ru']          |
| ['Sheldon']                        |                 | ['schartrand@ymail.com']        |
| ['Игорь Каширин']                  | ['79515406167'] | ['kashirin02.06.75@mail.ru']    |
| ['Ирина']                          | ['79102825641'] | ['ireniym1985@mail.ru']         |
| ['Любовь']                         | ['79650245258'] | ['ml@tdrusichi.ru']             |
| ['Марина']                         | ['79531468877'] | ['mar570@yandex.ru']            |
| ['Биксалиев Асхать Нурислямович']  | ['79176986001'] | ['sale1@scomposites.ru']        |
```