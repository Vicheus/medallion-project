# Parsetron results

## About row data

> - Code name: index_0186
> - File path: petitions.by - @bereza_bd.csv
> - Total rows: 208893

### Schema
```
root
 |-- name: string (nullable = true)
 |-- phone: long (nullable = true)
 |-- email: string (nullable = true)
 |-- date: string (nullable = true)
 |-- adress: string (nullable = true)
 |-- _c5: string (nullable = true)

```

### Data sample
```
| name                             |         phone | email                              | date                | adress                                                   | _c5   |
|:---------------------------------|--------------:|:-----------------------------------|:--------------------|:---------------------------------------------------------|:------|
| МАТВИЮК РУСЛАН                   | nan           | MATVIUKRUSLAN28@GMAIL.COM          | 2021-02-02 19:49:17 |                                                          |       |
| ЛАПИЦКИЙ АНДРЕЙ ЮРЬЕВИЧ          |   3.75296e+11 | MR.LAPIAN@GMAIL.COM                | 2020-12-08 19:19:32 | Г. МИНСК БЕЛОМОРСКАЯ 21 КВ.69                            |       |
| МАКАРЕНКО РИНА                   | nan           | ARINA.MAKARENKO.2003@MAIL.RU       | 2020-05-24 19:11:17 |                                                          |       |
| ГРИШКОВ АЛЕКСАНДР ВЛАДИМИРОВИЧ   |   3.75297e+11 | ALEXANDR.V.GRISHKOV@GMAIL.COM      | 2021-01-30 18:18:58 | МИНСКАЯ ОБЛ. МИНСКИЙ Р-Н Д. ЖДАНОВИЧИ ПОЛЕВАЯ 23 КВ.42   |       |
| ПАНЬКОВ ДМИТРИЙ                  | nan           | PDG@TUT.BY                         | 2020-04-14 10:22:45 |                                                          |       |
| KRISTINA                         | nan           | KIVACUKKRISTINA@GMAIL.COM          | 2020-05-23 22:58:23 |                                                          |       |
| БОРОДАВКО АНТОН ВЛАДИМИРОВИЧ     |   3.753e+11   | ANTON.B-METEOR@MAIL.RU             | 2021-04-17 07:50:33 | ЧАПАЕВА 24 КВ.72                                         |       |
| FARINO ART                       | nan           | FARINO.A.A@YANDEX.RU               | 2021-01-30 09:52:49 |                                                          |       |
| АНДРЕЕВ ВЛАДИМИР НИКОЛАЕВИЧ      |   3.75296e+11 | H3S9@MAIL.RU                       | 2021-04-17 13:14:21 | Г. МИНСК УЛИЦА БАГРАТИОНА 71 КВ.3                        |       |
| ЧЕРНЯК АЛЕКСАНДР ГЕННАДЬЕВИЧ     |   3.75447e+11 | SASHA_CHERNYAK@BK.RU               | 2021-01-31 17:09:05 | БРЕСТСКАЯ ОБЛ. Г. БАРАНОВИЧИ ЗВЁЗДНАЯ 18                 |       |
| ШАТЮК АННА ДМИТРИЕВНА            |   3.75293e+11 | DOBRAJA23@GMAIL.COM                | 2020-04-02 13:53:28 | ГРОДНЕНСКАЯ ОБЛ. Г. ЛИДА 8 МАРТА 16                      |       |
|                                  | nan           |                                    | 2021-01-30 10:42:54 |                                                          |       |
| ЧИСТОВ СЕРГЕЙ ВАЛЕРЬЕВИЧ         |   3.75296e+11 | CHISTOU2@GMAIL.COM                 | 2021-02-08 12:07:45 | Г. МИНСК ЛЮБИМОВА 33 КВ.75                               |       |
| КУЛИКОВА ОЛЬГА                   | nan           | 7022212@GMAIL.COM                  | 2021-01-31 00:45:49 |                                                          |       |
| СУХИНИНА ОЛЬГА                   | nan           | OLI.SUHININA@GMAIL.COM             | 2021-02-01 16:59:24 |                                                          |       |
| КРЕЧИК СЕРГЕЙ НИКОЛАЕВИЧ         |   3.75291e+11 | KRECHIK_S@MAIL.RU                  | 2020-06-20 16:03:12 | МИНСКАЯ ОБЛ. МИНСКИЙ Р-Н П. ЛЕСНОЙ АЛЕКСАНДРОВА 1 КВ.263 |       |
| ЯШИН АЛЕКСАНДР НИКОЛАЕВИЧ        |   3.75291e+11 | ALEXANDERYASHIN2020EXTRA@GMAIL.COM | 2021-01-30 14:31:16 | Г. МИНСК БУЛЬВАР ШЕВЧЕНКО 7 КВ.10                        |       |
| ГЕРАСИМЁНОК ОКСАНА АЛЕКСАНДРОВНА |   3.75297e+11 | OKSANA.GERASIMIONOK@GMAIL.COM      | 2020-06-21 15:25:19 | Г. МИНСК ЛОГОЙСКИЙ ТРАКТ 11 КВ.162                       |       |
| РАДЬКОВ АНДРЕЙ ДМИТРИЕВИЧ        |   3.75298e+11 | ADR242@GMAIL.COM                   | 2020-05-25 14:41:50 | Г. МИНСК ЧАЙЛЫТКО 1 КВ.96                                |       |
| ДАУРОВА СВЕТЛАНА                 | nan           | IRONMAM@RAMBLER.RU                 | 2021-02-04 16:47:49 |                                                          |       |
```


## About final data
> - Total rows: 203742

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 47.97% |
| Emails | 99.97% |
| Address | 52.74% |
| Actuality | 100.00% |



### Data sample
```
| names                     | phones   | emails                               | address   | actuality   |
|:--------------------------|:---------|:-------------------------------------|:----------|:------------|
| ['A Aleksander']          |          | ['shumskia@gmail.com']               |           | 01.02.2021  |
| ['A Anna']                |          | ['annanuta8@gmail.com']              |           | 03.01.2021  |
| ['A Anna']                |          | ['littleannny@gmail.com']            |           | 31.01.2021  |
| ['A D']                   |          | ['ave9706@gmail.com']                |           | 05.02.2021  |
| ['A Davno']               |          | ['denni334334@gmail.com']            |           | 03.01.2021  |
| ['A Helen']               |          | ['lenok138695@gmail.com']            |           | 19.05.2020  |
| ['A Karm']                |          | ['kseniatarashkevich1107@gmail.com'] |           | 22.05.2020  |
| ['A Maksim']              |          | ['belarusakva@gmail.com']            |           | 31.01.2021  |
| ['A Redmi']               |          | ['ar8785736@gmail.com']              |           | 30.01.2021  |
| ['A S']                   |          | ['sergey.avtonenko@gmail.com']       |           | 10.10.2020  |
| ['A Tati']                |          | ['art7t7t@gmail.com']                |           | 16.05.2020  |
| ['A Yuri']                |          | ['avlasevich@gmail.com']             |           | 30.01.2021  |
| ['A Алексей']             |          | ['woodman.minsk@gmail.com']          |           | 30.01.2021  |
| ['A Антон']               |          | ['bsranton@gmail.com']               |           | 03.02.2021  |
| ['A Наталья']             |          | ['glueksfee@mail.ru']                |           | 22.06.2020  |
| ['A Юрий']                |          | ['mgyura11@gmail.com']               |           | 16.04.2020  |
| ['Abaddon']               |          | ['yuriyskullvasilevich@gmail.com']   |           | 30.01.2021  |
| ['Abashkin Viktar']       |          | ['viktar.abashkin@gmail.com']        |           | 30.01.2021  |
| ['Abjava By Doka Abjava'] |          | ['abjava.by@gmail.com']              |           | 30.01.2021  |
| ['Aboud Svetlana']        |          | ['sveta.aboud63@gmail.com']          |           | 15.08.2020  |
```