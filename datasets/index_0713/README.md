# Parsetron results

## About row data

> - Code name: index_0713
> - File path: Плен РФ ВЧ 31134.csv
> - Total rows: 14

### Schema
```
root
 |-- name: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- birth_place: string (nullable = true)
 |-- address: string (nullable = true)
 |-- unit_code: string (nullable = true)
 |-- unit_name: string (nullable = true)
 |-- position: string (nullable = true)
 |-- rank: string (nullable = true)
 |-- education: string (nullable = true)

```

### Data sample
```
| name                             | birth_date   | birth_place                                         | address                                                                                  |   unit_code | unit_name   | position                     | rank      | education                |
|:---------------------------------|:-------------|:----------------------------------------------------|:-----------------------------------------------------------------------------------------|------------:|:------------|:-----------------------------|:----------|:-------------------------|
| Гаджиев Акиф Вагифович           | 23.01.2002   | республика Дагестан Дербентский район аул Вечрик    | Республика Дагестан, ул. Дербент, г. Тула, ул. Оболонная, 97                             |       31134 |             | стрелок                      | рядовой   | среднее профессиональное |
| Поздеев Андрей Юрьевич           | 16.06.2003   | Иркутская область Баханский район с. Ирёдкино       | Иркутская область, Бохарский район, с.Середкино, ул. Молодежная, 24, кв. 2               |       31134 |             | наводчик-оператор БМ-2       | рядовой   |                          |
| Городовалов Александр Васильевич | 15.04.2000   | Красноярский край пос. Байкит                       | Красноярский край, пос. Байкит, ул. Юрубчанская, 39, кв. 1                               |       31134 |             |                              |           | среднее профессиональное |
| Дмитреев Дмитрий Дмитриевич      | 15.04.2001   | г. Москва                                           | г. Москва, ул. Свободы, 19, и. 59                                                        |       31134 |             |                              | рядовой   | среднее профессиональное |
| Баканов Константин Александрович | 10.08.1974   | г. Псков                                            | Московская область, г. НароФоминск, ул. Восточная, 1, кв. 50                             |        3203 |             |                              |           |                          |
| Фонин Александр Сергеевич        | 26.02.1982   |                                                     | г. Дзержинск, ул. Ученая, 20                                                             |       11385 |             | заместитель командира взвода | сержант   | среднее                  |
| Черкасов Борис Олегович          | 04.02.2000   |                                                     | Московская, область,Наро-Фоминский район, пос. Калининец, 19, кв. 54                     |       31134 |             | водитель                     |           | среднее специальное      |
| Булгаков Александр Михайлович    | 20.09.2000   |                                                     | Московская область, Наро-Фоминский район, пос. Калининец,ул. Армейская, 1                |       31134 |             | водитель                     | рядовой   | среднее специальное      |
| Смолин Никита Иванович           | 11.06.1993   |                                                     | Московская область, Наро-Фоминский район, пос. Калининец,ул. Армейская, стр. 1           |       31134 |             | водитель медицинского отдела | рядовой   | высшее                   |
| Зунгруев Очер Олегович           | 17.12.1984   |                                                     | Московскаяобласть, Наро-Фоминский район, пос. Калининец, ул. Армейская, стр. 1           |       31134 |             |                              | капитан   | высшее                   |
| Тухфетов Рамиль Ренатович        | 10.09.1996   | Ульяновская область пгт. Новоспасское               | Московская область, Наро-Фоминский район, пос. Калининец,ул. Армейского строительства, 1 |       31134 |             | командир отделения           |           | среднее специальное      |
| Кружалов Александр Юрьевич       | 24.10.1987   |                                                     | Московскаяобласть, Наро-Фоминский район, рабочий поселок Калининец,ул. Армейская, стр. 1 |       31134 |             | фельдшер медицинского взвода | прапорщик | среднее специальное      |
| Польщиков Николай Валентинович   | 03.04.2001   | Воронежская обл, Ольховодкий район, пос. Ольховодка | Рязанская область, пос. Сарожок, ул. Коровинская, 95, кв. 2                              |       31134 |             | механик-водитель БМП-2       | ефрейтор  |                          |
| Морозов Александр Романович      | 08.06.2000   |                                                     | г. Москва, ул. Молодцова, 31, корп. 2 кв. 126                                            |       31134 |             | механик-водитель БМП-2       | ефрейтор  | среднее специальное      |
```


## About final data
> - Total rows: 14

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)
 |-- birth_place: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- educations: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = true)
 |    |    |-- level: integer (nullable = true)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- forces: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- tag_number: string (nullable = true)
 |    |    |-- unit_code: string (nullable = true)
 |    |    |-- unit_name: string (nullable = true)
 |    |    |-- callsign: string (nullable = true)
 |    |    |-- rank: string (nullable = true)
 |    |    |-- position: string (nullable = true)
 |    |    |-- mos_code: string (nullable = true)
 |    |    |-- category: integer (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 100.00% |
| Birth_place | 50.00% |
| Address | 100.00% |
| Educations | 78.57% |
| Forces | 100.00% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                                | birth_date   | birth_place                                       | address                                                                                   | educations                                                                             | forces                                                                                                                                                                                                          | source_entity_id                                         |
|:-------------------------------------|:-------------|:--------------------------------------------------|:------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| ['Польщиков Николай Валентинович']   | 03.04.2001   | Воронежская обл Ольховодкий район пос. Ольховодка | ['Рязанская область пос. Сарожок ул. Коровинская 95 кв. 2']                               |                                                                                        | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank='ефрейтор', position='механик-водитель БМП-2', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]        | adc098c13c8faae93e590bd2295c49781721ac038f1e8d5dd91a3857 |
| ['Баканов Константин Александрович'] | 10.08.1974   | г. Псков                                          | ['Московская область г. НароФоминск ул. Восточная 1 кв. 50']                              |                                                                                        | [Row(tag_number=None, unit_code='3203', unit_name=None, callsign=None, rank=None, position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                                   | e3114213978bce0e63a5a896aabfe176131b1c96b0870cd6facb28dc |
| ['Черкасов Борис Олегович']          | 04.02.2000   |                                                   | ['Московская область Наро-Фоминский район пос. Калининец 19 кв. 54']                      | [Row(title=None, level=5, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank=None, position='водитель', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                            | b95f192b8bd8d7caa2145a41e811d80974c28886512649b862827425 |
| ['Поздеев Андрей Юрьевич']           | 16.06.2003   | Иркутская область Баханский район с. Ирёдкино     | ['Иркутская область Бохарский район с.Середкино ул. Молодежная 24 кв. 2']                 |                                                                                        | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank='рядовой', position='наводчик-оператор БМ-2', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]         | 6c2d89760dff0155101fc73b050c449ab7954a106b440d29ac3ddc9d |
| ['Зунгруев Очер Олегович']           | 17.12.1984   |                                                   | ['Московскаяобласть Наро-Фоминский район пос. Калининец ул. Армейская стр. 1']            | [Row(title=None, level=6, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank='капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                             | b254901e27f785acb5872833a445a64099c75aeae55ed19a2785eed5 |
| ['Морозов Александр Романович']      | 08.06.2000   |                                                   | ['г. Москва ул. Молодцова 31 корп. 2 кв. 126']                                            | [Row(title=None, level=5, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank='ефрейтор', position='механик-водитель БМП-2', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]        | b1f5c9592faed4cf10dc6919cc1b9827c0d5a088b1bf848507a9f991 |
| ['Фонин Александр Сергеевич']        | 26.02.1982   |                                                   | ['г. Дзержинск ул. Ученая 20']                                                            | [Row(title=None, level=3, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='11385', unit_name=None, callsign=None, rank='сержант', position='заместитель командира взвода', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]   | d60572ad3f42c23289ae90f861b4b0f0ddff35e573495951ac7e7039 |
| ['Смолин Никита Иванович']           | 11.06.1993   |                                                   | ['Московская область Наро-Фоминский район пос. Калининец ул. Армейская стр. 1']           | [Row(title=None, level=6, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank='рядовой', position='водитель медицинского отдела', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]   | 3e4fef3b7e8be37ac3897766759cd674fbb43a540b08b9c520bfaed5 |
| ['Кружалов Александр Юрьевич']       | 24.10.1987   |                                                   | ['Московскаяобласть Наро-Фоминский район рабочий поселок Калининец ул. Армейская стр. 1'] | [Row(title=None, level=5, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank='прапорщик', position='фельдшер медицинского взвода', mos_code=None, category=None, date_start=None, date_end=None, comment=None)] | 4c2c77f554c949b63b45afc23c84efd3090f4b00882ed883e6bb1c03 |
| ['Тухфетов Рамиль Ренатович']        | 10.09.1996   | Ульяновская область пгт. Новоспасское             | ['Московская область Наро-Фоминский район пос. Калининец ул. Армейского строительства 1'] | [Row(title=None, level=5, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank=None, position='командир отделения', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                  | 0394a8c2964e416ac9c59886bb01dcbe6452b6e8bbf3b567d9632adc |
| ['Городовалов Александр Васильевич'] | 15.04.2000   | Красноярский край пос. Байкит                     | ['Красноярский край пос. Байкит ул. Юрубчанская 39 кв. 1']                                | [Row(title=None, level=4, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank=None, position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                                  | 8fa1a42aef8e1c99f04958197e1a6c08debbd76b0b54fc56ec501aa1 |
| ['Булгаков Александр Михайлович']    | 20.09.2000   |                                                   | ['Московская область Наро-Фоминский район пос. Калининец ул. Армейская 1']                | [Row(title=None, level=5, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank='рядовой', position='водитель', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                       | 0e819193c95074c6d112597a0067cf68dcb724e9eee3715d359b6c8b |
| ['Дмитреев Дмитрий Дмитриевич']      | 15.04.2001   | г. Москва                                         | ['г. Москва ул. Свободы 19 и. 59']                                                        | [Row(title=None, level=4, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank='рядовой', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                             | c841af27221e59dc6b2b9fd0afc64b4bb3a2ddb92d7474903f1b297b |
| ['Гаджиев Акиф Вагифович']           | 23.01.2002   | республика Дагестан Дербентский район аул Вечрик  | ['Республика Дагестан ул. Дербент г. Тула ул. Оболонная 97']                              | [Row(title=None, level=4, country=None, date_start=None, date_end=None, comment=None)] | [Row(tag_number=None, unit_code='31134', unit_name=None, callsign=None, rank='рядовой', position='стрелок', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                        | 7fd9763fcb67c917b85df602c73913a057b52ba6c6021e3bca7533e1 |
```