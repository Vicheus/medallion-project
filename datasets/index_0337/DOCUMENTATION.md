# Parsetron results

## About row data

> - File path: мойбизнес.рф.txt
> - Total rows: 375704

### Schema
```
root
 |-- Город: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- ИНН: string (nullable = true)

```

### Data sample
```
| Город   | Почта                             |   Номер телефона | ФИО               |          ИНН |
|:--------|:----------------------------------|-----------------:|:------------------|-------------:|
|         | redlih.vladimir@mail.ru           |      79214498427 | Владимир Редлих   |              |
|         | vanya_burmistrov@rambler.ru       |      79991203953 | Иван              |              |
|         | fontagira@bk.ru                   |      79140538520 | Анастасия         |              |
|         | onecoinkgd@gmail.com              |      79097796027 | Денис             |              |
|         | alina.r.amirova@mail.ru           |      79965793220 | Алина             |              |
|         | melkumyan.tn@bashesk.ru           |      79870555577 | Тигран            |              |
|         | kaspranova@yandex.ru              |      79174017111 | Регина            |              |
|         | urk100@mail.ru                    |      79174735067 | Алсу              |              |
|         | havronovm@gmail.com               |      79069633244 | Михаил            |              |
|         | apklub@mail.ru                    |      79272369601 | Дмитрий Озернов   | 023302863516 |
|         | aya@mail.ru                       |      77777778888 | Айя               |              |
|         | autotrans.18031990@gmail.com      |      79613088838 | Александр         |              |
|         | kristinanovikova-suvorova@mail.ru |      79114554356 | Кристина Новикова |              |
|         | hohma_77@mail.ru                  |      79174555364 | Анна              |              |
|         | starschoi74@yandex.ru             |      79517717993 | Илья Старшой      |              |
|         | fizikella@yandex.ru               |      79609454462 | Евгения           |              |
|         | bairts1969@gmail.com              |      79143695888 | Баир              |              |
|         | yulia.milashenko@mail.ru          |      79132486051 | Юлия              |              |
|         | engl-dec@yandex.ru                |      79534821711 | Сергей            |   1657075036 |
|         | orlov_o@list.ru                   |      79022518307 | Олег              |              |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
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

```

### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Address | 92.79% |
| Emails | 99.87% |
| Phones | 99.89% |
| Documents | 11.38% |


### Data sample
```
| names                | address   | emails                           | phones          | documents                                                                                                                   |
|:---------------------|:----------|:---------------------------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------|
| ['Регина']           |           | ['kaspranova@yandex.ru']         | ['79174017111'] |                                                                                                                             |
| ['Галина']           |           | ['galina.akht@mail.ru']          | ['79094508004'] |                                                                                                                             |
| ['Павел']            |           | ['pashatr28102002@mail.ru']      | ['79294832692'] |                                                                                                                             |
| ['Артур']            |           | ['artyr.badamshin@gmail.com']    | ['79177874321'] |                                                                                                                             |
| ['Маргарита']        |           | ['msolodunova@list.ru']          | ['79185152250'] |                                                                                                                             |
| ['Вячеслав']         |           | ['schatajlov2018@yandex.ru']     | ['79381077413'] |                                                                                                                             |
| ['Антон Штаблавый']  |           | ['sh85anton@gmail.com']          | ['79030590590'] | [Row(type=1, serial='524502806101', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| ['Максим']           |           | ['cao.pk@yandex.ru']             | ['79001231777'] |                                                                                                                             |
| ['Николай']          |           | ['anastasiya.czimbal@mail.ru']   | ['79515142654'] |                                                                                                                             |
| ['Нуне']             |           | ['gevorkyan.nune2012@yandex.ru'] | ['79517604222'] |                                                                                                                             |
| ['Виолетта']         |           | ['violettapopov@mail.ru']        | ['79185336251'] |                                                                                                                             |
| ['Ольга']            |           | ['littlefox666@yandex.ru']       | ['79003497884'] |                                                                                                                             |
| ['Марина Бисярина']  |           | ['farida.idrisova.00@mail.ru']   | ['79174233013'] |                                                                                                                             |
| ['Наталья Бабурина'] |           | ['info@sip-rost.ru']             | ['79289014079'] |                                                                                                                             |
| ['Ольга']            |           | ['o.i.beloborodowa@mail.ru']     | ['79279424072'] |                                                                                                                             |
| ['Нина']             |           | ['ninaa55@bk.ru']                | ['79094260871'] |                                                                                                                             |
| ['Иван']             |           | ['ivan3712@mail.ru']             | ['79216176835'] |                                                                                                                             |
| ['Никита']           |           | ['create.rnd@gmail.com']         | ['79064146989'] |                                                                                                                             |
| ['Никита']           |           | ['radzik.nikita@gmail.com']      | ['79085745293'] |                                                                                                                             |
| ['Алсу']             |           | ['alsu.vlv@gmail.com']           | ['79375213246'] |                                                                                                                             |
```