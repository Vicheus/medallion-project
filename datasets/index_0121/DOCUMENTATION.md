# Parsetron results

## About row data

> - Code name: index_0121
> - File path: /media/user/TRANSCEND/Databases/index_0121/raw/onona_ru_2022.csv
> - Total rows: 285145

### Schema
```
root
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- city: string (nullable = true)
 |-- address1: string (nullable = true)
 |-- address2: string (nullable = true)
 |-- address3: string (nullable = true)
 |-- address4: string (nullable = true)
 |-- address5: string (nullable = true)

```

### Data sample
```
| name               | email                    |        phone | city         | address1              | address2   |   address3 |   address4 | address5   |
|:-------------------|:-------------------------|-------------:|:-------------|:----------------------|:-----------|-----------:|-----------:|:-----------|
| Вадим              | domen2000@ya.ru          |              | Электросталь |                       |            |            |            |            |
| Игорь              | marketolog2000@gmail.com |  79266721060 | Москва       |                       |            |            |            |            |
| Мельникова Наталья | melnicko.nata@yandex.ru  |  79645761559 | домодедово   | Гагарина              | 15         |          1 |         36 |            |
| Максим             | maxlovex@mail.ru         |  79654181813 | Москва       |                       |            |            |            |            |
| Руслан             | 14rusy@mail.ru           | 380936411560 | Харьков      | Петра Свинарека       | 1          |            |         83 |            |
| капралов александр | swo1@rambler.ru          |  79145731164 | серышево-2   | ДОС                   | №3         |            |         16 |            |
| budnoka budnoka    | budnokaa1975@mail.ru     |              | москва       | budnoka               |            |            |            |            |
| ohoszgye ohoszgye  | ohoszgyerew@mail.ru      |              | москва       | ohoszgye              |            |            |            |            |
| Саров Радик        | sargsyan_razmik@mail.ru  |  79262964213 | Москва       | Рубцовская нобережная | 2          |          1 |            |            |
| Лена               | mail_forelena@mail.ru    |  79262233331 | МОсква       | Правды                | 26         |            |         12 |            |
```


## About final data
> - Total rows: 187325

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Data sample
```
| names                  | phones          | emails                       | address                                            |
|:-----------------------|:----------------|:-----------------------------|:---------------------------------------------------|
| ['Игорь']              | ['79266721060'] | ['marketolog2000@gmail.com'] | ['Москва']                                         |
| ['Мельникова Наталья'] | ['79645761559'] | ['melnicko.nata@yandex.ru']  | ['домодедово Гагарина 15 1 36']                    |
| ['Максим']             | ['79654181813'] | ['maxlovex@mail.ru']         | ['Москва']                                         |
| ['Капралов Александр'] | ['79145731164'] | ['swo1@rambler.ru']          | ['серышево-2 ДОС 3 16']                            |
| ['Саров Радик']        | ['79262964213'] | ['sargsyan_razmik@mail.ru']  | ['Москва Рубцовская нобережная 2 1']               |
| ['Лена']               | ['79262233331'] | ['mail_forelena@mail.ru']    | ['МОсква Правды 26 12']                            |
| ['Евгений']            | ['79096725650'] | ['mehryakov@mail.ru']        | ['Енисейская ул. д.19 к.1']                        |
| ['Sorokin Oleg']       | ['79262113994'] | ['cartier@rambler.ru']       | ['Москва г Ленинградское ш дом 106 корпус 1']      |
| ['Анастасия']          | ['79104360288'] | ['nikonova_a_v@inbox.ru']    | ['Москва Кутузовский пр-кт 26 350']                |
| ['Кулакова Наталья']   | ['79165383470'] | ['knet23@mail.ru']           | ['Москва г Никулинская ул дом 12 корпус 2 кв.235'] |
```