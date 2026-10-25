# Parsetron results

## About row data

> - Code name: index_0053
> - File path: /media/user/TRANSCEND/Databases/index_0053/raw/preprocessing/zaymer.csv
> - Total rows: 16857157

### Schema
```
root
 |-- registred_subject_id: string (nullable = true)
 |-- actual_subject_id: string (nullable = true)
 |-- status: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- sex: string (nullable = true)
 |-- birthday: string (nullable = true)
 |-- birthplace: string (nullable = true)
 |-- phone_mobile: string (nullable = true)
 |-- passport_series: string (nullable = true)
 |-- passport_number: string (nullable = true)
 |-- passport_date: string (nullable = true)
 |-- passport_issuer: string (nullable = true)
 |-- passport_subdivision: string (nullable = true)
 |-- registred_city: string (nullable = true)
 |-- registred_street: string (nullable = true)
 |-- registred_house: string (nullable = true)
 |-- registred_flat: string (nullable = true)
 |-- registred_postal: string (nullable = true)
 |-- actual_city: string (nullable = true)
 |-- actual_street: string (nullable = true)
 |-- actual_house: string (nullable = true)
 |-- actual_flat: string (nullable = true)
 |-- actual_postal: string (nullable = true)
 |-- INN: string (nullable = true)

```

### Data sample
```
| registred_subject_id   | actual_subject_id   | status              | first_name   | last_name    | middle_name     | sex      | birthday     | birthplace                                                 | phone_mobile   | passport_series   | passport_number   | passport_date   | passport_issuer                                                                                              | passport_subdivision   | registred_city                        | registred_street         | registred_house   | registred_flat   | registred_postal   | actual_city       | actual_street            | actual_house   | actual_flat   | actual_postal   |           INN |
|:-----------------------|:--------------------|:--------------------|:-------------|:-------------|:----------------|:---------|:-------------|:-----------------------------------------------------------|:---------------|:------------------|:------------------|:----------------|:-------------------------------------------------------------------------------------------------------------|:-----------------------|:--------------------------------------|:-------------------------|:------------------|:-----------------|:-------------------|:------------------|:-------------------------|:---------------|:--------------|:----------------|--------------:|
| null                   | null                | null                | 'Робот'      | 'Займер'     | null            | 'male'   | null         | null                                                       | null           | null              | null              | null            | null                                                                                                         | null                   | null                                  | null                     | null              | null             | null               | null              | null                     | null           | null          | null            |             0 |
| null                   | null                | 'ready'             | 'Денис'      | 'Чупрунов'   | 'Сергеевич'     | 'male'   | '1983-03-11' | 'Кемерово'                                                 | null           | null              | null              | '2008-07-07'    | 'ТП №68 ОТДЕЛА УФМС РОССИИ ПО САНКТ-ПЕТЕРБУРГУ И ЛЕНИНГРАДСКОЙ ОБЛ. В ПРИМОРСКОМ Р-НЕ ГОР. САНКТ-ПЕТЕРБУРГА' | null                   | 'Санкт-Петербург'                     | 'Комендантский проспект' | '17'              | '83'             | null               | 'Санкт-Петербург' | 'Комендантский проспект' | '17'           | '83'          | null            |             0 |
| 24                     | 24                  | 'ready'             | 'Ольга'      | 'Сидорова'   | 'Александровна' | 'female' | '1984-09-23' | 'пос.Южно-Енисейск Мотыгинского района Красноярского края' | 79233736056    | 413               | 499683            | '2013-10-21'    | 'отделом уфмс россии по красноярскому краю в минусинском районе'                                             | '240-013'              | 'пос.Южно-Енисейск Красноярский край' | 'Дачная'                 | '5'               | '1'              | '663416'           | 'Минусинск'       | 'Ботаническая'           | '51'           | '26'          | '662610'        |  242600470570 |
| null                   | null                | 'site_reg_aboutme'  | 'НАДЕЖДА'    | 'СИДОРОВА'   | 'НИКОЛАЕВНА'    | 'female' | '1961-03-27' | 'с.ходаки барского района винницкой обл.'                  | null           | null              | null              | '2006-04-07'    | 'отделом внутренних дел города губкина и губкинского района белгородской области'                            | null                   | 'губкин'                              | 'парковая'               | '3'               | '22'             | '309190'           | 'губкин'          | 'парковая'               | '3'            | '22'          | '309190'        |             0 |
| null                   | null                | 'site_reg_aboutme'  | 'МАРИЯ'      | 'СИДОРОВА'   | 'ВИКТОРОВНА'    | 'female' | '1984-04-17' | 'пос. пачелма пачелмского р-на пензенской обл.'            | 79067519129    | 1409              | 67012             | '2010-04-06'    | 'отделом уфмс россии по белгородской области в губкинском районе'                                            | null                   | 'Губкин'                              | 'парковая'               | '3'               | '22'             | null               | 'Москва'          | 'тамбовская'             | '10'           | '8'           | null            |  582801503237 |
| null                   | null                | 'site_reg_aboutme'  | 'СВЕТЛАНА'   | 'ЕРМОЛАЕВА'  | 'ИВАНОВНА'      | 'female' | '1986-12-05' | 'Губкин'                                                   | 79263690743    | 1409              | 42326             | '2009-10-14'    | 'ОТДЕЛОМ УФМС РОССИИ ПО БЕЛГОРОДСКОЙ ОБЛАСТИ В ГУБКИНСКОМ РАЙОНЕ'                                            | null                   | 'Губкин'                              | 'ПАРКОВАЯ'               | '3'               | '22'             | null               | 'Москва'          | 'ТАМБОВСКАЯ'             | '10'           | '8'           | null            |  312707335923 |
| 34                     | 34                  | 'ready'             | 'Андрей'     | 'Логинычев'  | 'Валентинович'  | 'male'   | '1986-12-31' | 'Балахна'                                                  | 79087325844    | 2206              | 942136            | '2007-04-13'    | 'Отделом Внутренних Дел города Балахны Нижегородской области'                                                | '520-011'              | 'Балахна'                             | 'Герцена'                | '29'              | '35'             | '606400'           | 'Балахна'         | 'Герцена'                | '29'           | '35'          | '606400'        |  524407673243 |
| null                   | null                | 'site_reg_personal' | 'Галина'     | 'Логинычева' | 'Семеновна'     | 'female' | null         | null                                                       | 79040686621    | null              | null              | null            | null                                                                                                         | null                   | null                                  | null                     | null              | null             | null               | null              | null                     | null           | null          | null            |             0 |
| null                   | null                | 'ready'             | 'Юлия'       | 'Логинычева' | 'Александровна' | 'female' | '1986-07-05' | 'Горький'                                                  | 79506110508    | 2208              | 327130            | '2009-05-04'    | 'Отделением УФМС России по Нижегородской обл. в Балахнинском р-не'                                           | null                   | 'Балахна'                             | 'Герцена'                | '29'              | '35'             | '606400'           | 'Балахна'         | 'Герцена'                | '29'           | '35'          | '606400'        |  524411631567 |
| null                   | null                | 'ready'             | 'Александр'  | 'Федотов'    | 'Геннадьевич'   | 'male'   | '1989-08-19' | 'гор. Златоуст Челябинской обл.'                           | null           | null              | null              | '2009-08-31'    | 'отделом уфмс россии по челябинской области в городе златоусте'                                              | '740-014'              | 'Златоуст'                            | 'Карла Маркса'           | '24'              | '13'             | null               | 'Златоуст'        | 'Карла Маркса'           | '24'           | '13'          | null            |             0 |
```


## About final data
> - Total rows: 14809043

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
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
| names                               |   sex | address                                                                                                                | phones          | birth_date   | documents                                                                                                                                                                                                                                                                                                                                    |
|:------------------------------------|------:|:-----------------------------------------------------------------------------------------------------------------------|:----------------|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Сидорова Ольга Александровна']    |     0 | ['пос.Южно-Енисейск Красноярский край 663416 ул. Дачная д. 5 кв. 1', 'Минусинск 662610 ул. Ботаническая д. 51 кв. 26'] | ['79233736056'] | 23.09.1984   | [Row(type=1, serial='242600470570', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                  |
| ['Сидорова Мария Викторовна']       |     0 | ['Губкин ул. парковая д. 3 кв. 22', 'Москва ул. тамбовская д. 10 кв. 8']                                               | ['79067519129'] | 17.04.1984   | [Row(type=1, serial='582801503237', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                  |
| ['Ермолаева Светлана Ивановна']     |     0 | ['Губкин ул. ПАРКОВАЯ д. 3 кв. 22', 'Москва ул. ТАМБОВСКАЯ д. 10 кв. 8']                                               | ['79263690743'] | 05.12.1986   | [Row(type=1, serial='312707335923', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                  |
| ['Логинычев Андрей Валентинович']   |     1 | ['Балахна 606400 ул. Герцена д. 29 кв. 35']                                                                            | ['79087325844'] | 31.12.1986   | [Row(type=0, serial='2206942136', country='RUS', date_issue='13.04.2007', date_expire=None, authority='Отделом Внутренних Дел города Балахны Нижегородской области', authority_code='520-011'), Row(type=1, serial='524407673243', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                   |
| ['Логинычева Галина Семеновна']     |     0 |                                                                                                                        | ['79040686621'] |              |                                                                                                                                                                                                                                                                                                                                              |
| ['Логинычева Юлия Александровна']   |     0 | ['Балахна 606400 ул. Герцена д. 29 кв. 35']                                                                            | ['79506110508'] | 05.07.1986   | [Row(type=0, serial='2208327130', country='RUS', date_issue='04.05.2009', date_expire=None, authority='Отделением УФМС России по Нижегородской обл. в Балахнинском р-не', authority_code=None), Row(type=1, serial='524411631567', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                   |
| ['Насырова Елена Борисовна']        |     0 |                                                                                                                        | ['79517779098'] |              |                                                                                                                                                                                                                                                                                                                                              |
| ['Уколов Олег Анатольевич']         |     1 | ['Ульяновск ул. Аносова д. 7 кв. 51']                                                                                  | ['79634698586'] | 08.03.1976   | [Row(type=0, serial='7302543151', country='RUS', date_issue='03.07.2002', date_expire=None, authority='ОВД Железнодорожного района гор.Ульяновска', authority_code=None), Row(type=1, serial='732601566410', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                         |
| ['Быков Дмитрий Александрович']     |     1 | ['Балахна 606400 ул. Крестьянская д. 26']                                                                              | ['79101084823'] | 10.11.1984   | [Row(type=0, serial='2210694838', country='RUS', date_issue='28.04.2011', date_expire=None, authority='Отделением УФМС России по Нижегородской обл. в Балахнинском р-не', authority_code=None), Row(type=1, serial='524411262422', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                   |
| ['Колесникова Марина Владимировна'] |     0 | ['Челябинск 454010 ул. Гюго д. 2 кв. 72']                                                                              | ['79049302485'] | 15.09.1989   | [Row(type=0, serial='7512198951', country='RUS', date_issue='19.12.2012', date_expire=None, authority='Отделом УФМС России по Челябинской области в Ленинском районе гор. Челябинска', authority_code='740-054'), Row(type=1, serial='742702608905', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
```