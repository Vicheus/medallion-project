# Parsetron results

## About row data

> - Code name: index_0014
> - File path: Yandex Praktikum Part.txt
> - Total rows: 300000

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- yauid: integer (nullable = true)
 |-- username: string (nullable = true)
 |-- email: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- phone_number: long (nullable = true)

```

### Data sample
```
|   id |       yauid | username                                  | email                                     | first_name   | last_name      |   phone_number |
|-----:|------------:|:------------------------------------------|:------------------------------------------|:-------------|:---------------|---------------:|
|   20 |   281067418 | vozgbm                                    | vozgbm@yandex.ru                          | Alexander    | Basov          |    7.90039e+10 |
|   21 |     9647938 | ardor                                     | ardor@yandex.ru                           | Евгений      | Лебедев        |    7.92553e+10 |
|   22 |   289999235 | pavelpbeta                                | pavelpbeta@yandex.by                      | Павел        | Пугач          |    3.75294e+11 |
|   23 |   282400888 | atnesness                                 | atnesness@yandex.ru                       | Artem        | Nesmianov      |    7.91268e+10 |
|   24 |   797072976 | eremin4nton                               | eremin4nton@yandex.ru                     | Антон        | Еремин         |    7.91621e+10 |
|   25 |   355001046 | sashabratchikov1                          | sashabratchikov1@yandex.ru                | Sasha        | Bratchikov     |    7.90463e+10 |
|   26 |   482938063 | stpnkv                                    | stpnkv@yandex.ru                          | Александр    | Ступников      |    7.92509e+10 |
|   27 |      364096 | treg                                      | treg@yandex.ru                            | Александр    | Трегер         |    7.92639e+10 |
|   28 | -1576022344 | pa7lux@kruzhok.io                         | pa7lux@kruzhok.io                         | Alexander    | Patlukh        |    7.91696e+10 |
|   29 |   718167381 | edutest42                                 | edutest42@yandex.ru                       | Кагоцел      | Оциллококцинов |    7.91643e+10 |
|   30 |   797321247 | anton4eremin                              | anton4eremin@yandex.ru                    | Антон        | Ереми          |    7.91621e+10 |
|   31 |   531295415 | doomzzd                                   | DoomzzD@yandex.ru                         | Алексей      | Коряков        |    7.98503e+10 |
|   32 |   318872247 | ya-sergeikudinov                          | ya.sergeikudinov@yandex.ru                | Sergei       | Kudinov        |    7.92633e+10 |
|   33 |   201327734 | utterstep                                 | utterstep@yandex.ru                       | Владислав    | Степанов       |    7.91628e+10 |
|   34 |   204307338 | yndx-iakolzin                             | yndx.iakolzin@yandex.ru                   | Илья         | Акользин       |    7.91643e+10 |
|   35 |   196297546 | dlccc4596                                 | dlccc4596@yandex.ru                       | Евгений      | Плотников      |    7.91284e+10 |
|   36 |   241593105 | yndx-ealebedev                            | yndx-ealebedev@yandex.ru                  | ealebedev    | Директ         |    7.92553e+10 |
|   38 |    99374674 | sofia-tex                                 | sofia.tex@yandex.ru                       | София        | Техажева       |    7.91542e+10 |
|   39 |   487366817 | serzhooooo                                | serzhooooo@yandex.ru                      | Sergey       | Parfenov       |    7.96479e+10 |
|   40 | -1567290340 | opashkovskaya@productschool.yaconnect.com | opashkovskaya@productschool.yaconnect.com | Олеся        | Пашковская     |  nan           |
```


## About final data
> - Total rows: 294672

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 77.28% |
| Emails | 99.99% |
| Accounts | 100.00% |



### Data sample
```
| names                      | phones          | emails                                        | accounts                                                                                                                                 |
|:---------------------------|:----------------|:----------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| ['Basov Alexander']        | ['79003887228'] | ['vozgbm@yandex.ru']                          | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='vozgbm', id='281067418')]                                      |
| ['Лебедев Евгений']        | ['79255331319'] | ['ardor@yandex.ru']                           | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='ardor', id='9647938')]                                         |
| ['Пугач Павел']            |                 | ['pavelpbeta@yandex.by']                      | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='pavelpbeta', id='289999235')]                                  |
| ['Nesmianov Artem']        | ['79126797696'] | ['atnesness@yandex.ru']                       | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='atnesness', id='282400888')]                                   |
| ['Еремин Антон']           | ['79162061502'] | ['eremin4nton@yandex.ru']                     | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='eremin4nton', id='797072976')]                                 |
| ['Bratchikov Sasha']       | ['79046336121'] | ['sashabratchikov1@yandex.ru']                | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='sashabratchikov1', id='355001046')]                            |
| ['Ступников Александр']    | ['79250904571'] | ['stpnkv@yandex.ru']                          | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='stpnkv', id='482938063')]                                      |
| ['Трегер Александр']       | ['79263937934'] | ['treg@yandex.ru']                            | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='treg', id='364096')]                                           |
| ['Patlukh Alexander']      | ['79169591695'] | ['pa7lux@kruzhok.io']                         | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='pa7lux@kruzhok.io', id='-1576022344')]                         |
| ['Оциллококцинов Кагоцел'] | ['79164308522'] | ['edutest42@yandex.ru']                       | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='edutest42', id='718167381')]                                   |
| ['Ереми Антон']            | ['79162061502'] | ['anton4eremin@yandex.ru']                    | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='anton4eremin', id='797321247')]                                |
| ['Коряков Алексей']        | ['79850301621'] | ['doomzzd@yandex.ru']                         | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='doomzzd', id='531295415')]                                     |
| ['Kudinov Sergei']         | ['79263264722'] | ['ya.sergeikudinov@yandex.ru']                | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='ya-sergeikudinov', id='318872247')]                            |
| ['Степанов Владислав']     | ['79162791330'] | ['utterstep@yandex.ru']                       | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='utterstep', id='201327734')]                                   |
| ['Акользин Илья']          | ['79164308522'] | ['yndx.iakolzin@yandex.ru']                   | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='yndx-iakolzin', id='204307338')]                               |
| ['Плотников Евгений']      | ['79128379768'] | ['dlccc4596@yandex.ru']                       | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='dlccc4596', id='196297546')]                                   |
| ['Директ Ealebedev']       | ['79255331319'] | ['yndx-ealebedev@yandex.ru']                  | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='yndx-ealebedev', id='241593105')]                              |
| ['Техажева София']         | ['79154162716'] | ['sofia.tex@yandex.ru']                       | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='sofia-tex', id='99374674')]                                    |
| ['Parfenov Sergey']        | ['79647942003'] | ['serzhooooo@yandex.ru']                      | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='serzhooooo', id='487366817')]                                  |
| ['Пашковская Олеся']       |                 | ['opashkovskaya@productschool.yaconnect.com'] | [Row(title='Яндекс практикум', link='https://practicum.yandex.ru', login='opashkovskaya@productschool.yaconnect.com', id='-1567290340')] |
```