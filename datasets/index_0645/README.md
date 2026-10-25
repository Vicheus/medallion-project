# Parsetron results

## About row data

> - Code name: index_0645
> - File path: pskb.com - @bereza_bd.csv
> - Total rows: 89767

### Schema
```
root
 |-- id: string (nullable = true)
 |-- updated_at: string (nullable = true)
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- _c4: string (nullable = true)

```

### Data sample
```
|    id | updated_at            | name                           | email                        | _c4   |
|------:|:----------------------|:-------------------------------|:-----------------------------|:------|
| 70861 | '2016-11-16 14:01:52' | 'наталья алексеевна'           | 'finansist101@gmail.com'     |       |
| 49969 | '2015-09-28 04:31:04' | 'Роман'                        | 'v-s-m@yandex.ru'            |       |
| 89250 | '2018-02-03 11:48:55' | 'жилин владимир александрович' | 'zhilin63@inbox.ru'          |       |
| 80733 | '2017-08-05 11:16:37' | 'Зубарева Ольга Леонидовна'    | 'stilyagi.s.k@mail.ru'       |       |
| 57710 | '2015-11-02 17:33:09' | 'ПРОХОРЕНКО ЮРИЙ ИВАНОВИЧ'     | '272asd@mail.ru'             |       |
|     2 | '2018-01-09 23:30:45' | ''Анастасия Шальнова'          | 'shalnova_ai@pskb.com'       |       |
|    13 | '2018-03-12 04:14:16' | ''Артем Хмель'                 | 'hmel_ai@pskb.com'           |       |
|     7 | '2018-04-13 02:33:59' | ''Галина Киричек'              | 'kirichek@pskb.com'          |       |
|     4 | '2017-12-07 01:18:32' | ''Георгий Бибаев'              | 'bibayev_ge@pskb.com'        |       |
|    19 | '2019-02-21 23:23:31' | ''Евгения Игнатенко'           | 'ignatenko_ey@pskb.com'      |       |
|     8 | '2018-04-13 02:34:23' | ''Наталья Денисова'            | 'denisova_nn@pskb.com'       |       |
|    10 | '2021-02-08 07:12:55' | ''Яна Дядченко'                | 'kazancheva_ya@pskb.com'     |       |
| 74109 | '2017-02-23 01:50:36' | 'Коробкова Алла Станиславовна' | 'mskorobkova1969@mail.ru'    |       |
| 89598 | '2018-02-10 01:43:45' | Денис Борисович'               | 'denis.zapevalov.88@mail.ru' |       |
| 89456 | '2018-02-07 06:57:30' | 'Бодухин Олег Юрьевич'         | 'oleg.msu@mail.ru'           |       |
|  9306 | '2015-09-28 04:30:56' | 'Боровиков Евгений Николаевич' | 'borev042@ya.ru'             |       |
| 43116 | '2015-09-28 04:31:03' | 'Сафронова Юлия Сергеевна'     | 'safronovays@mail.ru'        |       |
| 44947 | '2015-09-28 04:31:03' | 'AlekseyBarakov'               | 'barakov95@mail.ru'          |       |
| 25601 | '2015-09-28 04:30:59' | 'alex'                         | 'alex@pskb.com'              |       |
| 26643 | '2015-09-28 04:30:59' | 'Andrey'                       | 'pav@pskb.com'               |       |
```


## About final data
> - Total rows: 89657

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- actuality: date (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |
| Actuality | 99.99% |



### Data sample
```
| names                            | emails                         | actuality   |
|:---------------------------------|:-------------------------------|:------------|
| ['Наталья Алексеевна']           | ['finansist101@gmail.com']     | 16.11.2016  |
| ['Роман']                        | ['v-s-m@yandex.ru']            | 28.09.2015  |
| ['Жилин Владимир Александрович'] | ['zhilin63@inbox.ru']          | 03.02.2018  |
| ['Зубарева Ольга Леонидовна']    | ['stilyagi.s.k@mail.ru']       | 05.08.2017  |
| ['Прохоренко Юрий Иванович']     | ['272asd@mail.ru']             | 02.11.2015  |
| ['Анастасия Шальнова']           | ['shalnova_ai@pskb.com']       | 09.01.2018  |
| ['Артем Хмель']                  | ['hmel_ai@pskb.com']           | 12.03.2018  |
| ['Галина Киричек']               | ['kirichek@pskb.com']          | 13.04.2018  |
| ['Георгий Бибаев']               | ['bibayev_ge@pskb.com']        | 07.12.2017  |
| ['Евгения Игнатенко']            | ['ignatenko_ey@pskb.com']      | 21.02.2019  |
| ['Наталья Денисова']             | ['denisova_nn@pskb.com']       | 13.04.2018  |
| ['Яна Дядченко']                 | ['kazancheva_ya@pskb.com']     | 08.02.2021  |
| ['Коробкова Алла Станиславовна'] | ['mskorobkova1969@mail.ru']    | 23.02.2017  |
| ['Денис Борисович']              | ['denis.zapevalov.88@mail.ru'] | 10.02.2018  |
| ['Бодухин Олег Юрьевич']         | ['oleg.msu@mail.ru']           | 07.02.2018  |
| ['Боровиков Евгений Николаевич'] | ['borev042@ya.ru']             | 28.09.2015  |
| ['Сафронова Юлия Сергеевна']     | ['safronovays@mail.ru']        | 28.09.2015  |
| ['Alekseybarakov']               | ['barakov95@mail.ru']          | 28.09.2015  |
| ['Alex']                         | ['alex@pskb.com']              | 28.09.2015  |
| ['Andrey']                       | ['pav@pskb.com']               | 28.09.2015  |
```