# Parsetron results

## About row data

> - File path: Сайт_Cool-Motors_13_09_2022.csv
> - Total rows: 469

### Schema
```
root
 |-- Почта: string (nullable = true)
 |-- Номер телефона: long (nullable = true)
 |-- ФИО: string (nullable = true)

```

### Data sample
```
| Почта                        |   Номер телефона | ФИО                            |
|:-----------------------------|-----------------:|:-------------------------------|
| omega@gk-omega.ru            |      7.92223e+10 | Грищенко Олег                  |
| durnev@mail.ru               |    nan           | Кео                            |
| oleggrolvi@gmail.com         |    nan           | Программист И Дизайнер         |
| info@cool-motors.ru          |    nan           | Главный Игорь Рудак            |
| demon1994_16@mail.ru         |      7.90446e+10 | Ребриков Евгений               |
| saltykovaa1953@yandex.ru     |      7.91229e+10 | Салтыков Алексей Александрович |
| hudin1204@gmail.com          |      7.92106e+10 | Худяков Роман                  |
| vape_1990@mail.ru            |      7.90309e+10 | Муравьев Данила                |
| coolsansmt@yandex.ru         |      7.91939e+10 | Хоренженко Александр           |
| vogulk86@yandex.ru           |      7.92225e+10 | Шапошников Андрей              |
| arteeva.n.m@mail.ru          |      7.96349e+10 | Артеева Наталья                |
| ekb3835045@ya.ru             |      7.9222e+11  | Маньков Антон                  |
| timofey.murm@mail.ru         |      7.91132e+10 | Подгол Тимофей                 |
| onegacrb.kotirovka@yandex.ru |      7.91159e+10 | Облап Галина                   |
| pavel.zhogov@mail.ru         |      7.93254e+10 | Жогов Павел                    |
| oxotnik-69@mail.ru           |      7.92479e+10 | Качан Сергей                   |
| sbemas1111@rambler.ru        |      7.9229e+10  | Михеев Андрей                  |
| d-m010197@rambler.ru         |      7.98181e+10 | Дегтярев Максим                |
| den-nuk@rambler.ru           |      7.96785e+10 | Сухогузов Денис                |
| vab_777@mail.ru              |      7.92222e+10 | Бочаров Василий                |
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
| Emails | 99.35% |
| Phones | 91.18% |



### Data sample
```
| names                              | emails                            | phones          |
|:-----------------------------------|:----------------------------------|:----------------|
| ['Бочаров Василий']                | ['vab_777@mail.ru']               | ['79222162269'] |
| ['Козлов Николай']                 | ['prom-57@mail.ru']               | ['79292185920'] |
| ['Димитриев Игорь']                | ['l.s.d69@mail.ru']               | ['79533292333'] |
| ['Аникин Максим']                  | ['tanapopovskih69@gmail.com']     | ['79538257943'] |
| ['Беляков Антон']                  | ['antoha.nt@mail.ru']             | ['79506418676'] |
| ['Лихачев Николай']                | ['kolyasik41@gmail.com']          | ['79022630324'] |
| ['Дебелов Дмитрий']                | ['giniral39@gmail.com']           | ['79126501035'] |
| ['Ступин Виктор']                  |                                   | ['79619649221'] |
| ['Салтыков Алексей Александрович'] | ['saltykovaa1953@yandex.ru']      | ['79122869376'] |
| ['Кононов Алексей']                | ['kononov-8@rambler.ru']          | ['79221382398'] |
| ['Кармановскиц Сергей']            | ['oil51@mail.ru']                 | ['79209968799'] |
| ['Платонов Никита']                | ['ebobostunts@yandex.ru']         | ['79969467211'] |
| ['Парашин Павел']                  | ['racer_ppe@mail.ru']             | ['79823671986'] |
| ['Пономаренко Алексей']            | ['alex-pon1@yandex.ru']           | ['79270786404'] |
| ['Усманов Дэнис']                  | ['matizko@mail.ru']               | ['79045426869'] |
| ['Астафьев Александр']             | ['aleksandr.astafev13@gmail.com'] | ['79222022492'] |
| ['Нагорнова Наталья']              | ['natalanagornova495@gmail.com']  | ['79638528374'] |
| ['Устинов Константин']             | ['ukl@bk.ru']                     | ['79126146981'] |
| ['Емельянов Антон']                | ['aemov31@gmail.com']             | ['79676308376'] |
| ['Живанов Григорий']               | ['zhivgriga@yandex.ru']           | ['79028728006'] |
```