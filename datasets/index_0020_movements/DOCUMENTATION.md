# Parsetron results

## About row data

> - File path: sirena_rail_tickets.csv
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
|    TICKET | PASS_DOC     | PASS_NAME           | SEAT_TIER   |   SEAT | TKT_DATE            | CITIZENSHIP   | PHONE   | BIRTH_DATE   | ARR_DATE            | CLASS   |   COACH_NUM | COACH_TYPE   | DEP_DATE            | PORT_FROM   | PORT_TO      | TRAIN   |
|----------:|:-------------|:--------------------|:------------|-------:|:--------------------|:--------------|:--------|:-------------|:--------------------|:--------|------------:|:-------------|:--------------------|:------------|:-------------|:--------|
| 260421502 | ПС5708339755 | ПАНОВА АЛИНА        | НИЖНИЙ      |    007 | 2013-10-29 11:00:55 |               |         | NaT          | 2013-11-03 05:37:00 | 3П      |           1 | П            | 2013-11-03 00:14:00 | ПЕРМЬ 2     | ЕКАТЕРИНБ П  | 068ЫА   |
| 260451077 | ПС5009615730 | ПЕКАРЕВ ОЛЕГ        | НИЖНИЙ      |    009 | 2013-10-29 14:00:16 |               |         | NaT          | 2013-11-13 05:55:00 | 1Л      |           7 | Л            | 2013-11-12 20:30:00 | ОМСК-ПАСС   | НОВОСИБ ГЛ   | 088НА   |
| 260477665 | СРIАК741816  | ДРУЖИНИНА МАРГАРИТА |             |    027 | 2013-10-29 17:15:21 |               |         | NaT          | 2013-11-03 20:40:00 | 2В      |           3 | С            | 2013-11-03 16:30:00 | С-ПЕТЕР-ГЛ  | МОСКВА ОКТ   | 167ВА   |
| 260521724 | ПС0808790679 | СТЕФАНОВИЧ АНТОН    |             |    016 | 2013-10-30 10:57:57 |               |         | NaT          | 2013-12-13 19:40:00 | 2С      |           6 | С            | 2013-12-13 15:30:00 | МОСКВА ОКТ  | С-ПЕТЕР-ГЛ   | 158АА   |
| 260522415 | ПС4007270390 | ЩЕГОЛЕВА ОЛЬГА      |             |    036 | 2013-10-30 11:02:44 |               |         | NaT          | 2013-11-10 19:40:00 | 2С      |           4 | С            | 2013-11-10 15:30:00 | С-ПЕТЕР-ГЛ  | МОСКВА ОКТ   | 157АА   |
| 260522457 | ПС9204993348 | ЗАКИРОВ АЛЬБЕРТ     | НИЖНИЙ      |    039 | 2013-10-30 11:02:56 |               |         | NaT          | 2013-10-31 12:08:00 | 3Э      |          15 | П            | 2013-10-30 23:32:00 | ВОССТАН П   | МОСКВА КАЗ   | 025ГА   |
| 260567118 | ПС4004728057 | ВОЛКОВ АЛЕКСАНДР    | НИЖНИЙ      |    010 | 2013-10-30 15:52:21 |               |         | NaT          | 2013-11-14 09:55:00 | 1У      |           9 | Л            | 2013-11-14 01:55:00 | С-ПЕТЕР-ГЛ  | МОСКВА ОКТ   | 001АА   |
| 260605934 | ПС3600299033 | АБРОСИМОВА НАДЕЖДА  | ВЕРХНИЙ     |    012 | 2013-10-31 09:14:50 |               |         | NaT          | 2013-11-02 13:01:00 | 2Э      |          11 | К            | 2013-11-01 22:40:00 | ОРСК        | САМАРА       | 131УА   |
| 260626330 | ПС4007435264 | АВДЕЕВА ОЛЬГА       | НИЖНИЙ      |    013 | 2013-10-31 11:44:19 |               |         | NaT          | 2013-11-08 10:16:00 | 1Б      |           3 | Л            | 2013-11-07 19:41:00 | МИНСК ПАСС  | С-ПЕТ-ВИТ    | 052БД   |
| 260632090 | ПС8101241967 | НИКОГОСЯН МЕЛИК     | НИЖНИЙ      |    003 | 2013-10-31 12:20:45 |               |         | NaT          | 2013-11-01 15:33:00 | 2Т      |          12 | К            | 2013-11-01 02:15:00 | МОСКВА КАЗ  | КАЗАНЬ ПАС   | 098ХА   |
| 260656018 | PSP730631043 | KURT KHAVVA         |             |        | 2013-10-31 15:10:35 |               |         | NaT          | 2013-11-02 06:20:00 | 2К      |           1 | К            | 2013-11-02 00:55:00 | МОСКВА КУР  | Н.НОВГОРОД М | 460*АА  |
| 260663972 | ZAU01506633  | TURER TEVFIKOZGUR   |             |    006 | 2013-10-31 16:09:27 |               |         | NaT          | 2013-11-07 01:25:00 | 2С      |           6 | С            | 2013-11-06 21:30:00 | МОСКВА КУР  | Н.НОВГОРОД М | 174НА   |
| 260677221 | ПС4004478802 | СИЛАЕВА СВЕТЛАНА    | НИЖНИЙ      |    015 | 2013-10-31 17:50:02 |               |         | NaT          | 2013-12-01 09:55:00 | 2Т      |           3 | К            | 2013-12-01 01:55:00 | С-ПЕТЕР-ГЛ  | МОСКВА ОКТ   | 001АА   |
| 260677390 | СРIIАК806672 | ФОМИН ДАНИИЛ        |             |    024 | 2013-10-31 17:53:02 |               |         | NaT          | 2013-11-09 12:50:00 | 2С      |           7 | С            | 2013-11-09 10:02:00 | ТВЕРЬ       | С-ПЕТЕР-ГЛ   | 154АА   |
| 260678174 | ПС2802942613 | ФОМИН АНАТОЛИЙ      |             |    023 | 2013-10-31 18:04:57 |               |         | NaT          | 2013-11-09 12:50:00 | 2С      |           7 | С            | 2013-11-09 10:02:00 | ТВЕРЬ       | С-ПЕТЕР-ГЛ   | 154АА   |
| 260714741 | ПС7605105551 | КУЗНЕЦОВ АНДРЕЙ     | НИЖНИЙ      |    021 | 2013-11-01 10:33:56 |               |         | NaT          | 2013-11-24 04:42:00 | 2К      |           7 | К            | 2013-11-23 14:43:00 | ЧИТА 2      | КРАСНОКАМ    | 602ЧЦ   |
| 260743228 | ПС4010073159 | ЗАЙЦЕВ АНДРЕЙ       |             |    028 | 2013-11-01 13:26:00 |               |         | NaT          | 2013-12-09 01:25:00 | 2С      |           4 | С            | 2013-12-08 21:45:00 | С-ПЕТЕР-ГЛ  | МОСКВА ОКТ   | 165АА   |
| 260747135 | ПС4011410610 | ФЕДОРОВА НАТАЛЬЯ    |             |    008 | 2013-11-01 13:49:53 |               |         | NaT          | 2013-12-14 01:25:00 | 2С      |           4 | С            | 2013-12-13 21:45:00 | МОСКВА ОКТ  | С-ПЕТЕР-ГЛ   | 166АА   |
| 260757347 | ПС4012729600 | ВАГАНОВА КРИСТИНА   | НИЖНИЙ      |    018 | 2013-11-01 14:58:04 |               |         | NaT          | 2013-11-05 11:00:00 | 1Б      |           6 | Л            | 2013-11-05 02:20:00 | С-ПЕТЕР-ГЛ  | МОСКВА ОКТ   | 019УА   |
| 260763413 | ПС1201238063 | УРАЗАЛИЕВ РИЗУАН    | НИЖНИЙ      |    007 | 2013-11-01 15:31:53 |               |         | NaT          | 2013-11-03 21:10:00 | 3Э      |           8 | П            | 2013-11-02 16:45:00 | АСТРАХАНЬ1  | МОСКВА ПАВ   | 005ЖА   |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- movements: array (nullable = true)
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
| names                      | birth_date   | phones   | documents                                                                                                                 | movements                                                                                                                                                                                                                                                                                                                                  |
|:---------------------------|:-------------|:---------|:--------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Boltaev Erkin']          |              |          | [Row(type=4, serial='AA1598982', country=None, date_issue=None, date_expire=None, authority=None, authority_code=None)]   | [Row(from=Row(datetime='29.10.2013 22:08:00', country=None, city=None, code='ПЕТРОЗАВОД'), to=Row(datetime='30.10.2013 11:06:00', country=None, city=None, code='МОСКВА ОКТ'), code_type='CODE', ticket_order_datetime='28.10.2013 18:34', seat='022', ticket_number='260383321', trip_number='017АА', class='3Э', type=4, comment=None)]  |
| ['Катаев Михаил']          |              |          | [Row(type=0, serial='4605031667', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='07.11.2013 18:52:00', country=None, city=None, code='ВЛАДИМИР П'), to=Row(datetime='07.11.2013 20:40:00', country=None, city=None, code='МОСКВА КУР'), code_type='CODE', ticket_order_datetime='29.10.2013 09:28', seat='011', ticket_number='260407715', trip_number='173НА', class='2С', type=4, comment=None)]  |
| ['Щепила Александр']       |              |          | [Row(type=0, serial='1103970833', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='03.11.2013 19:34:00', country=None, city=None, code='ВОРКУТА'), to=Row(datetime='04.11.2013 23:51:00', country=None, city=None, code='КОНОША 1'), code_type='CODE', ticket_order_datetime='29.10.2013 10:28', seat='018', ticket_number='260415933', trip_number='041МА', class='2Л', type=4, comment=None)]       |
| ['Сажин Виктор']           |              |          | [Row(type=0, serial='4511042935', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='06.11.2013 08:45:00', country=None, city=None, code='МОСКВА ОКТ'), to=Row(datetime='06.11.2013 12:25:00', country=None, city=None, code='С-ПЕТЕР-ГЛ'), code_type='CODE', ticket_order_datetime='29.10.2013 11:23', seat='033', ticket_number='260425392', trip_number='152АА', class='2С', type=4, comment=None)]  |
| ['Захаров Евгений']        |              |          | [Row(type=0, serial='6399095672', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='03.11.2013 13:14:00', country=None, city=None, code='ЛАБЫТНАНГИ'), to=Row(datetime='03.11.2013 20:11:00', country=None, city=None, code='СЕЙДА'), code_type='CODE', ticket_order_datetime='29.10.2013 16:07', seat='031', ticket_number='260470173', trip_number='653ВА', class='2К', type=4, comment=None)]       |
| ['Дружинин Егор']          |              |          | [Row(type=5, serial='IIАК674687', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='03.11.2013 16:30:00', country=None, city=None, code='С-ПЕТЕР-ГЛ'), to=Row(datetime='03.11.2013 20:40:00', country=None, city=None, code='МОСКВА ОКТ'), code_type='CODE', ticket_order_datetime='29.10.2013 17:15', seat='028', ticket_number='260477666', trip_number='167ВА', class='2В', type=4, comment=None)]  |
| ['Бобоев Собир']           |              |          | [Row(type=4, serial='СР1420275', country=None, date_issue=None, date_expire=None, authority=None, authority_code=None)]   | [Row(from=Row(datetime='21.11.2013 16:23:00', country=None, city=None, code='УЛАН УДЭ П'), to=Row(datetime='22.11.2013 18:09:00', country=None, city=None, code='КРАСНОЯР П'), code_type='CODE', ticket_order_datetime='31.10.2013 11:04', seat='036', ticket_number='260620780', trip_number='099ЭА', class='3П', type=4, comment=None)]  |
| ['Коляда Анатолий']        |              |          | [Row(type=0, serial='0309385312', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='24.11.2013 18:10:00', country=None, city=None, code='РУБЦОВСК'), to=Row(datetime='25.11.2013 04:33:00', country=None, city=None, code='НОВОСИБ ГЛ'), code_type='CODE', ticket_order_datetime='31.10.2013 11:19', seat='003', ticket_number='260622758', trip_number='326НП', class='3П', type=4, comment=None)]    |
| ['Волков Александр']       |              |          | [Row(type=0, serial='4004728057', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='16.11.2013 01:55:00', country=None, city=None, code='МОСКВА ОКТ'), to=Row(datetime='16.11.2013 09:55:00', country=None, city=None, code='С-ПЕТЕР-ГЛ'), code_type='CODE', ticket_order_datetime='31.10.2013 11:30', seat='006', ticket_number='260624248', trip_number='002АА', class='1У', type=4, comment=None)]  |
| ['Калашников Евгений']     |              |          | [Row(type=0, serial='3406806418', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='02.11.2013 01:20:00', country=None, city=None, code='МОСКВА ЯР'), to=Row(datetime='02.11.2013 07:35:00', country=None, city=None, code='КОСТРОМА Н'), code_type='CODE', ticket_order_datetime='31.10.2013 11:40', seat='021', ticket_number='260625612', trip_number='148ЯА', class='3П', type=4, comment=None)]   |
| ['Порхун Мария']           |              |          | [Row(type=0, serial='7610543029', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='18.11.2013 14:46:00', country=None, city=None, code='КРАСНОКАМ'), to=Row(datetime='19.11.2013 04:40:00', country=None, city=None, code='ЧИТА 2'), code_type='CODE', ticket_order_datetime='31.10.2013 11:41', seat='020', ticket_number='260625763', trip_number='681ЧБ', class='2К', type=4, comment=None)]       |
| ['Никогосян Мелик']        |              |          | [Row(type=0, serial='8101241967', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='01.11.2013 02:15:00', country=None, city=None, code='МОСКВА КАЗ'), to=Row(datetime='01.11.2013 15:33:00', country=None, city=None, code='КАЗАНЬ ПАС'), code_type='CODE', ticket_order_datetime='31.10.2013 12:20', seat='003', ticket_number='260632090', trip_number='098ХА', class='2Т', type=4, comment=None)]  |
| ['Тарбаев Олег']           |              |          | [Row(type=0, serial='1104121423', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='02.11.2013 12:05:00', country=None, city=None, code='МОСКВА ЯР'), to=Row(datetime='03.11.2013 08:32:00', country=None, city=None, code='АРХАНГЕЛ Г'), code_type='CODE', ticket_order_datetime='31.10.2013 12:40', seat='008', ticket_number='260635730', trip_number='016ЯА', class='3П', type=4, comment=None)]   |
| ['Филицианский Александр'] |              |          | [Row(type=0, serial='1109731149', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='02.11.2013 12:05:00', country=None, city=None, code='МОСКВА ЯР'), to=Row(datetime='03.11.2013 08:32:00', country=None, city=None, code='АРХАНГЕЛ Г'), code_type='CODE', ticket_order_datetime='31.10.2013 14:42', seat='004', ticket_number='260652565', trip_number='016ЯА', class='3П', type=4, comment=None)]   |
| ['Глухов Евгений']         |              |          | [Row(type=0, serial='4102985877', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='07.11.2013 18:30:00', country=None, city=None, code='МОСКВА ОКТ'), to=Row(datetime='07.11.2013 22:25:00', country=None, city=None, code='С-ПЕТЕР-ГЛ'), code_type='CODE', ticket_order_datetime='31.10.2013 14:51', seat='043', ticket_number='260653559', trip_number='162АА', class='2С', type=4, comment=None)]  |
| ['Олегаш Василий']         |              |          | [Row(type=4, serial='BO146114', country=None, date_issue=None, date_expire=None, authority=None, authority_code=None)]    | [Row(from=Row(datetime='02.11.2013 01:10:00', country=None, city=None, code='МОСКВА ОКТ'), to=Row(datetime='02.11.2013 12:13:00', country=None, city=None, code='С-ПЕТЕР-ГЛ'), code_type='CODE', ticket_order_datetime='31.10.2013 15:36', seat='033', ticket_number='260659451', trip_number='810ЧА', class='1С', type=4, comment=None)]  |
| ['Цуканов Артем']          |              |          | [Row(type=0, serial='7507211518', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='05.11.2013 02:20:00', country=None, city=None, code='С-ПЕТЕР-ГЛ'), to=Row(datetime='05.11.2013 11:00:00', country=None, city=None, code='МОСКВА ОКТ'), code_type='CODE', ticket_order_datetime='31.10.2013 16:11', seat='011', ticket_number='260664262', trip_number='019УА', class='1Б', type=4, comment=None)]  |
| ['Блехан Игорь']           |              |          | [Row(type=0, serial='2013614896', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='02.12.2013 01:55:00', country=None, city=None, code='С-ПЕТЕР-ГЛ'), to=Row(datetime='02.12.2013 09:55:00', country=None, city=None, code='МОСКВА ОКТ'), code_type='CODE', ticket_order_datetime='31.10.2013 18:11', seat='009', ticket_number='260678635', trip_number='001АА', class='2Т', type=4, comment=None)]  |
| ['Kaptanoglu Mustafamert'] |              |          | [Row(type=4, serial='730021846', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]  | [Row(from=Row(datetime='07.11.2013 01:09:00', country=None, city=None, code='Н.НОВГОРОД М'), to=Row(datetime='07.11.2013 07:52:00', country=None, city=None, code='МОСКВА ЯР'), code_type='CODE', ticket_order_datetime='01.11.2013 10:52', seat='002', ticket_number='260717934', trip_number='001МА', class='3Э', type=4, comment=None)] |
| ['Вельможин Олег']         |              |          | [Row(type=0, serial='5708342407', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='05.11.2013 03:17:00', country=None, city=None, code='КРАСНОДАР1'), to=Row(datetime='07.11.2013 11:15:00', country=None, city=None, code='ПЕРМЬ 2'), code_type='CODE', ticket_order_datetime='01.11.2013 14:35', seat='022', ticket_number='260753947', trip_number='354СБ', class='3П', type=4, comment=None)]     |
```