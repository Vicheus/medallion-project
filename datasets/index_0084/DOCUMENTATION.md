# Parsetron results

## About row data

> - Code name: index_0084
> - File path: ock/osk_b_users_preprocessed.csv
> - Total rows: 600411

### Schema
```
root
 |-- name: string (nullable = true)
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)
 |-- email: string (nullable = true)
 |-- mobile_phone: long (nullable = true)

```

### Data sample
```
| name                         | login                                         | password                                 | email                       |   mobile_phone |
|:-----------------------------|:----------------------------------------------|:-----------------------------------------|:----------------------------|---------------:|
| Краснов Виктор               | krasnovvy@gmail.com                           | U2%k[f4M810589ded50a08fbdbc0089764e584d1 | krasnovvy@gmail.com         |  nan           |
| Краснов Виктор Юрьевич       | krasnovvy@gmail.com                           | bjYeVuIObc94c760959a91999f6176152e49e32b | krasnovvy@gmail.com         |  nan           |
| Краснов Виктор Юрьевич       | jeffreyelr@mail.ru                            | Ug97lOcV8ad49c47770cd83427ec484059b6d45b | jeffreyelr@mail.ru          |  nan           |
| Иванов Иван Иванович         | ivanov@tssoft.ru                              | DLi3kJ3U719df429fd5e5dd5de1ad0463fd6fb61 | ivanov@tssoft.ru            |  nan           |
| Khamtsov Konstantin          | Konstantin.Khamtsov@ergo.ru                   | Zu6UDgnXf13bf2c189914be6b2ca254bce0a5099 | konstantin.khamtsov@ergo.ru |  nan           |
| ШЛОМА ОЛЕГ БОРИСОВИЧ         | PersArea_fe1ce4c2-104d-44dd-93af-0fc1ba74b76c | 3Z5KEAhe42b0ada6371022e386c39a3f79083987 | olshlom@ya.ru               |    7.95041e+10 |
| Тураев Александр             | mister.turaev@yandex.ru                       | iijaM3Gq624b4e57b8558f66caa551bee8747030 | mister.turaev@yandex.ru     |  nan           |
| Калинин Вадим                | kalinin-vad@yandex.ru                         | 0gcCygT6148ad87c5e353b5f15786caf330f15b0 | kalinin-vad@yandex.ru       |  nan           |
| Матвейчук Александр          | almavi@yandex.ru                              | HCz3ejRd1e4ec5bc62dbbe39330aa470a680b2bc | almavi@yandex.ru            |  nan           |
| Васечкин Геннадий Васильевич | vas2vol@yandex.ru                             | bN7bSCjL758473b92dc4a0c16289fc2c832093aa | vas2vol@yandex.ru           |  nan           |
```

> - Code name: index_0084
> - File path: ock/osk_drafts_preprocessed.csv
> - Total rows: 46503

### Schema
```
root
 |-- full_name: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- sex: string (nullable = true)
 |-- work_place: string (nullable = true)
 |-- passport_number: string (nullable = true)
 |-- passport_date_of_issue: string (nullable = true)
 |-- passport_gived_out: string (nullable = true)
 |-- email: string (nullable = true)
 |-- payment_method: string (nullable = true)
 |-- telephones: string (nullable = true)
 |-- inn: string (nullable = true)
 |-- fact_address: string (nullable = true)
 |-- juridical_address: string (nullable = true)

```

### Data sample
```
| full_name                   | birth_date   | sex     | work_place    | passport_number   | passport_date_of_issue   | passport_gived_out   | email                | payment_method   | telephones                                                                           | inn   | fact_address                                                                             | juridical_address                                                                        |
|:----------------------------|:-------------|:--------|:--------------|:------------------|:-------------------------|:---------------------|:---------------------|:-----------------|:-------------------------------------------------------------------------------------|:------|:-----------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| Иванов Денис Анатольевич    | 27.07.1985   |         | АДС-СОФТ      | 0101 010101       | 01.01.2010               | УФМС                 | ivanovda@ads-soft.ru |                  | "[{""TelephoneType"": ""Контактный"", ""TelephonePresentation"": ""+79262232633""}]" |       | 111397, Россия, г Москва, ул Братская, д 19 к 1                                          | 111397, Россия, г Москва, ул Братская, д 19 к 1                                          |
| ыфвфыв фыв фыв              | 11.11.1991   | Мужской | фыв           | 2323 232323       | 05.12.2016               | фвывфы               |                      |                  | "[{""TelephoneType"": ""Мобильный"", ""TelephonePresentation"": ""+72131231231""}]"  | фыв   | 119334, Россия, г Москва, ул Сергея Капицы                                               | 119334, Россия, г Москва, ул Сергея Капицы                                               |
| Львов Александр Львович     | 29.01.2017   |         | 123213123     | 123123123 123123  | 30.01.2017               | 123213321            |                      |                  | "[{""TelephoneType"": ""Мобильный"", ""TelephonePresentation"": ""+71232131231""}]"  |       | 198206, Россия, г Санкт-Петербург, Санкт-Петербургское шоссе                             | 198206, Россия, г Санкт-Петербург, Санкт-Петербургское шоссе                             |
| Львов Александр Львович     | 30.01.2017   |         | 123123123     | 123123 123123     | 29.01.2017               | 123123               | вовов                |                  | "[{""TelephoneType"": ""Контактный"", ""TelephonePresentation"": ""+71231231231""}]" |       | 198206, Россия, г Санкт-Петербург, Санкт-Петербургское шоссе                             | 198206, Россия, г Санкт-Петербург, Санкт-Петербургское шоссе                             |
| Лыгин Денис Васильевич      | 03.04.1974   | Мужской | "АО ""ОСК"""  | 3600 313037       | 01.01.2001               | Советским Ровд       |                      |                  | "[{""TelephoneType"": ""Мобильный"", ""TelephonePresentation"": ""+79277409700""}]"  |       | 443023, Россия, Самарская обл, г Самара, Советский р-н, ул Советской Армии, д 17, кв 166 | 443023, Россия, Самарская обл, г Самара, Советский р-н, ул Советской Армии, д 17, кв 166 |
| Глотов Сергей Иванович      | 01.02.1976   | Мужской | "ООО ""ЛУЧ""" | 3617 123456       | 15.08.2016               | ОУФМС Самара         |                      |                  | "[{""TelephoneType"": ""Мобильный"", ""TelephonePresentation"": ""+79173333333""}]"  |       | 443041, Россия, Самарская обл, г Самара, Ленинский р-н, ул Ленинская, д 164              | 443041, Россия, Самарская обл, г Самара, Ленинский р-н, ул Ленинская, д 164              |
| Печенкина Алла Владимировна | 24.10.1959   | Женский | АО ОСК        | 3636 555555       | 10.11.2004               | РОВД                 |                      |                  | "[{""TelephoneType"": ""Мобильный"", ""TelephonePresentation"": ""+79879431030""}]"  |       | 443042, Россия, Самарская обл, г Самара, Куйбышевский р-н, ул Белорусская, д 107А, кв 56 | 443042, Россия, Самарская обл, г Самара, Куйбышевский р-н, ул Белорусская, д 107А, кв 56 |
| Козлов Виктор Иванович      | 01.02.1997   | Мужской |               | 3612 123456       | 01.02.2003               | ОУФМС                |                      |                  | "[{""TelephoneType"": ""Мобильный"", ""TelephonePresentation"": ""+79271111111""}]"  |       | 443099, Россия, Самарская обл, г Самара, Самарский р-н, ул Ленинградская, д 32, кв 18    | 443099, Россия, Самарская обл, г Самара, Самарский р-н, ул Ленинградская, д 32, кв 18    |
| Львов Александр Львович     | 25.12.1992   |         | АДС-СОФТ      | 44444 123456      | 01.03.2017               | ОВД                  | lvoval@ads-soft.ru   |                  | "[{""TelephoneType"": ""Мобильный"", ""TelephonePresentation"": ""+79165716205""}]"  |       | 123557, Россия, г Москва, Пресненский р-н, Электрический пер, д 1 к л                    | 123557, Россия, г Москва, Пресненский р-н, Электрический пер, д 1 к л                    |
| Львов Александр Львович     | 25.12.1992   | Мужской |               | 1234 123456       | 26.09.2016               | ОВД                  |                      |                  | "[{""TelephoneType"": ""Мобильный"", ""TelephonePresentation"": ""+71231241231""}]"  |       | 198206, Россия, г Санкт-Петербург, Санкт-Петербургское шоссе                             | 198206, Россия, г Санкт-Петербург, Санкт-Петербургское шоссе                             |
```

> - Code name: index_0084
> - File path: ock/osk_zay_base_preprocessed.csv
> - Total rows: 21981

### Schema
```
root
 |-- date: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- full_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- region: string (nullable = true)

```

### Data sample
```
| date                | ip             | full_name                                                                     | email                     | phone          | region          |
|:--------------------|:---------------|:------------------------------------------------------------------------------|:--------------------------|:---------------|:----------------|
| 25-02-2016 22:41:19 | 5.164.205.98   | Арсеньевв Алексей Сергеевич                                                   | staltorgarsenev@yansex.ru | 89202933156    | Нижний Новгород |
| 26-02-2016 15:32:46 | 77.40.117.234  | Вершинина Наталья Игоревна (адвокат)в интересах Столярова Александра Юрьевича | vernatalig@yandex.ru      | 8-9379-39-0747 | Йошкар-Ола      |
| 26-02-2016 15:49:55 | 95.67.144.243  | Изюмченко Олег Александрович                                                  | prov1950@rambler.ru       | 89277098683    | Самара          |
| 28-02-2016 13:15:31 | 5.227.12.53    | Кабанов Алексей Юрьевич                                                       | bumbox09@yandex.ru        | +7920 292 9476 | Нижний Новгород |
| 28-02-2016 15:08:49 | 95.79.75.219   | МОРОЗОВ АЛЕКСАНДР АЛЕКСЕЕВИЧ                                                  | sf1244@mail.ru            | 89202548900    | Нижний Новгород |
| 28-02-2016 18:11:52 | 94.232.184.7   | Печеркин Евгений Константинович                                               | pecherkin.jenya@yandex.ru | 89631435330    | Уфа             |
| 28-02-2016 21:33:15 | 31.133.236.242 | Глинников Олег Олегович                                                       | gli84@yandex.ru           | 89117961246    | Санкт-Петербург |
| 29-02-2016 12:20:36 | 85.236.170.66  | Григорьева Юлия Павловна                                                      | mamonova_yuliya@mail.ru   | 89879551223    | Самара          |
| 29-02-2016 13:12:14 | 85.140.2.129   | Кузьмина Анастасия                                                            | kuzminaanavlad@yandex.ru  | 89093636996    | Москва          |
| 29-02-2016 15:19:44 | 178.47.35.130  | Бродов Константин                                                             | kbrodov@yandex.ru         | 9043836268     | Екатеринбург    |
```

> - Code name: index_0084
> - File path: ock/osk_zay_users_preprocessed.csv
> - Total rows: 2879659

### Schema
```
root
 |-- email: string (nullable = true)
 |-- password: string (nullable = true)
 |-- name: string (nullable = true)
 |-- phone: string (nullable = true)

```

### Data sample
```
| email                  | password                         | name                   | phone   |
|:-----------------------|:---------------------------------|:-----------------------|:--------|
| CABINET_PARTNER        | 80e0f24a09c73f32e16a56648677b079 | CABINET_PARTNER        |         |
| sau@ads-soft.ru        | b1cfe9308b0eb3483c5450df01c3f06e | Ts Ts Ts               |         |
| korolev@osk-ins.ru     | f3a81f1f17af6e8e386a6ab9d4493338 | Королёв Сергей         |         |
| dvlopers@ya.ru         | c87224734d5072c985eb1452832a6099 | Лыгин Денис Васильевич |         |
| sharova@osk-ins.ru     | 621a3932a39143f54523eeefd9efc08e | Шарова Ульяна          |         |
| gribanova81@gmail.com  | e7cbce6235e6bf4ff3f33f83d48b58b7 | Грибанова Елена        |         |
| lukyanova@osk-ins.ru   | b61680a9d90dfd195371882131ad5270 | Лукьянова Анна         |         |
| kovalenko@osk-in.ru    | e10adc3949ba59abbe56e057f20f883e | Коваленко Антон        |         |
| kovalenko@osk-ins.ru   | e10adc3949ba59abbe56e057f20f883e | Коваленко Антон        |         |
| alenka19.08.87@list.ru | 804df73080e5010df7bbbe4c4fb8d60c | Малыхина Елена         |         |
```


## About final data
> - Total rows: 1136147

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
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
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)

```

### Data sample
```
| names                              | birth_date   |   sex | address   | phones   | emails                      | documents   | works   | accounts                                                                                                                                                               | ips   |
|:-----------------------------------|:-------------|------:|:----------|:---------|:----------------------------|:------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------|
| ['Кашин Денис Сергеевич']          |              |   nan |           |          | ['kasheen27@mail.ru']       |             |         | [Row(title='Объединённая страховая компания (ОСК)', link='https://www.osk-ins.ru', login='kasheen27@mail.ru', password_hash='63c499d17d0ecd9e557835b005029a5a')]       |       |
| ['Сибигатуллин Александр']         |              |   nan |           |          | ['sibigatullin89@mail.ru']  |             |         | [Row(title='Объединённая страховая компания (ОСК)', link='https://www.osk-ins.ru', login='sibigatullin89@mail.ru', password_hash='c988498e007546ed49553a9f7b97775a')]  |       |
| ['Емельянов Александр Михайлович'] |              |   nan |           |          | ['ale-x-ander@yandex.ru']   |             |         | [Row(title='Объединённая страховая компания (ОСК)', link='https://www.osk-ins.ru', login='ale-x-ander@yandex.ru', password_hash='c74792a5400fd57ca63196e7efa20c0e')]   |       |
| ['Калугин Дмитрий Игоревич']       |              |   nan |           |          | ['89221960462@mail.ru']     |             |         | [Row(title='Объединённая страховая компания (ОСК)', link='https://www.osk-ins.ru', login='89221960462@mail.ru', password_hash='f346b69b9336f12c5775d9a143fe7934')]     |       |
| ['Богданов Алексей']               |              |   nan |           |          | ['slim.v@mail.ru']          |             |         | [Row(title='Объединённая страховая компания (ОСК)', link='https://www.osk-ins.ru', login='slim.v@mail.ru', password_hash='d74ea44d4e89f0ee519a64e99f4941e7')]          |       |
| ['Евтеев Алексей']                 |              |   nan |           |          | ['nozdrja@mail.ru']         |             |         | [Row(title='Объединённая страховая компания (ОСК)', link='https://www.osk-ins.ru', login='nozdrja@mail.ru', password_hash='bfecd08ca59be60669be9a5ad77450a7')]         |       |
| ['Федорцов Владимир Васильевич']   |              |   nan |           |          | ['vladimir_fed_55@mail.ru'] |             |         | [Row(title='Объединённая страховая компания (ОСК)', link='https://www.osk-ins.ru', login='vladimir_fed_55@mail.ru', password_hash='9502e4a03302fe7349c8b383c631bc46')] |       |
| ['Диняев Радик Кямильевич']        |              |   nan |           |          | ['din.radik@yandex.ru']     |             |         | [Row(title='Объединённая страховая компания (ОСК)', link='https://www.osk-ins.ru', login='din.radik@yandex.ru', password_hash='f6e6aac66e656e28e1cf96defa5901f8')]     |       |
| ['Мкртчян Джаник Хачики']          |              |   nan |           |          | ['mnd94@mail.ru']           |             |         | [Row(title='Объединённая страховая компания (ОСК)', link='https://www.osk-ins.ru', login='mnd94@mail.ru', password_hash='3fc0a7acf087f549ac2b266baf94b8b1')]           |       |
| ['Сулейманов Рустам Фагилевич']    |              |   nan |           |          | ['sul-rustam@mail.ru']      |             |         | [Row(title='Объединённая страховая компания (ОСК)', link='https://www.osk-ins.ru', login='sul-rustam@mail.ru', password_hash='7977f2fb7f9cb9a5afcec029c71ea86e')]      |       |
```