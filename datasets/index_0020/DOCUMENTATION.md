# Parsetron results

## About row data

> - Code name: index_0020
> - File path: Sirena/sirena_rail_tickets.csv
> - Total rows: 9674578

### Schema
```
root
 |-- TICKET: integer (nullable = true)
 |-- PASS_DOC: string (nullable = true)
 |-- PASS_NAME: string (nullable = true)
 |-- SEAT_TIER: string (nullable = true)
 |-- SEAT: string (nullable = true)
 |-- TKT_DATE: timestamp (nullable = true)
 |-- CITIZENSHIP: string (nullable = true)
 |-- PHONE: string (nullable = true)
 |-- BIRTH_DATE: timestamp (nullable = true)
 |-- ARR_DATE: timestamp (nullable = true)
 |-- CLASS: string (nullable = true)
 |-- COACH_NUM: integer (nullable = true)
 |-- COACH_TYPE: string (nullable = true)
 |-- DEP_DATE: timestamp (nullable = true)
 |-- PORT_FROM: string (nullable = true)
 |-- PORT_TO: string (nullable = true)
 |-- TRAIN: string (nullable = true)

```

### Data sample
```
|    TICKET | PASS_DOC     | PASS_NAME           | SEAT_TIER   |   SEAT | TKT_DATE            | CITIZENSHIP   | PHONE   | BIRTH_DATE   | ARR_DATE            | CLASS   |   COACH_NUM | COACH_TYPE   | DEP_DATE            | PORT_FROM   | PORT_TO     | TRAIN   |
|----------:|:-------------|:--------------------|:------------|-------:|:--------------------|:--------------|:--------|:-------------|:--------------------|:--------|------------:|:-------------|:--------------------|:------------|:------------|:--------|
| 260421502 | ПС5708339755 | ПАНОВА АЛИНА        | НИЖНИЙ      |    007 | 2013-10-29 11:00:55 |               |         | NaT          | 2013-11-03 03:37:00 | 3П      |           1 | П            | 2013-11-02 22:14:00 | ПЕРМЬ 2     | ЕКАТЕРИНБ П | 068ЫА   |
| 260451077 | ПС5009615730 | ПЕКАРЕВ ОЛЕГ        | НИЖНИЙ      |    009 | 2013-10-29 14:00:16 |               |         | NaT          | 2013-11-13 03:55:00 | 1Л      |           7 | Л            | 2013-11-12 18:30:00 | ОМСК-ПАСС   | НОВОСИБ ГЛ  | 088НА   |
| 260477665 | СРIАК741816  | ДРУЖИНИНА МАРГАРИТА |             |    027 | 2013-10-29 17:15:21 |               |         | NaT          | 2013-11-03 18:40:00 | 2В      |           3 | С            | 2013-11-03 14:30:00 | С-ПЕТЕР-ГЛ  | МОСКВА ОКТ  | 167ВА   |
| 260521724 | ПС0808790679 | СТЕФАНОВИЧ АНТОН    |             |    016 | 2013-10-30 10:57:57 |               |         | NaT          | 2013-12-13 17:40:00 | 2С      |           6 | С            | 2013-12-13 13:30:00 | МОСКВА ОКТ  | С-ПЕТЕР-ГЛ  | 158АА   |
| 260522415 | ПС4007270390 | ЩЕГОЛЕВА ОЛЬГА      |             |    036 | 2013-10-30 11:02:44 |               |         | NaT          | 2013-11-10 17:40:00 | 2С      |           4 | С            | 2013-11-10 13:30:00 | С-ПЕТЕР-ГЛ  | МОСКВА ОКТ  | 157АА   |
| 260522457 | ПС9204993348 | ЗАКИРОВ АЛЬБЕРТ     | НИЖНИЙ      |    039 | 2013-10-30 11:02:56 |               |         | NaT          | 2013-10-31 10:08:00 | 3Э      |          15 | П            | 2013-10-30 21:32:00 | ВОССТАН П   | МОСКВА КАЗ  | 025ГА   |
| 260567118 | ПС4004728057 | ВОЛКОВ АЛЕКСАНДР    | НИЖНИЙ      |    010 | 2013-10-30 15:52:21 |               |         | NaT          | 2013-11-14 07:55:00 | 1У      |           9 | Л            | 2013-11-13 23:55:00 | С-ПЕТЕР-ГЛ  | МОСКВА ОКТ  | 001АА   |
| 260605934 | ПС3600299033 | АБРОСИМОВА НАДЕЖДА  | ВЕРХНИЙ     |    012 | 2013-10-31 09:14:50 |               |         | NaT          | 2013-11-02 11:01:00 | 2Э      |          11 | К            | 2013-11-01 20:40:00 | ОРСК        | САМАРА      | 131УА   |
| 260626330 | ПС4007435264 | АВДЕЕВА ОЛЬГА       | НИЖНИЙ      |    013 | 2013-10-31 11:44:19 |               |         | NaT          | 2013-11-08 08:16:00 | 1Б      |           3 | Л            | 2013-11-07 17:41:00 | МИНСК ПАСС  | С-ПЕТ-ВИТ   | 052БД   |
| 260632090 | ПС8101241967 | НИКОГОСЯН МЕЛИК     | НИЖНИЙ      |    003 | 2013-10-31 12:20:45 |               |         | NaT          | 2013-11-01 13:33:00 | 2Т      |          12 | К            | 2013-11-01 00:15:00 | МОСКВА КАЗ  | КАЗАНЬ ПАС  | 098ХА   |
```


## About final data
> - Total rows: 2008440

### Schema
```
root
 |-- names: array (nullable = false)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- documents: array (nullable = false)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- movements: array (nullable = false)
 |    |-- element: struct (containsNull = true)
 |    |    |-- from: struct (nullable = true)
 |    |    |    |-- datetime: string (nullable = true)
 |    |    |    |-- country: string (nullable = true)
 |    |    |    |-- city: string (nullable = true)
 |    |    |    |-- code: string (nullable = true)
 |    |    |-- to: struct (nullable = true)
 |    |    |    |-- datetime: string (nullable = true)
 |    |    |    |-- country: string (nullable = true)
 |    |    |    |-- city: string (nullable = true)
 |    |    |    |-- code: string (nullable = true)
 |    |    |-- code_type: string (nullable = true)
 |    |    |-- ticket_order_datetime: string (nullable = true)
 |    |    |-- seat: string (nullable = true)
 |    |    |-- ticket_number: string (nullable = true)
 |    |    |-- trip_number: string (nullable = true)
 |    |    |-- class: string (nullable = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- comment: string (nullable = true)

```

### Data sample
```
| names                                      | birth_date   | phones          | documents                                                                                                                | movements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-------------------------------------------|:-------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Парыгин Иван']                           |              |                 | [Row(type=4, serial='000000279', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='ОМСК-ПАССАЖИРСКИЙ'), to=Row(datetime=None, country=None, city=None, code='НОВОСИБИРСК-ГЛАВНЫЙ'), code_type='CODE', ticket_order_datetime=None, seat='011', ticket_number='487974255', trip_number='140СЦ', class='2К', type=4, comment=None), Row(from=Row(datetime=None, country=None, city=None, code='ОМСК-ПАССАЖИРСКИЙ'), to=Row(datetime=None, country=None, city=None, code='НОВОСИБИРСК-ГЛАВНЫЙ'), code_type='CODE', ticket_order_datetime=None, seat='011', ticket_number='488015684', trip_number='140СЦ', class='2К', type=4, comment=None)] |
| ['Чувальский Иван']                        |              |                 | [Row(type=4, serial='000000645', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='ХАБАРОВСК 1'), to=Row(datetime=None, country=None, city=None, code='СВОБОДНЫЙ'), code_type='CODE', ticket_order_datetime=None, seat='028', ticket_number='491543636', trip_number='325ЖЕ', class='3Л', type=4, comment=None), Row(from=Row(datetime=None, country=None, city=None, code='СВОБОДНЫЙ'), to=Row(datetime=None, country=None, city=None, code='ХАБАРОВСК 1'), code_type='CODE', ticket_order_datetime=None, seat='023', ticket_number='491555319', trip_number='326*ЭЦ', class='3Л', type=4, comment=None)]                                |
| ['Huynh Dacnhuquynh', 'Huynhdac Nhuquynh'] |              | ['79272323225'] | [Row(type=4, serial='000012166', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='МОСКВА КАЗАНСКАЯ'), to=Row(datetime=None, country=None, city=None, code='ЧЕБОКСАРЫ'), code_type='CODE', ticket_order_datetime=None, seat='096', ticket_number='685122450', trip_number='054ГА', class='1Э', type=4, comment=None), Row(from=Row(datetime=None, country=None, city=None, code='ТЮМЕНЬ'), to=Row(datetime=None, country=None, city=None, code='СУРГУТ'), code_type='CODE', ticket_order_datetime=None, seat='028', ticket_number='659916802', trip_number='108*ЖА', class='2Л', type=4, comment=None)]                                   |
| ['Дарвиш Раби']                            |              |                 | [Row(type=4, serial='000019176', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='МОСКВА КАЗАНСКАЯ'), to=Row(datetime=None, country=None, city=None, code='ПЕНЗА 1'), code_type='CODE', ticket_order_datetime=None, seat='020', ticket_number='607188946', trip_number='132УА', class='3Э', type=4, comment=None)]                                                                                                                                                                                                                                                                                                                       |
| ['Власьев Евгений']                        |              |                 | [Row(type=4, serial='0003128', country=None, date_issue=None, date_expire=None, authority=None, authority_code=None)]    | [Row(from=Row(datetime=None, country=None, city=None, code='ШЕКСНА'), to=Row(datetime=None, country=None, city=None, code='С-ПЕТ-ЛАД'), code_type='CODE', ticket_order_datetime=None, seat='030', ticket_number='307112947', trip_number='617ЯА', class='3Э', type=4, comment=None)]                                                                                                                                                                                                                                                                                                                               |
| ['Канивец Ольга']                          |              |                 | [Row(type=4, serial='000567273', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='МОСКВА КУРСКАЯ (КУРСКИЙ ВОКЗАЛ)'), to=Row(datetime=None, country=None, city=None, code='ТУЛА 1 КУРСКАЯ'), code_type='CODE', ticket_order_datetime=None, seat='090', ticket_number='500981571', trip_number='7047МА', class='3С', type=4, comment=None)]                                                                                                                                                                                                                                                                                                |
| ['Bova Oleksandr']                         |              |                 | [Row(type=4, serial='000807781', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='БЕЛГОРОД'), to=Row(datetime=None, country=None, city=None, code='МОСКВА КУРСКАЯ (КУРСКИЙ ВОКЗАЛ)'), code_type='CODE', ticket_order_datetime=None, seat='026', ticket_number='463410521', trip_number='072ВА', class='3Э', type=4, comment=None), Row(from=Row(datetime=None, country=None, city=None, code='НОВЫЙ УРЕНГОЙ'), to=Row(datetime=None, country=None, city=None, code='ПУРПЕ'), code_type='CODE', ticket_order_datetime=None, seat='005', ticket_number='463411014', trip_number='379УА', class='3Э', type=4, comment=None)]                |
| ['Synychych Viktoriia']                    |              |                 | [Row(type=4, serial='000854719', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='МОСКВА КИЕВСКАЯ'), to=Row(datetime=None, country=None, city=None, code='ЛЬВОВ'), code_type='CODE', ticket_order_datetime=None, seat='004', ticket_number='490363242', trip_number='073АА', class='3Д', type=4, comment=None)]                                                                                                                                                                                                                                                                                                                          |
| ['Карпа Нуцу']                             |              |                 | [Row(type=4, serial='001077061', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='САНКТ-ПЕТЕРБУРГ-ГЛАВН. (МОСКОВСКИЙ ВОКЗАЛ)'), to=Row(datetime=None, country=None, city=None, code='МОСКВА ОКТЯБРЬСКАЯ (ЛЕНИНГРАДСКИЙ ВОКЗАЛ)'), code_type='CODE', ticket_order_datetime=None, seat='013', ticket_number='405904569', trip_number='209АА', class='3Л', type=4, comment=None)]                                                                                                                                                                                                                                                           |
| ['Качмазова Сюзанна']                      |              |                 | [Row(type=4, serial='0013917', country=None, date_issue=None, date_expire=None, authority=None, authority_code=None)]    | [Row(from=Row(datetime=None, country=None, city=None, code='ЛАЗАРЕВСК'), to=Row(datetime=None, country=None, city=None, code='ВЛАДИКАВК'), code_type='CODE', ticket_order_datetime=None, seat='033', ticket_number='349931600', trip_number='680СА', class='3Л', type=4, comment=None)]                                                                                                                                                                                                                                                                                                                            |
```
