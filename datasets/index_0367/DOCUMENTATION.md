# Parsetron results

## About row data

> - File path: автоцентр_Lada_2022.csv
> - Total rows: 32579

### Schema
```
root
 |-- Номер телефона: long (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Машина: string (nullable = true)

```

### Data sample
```
|   Номер телефона | ФИО                              | Дата рождения   | Машина               |
|-----------------:|:---------------------------------|:----------------|:---------------------|
|      79127734806 | Магомедова Людмила Александровна | 06.04.1961      | ВАЗ 2112 2004 г.     |
|      79048150313 | Лукманов Урал Ризаевич           | 12.09.1953      | ВАЗ 2111 2004 г.     |
|      79193593488 | Сохань Олег Анатольевич          | 23.01.1966      | ВАЗ 2110 2004 г.     |
|      79827500671 | Гилев Александр Николаевич       | 25.01.1965      | ВАЗ 2110 2004 г.     |
|      79085855625 | Русаков Дмитрий Сергеевич        | 20.11.1992      | ВАЗ 21099 2004 г.    |
|      79033927766 | Мамонтов Андрей Викторович       | 06.04.1976      | ВАЗ 21099 2004 г.    |
|      79224421246 | Калитенко Антон Вячеславович     | 21.09.1996      | ВАЗ 2115 2004 г.     |
|      79527386703 | Анчугов Евгений Григорьевич      | 01.05.1950      | ВАЗ 2111 2004 г.     |
|      79615701459 | Харин Сергей Валентинович        | 19.11.1956      | ВАЗ 2107 2004 г.     |
|      79195719160 | Васильев Александр Владимирович  | 01.10.1976      | ВАЗ 2107 2004 г.     |
|      79878904393 | Качалин Юрий Николаевич          | 12.03.1976      | ВАЗ 2115 2004 г.     |
|      79045408047 | Рушков Иван Валентинович         | 22.03.1972      | ВАЗ 2110 2004 г.     |
|      79068597727 | Федюкова Елена Андреевна         | 24.08.1990      | ВАЗ 2112 2004 г.     |
|      79527165920 | Пшеничная Ольга Валериевна       | 29.05.1972      | ВАЗ 2107 2004 г.     |
|      79086390233 | Исаков Махмадтолиб Рашидович     | 15.05.1968      | ВАЗ 2110 2004 г.     |
|      79324776909 | Мокроусов Василий Валерьевич     | 17.04.1959      | ВАЗ 2107 2004 г.     |
|      79089347244 | Кондратьев Кирилл Валерьевич     | 03.01.1991      | ВАЗ 2107 2004 г.     |
|      79525192909 | Тайчинов Дмитрий Тагирович       | 08.11.1985      | ВАЗ 2110 2004 г.     |
|      79195830018 | Зайцев Владимир Васильевич       | 12.02.1961      | ВАЗ 2107 2004 г.     |
|      79228880231 | Захаров Сергей Петрович          | 06.08.1968      | ВАЗ 1111 Ока 2004 г. |
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
 |-- vehicles: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = false)
 |    |    |-- model: string (nullable = true)
 |    |    |-- year: integer (nullable = true)
 |    |    |-- color: string (nullable = true)
 |    |    |-- number: string (nullable = true)
 |    |    |-- vin: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 100.00% |
| Phones | 100.00% |
| Vehicles | 100.00% |



### Data sample
```
| names                                | birth_date   | phones          | vehicles                                                                                                |
|:-------------------------------------|:-------------|:----------------|:--------------------------------------------------------------------------------------------------------|
| ['Магомедова Людмила Александровна'] | 06.01.1961   | ['79127734806'] | [Row(type=1, model='ВАЗ 2112 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Лукманов Урал Ризаевич']           | 12.01.1953   | ['79048150313'] | [Row(type=1, model='ВАЗ 2111 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Сохань Олег Анатольевич']          | 23.01.1966   | ['79193593488'] | [Row(type=1, model='ВАЗ 2110 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Гилев Александр Николаевич']       | 25.01.1965   | ['79827500671'] | [Row(type=1, model='ВАЗ 2110 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Русаков Дмитрий Сергеевич']        | 20.01.1992   | ['79085855625'] | [Row(type=1, model='ВАЗ 21099 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]    |
| ['Мамонтов Андрей Викторович']       | 06.01.1976   | ['79033927766'] | [Row(type=1, model='ВАЗ 21099 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]    |
| ['Калитенко Антон Вячеславович']     | 21.01.1996   | ['79224421246'] | [Row(type=1, model='ВАЗ 2115 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Анчугов Евгений Григорьевич']      | 01.01.1950   | ['79527386703'] | [Row(type=1, model='ВАЗ 2111 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Харин Сергей Валентинович']        | 19.01.1956   | ['79615701459'] | [Row(type=1, model='ВАЗ 2107 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Васильев Александр Владимирович']  | 01.01.1976   | ['79195719160'] | [Row(type=1, model='ВАЗ 2107 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Качалин Юрий Николаевич']          | 12.01.1976   | ['79878904393'] | [Row(type=1, model='ВАЗ 2115 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Рушков Иван Валентинович']         | 22.01.1972   | ['79045408047'] | [Row(type=1, model='ВАЗ 2110 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Федюкова Елена Андреевна']         | 24.01.1990   | ['79068597727'] | [Row(type=1, model='ВАЗ 2112 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Пшеничная Ольга Валериевна']       | 29.01.1972   | ['79527165920'] | [Row(type=1, model='ВАЗ 2107 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Исаков Махмадтолиб Рашидович']     | 15.01.1968   | ['79086390233'] | [Row(type=1, model='ВАЗ 2110 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Мокроусов Василий Валерьевич']     | 17.01.1959   | ['79324776909'] | [Row(type=1, model='ВАЗ 2107 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Кондратьев Кирилл Валерьевич']     | 03.01.1991   | ['79089347244'] | [Row(type=1, model='ВАЗ 2107 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Тайчинов Дмитрий Тагирович']       | 08.01.1985   | ['79525192909'] | [Row(type=1, model='ВАЗ 2110 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Зайцев Владимир Васильевич']       | 12.01.1961   | ['79195830018'] | [Row(type=1, model='ВАЗ 2107 2004 г.', year=None, color=None, number=None, vin=None, comment=None)]     |
| ['Захаров Сергей Петрович']          | 06.01.1968   | ['79228880231'] | [Row(type=1, model='ВАЗ 1111 Ока 2004 г.', year=None, color=None, number=None, vin=None, comment=None)] |
```