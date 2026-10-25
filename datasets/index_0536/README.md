# Parsetron results

## About row data

> - Code name: index_0536
> - File path: *.csv
> - Total rows: 42782

### Schema
```
root
 |-- _c0: string (nullable = true)
 |-- _c1: string (nullable = true)
 |-- _c2: string (nullable = true)
 |-- _c3: string (nullable = true)
 |-- _c4: string (nullable = true)
 |-- _c5: string (nullable = true)
 |-- _c6: string (nullable = true)
 |-- _c7: string (nullable = true)
 |-- _c8: string (nullable = true)
 |-- _c9: string (nullable = true)
 |-- _c10: string (nullable = true)
 |-- _c11: string (nullable = true)

```

### Data sample
```
|   _c0 | _c1        | _c2   | _c3    | _c4                 | _c5                               |          _c6 | _c7                   | _c8       | _c9   | _c10   | _c11   |
|------:|:-----------|:------|:-------|:--------------------|:----------------------------------|-------------:|:----------------------|:----------|:------|:-------|:-------|
|     1 | 03.01.2025 | 8:00  | Линия2 | Техосмотр по записи | Сокольников Георгий Евгеньевич    | 375291849857 | Форд Виндстар         | 3766ОН7   |       |        |        |
|     2 | 03.01.2025 | 8:20  | Линия2 | Техосмотр по записи | счасный виктор станиславович      | 375295075615 | ниссан                |           |       |        |        |
|     3 | 03.01.2025 | 8:40  | Линия2 | Техосмотр по записи | Душеин Сергей Сергеевич           | 375293772188 | Крайслер таункантри   | 7240 io-7 |       |        |        |
|     4 | 03.01.2025 | 9:00  | Линия2 | Техосмотр по записи | Пискунович Сергей Карпович        | 375296312788 | Тойота Аурис          | 3333 КР-7 |       |        |        |
|     5 | 03.01.2025 | 10:00 | Линия2 | Техосмотр по записи | Дмитревич Алла Семёновна          | 375291808464 | Mercedes-Benz E300    | 0564XA-7  |       |        |        |
|     6 | 03.01.2025 | 10:40 | Линия2 | Техосмотр по записи | Козлов Александр Анатольевич      | 375445538988 | Фольксваген Поло      | 7643ТК-7  |       |        |        |
|     7 | 03.01.2025 | 11:20 | Линия2 | Техосмотр по записи | Клещенко Виктор Константинович    | 375297662783 | Mazda cx-9            | 4643 СМ-7 |       |        |        |
|     8 | 03.01.2025 | 13:00 | Линия2 | Техосмотр по записи | Каралькевич Людмила Львовна       | 375296314534 | Ниссан                | 7289НС7   |       |        |        |
|     9 | 03.01.2025 | 13:20 | Линия2 | Техосмотр по записи | Кривенков Владимир Борисович      | 375292696557 | Лада  веста св кросс  | 7062 СМ7  |       |        |        |
|    10 | 03.01.2025 | 13:40 | Линия2 | Техосмотр по записи | Мельник Владимир Сергеевич        | 375447242354 | Пежо 308              | 7178 РР-7 |       |        |        |
|    11 | 03.01.2025 | 14:00 | Линия2 | Техосмотр по записи | Шиш Виталий Владимирович          | 375293885412 | БМВ 118               | 1836 тт 7 |       |        |        |
|    12 | 03.01.2025 | 14:20 | Линия2 | Техосмотр по записи | Коровкин Кирилл Александрович     | 375298498299 | FAW BESTUNE T77       | 1201 KE-6 |       |        |        |
|    13 | 03.01.2025 | 14:40 | Линия2 | Техосмотр по записи | Абакумов Илья Сергеевич           | 375296617100 | Volkswagen polo       | 0752XT-7  |       |        |        |
|    14 | 03.01.2025 | 15:00 | Линия2 | Техосмотр по записи | Богданов Александр Сергеевич      | 375333558259 | Honda Civic 8 5d 2009 | 8395 HM-1 |       |        |        |
|    15 | 03.01.2025 | 15:20 | Линия2 | Техосмотр по записи | Антипенко Александр               | 375447705147 | Тойота Авенсис        | 0514 EX-2 |       |        |        |
|    16 | 03.01.2025 | 16:00 | Линия2 | Техосмотр по записи | Грузинская Елена Федоровна        | 375297086881 | BMW118i               | 9306MT-1  |       |        |        |
|    17 | 03.01.2025 | 17:30 | Линия2 | Техосмотр по записи | Дедовец А П                       | 375295732684 | ТИГО                  | 7676 TI-7 |       |        |        |
|    18 | 03.01.2025 | 17:50 | Линия2 | Техосмотр по записи | Филиппова Екатерина Александровна | 375299430797 | Хендай аксент         | 3424      |       |        |        |
|    19 | 03.01.2025 | 18:10 | Линия2 | Техосмотр по записи | Бабчик Дмитрий Владимирович       | 375291335588 | Мерседес              | 0785ТМ7   |       |        |        |
|    20 | 03.01.2025 | 18:30 | Линия2 | Техосмотр по записи | Ковалёв Виталий Алекспндрович     | 375292490523 | Chevrolet Cruze       | 1806 EX-2 |       |        |        |
```


## About final data
> - Total rows: 19655

### Schema
```
root
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- vehicles: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = false)
 |    |    |-- model: string (nullable = true)
 |    |    |-- year: integer (nullable = true)
 |    |    |-- color: string (nullable = true)
 |    |    |-- number: string (nullable = true)
 |    |    |-- vin: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Phones | 100.00% |
| Names | 100.00% |
| Vehicles | 71.95% |
| Actuality | 100.00% |



### Data sample
```
| phones           | names                                                                    | vehicles                                                                                                                                                                                                     | actuality   |
|:-----------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['375255464303'] | ['Дапкюнас Андрей Вадимович']                                            | [Row(type=1, model=None, year=None, color=None, number='2139 КТ-7', vin=None, comment=None)]                                                                                                                 | 20.07.2024  |
| ['375291244084'] | ['Чистая Оксана Вячеславовна']                                           | [Row(type=1, model='БМВ 320i', year=None, color=None, number='8366PH7', vin=None, comment=None)]                                                                                                             | 04.11.2025  |
| ['375291596925'] | ['Бабицкая А.А.']                                                        | [Row(type=1, model='Хенде Акцент', year=None, color=None, number='8588 тв-7', vin=None, comment=None), Row(type=1, model='Хендэ Акцент', year=None, color=None, number='8588ТВ7', vin=None, comment=None)]   | 22.07.2024  |
| ['375291721367'] | ['Левшунов Виталий Семенович', 'Левшунов В.С.']                          | [Row(type=1, model='HAMMER H3', year=None, color=None, number='1836 MO-7', vin=None, comment=None)]                                                                                                          | 20.08.2025  |
| ['375291733930'] | ['Кучук Евгений Дмитриевич']                                             |                                                                                                                                                                                                              | 03.05.2025  |
| ['375291798220'] | ['Живицкая Елена Александровна']                                         | [Row(type=1, model='Volkswagen polo', year=None, color=None, number='7579 ТВ-7', vin=None, comment=None)]                                                                                                    | 28.05.2023  |
| ['375291843129'] | ['Мельник']                                                              |                                                                                                                                                                                                              | 22.01.2024  |
| ['375291866257'] | ['Василевич Анна Леонидовна', 'Василевич Николай Владимирович']          | [Row(type=1, model=None, year=None, color=None, number='2383 HX-7', vin=None, comment=None), Row(type=1, model=None, year=None, color=None, number='2383 НХ-7', vin=None, comment=None)]                     | 28.04.2025  |
| ['375292007953'] | ['Романова Екатерина Владимировна']                                      | [Row(type=1, model='Audi q5', year=None, color=None, number='6977MT1', vin=None, comment=None)]                                                                                                              | 04.03.2025  |
| ['375292713827'] | ['Скрипко Анна Николаевна']                                              |                                                                                                                                                                                                              | 16.05.2025  |
| ['375293211160'] | ['Гордеев Денис Владимирович']                                           | [Row(type=1, model='Мерседес Бенц GLA', year=None, color=None, number='44-28 НК-5', vin=None, comment=None)]                                                                                                 | 23.03.2024  |
| ['375293241679'] | ['Воронцова Анастасия Дмитриевна']                                       | [Row(type=1, model='Мазда 3', year=None, color=None, number='9235 МН-7', vin=None, comment=None)]                                                                                                            | 06.09.2023  |
| ['375293370469'] | ['Холодинский', 'Корай Элгюн', 'Будикова']                               |                                                                                                                                                                                                              | 28.01.2022  |
| ['375293421669'] | ['Демидюк Дмитрий Николаевич']                                           | [Row(type=1, model='Ауди А4', year=None, color=None, number='8699 НН-7', vin=None, comment=None)]                                                                                                            | 27.04.2025  |
| ['375293502511'] | ['Бутько Стефания Юрьевна']                                              | [Row(type=1, model='Ниссан Тида', year=None, color=None, number='5200РК7', vin=None, comment=None)]                                                                                                          | 20.09.2024  |
| ['375295501672'] | ['Косиков Сергей Вадимович']                                             | [Row(type=1, model='Minsk r250', year=None, color=None, number='2524 AI-5', vin=None, comment=None), Row(type=1, model='Mинск R250', year=None, color=None, number='2524 МН-7', vin=None, comment=None)]     | 29.08.2023  |
| ['375295695349'] | ['Кузьменков Евгений Александрович', 'Кузьменков Евгениф Александрович'] | [Row(type=1, model='Kawasaki zr7', year=None, color=None, number='8843 AA-7', vin=None, comment=None), Row(type=1, model='Kawasaki zr7', year=None, color=None, number='8847 АА-7', vin=None, comment=None)] | 21.05.2025  |
| ['375295918040'] | ['Кудинова Мария Андреевна']                                             | [Row(type=1, model='Mercedes GLC', year=None, color=None, number='7779 CC-7', vin=None, comment=None)]                                                                                                       | 22.07.2023  |
| ['375296249552'] | ['Теслюк Дмитрий Иванович']                                              | [Row(type=1, model=None, year=None, color=None, number='1309HK-7', vin=None, comment=None)]                                                                                                                  | 11.06.2025  |
| ['375296257059'] | ['Давыдов Дмитрий Евгеньевич']                                           | [Row(type=1, model='Hyundai Solaris', year=None, color=None, number='6208 ХК-7', vin=None, comment=None)]                                                                                                    | 17.03.2025  |
```