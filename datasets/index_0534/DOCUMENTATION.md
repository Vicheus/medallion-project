# Parsetron results

## About row data

> - File path: info_hit_ru.csv
> - Total rows: 1473259

### Schema
```
root
 |-- last_name: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- email: string (nullable = true)
 |-- area: string (nullable = true)

```

### Data sample
```
| last_name   | first_name   |       phone | email                       | area               |
|:------------|:-------------|------------:|:----------------------------|:-------------------|
| Троицкая    | Алиса        | 79203401651 | alisontroitskaya91@inbox.ru | Финансы            |
| Дрыкина     | Ирина        | 79264648293 | finkon@inbox.ru             | Личностный рост    |
| Федьков     | Павел        | 79967916162 | fp1995@mail.ru              | Духовные практики  |
| Кошевая     | Светлана     | 79788497490 | svetko_64@mail.ru           | Женские курсы      |
| Абросимова  | Татьяна      | 79039763015 | oreshkova.70@mail.ru        | Мужские курсы      |
| Швецова     | Ирина        |             | iza.schev@yandex.ru         | Психология         |
| Рыжов       | Сергей       | 79257958550 | Pyps150@yandex.ru           | IT, разработка     |
| Татаринов   | Александр    | 79147865561 | glofiish77@mail.ru          | Аналитика          |
| Романова    | Татьяна      | 79033996584 | talero320@gmail.com         | Дизайн             |
| Зиатдинов   | Ренат        | 79274129889 | ziatdinchik@gmail.com       | Маркетинг          |
| Петакчян    | Наре         | 77965405955 | petakchian@gmail.com        | Бизнес-обучение    |
| Кулыгин     | Святослав    |             | ananda99921@mail.ru         | Управление         |
| Беляева     | Наталья      | 79291016115 | vendasever@gmail.com        | Карьера и работа   |
| Григорьева  | Татьяна      | 79689264117 | etatiyana@yandex.ru         | Здоровье           |
| Митюганова  | Нина         | 79787194905 | Mityuganova.nina@yandex.ru  | Спорт              |
| Другова     | Мария        | 79815051597 | maridry@mail.ru             | Иностранные языки  |
| Ибрагимова  | Севиндж      |             | 966ceymur@gmail.ru          | Творчество и хобби |
| Кулыгина    | Наталия      | 79117914627 | ananda99921@mail.ru         | Детям              |
| Бессонов    | Алексей      | 79272262831 | bessonov1987@inbox.ru       | Образование        |
| Серкина     | Светлана     | 79264162626 | s.serkina@gmail.com         | Искусство          |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.89% |
| Phones | 86.07% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                     | emails                      | phones   | raw_metadata                              |
|:--------------------------|:----------------------------|:---------|:------------------------------------------|
| ['Айнетдинова Маргарита'] | ['106@armed.ru']            |          | ['{"area": "Аналитика"}']                 |
| ['Сизов Максим']          | ['14029020@mail.ru']        |          | ['{"area": "Детям"}']                     |
| ['Тимканова Эльзира']     | ['2013.biblioteka@mail.ru'] |          | ['{"area": "Спорт"}']                     |
| ['Wang Bin']              | ['215640681@qq.com']        |          | ['{"area": "Аналитика"}']                 |
| ['Подольская Ирина']      | ['220975@bk.ru']            |          | ['{"area": "Творчество и хобби"}']        |
| ['Орехова Анна']          | ['262@rittal.ru']           |          | ['{"area": "IT разработка"}']             |
| ['Поздняков Александр']   | ['29-katya@mail.ru']        |          | ['{"area": "Аналитика"}']                 |
| ['Юй Бо']                 | ['297487777@qq.com']        |          | ['{"area": "Дизайн"}']                    |
| ['Сухоруков Артур']       | ['2callofduty5@mail.ru']    |          | ['{"area": "Спорт"}']                     |
| ['Акимов Валерий']        | ['4139691@mail.ru']         |          | ['{"area": "IT разработка"}']             |
| ['Жаворонков Александр']  | ['4852009@mail.ru']         |          | ['{"area": "Бизнес-обучение"}']           |
| ['Кулютина Юлия']         | ['4yulia@bk.ru']            |          | ['{"area": "Маркетинг"}']                 |
| ['Панасевич Анна']        | ['5554888@list.ru']         |          | ['{"area": "Управление"}']                |
| ['Василевич Александр']   | ['5854732@mail.ru']         |          | ['{"area": "Психология"}']                |
| ['Goguadze Irma']         | ['590asv668@rambler.ru']    |          | ['{"area": "Управление"}']                |
| ['Кальянов Сергей']       | ['5989202@mail.ru']         |          | ['{"area": "Дизайн"}']                    |
| ['Горская Стефания']      | ['61_08@bk.ru']             |          | ['{"area": "Психология"}']                |
| ['Митневский Евгений']    | ['6586696@gmail.com']       |          | ['{"area": "Здоровье"}']                  |
| ['Мужаидов Насурдин']     | ['6751878@gmail.com']       |          | ['{"area": "ФинансыТворчество и хобби"}'] |
| ['Яремко Арсений']        | ['73yarenko73@mail.ru']     |          | ['{"area": "Психология"}']                |
```