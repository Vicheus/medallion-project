# Parsetron results

## About row data

> - File path: nbki.ru_2024_500k_sample.csv
> - Total rows: 499997

### Schema
```
root
 |-- sum: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- document: string (nullable = true)
 |-- passport: string (nullable = true)
 |-- passport_date: string (nullable = true)
 |-- birthdate: string (nullable = true)
 |-- address: string (nullable = true)

```

### Data sample
```
|   sum | name                             |       phone |   document |   passport | passport_date   | birthdate   | address                         |
|------:|:---------------------------------|------------:|-----------:|-----------:|:----------------|:------------|:--------------------------------|
|  7000 | Фатьянов Иван Константинович     | 79283359633 |  701639483 | 0701639483 | 2002-01-05      | 24.10.1952  | Кисловодск, Ставропольский край |
|  3000 | Ёлкин Валерий Васильевич         | 79517784646 | 7512167155 | 7512167155 | 2012-08-16      | 06.07.1992  |                                 |
| 15000 | Ёлкин Илья Николаевич            | 79536925315 | 3008868023 | 3008868023 | 2009-04-15      | 30.08.1988  |                                 |
|  4000 | Ёлкина Ксения Александровна      | 79312973950 | 4016653613 | 4016653613 | 2016-10-28      | 30.11.1990  |                                 |
| 25000 | Ёрж Богдан Павлович              | 79282289897 |  316546159 | 0316546159 | 2016-09-22      | 02.08.1982  |                                 |
|  8000 | Ёрматова Зарнигор Хошимджоновна  | 79661464040 | 2909370769 | 2909370769 | 2009-10-27      | 31.05.1981  |                                 |
|  4000 | Ёров Умед Хатамович              | 79274393080 | 9207174161 | 9207174161 | 2007-08-07      | 06.07.1987  |                                 |
| 10000 | Ёршина Мария Александровна       | 79604648265 | 6014567475 | 6014567475 | 2014-07-14      | 24.02.1992  |                                 |
|  7000 | АБАКУМОВ АЛЕКСАНДР АЛЕКСАНДРОВИЧ | 79827789757 | 7116262208 | 7116262208 | 2017-02-21      | 26.10.1986  |                                 |
| 10000 | АБГАРЯН АРТУШ УСИКОВИЧ           | 79624803969 | 3311130597 | 3311130597 | 2011-12-30      | 03.10.1965  |                                 |
| 12000 | АБГАРЯН АРТУШ УСИКОВИЧ           | 79051682964 | 3311130597 | 3311130597 | 2011-12-30      | 03.10.1965  |                                 |
|  7000 | АБГАРЯН АРТУШ УСИКОВИЧ           | 79685614368 | 3311130597 | 3311130597 | 2011-12-30      | 03.10.1965  |                                 |
| 11000 | АБГАРЯН АРТУШ УСИКОВИЧ           | 79155021443 | 3311130597 | 3311130597 | 2011-12-30      | 03.10.1965  |                                 |
|  9000 | АБДРАШИТОВ РИАЛ РАИСОВИЧ         | 79373585079 | 8004108203 | 8004108203 | 2003-03-04      | 07.11.1982  |                                 |
|  7000 | АБДУЛИНА МАДИНА САРСЕНБАЕВНА     | 79102064869 | 1299050117 | 1299050117 | 2000-04-06      | 24.12.1978  |                                 |
|  7000 | АБДУРАФЕЕВА РОЗА ИСАКАЕВНА       | 79234695154 | 3215630512 | 3215630512 | 2016-03-23      | 05.03.1971  |                                 |
|  7000 | АБДУРАФЕЕВА РОЗА ИСАКАЕВНА       | 79512277141 | 3215630512 | 3215630512 | 2016-03-23      | 05.03.1971  |                                 |
|  7000 | АБЛЯКИМОВА РЕБЯ ЧИНГИЗОВНА       | 79618576646 | 3914908207 | 3914908207 | 2015-09-02      | 07.08.1997  |                                 |
|  3000 | АБРАМОВА ИРИНА МИХАЙЛОВНА        | 79167082775 | 4514911336 | 4514911336 | 2015-02-19      | 11.12.1969  |                                 |
|  7000 | АБРАМОВА ТАТЬЯНА БОРИСОВНА       | 79175127927 | 4501625010 | 4501625010 | 2001-10-22      | 01.02.1976  |                                 |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- addresses: array (nullable = true)
 |    |-- element: struct (containsNull = true)
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
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)

```



### Data sample
```
| names                                  | birth_date   | phones          | address                                   | addresses                                                                                                                                                                                                                                                                                                                                                                                                                                                     | documents                                                                                                                         |
|:---------------------------------------|:-------------|:----------------|:------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| ['Мишаков Анатолий Владимирович']      |              |                 |                                           | [None]                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Row(type=0, serial='6300268755', country='RUS', date_issue='31.10.2000', date_expire=None, authority=None, authority_code=None)] |
| ['Дмитриенко Галина Николаевна']       | 01.01.1948   | ['79627974852'] |                                           | [None]                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Row(type=0, serial='0103786693', country='RUS', date_issue='07.05.2003', date_expire=None, authority=None, authority_code=None)] |
| ['Адушева Ольга Федоровна']            | 01.01.1966   | ['79871396678'] |                                           | [None]                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Row(type=0, serial='8010228798', country='RUS', date_issue='20.01.2011', date_expire=None, authority=None, authority_code=None)] |
| ['Чепуштанов Игорь Анатольевич']       | 01.01.1973   | ['79029988622'] | ['Барнаул Алтайский край']                | [Row(type=1, raw='Барнаул Алтайский край', address='край Алтайский город Барнаул', location=Row(region_type='край', region_value='Алтайский', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Барнаул', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                              | [Row(type=0, serial='0116268836', country='RUS', date_issue='25.10.2016', date_expire=None, authority=None, authority_code=None)] |
| ['Акатов Роман Юрьевич']               | 01.01.1974   | ['79204459769'] | ['Воронеж Воронежская область']           | [Row(type=1, raw='Воронеж Воронежская область', address='область Воронежская город Воронеж', location=Row(region_type='область', region_value='Воронежская', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Воронеж', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                               | [Row(type=0, serial='2004254017', country='RUS', date_issue='17.05.2004', date_expire=None, authority=None, authority_code=None)] |
| ['Ляпичев Александр Сергеевич']        | 01.01.1980   | ['79052650379'] | ['Санкт-Петербург Ленинградская область'] | [Row(type=1, raw='Санкт-Петербург Ленинградская область', address='область Ленинградская город Санкт-петербург', location=Row(region_type='область', region_value='Ленинградская', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Санкт-петербург', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] | [Row(type=0, serial='4008556290', country='RUS', date_issue='12.08.2008', date_expire=None, authority=None, authority_code=None)] |
| ['Зубарева Татьяна Витальевна']        | 01.01.1981   | ['79122963330'] |                                           | [None]                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Row(type=0, serial='6505056358', country='RUS', date_issue='16.02.2004', date_expire=None, authority=None, authority_code=None)] |
| ['Сережа Асланян Михайловна']          | 01.01.1985   | ['79284131015'] | ['Геленджик Краснодарский край']          | [Row(type=1, raw='Геленджик Краснодарский край', address='край Краснодарский город Геленджик', location=Row(region_type='край', region_value='Краснодарский', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Геленджик', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                            | [Row(type=0, serial='0315172940', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]         |
| ['Малеев Дмитрий Викторович']          | 01.01.1987   | ['79182915525'] |                                           | [None]                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Row(type=0, serial='0808771655', country='RUS', date_issue='09.12.2008', date_expire=None, authority=None, authority_code=None)] |
| ['Янтурина Вилия Айратовна']           | 01.01.1987   | ['79050069986'] |                                           | [None]                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Row(type=0, serial='8006951251', country='RUS', date_issue='12.01.2007', date_expire=None, authority=None, authority_code=None)] |
| ['Деденева Татьяна Юрьевна']           | 01.01.1989   | ['79033856064'] | ['Балашов Саратовская область']           | [Row(type=1, raw='Балашов Саратовская область', address='область Саратовская', location=Row(region_type='область', region_value='Саратовская', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                     | [Row(type=0, serial='6308293669', country='RUS', date_issue='03.02.2009', date_expire=None, authority=None, authority_code=None)] |
| ['Алкалдл Опаопалд Щшомадлапло']       | 01.01.1990   | ['79885389232'] |                                           | [None]                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                   |
| ['Исаков Михаил Петрович']             | 01.01.1990   | ['79026368818'] | ['Пермь Пермский край']                   | [Row(type=1, raw='Пермь Пермский край', address='край Пермский город Пермь', location=Row(region_type='край', region_value='Пермский', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Пермь', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                       | [Row(type=0, serial='6915697330', country='RUS', date_issue='01.01.1970', date_expire=None, authority=None, authority_code=None)] |
| ['Бычков Алексей Эдуардович']          | 01.01.1992   | ['79814211461'] | ['Новосибирск Новосибирская область']     | [Row(type=1, raw='Новосибирск Новосибирская область', address='область Новосибирская город Новосибирск', location=Row(region_type='область', region_value='Новосибирская', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Новосибирск', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]             | [Row(type=0, serial='1911804175', country='RUS', date_issue='20.02.2012', date_expire=None, authority=None, authority_code=None)] |
| ['Уварова Татьяна Андреевна']          | 01.01.1993   | ['79009868507'] | ['Липецк Липецкая область']               | [Row(type=1, raw='Липецк Липецкая область', address='область Липецкая город Липецк', location=Row(region_type='область', region_value='Липецкая', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Липецк', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                           | [Row(type=0, serial='4216023685', country='RUS', date_issue='01.08.2016', date_expire=None, authority=None, authority_code=None)] |
| ['Суханова Елена Юрьевна']             | 01.01.1994   | ['79204298685'] | ['Нововоронеж Воронежская область']       | [Row(type=1, raw='Нововоронеж Воронежская область', address='область Воронежская', location=Row(region_type='область', region_value='Воронежская', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                 | [Row(type=0, serial='2013696872', country='RUS', date_issue='01.02.2014', date_expire=None, authority=None, authority_code=None)] |
| ['Володина Кристина Игоревна']         | 01.01.1995   | ['79158092171'] |                                           | [None]                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Row(type=0, serial='1514177095', country='RUS', date_issue='28.01.2015', date_expire=None, authority=None, authority_code=None)] |
| ['Магомедов Гамзат Замирович']         | 01.02.1965   | ['79170938018'] | ['Астрахань Астраханская область']        | [Row(type=1, raw='Астрахань Астраханская область', address='область Астраханская город Астрахань', location=Row(region_type='область', region_value='Астраханская', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Астрахань', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                      | [Row(type=0, serial='1211380959', country='RUS', date_issue='29.07.2011', date_expire=None, authority=None, authority_code=None)] |
| ['Мартемьянова Людмила Александровна'] | 01.02.1974   | ['79178557304'] |                                           | [None]                                                                                                                                                                                                                                                                                                                                                                                                                                                        | [Row(type=0, serial='9202948926', country='RUS', date_issue='23.03.2002', date_expire=None, authority=None, authority_code=None)] |
| ['Немтинова Анна Вячеславовна']        | 01.02.1979   | ['79514976638'] | ['Красный Сулин Ростовская область']      | [Row(type=1, raw='Красный Сулин Ростовская область', address='область Ростовская', location=Row(region_type='область', region_value='Ростовская', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                  | [Row(type=0, serial='6008409247', country='RUS', date_issue='02.12.2008', date_expire=None, authority=None, authority_code=None)] |
```