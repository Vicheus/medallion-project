# Parsetron results

## About row data

> - File path: users_preprocessed.csv
> - Total rows: 182705

### Schema
```
root
 |-- name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- email: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- date: timestamp (nullable = true)
 |-- login: string (nullable = true)
 |-- pass: string (nullable = true)
 |-- address: string (nullable = true)

```

### Data sample
```
| name       |        phone | email   | ip                                      | date                | login   | pass   | address   |
|:-----------|-------------:|:--------|:----------------------------------------|:--------------------|:--------|:-------|:----------|
| Ольга      |   9198155325 |         | 178.45.36.96                            | 2022-04-20 06:01:32 |         |        |           |
| Buddha     |  89879550013 |         | 85.140.5.194                            | 2022-04-20 07:31:02 |         |        |           |
| Анна       | +79023562595 |         | 176.116.137.93                          | 2022-04-20 07:54:15 |         |        |           |
| Олег       |  89297052628 |         | 85.26.165.133                           | 2022-04-20 08:54:18 |         |        |           |
| Наталья    | +79226220276 |         | 85.192.157.185                          | 2022-04-20 09:44:29 |         |        |           |
| Жанна      |  89879709207 |         | 85.249.30.108                           | 2022-04-20 10:28:31 |         |        |           |
| Сергей     |  89277081709 |         | 46.29.78.84                             | 2022-04-20 11:03:23 |         |        |           |
| Илья       |  89379988200 |         | 2.95.234.183                            | 2022-04-20 11:07:13 |         |        |           |
| Алёна      | +79046012412 |         | 176.116.137.26                          | 2022-04-20 11:35:12 |         |        |           |
| Александра |  89021527187 |         | 143.244.44.179                          | 2022-04-20 11:39:56 |         |        |           |
| Вячеслав   |   9874534350 |         | 2a00:1fa1:c453:470d:79c1:2d93:6032:953b | 2022-04-20 12:15:42 |         |        |           |
| Елена      |  89228192877 |         | 85.249.30.85                            | 2022-04-20 15:37:43 |         |        |           |
| Ольга      |  89372581948 |         | 188.162.204.237                         | 2022-04-20 15:37:56 |         |        |           |
| Наталья    |  89276001616 |         | 46.0.56.36                              | 2022-04-20 15:54:43 |         |        |           |
| Юлия       | 89667800877  |         | 85.249.31.171                           | 2022-04-20 16:13:42 |         |        |           |
| Екатерина  |  89872011975 |         | 109.124.230.61                          | 2022-04-20 17:49:32 |         |        |           |
| Арина      |  89042034305 |         | 176.59.98.5                             | 2022-04-20 17:53:50 |         |        |           |
| Дарья      |  89279023405 |         | 46.0.174.47                             | 2022-04-20 17:55:49 |         |        |           |
| Ангелина   | +79996502448 |         | 109.124.224.164                         | 2022-04-20 21:25:09 |         |        |           |
| Инна       |  89277617376 |         | 109.124.192.100                         | 2022-04-21 07:21:30 |         |        |           |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: array (containsNull = true)
 |    |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: array (containsNull = true)
 |    |    |-- element: string (containsNull = false)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 82.33% |
| Phones | 98.36% |
| Ips | 16.38% |
| Accounts | 81.21% |
| Address | 0.05% |
| Actuality | 17.84% |



### Data sample
```
| names                            | emails                                | phones          | ips                                          | accounts                                                                                                                         | address   | actuality   |
|:---------------------------------|:--------------------------------------|:----------------|:---------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:----------|:------------|
| ['.Юрий']                        | [['delfin21014@yandex.ru']]           |                 |                                              |                                                                                                                                  |           |             |
| ['Adamec']                       | [['admeclukas@seznam.cz']]            | ['79819803775'] |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='admeclukas@seznam.cz', password='45973')]       |           |             |
| ['Agaev']                        | [['kazhenova_diana@mail.ru']]         | ['79873451430'] |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='Kazhenova_diana@mail.ru', password='61222')]    |           |             |
| ['Ahmad Hasarma']                |                                       | ['79176162275'] |                                              |                                                                                                                                  |           | 10.03.2022  |
| ['Aidenuy']                      | [['bakela2200@bumss.fun']]            |                 |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='bakela2200@bumss.fun', password='65258')]       |           |             |
| ['Aleeva']                       | [['timuraleev200890@gmail.com']]      | ['79020483295'] |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='timuraleev200890@gmail.com', password='20581')] |           |             |
| ['Alja']                         | [['alijusha97@mail.ru']]              |                 |                                              |                                                                                                                                  |           |             |
| ['Andriyanov Maksim Sergeevich'] |                                       | ['79677269485'] | [Row(ip='128.69.72.8', date='05.04.2022')]   |                                                                                                                                  |           | 05.04.2022  |
| ['Anna']                         |                                       | ['79879258984'] | [Row(ip='62.118.73.127', date='02.09.2022')] |                                                                                                                                  |           | 02.09.2022  |
| ['Antonina']                     | [['antonina.kolesnikova.89@mail.ru']] |                 |                                              |                                                                                                                                  |           |             |
| ['Arseniykr']                    | [['arsenisokol@yandex.ru']]           |                 |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='arsenisokol@yandex.ru', password='96400')]      |           |             |
| ['Artemhix']                     | [['artemtixe@mail.ru']]               |                 |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='artemtixe@mail.ru', password='29536')]          |           |             |
| ['Aнна']                         | [['shustowa.anyuta@yandex.ru']]       |                 |                                              |                                                                                                                                  |           |             |
| ['Baklan']                       | [['guignolo1984@gmail.com']]          | ['79873887816'] |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='guignolo1984@gmail.com', password='96676')]     |           |             |
| ['Bodina']                       | [['bodina.yelena@mail.ru']]           | ['79649680343'] |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='bodina.yelena@mail.ru', password='91889')]      |           |             |
| ['Brnfitdf']                     | [['nastia.56@yandex.ru']]             | ['79878675611'] |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='nastia.56@yandex.ru', password='79760')]        |           |             |
| ['Buddha']                       |                                       | ['79879550013'] | [Row(ip='85.140.5.194', date='20.04.2022')]  |                                                                                                                                  |           | 20.04.2022  |
| ['Bulanova']                     | [['anton.bulanov.82@mail.ru']]        | ['79276004122'] |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='anton.bulanov.82@mail.ru', password='48932')]   |           |             |
| ['Casinoxwrago']                 | [['privet1218@bigmir.net']]           |                 |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='privet1218@bigmir.net', password='59512')]      |           |             |
| ['Cjrjkjd']                      | [['n.o.sokolov111@mail.ru']]          | ['79619056660'] |                                              | [Row(title='Медицинская компания Моя Наука', link='https://naykalab.ru/', login='n.o.sokolov111@mail.ru', password='37411')]     |           |             |
```