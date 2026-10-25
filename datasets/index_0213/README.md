# Parsetron results

## About row data

> - Code name: index_0213
> - File path: /media/user/SAMSUNG/Databases/index_0213/raw/erc_ecb_ru.csv
> - Total rows: 155498

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- Адрес: string (nullable = true)

```

### Data sample
```
| ФИО                             | Почта                     | Номер телефона     | Адрес                                                                      |
|:--------------------------------|:--------------------------|:-------------------|:---------------------------------------------------------------------------|
| Александр Толосейчук            | hell@index-art.ru         |                    |                                                                            |
| Инна Гуревич                    |                           |                    |                                                                            |
| Алексей Крепов                  | hellushka@mail.ru         |                    |                                                                            |
| gjgjgjg                         | aaaa                      |                    |                                                                            |
| Щигарцова Оксана Игоревна       | L.okc@mail.ru             |                    |                                                                            |
| Шишло Валерий Иосифович         | hotel@ricap.ru            | 79222084477        |                                                                            |
| Кайгородов Александр Васильевич | freepointers@olympus.ru   |                    |                                                                            |
| Ким Н.П.                        | bannikova_olga@mail.ru    | 2959850            | Готвальда, 19б-158                                                         |
| Михайлов Максим Юрьевич         | fentome@olympus.ru        |                    |                                                                            |
| горячевских                     | nica_vkh@mail.ru          | 73436126160        | Свердловская область Слободо-Туринский район с.Ницинское ул.Советская д 35 |
| Куклина М.В.                    | sci51@kodapost.ru         |                    |                                                                            |
| Зиновьев А.Н.                   | natali@nexcom.ru          |                    |                                                                            |
| Бредихина Марина Викторовна     | Ultra-Marin1409@yandex.ru | 79028764347        |                                                                            |
| Смагина Алия                    | Aliya@e1.ru               |                    |                                                                            |
| Букатина Елена Юрьевна          | oper@uralpost.ru          | 2408649            |                                                                            |
| Флейтлих Ольга Юрьевна          | flaute@mail.ru            |                    |                                                                            |
| Романова                        | roma_555_5@mail.ru        |                    |                                                                            |
| Коновалова Елена Анатольевна    | eugenik@uralweb.ru        |                    |                                                                            |
| Пуртов Игорь Сергеевич          | Igor_p@e1.ru              | 2467768,9028714804 | Рабочих 9-62                                                               |
| Овечкина                        | olgastnk@rambler.ru       | 79126705208        |                                                                            |
```


## About final data
> - Total rows: 154988

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Data sample
```
| names                               | emails                        | phones          | address                                                                        |
|:------------------------------------|:------------------------------|:----------------|:-------------------------------------------------------------------------------|
| ['Александр Толосейчук']            | ['hell@index-art.ru']         |                 |                                                                                |
| ['Алексей Крепов']                  | ['hellushka@mail.ru']         |                 |                                                                                |
| ['Щигарцова Оксана Игоревна']       | ['l.okc@mail.ru']             |                 |                                                                                |
| ['Шишло Валерий Иосифович']         | ['hotel@ricap.ru']            | ['79222084477'] |                                                                                |
| ['Кайгородов Александр Васильевич'] | ['freepointers@olympus.ru']   |                 |                                                                                |
| ['Ким Н.П.']                        | ['bannikova_olga@mail.ru']    |                 | ['Готвальда 19б-158']                                                          |
| ['Михайлов Максим Юрьевич']         | ['fentome@olympus.ru']        |                 |                                                                                |
| ['Горячевских']                     | ['nica_vkh@mail.ru']          | ['73436126160'] | ['Свердловская область Слободо-Туринский район с.Ницинское ул.Советская д 35'] |
| ['Куклина М.В.']                    | ['sci51@kodapost.ru']         |                 |                                                                                |
| ['Зиновьев А.Н.']                   | ['natali@nexcom.ru']          |                 |                                                                                |
| ['Бредихина Марина Викторовна']     | ['ultra-marin1409@yandex.ru'] | ['79028764347'] |                                                                                |
| ['Смагина Алия']                    | ['aliya@e1.ru']               |                 |                                                                                |
| ['Букатина Елена Юрьевна']          | ['oper@uralpost.ru']          |                 |                                                                                |
| ['Флейтлих Ольга Юрьевна']          | ['flaute@mail.ru']            |                 |                                                                                |
| ['Романова']                        | ['roma_555_5@mail.ru']        |                 |                                                                                |
| ['Коновалова Елена Анатольевна']    | ['eugenik@uralweb.ru']        |                 |                                                                                |
| ['Пуртов Игорь Сергеевич']          | ['igor_p@e1.ru']              |                 | ['Рабочих 9-62']                                                               |
| ['Овечкина']                        | ['olgastnk@rambler.ru']       | ['79126705208'] |                                                                                |
| ['Ашкинадзе Сергей Валерьевич']     | ['hitrec@e1.ru']              | ['79090180218'] |                                                                                |
| ['Ежов Антон Сергеевич']            | ['tatyaezh@yandex.ru']        |                 |                                                                                |
```