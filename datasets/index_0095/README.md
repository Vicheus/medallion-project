# Parsetron results

## About row data

> - Code name: index_0095
> - File path: askona_preprocessed.csv
> - Total rows: 1949212

### Schema
```
root
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)
 |-- full_name: string (nullable = true)
 |-- sex: string (nullable = true)
 |-- phone1: string (nullable = true)
 |-- phone2: string (nullable = true)
 |-- email1: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- birth_date: date (nullable = true)

```

### Data sample
```
| login                       | password                                 | full_name                    | sex   |      phone1 | phone2   | email1                      | email2   | birth_date   |
|:----------------------------|:-----------------------------------------|:-----------------------------|:------|------------:|:---------|:----------------------------|:---------|:-------------|
| 99999999999                 | Z1w\/7Bmaad29419904baea1c62ee1d9592d1631 | Askona Askona                |       | 99999999999 |          |                             |          | 1970-01-01   |
| 79278633263                 | Q<1cdS0[81006bcd3460aa65b25535a903294d10 | Кириллов Александр           |       | 79278633263 |          | info@axdr.ru                |          |              |
| nataliepotapova30@gmail.com | q3dVC02S94dc8192043565cb7599e5e074c296bc | nataliya nataliya            |       | 79204136615 |          | nataliepotapova30@gmail.com |          |              |
| voroninny@askona.ru         | @0In!7Paf62e04e91ac9ca195c12fe41db01d1db | Воронин Николай              |       |             |          | voroninny@askona.ru         |          |              |
| 79277213199                 | N_a7{B9m17549c81a45cb42862263fa5aaeacb78 | Рыбушкин Александр Сергеевич |       | 79277213199 |          | test@ttt.tt                 |          | 2021-09-15   |
| merkulovsm@askona.ru        | 5G[e1D_t143c8e62606637cae7ac302247d1dfd2 | Меркулов Сергей              |       |             |          | merkulovsm@askona.ru        |          | 1990-04-25   |
| 93718522880                 | Tl}93(Kdc5420c6e7bb1c27640a720a018eb02b1 | Скрипай Юля                  |       | 93718522880 |          | skripayyv@askona.ru         |          |              |
| shuinovii@askona.ru         | jP9,2n<I5d776e21a6c703bda161a9914b2ec3a0 | Шуинов Илья Ильич            |       | 79209002544 |          | shuinovii@askona.ru         |          |              |
| 79270057642                 | 9_iD7r|O4c929d5ddd4bcd46039cb9e51a6be2b5 | 2 Дмитрий                    | M     | 79270057642 |          | etozhedafomenko@gmail.com   |          | 1994-09-29   |
| zhiryakovatb@askona.ru      | Hx:57nJ}2bc0a433ac7441c0f54dc3cc0ef20516 | Рудикова Татьяна Борисовна   | F     | 79190172821 |          | zhiryakovatb@askona.ru      |          | 1980-07-01   |
```


## About final data
> - Total rows: 1767922

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```

### Data sample
```
| names                     |   sex | birth_date   | emails                             | phones          | accounts                                                                                                                                              |
|:--------------------------|------:|:-------------|:-----------------------------------|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['- Рината']              |   nan |              |                                    | ['79874828740'] | [Row(title='Аскона', link='https://www.askona.ru', login='79874828740', password_hash='USQAUwfJ826766aa472282e683cb8b73ef1b6c60')]                    |
| ['- Яна']                 |   nan |              |                                    | ['79515139118'] | [Row(title='Аскона', link='https://www.askona.ru', login='79515139118', password_hash='PBWiWnGf5aadfd4c288268898073270ba848b5a3')]                    |
| ['A Arina']               |   nan |              | ['arina_anina@mail.ru']            | ['79854461656'] | [Row(title='Аскона', link='https://www.askona.ru', login='79854461656', password_hash='uEyHBf3A6771d88c13ab469d28f960347e82651f')]                    |
| ['Aleksey']               |   nan |              |                                    | ['79217507957'] | [Row(title='Аскона', link='https://www.askona.ru', login='79217507957', password_hash='q6Pom9CVdef5da8dd5871d52b64dd32bf5e269c8')]                    |
| ['Alexey Бузырев']        |   nan |              | ['alexeybuzyrev@yandex.ru']        | ['79169169963'] | [Row(title='Аскона', link='https://www.askona.ru', login='79169169963', password_hash='jxnq2pf5bf1dc79556f23113408959a8d9a90c1c')]                    |
| ['Amellinalist.Ru']       |   nan |              | ['amellina@list.ru']               |                 | [Row(title='Аскона', link='https://www.askona.ru', login='amellina@list.ru', password_hash='0-^4S$QF7289be90dc3a33a29d9c9ec5bb129a5e')]               |
| ['Anastasia Magid']       |   nan |              | ['cgreg.low@gmail.com']            | ['79164536318'] | [Row(title='Аскона', link='https://www.askona.ru', login='79164536318', password_hash='HmdxsqWL00f7b89691bff8755fd36088a05f2514')]                    |
| ['Andreyoymail.Ru']       |   nan |              | ['andreyoy@mail.ru']               |                 | [Row(title='Аскона', link='https://www.askona.ru', login='andreyoy@mail.ru', password_hash='I!:g8.y839c63b1f8bfde22a979abac0755ed87d')]               |
| ['Artyushkina Ekaterina'] |   nan |              |                                    | ['79265378226'] | [Row(title='Аскона', link='https://www.askona.ru', login='79265378226', password_hash='I8p4fRqrb5614584153cec69d03683f16f3a125b')]                    |
| ['Asdasdasd Adasda']      |   nan |              | ['gildasdasdaadman.m@qasquad.com'] | ['73424343322'] | [Row(title='Аскона', link='https://www.askona.ru', login='gildasdasdaadman.m@qasquad.com', password_hash='wdRSDMZTd62265f3bd5dc6c2f1411e602b1e3cf9')] |
```