# Parsetron results

## About row data

> - File path: contact.csv
> - Total rows: 867

### Schema
```
root
 |-- C_ID: integer (nullable = true)
 |-- C_FULLNAME: string (nullable = true)
 |-- C_FIRSTNAME: string (nullable = true)
 |-- C_MIDDLENAME: string (nullable = true)
 |-- C_LASTNAME: string (nullable = true)
 |-- C_TITLE: string (nullable = true)
 |-- C_COMPANY: string (nullable = true)
 |-- C_EMAILADDRESS: string (nullable = true)

```

### Data sample
```
|   C_ID | C_FULLNAME                      | C_FIRSTNAME   | C_MIDDLENAME   | C_LASTNAME   | C_TITLE   | C_COMPANY   | C_EMAILADDRESS          |
|-------:|:--------------------------------|:--------------|:---------------|:-------------|:----------|:------------|:------------------------|
|      1 | ADMIN VAGA007                   | ADMIN         | NULL           | VAGA007      | NULL      | NULL        | info@vaga007.ru         |
|      2 | Андрей Макаров                  | Андрей        | NULL           | Макаров      | NULL      | NULL        | makkorolev@rambler.ru   |
|      3 | Светлана Александровна Тюленева | Светлана      | Александровна  | Тюленева     | NULL      | NULL        | sveta@vaga007.ru        |
|      4 | Марина                          | Марина        | NULL           | NULL         | NULL      | NULL        | marina@vaga007.ru       |
|      6 | Александр Белявский             | Александр     | NULL           | Белявский    | NULL      | NULL        | ork7@list.ru            |
|    137 | Александр Гусев                 | Александр     | NULL           | Гусев        | NULL      | NULL        | avtoskoda@rambler.ru    |
|      9 | Левина Татьяна                  | Левина        | NULL           | Татьяна      | NULL      | NULL        | avto-t@bk.ru            |
|     10 | Смирнов Павел                   | Смирнов       | NULL           | Павел        | NULL      | NULL        | region-m@inbox.ru       |
|     11 | Олег Болдырев                   | Олег          | NULL           | Болдырев     | NULL      | NULL        | bolid@mail15.com        |
|     12 | Олег Дощицын                    | Олег          | NULL           | Дощицын      | NULL      | NULL        | palmira-33@mail.ru      |
|     13 | Максим Смага                    | Максим        | NULL           | Смага        | NULL      | NULL        | S.M.V.2000@mail.ru      |
|     14 | Гринин Дмитрий                  | Гринин        | NULL           | Дмитрий      | NULL      | NULL        | gdv2005@bk.ru           |
|     15 | Максим Дадеев                   | Максим        | NULL           | Дадеев       | NULL      | NULL        | magazin9@list.ru        |
|     16 | Юрий Золотов                    | Юрий          | NULL           | Золотов      | NULL      | NULL        | forsage_dmitrov@mail.ru |
|     17 | Алексей Новик                   | Алексей       | NULL           | Новик        | NULL      | NULL        | a.novik_@mail.ru        |
|     18 | VAGA VAGA                       | VAGA          | NULL           | VAGA         | NULL      | NULL        | vaga.007@mail.ru        |
|     19 | Александр  Антипов              | Александр     | NULL           | Антипов      | NULL      | NULL        | antipov-a@bk.ru         |
|     20 | алексей угольков                | алексей       | NULL           | угольков     | NULL      | NULL        | aleugolkov@mail.ru      |
|     21 | Олег Соснин                     | Олег          | NULL           | Соснин       | NULL      | NULL        | vasilic@inbox.ru        |
|     22 | Михаил Мерзликин                | Михаил        | NULL           | Мерзликин    | NULL      | NULL        | 940771@inbox.ru         |
```

> - File path: sc_customers.csv
> - Total rows: 1478

### Schema
```
root
 |-- customerID: integer (nullable = true)
 |-- Login: string (nullable = true)
 |-- cust_password: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)

```

### Data sample
```
|   customerID | Login        | cust_password    | Email                   | first_name   | last_name   |
|-------------:|:-------------|:-----------------|:------------------------|:-------------|:------------|
|            2 | ork7         | MTM1Nw==         | ork7@list.ru            | Александр    | Белявский   |
|           15 | avto-t       | MTEyMjMz         | avto-t@bk.ru            | Левина       | Татьяна     |
|            4 |              |                  | Anches30001@rambler.ru  | Александр    | Лубов       |
|            5 | z4u          | MTIzNjU0Nzg5     | region-m@inbox.ru       | Смирнов      | Павел       |
|          105 |              |                  | sergei241997@mail.ru    | АНДРЕЙ       | ЦУПИЛО      |
|           16 | bolid        | MTQ3ODk2Mw==     | bolid@mail15.com        | Олег         | Болдырев    |
|            7 | Palmira33    | MTMyNA==         | palmira-33@mail.ru      | Олег         | Дощицын     |
|            9 | s.m.v.2000   | emFx             | S.M.V.2000@mail.ru      | Максим       | Смага       |
|           10 | tcbalabanovo | bW95a2E=         | gdv2005@bk.ru           | Гринин       | Дмитрий     |
|           11 | magazin9     | c2FhYg==         | magazin9@list.ru        | Максим       | Дадеев      |
|           12 | f777         | Zm9yc2FnZTc3Nw== | forsage_dmitrov@mail.ru | Юрий         | Золотов     |
|           19 | a.novik_     | MTMxMjg1         | a.novik_@mail.ru        | Алексей      | Новик       |
|           18 | vaga         | MDA3             | vaga.007@mail.ru        | VAGA         | VAGA        |
|           14 | zimin        | MjUwMTQ1         | antipov-a@bk.ru         | Александр    | Антипов     |
|           17 | alexvag11    | MTFranZicg==     | aleugolkov@mail.ru      | алексей      | угольков    |
|           20 | viking       | c2VuYXRvcg==     | vasilic@inbox.ru        | Олег         | Соснин      |
|           21 |              |                  | 101802@rambler.ru       | андрей       | румянцев    |
|           22 | mic_bumer    | OTY0Njg3         | 940771@inbox.ru         | Михаил       | Мерзликин   |
|           23 |              |                  | infected87@bk.ru        | Александр    | Некрасов    |
|           24 | ndroid082    | cmp5dzJ0Zw==     | ndroid082@rambler.ru    | Сергей       | Доценко     |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |
| Accounts | 53.87% |



### Data sample
```
| names                                | emails                          | accounts                                                                                               |
|:-------------------------------------|:--------------------------------|:-------------------------------------------------------------------------------------------------------|
| ['Вакуленко Виктор']                 | ['wiktor0219@mail.ru']          | [Row(title='DePPul.ru', link='http://deppul.ru', login='wiktor0219', password='djAyMTkxOTU4')]         |
| ['Андрей']                           | ['andrei.chelnockov@yandex.ru'] | [Row(title='DePPul.ru', link='http://deppul.ru', login='chelnockov', password='MTYxNTk3NA==')]         |
| ['Богданов Андрей']                  | ['bas1@yandex.ru']              |                                                                                                        |
| ['Пашков Владимир']                  | ['coreopsis@yandex.ru']         |                                                                                                        |
| ['Садретдинов Ренат']                | ['renat88.08@mail.ru']          |                                                                                                        |
| ['Галкина Марина']                   | ['frau.galkina@yandex.ru']      | [Row(title='DePPul.ru', link='http://deppul.ru', login='frau.galkina', password='ZWttenlmMjAwMw==')]   |
| ['Титаев Алексей']                   | ['goukat@rambler.ru']           |                                                                                                        |
| ['Иванов Константин']                | ['ivanovkv@rambler.ru']         |                                                                                                        |
| ['Алексей Мошаров']                  | ['info@tryeparts.ru']           | [Row(title='DePPul.ru', link='http://deppul.ru', login='scuderia', password='MDEwNTE5ODY=')]           |
| ['Павловский Валерий']               | ['pavlovskiy-vv@mail.ru']       | [Row(title='DePPul.ru', link='http://deppul.ru', login='pvv10', password='MTQwOTc4')]                  |
| ['Никитин Игорь']                    | ['9709916@mail.ru']             | [Row(title='DePPul.ru', link='http://deppul.ru', login='igor_urist', password='MTIzNDU=')]             |
| ['Кучужин Антон']                    | ['antonkv@rambler.ru']          | [Row(title='DePPul.ru', link='http://deppul.ru', login='antonkv@rambler.ru', password='dWZ2LGVodQ==')] |
| ['Шевелин Миша']                     | ['shma2001@gmail.com']          | [Row(title='DePPul.ru', link='http://deppul.ru', login='shma2001', password='c3dhbGxvd3RoZTY5')]       |
| ['Котов Андрей']                     | ['drug4u@mail.ru']              |                                                                                                        |
| ['Самвел']                           | ['samvel1978@mail.ru']          | [Row(title='DePPul.ru', link='http://deppul.ru', login='samvel1978@mail.ru', password='MjAwMjc3Nw==')] |
| ['Алексей Фомин']                    | ['fomin@rostovavto.su']         | [Row(title='DePPul.ru', link='http://deppul.ru', login='RostovAvto', password='MTIzNDU2')]             |
| ['Юрий Махов']                       | ['levsha.73@bk.ru']             | [Row(title='DePPul.ru', link='http://deppul.ru', login='Yurez117', password='NTU1Nzc3')]               |
| ['Орлик Сергей']                     | ['sergeorlik@mail.ru']          |                                                                                                        |
| ['Беркутов Игорь', 'Игорь Беркутов'] | ['traliman@nm.ru']              |                                                                                                        |
| ['Avs Виктор']                       | ['vikavs@gmail.com']            | [Row(title='DePPul.ru', link='http://deppul.ru', login='vikavs', password='MTIzNDU2')]                 |
```