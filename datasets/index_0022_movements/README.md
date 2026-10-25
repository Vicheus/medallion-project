# Parsetron results

## About row data

> - Code name: index_0022_movements
> - File path: sirena-pboarded_raw.json
> - Total rows: 159942273

### Schema
```
root
 |-- _id: string (nullable = true)
 |-- _index: string (nullable = true)
 |-- _score: long (nullable = true)
 |-- _source: struct (nullable = true)
 |    |-- @timestamp: string (nullable = true)
 |    |-- @version: string (nullable = true)
 |    |-- arrival_point: string (nullable = true)
 |    |-- birth_date: string (nullable = true)
 |    |-- booking_date: string (nullable = true)
 |    |-- citizenship: string (nullable = true)
 |    |-- departure_date: string (nullable = true)
 |    |-- departure_point: string (nullable = true)
 |    |-- email: string (nullable = true)
 |    |-- first_name: string (nullable = true)
 |    |-- full_name: string (nullable = true)
 |    |-- last_name: string (nullable = true)
 |    |-- middle_name: string (nullable = true)
 |    |-- passport: string (nullable = true)
 |    |-- phone_number: string (nullable = true)
 |    |-- phone_type: string (nullable = true)
 |    |-- tags: array (nullable = true)
 |    |    |-- element: string (containsNull = true)

```

### Data sample
```
| _id                  | _index                     |   _score | _source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:---------------------|:---------------------------|---------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| O-YJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.773183200Z', @version='1', arrival_point='AER', birth_date='2003-09-05T00:00:00.000Z', booking_date='2020-07-07T13:42:56.000Z', citizenship='RU', departure_date='2020-08-06T10:10:00.000Z', departure_point='KJA', email='ANNIJUR@MAIL.RU', first_name='ОЛЬГА', full_name='ОЛЬГА  ШАДРОВА', last_name='ШАДРОВА', middle_name=None, passport='0417123978', phone_number='79029818107', phone_type='mobile', tags=None)                                |
| POYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.773183200Z', @version='1', arrival_point='ТЗВ', birth_date='1986-11-15T00:00:00.000Z', booking_date='2020-07-27T10:09:52.000Z', citizenship='RU', departure_date='2020-08-06T14:05:00.000Z', departure_point='АПЮ', email=None, first_name='АЛЕКСАНДР', full_name='АЛЕКСАНДР  ВАСИН', last_name='ВАСИН', middle_name=None, passport='7109737348', phone_number='79088634693', phone_type='mobile', tags=None)                                         |
| PeYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.773183200Z', @version='1', arrival_point='DME', birth_date='1991-06-25T00:00:00.000Z', booking_date='2020-08-02T12:33:56.000Z', citizenship='TJ', departure_date='2020-08-06T07:40:00.000Z', departure_point='KJA', email=None, first_name='MADINA', full_name='MADINA  BOZOROVA', last_name='BOZOROVA', middle_name=None, passport='402894381', phone_number='79607717698', phone_type='mobile', tags=None)                                          |
| PuYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.777183400Z', @version='1', arrival_point='CIT', birth_date='1996-12-25T00:00:00.000Z', booking_date='2020-07-27T16:14:18.000Z', citizenship='KZ', departure_date='2020-08-01T06:15:00.000Z', departure_point='NQZ', email='AIAULIM.UTEBAY@MAIL.RU', first_name='AIAULYM', full_name='AIAULYM  UTEBAY', last_name='UTEBAY', middle_name=None, passport='035245015', phone_number='77715920531', phone_type='mobile', tags=None)                        |
| P-YJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.777183400Z', @version='1', arrival_point='NQZ', birth_date='1954-11-20T00:00:00.000Z', booking_date='2020-05-15T11:16:07.000Z', citizenship='KZ', departure_date='2020-08-01T21:35:00.000Z', departure_point='ALA', email='ALIYAZHMBK@GMAIL.COM', first_name='RAUSHAN', full_name='RAUSHAN  RYSBAYEVA', last_name='RYSBAYEVA', middle_name=None, passport='040078549', phone_number='77777008881', phone_type='mobile', tags=None)                    |
| QOYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.777183400Z', @version='1', arrival_point='ALA', birth_date='1994-05-02T00:00:00.000Z', booking_date='2020-07-12T20:50:34.000Z', citizenship='KZ', departure_date='2020-08-01T19:10:00.000Z', departure_point='UKK', email='AIZHAN.BASHENOVA@GMAIL.COM', first_name='ZHANSULU', full_name='ZHANSULU  RYSBAY', last_name='RYSBAY', middle_name=None, passport='044727746', phone_number='77087082141', phone_type='mobile', tags=None)                  |
| QeYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.777183400Z', @version='1', arrival_point='AKX', birth_date='1982-01-01T00:00:00.000Z', booking_date='2020-07-21T11:21:31.000Z', citizenship='KZ', departure_date='2020-08-01T12:10:00.000Z', departure_point='NQZ', email='ABAI.NURMAHAMAT@GMAIL.COM', first_name='ABAY', full_name='ABAY  NURMAKHAMAT', last_name='NURMAKHAMAT', middle_name=None, passport='041216525', phone_number='77716277583', phone_type='mobile', tags=None)                 |
| QuYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.777183400Z', @version='1', arrival_point='SCO', birth_date='1998-10-17T00:00:00.000Z', booking_date='2020-07-22T15:47:48.000Z', citizenship='KZ', departure_date='2020-08-01T15:35:00.000Z', departure_point='GUW', email='AVIA.SATVOYAGE@LIST.RU', first_name='DINARA', full_name='DINARA  KUANGALYYEVA', last_name='KUANGALYYEVA', middle_name=None, passport='041088042', phone_number='77086609375', phone_type='mobile', tags=None)              |
| Q-YJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.777183400Z', @version='1', arrival_point='AKX', birth_date='1979-02-07T00:00:00.000Z', booking_date='2020-07-30T10:23:24.000Z', citizenship='KZ', departure_date='2020-08-01T12:10:00.000Z', departure_point='NQZ', email='AGENTG@ITPLUS.KZ', first_name='ALMA', full_name='ALMA  BISSENBAYEVA', last_name='BISSENBAYEVA', middle_name=None, passport='044368879', phone_number='77718095008', phone_type='mobile', tags=None)                        |
| ROYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.774183900Z', @version='1', arrival_point='TJM', birth_date='1995-10-05T00:00:00.000Z', booking_date='2020-07-27T18:11:54.000Z', citizenship='RU', departure_date='2020-08-06T15:20:00.000Z', departure_point='NUX', email='AMANTAEV_DANIK@MAIL.RU', first_name='ДАНИЯР', full_name='ДАНИЯР МАКСУТОВИЧ  АМАНТАЕВ', last_name='АМАНТАЕВ', middle_name='МАКСУТОВИЧ', passport='7115186335', phone_number='79504818036', phone_type='mobile', tags=None)  |
| ReYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.774183900Z', @version='1', arrival_point='SVX', birth_date='1982-12-28T00:00:00.000Z', booking_date='2020-02-07T09:41:28.000Z', citizenship='RU', departure_date='2020-08-06T12:00:00.000Z', departure_point='NSK', email=None, first_name='АЛЕКСЕЙ', full_name='АЛЕКСЕЙ ФЕДОРОВИЧ  БУРЕНКОВ', last_name='БУРЕНКОВ', middle_name='ФЕДОРОВИЧ', passport='0402716557', phone_number='79135088780', phone_type='mobile', tags=None)                      |
| RuYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.774183900Z', @version='1', arrival_point='DME', birth_date='1983-11-30T00:00:00.000Z', booking_date='2020-08-05T18:02:11.000Z', citizenship='RU', departure_date='2020-08-06T09:50:00.000Z', departure_point='LED', email=None, first_name='ВЛАДИМИР', full_name='ВЛАДИМИР ЛЕОНИДОВИЧ  СТАРОДУБЦЕВ', last_name='СТАРОДУБЦЕВ', middle_name='ЛЕОНИДОВИЧ', passport='5403750892', phone_number='78123096847', phone_type='mobile', tags=None)            |
| R-YJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.774183900Z', @version='1', arrival_point='SIP', birth_date='1976-06-27T00:00:00.000Z', booking_date='2020-07-16T21:41:56.000Z', citizenship='RU', departure_date='2020-08-01T12:45:00.000Z', departure_point='SVO', email='KAMP-IRINA7@YANDEX.RU', first_name='ИРИНА', full_name='ИРИНА БОРИСОВНА  КАМПАНЬЯ', last_name='КАМПАНЬЯ', middle_name='БОРИСОВНА', passport='4614807497', phone_number='79855199919', phone_type='mobile', tags=None)       |
| SOYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.774183900Z', @version='1', arrival_point='SVO', birth_date='1964-04-17T00:00:00.000Z', booking_date='2020-07-12T06:38:37.000Z', citizenship='RU', departure_date='2020-08-01T14:45:00.000Z', departure_point='AER', email='DASHA.SEMINENKO@MAIL.RU', first_name='НАТАЛЬЯ', full_name='НАТАЛЬЯ НИКОЛАЕВНА  БРАГИНА', last_name='БРАГИНА', middle_name='НИКОЛАЕВНА', passport='0814265822', phone_number='79997954612', phone_type='mobile', tags=None) |
| SeYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.774183900Z', @version='1', arrival_point='UFA', birth_date='2008-05-05T00:00:00.000Z', booking_date='2020-07-20T15:00:33.000Z', citizenship='RU', departure_date='2020-08-01T16:10:00.000Z', departure_point='AER', email='ASPIRANTAGRO@YANDEX.RU', first_name='АКИМ', full_name='АКИМ РЕНАТОВИЧ  МАМАЕВ', last_name='МАМАЕВ', middle_name='РЕНАТОВИЧ', passport='IIАР721572', phone_number='79053191119', phone_type='mobile', tags=None)            |
| SuYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.775183500Z', @version='1', arrival_point='SIP', birth_date='1984-05-16T00:00:00.000Z', booking_date='2020-07-15T16:51:25.000Z', citizenship='RU', departure_date='2020-08-01T15:55:00.000Z', departure_point='SVO', email='VCHURKINA@MAIL.RU', first_name='ВЛАДА', full_name='ВЛАДА АЛЕКСАНДРОВНА  КИРЕЕВА', last_name='КИРЕЕВА', middle_name='АЛЕКСАНДРОВНА', passport='4511284763', phone_number='79852253530', phone_type='mobile', tags=None)     |
| S-YJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.776183400Z', @version='1', arrival_point='AER', birth_date='1996-07-25T00:00:00.000Z', booking_date='2020-07-28T11:46:23.000Z', citizenship='RU', departure_date='2020-08-01T10:30:00.000Z', departure_point='KUF', email='VSVIKKI@YANDEX.RU', first_name='VIKTORIIA', full_name='VIKTORIIA ALEKSEEVNA  GUREEVA', last_name='GUREEVA', middle_name='ALEKSEEVNA', passport='3618594679', phone_number='79270097380', phone_type='mobile', tags=None)   |
| TOYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.776183400Z', @version='1', arrival_point='VKO', birth_date='1983-01-01T00:00:00.000Z', booking_date='2020-07-06T08:24:58.000Z', citizenship='RU', departure_date='2020-08-01T07:40:00.000Z', departure_point='YKS', email=None, first_name='ТУЯРА', full_name='ТУЯРА НИКОЛАЕВНА  ШОХИНА', last_name='ШОХИНА', middle_name='НИКОЛАЕВНА', passport='6809542532', phone_number='79248677615', phone_type='mobile', tags=None)                            |
| TeYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.776183400Z', @version='1', arrival_point='AER', birth_date='1984-06-18T00:00:00.000Z', booking_date='2019-12-24T16:15:14.000Z', citizenship='RU', departure_date='2020-08-01T10:55:00.000Z', departure_point='VKO', email='OLEGAS84@MAIL.RU', first_name='ОЛЕГ', full_name='ОЛЕГ ВЛАДИМИРОВИЧ  КУЗЬМЕНКО', last_name='КУЗЬМЕНКО', middle_name='ВЛАДИМИРОВИЧ', passport='4520794761', phone_number='79688290854', phone_type='mobile', tags=None)      |
| TuYJIIwBFyZahMVzVdz3 | ru-persons-sirena-pboarded |        1 | Row(@timestamp='2023-11-30T11:42:11.776183400Z', @version='1', arrival_point='YKS', birth_date='1983-08-19T00:00:00.000Z', booking_date='2020-07-09T08:38:14.000Z', citizenship='RU', departure_date='2020-08-01T13:20:00.000Z', departure_point='IKT', email='PONOMAREVA_EL@AVIAFLIGHT.RU', first_name='ПАВЕЛ', full_name='ПАВЕЛ АНДРЕЕВИЧ  ТИМОФЕЕВ', last_name='ТИМОФЕЕВ', middle_name='АНДРЕЕВИЧ', passport='9804937071', phone_number='79834183345', phone_type='mobile', tags=None) |
```


## About final data
> - Total rows: 157756687

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
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
| names                               | birth_date   | emails                          | phones          | documents                                                                                                                 | movements                                                                                                                                                                                                                                                                                       |
|:------------------------------------|:-------------|:--------------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Ольга Шадрова']                   | 05.09.2003   | ['annijur@mail.ru']             | ['79029818107'] | [Row(type=0, serial='0417123978', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='06.08.2020 10:10:00', country=None, city=None, code='KJA'), to=Row(datetime=None, country=None, city=None, code='AER'), code_type='IATA', ticket_order_datetime='07.07.2020 13:42', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Александр Васин']                 | 15.11.1986   |                                 | ['79088634693'] | [Row(type=0, serial='7109737348', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='06.08.2020 14:05:00', country=None, city=None, code='АПЮ'), to=Row(datetime=None, country=None, city=None, code='ТЗВ'), code_type='IATA', ticket_order_datetime='27.07.2020 10:09', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Madina Bozorova']                 | 25.06.1991   |                                 | ['79607717698'] |                                                                                                                           | [Row(from=Row(datetime='06.08.2020 07:40:00', country=None, city=None, code='KJA'), to=Row(datetime=None, country=None, city=None, code='DME'), code_type='IATA', ticket_order_datetime='02.08.2020 12:33', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Aiaulym Utebay']                  | 25.12.1996   | ['aiaulim.utebay@mail.ru']      |                 |                                                                                                                           | [Row(from=Row(datetime='01.08.2020 06:15:00', country=None, city=None, code='NQZ'), to=Row(datetime=None, country=None, city=None, code='CIT'), code_type='IATA', ticket_order_datetime='27.07.2020 16:14', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Raushan Rysbayeva']               | 20.11.1954   | ['aliyazhmbk@gmail.com']        |                 |                                                                                                                           | [Row(from=Row(datetime='01.08.2020 21:35:00', country=None, city=None, code='ALA'), to=Row(datetime=None, country=None, city=None, code='NQZ'), code_type='IATA', ticket_order_datetime='15.05.2020 11:16', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Zhansulu Rysbay']                 | 02.05.1994   | ['aizhan.bashenova@gmail.com']  |                 |                                                                                                                           | [Row(from=Row(datetime='01.08.2020 19:10:00', country=None, city=None, code='UKK'), to=Row(datetime=None, country=None, city=None, code='ALA'), code_type='IATA', ticket_order_datetime='12.07.2020 20:50', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Abay Nurmakhamat']                | 01.01.1982   | ['abai.nurmahamat@gmail.com']   |                 |                                                                                                                           | [Row(from=Row(datetime='01.08.2020 12:10:00', country=None, city=None, code='NQZ'), to=Row(datetime=None, country=None, city=None, code='AKX'), code_type='IATA', ticket_order_datetime='21.07.2020 11:21', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Dinara Kuangalyyeva']             | 17.10.1998   | ['avia.satvoyage@list.ru']      |                 |                                                                                                                           | [Row(from=Row(datetime='01.08.2020 15:35:00', country=None, city=None, code='GUW'), to=Row(datetime=None, country=None, city=None, code='SCO'), code_type='IATA', ticket_order_datetime='22.07.2020 15:47', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Alma Bissenbayeva']               | 07.02.1979   | ['agentg@itplus.kz']            |                 |                                                                                                                           | [Row(from=Row(datetime='01.08.2020 12:10:00', country=None, city=None, code='NQZ'), to=Row(datetime=None, country=None, city=None, code='AKX'), code_type='IATA', ticket_order_datetime='30.07.2020 10:23', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Данияр Максутович Амантаев']      | 05.10.1995   | ['amantaev_danik@mail.ru']      | ['79504818036'] | [Row(type=0, serial='7115186335', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='06.08.2020 15:20:00', country=None, city=None, code='NUX'), to=Row(datetime=None, country=None, city=None, code='TJM'), code_type='IATA', ticket_order_datetime='27.07.2020 18:11', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Алексей Федорович Буренков']      | 28.12.1982   |                                 | ['79135088780'] | [Row(type=0, serial='0402716557', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='06.08.2020 12:00:00', country=None, city=None, code='NSK'), to=Row(datetime=None, country=None, city=None, code='SVX'), code_type='IATA', ticket_order_datetime='07.02.2020 09:41', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Владимир Леонидович Стародубцев'] | 30.11.1983   |                                 | ['78123096847'] | [Row(type=0, serial='5403750892', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='06.08.2020 09:50:00', country=None, city=None, code='LED'), to=Row(datetime=None, country=None, city=None, code='DME'), code_type='IATA', ticket_order_datetime='05.08.2020 18:02', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Ирина Борисовна Кампанья']        | 27.06.1976   | ['kamp-irina7@yandex.ru']       | ['79855199919'] | [Row(type=0, serial='4614807497', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='01.08.2020 12:45:00', country=None, city=None, code='SVO'), to=Row(datetime=None, country=None, city=None, code='SIP'), code_type='IATA', ticket_order_datetime='16.07.2020 21:41', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Наталья Николаевна Брагина']      | 17.04.1964   | ['dasha.seminenko@mail.ru']     | ['79997954612'] | [Row(type=0, serial='0814265822', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='01.08.2020 14:45:00', country=None, city=None, code='AER'), to=Row(datetime=None, country=None, city=None, code='SVO'), code_type='IATA', ticket_order_datetime='12.07.2020 06:38', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Аким Ренатович Мамаев']           | 05.05.2008   | ['aspirantagro@yandex.ru']      | ['79053191119'] |                                                                                                                           | [Row(from=Row(datetime='01.08.2020 16:10:00', country=None, city=None, code='AER'), to=Row(datetime=None, country=None, city=None, code='UFA'), code_type='IATA', ticket_order_datetime='20.07.2020 15:00', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Влада Александровна Киреева']     | 16.05.1984   | ['vchurkina@mail.ru']           | ['79852253530'] | [Row(type=0, serial='4511284763', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='01.08.2020 15:55:00', country=None, city=None, code='SVO'), to=Row(datetime=None, country=None, city=None, code='SIP'), code_type='IATA', ticket_order_datetime='15.07.2020 16:51', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Viktoriia Alekseevna Gureeva']    | 25.07.1996   | ['vsvikki@yandex.ru']           | ['79270097380'] | [Row(type=0, serial='3618594679', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='01.08.2020 10:30:00', country=None, city=None, code='KUF'), to=Row(datetime=None, country=None, city=None, code='AER'), code_type='IATA', ticket_order_datetime='28.07.2020 11:46', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Туяра Николаевна Шохина']         | 01.01.1983   |                                 | ['79248677615'] | [Row(type=0, serial='6809542532', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='01.08.2020 07:40:00', country=None, city=None, code='YKS'), to=Row(datetime=None, country=None, city=None, code='VKO'), code_type='IATA', ticket_order_datetime='06.07.2020 08:24', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Олег Владимирович Кузьменко']     | 18.06.1984   | ['olegas84@mail.ru']            | ['79688290854'] | [Row(type=0, serial='4520794761', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='01.08.2020 10:55:00', country=None, city=None, code='VKO'), to=Row(datetime=None, country=None, city=None, code='AER'), code_type='IATA', ticket_order_datetime='24.12.2019 16:15', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
| ['Павел Андреевич Тимофеев']        | 19.08.1983   | ['ponomareva_el@aviaflight.ru'] | ['79834183345'] | [Row(type=0, serial='9804937071', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='01.08.2020 13:20:00', country=None, city=None, code='IKT'), to=Row(datetime=None, country=None, city=None, code='YKS'), code_type='IATA', ticket_order_datetime='09.07.2020 08:38', seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)] |
```