# Parsetron results

## About row data

> - File path: revitonica_ru_898k_31_05_2024.csv
> - Total rows: 898933

### Schema
```
root
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- name: string (nullable = true)
 |-- city: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- _c6: string (nullable = true)

```

### Data sample
```
| email                    |       phone | name      | city                  | ip                                      | birth_date   | _c6   |
|:-------------------------|------------:|:----------|:----------------------|:----------------------------------------|:-------------|:------|
| l_bilan@mail.ru          | 79122493185 | ЛЮБОВЬ    | ЕКАТЕРИНБУРГ          | 94.140.145.96                           | 07.12.1948   |       |
| jane-vp@mail.ru          |             |           |                       |                                         |              |       |
| kalinina.anna@mail.ru    | 79261846353 | Анна      | Москва                | 193.34.211.30                           | 24.09.1976   |       |
| dubinskaya@revitonica.ru | 79165666688 | Анастасия | Москва                | 109.252.115.3                           | 23.05.1980   |       |
| kurudimova@revitonica.ru | 79017492596 | Наталья   | Москва                | 212.46.18.183                           | 02.03.1990   |       |
| help@revitonica.ru       | 74951182279 | Help      | Россия                | 95.131.149.33                           | 07.08.2018   |       |
| innazinoveva@yandex.ru   | 79116155020 | Инна      | Великий Новгород      | 62.217.186.168                          | 01.11.1973   |       |
| konenkova.nv@gmail.com   | 79030006631 | Наталья   | Москва                | 91.193.178.232                          | 15.10.1980   |       |
| lyudk.rozhnova@yandex.ru | 79044669773 | Людмила   | Ханты-Мансийск        | 188.18.240.217                          | 01.05.1956   |       |
| logostyle@hotmail.com    |             | Лена      | Берлин                | 2a02:8109:b585:7200:ad6b:bd51:9275:1405 |              |       |
| mammadaragaya@mail.ru    | 79119683863 | Юлия      | Санкт-Петербург       | 2a00:1fa0:8666:1bc0:417f:2cd6:4865:2ffa | 17.11.1968   |       |
| weet@mail.ru             | 79286059777 | Людмила   | Россия Ростов—на-Дону | 86.110.189.174                          | 05.06.1962   |       |
| elmill@yandex.ru         | 70546366919 | Елизавета | Тель Авив             | 79.181.107.133                          | 15.10.1967   |       |
| trest-ufa@mail.ru        | 79173751167 | Юлия      | Уфа                   | 94.41.237.139                           | 20.09.1967   |       |
| valital@mail.ru          | 79163363407 | Валентина | Москва                | 95.220.43.234                           | 17.11.1953   |       |
| golddan07@rambler.ru     | 79052869240 | Ирина     | Санкт-Петербург       | 95.24.211.236                           | 28.08.1965   |       |
| elen-gubinskay@yandex.ru | 79023384543 | Елена     | Самара                | 80.234.0.12                             | 18.06.1975   |       |
| ahmedof.e@gmail.com      | 76476374876 | Eugenia   | Mississauga           | 66.203.207.68                           | 10.08.1973   |       |
| elen7771@ya.ru           | 79266710622 | Елена     | Москва                | 46.242.90.122                           | 17.03.1966   |       |
| elena16642@gmail.com     |             | Elena     | Israel                | 46.210.60.158                           |              |       |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 89.82% |
| Phones | 62.66% |
| Emails | 99.97% |
| Address | 91.31% |
| Ips | 99.99% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                      | birth_date   | phones          | emails                           | address                   | ips                                                  | source_entity_id                                         |
|:---------------------------|:-------------|:----------------|:---------------------------------|:--------------------------|:-----------------------------------------------------|:---------------------------------------------------------|
| ['Aizhan']                 | 09.01.2000   |                 | ['ajzanturysbek@gmail.com']      | ['Alma-ata']              | [Row(ip='2.133.76.239', date=None, comment=None)]    | 7e79bbd64f1eafb092029782c9fef916997c021c83c643679ee6508c |
| ['Akbota']                 | 31.12.1971   |                 | ['omarova_akbota@mail.ru']       | ['Kazakhstan']            | [Row(ip='178.88.101.58', date=None, comment=None)]   | 336c0d497bddb3539daffdb7fd9edd2353a0c45594e1d7db7dc64be0 |
| ['Albina']                 | 05.01.1995   |                 | ['a.gilazutdinova@gmail.com']    | ['Room 404']              | [Row(ip='46.193.67.146', date=None, comment=None)]   | da31f1a6df3a82f3930d7cc5eef25af1d8033658ec007f022f4ad81d |
| ['Aleksandra Fortuna']     |              |                 | ['alexariga2017@gmail.com']      | ['Латвия']                | [Row(ip='95.68.103.109', date=None, comment=None)]   | e7c0efb72fdc360199f4a331eb4c62e8c4e495a87557f9936884f5bf |
| ['Alina Corjan']           | 17.09.1982   |                 | ['alina.corjan@gmail.com']       | ['Canada']                | [Row(ip='142.114.65.187', date=None, comment=None)]  | 063ac44307058a80ebe48bdd04c0ebada42af26c48e729c284097474 |
| ['Alla Rafuse']            | 16.03.1965   |                 | ['alla.trifanova@gmail.com']     | ['Canada']                | [Row(ip='64.231.66.148', date=None, comment=None)]   | 40248a950770ab7a2f5245df1867cb143fd0feba13149266404565b7 |
| ['Amina']                  | 18.07.1984   |                 | ['a.tsukar@seznam.cz']           | ['Czechia']               | [Row(ip=None, date=None, comment=None)]              | 8e47b6c16f3ebe649139eb15a37c238fc271b808895c7d39eefb2e71 |
| ['Anastasia']              | 30.09.1980   |                 | ['a_neverovska@yahoo.de']        |                           | [Row(ip=None, date=None, comment=None)]              | 55934bfa9a9ebc5f7672b4d99bd678a5f92289d7f692b4711b6a312a |
| ['Anna Broumerioti']       | 17.06.1984   |                 | ['broumetaki@gmail.com']         | ['Афины']                 | [Row(ip=None, date=None, comment=None)]              | 7408362d5a9573b5ba711fdd6d19d669899deeb4540c2abaea4eb528 |
| ['Anna Gavrilenko']        | 28.02.1986   | ['79241809084'] | ['gavrilenko_anna_v@rambler.ru'] | ['Южно-Сахалинск']        | [Row(ip='188.113.158.75', date=None, comment=None)]  | 33410fcf998b14e6194fd97638646f20fb4eb05e4a655bcfc9dc8c8c |
| ['Audinga Dalinkeviciene'] | 07.07.1979   |                 | ['audute@gmail.com']             | ['Vilnius']               | [Row(ip='78.60.244.24', date=None, comment=None)]    | 474608c9fa3b24eb449dcb77daf4212f62a1bea1bbf0c05b365ac75c |
| ['Carmen Ferrer']          | 31.05.1965   |                 | ['infantilcastell@gmail.com']    | ['Espa a Valencia 46760'] | [Row(ip='90.167.50.145', date=None, comment=None)]   | 3c2bb3f3503cba6c1f6b3b5ed9ba4b8270a13ed0e5674ece1c134f11 |
| ['Diana']                  | 20.08.1996   | ['79139224515'] | ['vedinara@yahoo.com']           | ['Russia']                | [Row(ip='109.174.112.204', date=None, comment=None)] | fddff0448b5d5ce38d45bf15359fa605aca77a8eba85e9b9fc4cafe2 |
| ['Elena']                  | 29.09.1983   |                 | ['elengot@mail.ru']              | ['Беларусь']              | [Row(ip='46.56.239.93', date=None, comment=None)]    | 21128d6f5eeac97bb128765273e394f8a6532dc9dc0f61a791cca6eb |
| ['Elena']                  | 08.07.1982   | ['79169152256'] | ['elena.gordeenkova@gmail.com']  | ['Москва']                | [Row(ip='188.191.126.211', date=None, comment=None)] | ea113f138ef695c5606b27ab95cb2bd5fdc414b16e1ac87117828e03 |
| ['Elena']                  | 01.05.1970   | ['79263896380'] | ['3896380@mail.ru']              | ['Москва']                | [Row(ip='109.252.70.78', date=None, comment=None)]   | 21252a80c2d5f390ab6d01c7006173e332d8107550005d4911fa2d3f |
| ['Elena']                  | 09.05.1979   | ['79996091221'] | ['elenabutova1979@gmail.com']    | ['Kursk']                 | [Row(ip='176.194.219.84', date=None, comment=None)]  | d1b42667260c9363db7dbd5c6ad5e97ed1e35e6db0facca2660ff44e |
| ['Elena Smith']            |              |                 | ['elenasmith888@me.com']         |                           | [Row(ip='211.30.197.105', date=None, comment=None)]  | 14261b2052d5d31ca92e80053f323c2aaafff36800ae9b5f981ae282 |
| ['Elnara']                 | 09.04.1991   |                 | ['elnara_qasimova@bk.ru']        | ['Baku']                  | [Row(ip='185.43.191.70', date=None, comment=None)]   | b0403f8c2f36ca42bc25ba4550562b6ba548c89b4e8562ff444b2473 |
| ['Evgeniya Moser']         | 18.05.1982   |                 | ['jeny.moser@googlemail.com']    |                           | [Row(ip='50.19.181.220', date=None, comment=None)]   | f0c83dc421323b8e7c35fb959ef2899613cb8347467e319083449d40 |
```