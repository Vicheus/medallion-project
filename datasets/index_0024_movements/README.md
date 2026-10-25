# Parsetron results

## About row data

> - Code name: index_0024_movements
> - File path: Sirena-travel_2014-2016_60M.txt
> - Total rows: 60628351

### Schema
```
root
 |-- full_name: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- document_type: string (nullable = true)
 |-- document_number: string (nullable = true)
 |-- flight_company: string (nullable = true)
 |-- flight_number: string (nullable = true)
 |-- flight_date: string (nullable = true)
 |-- flight_time: string (nullable = true)
 |-- airport_from: string (nullable = true)
 |-- airport_to: string (nullable = true)
 |-- operation_date: string (nullable = true)
 |-- operation: string (nullable = true)
 |-- all_boarded: string (nullable = true)
 |-- passenger_with: string (nullable = true)
 |-- flight_signature: string (nullable = true)
 |-- operator_code: string (nullable = true)

```

### Data sample
```
| full_name                    | birth_date    | document_type   | document_number   | flight_company   | flight_number   | flight_date   | flight_time   | airport_from    | airport_to       | operation_date   | operation   | all_boarded   | passenger_with   | flight_signature                 | operator_code   |
|:-----------------------------|:--------------|:----------------|:------------------|:-----------------|:----------------|:--------------|:--------------|:----------------|:-----------------|:-----------------|:------------|:--------------|:-----------------|:---------------------------------|:----------------|
| Ф.И.О.                       | Дата рождения | Вид документа   | Серия, номер      | Авиакомпания     | Номер рейса     | Дата рейса    | Время рейса   | Аэропорт вылета | Аэропорт прилета | Дата операции    | Операция    | Все на борту  | С кем летит      | Сигнатура рейса                  | Код оператора   |
| Агеев Александр              | 24.08.1972    |                 |                   | В2               | 955             | 28.02.2016    | 17:35         | МИК             | ДМД              | 28.02.2016       | АМ          | 3             | 3                | 94A04405222006581CAB6EA2406C4AC7 | Т1Х4П6          |
| Кузенкова Ольга Олеговна     | 13.03.1994    | ПС              | 1113977775        | 5Н               | 322             | 29.10.2015    | 10:00         | ПЛК             | АХГ              | 28.02.2016       | 7О          | 4             | 4                | BC200962397C51B25F7D6A1D56208C64 | СКШ66Н          |
| Кузенкова Ольга Олеговна     | 13.03.1994    | ПС              | 1113977775        | 5Н               | 321             | 13.12.2015    | 17:50         | АХГ             | ПЛК              | 28.02.2016       | 7О          | 5             | 4                | 67D4534B20C74B3DA83F7D9DC95FBC57 | СКШ66Н          |
| Кузенкова Ольга Олеговна     | 13.03.1994    | ПС              | 1113977775        | 5Н               | 146             | 17.02.2016    | 20:10         | ПЛК             | АХГ              | 28.02.2016       | 7О          | 6             | 4                | EBC459FD507BCBF834BB4A0B9B01129E | СКШ66Н          |
| Кузенкова Ольга Олеговна     | 13.03.1994    | ПС              | 1113977775        | 5Н               | 145             | 29.02.2016    | 07:30         | АХГ             | ПЛК              | 28.02.2016       | 7О          | 7             | 4                | 4C43AEAC023156250648D865B7D69E7A | СКШ66Н          |
| Кузенкова Ольга Олеговна     | 13.03.1994    | ПС              | 1113977775        | 5Н               | 322             |               |               | ПЛК             | АХГ              | 28.02.2016       | 7О          | 8             | 4                | DD16996D8B41B48D3649E3FC55317685 | СКШ66Н          |
| Хуббатова Кристина Андреевна | 20.07.1993    | ПС              | 5512065083        | 5Н               | 323             | 13.03.2016    | 14:10         | ПЛК             | ННР              | 28.02.2016       | АП          | 9             | 9                | BFB0E8DA5A1DBE8E641644CA9D103BBC | СЦ2ФЖР          |
| Муртазина Фанюза             | 25.12.1967    | ПС              | 3612657900        | 5Н               | 532             | 14.03.2016    | 14:55         | СКЧ             | ПЛК              | 28.02.2016       | АП          | 10            | 10               | AE629374B3CFDDC7FD164C2C61CA5025 | СШ0С8Л          |
| Муртазин Салават             | 09.05.1997    | ПС              | 3610420107        | 5Н               | 532             | 14.03.2016    | 14:55         | СКЧ             | ПЛК              | 28.02.2016       | АП          | 10            | 10               | AE629374B3CFDDC7FD164C2C61CA5025 | СШ0С8Л          |
| Осипова Елена                | 12.06.1986    | ПС              | 4909914355        | 5Н               | 541             | 18.03.2016    | 12:15         | ШРМ             | АПХ              | 28.02.2016       | АП          | 12            | 12               | DE32DDB8892DF7507FE71094227C1F8A | Т00Ш87          |
| Осипов Матвей                | 19.09.2015    | СР              | VАГ533791         | 5Н               | 541             | 18.03.2016    | 12:15         | ШРМ             | АПХ              | 28.02.2016       | АП          | 12            | 12               | DE32DDB8892DF7507FE71094227C1F8A | Т00Ш87          |
| Остроухова Наталия           | 16.01.1978    | ПС              | 5508053051        | 5Н               | 323             | 28.02.2016    | 14:10         | ПЛК             | ННР              | 28.02.2016       | АП          | 14            | 14               | 6835D26B258BB546D83E95D4445BA822 | Т0ГВГ2          |
| Носова Екатерина             | 13.05.1957    | ПС              | 4702413251        | 5Н               | 518             | 29.04.2016    | 14:30         | МУН             | ДМД              | 28.02.2016       | АП          | 15            | 15               | 95418DEEEBBFFD136824736A35F823A8 | Т0М75Л          |
| Носова Екатерина             | 13.05.1957    | ПС              | 4702413251        | 5Н               | 517             | 08.05.2016    | 10:45         | ДМД             | МУН              | 28.02.2016       | АП          | 16            | 15               | C070EEA36572D89B97D891E1D0E1CEA1 | Т0М75Л          |
| Летфуллина Миляуша           | 27.11.1991    | ПС              | 3611540813        | 5Н               | 532             | 14.03.2016    | 14:55         | СКЧ             | ПЛК              | 28.02.2016       | АП          | 10            | 17               | AE629374B3CFDDC7FD164C2C61CA5025 | Т1030Д          |
| Кузнецов Михаил Алексеевич   | 30.05.2015    | СР              | 1УГ519562         | 5Н               | 318             | 01.03.2016    | 18:00         | АХГ             | ННР              | 28.02.2016       | АП          | 18            | 18               | DDB4CF0F230BE1BE4BDD69E79DD4AC4F | Т0Б2Ж3          |
| Жданова Елена Михайловна     | 05.01.1978    | ПС              | 1107541657        | 5Н               | 145             | 28.02.2016    | 07:30         | АХГ             | ПЛК              | 28.02.2016       | АП          | 19            | 19               | B6797A7B7900792E81E975AF522964F1 | Т1ХЖРМ          |
| Жданова Елена Михайловна     | 05.01.1978    | ПС              | 1107541657        | 5Н               | 322             | 29.02.2016    | 10:00         | ПЛК             | АХГ              | 28.02.2016       | АП          | 20            | 19               | D6829B683539AF33775947F86285FD70 | Т1ХЖРМ          |
| Серенко Иван Александрович   | 17.01.1982    | ПСП             | 730927891         | 5Н               | 118             | 04.03.2016    | 20:05         | ШРМ             | АХГ              | 28.02.2016       | АП          | 21            | 21               | D0F915673AB1418850C84C21BD855A5E | Т215ЖТ          |
```


## About final data
> - Total rows: 60627667

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
| names                            | birth_date   | documents                                                                                                                 | movements                                                                                                                                                                                                                                                                                                                |
|:---------------------------------|:-------------|:--------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Ф.И.О.']                       |              |                                                                                                                           | [Row(from=Row(datetime=None, country='RUS', city=None, code=None), to=Row(datetime=None, country='RUS', city=None, code=None), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='Номер рейса', class=None, type=2, comment=None)]                                                |
| ['Агеев Александр']              | 24.08.1972   |                                                                                                                           | [Row(from=Row(datetime='28.02.2016 17:35:00', country='RUS', city=None, code=None), to=Row(datetime=None, country='RUS', city='Москва', code='DME'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='955', class=None, type=2, comment=None)]                    |
| ['Кузенкова Ольга Олеговна']     | 13.03.1994   | [Row(type=0, serial='1113977775', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='29.10.2015 10:00:00', country='RUS', city='Санкт-Петербург', code='LED'), to=Row(datetime=None, country='RUS', city='Архангельск', code='ARH'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='322', class=None, type=2, comment=None)] |
| ['Кузенкова Ольга Олеговна']     | 13.03.1994   | [Row(type=0, serial='1113977775', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='13.12.2015 17:50:00', country='RUS', city='Архангельск', code='ARH'), to=Row(datetime=None, country='RUS', city='Санкт-Петербург', code='LED'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='321', class=None, type=2, comment=None)] |
| ['Кузенкова Ольга Олеговна']     | 13.03.1994   | [Row(type=0, serial='1113977775', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='17.02.2016 20:10:00', country='RUS', city='Санкт-Петербург', code='LED'), to=Row(datetime=None, country='RUS', city='Архангельск', code='ARH'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='146', class=None, type=2, comment=None)] |
| ['Кузенкова Ольга Олеговна']     | 13.03.1994   | [Row(type=0, serial='1113977775', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='29.02.2016 07:30:00', country='RUS', city='Архангельск', code='ARH'), to=Row(datetime=None, country='RUS', city='Санкт-Петербург', code='LED'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='145', class=None, type=2, comment=None)] |
| ['Кузенкова Ольга Олеговна']     | 13.03.1994   | [Row(type=0, serial='1113977775', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime=None, country='RUS', city='Санкт-Петербург', code='LED'), to=Row(datetime=None, country='RUS', city='Архангельск', code='ARH'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='322', class=None, type=2, comment=None)]                  |
| ['Хуббатова Кристина Андреевна'] | 20.07.1993   | [Row(type=0, serial='5512065083', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='13.03.2016 14:10:00', country='RUS', city='Санкт-Петербург', code='LED'), to=Row(datetime=None, country='RUS', city='Нарьян-Мар', code='NNM'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='323', class=None, type=2, comment=None)]  |
| ['Муртазина Фанюза']             | 25.12.1967   | [Row(type=0, serial='3612657900', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='14.03.2016 14:55:00', country='RUS', city='Самара', code='KUF'), to=Row(datetime=None, country='RUS', city='Санкт-Петербург', code='LED'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='532', class=None, type=2, comment=None)]      |
| ['Муртазин Салават']             | 09.05.1997   | [Row(type=0, serial='3610420107', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='14.03.2016 14:55:00', country='RUS', city='Самара', code='KUF'), to=Row(datetime=None, country='RUS', city='Санкт-Петербург', code='LED'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='532', class=None, type=2, comment=None)]      |
| ['Осипова Елена']                | 12.06.1986   | [Row(type=0, serial='4909914355', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='18.03.2016 12:15:00', country='RUS', city='Москва', code='SVO'), to=Row(datetime=None, country='RUS', city='Апатиты', code='KVK'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='541', class=None, type=2, comment=None)]              |
| ['Осипов Матвей']                | 19.09.2015   | [Row(type=5, serial='VАГ533791', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]  | [Row(from=Row(datetime='18.03.2016 12:15:00', country='RUS', city='Москва', code='SVO'), to=Row(datetime=None, country='RUS', city='Апатиты', code='KVK'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='541', class=None, type=2, comment=None)]              |
| ['Остроухова Наталия']           | 16.01.1978   | [Row(type=0, serial='5508053051', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='28.02.2016 14:10:00', country='RUS', city='Санкт-Петербург', code='LED'), to=Row(datetime=None, country='RUS', city='Нарьян-Мар', code='NNM'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='323', class=None, type=2, comment=None)]  |
| ['Носова Екатерина']             | 13.05.1957   | [Row(type=0, serial='4702413251', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='29.04.2016 14:30:00', country='RUS', city='Мурманск', code='MMK'), to=Row(datetime=None, country='RUS', city='Москва', code='DME'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='518', class=None, type=2, comment=None)]             |
| ['Носова Екатерина']             | 13.05.1957   | [Row(type=0, serial='4702413251', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='08.05.2016 10:45:00', country='RUS', city='Москва', code='DME'), to=Row(datetime=None, country='RUS', city='Мурманск', code='MMK'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='517', class=None, type=2, comment=None)]             |
| ['Летфуллина Миляуша']           | 27.11.1991   | [Row(type=0, serial='3611540813', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='14.03.2016 14:55:00', country='RUS', city='Самара', code='KUF'), to=Row(datetime=None, country='RUS', city='Санкт-Петербург', code='LED'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='532', class=None, type=2, comment=None)]      |
| ['Кузнецов Михаил Алексеевич']   | 30.05.2015   | [Row(type=5, serial='1УГ519562', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]  | [Row(from=Row(datetime='01.03.2016 18:00:00', country='RUS', city='Архангельск', code='ARH'), to=Row(datetime=None, country='RUS', city='Нарьян-Мар', code='NNM'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='318', class=None, type=2, comment=None)]      |
| ['Жданова Елена Михайловна']     | 05.01.1978   | [Row(type=0, serial='1107541657', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='28.02.2016 07:30:00', country='RUS', city='Архангельск', code='ARH'), to=Row(datetime=None, country='RUS', city='Санкт-Петербург', code='LED'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='145', class=None, type=2, comment=None)] |
| ['Жданова Елена Михайловна']     | 05.01.1978   | [Row(type=0, serial='1107541657', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='29.02.2016 10:00:00', country='RUS', city='Санкт-Петербург', code='LED'), to=Row(datetime=None, country='RUS', city='Архангельск', code='ARH'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='322', class=None, type=2, comment=None)] |
| ['Серенко Иван Александрович']   | 17.01.1982   | [Row(type=4, serial='730927891', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]  | [Row(from=Row(datetime='04.03.2016 20:05:00', country='RUS', city='Москва', code='SVO'), to=Row(datetime=None, country='RUS', city='Архангельск', code='ARH'), code_type='IATA', ticket_order_datetime='28.02.2016 00:00', seat=None, ticket_number=None, trip_number='118', class=None, type=2, comment=None)]          |
```