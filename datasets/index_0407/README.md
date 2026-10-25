# Parsetron results

## About row data

> - Code name: index_0407
> - File path: clients_aspro_mobi_10k.csv
> - Total rows: 19306

### Schema
```
root
 |-- name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- email: string (nullable = true)
 |-- manager: string (nullable = true)
 |-- edrpou: string (nullable = true)

```

### Data sample
```
| name                | phone             | email                         | manager           |   edrpou |
|:--------------------|:------------------|:------------------------------|:------------------|---------:|
| Надежда Асташова    |                   | nadya.astashowa@gmail.com     | Не указан         |          |
| Надежда Арт         |                   | pochta@sochiforum.ru          | Не указан         |          |
| Надежда             | +7 961 791-80-03  | nmaskal@b-urist.ru            | Не указан         |          |
| Надежда             |                   | rbt.moryakov@yandex.ru        | Не указан         |          |
| Надежда             |                   | jigolga@mail.ru               | Не указан         |          |
| Надежда             | +7 905 204-71-17  | press@nbcomgroup.ru           | Не указан         |          |
| Надежда             | +7 927 741-58-73  | envtarget2020@gmail.com       | Не указан         |          |
| Надежда             | +375 44 758-77-77 | imarketing@belfood.by         | Владислав Билалов | 34380865 |
| Надежда             | +7 968 781-30-01  | n.vashurina@samoletgroup.ru   | Александр Черняк  | 35163583 |
| Надежда             | +7 843 526-56-55  | smm@aquapark-riviera.ru       | Владислав Билалов | 37680689 |
| Надежда             |                   | nadezhda.ilina@kaspersky.com  | Владислав Билалов | 38330791 |
| Надежда             | +7 952 721-83-58  | nvlasova@umuseum.ru           | Владислав Билалов | 39002763 |
| Н                   | +7 910 923-63-36  | nik@seleb.me                  | Алексей Танцура   | 40135795 |
| МЦСемейныйдоктор    |                   |                               | Александр Черняк  | 22291901 |
| МЦ Сиз и САС OOO    | +7 495 357-27-67  | info@mcsiz.ru                 | Алексей Танцура   | 40384967 |
| Мухаммаджон,        | +7 977 653-03-50  | Muhammadjonmalikov2@gmail.com | Не указан         |          |
| Мухаметзянова Олеся |                   | m.olesya@unibell.ru           | Не указан         |          |
| Муслим              | +7 901 747-64-74  | shahloklin@gmail.com          | Алексей Танцура   |          |
| Мурат Мурат         | +7 705 380 7777   | make753@mail.ru               | Александр Черняк  | 38510787 |
| Мурат Мурат         | +7 705 380 7777   | make753@mail.ru               | Владислав Билалов | 38512301 |
```


## About final data
> - Total rows: 6881

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 34.95% |
| Emails | 96.24% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                             | phones          | emails                             | raw_metadata                                               |
|:----------------------------------|:----------------|:-----------------------------------|:-----------------------------------------------------------|
| ['A-Jung Im']                     |                 | ['dslevel_en01@dslevel.com']       | ['{"manager": "Не указан"}']                               |
| ['A.Duzhyltst.Ru']                | ['79994556585'] | ['a.duzhy@ltst.ru']                | ['{"edrpou": "23340355", "manager": "Александр Черняк"}']  |
| ['A.Khristenkodominos.Ru']        |                 | ['a.khristenko@dominos.ru']        | ['{"edrpou": "29787227", "manager": "Владислав Билалов"}'] |
| ['A.Kochanovamyunifor.Ru']        |                 | ['a.kochanova@myunifor.ru']        | ['{"manager": "Не указан"}']                               |
| ['A.Krylovmobecan.Com']           |                 | ['a.krylov@mobecan.com']           | ['{"manager": "Не указан"}']                               |
| ['A.Mazurkevichbitcoinchange.Eu'] |                 | ['a.mazurkevich@bitcoinchange.eu'] | ['{"edrpou": "17658877", "manager": "Александр Черняк"}']  |
| ['A.Nurtazadat-Lab.Kz']           |                 | ['a.nurtaza@dat-lab.kz']           | ['{"manager": "Не указан"}']                               |
| ['A.Povarakarussia.Ru']           |                 | ['a.povar@akarussia.ru']           | ['{"manager": "Не указан"}']                               |
| ['A.Razumovtalentpul.Com']        |                 | ['a.razumov@talentpul.com']        | ['{"manager": "Не указан"}']                               |
| ['A.Semakovinostudio.Com']        |                 | ['a.semakov@inostudio.com']        | ['{"edrpou": "21811919", "manager": "Александр Черняк"}']  |
| ['A.Semenovngenix.Net']           |                 | ['a.semenov@ngenix.net']           | ['{"manager": "Не указан"}']                               |
| ['A.Soldatenkomubint.Ru']         |                 | ['a.soldatenko@mubint.ru']         | ['{"manager": "Не указан"}']                               |
| ['A.Zaozerovmetrafor.Ru']         |                 | ['a.zaozerov@metrafor.ru']         | ['{"edrpou": "21811937", "manager": "Александр Черняк"}']  |
| ['Aarav Rana']                    |                 | ['aarav@aplushitechs.com']         | ['{"manager": "Не указан"}']                               |
| ['Abbas Zeynalli']                |                 | ['abbas.zeynalli@startus.cc']      | ['{"manager": "Не указан"}']                               |
| ['Abby Reynolds']                 |                 | ['abby@websyetem.online']          | ['{"manager": "Не указан"}']                               |
| ['Abdurahman']                    |                 | ['soft-technology@mail.ru']        | ['{"edrpou": "28403809", "manager": "Владислав Билалов"}'] |
| ['Aborodinhtc-Cs.Ru']             |                 | ['aborodin@htc-cs.ru']             | ['{"edrpou": "21811943", "manager": "Александр Черняк"}']  |
| ['Abramova Darya']                |                 | ['darya.abramova@tikkurila.com']   | ['{"edrpou": "34283381", "manager": "Александр Черняк"}']  |
| ['Absolut-Novorosmail.Ru']        |                 | ['absolut-novoros@mail.ru']        | ['{"manager": "Не указан"}']                               |
```