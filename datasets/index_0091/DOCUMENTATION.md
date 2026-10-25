# Parsetron results

## About row data

> - Code name: index_0091
> - File path: millenium_passengers_preprocessed.csv
> - Total rows: 59671

### Schema
```
root
 |-- user_id: string (nullable = true)
 |-- name: string (nullable = true)
 |-- work_position: string (nullable = true)
 |-- phone1: string (nullable = true)
 |-- phone2: string (nullable = true)
 |-- email: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- birthdate: string (nullable = true)
 |-- passport: string (nullable = true)
 |-- passport_date: date (nullable = true)
 |-- passport_enddate: date (nullable = true)
 |-- foreign_passport: string (nullable = true)
 |-- foreign_passport_date: date (nullable = true)
 |-- foreign_passport_enddate: date (nullable = true)

```

### Data sample
```
|   user_id | name                           | work_position   |      phone1 |      phone2 | email                           |   sex | birthdate   | passport   | passport_date   | passport_enddate   | foreign_passport   | foreign_passport_date   | foreign_passport_enddate   |
|----------:|:-------------------------------|:----------------|------------:|------------:|:--------------------------------|------:|:------------|:-----------|:----------------|:-------------------|:-------------------|:------------------------|:---------------------------|
|   1161446 | АЙТАСОВА ГУЛЬНАРА САМИГУЛОВНА  | Маркет менеджер | 79678811305 | 79678811305 | gulnara.aytasova@irb.rest       |     0 | 1984-02-07  | 3604910898 | 2004-07-09      |                    |                    |                         |                            |
|   1306077 | ЗАДОРОЖНЫЙ АЛЕКСАНДР           |                 | 79252688078 | 79252688078 | aleksandr.zadorozhnyi@zyfra.com |     1 | 1991-06-27  |            |                 |                    | FK049929           |                         | 2027-11-20                 |
|   1136203 | Шевелев Сергей Вячеславович    |                 | 79122403101 | 79122403101 | o.ulyanova@caterinburg.ru       |     1 | 1974-05-28  | 6519890433 | 2019-06-06      |                    |                    |                         |                            |
|   1151286 | ОСПЕНКОВ ИГОРЬ СЕРГЕЕВИЧ       |                 | 79068022657 | 79068022657 | o.ulyanova@caterinburg.ru       |     1 | 1984-10-12  | 6505777599 | 2006-03-21      |                    |                    |                         |                            |
|   1161418 | Андреев Дмитрий Евгеньевич     |                 | 79150160626 | 79150160626 | dmitriy.andreev@irb.rest        |     1 | 1981-10-23  | 9801328780 | 2002-04-29      |                    | 714909332          |                         | 2021-06-14                 |
|   1203515 | Кириллов Алексей Борисович     |                 | 79853353070 |             | kramarenko_v@ews.ru             |     1 | 1982-03-19  | 9704300034 | 2005-04-13      |                    |                    |                         |                            |
|   1327438 | Лосев Алексей Андреевич        |                 | 79257198683 |             | kramarenko_v@ews.ru             |     1 | 1989-07-27  | 4610911332 | 2010-01-19      |                    |                    |                         |                            |
|   1180136 | Нешитой Дмитрий Николаевич     |                 | 79898227558 |             | lezin_s@ews.ru                  |     1 | 1994-06-20  | 0313500280 | 2014-07-09      |                    |                    |                         |                            |
|   1140879 | HENS STEPHANE                  |                 | 79603228520 | 79603228520 | travel@sucden.ru                |     1 | 1992-12-25  | 15DK34442  | 2015-12-31      |                    |                    |                         | 2025-12-30                 |
|   1259194 | БУРНЯШЕВ КОНСТАНТИН АЛЕКСЕЕВИЧ |                 | 79370672516 | 79370672516 | mwd_kogalym@spprazvitie.ru      |     1 | 1988-11-18  | 3609019185 | 2009-09-19      |                    |                    |                         |                            |
```

> - Code name: index_0091
> - File path: millenium_users_preprocessed.csv
> - Total rows: 252282

### Schema
```
root
 |-- login: string (nullable = true)
 |-- pass: string (nullable = true)
 |-- name: string (nullable = true)
 |-- work_position: string (nullable = true)
 |-- phone1: string (nullable = true)
 |-- phone2: string (nullable = true)
 |-- phone3: string (nullable = true)
 |-- email: string (nullable = true)
 |-- sex: string (nullable = true)
 |-- birthdate: string (nullable = true)
 |-- passport: string (nullable = true)
 |-- passport_date: date (nullable = true)
 |-- passport_enddate: date (nullable = true)
 |-- foreign_passport: string (nullable = true)
 |-- foreign_passport_date: date (nullable = true)
 |-- foreign_passport_enddate: date (nullable = true)
 |-- other_passport: string (nullable = true)
 |-- other_passport_date: date (nullable = true)
 |-- other_passport_enddate: date (nullable = true)
 |-- ip: string (nullable = true)

```

### Data sample
```
| login   | pass                             | name                           | work_position          |      phone1 |      phone2 | phone3         | email                           |   sex | birthdate   |           passport | passport_date   | passport_enddate   |   foreign_passport | foreign_passport_date   | foreign_passport_enddate   |   other_passport | other_passport_date   | other_passport_enddate   | ip             |
|:--------|:---------------------------------|:-------------------------------|:-----------------------|------------:|------------:|:---------------|:--------------------------------|------:|:------------|-------------------:|:----------------|:-------------------|-------------------:|:------------------------|:---------------------------|-----------------:|:----------------------|:-------------------------|:---------------|
|         | 2b7c28a4d2baf6ccb8677c5e6f2ceaa7 | ИВАНОВ ИВАН ИВАНОВИЧ           | position               | 79377957999 |    12345678 |                | Email                           |     1 | 1990-01-01  |         1234567890 | 2020-01-01      | 2025-01-01         |                    |                         |                            |                  |                       |                          | 85.236.176.58  |
|         |                                  | Литвинова Ксения Александровна | менеджер отдела продаж |             | 89874561232 | 270-66-50      | office@millennium-dream.ru      |     0 | 1987-09-04  |            1234567 | 2012-09-01      |                    |                    | 1970-01-01              | 1970-01-01                 |                  | 1970-01-01            | 1970-01-01               | 85.140.63.209  |
|         |                                  | Сидоров Иван Петрович          |                        |             |             | 270-66-50      | sidorov@mail.ru                 |     1 | 1984-04-13  |          456456456 | 2008-04-13      |                    |             456456 | 2008-04-13              | 2011-04-13                 |                  | 1970-01-01            | 1970-01-01               | 85.140.63.209  |
|         |                                  | Комоско Алексей Александрович  | Programmer             |             |    34654987 | 9302066        | 12345                           |     1 | 1978-12-20  | 123123123123324213 | 2012-09-04      |                    |           32165487 | 2012-09-04              | 2012-09-04                 |       6304527896 | 2012-09-04            | 2012-09-04               | 85.140.63.209  |
|         |                                  | Иванов Пётр Николаевич         |                        |             | 79153789699 | 1234567        | hudg@joiahs.com                 |     1 | 1965-10-20  |         5013063489 | 2011-09-29      |                    |           12341234 | 2008-10-08              | 2012-12-31                 |          1234567 | 2003-09-14            | 2014-09-14               | 85.140.63.209  |
| girshon | 762cc0ea3b084b08879d92167c31e799 | Гиршон Анна Владимировна       |                        | 79153789699 | 79153789699 | +7(495)5102828 | a.girshon@millennium-dream.ru   |     0 | 1988-12-27  |         5300434343 | 2020-12-27      |                    |         5300434343 | 1970-01-01              | 1970-01-01                 |                  | 1970-01-01            | 1970-01-01               | 194.226.11.178 |
|         | d502e8c47fd161129218cbd0bab990a7 | Чурсина Светлана               |                        |           0 |             |                | Chursina@millennium-dream.ru    |     0 | 1970-01-01  |                    | 1970-01-01      |                    |                    | 1970-01-01              | 1970-01-01                 |                  | 1970-01-01            | 1970-01-01               | 46.0.156.5     |
|         | b863e064c1c2b6d94f864535bffac3aa | Холодкова Юлия                 |                        |             |             |                | y.holodkova@millennium-dream.ru |     0 |             |                    |                 |                    |                    |                         |                            |                  |                       |                          | 85.140.63.209  |
|         | 0e722be62e3369c241ca145172adaf42 | Каримова Лариса Валерьевна     |                        | 79153789699 | 78463746090 | 78463746090    | larisa@millennium-dream.ru      |     0 | 1985-03-14  |         3605124578 | 2003-10-09      |                    |          641542145 | 2011-02-15              | 2028-07-05                 |                  |                       |                          | 80.234.45.208  |
|         | 7e2aa2d446de8471802242d4a745ac14 | Ярчук Марина                   |                        |             |             | 78463746090    | m.yarchuk@millennium-dream.ru   |     0 |             |                    |                 |                    |                    |                         |                            |                  |                       |                          | 85.140.63.209  |
```


## About final data
> - Total rows: 310140

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password: string (nullable = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)

```

### Data sample
```
| names                              | emails                              | phones          |   sex | birth_date   | accounts                                                                                                              | works                                                                                                   | documents                                                                                                                                                                                                                                                 | ips   |
|:-----------------------------------|:------------------------------------|:----------------|------:|:-------------|:----------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------|
| ['Айтасова Гульнара Самигуловна']  | ['gulnara.aytasova@irb.rest']       | ['79678811305'] |     0 |              | [Row(title='millennium-platform.ru', link='https://millennium-platform.ru', id='1161446', login=None, password=None)] | [Row(post=None, date_start=None, date_end=None, company='Маркет менеджер', address=None, comment=None)] | [Row(type=0, serial='3604910898', country='RUS', date_issue='09.07.2004', date_expire=None, authority=None, authority_code=None)]                                                                                                                         |       |
| ['Задорожный Александр']           | ['aleksandr.zadorozhnyi@zyfra.com'] | ['79252688078'] |     1 |              | [Row(title='millennium-platform.ru', link='https://millennium-platform.ru', id='1306077', login=None, password=None)] |                                                                                                         | [Row(type=4, serial='FK049929', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                   |       |
| ['Шевелев Сергей Вячеславович']    | ['o.ulyanova@caterinburg.ru']       | ['79122403101'] |     1 |              | [Row(title='millennium-platform.ru', link='https://millennium-platform.ru', id='1136203', login=None, password=None)] |                                                                                                         | [Row(type=0, serial='6519890433', country='RUS', date_issue='06.06.2019', date_expire=None, authority=None, authority_code=None)]                                                                                                                         |       |
| ['Оспенков Игорь Сергеевич']       | ['o.ulyanova@caterinburg.ru']       | ['79068022657'] |     1 |              | [Row(title='millennium-platform.ru', link='https://millennium-platform.ru', id='1151286', login=None, password=None)] |                                                                                                         | [Row(type=0, serial='6505777599', country='RUS', date_issue='21.03.2006', date_expire=None, authority=None, authority_code=None)]                                                                                                                         |       |
| ['Андреев Дмитрий Евгеньевич']     | ['dmitriy.andreev@irb.rest']        | ['79150160626'] |     1 |              | [Row(title='millennium-platform.ru', link='https://millennium-platform.ru', id='1161418', login=None, password=None)] |                                                                                                         | [Row(type=0, serial='9801328780', country='RUS', date_issue='29.04.2002', date_expire=None, authority=None, authority_code=None), Row(type=4, serial='714909332', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |       |
| ['Кириллов Алексей Борисович']     | ['kramarenko_v@ews.ru']             | ['79853353070'] |     1 |              | [Row(title='millennium-platform.ru', link='https://millennium-platform.ru', id='1203515', login=None, password=None)] |                                                                                                         | [Row(type=0, serial='9704300034', country='RUS', date_issue='13.04.2005', date_expire=None, authority=None, authority_code=None)]                                                                                                                         |       |
| ['Лосев Алексей Андреевич']        | ['kramarenko_v@ews.ru']             | ['79257198683'] |     1 |              | [Row(title='millennium-platform.ru', link='https://millennium-platform.ru', id='1327438', login=None, password=None)] |                                                                                                         | [Row(type=0, serial='4610911332', country='RUS', date_issue='19.01.2010', date_expire=None, authority=None, authority_code=None)]                                                                                                                         |       |
| ['Нешитой Дмитрий Николаевич']     | ['lezin_s@ews.ru']                  | ['79898227558'] |     1 |              | [Row(title='millennium-platform.ru', link='https://millennium-platform.ru', id='1180136', login=None, password=None)] |                                                                                                         | [Row(type=0, serial='0313500280', country='RUS', date_issue='09.07.2014', date_expire=None, authority=None, authority_code=None)]                                                                                                                         |       |
| ['Hens Stephane']                  | ['travel@sucden.ru']                | ['79603228520'] |     1 |              | [Row(title='millennium-platform.ru', link='https://millennium-platform.ru', id='1140879', login=None, password=None)] |                                                                                                         |                                                                                                                                                                                                                                                           |       |
| ['Бурняшев Константин Алексеевич'] | ['mwd_kogalym@spprazvitie.ru']      | ['79370672516'] |     1 |              | [Row(title='millennium-platform.ru', link='https://millennium-platform.ru', id='1259194', login=None, password=None)] |                                                                                                         | [Row(type=0, serial='3609019185', country='RUS', date_issue='19.09.2009', date_expire=None, authority=None, authority_code=None)]                                                                                                                         |       |
```