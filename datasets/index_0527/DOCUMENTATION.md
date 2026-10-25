# Parsetron results

## About row data

> - File path: RUSTIRKA CLEAN.txt
> - Total rows: 25726

### Schema
```
root
 |-- Телефон: string (nullable = true)
 |-- Адрес: string (nullable = true)
 |-- Тип оплат: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Сумма1: integer (nullable = true)
 |-- Сумма2: double (nullable = true)
 |-- Время доставки: string (nullable = true)

```

### Data sample
```
| Телефон         | Адрес                                               | Тип оплат                | ФИО                            |   Сумма1 |           Сумма2 | Время доставки                                |
|:----------------|:----------------------------------------------------|:-------------------------|:-------------------------------|---------:|-----------------:|:----------------------------------------------|
| 8 968 962 36 10 | р-н Адлерский ул Гастелло 5                         | Безналичный расчет.      | Маргарян Андраник              |  3393350 |      3.39795e+06 | Доставка в ТК "ПЭК" Москва 1-ый Вязовский д.4 |
| 375296888867    | наставнический переулок 3 кв 58                     | Безналичный расчет.      | Руденков Алексей Станиславович |  1557500 |      1.5575e+06  | Доставка  c 16.00 до 24.00                    |
| 8-911-925-95-61 | ГП Заречье ул. Всесенняя д.1 корп.2 кв.22           | Безналичный расчет.      | Вячеслав                       |  1060630 |      1.06063e+06 | Доставка  c 10.00 до 18.00                    |
| 79521872245     | <blank>                                             | <blank>                  | Илья                           |  1059990 |      1.05999e+06 | <blank>                                       |
| 89166131556     | Москва| ул. Маршала Конева| 14                      | Оплата кредитной картой. | Апрятина Надежда Александровна |   887350 | 887350           | Доставка  c 10.00 до 18.00                    |
| 89608514692     | Бехтерева 2 Б                                       | Безналичный расчет.      | Ханов Сергей Евгеньевич        |   860000 | 860000           | Доставка в ТК "Деловые линии"                 |
| 79184071417     | Гагринская 10| 24                                   | Оплата кредитной картой. | Бояркин Роман Викторович       |   840000 | 840000           | Доставка  c 16.00 до 24.00                    |
| 9037680137      | КП Богородское Калужское ш                          | Безналичный расчет.      | Дубик Николай Николаевич       |   660000 | 660000           | Доставка  c 10.00 до 18.00                    |
| 89037214053     | судостроительная                                    | Наличными                | Орешкина Вера                  |   603180 | 603180           | Доставка  c 10.00 до 18.00                    |
| 89104009944     | Москва| Ломоносовский проспект| 25 корпус 2| кв.275 | Оплата кредитной картой. | Миронов Евгений Анатольевич    |   536250 | 445088           | Доставка  c 10.00 до 18.00                    |
| 89859940879     | п. Востряково| ул. Подольская| 24                   | Наличными                | Олег Белов                     |   466910 | 396874           | Доставка  c 16.00 до 24.00                    |
| 89262827003     | Moscow. Samarkandskiy b-r. 22-1-77                  | Наличными                | Наталья                        |   459950 | 459950           | Доставка  c 16.00 до 24.00                    |
| 89154664849     | Краснодарская| 12                                   | Наличными                | Качалин Алексей                |   457596 | 457596           | Доставка  c 10.00 до 18.00                    |
| 89258763365     | <blank>                                             | <blank>                  | Индира Рабаданова              |   453480 | 453480           | <blank>                                       |
| 79038460629     | <blank>                                             | <blank>                  | Вячеслав Коробов               |   453480 | 453480           | <blank>                                       |
| 89859999237     | МО                                                  | Безналичный расчет.      | Константин                     |   445580 | 369831           | Доставка  c 10.00 до 18.00                    |
| 89257983434     | Горки-8 деревня Солослово                           | Оплата кредитной картой. | Саид                           |   421190 | 362223           | Доставка  c 10.00 до 18.00                    |
| 79161584550     | Улица маршала Рыбалко| 13| 4 этаж| кв 55            | Оплата кредитной картой. | Казей Василий                  |   415950 | 415950           | Доставка  c 10.00 до 18.00                    |
| 79161584550     | <blank>                                             | <blank>                  | Василий                        |   415950 | 415950           | <blank>                                       |
| 8 917 5525520   | Ходынская 2| 294 кв| 25 этаж                        | Наличными                | Ефимов Виталий                 |   415773 | 415773           | Доставка  c 10.00 до 18.00                    |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- addresses: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- raw: string (nullable = false)
 |    |    |-- address: string (nullable = true)
 |    |    |-- location: struct (nullable = true)
 |    |    |    |-- region_type: string (nullable = true)
 |    |    |    |-- region_value: string (nullable = true)
 |    |    |    |-- settlement_region_type: string (nullable = true)
 |    |    |    |-- settlement_region_value: string (nullable = true)
 |    |    |    |-- settlement_type: string (nullable = true)
 |    |    |    |-- settlement_value: string (nullable = true)
 |    |    |    |-- street_type: string (nullable = true)
 |    |    |    |-- street_value: string (nullable = true)
 |    |    |    |-- house: string (nullable = true)
 |    |    |    |-- flat: string (nullable = true)
 |    |    |    |-- floor: string (nullable = true)
 |    |    |    |-- office: string (nullable = true)
 |    |    |    |-- corpus: string (nullable = true)
 |    |    |    |-- coordinates: array (nullable = true)
 |    |    |    |    |-- element: double (containsNull = true)
 |    |    |    |-- coord_detalization_lvl: integer (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 100.00% |
| Address | 95.02% |
| Addresses | 77.96% |



### Data sample
```
| names                              | phones          | address                                              | addresses                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:-----------------------------------|:----------------|:-----------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Маргарян Андраник']              | ['79689623610'] | ['р-н Адлерский ул Гастелло 5']                      | [Row(type=1, raw='р-н Адлерский ул Гастелло 5', address='улица Гастелло дом 5', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type='улица', street_value='Гастелло', house='5', flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                                                        |
| ['Вячеслав']                       | ['79119259561'] | ['ГП Заречье ул. Всесенняя д.1 корп.2 кв.22']        | [Row(type=1, raw='ГП Заречье ул. Всесенняя д.1 корп.2 кв.22', address='городское поселение Заречье улица Всесенняя дом 1 корпус 2 квартира 22', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='городское поселение', settlement_value='Заречье', street_type='улица', street_value='Всесенняя', house='1', flat='22', floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] |
| ['Илья']                           | ['79521872245'] |                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Апрятина Надежда Александровна'] | ['79166131556'] | ['Москва ул. Маршала Конева 14']                     | [Row(type=1, raw='Москва ул. Маршала Конева 14', address='город Москва улица Маршала конева дом 14', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type='улица', street_value='Маршала конева', house='14', flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                     |
| ['Ханов Сергей Евгеньевич']        | ['79608514692'] | ['Бехтерева 2 Б']                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Бояркин Роман Викторович']       | ['79184071417'] | ['Гагринская 10 24']                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Дубик Николай Николаевич']       | ['79037680137'] | ['КП Богородское Калужское ш']                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Орешкина Вера']                  | ['79037214053'] | ['Судостроительная']                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Миронов Евгений Анатольевич']    | ['79104009944'] | ['Москва Ломоносовский проспект 25 корпус 2 кв.275'] | [Row(type=1, raw='Москва Ломоносовский проспект 25 корпус 2 кв.275', address='город Москва проспект Ломоносовский дом 25 корпус 2 квартира 275', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type='проспект', street_value='Ломоносовский', house='25', flat='275', floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]      |
| ['Олег Белов']                     | ['79859940879'] | ['п. Востряково ул. Подольская 24']                  | [Row(type=1, raw='п. Востряково ул. Подольская 24', address='посёлок Востряково улица Подольская дом 24', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='посёлок', settlement_value='Востряково', street_type='улица', street_value='Подольская', house='24', flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                              |
| ['Наталья']                        | ['79262827003'] | ['Moscow. Samarkandskiy b-r. 22-1-77']               | [Row(type=1, raw='Moscow. Samarkandskiy b-r. 22-1-77', address='город Moscow', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Moscow', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                                                          |
| ['Качалин Алексей']                | ['79154664849'] | ['Краснодарская 12']                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Индира Рабаданова']              | ['79258763365'] |                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Вячеслав Коробов']               | ['79038460629'] |                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Константин']                     | ['79859999237'] |                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Саид']                           | ['79257983434'] | ['Горки-8 деревня Солослово']                        | [Row(type=1, raw='Горки-8 деревня Солослово', address='деревня Солослово', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='деревня', settlement_value='Солослово', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                                                         |
| ['Казей Василий']                  | ['79161584550'] | ['Улица маршала Рыбалко 13 4 этаж кв 55']            | [Row(type=1, raw='Улица маршала Рыбалко 13 4 этаж кв 55', address='улица Маршала Рыбалко', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type='улица', street_value='Маршала Рыбалко', house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                                     |
| ['Василий']                        | ['79161584550'] |                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Ефимов Виталий']                 | ['79175525520'] | ['Ходынская 2 294 кв 25 этаж']                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ['Шихалеев Алексей']               | ['79829128664'] | ['г.Тюмень Энергостроителей 29 кв 2']                | [Row(type=1, raw='г.Тюмень Энергостроителей 29 кв 2', address='город Тюмень квартира 2', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Тюмень', street_type=None, street_value=None, house=None, flat='2', floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                                                 |
```