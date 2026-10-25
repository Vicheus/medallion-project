# Parsetron results

## About row data

> - Code name: index_0132
> - File path: /media/user/TRANSCEND/Databases/index_0132/raw/infourok.ru (2024).txt
> - Total rows: 1063537

### Schema
```
root
 |-- ID: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Страна: string (nullable = true)
 |-- Должность: string (nullable = true)
 |-- Место работы: string (nullable = true)
 |-- URL фото: string (nullable = true)

```

### Data sample
```
|   ID | ФИО                           | Дата рождения   | Страна   | Должность                              | Место работы                                                       | URL фото                                                            |
|-----:|:------------------------------|:----------------|:---------|:---------------------------------------|:-------------------------------------------------------------------|:--------------------------------------------------------------------|
|    1 | Иванов Сергей Иванович        | 14.12.1982      | Беларусь | Специалист                             | МБОУ СОШ № 28                                                      | https://img.infourok.ru/is03/img/04d5-00090584-b1f9fe82-250x350.jpg |
|    2 | Цуркан  Алла  Владимировна    | None            | Украина  | учитель русского языка и литературы    | None                                                               | https://cdn.infourok.ru/views/assets/img/noavatar.jpg               |
|    3 | Мусиенко Наталья Владимировна | 17.04.1971      | Россия   | учитель начальных классов              | МОБУ СОШ № 4 города Лабинска Лабинского района                     | https://cdn.infourok.ru/views/assets/img/noavatar.jpg               |
|    4 | Бережная Олеся Юрьевна        | 03.06.1982      | Россия   | Заместитель заведующего по УВР         | МБДОУ № 9 детский сад «Елочка»                                     | https://cdn.infourok.ru/views/assets/img/noavatar.jpg               |
|    5 | Станченко Елена Николаевна    | 24.04.1970      | Россия   | преподаватель                          | самозанятость                                                      | https://cdn.infourok.ru/views/assets/img/noavatar.jpg               |
|    6 | Шпирна Надежда Юрьевна        | 29.03.1963      | Россия   | учитель истории                        | МБОУ СОШ № 28                                                      | https://cdn.infourok.ru/views/assets/img/noavatar.jpg               |
|    7 | Сорокина Ольга Адольфовна     | 30.07.1960      | Россия   | учитель физики и математики            | "ГОКУ АО ""ОШ при УИН"" с. Среднебелая"                            | https://img.infourok.ru/is02/img/02e9-00011458-f0d5de7b-250x350.jpg |
|    8 | Микотина Тамара Сергеевна     | None            | None     | МБДОУ Детский сад № 5 город Уфа        | МБДОУ Детский сад № 5 город Уфа                                    | https://cdn.infourok.ru/views/assets/img/noavatar.jpg               |
|   11 | Соловьева Светлана Николаевна | 16.01.1965      | Россия   | учитель информатики и математики       | МАОУ СОШ № 3 имени Героя России Сергея Ромашина г. Южно-Сахалинска | https://cdn.infourok.ru/views/assets/img/noavatar.jpg               |
|   10 | Миндубаева Эльмира Саматовна  | 17.04.1976      | Россия   | учитель технологии и начальных классов | "МБОУ""Гимназия №14"""                                             | https://img.infourok.ru/is06/img/0781-000f22b0-523dd47f-250x350.jpg |
```


## About final data
> - Total rows: 845956

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```

### Data sample
```
| names                              | birth_date   | works                                                                                                                                                                                  |
|:-----------------------------------|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Мусиенко Наталья Владимировна']  | 17.01.1971   | [Row(post='учитель начальных классов', date_start=None, date_end=None, company='МОБУ СОШ 4 города Лабинска Лабинского района', address=None, comment=None)]                            |
| ['Бережная Олеся Юрьевна']         | 03.01.1982   | [Row(post='Заместитель заведующего по УВР', date_start=None, date_end=None, company='МБДОУ 9 детский сад Елочка', address=None, comment=None)]                                         |
| ['Станченко Елена Николаевна']     | 24.01.1970   | [Row(post='преподаватель', date_start=None, date_end=None, company='самозанятость', address=None, comment=None)]                                                                       |
| ['Шпирна Надежда Юрьевна']         | 29.01.1963   | [Row(post='учитель истории', date_start=None, date_end=None, company='МБОУ СОШ 28', address=None, comment=None)]                                                                       |
| ['Сорокина Ольга Адольфовна']      | 30.01.1960   | [Row(post='учитель физики и математики', date_start=None, date_end=None, company='ГОКУ АО ОШ при УИН с. Среднебелая', address=None, comment=None)]                                     |
| ['Соловьева Светлана Николаевна']  | 16.01.1965   | [Row(post='учитель информатики и математики', date_start=None, date_end=None, company='МАОУ СОШ 3 имени Героя России Сергея Ромашина г. Южно-Сахалинска', address=None, comment=None)] |
| ['Миндубаева Эльмира Саматовна']   | 17.01.1976   | [Row(post='учитель технологии и начальных классов', date_start=None, date_end=None, company='МБОУГимназия 14', address=None, comment=None)]                                            |
| ['Маслова Юлия Леонидовна']        |              | [Row(post='учитель биологии и технологии', date_start=None, date_end=None, company=None, address=None, comment=None)]                                                                  |
| ['Пирогова Наталья Васильевна']    | 24.01.1971   | [Row(post='Учитель', date_start=None, date_end=None, company='МБОУ ОСОШ 1 имени Героя РФ В. П. Брюхова', address=None, comment=None)]                                                  |
| ['Лебедева Наталья Александровна'] | 06.01.1975   | [Row(post='учитель математики и физики', date_start=None, date_end=None, company='МОУ Никольская СОШ', address=None, comment=None)]                                                    |
```