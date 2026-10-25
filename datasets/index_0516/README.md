# Parsetron results

## About row data

> - Code name: index_0516
> - File path: users.csv
> - Total rows: 4001

### Schema
```
root
 |-- RESULT_ID: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)

```

### Data sample
```
|   RESULT_ID | name                             | email                    | phone                       |
|------------:|:---------------------------------|:-------------------------|:----------------------------|
|        5217 | Александра                       | info@avantransport.com   | 89053419696                 |
|        3969 | Балхановкая Кристина анатольевна | balkris0801@yandex.ru    | 89262658787                 |
|        5103 | Вера                             | elanverawell@mail.ru     | 89222114842                 |
|        4744 | Гузель                           | lawfirm.ds.llc@gmail.com |                             |
|        1041 | Диана Чартаева                   | kvartira@investaktiv.ru  | (343)3103986                |
|        2534 | Дмитрий                          | Grishanindm@yandex.ru    | 9022635672                  |
|        5535 | ЕРМАКОва наталья васильевна      | AAAmikkaa@gmail.com      | 79002103343                 |
|        5720 | Ковалёв Николай Иванович         | kolyadk2010@yandex.ru    | 79538261693                 |
|        5303 | Ливанова Ольга Владимировна      | livanova_olga@mail.ru    | 89033790496                 |
|        3130 | Наталья                          | natalia.grekhova@mail.ru | 89030786969                 |
|        4250 | Полина                           | polinatkn@yandex.ru      | 79266911878                 |
|        4264 | Полина                           | polinatkn@yandex.ru      | 79266911878                 |
|        2592 | Светлана Конева                  | S.Koneva@renova-group.ru | (495) 720-49-99 (доб.58-67) |
|         495 | Яковлева Наталья                 | natka154@yandex.ru       | +7-9-222-00-78-40           |
|        5091 | Aleksandra Gvozdenovic lakic     | Pharmacy.house@t-com.me  | 38269015050                 |
|        3885 | Alex                             | pepsiman665@gmail.com    |                             |
|         756 | Alexander                        | sett@mail.ru             | +7 916 179 64 07            |
|         442 | Alexander Atharov                | roy707@mail.ru           |                             |
|          95 | Alexandr                         | pa@ravolna.ru            | 89222421355                 |
|         909 | ALEXANDRE LISBOA                 | PRIMORIO@HOTMAIL.COM     |                             |
```


## About final data
> - Total rows: 3497

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.89% |
| Phones | 66.94% |



### Data sample
```
| names                            | emails                          | phones          |
|:---------------------------------|:--------------------------------|:----------------|
| ['Alexey']                       | ['raskatovamn@yandex.ru']       | ['78005266742'] |
| ['Yulia Raskatova']              | ['guffon@yandex.ru']            | ['78005266742'] |
| ['Василь Юсуфкулов']             | ['pk@m-group.perm.ru']          | ['79028084228'] |
| ['Вера']                         | ['wero4ka05@mail.ru']           | ['79082683159'] |
| ['Елена']                        | ['fitot@yandex.ru']             | ['79269743460'] |
| ['Игорь']                        | ['migrac-centr@mail.ru']        | ['79122744708'] |
| ['Ксения']                       | ['kseniya.nikitina.94@list.ru'] | ['79521445862'] |
| ['Матеров Никита Романович']     | ['materov-2002@mail.ru']        | ['79041348862'] |
| ['Морозовская Ирина Михайловна'] | ['khlirina@yandex.ru']          | ['79053289701'] |
| ['Ооо Пкп Росмет']               | ['ktn@pkp-rosmet.ru']           | ['73439349800'] |
| ['Пермяков Александр']           | ['permyakov-aa@yandex.ru']      | ['79091033112'] |
| ['Сергей Корепанов']             | ['sergio_kor@mail.ru']          | ['79823898846'] |
| ['Андрей']                       | ['stella-gorbunov@mail.ru']     |                 |
| ['Дмитрий']                      | ['sdr57@mail.ru']               |                 |
| ['Елена']                        | ['fox.lena@rambler.ru']         |                 |
| ['Топджу']                       | ['hhh@yandex.ru']               |                 |
| ['Эртугрул Молулу']              | ['export@flekssitoffice.com']   |                 |
| ['Юлия']                         | ['c-julya@yandex.ru']           |                 |
| ['Василий']                      | ['vmatveevv@yandex.ru']         | ['79826465186'] |
| ['Дарья']                        | ['d.rysina@hostco.ru']          | ['79122096972'] |
```