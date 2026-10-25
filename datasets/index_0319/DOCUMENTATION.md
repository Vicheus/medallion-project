# Parsetron results

## About row data

> - File path: foamstore.csv
> - Total rows: 809260

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Персональная ссылка: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- адрес: string (nullable = true)

```

### Data sample
```
| ФИО   | Дата рождения   | Почта                         | Персональная ссылка   |   Номер телефона | адрес                                       |
|:------|:----------------|:------------------------------|:----------------------|-----------------:|:--------------------------------------------|
|       |                 |                               |                       |      79895146996 | Батайск, ул Октябрьская, д 116, кв 121      |
|       |                 | alvarganova01@yandex.ru       |                       |      79823289559 |                                             |
|       |                 | max21091978@gmail.com         |                       |      79994651132 |                                             |
|       |                 | 79857445524@phone.ru          |                       |      79857445524 |                                             |
|       |                 | flida713@bk.ru                |                       |      79823612353 |                                             |
|       |                 | uliana.podghornova.92@mail.ru |                       |      79823612142 |                                             |
|       |                 | kristina.nk.trg@gmail.com     |                       |      79823607131 |                                             |
|       |                 | 80pxkikbii@site.ru            |                       |      79841143670 |                                             |
|       |                 | baruev_vd@mail.ru             |                       |      79823289626 |                                             |
|       |                 | irina_neizvestna@mail.ru      |                       |      79823603628 |                                             |
|       |                 |                               |                       |      79885618390 | Ростов-на-Дону, Аксай. Платова 101а.кв 89.  |
|       |                 | top-stat@mail.ru              |                       |      79999221102 |                                             |
|       |                 | katia_1998@bk.ru              |                       |      79852169796 |                                             |
|       |                 | zhfy0039@gmail.com            |                       |      79782792887 |                                             |
|       |                 | velickoa05@gmail.com          |                       |      79857325952 |                                             |
|       |                 | battlerap89@mail.ru           |                       |      79823251377 |                                             |
|       |                 | anutohka2008@mail.ru          |                       |      79823593369 |                                             |
|       |                 |                               |                       |      79896191260 | Ростов-на-Дону, ул Орбитальная, д 30, кв 13 |
|       |                 | chegevarra64@gmail.com        |                       |      79823292620 |                                             |
|       |                 | 79994524032@phone.ru          |                       |      79994524032 |                                             |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)

```

### Data sample
```
| names                                   | emails                                   | phones          | birth_date   | address                                                | socials   |
|:----------------------------------------|:-----------------------------------------|:----------------|:-------------|:-------------------------------------------------------|:----------|
| ['Dennisfex']                           | ['zhidkiioleg1999@gmail.com']            |                 |              |                                                        |           |
| ['Армянка']                             | ['astx.vard54@gmail.com']                |                 | 28.08.2003   | ['Сюникская область Капан']                            |           |
| ['Yusuf Wa Zuleiha']                    |                                          | ['79224857687'] |              |                                                        |           |
| ['Аксай Ул.']                           | ['buyer1602490778qo@face-market.ru']     | ['79514922131'] |              |                                                        |           |
| ['Анна Ул.']                            | ['buyer1602490779sa@face-market.ru']     | ['79001263677'] |              |                                                        |           |
| ['Медина']                              | ['user_15649022955d46839721996@crm.com'] | ['79313921762'] |              |                                                        |           |
| ['Рубка Металла Ценаlk Лазерная Резка'] | ['arsentiy.kalashnikov@bk.ru']           |                 |              |                                                        |           |
| ['Елена']                               | ['fedosova_elena1973@mail.ru']           |                 |              |                                                        |           |
| ['Anabelmordn Anabelmor']               | ['valikmetalikhh@yandex.ru']             |                 |              |                                                        |           |
| ['Гмызина Анна']                        | ['gmyzinaaa@yandex.ru']                  |                 |              |                                                        |           |
| ['R.A.Mn']                              |                                          | ['79999097010'] |              |                                                        |           |
| ['Макс']                                | ['kudoist66@gmail.com']                  | ['79143139231'] |              |                                                        |           |
| ['Ooo Бауэрмашиненруссланд']            | ['a.mironenko@bauer-rus.ru']             | ['79166628089'] |              | ['МО. Люберцы ул. Железнодорожная 4 стр.3']            |           |
| ['Ooo Сергей Основа']                   | ['bel_sv@mail.ru']                       | ['79050001606'] |              | ['125284 г.Москва ул. Беговая д.11']                   |           |
| ['Ано Танцевальныйквартал']             | ['natalia.kasatkina.86@mail.ru']         | ['79105990707'] |              |                                                        |           |
| ['Ао Алмаз-Сп']                         | ['om@almaz-sp.ru']                       | ['74952216921'] |              | ['Москва ул Образцова д. 7 3 подъезд']                 |           |
| ['Ао Альфастрахование']                 | ['kazakev1@alfastrah.ru']                | ['79613212941'] |              |                                                        |           |
| ['Ао Бецема']                           | ['oprosinjak@becema.ru']                 | ['79777608820'] |              | ['Россия Московская обл Красногорск г']                |           |
| ['Ао Бецема']                           | ['dkuranov@becema.ru']                   | ['79167967853'] |              | ['Московская обл г Красногорск Ильинское шоссе д 15А'] |           |
| ['Ао Гжелка']                           | ['788455@mail.ru']                       | ['79259120651'] |              |                                                        |           |
```