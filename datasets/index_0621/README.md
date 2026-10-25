# Parsetron results

## About row data

> - Code name: index_0621
> - File path: ree_md.csv
> - Total rows: 30304

### Schema
```
root
 |-- id: string (nullable = true)
 |-- code: string (nullable = true)
 |-- fam: string (nullable = true)
 |-- im: string (nullable = true)
 |-- ot: string (nullable = true)
 |-- w: integer (nullable = true)
 |-- dr: date (nullable = true)
 |-- ds: string (nullable = true)
 |-- date_add: integer (nullable = true)
 |-- date_delete: integer (nullable = true)
 |-- is_deleted: integer (nullable = true)

```

### Data sample
```
|   id | code        | fam         | im       | ot            |   w | dr         | ds   |   date_add |   date_delete |   is_deleted |
|-----:|:------------|:------------|:---------|:--------------|----:|:-----------|:-----|-----------:|--------------:|-------------:|
|   98 | 133-577-471 | Аветисян    | Гамлет   | Дереникович   |   1 | 1981-09-28 |      | 1364760000 |             0 |            0 |
|   99 | 146-146-089 | Агалиева    | Нодира   | Заимовна      |   2 | 1981-10-20 |      | 1364760000 |             0 |            0 |
|  100 | 031-272-667 | Агафонов    | Андрей   | Николаевич    |   1 | 1972-07-09 |      | 1364760000 |             0 |            0 |
|  101 | 158-597-126 | Акинчикова  | Юлия     | Витальевна    |   2 | 1986-07-01 |      | 1364760000 |             0 |            0 |
|  102 | 031-272-739 | Андреева    | Татьяна  | Ивановна      |   2 | 1953-01-23 |      | 1364760000 |             0 |            0 |
|  103 | 036-540-699 | Андреева    | Татьяна  | Матвеевна     |   2 | 1959-04-30 |      | 1364760000 |             0 |            0 |
|  104 | 031-272-664 | Аненкова    | Наталья  | Сергеевна     |   2 | 1959-05-26 |      | 1364760000 |             0 |            0 |
|  105 | 031-272-671 | Антипова    | Елена    | Николаевна    |   2 | 1955-10-05 |      | 1364760000 |             0 |            0 |
|  106 | 031-086-145 | Аристовская | Светлана | Геннадьевна   |   2 | 1966-09-16 |      | 1364760000 |             0 |            0 |
|  107 | 031-447-716 | Артамонова  | Нинель   | Михайловна    |   2 | 1967-04-17 |      | 1364760000 |             0 |            0 |
|  108 | 039-657-706 | Архипенкова | Галина   | Викторовна    |   2 | 1959-03-30 |      | 1364760000 |             0 |            0 |
|  109 | 042-142-638 | Аснин       | Ефим     | Семенович     |   1 | 1948-06-30 |      | 1364760000 |             0 |            0 |
|  110 | 031-272-740 | Бакулина    | Тамара   | Михайловна    |   2 | 1962-01-25 |      | 1364760000 |             0 |            0 |
|  111 | 031-447-707 | Балобин     | Алексей  | Алексеевич    |   1 | 1959-09-11 |      | 1364760000 |             0 |            0 |
|  112 | 031-272-672 | Бардаш      | Галина   | Александровна |   2 | 1953-08-11 |      | 1364760000 |             0 |            0 |
|  113 | 152-586-747 | Бахова      | Юлия     | Владимировна  |   2 | 1987-05-07 |      | 1364760000 |             0 |            0 |
|  114 | 031-810-257 | Белова      | Татьяна  | Федоровна     |   2 | 1957-05-03 |      | 1364760000 |             0 |            0 |
|  115 | 063-375-219 | Бернасеева  | Елена    | Михайловна    |   2 | 1979-07-30 |      | 1364760000 |             0 |            0 |
|  116 | 063-370-572 | Бирюлина    | Татьяна  | Николаевна    |   2 | 1978-08-04 |      | 1364760000 |             0 |            0 |
|  117 | 031-810-277 | Бобылева    | Татьяна  | Ивановна      |   2 | 1962-12-17 |      | 1364760000 |             0 |            0 |
```

> - Code name: index_0621
> - File path: ree_md_s.csv
> - Total rows: 80722

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- code: string (nullable = true)
 |-- code_s: integer (nullable = true)
 |-- name_s: string (nullable = true)
 |-- beg_s: date (nullable = true)
 |-- end_s: date (nullable = true)
 |-- date_add: integer (nullable = true)
 |-- date_delete: integer (nullable = true)
 |-- is_deleted: integer (nullable = true)

```

### Data sample
```
|   id | code        |   code_s | name_s                          | beg_s      | end_s      |   date_add |   date_delete |   is_deleted |
|-----:|:------------|---------:|:--------------------------------|:-----------|:-----------|-----------:|--------------:|-------------:|
|  124 | 006-464-892 |   112212 | Функциональная диагностика      | 2013-02-16 | 2018-02-16 | 1364760000 |             0 |            0 |
|  125 | 017-441-767 |     1126 | Хирургия                        | 2008-03-05 | 2013-03-05 | 1364760000 |             0 |            0 |
|  126 | 028-821-573 |     2002 | Лечебное дело                   | 2009-11-06 | 2014-11-06 | 1364760000 |             0 |            0 |
|  127 | 029-830-076 |     2015 | Сестринское дело                | 2010-02-12 | 2015-02-12 | 1364760000 |             0 |            0 |
|  128 | 030-653-814 |     2020 | Рентгенология                   | 2009-12-29 | 2014-12-29 | 1364760000 |             0 |            0 |
|  129 | 030-654-231 |     2015 | Сестринское дело                | 2011-02-10 | 2016-02-10 | 1364760000 |             0 |            0 |
|  130 | 030-654-342 |   112609 | Эндоскопия                      | 2012-04-11 | 2017-04-11 | 1364760000 |             0 |            0 |
|  131 | 030-656-478 |     2015 | Сестринское дело                | 2012-12-07 | 2017-12-07 | 1364760000 |             0 |            0 |
|  132 | 030-656-519 |     2020 | Рентгенология                   | 2009-11-11 | 2014-11-11 | 1364760000 |             0 |            0 |
|  133 | 030-656-879 |     2015 | Сестринское дело                | 2009-04-16 | 2014-04-16 | 1364760000 |             0 |            0 |
|  134 | 030-657-051 |     2015 | Сестринское дело                | 2011-04-14 | 2016-04-14 | 1364760000 |             0 |            0 |
|  135 | 030-657-787 |   112221 | Эндоскопия                      | 2010-06-25 | 2015-06-25 | 1364760000 |             0 |            0 |
|  136 | 030-657-912 |     2015 | Сестринское дело                | 2010-03-18 | 2015-03-18 | 1364760000 |             0 |            0 |
|  137 | 030-661-732 |     1106 | Инфекционные болезни            | 2009-03-21 | 2014-03-21 | 1364760000 |             0 |            0 |
|  138 | 031-086-145 |     1103 | Анестезиология и реаниматология | 2011-03-28 | 2016-03-28 | 1364760000 |             0 |            0 |
|  139 | 031-272-664 |   112211 | Ультразвуковая диагностика      | 2011-03-14 | 2016-03-14 | 1364760000 |             0 |            0 |
|  140 | 031-272-667 |     1122 | Терапия                         | 2011-05-31 | 2016-05-31 | 1364760000 |             0 |            0 |
|  141 | 031-272-671 |   112219 | Рефлексотерапия                 | 2010-05-20 | 2015-05-20 | 1364760000 |             0 |            0 |
|  142 | 031-272-671 |   112220 | Физиотерапия                    | 2010-03-15 | 2015-03-15 | 1364760000 |             0 |            0 |
|  143 | 031-272-672 |   112205 | Кардиология                     | 2012-03-05 | 2017-03-05 | 1364760000 |             0 |            0 |
```


## About final data
> - Total rows: 15199

### Schema
```
root
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Documents | 100.00% |
| Sex | 99.98% |
| Birth_date | 99.92% |
| Names | 100.00% |
| Works | 99.01% |



### Data sample
```
| documents                                                                                                                  |   sex | birth_date   | names                                                     | works                                                                                                                                                                                                                                                   |
|:---------------------------------------------------------------------------------------------------------------------------|------:|:-------------|:----------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Row(type=2, serial='01397657373', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 19.12.1958   | ['Абузярова София Хасановна']                             | [Row(post='Педиатрия', date_start='19.04.2010', date_end='19.04.2015', company=None, address=None, comment=None)]                                                                                                                                       |
| [Row(type=2, serial='02339561140', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     1 | 11.07.1955   | ['Терещенко Александр Владимирович']                      | [Row(post='Офтальмология', date_start='21.11.2015', date_end='21.11.2020', company=None, address=None, comment=None)]                                                                                                                                   |
| [Row(type=2, serial='02882178171', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 04.05.1965   | ['Родина Наталья Романовна']                              | [Row(post='Педиатрия', date_start='19.04.2010', date_end='22.04.2020', company=None, address=None, comment=None)]                                                                                                                                       |
| [Row(type=2, serial='02946435572', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 19.10.1972   | ['Андреенкова Татьяна Владимировна']                      | [Row(post='Сестринское дело', date_start='07.10.2011', date_end='12.10.2021', company=None, address=None, comment=None)]                                                                                                                                |
| [Row(type=2, serial='02995919922', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 07.04.1938   | ['Дейтер Нина Ивановна']                                  | [Row(post='Офтальмология', date_start='03.12.2011', date_end='23.11.2020', company=None, address=None, comment=None)]                                                                                                                                   |
| [Row(type=2, serial='02996096101', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 09.01.1942   | ['Клюева Нина Федоровна']                                 | [Row(post='Отоларингология', date_start='06.12.2008', date_end='02.12.2018', company=None, address=None, comment=None)]                                                                                                                                 |
| [Row(type=2, serial='03065649846', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 28.03.1972   | ['Сидоренко Елена Александровна']                         | [Row(post='Операционное дело', date_start='23.05.2011', date_end='26.05.2021', company=None, address=None, comment=None)]                                                                                                                               |
| [Row(type=2, serial='03065705325', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 17.07.1958   | ['Москалева Ирина Яковлевна']                             | [Row(post='Сестринское дело', date_start='15.04.2010', date_end='20.02.2020', company=None, address=None, comment=None)]                                                                                                                                |
| [Row(type=2, serial='03065707127', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 15.06.1971   | ['Москалева Татьяна Николаевна']                          | [Row(post='Операционное дело', date_start='11.06.2010', date_end='22.05.2020', company=None, address=None, comment=None)]                                                                                                                               |
| [Row(type=2, serial='03066146017', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 27.09.1958   | ['Минченкова Валентина Олеговна']                         | [Row(post='Сестринское дело', date_start='26.06.2008', date_end='26.06.2018', company=None, address=None, comment=None)]                                                                                                                                |
| [Row(type=2, serial='03066159228', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 01.11.1969   | ['Шамплетова Ирина Владимировна']                         | [Row(post='Сестринское дело', date_start='25.09.2009', date_end='16.10.2019', company=None, address=None, comment=None)]                                                                                                                                |
| [Row(type=2, serial='03108593023', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 02.02.1948   | ['Артеменкова Галина Николаевна']                         | [Row(post='Стоматология детская', date_start='19.10.2011', date_end='12.02.2018', company=None, address=None, comment=None)]                                                                                                                            |
| [Row(type=2, serial='03127278931', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 23.09.1948   | ['Сурикова Светлана Михайловна']                          | [Row(post='Физиотерапия', date_start='01.04.2011', date_end='01.04.2016', company=None, address=None, comment=None)]                                                                                                                                    |
| [Row(type=2, serial='03145532113', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     1 | 24.05.1972   | ['Мартынов Борис Иванович']                               | [Row(post='Нефрология', date_start='06.05.2009', date_end='23.05.2019', company=None, address=None, comment=None)]                                                                                                                                      |
| [Row(type=2, serial='03145544827', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 31.07.1964   | ['Соловьева Елена Ивановна', 'Фроленкова Елена Ивановна'] | [Row(post='Скорая и неотложная помощь', date_start='21.03.2014', date_end='21.03.2019', company=None, address=None, comment=None), Row(post='Лечебное дело', date_start='27.03.2009', date_end='27.03.2014', company=None, address=None, comment=None)] |
| [Row(type=2, serial='03176841452', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 01.01.1956   | ['Савченкова Валентина Григорьевна']                      | [Row(post='Сестринское дело', date_start='16.02.2007', date_end='23.12.2021', company=None, address=None, comment=None)]                                                                                                                                |
| [Row(type=2, serial='03346054021', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 03.05.1963   | ['Стецюк Зоя Евгеньевна']                                 | [Row(post='Акушерское дело', date_start='27.03.2008', date_end='07.06.2018', company=None, address=None, comment=None)]                                                                                                                                 |
| [Row(type=2, serial='03548255459', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 11.09.1963   | ['Чернина Оксана Орестовна']                              | [Row(post='Сестринское дело', date_start='15.05.2014', date_end='15.05.2019', company=None, address=None, comment=None), Row(post='Операционное дело', date_start='23.03.2006', date_end='24.05.2016', company=None, address=None, comment=None)]       |
| [Row(type=2, serial='03548273663', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     0 | 10.07.1951   | ['Кожухова Галина Ришардовна']                            | [Row(post='Общая практика', date_start='28.03.2012', date_end='28.03.2017', company=None, address=None, comment=None)]                                                                                                                                  |
| [Row(type=2, serial='03623475544', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |     1 | 17.03.1967   | ['Тризно Елена Васильевна']                               | [Row(post='Операционное дело', date_start='04.04.2008', date_end='04.04.2013', company=None, address=None, comment=None)]                                                                                                                               |
```