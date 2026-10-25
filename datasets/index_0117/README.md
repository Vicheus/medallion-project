# Parsetron results

## About row data

> - Code name: index_0117
> - File path: /media/user/TRANSCEND/Databases/index_0117/raw/preprocessed/webleo_preprocessed_stage_2.csv
> - Total rows: 157572

### Schema
```
root
 |-- name1: string (nullable = true)
 |-- tel: string (nullable = true)
 |-- link: string (nullable = true)
 |-- email: string (nullable = true)
 |-- vk_id: string (nullable = true)
 |-- name2: string (nullable = true)
 |-- address: string (nullable = true)
 |-- inn: string (nullable = true)
 |-- passport: string (nullable = true)

```

### Data sample
```
| name1               | tel             | link                         | email   |     vk_id | name2                        | address                                                                            | inn   | passport   |
|:--------------------|:----------------|:-----------------------------|:--------|----------:|:-----------------------------|:-----------------------------------------------------------------------------------|:------|:-----------|
|                     |                 |                              |         |           |                              |                                                                                    |       |            |
| Маргарита Шафранова | -               | https://vk.com/manager_margo |         | 356450730 | я                            |                                                                                    |       |            |
| Елена Гусева        | 89216333931     | https://vk.com/id85600507    |         |  85600507 | Гусева Елена Николаевна      | 187555, обл Ленинградская, г. Тихвин, пл-ка. Усадьба РТС, д. 9, кв. 1              |       |            |
| Диана Андреева      | 89267129995     | https://vk.com/id197542359   |         | 197542359 | Рагимова Ксения Игоревна     | 123182, г. Москва, ул. Инженерная, д. 20, к. 1, кв. 5                              |       |            |
| Татьяна Пономарева  | 89068574209     | https://vk.com/id66101876    |         |  66101876 | Шевель Татьяна Геннадьевна   | 622049, обл Свердловская, г. Нижний Тагил, пр-кт. Октябрьский, д. 28, к. -, кв. 34 |       |            |
| Галина Рыбина       | 89028354472     | https://vk.com/g.rybina      |         |  15396825 | Рыбина Галина Михайловна     | 618122, край Пермский, г. Оса, ул. Гамицкая, д. 21 А, к. -, кв. -                  |       |            |
| Марина Ложкина      | 89223874464     | https://vk.com/marusyalo     |         |  66318114 | Ложкина Марина Николаевна    | 614058, край Пермский, г. Пермь, ул. Колхозная 1-я, д. 4, кв. 31                   |       |            |
| Альбина Тимина      | 8 922 910 78 66 | https://vk.com/id214533741   |         | 214533741 | Тимина Альбина Рауиловна     | 610901, обл Кировская, д. Барановщина, ул. Новая, д. 3, кв. 2                      |       |            |
| Юлия Трифонова      | 89066458787     | https://vk.com/id92816788    |         |  92816788 | Трифонова Юлия Александровна | 248002, обл Калужская, г. Калуга, ул. Степана Разина, д. 89, к. -, кв. 60          |       |            |
| Юленька Илянкина    | 89026088642     | https://vk.com/id3408105     |         |   3408105 | Илянкина Юлия Викторовна     | 456918, обл Челябинская, г. Сатка, ул. Парковая, д. 14А, кв. 13                    |       |            |
```


## About final data
> - Total rows: 156533

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
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
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Data sample
```
| names                                                | emails   | socials                                                                    | phones          | documents   | address                                                                          |
|:-----------------------------------------------------|:---------|:---------------------------------------------------------------------------|:----------------|:------------|:---------------------------------------------------------------------------------|
| ['Маргарита Шафранова']                              |          | [Row(title='Vk', id='manager_margo', link='https://vk.com/manager_margo')] |                 |             |                                                                                  |
| ['Елена Гусева', 'Гусева Елена Николаевна']          |          | [Row(title='Vk', id='id85600507', link='https://vk.com/id85600507')]       | ['79216333931'] |             | ['187555 обл Ленинградская г. Тихвин пл-ка. Усадьба РТС д. 9 кв. 1']             |
| ['Диана Андреева', 'Рагимова Ксения Игоревна']       |          | [Row(title='Vk', id='id197542359', link='https://vk.com/id197542359')]     | ['79267129995'] |             | ['123182 г. Москва ул. Инженерная д. 20 к. 1 кв. 5']                             |
| ['Татьяна Пономарева', 'Шевель Татьяна Геннадьевна'] |          | [Row(title='Vk', id='id66101876', link='https://vk.com/id66101876')]       | ['79068574209'] |             | ['622049 обл Свердловская г. Нижний Тагил пр-кт. Октябрьский д. 28 к. - кв. 34'] |
| ['Галина Рыбина', 'Рыбина Галина Михайловна']        |          | [Row(title='Vk', id='g.rybina', link='https://vk.com/g.rybina')]           | ['79028354472'] |             | ['618122 край Пермский г. Оса ул. Гамицкая д. 21 А к. - кв. -']                  |
| ['Марина Ложкина', 'Ложкина Марина Николаевна']      |          | [Row(title='Vk', id='marusyalo', link='https://vk.com/marusyalo')]         | ['79223874464'] |             | ['614058 край Пермский г. Пермь ул. Колхозная 1-я д. 4 кв. 31']                  |
| ['Альбина Тимина', 'Тимина Альбина Рауиловна']       |          | [Row(title='Vk', id='id214533741', link='https://vk.com/id214533741')]     | ['79229107866'] |             | ['610901 обл Кировская д. Барановщина ул. Новая д. 3 кв. 2']                     |
| ['Юлия Трифонова', 'Трифонова Юлия Александровна']   |          | [Row(title='Vk', id='id92816788', link='https://vk.com/id92816788')]       | ['79066458787'] |             | ['248002 обл Калужская г. Калуга ул. Степана Разина д. 89 к. - кв. 60']          |
| ['Юленька Илянкина', 'Илянкина Юлия Викторовна']     |          | [Row(title='Vk', id='id3408105', link='https://vk.com/id3408105')]         | ['79026088642'] |             | ['456918 обл Челябинская г. Сатка ул. Парковая д. 14А кв. 13']                   |
| ['Марианна Поткина']                                 |          | [Row(title='Vk', id='id214647477', link='https://vk.com/id214647477')]     |                 |             |                                                                                  |
```