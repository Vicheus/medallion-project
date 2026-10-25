# Parsetron results

## About row data

> - Code name: index_0819
> - File path: vinum_users.csv
> - Total rows: 570847

### Schema
```
root
 |-- id: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- email_verified: string (nullable = true)
 |-- discount_percent: string (nullable = true)
 |-- orders_count: string (nullable = true)

```

### Data sample
```
|   id | first_name   | email                           |       phone | email_verified   |   discount_percent |   orders_count |
|-----:|:-------------|:--------------------------------|------------:|:-----------------|-------------------:|---------------:|
|    1 | Римма        | rimma.star.2002@gmail.com       | 79655861383 | true             |                  5 |              0 |
|    2 | Екатерина    | seifulowa@yandex.ru             | 79869479837 | true             |                  5 |              0 |
|    3 | мария        | mariya.tolkacheva2003@gmail.com | 79020473034 | true             |                 15 |             12 |
|    4 | Елена        | korenyako.elena@gmail.com       | 79103510685 | true             |                  5 |              0 |
|    5 | Дмитрий      | teplov.dimas@bk.ru              | 79823633808 | true             |                  5 |              0 |
|    6 | Кирилл       | kirillmesherinov@gmail.com      | 79875252328 | true             |                  5 |              0 |
|    7 | Cholpon      | cholpan-jumashova@ramplen.ru    | 79125052267 | true             |                 15 |             15 |
|    8 | Ольга        | Lelyas85@inbox.ru               | 79167268015 | true             |                  5 |              0 |
|    9 | Ринат        | lyaushinr@icloud.com            | 79875214761 | true             |                  5 |              0 |
|   10 | Ekaterina    | katerina.gavrilkevich@gmail.com | 79211520441 | true             |                 15 |              7 |
|   11 | Лилиана      | lil.bobkova@yandex.ru           | 79251406778 | true             |                 15 |             19 |
|   12 | Maksim       | maxsuraev123@gmail.com          | 79297012840 | true             |                  5 |              3 |
|   13 | Екатерина    | kropotova_03@mail.ru            | 79787533602 | true             |                  5 |              0 |
|   14 | Эльвира      | valeeva_80@mail.ru              | 79502036153 | true             |                 15 |              9 |
|   15 | Валерия      | leraakulova7716@gmail.com       | 79613549053 | true             |                 15 |              9 |
|   16 | михаил       | misha.starkov.99@mail.ru        | 79871509895 | true             |                  5 |              1 |
|   17 | евгения      | Gazheka@yandex.ru               | 79858054265 | true             |                 15 |             10 |
|   18 | анна         | mama_love_2016@mail.ru          | 79248430348 | true             |                 15 |             10 |
|   19 | лейвик       | lev.kilinka@yandex.ru           | 79245117116 | true             |                 25 |             52 |
|   20 | Елизавета    | kriklivaia.liza@mail.ru         | 79378052390 | true             |                  5 |              0 |
```


## About final data
> - Total rows: 560824

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 99.97% |
| Emails | 99.97% |
| Source_entity_id | 100.00% |



### Data sample
```
| names         | phones          | emails                                 | source_entity_id                                         |
|:--------------|:----------------|:---------------------------------------|:---------------------------------------------------------|
| ['Наталья']   | ['79030837831'] | ['tyusheva14@yandex.ru']               | 002d3f6ad5b2acfc1e29375c491a57389312a9abf1a24c7e75dc5546 |
| ['Ольга']     | ['79867907800'] | ['karp0v4.svet@yandex.ru']             | 004ec2c55a48aa937fdb59912edbaca4348544dc5e198999141d517d |
| ['Елена']     | ['79286009080'] | ['moliblum@yandex.ru']                 | 00525df12efdb92215bb119da75a47025bd51075284c753ee911616e |
| ['Ирина']     | ['79831272188'] | ['irina.bondar899@gmail.com']          | 007b3196fc5c429cca11f8d4f911049b3b3e70ff44024db064b408f8 |
| ['Дмитрий']   | ['79026365060'] | ['tda64@mail.ru']                      | 008de5f3c4b7018fdab4016e96dafeb958fa363a0ba66843ef18fa98 |
| ['Артем']     | ['79200413305'] | ['gavrilov-83@mail.ru']                | 00f540365e546fc4a5ec9aa1553694ecf774367d101f0b943373ec30 |
| ['Сергей']    | ['79647159823'] | ['sergey_386@mail.ru']                 | 00f77eff6a04805105480615f04b7db940e7652545a699f48565c26e |
| ['Ekaterina'] | ['79202668461'] | ['skarlett.2010@mail.ru']              | 00f89365d0a31673ac1aa410d1202de48b3084c74072b2f0e8a1e635 |
| ['Tatyana']   | ['79081329267'] | ['fatsiy@mail.ru']                     | 01064f85826d03dcbd8f3050192a66d01e1bfcd047c95f9f03fd59c5 |
| ['Валерия']   | ['79216434960'] | ['shendrikv@yandex.ru']                | 010b013ccffb643d23cfda0c4438ef3aef26b773fd2ff5df1f2d4156 |
| ['Сергей']    | ['79192156370'] | ['spsviridov@mail.ru']                 | 012bdbd673cf58aa3a401c59cbea1b956d87053dadf256c757123bc5 |
| ['Антонина']  | ['79505731472'] | ['a.prokydina2014@yandex.ru']          | 01533c2aeff644e1eeb97aa779254255e03fb51e146ae648de869117 |
| ['Elena']     | ['79182866386'] | ['order-209541653@insmail3.sravni.ru'] | 01548843d9ced0b6b24d68d7c5a6543852dbaffdf5a7fe2aa5f17cec |
| ['Дмитрий']   | ['79027699696'] | ['melentevna@rambler.ru']              | 01555f8bcf8d598f26ae51bb541d3754ec0ccf620100f54bbad7cc56 |
| ['Алексей']   | ['79136229797'] | ['papay2122@yandex.ru']                | 015873268901c088bb4ac27c09ba6d872a0a0b37c39bfdc9c43a3ed1 |
| ['Denis']     | ['79262207373'] | ['tuzoff@mail.ru']                     | 0159fc682d51b980784ef72b513a84a4c0e8e58cb67a85222e470c95 |
| ['Игорь']     | ['79108837341'] | ['tkachenkoigor22@gmail.com']          | 0182232b011aceb2c4fae6994227b67cf24be129965eda31afebfc95 |
| ['Алина']     | ['79254914775'] | ['asalina2511@gmail.com']              | 01824189ca8deb3d1f22510d79f7a40a8d4fe764545fdfddef100294 |
| ['Наталия']   | ['79807248453'] | ['lapa221222@gmail.com']               | 0194a4b0a15c07e2f16e9dc69778326a1f4958dc7922b91b00b89c03 |
| ['Алексей']   | ['79806568997'] | ['ermolaevala0909@gmail.com']          | 01997e53b91375f14f1a8502174ccc1a7aa33af8f78c60f77c107a25 |
```