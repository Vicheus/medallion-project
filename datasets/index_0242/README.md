# Parsetron results

## About row data

> - Code name: index_0242
> - File path: users_preprocessed.csv
> - Total rows: 3020

### Schema
```
root
 |-- firstname: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- email: string (nullable = true)
 |-- telephone: string (nullable = true)
 |-- password: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- date_added: timestamp (nullable = true)
 |-- company: string (nullable = true)
 |-- postcode: string (nullable = true)
 |-- city: string (nullable = true)
 |-- address_1: string (nullable = true)

```

### Data sample
```
| firstname   | lastname   | email                  |   telephone | password                                 | ip             | date_added          | company          |   postcode | city            | address_1                              |
|:------------|:-----------|:-----------------------|------------:|:-----------------------------------------|:---------------|:--------------------|:-----------------|-----------:|:----------------|:---------------------------------------|
| Денис       | миронов    | logosat@mail.ru        | 79024714707 | 874f4cbbba06db73e6b4342e90639fe392efdb2f | 178.47.72.186  | 2015-12-11 19:44:15 | ИнтерСтромСервис |            | пермь           | ш космонавтов                          |
| Вячеслав    | Осипик     | agronom.perm@mail.ru   | 79223083859 | 3462f23e17944ba6cc2e2f7e6c6db0e350395f61 | 46.146.238.129 | 2015-12-22 09:43:42 |                  |            | Пермь           | Пермь                                  |
| Елена       | Попова     | lowe1977@mail.ru       | 79194718878 | 541bba86f97fe8220f6fa2e48ab774a6b9505193 | 46.146.221.130 | 2015-12-22 10:42:29 |                  |     614065 | Пермь           | г. Пермь ул. Шоссе Космонавтов 326А-12 |
| Полина      | Буланова   | polina-kupcova@mail.ru | 79125872606 | c680eb8b0d9669c0f6db2b58648916b91606240b | 37.79.0.183    | 2015-12-22 10:53:59 |                  |            | Пермь           | Ивана Франко 44                        |
| Владимир    | Шляпин     | 79082662691@ya.ru      | 79082662691 | 4ccb0bf1968babf8cada3d31ca11aed816c75ee0 | 188.17.149.127 | 2015-12-22 11:03:22 |                  |            | Березники       | Мира 34-12                             |
| Мария       | Лалетина   | Lemon_25@list.ru       | 79194475513 | 74f550f0c7e503dc116aeaadeb8291ca1fcd7ac7 | 195.64.208.173 | 2015-12-22 11:24:05 |                  |            | Березники       | Свердлова 59                           |
| Мария       | Бычина     | markiza_@bk.ru         | 79223661196 | 87a184f6f6cb6df1a6269ca0ba5dcbe4d634af25 | 194.190.5.136  | 2015-12-22 12:34:00 |                  |            | Пермь           | Сочинская 6-54                         |
| желанна     | гунгер     | zelanna777@yandex.ru   | 79128852671 | 9d2c4fd1970191060a19d9ac6f72c9ed747c3620 | 188.168.78.245 | 2015-12-22 13:59:01 |                  |            | Березники       | Мира ул 112-4                          |
| Андрей      | Логинов    | oumm61@gmail.cdom      | 79788080198 | 250a860408cbdb565563d17af1dce77199c16fb1 | 62.76.12.227   | 2015-12-22 18:33:12 |                  |     299053 | Севастополь     | Глухова9                               |
| Александр   | Шмыков     | shmikovall@gmail.com   | 79026490790 | 3962a38acea331d4c0119ee37631aaaf4c6f3d4f | 77.236.71.248  | 2015-12-22 20:03:00 |                  |     618426 | Березники       | Комсомольская, 4 - 4                   |
| станислав   | кудряшев   | kirasa@ya.ru           | 79024764155 | 2f46f19081bd284140fe4437f3348475c6ad4cf9 | 37.76.144.24   | 2015-12-22 20:19:28 |                  |            | пермь           | Качалова,21-34                         |
| Роман       | Кузнецов   | romochka-4@gmail.com   | 79125904825 | cb670a10dbdaeaf2e77801fce6c6d584a0fb208d | 5.141.194.213  | 2015-12-22 21:13:02 |                  |            | Пермь           | Боровая, 2-14                          |
| Владимир    | Краснов    | xateee@gmail.com       | 79824510784 | 7a6b30fad8dbd362c34fce250c49c37696d6155a | 46.146.213.90  | 2015-12-23 12:03:06 |                  |     615008 | Пермь           | Красновишерская 35                     |
| Андрей      | Логинов    | oumm61@gmail.com       | 79788180198 | f84468c04f82bf1c9d45eacf80b2090f27f6d1b3 | 62.76.12.249   | 2015-12-23 12:35:12 |                  |      99053 | Севастополь     | Глухова 9-60                           |
| Елена       | Кретова    | helena_919@mail.ru     | 79653992477 | fb6194abce58a41d7c08241d510472cf9ce156af | 93.174.118.7   | 2015-12-23 13:19:51 |                  |            | perm            | Березники, улица Свердлова 20          |
| Анастасия   | Бузырева   | avbuzyreva@yandex.ru   | 79048474594 | 8739b0c5495f87b75a2b0e08f66a1d53d1018c72 | 188.18.86.243  | 2015-12-23 17:19:41 |                  |            | Березники       | Котовского,40                          |
| Адиля       | Наумова    | naumovaad@mail.ru      | 79128835350 | ee6ac1754618f97918e7c7b4d4129dc348898e68 | 37.79.28.59    | 2015-12-24 17:50:03 |                  |     618409 | Березники       | И. Дощеникова, 12                      |
| Валентина   | Федорова   | andyrev98@mail.ru      | 79082529653 | eb05f9e38d57e2b3c3e61a942be7b7c5fe2a9eea | 93.90.107.219  | 2015-12-26 15:45:18 |                  |            | Березники       | Ломоносова 97-1                        |
| Владимир    | Власов     | record104@mail.ru      | 79082568498 | 403cd2d5dd987b2b3d26aa8964672e68238bc50d | 5.141.232.50   | 2015-12-27 13:07:19 |                  |     617001 | Нытва           | Ленина                                 |
| Петр        | Анфалов    | apelsin-90@mail.ru     | 79522489700 | 1a548acb54f87e5ec89ba6e9e315e7c75d574a5e | 176.59.202.34  | 2015-12-27 17:56:25 |                  |     197371 | Санкт-Петербург | Мартыновская ул                        |
```


## About final data
> - Total rows: 3019

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
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.77% |
| Phones | 95.33% |
| Address | 99.87% |
| Ips | 100.00% |
| Works | 4.84% |
| Accounts | 100.00% |
| Actuality | 100.00% |



### Data sample
```
| names                  | emails                     | phones          | address                                                 | ips                                           | works                                                                                                    | accounts                                                                                                                                       | actuality   |
|:-----------------------|:---------------------------|:----------------|:--------------------------------------------------------|:----------------------------------------------|:---------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Миронов Денис']      | ['logosat@mail.ru']        | ['79024714707'] | ['Пермь Ш Космонавтов']                                 | [Row(ip='178.47.72.186', date='11.12.2015')]  | [Row(post=None, date_start=None, date_end=None, company='ИнтерСтромСервис', address=None, comment=None)] | [Row(title='аэробас.рф', link='https://аэробас.рф', login='logosat@mail.ru', password_hash='874f4cbbba06db73e6b4342e90639fe392efdb2f')]        | 11.12.2015  |
| ['Осипик Вячеслав']    | ['agronom.perm@mail.ru']   | ['79223083859'] | ['Пермь Пермь']                                         | [Row(ip='46.146.238.129', date='22.12.2015')] |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='agronom.perm@mail.ru', password_hash='3462f23e17944ba6cc2e2f7e6c6db0e350395f61')]   | 22.12.2015  |
| ['Попова Елена']       | ['lowe1977@mail.ru']       | ['79194718878'] | ['614065 Пермь г. Пермь ул. Шоссе Космонавтов 326А-12'] | [Row(ip='46.146.221.130', date='22.12.2015')] |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='lowe1977@mail.ru', password_hash='541bba86f97fe8220f6fa2e48ab774a6b9505193')]       | 22.12.2015  |
| ['Буланова Полина']    | ['polina-kupcova@mail.ru'] | ['79125872606'] | ['Пермь Ивана Франко 44']                               | [Row(ip='37.79.0.183', date='22.12.2015')]    |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='polina-kupcova@mail.ru', password_hash='c680eb8b0d9669c0f6db2b58648916b91606240b')] | 22.12.2015  |
| ['Шляпин Владимир']    | ['79082662691@ya.ru']      | ['79082662691'] | ['Березники Мира 34-12']                                | [Row(ip='188.17.149.127', date='22.12.2015')] |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='79082662691@ya.ru', password_hash='4ccb0bf1968babf8cada3d31ca11aed816c75ee0')]      | 22.12.2015  |
| ['Лалетина Мария']     | ['lemon_25@list.ru']       | ['79194475513'] | ['Березники Свердлова 59']                              | [Row(ip='195.64.208.173', date='22.12.2015')] |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='Lemon_25@list.ru', password_hash='74f550f0c7e503dc116aeaadeb8291ca1fcd7ac7')]       | 22.12.2015  |
| ['Бычина Мария']       | ['markiza_@bk.ru']         | ['79223661196'] | ['Пермь Сочинская 6-54']                                | [Row(ip='194.190.5.136', date='22.12.2015')]  |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='markiza_@bk.ru', password_hash='87a184f6f6cb6df1a6269ca0ba5dcbe4d634af25')]         | 22.12.2015  |
| ['Гунгер Желанна']     | ['zelanna777@yandex.ru']   | ['79128852671'] | ['Березники Мира ул 112-4']                             | [Row(ip='188.168.78.245', date='22.12.2015')] |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='zelanna777@yandex.ru', password_hash='9d2c4fd1970191060a19d9ac6f72c9ed747c3620')]   | 22.12.2015  |
| ['Логинов Андрей']     | ['oumm61@gmail.cdom']      | ['79788080198'] | ['299053 Севастополь Глухова9']                         | [Row(ip='62.76.12.227', date='22.12.2015')]   |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='oumm61@gmail.cdom', password_hash='250a860408cbdb565563d17af1dce77199c16fb1')]      | 22.12.2015  |
| ['Шмыков Александр']   | ['shmikovall@gmail.com']   | ['79026490790'] | ['618426 Березники Комсомольская 4 - 4']                | [Row(ip='77.236.71.248', date='22.12.2015')]  |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='shmikovall@gmail.com', password_hash='3962a38acea331d4c0119ee37631aaaf4c6f3d4f')]   | 22.12.2015  |
| ['Кудряшев Станислав'] | ['kirasa@ya.ru']           | ['79024764155'] | ['пермь Качалова21-34']                                 | [Row(ip='37.76.144.24', date='22.12.2015')]   |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='kirasa@ya.ru', password_hash='2f46f19081bd284140fe4437f3348475c6ad4cf9')]           | 22.12.2015  |
| ['Кузнецов Роман']     | ['romochka-4@gmail.com']   | ['79125904825'] | ['Пермь Боровая 2-14']                                  | [Row(ip='5.141.194.213', date='22.12.2015')]  |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='romochka-4@gmail.com', password_hash='cb670a10dbdaeaf2e77801fce6c6d584a0fb208d')]   | 22.12.2015  |
| ['Краснов Владимир']   | ['xateee@gmail.com']       | ['79824510784'] | ['615008 Пермь Красновишерская 35']                     | [Row(ip='46.146.213.90', date='23.12.2015')]  |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='xateee@gmail.com', password_hash='7a6b30fad8dbd362c34fce250c49c37696d6155a')]       | 23.12.2015  |
| ['Логинов Андрей']     | ['oumm61@gmail.com']       | ['79788180198'] | ['99053 Севастополь Глухова 9-60']                      | [Row(ip='62.76.12.249', date='23.12.2015')]   |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='oumm61@gmail.com', password_hash='f84468c04f82bf1c9d45eacf80b2090f27f6d1b3')]       | 23.12.2015  |
| ['Кретова Елена']      | ['helena_919@mail.ru']     | ['79653992477'] | ['perm Березники улица Свердлова 20']                   | [Row(ip='93.174.118.7', date='23.12.2015')]   |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='helena_919@mail.ru', password_hash='fb6194abce58a41d7c08241d510472cf9ce156af')]     | 23.12.2015  |
| ['Бузырева Анастасия'] | ['avbuzyreva@yandex.ru']   | ['79048474594'] | ['Березники Котовского40']                              | [Row(ip='188.18.86.243', date='23.12.2015')]  |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='avbuzyreva@yandex.ru', password_hash='8739b0c5495f87b75a2b0e08f66a1d53d1018c72')]   | 23.12.2015  |
| ['Наумова Адиля']      | ['naumovaad@mail.ru']      | ['79128835350'] | ['618409 Березники И. Дощеникова 12']                   | [Row(ip='37.79.28.59', date='24.12.2015')]    |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='naumovaad@mail.ru', password_hash='ee6ac1754618f97918e7c7b4d4129dc348898e68')]      | 24.12.2015  |
| ['Федорова Валентина'] | ['andyrev98@mail.ru']      | ['79082529653'] | ['Березники Ломоносова 97-1']                           | [Row(ip='93.90.107.219', date='26.12.2015')]  |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='andyrev98@mail.ru', password_hash='eb05f9e38d57e2b3c3e61a942be7b7c5fe2a9eea')]      | 26.12.2015  |
| ['Власов Владимир']    | ['record104@mail.ru']      | ['79082568498'] | ['617001 Нытва Ленина']                                 | [Row(ip='5.141.232.50', date='27.12.2015')]   |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='record104@mail.ru', password_hash='403cd2d5dd987b2b3d26aa8964672e68238bc50d')]      | 27.12.2015  |
| ['Анфалов Петр']       | ['apelsin-90@mail.ru']     | ['79522489700'] | ['197371 Санкт-Петербург Мартыновская ул']              | [Row(ip='176.59.202.34', date='27.12.2015')]  |                                                                                                          | [Row(title='аэробас.рф', link='https://аэробас.рф', login='apelsin-90@mail.ru', password_hash='1a548acb54f87e5ec89ba6e9e315e7c75d574a5e')]     | 27.12.2015  |
```