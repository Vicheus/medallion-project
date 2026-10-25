# Parsetron results

## About row data

> - Code name: index_0238
> - File path: /media/user/SAMSUNG/Databases/index_0238/raw/forento.ru (09.2023).txt
> - Total rows: 363027

### Schema
```
root
 |-- Фамилия: string (nullable = true)
 |-- Имя: string (nullable = true)
 |-- Отчество: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Ссылка на фото: string (nullable = true)
 |-- Логин: string (nullable = true)
 |-- Пароль: string (nullable = true)

```

### Data sample
```
| Фамилия    | Имя         | Отчество      | Дата рождения   | Ссылка на фото                                     | Логин                       | Пароль     |
|:-----------|:------------|:--------------|:----------------|:---------------------------------------------------|:----------------------------|:-----------|
|            | Форенто     |               |                 |                                                    |                             | 7c75820f3e |
|            | Мария       | Александровна |                 |                                                    | maria.crimea@gmail.com      | maria      |
| Лазарев    | Сергей      | Александрович |                 |                                                    | ivanpetrunya@yandex.ru      | 1111111    |
| Юлианова   | Юлия        |               | 1978.08.04      |                                                    | evpatoriya-leto2010@mail.ru | 19772511   |
| Назаренко  | Елена       |               |                 |                                                    | incognita25@mail.ru         | 23109lena  |
|            | Юрий        |               |                 |                                                    | schelkino.krym@gmail.com    | w9019382   |
|            | Федор       |               |                 |                                                    | robotyr@mail.ru             | 75f91i     |
| Ivanov     | Yuri        |               |                 |                                                    | yuri.zenon@mail.ru          | 10000000a  |
|            | Владимир    | Петрович      |                 |                                                    | vovsev82@rambler.ru         | vovsev82   |
| Иванов     | Константин  | Анатольевич   |                 |                                                    | kotfrontoza@mail.ru         | 987654321  |
| Горлова    | Евгения     | Борисовна     |                 |                                                    | evgenia-gorlova@yandex.ru   | 210596     |
| Настечко   | Наталья     |               |                 |                                                    | nastechko@ua.fm             | natali     |
| Шельпякова | Лина        |               |                 |                                                    | lina.shelpyakova@gmail.com  | Lina1381   |
|            | Dmitry19_71 |               |                 |                                                    | Dmitry19_71@mail.ru         | 88d994eva  |
| Науменко   | Андрей      |               |                 |                                                    | stun-42@yandex.ru           | 110965     |
| Громко     | Наталия     | Борисовна     |                 | https://graph.facebook.com/100008200335924/picture | gromnataliya1@yandex.ru     | rakierova  |
| Иванова    | Мария       |               |                 |                                                    | maria1@ua.fm                | 29102000   |
| Иванов     | Владимир    |               | 2016.01.23      |                                                    | otem@ukr.net                | assa40656  |
| Бабкин     | Эдуард      | Валериевич    |                 |                                                    | vedigal@mail.ru             | ganesh     |
| Толстов    | Витя        |               |                 |                                                    | vitya676@ukr.net            | 4815162342 |
```


## About final data
> - Total rows: 340694

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password: string (nullable = true)

```

### Data sample
```
| names                             | birth_date   | emails                          | accounts                                                                                                       |
|:----------------------------------|:-------------|:--------------------------------|:---------------------------------------------------------------------------------------------------------------|
| ['Мария Александровна']           |              | ['maria.crimea@gmail.com']      | [Row(title='Forento.ru', link='https://forento.ru', login='maria.crimea@gmail.com', password='maria')]         |
| ['Лазарев Сергей Александрович']  |              | ['ivanpetrunya@yandex.ru']      | [Row(title='Forento.ru', link='https://forento.ru', login='ivanpetrunya@yandex.ru', password='1111111')]       |
| ['Юлианова Юлия']                 | 04.08.1978   | ['evpatoriya-leto2010@mail.ru'] | [Row(title='Forento.ru', link='https://forento.ru', login='evpatoriya-leto2010@mail.ru', password='19772511')] |
| ['Назаренко Елена']               |              | ['incognita25@mail.ru']         | [Row(title='Forento.ru', link='https://forento.ru', login='incognita25@mail.ru', password='23109lena')]        |
| ['Юрий']                          |              | ['schelkino.krym@gmail.com']    | [Row(title='Forento.ru', link='https://forento.ru', login='schelkino.krym@gmail.com', password='w9019382')]    |
| ['Федор']                         |              | ['robotyr@mail.ru']             | [Row(title='Forento.ru', link='https://forento.ru', login='robotyr@mail.ru', password='75f91i')]               |
| ['Ivanov Yuri']                   |              | ['yuri.zenon@mail.ru']          | [Row(title='Forento.ru', link='https://forento.ru', login='yuri.zenon@mail.ru', password='10000000a')]         |
| ['Владимир Петрович']             |              | ['vovsev82@rambler.ru']         | [Row(title='Forento.ru', link='https://forento.ru', login='vovsev82@rambler.ru', password='vovsev82')]         |
| ['Иванов Константин Анатольевич'] |              | ['kotfrontoza@mail.ru']         | [Row(title='Forento.ru', link='https://forento.ru', login='kotfrontoza@mail.ru', password='987654321')]        |
| ['Горлова Евгения Борисовна']     |              | ['evgenia-gorlova@yandex.ru']   | [Row(title='Forento.ru', link='https://forento.ru', login='evgenia-gorlova@yandex.ru', password='210596')]     |
| ['Настечко Наталья']              |              | ['nastechko@ua.fm']             | [Row(title='Forento.ru', link='https://forento.ru', login='nastechko@ua.fm', password='natali')]               |
| ['Шельпякова Лина']               |              | ['lina.shelpyakova@gmail.com']  | [Row(title='Forento.ru', link='https://forento.ru', login='lina.shelpyakova@gmail.com', password='Lina1381')]  |
| ['Науменко Андрей']               |              | ['stun-42@yandex.ru']           | [Row(title='Forento.ru', link='https://forento.ru', login='stun-42@yandex.ru', password='110965')]             |
| ['Громко Наталия Борисовна']      |              | ['gromnataliya1@yandex.ru']     | [Row(title='Forento.ru', link='https://forento.ru', login='gromnataliya1@yandex.ru', password='rakierova')]    |
| ['Иванова Мария']                 |              | ['maria1@ua.fm']                | [Row(title='Forento.ru', link='https://forento.ru', login='maria1@ua.fm', password='29102000')]                |
| ['Иванов Владимир']               | 23.01.2016   | ['otem@ukr.net']                | [Row(title='Forento.ru', link='https://forento.ru', login='otem@ukr.net', password='assa40656')]               |
| ['Бабкин Эдуард Валериевич']      |              | ['vedigal@mail.ru']             | [Row(title='Forento.ru', link='https://forento.ru', login='vedigal@mail.ru', password='ganesh')]               |
| ['Толстов Витя']                  |              | ['vitya676@ukr.net']            | [Row(title='Forento.ru', link='https://forento.ru', login='vitya676@ukr.net', password='4815162342')]          |
| ['Анастасия']                     |              | ['nastjaclarnet@mail.ru']       | [Row(title='Forento.ru', link='https://forento.ru', login='nastjaclarnet@mail.ru', password='1122334455abc')]  |
| ['Марина']                        |              | ['rentinfeo2011@yandex.ru']     | [Row(title='Forento.ru', link='https://forento.ru', login='rentinfeo2011@yandex.ru', password='25091959')]     |
```