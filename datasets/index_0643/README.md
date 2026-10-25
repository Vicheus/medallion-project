# Parsetron results

## About row data

> - Code name: index_0643
> - File path: ngs_users.csv
> - Total rows: 1900970

### Schema
```
root
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- modify_date: string (nullable = true)
 |-- owner: integer (nullable = true)

```

### Data sample
```
| login                 | password                         | name                     | email                     | modify_date         |   owner |
|:----------------------|:---------------------------------|:-------------------------|:--------------------------|:--------------------|--------:|
| p.prudnikov@ngs.ru    | 2de4d824bb31b23756dce8b22a298b98 | Пётр                     | p.prudnikov@office.ngs.ru | 2021-02-08 11:32:19 |       0 |
| hilda                 | 844b671d51b968d308549ca32373b740 | Инна                     | iva@ngs.ru                | 2008-03-24 12:57:14 |       0 |
| kopeyka               | f27c69e5933df2e414acace56c229053 | Копейка                  | kopeyka@ngs.ru            | 2008-03-24 12:57:14 |       0 |
| creditrealty          | 704359e4ecaec71af400f29a89065d6b | АН Крэдит Риэлт          | info@creditrealty.ru      | 2008-03-24 12:57:14 |       0 |
| arenda@trudsib.ru     | 63cb493168a61432c9013955a734fdf6 | Группа компаний "Труд"   | arenda@upkekoplast.ru     | 2011-06-15 09:20:28 |       0 |
| centrdn               | ec38d1ccf6947dc349aa54d21d5cde4c | Объединение Регистрация  | komn@taxlab.ru            | 2008-03-24 12:57:14 |       0 |
| riona                 | e2b3b976f3049e6bd6f8dc07f2a8f095 | Светлана (Агентство)     | newmail@ngs.ru            | 2008-04-02 12:31:18 |       0 |
| ilia_k                | 4e2fb7a80f85f7b1a991601366167073 | Илья                     | ilia_k@online.sinor.ru    | 2008-03-24 12:57:14 |       0 |
| akadem                | 3737a992d8ae9b9995501dad7843f803 | АН « Академгородок»      | sipay@mail.ru             | 2008-03-24 12:57:14 |       0 |
| info@magnsk.ru        | 9466f657b7eb43d3041d9db8ac7b2dee | Магистраль               | magistral@nvcom.ru        | 2011-06-15 09:43:48 |       0 |
| kvburo                | 102dc7fcc403e6248a07c48fc5e5d68b | Квартирное бюро          | buro@list.ru              | 2008-03-24 12:57:14 |       0 |
| max                   | a821d22589d66b0ede0e275939bfcddd | Максим                   | mail@office.ngs.ru        | 2009-03-31 14:11:47 |       0 |
| mdv                   | e48a51488e5aa517041a15bf5db69a9b | Молчанов Дмитрий         | mdv@office.ngs.ru         | 2009-02-10 11:22:27 |       0 |
| info@sian-n.ru        | f82caacb152c6a1d976223ea7ac291fe | СИАН                     | info@sian-n.ru            | 2011-06-16 10:11:55 |       0 |
| 119590@acropol.com.ru | ef237f7f4217cff5616eaf0f26e8bff7 | Акрополь                 | 119590@acropol.com.ru     | 2015-03-23 16:51:41 |       0 |
| po                    | 32ccac7e338550b58836d7686774b690 | ПРАВИЛЬНЫЙ ОБМЕН         | info@p-obmen.ru           | 2008-03-24 12:57:14 |       0 |
| whitebird             | 9bf717e90cd644d9e8d2992c15262105 | Александр Владимирович   | whitebird@ngs.ru          | 2008-03-24 12:57:14 |       0 |
| agent                 | 8e44be1b115c131afb3096f2e99e9b27 | Орион Владимир           | agent2003@bk.ru           | 2008-03-24 12:57:14 |       0 |
| obskaya               | 03dfd4617269b3e6bd133a3b8a6bb77c | Первый строительный фонд | psfcentr@risp.ru          | 2008-12-08 13:38:06 |       0 |
| busness_r             | e72b85ef0fb7a4bcb15666b27501c8e5 | Бизнес Риэлт             | busness_r@mail.ru         | 2008-03-24 12:57:14 |       0 |
```


## About final data
> - Total rows: 1686326

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- actuality: date (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |
| Accounts | 100.00% |
| Actuality | 95.40% |



### Data sample
```
| names                          | emails                            | accounts                                                                                                                           | actuality   |
|:-------------------------------|:----------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['A.Toochina']                 | ['a.toochina@gmail.com']          | [Row(title='NGS', link='https://ngs.ru', login='99157#nn.ru', password_hash='91a6113711ae81d677eb9bffdde1cba2')]                   | 21.09.2015  |
| ['Aaazaliaaa']                 | ['janerichvillalobos6@gmail.com'] | [Row(title='NGS', link='https://ngs.ru', login='janerichvillalobos6@gmail.com', password_hash='261b22bda9ce50e69d5c3b9adb6bdeba')] |             |
| ['Abcent']                     | ['sa-konov@mail.ru']              | [Row(title='NGS', link='https://ngs.ru', login='128723#nn.ru', password_hash='b2441d680667ed1104adeb240e7dded2')]                  | 25.03.2009  |
| ['Abdaliev Aziz Alisherovich'] | ['www.azisu@mail.ru']             | [Row(title='NGS', link='https://ngs.ru', login='www.azisu@mail.ru', password_hash='1eff32235e4e11dac05d843635c3039a')]             | 04.12.2007  |
| ['Absolutelove']               | ['absoluteloveml@gmail.com']      | [Row(title='NGS', link='https://ngs.ru', login='104096#nn.ru', password_hash='5dff75da06a278c8b11e74bb41837ffa')]                  | 21.10.2008  |
| ['Academeml.Ru']               | ['redemp@mail.ru']                | [Row(title='NGS', link='https://ngs.ru', login='academ@eml.ru', password_hash='02ee727acfe630e25104586e857e8ed4')]                 | 03.05.2019  |
| ['Aciseegrordic']              | ['pikatorov1298@gmail.com']       | [Row(title='NGS', link='https://ngs.ru', login='pikatorov1298@gmail.com', password_hash='15c1d768290e542741cd6d0037f8acb8')]       |             |
| ['Acureq']                     | ['acureq@ngs.ru']                 | [Row(title='NGS', link='https://ngs.ru', login='acureq@ngs.ru', password_hash='f9759827a5d2cfafddce7f7c5c13c67e')]                 |             |
| ['Adorable']                   | ['lykavaya_85@mail.ru']           | [Row(title='NGS', link='https://ngs.ru', login='257941#nn.ru', password_hash='ee6efc8eb2ac5d725031544ed5f9a21b')]                  | 25.11.2013  |
| ['Advertise']                  | ['advert@mail.nnov.ru']           | [Row(title='NGS', link='https://ngs.ru', login='5903#nn.ru', password_hash='9b6a7eff8027bd2caf83428093d59ce0')]                    | 28.04.2008  |
| ['Advnoka']                    | ['adv.noka@mai.ru']               | [Row(title='NGS', link='https://ngs.ru', login='426185#nn.ru', password_hash='8619f5a05c30657293ba6f496e859b6e')]                  | 03.07.2013  |
| ['Aenca']                      | ['aenca@yandex.ru']               | [Row(title='NGS', link='https://ngs.ru', login='275488#nn.ru', password_hash='1e9fbd90d08db5a87ff19db4625e0108')]                  | 20.05.2011  |
| ['Aerober']                    | ['ape-nn@mail.ru']                | [Row(title='NGS', link='https://ngs.ru', login='3756#nn.ru', password_hash='2544b26b16f2d2b583b60f33874b5be0')]                    | 25.11.2013  |
| ['Aerowhera']                  | ['haixclalync@mail.ru']           | [Row(title='NGS', link='https://ngs.ru', login='101323#nn.ru', password_hash='9cdfcd0c5520f123bba44ce4d342c0a8')]                  | 02.10.2008  |
| ['Afri']                       | ['golovizin@yandex.ru']           | [Row(title='NGS', link='https://ngs.ru', login='158592#nn.ru', password_hash='e0b6913a43294236bf6720792a465e56')]                  | 07.10.2009  |
| ['Agata Кристи']               | ['kira-mor@mail.ru']              | [Row(title='NGS', link='https://ngs.ru', login='kira-mor@mail.ru', password_hash='cf858fabba1c5163142734e1fd399cec')]              | 26.03.2012  |
| ['Ageyevvpngs.Ru']             | ['ageyevav@ngs.ru']               | [Row(title='NGS', link='https://ngs.ru', login='ageyevvp@ngs.ru', password_hash='297b98356be143713ad65d075045ea59')]               | 23.10.2018  |
| ['Agnin']                      | ['agnin@yandex.ru']               | [Row(title='NGS', link='https://ngs.ru', login='314743#nn.ru', password_hash='d931f68fede213ca5f9b2d6d2dad17c6')]                  | 11.12.2011  |
| ['Aideniumnib']                | ['useneurne@gmail.com']           | [Row(title='NGS', link='https://ngs.ru', login='105648#nn.ru', password_hash='aaa65fdae98317bbd20dd755472bd00f')]                  | 03.11.2008  |
| ['Airat']                      | ['gaght@bk.ru']                   | [Row(title='NGS', link='https://ngs.ru', login='gaght@bk.ru', password_hash='bf3eec3ef84bd905296e8821cfeeca35')]                   | 04.12.2007  |
```