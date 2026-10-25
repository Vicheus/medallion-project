# Parsetron results

## About row data

> - Code name: index_0043
> - File path: /media/user/SAMSUNG/Databases/index_0043/raw/DengiSrazy.ru_@BDdump/dengisrazy.ru_nbki.ru_03.2024_(46.230.018).csv
> - Total rows: 46230017

### Schema
```
root
 |-- sum: long (nullable = true)
 |-- name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- document: string (nullable = true)
 |-- passport_date: string (nullable = true)
 |-- birthdate: string (nullable = true)
 |-- address: string (nullable = true)

```

### Data sample
```
|   sum | name                              |       phone |   document | passport_date   | birthdate   | address   |
|------:|:----------------------------------|------------:|-----------:|:----------------|:------------|:----------|
|  2000 | Фролов Дмитрий Сергеевич          | 79202868411 | 5415407271 | 2016-02-24      | 03.12.1987  |           |
| 11000 | Ярлыков Дмитрий Сергеевич         | 79513718791 | 5013125851 | 2013-08-05      | 14.06.1993  |           |
|  7000 | Григорьева Валентина Владимировна | 79272515629 | 1804309355 | 2004-01-17      | 14.02.1944  |           |
|  7000 | Янц Владимир Игоревич             | 79094074083 | 0310707519 | 2010-07-14      | 27.07.1991  |           |
|  6000 | Двуреченский Денис Николаевич     | 79508005563 | 4214891507 | 2014-07-15      | 29.07.2016  |           |
|  7000 | Дегтярев Алексей Вячеславович     | 79198782305 | 2005727359 | 2016-07-29      | 29.07.1991  |           |
|  7000 | Путин Владимир Владимирович       | 79198782305 |            | 1991-07-29      | 29.07.1991  |           |
|  7000 | Кондратюк Игорь Андреевич         | 79613135150 | 2548664257 | 2010-07-29      | 02.07.1992  |           |
|  7000 | Пиюков Дмитрий Сергеевич          | 79198782305 | 6004083881 | 2016-07-22      | 29.07.1980  |           |
|  7000 | Рукевич Алексей Дмитриевич        | 79198782305 | 0110600214 | 2011-04-01      | 07.11.1988  |           |
|  8000 | Ильичева Альбина Владимировна     | 78988602359 | 0310535878 | 2010-12-11      | 10.11.1996  |           |
| 25000 | Путин Владимир Владимирович       | 79614052288 |            | 2016-03-08      | 13.12.1988  |           |
| 13000 | Кондратенко Игорь Андреевич       | 79613135150 | 5451365894 | 2008-08-30      | 02.07.1992  |           |
|  5000 | Ильичева Альбина Владимировна     | 79886023595 | 0310585378 | 2010-12-11      | 10.11.1996  |           |
|  7000 | Шубина Ольга Сергеевна            |             | 1106500038 | 2007-03-14      | 12.01.1981  |           |
| 25000 | Гаврикова Юлия Анатольевна        | 79156890029 | 7014553151 | 2014-12-18      | 02.08.1978  |           |
|  6000 | Шлейников Николай Николаевич      | 79028457411 | 7004686515 | 2005-03-31      | 08.08.1984  |           |
| 15000 | Иванова Екатерина Викторовна      | 79046599063 | 1701347054 | 2001-07-19      | 01.04.1977  |           |
|  2000 | Евдокимов Александр Николаевич    | 79271568719 | 4510137709 | 2009-04-13      | 29.09.1957  |           |
|  7000 | Никитина Татьяна Сергеевна        | 79510869293 | 3802565172 | 2002-05-29      | 25.03.1957  |           |
```


## About final data
> - Total rows: 45926159

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
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
| names                                 | phones          | address   | birth_date   | documents                                                                                                                         |
|:--------------------------------------|:----------------|:----------|:-------------|:----------------------------------------------------------------------------------------------------------------------------------|
| ['Фролов Дмитрий Сергеевич']          | ['79202868411'] |           | 03.12.1987   | [Row(type=0, serial='5415407271', country='RUS', date_issue='24.02.2016', date_expire=None, authority=None, authority_code=None)] |
| ['Ярлыков Дмитрий Сергеевич']         | ['79513718791'] |           | 14.06.1993   | [Row(type=0, serial='5013125851', country='RUS', date_issue='05.08.2013', date_expire=None, authority=None, authority_code=None)] |
| ['Григорьева Валентина Владимировна'] | ['79272515629'] |           | 14.02.1944   | [Row(type=0, serial='1804309355', country='RUS', date_issue='17.01.2004', date_expire=None, authority=None, authority_code=None)] |
| ['Янц Владимир Игоревич']             | ['79094074083'] |           | 27.07.1991   | [Row(type=0, serial='0310707519', country='RUS', date_issue='14.07.2010', date_expire=None, authority=None, authority_code=None)] |
| ['Двуреченский Денис Николаевич']     | ['79508005563'] |           | 29.07.2016   | [Row(type=0, serial='4214891507', country='RUS', date_issue='15.07.2014', date_expire=None, authority=None, authority_code=None)] |
| ['Дегтярев Алексей Вячеславович']     | ['79198782305'] |           | 29.07.1991   | [Row(type=0, serial='2005727359', country='RUS', date_issue='29.07.2016', date_expire=None, authority=None, authority_code=None)] |
| ['Путин Владимир Владимирович']       | ['79198782305'] |           | 29.07.1991   |                                                                                                                                   |
| ['Кондратюк Игорь Андреевич']         | ['79613135150'] |           | 02.07.1992   | [Row(type=0, serial='2548664257', country='RUS', date_issue='29.07.2010', date_expire=None, authority=None, authority_code=None)] |
| ['Пиюков Дмитрий Сергеевич']          | ['79198782305'] |           | 29.07.1980   | [Row(type=0, serial='6004083881', country='RUS', date_issue='22.07.2016', date_expire=None, authority=None, authority_code=None)] |
| ['Рукевич Алексей Дмитриевич']        | ['79198782305'] |           | 07.11.1988   | [Row(type=0, serial='0110600214', country='RUS', date_issue='01.04.2011', date_expire=None, authority=None, authority_code=None)] |
| ['Ильичева Альбина Владимировна']     |                 |           | 10.11.1996   | [Row(type=0, serial='0310535878', country='RUS', date_issue='11.12.2010', date_expire=None, authority=None, authority_code=None)] |
| ['Путин Владимир Владимирович']       | ['79614052288'] |           | 13.12.1988   |                                                                                                                                   |
| ['Кондратенко Игорь Андреевич']       | ['79613135150'] |           | 02.07.1992   | [Row(type=0, serial='5451365894', country='RUS', date_issue='30.08.2008', date_expire=None, authority=None, authority_code=None)] |
| ['Ильичева Альбина Владимировна']     | ['79886023595'] |           | 10.11.1996   | [Row(type=0, serial='0310585378', country='RUS', date_issue='11.12.2010', date_expire=None, authority=None, authority_code=None)] |
| ['Шубина Ольга Сергеевна']            |                 |           | 12.01.1981   | [Row(type=0, serial='1106500038', country='RUS', date_issue='14.03.2007', date_expire=None, authority=None, authority_code=None)] |
| ['Гаврикова Юлия Анатольевна']        | ['79156890029'] |           | 02.08.1978   | [Row(type=0, serial='7014553151', country='RUS', date_issue='18.12.2014', date_expire=None, authority=None, authority_code=None)] |
| ['Шлейников Николай Николаевич']      | ['79028457411'] |           | 08.08.1984   | [Row(type=0, serial='7004686515', country='RUS', date_issue='31.03.2005', date_expire=None, authority=None, authority_code=None)] |
| ['Иванова Екатерина Викторовна']      | ['79046599063'] |           | 01.04.1977   | [Row(type=0, serial='1701347054', country='RUS', date_issue='19.07.2001', date_expire=None, authority=None, authority_code=None)] |
| ['Евдокимов Александр Николаевич']    | ['79271568719'] |           | 29.09.1957   | [Row(type=0, serial='4510137709', country='RUS', date_issue='13.04.2009', date_expire=None, authority=None, authority_code=None)] |
| ['Никитина Татьяна Сергеевна']        | ['79510869293'] |           | 25.03.1957   | [Row(type=0, serial='3802565172', country='RUS', date_issue='29.05.2002', date_expire=None, authority=None, authority_code=None)] |
```