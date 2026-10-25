# Parsetron results

## About row data

> - File path: spiritfit.ru - @StormBaseAdapter.txt
> - Total rows: 77253

### Schema
```
root
 |-- Phone: long (nullable = true)
 |-- Name: string (nullable = true)
 |-- Email: string (nullable = true)

```

### Data sample
```
|       Phone | Name               | Email                     |
|------------:|:-------------------|:--------------------------|
| 79859977057 | Светлана           | svetlana-a222@mail.ru     |
| 79262250630 | Аарламова Регина   | regi6kaone@mail.ru        |
| 79252148307 | Абабий  Адриана    | adrianna.ababii03@mail.ru |
| 79859959774 | Абаев Евгений      | evgenuch2@yandex.ru       |
| 79696753015 | Абаева Дана        | aminagigi0@mail.ru        |
| 79372137602 | Абаза Екатерина    | hoom18@mail.ru            |
| 79257179534 | Абазалиев Алим     | mr.abazaliev@bk.ru        |
| 79287238097 | Абазов Алим        | abazov2001@icloud.com     |
| 79684150001 | Абазов Беслан      | beslan-abazov@yandex.ru   |
| 79161998750 | Абазов Мурат       | doberman-amh@yandex.ru    |
| 79040614312 | Абазов Руслан      | rus.abazov.99@mail.ru     |
| 79153176229 | Абазян Ашот        | a.abazyan@bk.ru           |
| 79779149392 | Абай               |                           |
| 79096356144 | Абай               |                           |
| 79166592585 | Абай               |                           |
| 79309374761 | Абай               |                           |
| 79060660660 | Абакар             | 4ebaksar90@gmail.com      |
| 79017560665 | Абакар             |                           |
| 79896579799 | Абакаров Джанболат | 7867871zaw@mail.ru        |
| 79316661111 | Абакарова  Оксана  | kurban.oksana24@mail.ru   |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 99.97% |
| Emails | 59.47% |



### Data sample
```
| names                  | phones          | emails                        |
|:-----------------------|:----------------|:------------------------------|
| ['Светлана']           | ['79859977057'] | ['svetlana-a222@mail.ru']     |
| ['Аарламова Регина']   | ['79262250630'] | ['regi6kaone@mail.ru']        |
| ['Абабий Адриана']     | ['79252148307'] | ['adrianna.ababii03@mail.ru'] |
| ['Абаев Евгений']      | ['79859959774'] | ['evgenuch2@yandex.ru']       |
| ['Абаева Дана']        | ['79696753015'] | ['aminagigi0@mail.ru']        |
| ['Абаза Екатерина']    | ['79372137602'] | ['hoom18@mail.ru']            |
| ['Абазалиев Алим']     | ['79257179534'] | ['mr.abazaliev@bk.ru']        |
| ['Абазов Алим']        | ['79287238097'] | ['abazov2001@icloud.com']     |
| ['Абазов Беслан']      | ['79684150001'] | ['beslan-abazov@yandex.ru']   |
| ['Абазов Мурат']       | ['79161998750'] | ['doberman-amh@yandex.ru']    |
| ['Абазов Руслан']      | ['79040614312'] | ['rus.abazov.99@mail.ru']     |
| ['Абазян Ашот']        | ['79153176229'] | ['a.abazyan@bk.ru']           |
| ['Абай']               | ['79779149392'] |                               |
| ['Абай']               | ['79096356144'] |                               |
| ['Абай']               | ['79166592585'] |                               |
| ['Абай']               | ['79309374761'] |                               |
| ['Абакар']             | ['79060660660'] | ['4ebaksar90@gmail.com']      |
| ['Абакар']             | ['79017560665'] |                               |
| ['Абакаров Джанболат'] | ['79896579799'] | ['7867871zaw@mail.ru']        |
| ['Абакарова Оксана']   | ['79316661111'] | ['kurban.oksana24@mail.ru']   |
```