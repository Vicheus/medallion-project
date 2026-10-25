# Parsetron results

## About row data

> - Code name: index_0142
> - File path: /media/user/SAMSUNG/Databases/index_0142/raw/kazany_preprocessed.csv
> - Total rows: 1565

### Schema
```
root
 |-- user_id: integer (nullable = true)
 |-- firstname: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- address_1_1: string (nullable = true)
 |-- address_1_2: string (nullable = true)
 |-- address_1_city: string (nullable = true)
 |-- address_1_zipcode: string (nullable = true)
 |-- address_2_1: string (nullable = true)
 |-- address_2_2: string (nullable = true)
 |-- address_2_city: string (nullable = true)
 |-- address_2_zipcode: string (nullable = true)
 |-- phone1: string (nullable = true)
 |-- phone2: string (nullable = true)
 |-- company: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone3: string (nullable = true)
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)

```

### Data sample
```
|   user_id | firstname                     | lastname   | address_1_1                                                 | address_1_2   | address_1_city   |   address_1_zipcode | address_2_1                                                 | address_2_2   | address_2_city   |   address_2_zipcode | phone1           | phone2           | company   | email                                   | phone3           | login     | password                                                     |
|----------:|:------------------------------|:-----------|:------------------------------------------------------------|:--------------|:-----------------|--------------------:|:------------------------------------------------------------|:--------------|:-----------------|--------------------:|:-----------------|:-----------------|:----------|:----------------------------------------|:-----------------|:----------|:-------------------------------------------------------------|
|         1 | Администратор                 | Главный    | Test                                                        | Прогресса, 1  | Красногорск      |              143407 | Test                                                        | Прогресса, 1  | Красногорск      |              143407 | +7(925)555-55-55 | +7(925)555-55-55 | Simtech   | info@kazany.ru                          | +7(925)555-55-55 | admin     | $2y$10$s9gu3sCHvF2Isa0g9OF21.qIh.OQDVOP/VVg40GDMrr9BcyyKBFvy |
|         3 | Покупатель                    | Первый     | Карла Маркса                                                |               | Калининград      |              236000 | Карла Маркса                                                |               | Калининград      |              236000 |                  |                  | Simtech   | customer@example.com                    | 77 77 777 7777   | customer  | 91ec1f9324753048c0096d036a694f86                             |
|         4 | Анна                          | Петрова    | Трудовой 17-25                                              |               | Тула             |              300911 | Трудовой 17-25                                              |               | Тула             |              300911 | +79278172311     | +79278172311     |           | user1@example.com                       | +79278172311     | user_4    | 7d55bd65cea460d6a432e3778c7f28f8                             |
|         5 | Мария                         | Иванова    | Кировск 17-107                                              |               | Светогорск       |              188992 | Кировск 17-107                                              |               | Светогорск       |              188992 | +79174310021     | +79174310021     |           | user2@example.com                       | +79174310021     | user_5    | 6036d5834e0aa75752947b095a0d0002                             |
|         6 | Ольга                         | Григорьева | Азовская 41-74                                              |               | Белово           |              652607 | Азовская 41-74                                              |               | Белово           |              652607 | +79512130041     | +79512130041     |           | user3@example.com                       | +79512130041     | user_6    | 9931f39915fb0342bab5c28f863ba4b9                             |
|         7 | Николай                       | Ворошилов  | Луговая 7-85                                                |               | Москва           |              119027 | Луговая 7-85                                                |               | Москва           |              119027 | +79510012311     | +79510012311     |           | user4@example.com                       | +79510012311     | user_7    | b5eec3edb2c5e23cee651093e03fdb3a                             |
|         8 | Елена                         | Михайлова  | Химки 17-104                                                |               | Пермь            |              614030 | Химки 17-104                                                |               | Пермь            |              614030 | +79272301124     | +79272301124     |           | user6@example.com                       | +79272301124     | user_8    | 6ae57dfea08e4ca117d79b366650ca18                             |
|        10 | Екатерина                     | Смирнова   | Успешная 6-45                                               |               | Омск             |              644013 | Успешная 6-45                                               |               | Омск             |              644013 | +79512331011     | +79512331011     |           | user8@example.com                       | +79512331011     | user_10   | af4106da5e00838c425ad8d2590946dd                             |
|        11 | Надежда                       | Ефимова    | Успешная 9-105                                              |               | Омск             |              644013 | Успешная 9-105                                              |               | Омск             |              644013 | +79023221458     | +79023221458     |           | user7@example.com                       | +79023221458     | user_11   | b0d60e7533b0d36c8e4799ae3f386836                             |
|        12 | Алексей                       | Маслов     | Никольская 4-12                                             |               | Воронеж          |              394080 | Никольская 4-12                                             |               | Воронеж          |              394080 | +79032125622     | +79032125622     |           | user9@example.com                       | +79032125622     | user_12   | db7713ba6ae01915bc71ea177ec0f1b7                             |
|        14 | Ксения                        | Родионова  | Салова 8-25                                                 |               | Санкт-Петербург  |              192102 | Салова 8-25                                                 |               | Санкт-Петербург  |              192102 | +79174453201     | +79174453201     |           | user13@example.com                      | +79174453201     | user_14   | f03e7984852302d7c6607b205e2e18a6                             |
|        43 | Ирина                         |            | ул. Маршала Блюхера                                         |               | Санкт-Петербург  |              194021 | ул. Маршала Блюхера                                         |               | Санкт-Петербург  |              194021 |                  |                  |           | domashevskayaiv@mail.ru                 |                  | user_43   | 2a9453fb08331787c4d7f3c0b8f7705b                             |
|       659 | Ruslan                        |            |                                                             |               |                  |                     |                                                             |               |                  |                     | +7(926)055-87-96 | +7(926)055-87-96 |           | shel.put@yandex.ru                      | +7(926)055-87-96 | user_659  | 9cb2fa0d751cd0037b67d771d3b7a874                             |
|      1510 | Кристина                      | Климова    | krisklimova, gmail.com                                      |               | Курган           |              640000 | krisklimova, gmail.com                                      |               | Курган           |              640000 | +7(912)970-04-77 | +7(912)970-04-77 |           | Krisklimova@gmail.com                   |                  | user_1510 | d8371d56ffa84072ca50c0195fc675b7                             |
|      1513 | Кристина                      | Климова    | krisklimova, gmail.com                                      |               | Курган           |              640000 | г.Курган, ул.Зорге, 35                                      |               | Курган           |              640000 | +7(912)970-04-77 |                  |           | klimova-kristina-1575001906@example.com | +7(912)970-04-77 | user_1513 | b3a98d8286702cb3e60d9168a734a9bb                             |
|      1520 | Алексей                       | Дурнев     | Знаменка,19                                                 |               | Фрязино          |              141190 | Знаменка,19                                                 |               | Фрязино          |              141190 |                  |                  |           | av@mywebsupport.ru                      | +7(777)777-77-77 | user_1520 | $2y$10$9sRQ2rhma22r/7pNc6Ouz.dblwxXtMsIDEbhBAjM8GYI9BAYZeJzK |
|      3328 | JasonElole                    | JasonElole | москва                                                      |               | москва           |              151115 | москва                                                      |               | москва           |              152242 | 81294136985      | 83588938543      |           | mmf-01@mail.ru                          | 83588938543      | user_3328 | aacbd17d18e04d25fbbab085333a87d7                             |
|      3700 | Борис                         |            | г. Воронеж, Московский пр-кт, дом 90 корпус 1, квартира 119 |               | Воронеж          |              394000 | г. Воронеж, Московский пр-кт, дом 90 корпус 1, квартира 119 |               | Воронеж          |              394000 | +7(906)680-26-78 | +7(906)680-26-78 |           | pensar@mail.ru                          | +7(906)680-26-78 | user_3700 | ed7c009c713bd421df07d3525a484d70                             |
|      3740 | Худолей Николай Александрович |            | ул. Рябиновая,  владение 38Б / стр. 6, квартира 10 / T1754  |               | Москва           |              121471 | ул. Рябиновая,  владение 38Б / стр. 6, квартира 10 / T1754  |               | Москва           |              121471 | +7(926)982-87-18 | +7(926)982-87-18 |           | Vahan24@yahoo.com                       | +7(926)982-87-18 | user_3740 | 5c22762a04b6bbf43fd6b599e1d1ec25                             |
|      3773 | Дмитрий                       |            | 3-я Мытищинская, дом 16А                                    |               | Москва           |              129226 | 3-я Мытищинская, дом 16А                                    |               | Москва           |              129226 | +7(925)063-82-72 | +7(925)063-82-72 |           | sdv@inbox.ru                            | +7(925)063-82-72 | user_3773 | 8c34bd5d5aa83cadca41bdabd4ed792e                             |
```

> - Code name: index_0142
> - File path: /media/user/SAMSUNG/Databases/index_0142/raw/kazany_preprocessed-2.csv
> - Total rows: 3360

### Schema
```
root
 |-- firstname: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- address_1_1: string (nullable = true)
 |-- address_1_2: string (nullable = true)
 |-- address_1_city: string (nullable = true)
 |-- address_1_zipcode: string (nullable = true)
 |-- address_2_1: string (nullable = true)
 |-- address_2_2: string (nullable = true)
 |-- address_2_city: string (nullable = true)
 |-- address_2_zipcode: string (nullable = true)
 |-- phone1: string (nullable = true)
 |-- phone2: string (nullable = true)

```

### Data sample
```
| firstname                     | lastname   | address_1_1                                                 | address_1_2   | address_1_city   |   address_1_zipcode | address_2_1                                                 | address_2_2   | address_2_city   |   address_2_zipcode | phone1           |       phone2 |
|:------------------------------|:-----------|:------------------------------------------------------------|:--------------|:-----------------|--------------------:|:------------------------------------------------------------|:--------------|:-----------------|--------------------:|:-----------------|-------------:|
| Виктория                      | Смирнова   | Авиационая 4-62                                             |               | Липецк           |              398042 | Авиационая 4-62                                             |               | Липецк           |              398042 | +79021121582     | +79021121582 |
| Николай                       | Ворошилов  | Луговая 7-85                                                |               | Москва           |              119027 | Луговая 7-85                                                |               | Москва           |              119027 | +79510012311     | +79510012311 |
| Ольга                         | Григорьева | Азовская 41-74                                              |               | Белово           |              652607 | Азовская 41-74                                              |               | Белово           |              652607 | +79512130041     | +79512130041 |
| Надежда                       | Ефимова    | Успешная 9-105                                              |               | Омск             |              644013 | Успешная 9-105                                              |               | Омск             |              644013 | +79023221458     | +79023221458 |
| Мария                         | Иванова    | Кировск 17-107                                              |               | Светогорск       |              188992 | Кировск 17-107                                              |               | Светогорск       |              188992 | +79174310021     | +79174310021 |
| Алексей                       | Маслов     | Никольская 4-12                                             |               | Воронеж          |              394083 | Никольская 4-12                                             |               | Воронеж          |              394083 | +79032125622     | +79032125622 |
| Елена                         | Михайлова  | Химки 17-104                                                |               | Пермь            |              614030 | Химки 17-104                                                |               | Пермь            |              614030 | +79272301124     | +79272301124 |
| Анна                          | Петрова    | Трудовой 17-25                                              |               | Тула             |              300911 | Трудовой 17-25                                              |               | Тула             |              300911 | +79278172311     | +79278172311 |
| Екатерина                     | Смирнова   | Успешная 6-45                                               |               | Омск             |              644013 | Успешная 6-45                                               |               | Омск             |              644013 | +79512331011     | +79512331011 |
| Светлана                      | Дмитриева  | Мира 8-674                                                  |               | Санкт-Петербург  |              197183 | Мира 8-674                                                  |               | Санкт-Петербург  |              197183 | +79092352122     | +79092352122 |
| Ксения                        | Родионова  | Салова 8-25                                                 |               | Санкт-Петербург  |              192102 | Салова 8-25                                                 |               | Санкт-Петербург  |              192102 | +79174453201     | +79174453201 |
| Ольга                         | Григорьева | Азовская 41-74                                              |               | Белово           |              650000 | Азовская 41-74                                              |               | Белово           |              650000 | +79512130041     | +79512130041 |
| Алексей                       | Маслов     | Никольская 4-12                                             |               | Воронеж          |              394080 | Никольская 4-12                                             |               | Воронеж          |              394080 | +79032125622     | +79032125622 |
| Кристина                      | Климова    | krisklimova, gmail.com                                      |               | Курган           |              640000 | г.Курган, ул.Зорге, 35                                      |               | Курган           |              640000 | +7(912)970-04-77 |              |
| Борис                         |            | г. Воронеж, Московский пр-кт, дом 90 корпус 1, квартира 119 |               | Воронеж          |              394000 | г. Воронеж, Московский пр-кт, дом 90 корпус 1, квартира 119 |               | Воронеж          |              394000 | +7(906)680-26-78 |              |
| Худолей Николай Александрович |            | ул. Рябиновая,  владение 38Б / стр. 6, квартира 10 / T1754  |               | Москва           |              121471 | ул. Рябиновая,  владение 38Б / стр. 6, квартира 10 / T1754  |               | Москва           |              121471 | +7(926)982-87-18 |              |
| Дмитрий                       |            | 3-я Мытищинская, дом 16А                                    |               | Москва           |              129226 | 3-я Мытищинская, дом 16А                                    |               | Москва           |              129226 | +7(925)063-82-72 |              |
| Александр                     | Волков     |                                                             |               | Казань           |              420000 |                                                             |               | Казань           |              420000 |                  |              |
| Шилова                        | Марина     | Холмогорова 23 152                                          |               | Ижевск           |              426000 |                                                             |               | Ижевск           |              426000 | +7(912)854-40-81 |              |
| Шакаев                        | Зелимхан   | Изюмская 34/1 квартира 5                                    |               | Москва           |              117624 | Изюмская 34/1 квартира 5                                    |               | Москва           |              117624 | +7(960)345-40-40 |              |
```


## About final data
> - Total rows: 4553

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
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```

### Data sample
```
| names                 | emails                         | phones          | address                                                                               | accounts                                                                                                                                              | works   |
|:----------------------|:-------------------------------|:----------------|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|
| ['Владислав']         | ['chvv-197008@mail.ru']        | ['79257040888'] | ['101000 Москва Тихорецкий б-р д. 1 стр. 5']                                          | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_6963', password_hash='$2y$10$ltWT3q3rxVJhPZAGI1Irp.0vSxbSHXPMGcA4PT2XQ7xqYSXxNxrlG')]  |         |
| ['Максим']            |                                | ['79295615775'] | ['101000 Москва Бескудниковский б-р д. 11к. 1кв. 137']                                | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_8688', password_hash='$2y$10$.Q7LZPWJCW5PHcmfANuJa.6BHad0ycU3Oc9XQsAm3sOYu7/lxEt82')]  |         |
| ['Лукашин']           | ['oleg-lukashin@mail.ru']      | ['79168077900'] | ['140144 Рылеево Пос Рылеево ул Шоссейная дом 55']                                    | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_9625', password_hash='$2y$10$Jra8WP.Drann3ls85IIlB.mEKg3PjHGHA/lfiPfZ83/G69uviC.lu')]  |         |
| ['Александр']         | ['ms_voice@list.ru']           | ['79787062036'] |                                                                                       | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_9940', password_hash='$2y$10$Sy/pkJxkmopWENanSiAGf.3a4ISBr9zRCZQy9WSA1vVemj1vrTdDu')]  |         |
| ['Максим']            | ['mmw.1990@mail.ru']           | ['79264738919'] |                                                                                       | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_11659', password_hash='$2y$10$6d35L5OUFnphI1LQd/DnIuCWLjDlied.bKeO1LzygazK89H5Kt41O')] |         |
| ['Андрей']            | ['liav64@rambler.ru']          | ['79165181180'] | ['101000 Москва Щелковский р-н СНТ Купол 444']                                        | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_13489', password_hash='$2y$10$yz6mT1BrKsZqgz/oK3CDwOOCgLo5IWhLbBS9Fvor8mV4CxASh95IC')] |         |
| ['Илья']              | ['8003716@gmail.com']          | ['79268003716'] |                                                                                       | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_15436', password_hash='$2y$10$f.66i2h0y8AXRt6aWzsKzOsCwtGaHznAHWKLA/AO3I1ge1Lhfj8fO')] |         |
| ['Елена']             | ['s.elena.r@mail.ru']          | ['79373521677'] |                                                                                       | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_17580', password_hash='$2y$10$o6eZV1Nz6vPsldqyqOLGc..3C0YyQTeN9QGdiKOX5Hjx7/AN8qYi2')] |         |
| ['Данила']            | ['emelyanov.d.yu@yandex.ru']   | ['79199634129'] | ['101000 Москва Лазурная 10']                                                         | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_17822', password_hash='$2y$10$7LKeacYqlmsfeQj/ZVpum.oUsQKUHiMxUg4qOPSKQFlPVEz1qfNqS')] |         |
| ['Виктор']            |                                | ['79260481451'] | ['101000 Москва ул.Юнных ленинцев д.113 корп.4']                                      | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_18848', password_hash='$2y$10$pNHl7e3.Ru2nZGdygJtjCOHIPVqTPN/kJM6ng2Hgc8y0TKZWFoR2W')] |         |
| ['Сергей']            | ['ivk9@mail.ru']               | ['79218835838'] |                                                                                       | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_20107', password_hash='$2y$10$loYZnb675RjachUJOW1AKOrvd9OIiU419Fhk4n46/BJlDXfm.LdZi')] |         |
| ['Андрей']            | ['ronald7sa@gmail.com']        | ['79166173863'] | ['141400 Химки г.Химки Московская обл мкр Сходня ул Микояна д 10 корп 21 кв 2']       | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_20404', password_hash='$2y$10$Zj6.Wrc5ub9/PbnPbRyPM.oEarQI0VfDd4DAXVycyJHyaT8A3HkQS')] |         |
| ['Юрий']              | ['de_vikol@mail.ru']           | ['79659119979'] | ['655016 Абакан Ул. Торосова д.15 кв.149']                                            | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_9410', password_hash='$2y$10$4.igkvDu4uOWqdzTIVLZrOZTGL2rIuBrBZ6iDLW6H3FNpvLa7ipEK')]  |         |
| ['Александр']         | ['bav6@yandex.ru']             | ['79152334923'] | ['101000 Москва Туристская 13 корп. 1 кв. 36']                                        | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_10935', password_hash='$2y$10$yu3Tk1u2.BdrWUfTV5Svo.4hVscAK7VSOwap21VjBTKZ2LjBf1fwq')] |         |
| ['Дмитрий']           | ['dim.solovev17@gmail.com']    | ['79017519020'] |                                                                                       | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_11352', password_hash='$2y$10$FlJ1kw5XD8FlzmjajNfA5eovCnSIyNLET20CYqgTXjwTNKzRYPcS.')] |         |
| ['Георгий']           | ['krupnovgeorge@yandex.ru']    | ['79032010897'] | ['101000 Москва Щелковское шоссе39 кв.69']                                            | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_11467', password_hash='$2y$10$qfL7Sd/CLsgdXlOyHjL.Ouduez6xlvYZlrecu.X2iIjfq09KYLh2G')] |         |
| ['Евгений']           | ['polyakoff.92@mail.ru']       | ['79853585108'] | ['101000 Москва Южное медведково ул. Заповедная д. 2 кв. 52']                         | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_14579', password_hash='$2y$10$tN2YF00im5BUHx.ca94RhOJCgkxcvCL24pOyskAKiyjglYVT.YCIm')] |         |
| ['Роман']             | ['urv1972@yandex.ru']          | ['79152596059'] |                                                                                       | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_17307', password_hash='$2y$10$3F3mUdxTNG87nL/o2OxicuM9WNsGsK7ZeWoRhJaG.K/u.OaOLUWNy')] |         |
| ['Сокуренко Валерий'] | ['valery.sokurenko@gmail.com'] | ['79302710222'] | ['142800 Ступино Нижегородская областьгород Борпосёлок Октябрьскийбаза отдыха Дубки'] | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_19332', password_hash='$2y$10$r/i5pX72Qow6.lG7mesEheCzM6vudBZHy/QVJLhmHj.qLXtqqpovO')] |         |
| ['Валерий']           |                                | ['79165910670'] |                                                                                       | [Row(title='Kazany.ru', link='https://kazany.ru/', login='user_9957', password_hash='$2y$10$ncepl/qC3L0ZzRpN47Vqs.r8V2oMMjY312u.gSbMLruXDUqfv8WRC')]  |         |
```