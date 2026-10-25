# Parsetron results

## About row data

> - File path: max.ru - @StormBaseAdapter.csv
> - Total rows: 2644018

### Schema
```
root
 |-- Номер телефона: long (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Пол: string (nullable = true)
 |-- Регион: string (nullable = true)
 |-- Оператор: string (nullable = true)
 |-- Часовой пояс: string (nullable = true)

```

### Data sample
```
|   Номер телефона | ФИО                             | Дата рождения   | Пол     | Регион              | Оператор                  | Часовой пояс   |
|-----------------:|:--------------------------------|:----------------|:--------|:--------------------|:--------------------------|:---------------|
|      79624039854 | ПАНЮКОВА ТАТЬЯНА АЛЕКСЕЕВНА     | 26.01.1961      | Женский | Ставропольский край | ПАО "Вымпел-Коммуникации" | UTC+3:00       |
|      79020566820 | РЕШЕТОВ ВЯЧЕСЛАВ ПЕТРОВИЧ       | 17.10.1948      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79020570002 | ЛАТИПОВ БЕХРУЗ УТКИРОВИЧ        | 06.09.1995      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79020581651 | ЕЛЕНА РУСАНОВА ПЕТРОВНА         | 04.07.1972      | Женский | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79020613043 | КУЧМЕНОК ЕЛЕНА ВИКТОРОВНА       | 07.03.1960      | Женский | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79020664106 | ТАРАСЮК ОЛЬГА ПАВЛОВНА          | 26.04.1962      | Женский | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79020680965 | СТЕПАНЕЦ СЕРГЕЙ ВАЛЕНТИНОВИЧ    | 13.06.1957      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79020778255 | ДИОРГЕСОВА ЛЮБОВЬ БОРИСОВНА     | 20.10.1949      | Женский | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025206344 | МИРЗОЯН ЮРИЙ ЛЕВОНОВИЧ          | 13.03.1997      | Женский | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025209898 | САДОВСКАЯ ЮЛИЯ ЮРЬЕВНА          | 10.11.1974      | Женский | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025215151 | ЯКУБОВИЧ АНДРЕЙ ГЕОРГИЕВИЧ      | 01.02.1975      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025218322 | КАДАНЦЕВ ВЯЧЕСЛАВ ВЛАДИМИРОВИЧ  | 21.09.1961      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025220062 | ЛЕЩУК НАТАЛЬЯ АЛЕКСАНДРОВНА     | 18.04.1972      | Женский | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025221360 | ШЕЛКОВ МАРАТ ВЛАДИМИРОВИЧ       | 13.08.1968      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025224252 | СУШКОВ ФЕДОР ФЕДОРОВИЧ          | 31.12.1958      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025228846 | СЕРГЕЕВ ГЕННАДИЙ МИХАЙЛОВИЧ     | 28.04.1958      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025235360 | ПЕРЕТЯТЬКО ВАСИЛИЙ ВИКТОРОВИЧ   | 23.03.1964      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025240479 | ГОНЧАРУК АЛЕКСЕЙ КОНСТАНТИНОВИЧ | 09.07.1962      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025240983 | ДЫБОВ ВЛАДИМИР ВИКТОРОВИЧ       | 08.04.1968      | Мужской | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
|      79025243754 | ШПАК ТАТЬЯНА МИХАЙЛОВНА         | 28.09.1965      | Женский | Приморский край     | ПАО "Вымпел-Коммуникации" | UTC+10:00      |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
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
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 99.87% |
| Sex | 100.00% |
| Phones | 100.00% |
| Address | 100.00% |
| Addresses | 100.00% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                                | birth_date   |   sex | phones          | address                          | addresses                                                                                                                                                                                                                                                                                                                                                                                                                       | raw_metadata                                |
|:-------------------------------------|:-------------|------:|:----------------|:---------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|
| ['Cадчикова Полина Андреевна']       | 13.09.1988   |     0 | ['79033950940'] | ['Оренбургская обл.']            | [Row(type=1, raw='Оренбургская обл.', address='Оренбургская обл.', location=Row(region_type=None, region_value='Оренбургская обл.', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                  | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['А Алексей А']                      | 18.11.2017   |     1 | ['79067620590'] | ['г. Москва Московская область'] | [Row(type=1, raw='г. Москва Московская область', address='г. Москва Московская область', location=Row(region_type=None, region_value='г. Москва Московская область', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абаимов Глеб Германович']          | 06.02.1968   |     1 | ['79683784630'] | ['г. Москва Московская область'] | [Row(type=1, raw='г. Москва Московская область', address='г. Москва Московская область', location=Row(region_type=None, region_value='г. Москва Московская область', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абакумец Любовь Ивановна']         | 22.02.1945   |     0 | ['79089961173'] | ['Приморский край']              | [Row(type=1, raw='Приморский край', address='Приморский край', location=Row(region_type=None, region_value='Приморский край', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                        | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абакумова Вера Геннадьевна']       | 29.01.1983   |     0 | ['79683883213'] | ['г. Москва Московская область'] | [Row(type=1, raw='г. Москва Московская область', address='г. Москва Московская область', location=Row(region_type=None, region_value='г. Москва Московская область', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абакумова Людмила Николаевна']     | 06.04.1980   |     0 | ['79651666699'] | ['г. Москва Московская область'] | [Row(type=1, raw='г. Москва Московская область', address='г. Москва Московская область', location=Row(region_type=None, region_value='г. Москва Московская область', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абакшина Валентина Васильевна']    | 17.01.1959   |     0 | ['79094634508'] | ['Краснодарский край']           | [Row(type=1, raw='Краснодарский край', address='Краснодарский край', location=Row(region_type=None, region_value='Краснодарский край', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                               | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абанина Юлия Павловна']            | 28.01.1986   |     0 | ['79657127515'] | ['Рязанская обл.']               | [Row(type=1, raw='Рязанская обл.', address='Рязанская обл.', location=Row(region_type=None, region_value='Рязанская обл.', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                           | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абаносимов Александр Петрович']    | 27.11.1955   |     1 | ['79033955337'] | ['Оренбургская обл.']            | [Row(type=1, raw='Оренбургская обл.', address='Оренбургская обл.', location=Row(region_type=None, region_value='Оренбургская обл.', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                  | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абасова Натаван Викторовна']       | 22.08.1978   |     1 | ['79057219458'] | ['г. Москва Московская область'] | [Row(type=1, raw='г. Москва Московская область', address='г. Москва Московская область', location=Row(region_type=None, region_value='г. Москва Московская область', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абасова Ольга Викторовна']         | 04.02.1958   |     0 | ['79067999510'] | ['г. Москва Московская область'] | [Row(type=1, raw='г. Москва Московская область', address='г. Москва Московская область', location=Row(region_type=None, region_value='г. Москва Московская область', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абашева Анастасия Борисовна']      | 21.07.1988   |     0 | ['79634838194'] | ['Республика Удмуртская']        | [Row(type=1, raw='Республика Удмуртская', address='Республика Удмуртская', location=Row(region_type=None, region_value='Республика Удмуртская', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                      | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абашина Лидия Романовна']          | 01.04.1959   |     0 | ['79099400745'] | ['г. Москва Московская область'] | [Row(type=1, raw='г. Москва Московская область', address='г. Москва Московская область', location=Row(region_type=None, region_value='г. Москва Московская область', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абгарян Анна Константиновна']      | 17.09.1988   |     0 | ['79630202120'] | ['Пермский край']                | [Row(type=1, raw='Пермский край', address='Пермский край', location=Row(region_type=None, region_value='Пермский край', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                              | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абдикаев Ильмас Шарифзянович']     | 01.06.1960   |     1 | ['79033362438'] | ['Ульяновская обл.']             | [Row(type=1, raw='Ульяновская обл.', address='Ульяновская обл.', location=Row(region_type=None, region_value='Ульяновская обл.', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                     | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абдрафикова Альбина Агзамовна']    | 07.01.1967   |     1 | ['79674578235'] | ['Республика Башкортостан']      | [Row(type=1, raw='Республика Башкортостан', address='Республика Башкортостан', location=Row(region_type=None, region_value='Республика Башкортостан', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абдрафикова Анастасия Андреевна']  | 21.05.1987   |     0 | ['79639057138'] | ['Республика Башкортостан']      | [Row(type=1, raw='Республика Башкортостан', address='Республика Башкортостан', location=Row(region_type=None, region_value='Республика Башкортостан', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абдрахманова Жумабике Хадимовна']  | 21.11.1957   |     1 | ['79608644703'] | ['Астраханская обл.']            | [Row(type=1, raw='Астраханская обл.', address='Астраханская обл.', location=Row(region_type=None, region_value='Астраханская обл.', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                  | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абдрахманова Сумая']               | 03.05.1990   |     1 | ['79632726185'] | ['Свердловская обл.']            | [Row(type=1, raw='Свердловская обл.', address='Свердловская обл.', location=Row(region_type=None, region_value='Свердловская обл.', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                  | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
| ['Абдуламинов Искандар Шомуратович'] | 01.04.1976   |     1 | ['79038023668'] | ['Тверская обл.']                | [Row(type=1, raw='Тверская обл.', address='Тверская обл.', location=Row(region_type=None, region_value='Тверская обл.', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                              | ['{"Оператор": "ПАО Вымпел-Коммуникации"}'] |
```