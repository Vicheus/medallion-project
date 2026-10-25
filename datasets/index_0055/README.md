# Parsetron results

## About row data

> - Code name: index_0055
> - File path: Tinkoff Invest.txt
> - Total rows: 394819

### Schema
```
root
 |-- last_name: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- city: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- email: string (nullable = true)

```

### Data sample
```
| last_name   | first_name   | middle_name   | city             |       phone | email                      |
|:------------|:-------------|:--------------|:-----------------|------------:|:---------------------------|
| Желудкова   | Светлана     | Александровна | Челябинск        | 79043005898 | Vischenka74@mail.ru        |
| Букреева    | Ирина        | Сергеевна     | Анапа            | 79883476910 | bonifacio777@mail.ru       |
| Заболотная  | Людмила      | Геннадьевна   | Жуковский        | 79261541669 | boykova1601@mail.ru        |
| Шамбазова   | Дамис        | Мусаевна      | Набережные Челны | 79196445556 | aimash00@mail.ru           |
| Семёнов     | Павел        | Владимирович  | Санкт-Петербург  | 79995202695 | semenov1980navel@gmail.com |
| Закирова    | Ольга        | Вячеславовна  | Москва           | 79850092280 | jjvfyhb@mail.ru            |
| Семенова    | Влада        | Владимировна  | Санкт-Петербург  | 79883572496 | vladasemenova89@gmail.come |
| Балакина    | Светлана     | Рафаиловна    | Челябинск        | 79514653292 | stinnert@mail.ru           |
| Сидорова    | Мария        | Александровна | Барнаул          | 79095037776 | sokolovaeo@mail.ru         |
| Хасанова    | Наргиза      | Абдикаримовна | Иркутск          | 79501286362 | abdi.n.ha@ya.ru            |
```


## About final data
> - Total rows: 394350

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

```

### Data sample
```
| names                                | emails                         | phones          | address              |
|:-------------------------------------|:-------------------------------|:----------------|:---------------------|
| ['Желудкова Светлана Александровна'] | ['vischenka74@mail.ru']        | ['79043005898'] | ['Челябинск']        |
| ['Букреева Ирина Сергеевна']         | ['bonifacio777@mail.ru']       | ['79883476910'] | ['Анапа']            |
| ['Заболотная Людмила Геннадьевна']   | ['boykova1601@mail.ru']        | ['79261541669'] | ['Жуковский']        |
| ['Шамбазова Дамис Мусаевна']         | ['aimash00@mail.ru']           | ['79196445556'] | ['Набережные Челны'] |
| ['Семнов Павел Владимирович']        | ['semenov1980navel@gmail.com'] | ['79995202695'] | ['Санкт-Петербург']  |
| ['Закирова Ольга Вячеславовна']      | ['jjvfyhb@mail.ru']            | ['79850092280'] | ['Москва']           |
| ['Семенова Влада Владимировна']      | ['vladasemenova89@gmail.come'] | ['79883572496'] | ['Санкт-Петербург']  |
| ['Балакина Светлана Рафаиловна']     | ['stinnert@mail.ru']           | ['79514653292'] | ['Челябинск']        |
| ['Сидорова Мария Александровна']     | ['sokolovaeo@mail.ru']         | ['79095037776'] | ['Барнаул']          |
| ['Хасанова Наргиза Абдикаримовна']   | ['abdi.n.ha@ya.ru']            | ['79501286362'] | ['Иркутск']          |
```