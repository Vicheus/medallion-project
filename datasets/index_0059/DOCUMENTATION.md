# Parsetron results

## About row data

> - File path: burgerkingrus.ru_08.2024_(5.627.676)_orders.csv.csv
> - Total rows: 5627676

### Schema
```
root
 |-- phone: long (nullable = true)
 |-- email: string (nullable = true)
 |-- name: string (nullable = true)
 |-- birthdate: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- address: string (nullable = true)
 |-- favcategory: string (nullable = true)
 |-- favdish: string (nullable = true)
 |-- loyaltysegment: string (nullable = true)
 |-- spicylover: boolean (nullable = true)
 |-- timezone: string (nullable = true)
 |-- emailconfirmed: boolean (nullable = true)
 |-- phoneconfirmed: boolean (nullable = true)
 |-- datetime: timestamp (nullable = true)

```

### Data sample
```
|       phone | email                         | name           | birthdate   | gender   | address         | favcategory          | favdish           | loyaltysegment     | spicylover   | timezone           | emailconfirmed   | phoneconfirmed   | datetime                   |
|------------:|:------------------------------|:---------------|:------------|:---------|:----------------|:---------------------|:------------------|:-------------------|:-------------|:-------------------|:-----------------|:-----------------|:---------------------------|
| 79162030883 | fioshkin.mikhaily@mail.ru     | Михаил         | 09.06.2021  | male     | Москва          |                      |                   | Невозвратный отток |              | Europe/Moscow      | False            | True             | 2024-08-22 19:41:46.990000 |
| 79011016394 | polina.masych@mail.ru         | Полина         | 19.11.2002  | female   | Краснодар       |                      |                   |                    |              | Europe/Moscow      | True             | True             | 2024-08-25 23:47:34.017000 |
| 79246855479 | sofya_shestak@mail.ru         | Софья          | 12.01.2007  | female   | Санкт-Петербург |                      |                   |                    |              | Europe/Moscow      | False            | True             | 2024-08-25 23:47:52.943000 |
| 79964497507 | nice.shkolin02@mail.ru        | Егор           | 24.06.2000  | male     | Брянск          | Закуски              | НАГГЕТСЫ          |                    | False        | Europe/Moscow      | True             | True             | 2024-08-02 10:35:46.557000 |
| 79806596299 | lokomotiv_yar@mail.ru         | Семен          | 02.05.1994  | male     | Москва          | закускам             | Кинг Фри (станд.) | Активный           |              | Europe/Moscow      | False            | True             | 2024-08-25 17:15:28.363000 |
| 79604654515 |                               |                |             |          | Таганрог        |                      |                   |                    |              | Europe/Moscow      |                  | True             | 2024-08-25 16:56:11.957000 |
| 79326131008 | smirnova.e.y88@gmail.com      | Максимка       | 29.09.1999  |          | Екатеринбург    |                      |                   |                    |              | Asia/Yekaterinburg | False            | True             | 2024-08-23 03:12:48.420000 |
| 79775959137 |                               |                |             |          | Орехово-Зуево   |                      |                   | Невозвратный отток |              | Europe/Moscow      |                  | True             | 2024-08-25 18:07:37.650000 |
| 79937499439 | daniil.krasovskiy2000@mail.ru | Даниил         | 05.04.2006  | male     | Вологда         |                      |                   |                    |              | Europe/Moscow      | False            | True             | 2024-08-25 00:14:43.697000 |
| 79611625761 | doronin.timofey@gmail.com     | Тимофей        |             | male     | Москва          | закускам             | Кинг Фри джун     | Активный           |              | Europe/Moscow      | True             | True             | 2024-08-25 23:36:14.840000 |
| 79031112073 |                               |                |             |          | Москва          |                      |                   |                    |              | Europe/Moscow      |                  | True             | 2024-08-25 15:44:47.307000 |
| 79192877735 | alinaivanchenkova@gmail.com   | Алина          | 10.05.2021  | female   | Старый Оскол    | бургерам с говядиной | Чизбургер         | Невозвратный отток |              | Europe/Moscow      | True             | True             | 2024-08-20 14:02:14.907000 |
| 79867031606 | artemtrucahev@gmail.com       | Артём          | 18.08.2007  | male     | Уфа             |                      |                   |                    |              | Asia/Yekaterinburg | False            | True             | 2024-08-24 08:40:18.157000 |
| 79196383350 |                               |                |             |          | Казань          |                      |                   |                    |              | Europe/Moscow      |                  | True             | 2024-08-02 10:56:08.347000 |
| 79257700198 |                               |                |             |          | Химки           |                      |                   |                    |              | Europe/Moscow      |                  | True             | 2024-08-25 19:53:36.887000 |
| 79686834845 | andrey.karasev.2003@gmail.com | Карасев Андрей |             | male     | Москва          | бургерам с говядиной | Чизбургер         | Активный           |              | Europe/Moscow      | False            | True             | 2024-06-22 20:22:39.653000 |
| 79067987668 | miyako_yuu@mail.ru            | Алёна          | 08.03.1992  | female   | Мытищи          |                      |                   |                    |              | Europe/Moscow      | True             | True             | 2024-08-25 19:50:17.880000 |
| 79829624633 | gyuygggg@gmail.com            | Гегенпгрг      | 28.07.2000  |          | Тюмень          | Закуски              | КИНГ ФРИ          | Невозвратный отток | False        | Asia/Yekaterinburg | False            | True             | 2024-08-24 17:59:02.533000 |
| 79885488922 |                               |                |             |          | Новошахтинск    |                      |                   |                    |              | Europe/Moscow      |                  | True             | 2024-06-12 14:33:38.340000 |
| 79638991162 |                               |                |             |          | Уфа             |                      |                   |                    |              | Asia/Yekaterinburg |                  | True             | 2024-08-25 13:54:41.440000 |
```


## About final data

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
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- actuality: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 89.99% |
| Phones | 99.98% |
| Address | 89.26% |
| Sex | 91.22% |
| Birth_date | 69.59% |
| Actuality | 99.66% |
| Raw_metadata | 39.87% |



### Data sample
```
| names                    | emails                             | phones          | address             |   sex | birth_date   | actuality   | raw_metadata                                                            |
|:-------------------------|:-----------------------------------|:----------------|:--------------------|------:|:-------------|:------------|:------------------------------------------------------------------------|
| ['- Котёнок Катя']       |                                    | ['79914870862'] |                     |     0 | 29.04.2015   | 16.06.2024  |                                                                         |
| ['- Мелисса']            |                                    | ['79004673950'] | ['Пенза']           |   nan |              | 21.08.2024  |                                                                         |
| ['- Соняняня']           | ['vera.kolbas@mail.ru']            | ['79227762948'] | ['Нижневартовск']   |   nan |              | 07.08.2024  | ['{"favcategory": "Закуски", "favdish": "КИНГ ФРИ"}']                   |
| ['A Andrey']             | ['mamatov2019@mail.ru']            | ['79263055000'] | ['Апрелевка']       |     1 | 16.05.1984   | 06.08.2024  |                                                                         |
| ['A.Gerasimovainbox.Ru'] | ['a.gerasimova@inbox.ru']          | ['79613137813'] | ['Ростов-на-Дону']  |   nan |              | 25.08.2024  | ['{"favcategory": "закускам", "favdish": "Кинг Фри джун"}']             |
| ['Aachidorri']           | ['kirillbykov468@gmail.com']       | ['79093277112'] | ['Саранск']         |   nan | 04.05.2000   | 23.08.2024  | ['{"favcategory": "Закуски", "favdish": "НАГГЕТСЫ"}']                   |
| ['Aalarchenko']          | ['lar4enkoandrey@gmail.com']       | ['79162164070'] | ['Москва']          |   nan | 20.03.1989   | 17.08.2024  |                                                                         |
| ['Aalllooo']             | ['galkevich-anya@mail.ru']         | ['79103989324'] | ['Нижний Новгород'] |   nan | 04.11.2004   | 24.08.2024  | ['{"favcategory": "Закуски", "favdish": "КИНГ ФРИ"}']                   |
| ['Abakumov Ilya']        | ['ilyaabakumov070600@icloud.com']  | ['79856476402'] | ['Протвино']        |   nan | 07.06.2000   | 24.08.2024  | ['{"favcategory": "Бургеры из курицы", "favdish": "Чикенбургер"}']      |
| ['Abama']                | ['abamakniga@gmail.com']           | ['79656805539'] | ['Чебоксары']       |   nan | 15.09.2004   | 23.08.2024  |                                                                         |
| ['Abama']                | ['nik.abaturov2006@gmail.com']     | ['79777783798'] | ['Котельники']      |   nan |              | 12.08.2024  | ['{"favcategory": "Закуски", "favdish": "КИНГ ФРИ"}']                   |
| ['Abasov Anar']          | ['lurchic@mail.ru']                | ['79539399264'] | ['Москва']          |   nan | 25.02.2001   | 25.08.2024  |                                                                         |
| ['Abbas']                | ['abbas.heydarov42@gmail.com']     | ['79969271836'] | ['Москва']          |     1 | 16.04.2008   | 25.08.2024  |                                                                         |
| ['Abbasov']              | ['abbasov.pasha_7@mail.ru']        | ['79514487628'] | ['Челябинск']       |   nan | 01.06.1995   | 24.08.2024  |                                                                         |
| ['Abbasov Tural']        | ['tural1631@yandex.ru']            | ['79372349911'] | ['Тольятти']        |   nan | 25.06.1992   | 12.08.2024  |                                                                         |
| ['Abbos']                | ['asliddinov.a@mail.ru']           | ['79500278185'] | ['Санкт-Петербург'] |   nan |              | 03.08.2024  |                                                                         |
| ['Abdalla']              | ['abdo.deban55@gmail.com']         | ['79003314362'] | ['Казань']          |   nan |              | 19.08.2024  | ['{"favcategory": "Закуски", "favdish": "КИНГ ФРИ"}']                   |
| ['Abdalla']              | ['gaz95iev@gmail.com']             | ['79613131202'] | ['Санкт-Петербург'] |   nan | 13.12.2002   | 02.08.2024  | ['{"favcategory": "закускам", "favdish": "Кинг Фри джун"}']             |
| ['Abdelbaki']            | ['abdelbakihadjali2003@gmail.com'] | ['79522292545'] | ['Санкт-Петербург'] |     1 | 26.08.2003   | 25.08.2024  | ['{"favcategory": "Десерты", "favdish": "Горячий Брауни с мороженым"}'] |
| ['Abdelkadir']           | ['ka.merili@mail.ru']              | ['79992405901'] | ['Санкт-Петербург'] |   nan | 08.03.1985   | 24.08.2024  |                                                                         |
```