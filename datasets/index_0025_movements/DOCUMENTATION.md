# Parsetron results

## About row data

> - File path: Sirena 2019.txt
> - Total rows: 16294748

### Schema
```
root
 |-- FullName: string (nullable = true)
 |-- BDay: string (nullable = true)
 |-- Passport: string (nullable = true)
 |-- PlaceDeparture: string (nullable = true)
 |-- Destination: string (nullable = true)
 |-- FlightNumber: integer (nullable = true)
 |-- Airline: string (nullable = true)
 |-- FlightDate: string (nullable = true)

```

### Data sample
```
| FullName                            | BDay       | Passport   | PlaceDeparture               | Destination                  |   FlightNumber | Airline                                    | FlightDate   |
|:------------------------------------|:-----------|:-----------|:-----------------------------|:-----------------------------|---------------:|:-------------------------------------------|:-------------|
| FullName                            | BDay       | Passport   |                              |                              |            nan |                                            |              |
| FullName                            | BDay       | Passport   | PlaceDeparture               | Destination                  |            nan | Airline                                    | FlightDate   |
| А ВАЛЕНТИНА ОЛЕГОВНА 1985           | 07.09.1985 | 4508066504 | Грозный Россия               | Шереметьево Москва Россия    |            554 | СЕВЕРНЫЙ ВЕТЕР (ООО) а/к NWS N4 РОССИЯ СЕВ | 05.11.2018   |
| А ВАЛЕНТИНА ОЛЕГОВНА 1985           | 07.09.1985 | 4508066504 | Домодедово Москва Россия     | Норильск Россия              |            103 | Авиакомпания Таймыр                        | 18.11.2018   |
| А ВАЛЕНТИНА ОЛЕГОВНА 1985           | 07.09.1985 | 4508066504 | Домодедово Москва Россия     | Норильск Россия              |            403 | Авиакомпания Таймыр                        | 17.01.2019   |
| А ВАЛЕНТИНА ОЛЕГОВНА 1985           | 07.09.1985 | 4508066504 | Норильск Россия              | Домодедово Москва Россия     |            104 | Авиакомпания Таймыр                        | 21.11.2018   |
| А ВАЛЕНТИНА ОЛЕГОВНА 1985           | 07.09.1985 | 4508066504 | Норильск Россия              | Домодедово Москва Россия     |            402 | Авиакомпания Таймыр                        | 23.01.2019   |
| А ВАЛЕНТИНА ОЛЕГОВНА 1985           | 07.09.1985 | 4508066504 | Шереметьево Москва Россия    | Грозный Россия               |            553 | СЕВЕРНЫЙ ВЕТЕР (ООО) а/к NWS N4 РОССИЯ СЕВ | 02.11.2018   |
| А ВЕРА ЕВГЕНЬЕВНА 1980              | 02.02.1980 | 7902171307 | Внуково Москва Россия        | Пашковский Краснодар Россия  |            575 | ЮТЭЙР авиакомпания UTA UT РОССИЯ ЮТЭ       | 01.04.2019   |
| А ВЕРА ЕВГЕНЬЕВНА 1980              | 02.02.1980 | 7902171307 | Пашковский Краснодар Россия  | Внуково Москва Россия        |            576 | ЮТЭЙР авиакомпания UTA UT РОССИЯ ЮТЭ       | 29.03.2019   |
| А ДИАНОВА АЛЬБИНА РЕДЖЕПОВНА 1988   | 27.04.1988 | 7314065601 | Внуково Москва Россия        | Баратаевка Ульяновск Россия  |            221 | RUSLINE                                    | 29.03.2019   |
| А МАРИЯ СЕРГЕЕВНА 1984              | 14.02.1984 | 4507496726 | Адлер Сочи Россия            | Внуково Москва Россия        |            268 | ЮТЭЙР авиакомпания UTA UT РОССИЯ ЮТЭ       | 26.05.2019   |
| А МАРИЯ СЕРГЕЕВНА 1984              | 14.02.1984 | 4507496726 | Домодедово Москва Россия     | Геленджик Россия             |            231 | ЮВТ-Аэро (UVT-Aero)                        | 30.12.2018   |
| ААБ ЕЛЕНА ВИКТОРОВНА 1986           | 16.05.1986 | 5010761005 | Толмачево Новосибирск Россия | Шереметьево Москва Россия    |            546 | СЕВЕРНЫЙ ВЕТЕР (ООО) а/к NWS N4 РОССИЯ СЕВ | 02.11.2018   |
| ААБ ЕЛЕНА ВИКТОРОВНА 1986           | 16.05.1986 | 5010761005 | Шереметьево Москва Россия    | Толмачево Новосибирск Россия |            545 | СЕВЕРНЫЙ ВЕТЕР (ООО) а/к NWS N4 РОССИЯ СЕВ | 05.11.2018   |
| ААБДУЛЛИНА ГУЛЬЧАЧАК РАШИТОВНА 1968 | 05.08.1968 | 8012696848 | Домодедово Москва Россия     | Уфа Россия                   |             91 | СИБИРЬ авиакомпания SBI S7 РОССИЯ СИБ      | 13.02.2019   |
| ААБДУЛЛИНА ГУЛЬЧАЧАК РАШИТОВНА 1968 | 05.08.1968 | 8012696848 | Симферополь Россия           | Уфа Россия                   |            108 | СЕВЕРНЫЙ ВЕТЕР (ООО) а/к NWS N4 РОССИЯ СЕВ | 08.06.2018   |
| ААБДУЛЛИНА ГУЛЬЧАЧАК РАШИТОВНА 1968 | 05.08.1968 | 8012696848 | Уфа Россия                   | Внуково Москва Россия        |            364 | ЮТЭЙР авиакомпания UTA UT РОССИЯ ЮТЭ       | 02.02.2019   |
| ААБДУЛЛИНА ГУЛЬЧАЧАК РАШИТОВНА 1968 | 05.08.1968 | 8012696848 | Уфа Россия                   | Симферополь Россия           |            107 | СЕВЕРНЫЙ ВЕТЕР (ООО) а/к NWS N4 РОССИЯ СЕВ | 05.06.2018   |
| ААЗИЗ А ВАЛИ 1985                   | 01.07.1985 | 7313973402 | Баратаевка Ульяновск Россия  | Внуково Москва Россия        |            226 | RUSLINE                                    | 25.12.2018   |
```


## About final data

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
| names                              | birth_date   | documents                                                                                                                 | movements                                                                                                                                                                                                                                                                                                                 |
|:-----------------------------------|:-------------|:--------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Fullname']                       |              |                                                                                                                           | [Row(from=Row(datetime=None, country=None, city='PlaceDeparture', code=None), to=Row(datetime=None, country=None, city='Destination', code=None), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number=None, class=None, type=2, comment=None)]                                       |
| ['А Валентина Олеговна']           | 07.09.1985   | [Row(type=0, serial='4508066504', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='05.11.2018', country=None, city='Грозный Россия', code=None), to=Row(datetime=None, country=None, city='Шереметьево Москва Россия', code=None), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='554', class=None, type=2, comment=None)]                |
| ['А Валентина Олеговна']           | 07.09.1985   | [Row(type=0, serial='4508066504', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='18.11.2018', country=None, city='Домодедово Москва Россия', code='DME'), to=Row(datetime=None, country=None, city='Норильск Россия', code=None), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='103', class=None, type=2, comment=None)]               |
| ['А Валентина Олеговна']           | 07.09.1985   | [Row(type=0, serial='4508066504', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='17.01.2019', country=None, city='Домодедово Москва Россия', code='DME'), to=Row(datetime=None, country=None, city='Норильск Россия', code=None), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='403', class=None, type=2, comment=None)]               |
| ['А Валентина Олеговна']           | 07.09.1985   | [Row(type=0, serial='4508066504', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='21.11.2018', country=None, city='Норильск Россия', code=None), to=Row(datetime=None, country=None, city='Домодедово Москва Россия', code='DME'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='104', class=None, type=2, comment=None)]               |
| ['А Валентина Олеговна']           | 07.09.1985   | [Row(type=0, serial='4508066504', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='23.01.2019', country=None, city='Норильск Россия', code=None), to=Row(datetime=None, country=None, city='Домодедово Москва Россия', code='DME'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='402', class=None, type=2, comment=None)]               |
| ['А Валентина Олеговна']           | 07.09.1985   | [Row(type=0, serial='4508066504', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='02.11.2018', country=None, city='Шереметьево Москва Россия', code=None), to=Row(datetime=None, country=None, city='Грозный Россия', code=None), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='553', class=None, type=2, comment=None)]                |
| ['А Вера Евгеньевна']              | 02.02.1980   | [Row(type=0, serial='7902171307', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='01.04.2019', country=None, city='Внуково Москва Россия', code='VKO'), to=Row(datetime=None, country=None, city='Пашковский Краснодар Россия', code='KRR'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='575', class=None, type=2, comment=None)]     |
| ['А Вера Евгеньевна']              | 02.02.1980   | [Row(type=0, serial='7902171307', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='29.03.2019', country=None, city='Пашковский Краснодар Россия', code='KRR'), to=Row(datetime=None, country=None, city='Внуково Москва Россия', code='VKO'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='576', class=None, type=2, comment=None)]     |
| ['А Дианова Альбина Реджеповна']   | 27.04.1988   | [Row(type=0, serial='7314065601', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='29.03.2019', country=None, city='Внуково Москва Россия', code='VKO'), to=Row(datetime=None, country=None, city='Баратаевка Ульяновск Россия', code=None), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='221', class=None, type=2, comment=None)]      |
| ['А Мария Сергеевна']              | 14.02.1984   | [Row(type=0, serial='4507496726', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='26.05.2019', country=None, city='Адлер Сочи Россия', code='AER'), to=Row(datetime=None, country=None, city='Внуково Москва Россия', code='VKO'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='268', class=None, type=2, comment=None)]               |
| ['А Мария Сергеевна']              | 14.02.1984   | [Row(type=0, serial='4507496726', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='30.12.2018', country=None, city='Домодедово Москва Россия', code='DME'), to=Row(datetime=None, country=None, city='Геленджик Россия', code='GDZ'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='231', class=None, type=2, comment=None)]             |
| ['Ааб Елена Викторовна']           | 16.05.1986   | [Row(type=0, serial='5010761005', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='02.11.2018', country=None, city='Толмачево Новосибирск Россия', code='OVB'), to=Row(datetime=None, country=None, city='Шереметьево Москва Россия', code=None), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='546', class=None, type=2, comment=None)] |
| ['Ааб Елена Викторовна']           | 16.05.1986   | [Row(type=0, serial='5010761005', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='05.11.2018', country=None, city='Шереметьево Москва Россия', code=None), to=Row(datetime=None, country=None, city='Толмачево Новосибирск Россия', code='OVB'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='545', class=None, type=2, comment=None)] |
| ['Аабдуллина Гульчачак Рашитовна'] | 05.08.1968   | [Row(type=0, serial='8012696848', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='13.02.2019', country=None, city='Домодедово Москва Россия', code='DME'), to=Row(datetime=None, country=None, city='Уфа Россия', code='UFA'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='91', class=None, type=2, comment=None)]                    |
| ['Аабдуллина Гульчачак Рашитовна'] | 05.08.1968   | [Row(type=0, serial='8012696848', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='08.06.2018', country=None, city='Симферополь Россия', code=None), to=Row(datetime=None, country=None, city='Уфа Россия', code='UFA'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='108', class=None, type=2, comment=None)]                          |
| ['Аабдуллина Гульчачак Рашитовна'] | 05.08.1968   | [Row(type=0, serial='8012696848', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='02.02.2019', country=None, city='Уфа Россия', code='UFA'), to=Row(datetime=None, country=None, city='Внуково Москва Россия', code='VKO'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='364', class=None, type=2, comment=None)]                      |
| ['Аабдуллина Гульчачак Рашитовна'] | 05.08.1968   | [Row(type=0, serial='8012696848', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='05.06.2018', country=None, city='Уфа Россия', code='UFA'), to=Row(datetime=None, country=None, city='Симферополь Россия', code=None), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='107', class=None, type=2, comment=None)]                          |
| ['Аазиз А Вали']                   | 01.07.1985   | [Row(type=0, serial='7313973402', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='25.12.2018', country=None, city='Баратаевка Ульяновск Россия', code=None), to=Row(datetime=None, country=None, city='Внуково Москва Россия', code='VKO'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='226', class=None, type=2, comment=None)]      |
| ['Аазиз А Вали']                   | 01.07.1985   | [Row(type=0, serial='7313973402', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | [Row(from=Row(datetime='27.12.2018', country=None, city='Баратаевка Ульяновск Россия', code=None), to=Row(datetime=None, country=None, city='Внуково Москва Россия', code='VKO'), code_type='IATA', ticket_order_datetime=None, seat=None, ticket_number=None, trip_number='226', class=None, type=2, comment=None)]      |
```