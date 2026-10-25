# Parsetron results

## About row data

> - Code name: index_0627
> - File path: Такси_Москва_2019.csv
> - Total rows: 23426

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- ТЕЛЕФОН: string (nullable = true)
 |-- НОМЕР АВТО: string (nullable = true)
 |-- ЦВЕТ: string (nullable = true)
 |-- МОДЕЛЬ: string (nullable = true)
 |-- ГОРОД: string (nullable = true)
 |-- КЛАСС: string (nullable = true)
 |-- СЛУЖБА ТАКСИ: string (nullable = true)

```

### Data sample
```
| ФИО                              |     ТЕЛЕФОН | НОМЕР АВТО   | ЦВЕТ   | МОДЕЛЬ                 | ГОРОД   | КЛАСС    | СЛУЖБА ТАКСИ                  |
|:---------------------------------|------------:|:-------------|:-------|:-----------------------|:--------|:---------|:------------------------------|
| Атакулов Умиджон Абдиазим Оглы   | 79853302606 | О979РА750    | белый  | Hyundai Solaris        | Москва  | Econom   | 505                           |
| Калиш Владимир Владимирович      | 79653338080 | Е451АС799    | чёрный | Mercedes-Benz E-klasse | Москва  |          | Риалтакси (5177746250150)     |
| Яворский Сергей Сергеевич        | 79250383944 | МН03077      | жёлтый | Skoda Octavia          | Москва  | Econom   | ООО Э.М.Е. (ТАКСОПАРК ПОБЕДА) |
| Асадов Джонхонгир                | 79998490160 | УА15877      | жёлтый | Kia Rio                | Москва  | Econom   | LigaTrans                     |
| Давлетбаев Айрат Дилфасович      | 79951215835 | МТ58277      | жёлтый | Kia Optima             | Москва  | Comfort+ | Фанта Такси                   |
| Кравченко Валерий Викторович     | 79916658574 | У142МТ197    | белый  | Hyundai Sonata         | Москва  | Econom   | Кравченко                     |
| Тагаев Ибро Дурусбекович         | 79330008858 | У941ММ750    | белый  | Kia Optima             | Москва  | Comfort+ | АВТО ЮРОЛ                     |
| Досумбетов Эмилбек Нурмаматович  | 79261672358 | Т792ВК799    | белый  | Hyundai Solaris        | Москва  | Econom   | ИП                            |
| Темиров Темирхан Азизханович     | 79261526273 | Н412ТА750    | белый  | Hyundai Solaris        | Москва  | Econom   | Вива                          |
| Орозбеков Самат Толонович        | 79999262419 | НЕ64177      | жёлтый | Hyundai Solaris        | Москва  | Econom   | Транспортная                  |
| Азимов Бехруз Аброрович          | 79999169010 | В512ХС777    | белый  | Hyundai Solaris        | Москва  | Econom   | Шустрик                       |
| Епифанцев Алексей                | 79690878351 | У737РР750    | белый  | Kia Rio                | Москва  | Econom   | Удача_балашиха                |
| Жарматов Тимурлан Абдылвакыпович | 79017595065 | ОЕ21377      | жёлтый | Citroen C4 Picasso     | Москва  | Econom   | ООО АЛЬФА-СЕРВИС              |
| Лукин Владислав Михайлович       | 79260090097 | УК09777      | жёлтый | Volkswagen Polo        | Москва  | Econom   | МедиаХолдинг                  |
| Хрипко Игорь Иванович            | 79537362309 | РР24077      | жёлтый | Skoda Rapid            | Москва  | Econom   | SouthPort Taxi                |
| Саъдиев Одилжон Шодиходжаевич    | 79683882020 | С789КТ123    | белый  | Chevrolet Cruze        | Москва  | Econom   | MaSteR                        |
| Солянник Виктор Викторович       | 79267022710 | О928ЕА799    | белый  | Ravon Gentra           | Москва  | Econom   | Солянник                      |
| Свинцов Василий Георгиевич       | 79150767667 | Х602ТК750    | белый  | Toyota Camry           | Москва  | Econom   | Свинцов                       |
| Шукюров Фарид Физулиевич         | 79929992949 | Н555ВЕ37     | белый  | Ford Mondeo            | Москва  | Comfort  | Шукюров                       |
| Гаджиев Тагир Казибекович        | 79207996082 | Р205ВА750    | жёлтый | Volkswagen Polo        | Москва  | Econom   | Билал                         |
```


## About final data
> - Total rows: 23424

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- vehicles: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = false)
 |    |    |-- model: string (nullable = true)
 |    |    |-- year: integer (nullable = true)
 |    |    |-- color: string (nullable = true)
 |    |    |-- number: string (nullable = true)
 |    |    |-- vin: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Raw_metadata | 100.00% |
| Address | 100.00% |
| Phones | 99.91% |
| Vehicles | 100.00% |



### Data sample
```
| names                                | raw_metadata                                                           | address    | phones          | vehicles                                                                                                             |
|:-------------------------------------|:-----------------------------------------------------------------------|:-----------|:----------------|:---------------------------------------------------------------------------------------------------------------------|
| ['Атакулов Умиджон Абдиазим Оглы']   | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "505"}']                         | ['Москва'] | ['79853302606'] | [Row(type=1, model='Hyundai Solaris', year=None, color='белый', number='О979РА750', vin=None, comment=None)]         |
| ['Калиш Владимир Владимирович']      | ['{"СЛУЖБА ТАКСИ": "Риалтакси 5177746250150"}']                        | ['Москва'] | ['79653338080'] | [Row(type=1, model='Mercedes-Benz E-klasse', year=None, color='чёрный', number='Е451АС799', vin=None, comment=None)] |
| ['Яворский Сергей Сергеевич']        | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "ООО Э.М.Е. ТАКСОПАРК ПОБЕДА"}'] | ['Москва'] | ['79250383944'] | [Row(type=1, model='Skoda Octavia', year=None, color='жёлтый', number='МН03077', vin=None, comment=None)]            |
| ['Асадов Джонхонгир']                | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "LigaTrans"}']                   | ['Москва'] | ['79998490160'] | [Row(type=1, model=None, year=None, color='жёлтый', number='УА15877', vin=None, comment=None)]                       |
| ['Давлетбаев Айрат Дилфасович']      | ['{"КЛАСС": "Comfort", "СЛУЖБА ТАКСИ": "Фанта Такси"}']                | ['Москва'] | ['79951215835'] | [Row(type=1, model=None, year=None, color='жёлтый', number='МТ58277', vin=None, comment=None)]                       |
| ['Кравченко Валерий Викторович']     | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "Кравченко"}']                   | ['Москва'] | ['79916658574'] | [Row(type=1, model='Hyundai Sonata', year=None, color='белый', number='У142МТ197', vin=None, comment=None)]          |
| ['Тагаев Ибро Дурусбекович']         | ['{"КЛАСС": "Comfort", "СЛУЖБА ТАКСИ": "АВТО ЮРОЛ"}']                  | ['Москва'] | ['79330008858'] | [Row(type=1, model=None, year=None, color='белый', number='У941ММ750', vin=None, comment=None)]                      |
| ['Досумбетов Эмилбек Нурмаматович']  | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "ИП"}']                          | ['Москва'] | ['79261672358'] | [Row(type=1, model='Hyundai Solaris', year=None, color='белый', number='Т792ВК799', vin=None, comment=None)]         |
| ['Темиров Темирхан Азизханович']     | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "Вива"}']                        | ['Москва'] | ['79261526273'] | [Row(type=1, model='Hyundai Solaris', year=None, color='белый', number='Н412ТА750', vin=None, comment=None)]         |
| ['Орозбеков Самат Толонович']        | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "Транспортная"}']                | ['Москва'] | ['79999262419'] | [Row(type=1, model='Hyundai Solaris', year=None, color='жёлтый', number='НЕ64177', vin=None, comment=None)]          |
| ['Азимов Бехруз Аброрович']          | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "Шустрик"}']                     | ['Москва'] | ['79999169010'] | [Row(type=1, model='Hyundai Solaris', year=None, color='белый', number='В512ХС777', vin=None, comment=None)]         |
| ['Епифанцев Алексей']                | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "Удачабалашиха"}']               | ['Москва'] | ['79690878351'] | [Row(type=1, model=None, year=None, color='белый', number='У737РР750', vin=None, comment=None)]                      |
| ['Жарматов Тимурлан Абдылвакыпович'] | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "ООО АЛЬФА-СЕРВИС"}']            | ['Москва'] | ['79017595065'] | [Row(type=1, model='Citroen C4 Picasso', year=None, color='жёлтый', number='ОЕ21377', vin=None, comment=None)]       |
| ['Лукин Владислав Михайлович']       | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "МедиаХолдинг"}']                | ['Москва'] | ['79260090097'] | [Row(type=1, model='Volkswagen Polo', year=None, color='жёлтый', number='УК09777', vin=None, comment=None)]          |
| ['Хрипко Игорь Иванович']            | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "SouthPort Taxi"}']              | ['Москва'] | ['79537362309'] | [Row(type=1, model='Skoda Rapid', year=None, color='жёлтый', number='РР24077', vin=None, comment=None)]              |
| ['Саъдиев Одилжон Шодиходжаевич']    | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "MaSteR"}']                      | ['Москва'] | ['79683882020'] | [Row(type=1, model=None, year=None, color='белый', number='С789КТ123', vin=None, comment=None)]                      |
| ['Солянник Виктор Викторович']       | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "Солянник"}']                    | ['Москва'] | ['79267022710'] | [Row(type=1, model='Ravon Gentra', year=None, color='белый', number='О928ЕА799', vin=None, comment=None)]            |
| ['Свинцов Василий Георгиевич']       | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "Свинцов"}']                     | ['Москва'] | ['79150767667'] | [Row(type=1, model=None, year=None, color='белый', number='Х602ТК750', vin=None, comment=None)]                      |
| ['Шукюров Фарид Физулиевич']         | ['{"КЛАСС": "Comfort", "СЛУЖБА ТАКСИ": "Шукюров"}']                    | ['Москва'] | ['79929992949'] | [Row(type=1, model='Ford Mondeo', year=None, color='белый', number='Н555ВЕ37', vin=None, comment=None)]              |
| ['Гаджиев Тагир Казибекович']        | ['{"КЛАСС": "Econom", "СЛУЖБА ТАКСИ": "Билал"}']                       | ['Москва'] | ['79207996082'] | [Row(type=1, model='Volkswagen Polo', year=None, color='жёлтый', number='Р205ВА750', vin=None, comment=None)]        |
```