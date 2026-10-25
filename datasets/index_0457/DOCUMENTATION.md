# Parsetron results

## About row data

> - File path: Магазин_одежды_Nice-one_26_02_2025.csv
> - Total rows: 25401

### Schema
```
root
 |-- Номер телефона: long (nullable = true)
 |-- Никнейм: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Почта: string (nullable = true)

```

### Data sample
```
|   Номер телефона | Никнейм                                     | ФИО                                | Почта                                      |
|-----------------:|:--------------------------------------------|:-----------------------------------|:-------------------------------------------|
|      78005553156 | Manager.artgk, pn_, pn_30065                | Неля, Неля Полухина, Полухина Неля | Manager.artgk@gmail.com, pn@artgk.ru       |
|      79806535555 | R.belousov                                  | Белоусов Роман                     | r.belousov@nice-one.ru                     |
|      79296764377 | 999966                                      | Тан Клим                           | 999966@mail.ru                             |
|      79163516077 | Ishishova                                   | Шишова Инна                        | Ishishova@bk.ru                            |
|      79652113045 | Fil1317                                     | Комлева Юлия                       | Fil1317@mail.ru                            |
|     380969861932 | romannesterenko87                           | Роман Нестеренко                   | romannesterenko87@gmail.com                |
|      79269521208 | zaytseva                                    | Anna Zaytseva                      | zaytseva@yandex.ru                         |
|      79851232132 | test                                        | Тест                               | test@test.ru                               |
|      79994411696 | volkwwww                                    | тест                               | volkwwww@gmail.com                         |
|     786665565555 | ira34                                       | Ира                                | ira34@mail.ru                              |
|     743555688887 | mari2124                                    | Маша                               | mari2124@mail.ru                           |
|      78694556444 | test7456                                    | Тест                               | Test@mail.ru                               |
|       7889997766 | 222                                         | 1111                               | 222@jldsjf.ru                              |
|    7896566575656 | ira                                         | Ира                                | ira@mail.ru                                |
|      79161221717 | inessa_and                                  | Инесса                             | inessa_and@mail.ru                         |
|     776568877565 | admin33493                                  | Администратор сайта                | admin@mail.ru                              |
|     776456454565 | admin1                                      | аминистратор сайта                 | admin1@mail.ru                             |
|      79057733666 | Verakush92, Verakush9226938, veraalmamedova | Вера, Вера Алмамедова              | Verakush92@mail.ru, veraalmamedova@mail.ru |
|      79163299743 | NellyF4815, NellyF481532277, NellyF48158752 | Моисеева Наиля                     | NellyF4815@yandex.ru                       |
|      79167721686 | prittykitty                                 | Наруцкая Екатерина                 | prittykitty@yandex.ru                      |
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
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 98.37% |
| Phones | 98.70% |
| Raw_metadata | 99.99% |



### Data sample
```
| names                                           | emails                         | phones          | raw_metadata                                              |
|:------------------------------------------------|:-------------------------------|:----------------|:----------------------------------------------------------|
| ['Ekaterina Listovskaya']                       | ['listovskaya_ek@outlook.com'] | ['79032069027'] | ['{"Никнейм": "listovskayaek"}']                          |
| ['Ekaterina Zagorodnyaya Загородняя Екатерина'] | ['ezagorodniaia@gmail.com']    | ['79031640008'] | ['{"Никнейм": "ezagorodniaia ezagorodniaia46391"}']       |
| ['Азиза Нармамедова']                           | ['aziza.89@inbox.ru']          | ['79772619395'] | ['{"Никнейм": "aziza.89"}']                               |
| ['Александра Игоревна']                         | ['alexandrachrnv@gmail.com']   | ['79636864748'] | ['{"Никнейм": "alexandrachrnv"}']                         |
| ['Александра Пильчина']                         | ['sasha777moisey@gmail.com']   | ['79629145461'] | ['{"Никнейм": "sasha777moisey20643 sasha777moisey3403"}'] |
| ['Амирзадова Алина']                            | ['amirzadova_alina@mail.ru']   | ['79096871667'] | ['{"Никнейм": "amirzadovaalina"}']                        |
| ['Анастасия']                                   | ['atrepolovskaa@gmail.com']    | ['79153517328'] | ['{"Никнейм": "79153517328"}']                            |
| ['Анастасия Мокрова']                           | ['mokrovochka@mail.ru']        | ['79175258565'] | ['{"Никнейм": "mokrovochka"}']                            |
| ['Андрианова Анна']                             | ['andrianova-anna@bk.ru']      | ['79169595205'] | ['{"Никнейм": "Andrianova-Anna"}']                        |
| ['Андриенко Мария']                             | ['world-post@bk.ru']           | ['79219618271'] | ['{"Никнейм": "World-post"}']                             |
| ['Аро Паро']                                    | ['asdf@sdf.ru']                | ['79234543254'] | ['{"Никнейм": "asdf"}']                                   |
| ['Артемьева Екатерина']                         | ['artemevakiki@mail.ru']       |                 | ['{"Никнейм": "artemevakiki"}']                           |
| ['Афонина Юлия']                                | ['julyfox97@mail.ru']          | ['79013457701'] | ['{"Никнейм": "julyfox97"}']                              |
| ['Белинская Виктория']                          | ['v.belinskaya@inbox.ru']      | ['79267508286'] | ['{"Никнейм": "v.belinskaya"}']                           |
| ['Белова Юлия']                                 | ['belova.yuliya.98@mail.ru']   | ['79301057173'] | ['{"Никнейм": "belova.yuliya.98"}']                       |
| ['Беляева']                                     | ['nbeliaeva@inbox.ru']         | ['79025550355'] | ['{"Никнейм": "nbeliaeva"}']                              |
| ['Березовский Вячеслав']                        | ['slaval.69@mail.ru']          | ['79135043406'] | ['{"Никнейм": "slaval.69"}']                              |
| ['Воробьева Елена']                             | ['valya_ya_zhno@mail.ry']      | ['79683618948'] | ['{"Никнейм": "Valyayazhno"}']                            |
| ['Вяткина Юлия']                                | ['vyatkinajulia@gmail.com']    | ['79161265803'] | ['{"Никнейм": "JuliV"}']                                  |
| ['Габриелян Лилит']                             | ['lilitgabriel1@gmail.com']    | ['79647227505'] | ['{"Никнейм": "lilitgabriel1"}']                          |
```