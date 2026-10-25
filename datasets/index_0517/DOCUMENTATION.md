# Parsetron results

## About row data

> - File path: users.csv
> - Total rows: 1760

### Schema
```
root
 |-- email: string (nullable = true)
 |-- name: string (nullable = true)

```

### Data sample
```
| email                       | name                             |
|:----------------------------|:---------------------------------|
| kompleksarstroi@mail.ru     | Сидоров Александр Владимирович   |
| evg-sinelnikov@yandex.ru    | Синельников Евгений Викторович   |
| "79312322258@yandex.ru"     | "aleksandr"                      |
| "n.zherebtsov@vbh.ru"       | "Nikita"                         |
| "1111965@list.ru"           | "Sergei Makarov"                 |
| "tergspecservice@mail.ru"   | "Sergey"                         |
| "y.shishkina@vbh.ru"        | "Shishkina Yana"                 |
| "ds.lenovo@gmail.com"       | "vadim"                          |
| "zaurrahimli1971@gmail.com" | "Zaur"                           |
| "zarik9999@rambler.ru"      | "Zorikhin Alexander Nikolaevich" |
| krona-okna@mail.ru          | Абалихин Александр Сергеевич     |
| kpd-group.sale@mail.ru      | Абалова                          |
| abdrahimov.marat@mail.ru    | Абдрахимов Марат Ринатович       |
| abdumelov.vitaly@yandex.ru  | Абдумелов Виталий Николаевич     |
| abduhametovtoxa@gmail.com   | Абдухаметов тохирбек             |
| k.ablov@vbh.ru              | Аблов Константин Викторович      |
| fusion_ltd@mail.ru          | Абрамов Андрей Евгеньевич        |
| sts2011aff@yandex.ru        | Абузаров Фидус                   |
| dominant2019@yandex.ru      | Аванесян Александр               |
| maxim_1403@mail.ru          | Авдонин Максим Константинович    |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |



### Data sample
```
| names                             | emails                       |
|:----------------------------------|:-----------------------------|
| ['Кириллова Елена']               | ['plastik-trest@rambler.ru'] |
| ['Мальцев Сергей']                | ['89525771373@mail.ru']      |
| ['Сергей Анатольевич Тихонов']    | ['s_tihonov_77@mail.ru']     |
| ['Соколов Николай Игоревич']      | ['nik666666nik@bk.ru']       |
| ['Чурикова Светлана Валерьевна']  | ['snab@etp.one']             |
| ['Антон']                         | ['solohinanton@yandex.ru']   |
| ['Ирина Карабанова']              | ['snab2@sdobnov.ru']         |
| ['Красникова Юлия Александровна'] | ['yulya.kraseikova@mail.ru'] |
| ['Медведев Николай Сергеевич']    | ['nokna_post@mail.ru']       |
| ['Мельниченко Алексей Сергеевич'] | ['avangard.plys@mail.ru']    |
| ['Мильков']                       | ['amilkov02@mail.ru']        |
| ['Саватеев']                      | ['master_okon2023@bk.ru']    |
| ['Умные Двери']                   | ['torexsklad1@yandex.ru']    |
| ['Алексей Панов']                 | ['info@2-sklad.ru']          |
| ['Артемов']                       | ['best-plast@list.ru']       |
| ['Баркалова Елена Николаевна']    | ['omts@ecookna.ru']          |
| ['Давыдов Анатолий Анатольевич']  | ['shegay@knipping.ru']       |
| ['Елена Егоровна Щукина']         | ['lenasnabdom@mail.ru']      |
| ['Жолобов Артем Михайлович']      | ['a.zholobov@vbh.ru']        |
| ['Иванов Валерий Олегович']       | ['ivanov4mail@gmail.com']    |
```