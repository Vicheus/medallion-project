# Parsetron results

## About row data

> - Code name: index_0054_movements
> - File path: doc_serial_to_ignore.csv
> - Total rows: 11206

### Schema
```
root
 |-- serial: string (nullable = true)

```

### Data sample
```
|     serial |
|-----------:|
|  301448850 |
|  503456789 |
|  705744073 |
|  712345678 |
|   11111111 |
| 1203691644 |
| 1213123456 |
| 1512123456 |
|         21 |
|  221234567 |
| 2603123654 |
| 3003123456 |
| 4004861708 |
| 4504339917 |
| 4505120422 |
| 4505188684 |
| 4506867752 |
| 4507465085 |
| 4508203976 |
| 4508333133 |
```

> - Code name: index_0054_movements
> - File path: *.json
> - Total rows: 637597280

### Schema
```
root
 |-- _corrupt_record: string (nullable = true)
 |-- _id: string (nullable = true)
 |-- _index: string (nullable = true)
 |-- _score: long (nullable = true)
 |-- _source: struct (nullable = true)
 |    |-- airline_code: string (nullable = true)
 |    |-- airline_name: string (nullable = true)
 |    |-- arrival_point: string (nullable = true)
 |    |-- booking_date: string (nullable = true)
 |    |-- departure_point: string (nullable = true)
 |    |-- full_name: string (nullable = true)
 |    |-- passport: string (nullable = true)
 |    |-- ticket_issuer: string (nullable = true)

```

### Data sample
```
| _corrupt_record   | _id                  | _index                    |   _score | _source                                                                                                                                                                                                                                                                                                         |
|:------------------|:---------------------|:--------------------------|---------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   | YycnJo0BdMMFZS6WrzY_ | ru-persons-sirena-tickets |        1 | Row(airline_code='733', airline_name='JSC AEROFLOT DON', arrival_point='AER', booking_date='2007-06-10T08:46:13.000Z', departure_point='NUX', full_name='LOZOVAYA/ZINAIDA MS 23NOV48', passport='PS7403436404', ticket_issuer='02НУР ТКП          НОВОУРЕНГОЙСКОЕ АВСНОВЫЙ УРЕНГОЙ РФ   00507113     0011')     |
|                   | ZicnJo0BdMMFZS6WrzY_ | ru-persons-sirena-tickets |        1 | Row(airline_code='733', airline_name='JSC AEROFLOT DON', arrival_point='ROV', booking_date='2007-06-08T15:33:32.000Z', departure_point='MOW', full_name='NAPRASNIKOVA/MARINA MS', passport='PS6099177004', ticket_issuer='Д9306056           ТРЕВЕЛ СИТИ-АВИА   РОСТОВ             0254')                       |
|                   | aCcnJo0BdMMFZS6WrzY_ | ru-persons-sirena-tickets |        1 | Row(airline_code='664', airline_name='ЯМАЛ', arrival_point='УФА', booking_date='2007-06-08T15:33:32.000Z', departure_point='НДМ', full_name='ЧЕРЕСОВА/ЮЛИЯ Ь Г-ЖА', passport='ПС8002625191', ticket_issuer='02СХД 08 ИЮН 07    ООО"АВИАСПЕЦТЕХНОЛОНАДЫМ РФ           ЛА502596     0054')                        |
|                   | aycnJo0BdMMFZS6WrzY_ | ru-persons-sirena-tickets |        1 | Row(airline_code='298', airline_name='ОАО АВИАКОМПАНИЯ ЮТЭЙР', arrival_point='НОЯ', booking_date='2007-06-08T15:33:32.000Z', departure_point='МОВ', full_name='БАКАН/ВАЛЕНТИНА Г-ЖА', passport='ПС7402322429', ticket_issuer='46МОС ТКП          "ТА ВНУКОВО"       МОСКВА РФ          92317282     1037')      |
|                   | XycnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='195', airline_name='ГТК РОССИЯ', arrival_point='МОВ', booking_date='2007-06-09T10:59:34.000Z', departure_point='СПТ', full_name='ПАРСАДАНЯН/СЕРГЕЙ А Г-Н', passport='ПС4000641683', ticket_issuer='20МОЮ ТКП          ООО"МАВИНС"        САНКТ ПЕТЕРБУРГ РФ 00204282     0128')               |
|                   | YCcnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='262', airline_name='УРАЛЬСКИЕ АЛ', arrival_point=None, booking_date='2007-06-08T10:37:05.000Z', departure_point=None, full_name='МАРИНИЧЕВА/НАДЕЖДА М Г-ЖА', passport='ПС4508377725', ticket_issuer='04БРС ТКП          ООО"ПОЛЕТ-СЕРВИС"  БРАТСК РФ          00604925     0008')             |
|                   | YScnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='313', airline_name='КОГАЛЫМАВИА', arrival_point='СУР', booking_date='2007-06-08T10:37:05.000Z', departure_point='МОВ', full_name='ФИРЕР/СВЕТЛАНА П Г-ЖА 02АПР57', passport='ПС6704334129', ticket_issuer='02СУР 08 ИЮН 07    СГМУП "АВС"        СУРГУТ РФ          7К500894     0043')        |
|                   | YicnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='555', airline_name='AEROFLOT', arrival_point='MOW', booking_date='2007-06-08T10:37:05.000Z', departure_point='MOW', full_name='KOSTYLEVA/IRINA MS', passport='PS1106471655', ticket_issuer='55508364 08JUN7    ARH.CAWS           UL.TRUDA,12        SEVERODVINSK')                           |
|                   | YycnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='184', airline_name='ООО ЮТЭЙР ЭКСПРЕСС', arrival_point='УСН', booking_date='2007-06-09T17:20:32.000Z', departure_point='СЫВ', full_name='ЧАЛЫХ/АННА Г-ЖА', passport='НП2505485740', ticket_issuer='01БРЮ ТКП          К.И.ВАГОНЛИ ТРАВЕЛЬСАНКТ ПЕТЕРБУРГ РФ 00204072     0026')               |
|                   | dScnJo0BdMMFZS6WrzY_ | ru-persons-sirena-tickets |        1 | Row(airline_code='262', airline_name=None, arrival_point=None, booking_date='2007-06-08T13:17:44.000Z', departure_point=None, full_name='КИСИЛЕВ/ИГОРЬ В Г-Н', passport='ПС9201426496', ticket_issuer=None)                                                                                                     |
|                   | dycnJo0BdMMFZS6WrzY_ | ru-persons-sirena-tickets |        1 | Row(airline_code='291', airline_name='ORENBURG AIRLINES', arrival_point='DYU', booking_date='2007-06-09T14:16:50.000Z', departure_point='REN', full_name='KHUSANOVA/GULNORA MS', passport='NP048177', ticket_issuer=None)                                                                                       |
|                   | ZScnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='421', airline_name='АВИАКОМПАНИЯ СИБИРЬ', arrival_point='ЧЛБ', booking_date='2007-06-09T10:09:48.000Z', departure_point='ЧЛБ', full_name='БАРВИНКО/АЛЕНА Г-ЖА РМ15ЯНВ06', passport='СР1ФР684595', ticket_issuer='01ТЮМ ТКП          ТЦАВС              ТОБОЛЬСК РФ        00500076     0153') |
|                   | ZicnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='298', airline_name='ОАО АВИАКОМПАНИЯ ЮТЭЙР', arrival_point='СУР', booking_date='2007-06-09T10:09:50.000Z', departure_point='МОВ', full_name='АНДРОНОВА/НАТАЛЬЯ М Г-ЖА', passport='ПС6700297885', ticket_issuer='02ТЮМ ТКП          ООО ЦРПУ           НЕФТЕЮГАНСК РФ     00503322     0084')  |
|                   | ZycnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='601', airline_name='АК ЦЕНТР АВИА', arrival_point='ИНШ', booking_date='2007-06-09T10:09:51.000Z', departure_point='МОВ', full_name='АЛБАКОВ/АДАМ', passport='ПС2603091840', ticket_issuer='31МОЮ 09 ИЮН 07    ОАО"АВК "ЦЕНТР-АВИАМОСКВА РФ          ЦР000301     0303')                       |
|                   | aCcnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='497', airline_name='ASR DOMODEDOVO', arrival_point='DYU', booking_date='2007-06-09T16:28:50.000Z', departure_point='MOW', full_name='KARIMOV/ABDUKAKHOR MR', passport='NP472796', ticket_issuer='26МОВ ТКП          ЗАО"В.И.П.СЕРВИС"  МОСКВА РФ          92328132     1079')                 |
|                   | aScnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='555', airline_name='AEROFLOT', arrival_point='MOW', booking_date='2007-06-09T16:28:51.000Z', departure_point='MOW', full_name='GAYNUTDINOV/ARTUR MR', passport='PS9297043063', ticket_issuer='25МОЮ ТКП          ЗАО"АЭРОДОМ"       МОСКВА РФ          00111355     0018')                    |
|                   | aicnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='262', airline_name='УРАЛЬСКИЕ АЛ', arrival_point='МОВ', booking_date='2007-06-09T16:28:52.000Z', departure_point='ЧЛБ', full_name='ДМИТРИШИНА/МАРГАРИТА В Г-ЖА', passport='ПС1701370768', ticket_issuer='02НЖС ТКП          ООО АВС АВИАЛОТ    НИЖН НОВГОРОД РФ   92318111     0015')         |
|                   | aycnJo0BdMMFZS6WrzdB | ru-persons-sirena-tickets |        1 | Row(airline_code='555', airline_name='AEROFLOT', arrival_point='MOW', booking_date='2007-06-09T16:28:53.000Z', departure_point='MOW', full_name='KOLGUNOVA/TATYANA MR', passport='PS4506483824', ticket_issuer='25МОЮ ТКП          ЗАО"АЭРОДОМ"       МОСКВА РФ          00111355     0018')                    |
|                   | hScnJo0BdMMFZS6WrzY_ | ru-persons-sirena-tickets |        1 | Row(airline_code='298', airline_name='ОАО АВИАКОМПАНИЯ ЮТЭЙР', arrival_point='УРА', booking_date='2007-06-07T14:36:11.000Z', departure_point='ТЮМ', full_name='МАНОХИН/АЛЕКСАНДР А Г-Н', passport='ПС7403341912', ticket_issuer='02СХД ТКП          АВИАСПЕЦТЕХНОЛОГИЯ НАДЫМ РФ           92303245     0106')   |
|                   | ZycnJo0BdMMFZS6WrzY_ | ru-persons-sirena-tickets |        1 | Row(airline_code='560', airline_name='ОАО ДАЛЬАВИА', arrival_point='ХБР', booking_date='2007-06-08T06:52:24.000Z', departure_point='ЮЖХ', full_name='ШЕПОВАЛОВА/ЛЮДМИЛА Ю Г-ЖА', passport='ПС6402265273', ticket_issuer='05ЮЖХ ТКП          "СОБИ"             ЮЖНОСАХАЛИНСК РФ   00708035     0005')           |
```


## About final data
> - Total rows: 609432837

### Schema
```
root
 |-- names: array (nullable = true)
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
| names                       | birth_date   | documents                                                                                                                 | movements                                                                                                                                                                                                                                                                                      |
|:----------------------------|:-------------|:--------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Ходаковский Александр']   |              | [Row(type=0, serial='4706087336', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city='Мурманск', code='MMK'), to=Row(datetime=None, country=None, city='Анапа', code='AAQ'), code_type='IATA', ticket_order_datetime='11.06.2007 16:25', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]        |
| ['Vagapov Marat']           |              |                                                                                                                           | [Row(from=Row(datetime=None, country=None, city=None, code='DYU'), to=Row(datetime=None, country=None, city=None, code='MOW'), code_type='CODE', ticket_order_datetime='09.06.2007 07:19', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                 |
| ['Аксенов Андрей']          |              | [Row(type=0, serial='4508436067', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='МОВ'), to=Row(datetime=None, country=None, city=None, code='ТЮМ'), code_type='CODE', ticket_order_datetime='13.06.2007 15:48', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                 |
| ['Москаленко Николай']      |              | [Row(type=0, serial='0303303871', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='КРР'), to=Row(datetime=None, country=None, city=None, code='ЕКБ'), code_type='CODE', ticket_order_datetime='12.06.2007 09:54', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                 |
| ['Николаев Александр']      |              | [Row(type=0, serial='5302812104', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city='Уфа', code='UFA'), to=Row(datetime=None, country=None, city='Нижневартовск', code='NJC'), code_type='IATA', ticket_order_datetime='12.06.2007 00:42', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]     |
| ['Kuklinov Mikhail']        |              | [Row(type=4, serial='604857798', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]  | [Row(from=Row(datetime=None, country=None, city=None, code='MOW'), to=Row(datetime=None, country=None, city=None, code='KIV'), code_type='CODE', ticket_order_datetime='16.06.2007 13:08', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                 |
| ['Сизова Юлия']             |              | [Row(type=0, serial='3697042031', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city='Нижневартовск', code='NJC'), to=Row(datetime=None, country=None, city=None, code='ТЮМ'), code_type='CODE', ticket_order_datetime='13.06.2007 11:30', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]      |
| ['Сагадеев Ильнур']         |              | [Row(type=0, serial='8003702616', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='СОЙ'), to=Row(datetime=None, country=None, city=None, code='ППО'), code_type='CODE', ticket_order_datetime='15.06.2007 09:21', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                 |
| ['Суворов Василий']         |              | [Row(type=0, serial='4507222916', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='МОВ'), to=Row(datetime=None, country=None, city=None, code='МОВ'), code_type='CODE', ticket_order_datetime='15.06.2007 18:02', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                 |
| ['Бердышева Инна']          |              | [Row(type=0, serial='6505639535', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='ЕКБ'), to=Row(datetime=None, country=None, city=None, code='СПТ'), code_type='CODE', ticket_order_datetime='14.06.2007 09:57', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                 |
| ['Гладких Любовь Ивановна'] |              | [Row(type=0, serial='6701436739', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |                                                                                                                                                                                                                                                                                                |
| ['Волкова Надежда']         |              | [Row(type=0, serial='7504593278', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='ЕКБ'), to=Row(datetime=None, country=None, city=None, code='МОВ'), code_type='CODE', ticket_order_datetime='11.06.2007 14:35', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                 |
| ['Кузин Михаил']            |              | [Row(type=0, serial='3204250413', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='МОВ'), to=Row(datetime=None, country=None, city='Чебоксары', code='CSY'), code_type='CODE', ticket_order_datetime='13.06.2007 14:41', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]          |
| ['Терек Андрей']            |              | [Row(type=0, serial='4605866916', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='МОВ'), to=Row(datetime=None, country=None, city=None, code='МОВ'), code_type='CODE', ticket_order_datetime='15.06.2007 17:58', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                 |
| ['Фомин Юрий']              |              | [Row(type=0, serial='7500278983', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |                                                                                                                                                                                                                                                                                                |
| ['Федорова Евгения']        |              | [Row(type=0, serial='9803845404', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city='Якутск', code='YKS'), to=Row(datetime=None, country=None, city='Якутск', code='YKS'), code_type='IATA', ticket_order_datetime='11.06.2007 11:36', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]         |
| ['Юсупова Эльвира']         |              | [Row(type=0, serial='8003514829', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='МОВ'), to=Row(datetime=None, country=None, city='Уфа', code='UFA'), code_type='CODE', ticket_order_datetime='17.06.2007 15:45', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                |
| ['Молодило Владимир']       |              | [Row(type=0, serial='5703384109', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city=None, code='МОВ'), to=Row(datetime=None, country=None, city=None, code='ПРМ'), code_type='CODE', ticket_order_datetime='15.06.2007 11:46', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                 |
| ['Юдичева Дарья']           |              | [Row(type=0, serial='6704285199', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city='Сургут', code='SGC'), to=Row(datetime=None, country=None, city='Ханты-Мансийск', code='HMA'), code_type='IATA', ticket_order_datetime='14.06.2007 15:01', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Пономарев Сергей']        |              | [Row(type=0, serial='0405013339', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country=None, city='Казань', code='KZN'), to=Row(datetime=None, country=None, city=None, code='НРС'), code_type='CODE', ticket_order_datetime='15.06.2007 11:39', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]             |
```