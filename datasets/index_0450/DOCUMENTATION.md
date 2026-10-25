# Parsetron results

## About row data

> - File path: Магазин_канцелярии_Феникс+_2023.csv
> - Total rows: 2308

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Номер телефона: long (nullable = true)

```

### Data sample
```
| ФИО                         | Почта                       |   Номер телефона |
|:----------------------------|:----------------------------|-----------------:|
| Ирина                       | iefremidis@yandex.ru        |              nan |
| Феникс Админ                | fpl-it@fenixrostov.ru       |              nan |
| Анна                        | diza22@mail.ru              |              nan |
| Юлия Крохалева              | koral26@yandex.ru           |              nan |
| Татьяна                     | antiza@yandex.ru            |              nan |
| Вилли Маяковского 12 стр 2  | Kanzpark@list.ru            |              nan |
| Богатырева Марина           | DaDetyam@yandex.ru          |              nan |
| Вилли Фараджов              | farajov1976@mail.ru         |              nan |
| ИП Анохина Ирина Николаевна | Kez-stilus@yandex.ru        |              nan |
| Елена                       | rominalenulya@yandex.ru     |              nan |
| валентин                    | smile.fcompany@gmail.com    |              nan |
| Левкова Ирина Николаевна    | sochilevkova@mail.ru        |              nan |
| Ирина                       | vm-presstorg@yandex.ru      |              nan |
| Янна                        | OOO_eurostyle@list.ru       |              nan |
| Бойченко                    | a.boychenko@phoenix-plus.ru |              nan |
| Вера                        | goodprice-buy@yandex.ru     |              nan |
| Надежда                     | office@lazur29.ru           |              nan |
| Матейко Татьяна             | Mrs.stationery@mail.ru      |              nan |
| Абузарова Гузель Раисовна   | zakup4@kancler02.ru         |              nan |
| Манько Анна                 | pol3d@yandex.ru             |              nan |
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
| Emails | 99.82% |
| Phones | 22.05% |



### Data sample
```
| names                              | emails                          | phones          |
|:-----------------------------------|:--------------------------------|:----------------|
| ['Казарцева Оксана Анатольевна']   | ['opts@papirus51.ru']           | ['78152422675'] |
| ['Вариханова Елена Александровна'] | ['alenaalexv@gmail.com']        | ['79188224283'] |
| ['Татьяна Викторовна']             | ['mag@avtograf32.ru']           |                 |
| ['Горбанева Татьяна Владимировна'] | ['tatiana_73@list.ru']          |                 |
| ['Батяева Елена Викторовна']       | ['batiaeva.elena@yandex.ru']    |                 |
| ['Дмиттрий']                       | ['dbiz@mail.ru']                |                 |
| ['Кира']                           | ['777kira@bk.ru']               |                 |
| ['Галина']                         | ['212@fox56.ru']                |                 |
| ['Хакан']                          | ['khaqanomar@mail.ru']          |                 |
| ['Гладкова Маргарита']             | ['3011@mail.ru']                | ['79185265076'] |
| ['Зонов Сергей Андреевич']         | ['zonovsergey@gmail.com']       | ['79053365774'] |
| ['Алена']                          | ['skrepkairina@mail.ru']        | ['74114762722'] |
| ['Тупов Василий Викторович']       | ['sveta_moskalenko_25@mail.ru'] | ['79787125126'] |
| ['Синкевич Мария Витальевна']      | ['mariya-24.04@mail.ru']        | ['79186562534'] |
| ['Татьяна']                        | ['antiza@yandex.ru']            |                 |
| ['Валерий']                        | ['ipzatsepin@mail.ru']          |                 |
| ['Татьяна Колесникова']            | ['tanysha2012@mail.ru']         |                 |
| ['Юлия']                           | ['sergey_uli@list.ru']          |                 |
| ['Сергей']                         | ['pegovs@mail.ru']              |                 |
| ['Ольга']                          | ['akishevaolga@yandex.ru']      |                 |
```