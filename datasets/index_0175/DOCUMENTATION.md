# Parsetron results

## About row data

> - File path: preprocessed.csv
> - Total rows: 237288

### Schema
```
root
 |-- customers_id: integer (nullable = true)
 |-- customers_email_address: string (nullable = true)
 |-- customers_telephone: string (nullable = true)
 |-- customers_password: string (nullable = true)
 |-- street: string (nullable = true)
 |-- postcode: string (nullable = true)
 |-- city: string (nullable = true)
 |-- fullname: string (nullable = true)
 |-- address2: string (nullable = true)
 |-- phone2: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- ip_date: timestamp (nullable = true)

```

### Data sample
```
|   customers_id | customers_email_address      | customers_telephone   | customers_password               | street                                                                                             |   postcode | city                               | fullname          | address2                                                                                           | phone2            | email2                       | ip              | ip_date             |
|---------------:|:-----------------------------|:----------------------|:---------------------------------|:---------------------------------------------------------------------------------------------------|-----------:|:-----------------------------------|:------------------|:---------------------------------------------------------------------------------------------------|:------------------|:-----------------------------|:----------------|:--------------------|
|             11 | savva34@yandex.ru            | 91425-299-77          | fd26661b3b7aa201269837dd2b54fbcb | Советская 13|7, кв 15                                                                              |            | Республика Саха (Якутия) г. Мирный | Юлия  Савинцева   | ул. Советская 18А, кв 28                                                                           | 89142529977       | savva34@yandex.ru            | 10.64.95.16     | 2011-08-31 07:45:26 |
|             14 | chedrova@mail.ru             | 89104558355           | 9880132d48590aca22077e6d3ffbae3e | ул. Амурская, д.7                                                                                  |     107497 | Москва                             | Ольга  Щедрова    | Духовской пер. 10-87                                                                               | 89104558355       | chedrova@mail.ru             | 91.77.32.157    | 2011-11-13 10:43:15 |
|             14 | chedrova@mail.ru             | 89104558355           | 9880132d48590aca22077e6d3ffbae3e | ул. Амурская, д.7                                                                                  |     107497 | Москва                             | Ольга  Щедрова    | Амурская, 7                                                                                        | 8-910-455-83-55   | chedrova@mail.ru             | 85.140.104.199  | 2010-12-11 22:35:53 |
|             14 | chedrova@mail.ru             | 89104558355           | 9880132d48590aca22077e6d3ffbae3e | ул. Амурская, д.7                                                                                  |     107497 | Москва                             | Ольга  Щедрова    | Духовской пер. 10-87                                                                               | 89104558355       | chedrova@mail.ru             | 84.253.90.118   | 2010-08-16 16:45:59 |
|             14 | chedrova@mail.ru             | 89104558355           | 9880132d48590aca22077e6d3ffbae3e | Духовской пер. 10-87                                                                               |            | Москва                             | Ольга  Щедрова    | Духовской пер. 10-87                                                                               | 89104558355       | chedrova@mail.ru             | 91.77.32.157    | 2011-11-13 10:43:15 |
|             14 | chedrova@mail.ru             | 89104558355           | 9880132d48590aca22077e6d3ffbae3e | Духовской пер. 10-87                                                                               |            | Москва                             | Ольга  Щедрова    | Амурская, 7                                                                                        | 8-910-455-83-55   | chedrova@mail.ru             | 85.140.104.199  | 2010-12-11 22:35:53 |
|             14 | chedrova@mail.ru             | 89104558355           | 9880132d48590aca22077e6d3ffbae3e | Духовской пер. 10-87                                                                               |            | Москва                             | Ольга  Щедрова    | Духовской пер. 10-87                                                                               | 89104558355       | chedrova@mail.ru             | 84.253.90.118   | 2010-08-16 16:45:59 |
|             18 | 280374n@rambler.ru           | 8 915 329 03 08       | 984f4014883a1a4c947b647746674f6d | 1-ый Новоподмосковный переулок,д.2/1                                                               |            | Москва                             | Наталия  Панкова  | 1-ый Новоподмосковный переулок, д2/1                                                               | 8 915 329 03 08   | 280374n@rambler.ru           | 188.123.252.163 | 2011-12-08 11:57:26 |
|             18 | 280374n@rambler.ru           | 8 915 329 03 08       | 984f4014883a1a4c947b647746674f6d | 1-ый Новоподмосковный переулок,д.2/1                                                               |            | Москва                             | Наталия  Панкова  | 1-ый Новоподмосковный переулок, д2/1                                                               | 8 915 329 03 08   | 280374n@rambler.ru           | 85.140.248.210  | 2010-12-12 18:35:05 |
|            740 | greenwall@nextmail.ru        | 8-926-060-07-14       | 7b6a1dc3a5de4e7ce04b5b99733fe751 | ул. 3-я Рыбинская, д. 1 ОАО "Хонты-Мансийский" банк                                                |            | Москва                             | ольга  красникова | ул. 3-я Рыбинская, д. 1 ОАО "Хонты-Мансийский" банк                                                | 8-926-060-07-14   | greenwall@nextmail.ru        | 213.33.214.22   | 2011-01-13 14:42:46 |
|             69 | hbabiyan@rencap.com          | 89037690882           | bcb591517cb8b866af64e71ba194ded9 | пресненская наб 10, блок С                                                                         |            | Москва                             | Елена  Бабиян     | Пресненская наб 10, блок С                                                                         | 890379690882      | hbabiyan@rencap.com          | 213.221.33.54   | 2010-11-24 12:45:52 |
|             75 | kiska444@mail.ru             | 9660378018            | 2f4c70126684472c51aeff06c4139f1f | москва тц атриум земляной вал 33                                                                   |     101000 | москва                             | людмила  климчук  | ворошилова 153 - 52                                                                                | 8-916-016-51-47   | kiska444@mail.ru             | 95.73.88.71     | 2011-04-26 22:56:12 |
|           1876 | legioneks@gmail.com          | 782-30-27             | 4caa0d8159c8223d4567a9023e9e3480 | Рубцовская набережная д.3 стр.1                                                                    |     105082 | Москва                             | Светлана  Козлова | Рубцовская набережная д.3 стр.1                                                                    | 782-30-27         | legioneks@gmail.com          | 92.36.35.20     | 2012-02-01 00:37:29 |
|           1876 | legioneks@gmail.com          | 782-30-27             | 4caa0d8159c8223d4567a9023e9e3480 | Рубцовская набережная д.3 стр.1                                                                    |     105082 | Москва                             | Светлана  Козлова | Рубцовская набережная д.3 стр.1                                                                    | 782-30-27         | legioneks@gmail.com          | 92.36.14.178    | 2011-10-31 23:01:36 |
|           1877 | marinabell@mail.ru           | 89140802312           | 04315489b4db6c3cdb1fe18470836615 | ул.Дежнева 39, кв.22                                                                               |     689251 | Провидения                         | Марина  Сапрыкина | ул.Дежнева 39, кв.22                                                                               | 89140802312       | marinabell@mail.ru           | 194.84.68.162   | 2011-11-01 09:26:22 |
|           1878 | afonya111@yandex.ru          | 8-905-5685696         | e175aed73c5fc7f58ca0762c4358afe9 | метро Электрозаводская, ул. Малая Семеновская, 3А, стр. 2 (бизнес центр на территории ЦНИИ шерсть) |     107023 | Москва                             | Алла  Баранова    | метро Электрозаводская, ул. Малая Семеновская, 3А, стр. 2 (бизнес центр на территории ЦНИИ шерсть) | 8-905-5685696     | afonya111@yandex.ru          | 95.163.68.130   | 2011-11-01 17:37:45 |
|            156 | kondratenko_ox@mail.ru       | 8 (926) 239-22-79     | 2db5af16da1098474d1a0661e3b25bf2 | Дербеневская набережная, д. 7, стр. 12, этаж 2                                                     |    0000000 | Москва                             | Оксана  Громова   | Проспект Мира д. 95 стр. 1 офис 203                                                                | 8 (926) 239-22-79 | kondratenko_ox@mail.ru       | unknown         | 2011-09-19 11:06:40 |
|            156 | kondratenko_ox@mail.ru       | 8 (926) 239-22-79     | 2db5af16da1098474d1a0661e3b25bf2 | Дербеневская набережная, д.7, стр. 12, этаж 2                                                      |    0000000 | Москва                             | Оксана  Громова   | Проспект Мира д. 95 стр. 1 офис 203                                                                | 8 (926) 239-22-79 | kondratenko_ox@mail.ru       | unknown         | 2011-09-19 11:06:40 |
|           2565 | garanina_oksana@geprobank.ru | 8-925-060-33-34       | 174de820206a9c5e0c8caf2608b6c446 | метро Академическая ул. Ново- Черемушкинская, дом 18                                               |     142793 | москва                             | оксана  гаранина  | метро Академическая ул. Ново- Черемушкинская, дом 18 18                                            | 8-925-060-33-34   | garanina_oksana@geprobank.ru | 82.138.40.153   | 2012-02-21 16:41:15 |
|           2565 | garanina_oksana@geprobank.ru | 8-925-060-33-34       | 174de820206a9c5e0c8caf2608b6c446 | метро Академическая ул. Ново- Черемушкинская, дом 18 18                                            |     142793 | москва                             | оксана  гаранина  | метро Академическая ул. Ново- Черемушкинская, дом 18 18                                            | 8-925-060-33-34   | garanina_oksana@geprobank.ru | 82.138.40.153   | 2012-02-21 16:41:15 |
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
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.86% |
| Phones | 98.11% |
| Ips | 99.75% |
| Address | 84.20% |
| Accounts | 100.00% |
| Actuality | 100.00% |



### Data sample
```
| names                  | emails                            | phones                         | ips                                                                        | address                                                                                                                                            | accounts                                                                                                                       | actuality   |
|:-----------------------|:----------------------------------|:-------------------------------|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Валерия']            | ['astral1979@yandex.ru']          | ['79775569913', '79167800012'] | [Row(ip='109.188.124.37', date=None)]                                      | ['1-й Красногвардейский проезд 15', 'Москва г Москва ул Юных Ленинцев д 66', '125364 Санкт-Петербург фывфыв', '413111 Москва ул. Мира 346 кв. 78'] | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='1', password_hash='629dc3ac02aaef4dad26cf44dd6cb646')]     | 28.05.2015  |
| ['Светлана']           | ['astral1979@yandex.ru']          | ['79775569913', '79167828284'] | [Row(ip='109.188.127.22', date=None)]                                      | ['улица Кирова 5', 'Москва г Москва ул Юных Ленинцев д 66', '125364 Санкт-Петербург фывфыв', '413111 Москва ул. Мира 346 кв. 78']                  | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='1', password_hash='629dc3ac02aaef4dad26cf44dd6cb646')]     | 07.07.2015  |
| ['Кравец Елена']       | ['emkravets@gmail.com']           | ['79688248936']                | [Row(ip='109.68.184.72', date=None), Row(ip='134.209.190.168', date=None)] | ['пр-кт Ломоносовский д 25 к 5', '117447 Москва Дмитрия Ульянова 31', 'г Москва пр-кт Ломоносовский д 25 к 5']                                     | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='10310', password_hash='69d123df2514ef9968984d72792982ff')] | 22.05.2020  |
| ['Альбина Муратова']   | ['ibina21@rambler.ru']            | ['79160172527']                | [Row(ip='37.110.51.36', date=None)]                                        | ['2ой Сетуньский проезд д11 кв 92', '1111 москва 2ой Сетуньский проезд д11 кв 92']                                                                 | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='10374', password_hash='ee070fb03467f5fa41d3d37a343491d1')] | 26.02.2014  |
| ['Анна Хорошая']       | ['luizade@rambler.ru']            | ['79163239811']                | [Row(ip='176.193.23.214', date=None)]                                      | ['ул. Б. Андроньевская д.18', '109544 Москва ул. Б. Андроньевская д.18']                                                                           | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='10515', password_hash='a8108cd718e9e4eaaef9c08262a029a2')] | 08.03.2014  |
| ['Галина Егорова']     | ['enasamson@mail.ru']             | ['79184603050']                | [Row(ip='31.181.127.143', date=None), Row(ip='46.159.21.100', date=None)]  | ['ул.Зиповская 14 кв.84', '350072 Краснодар ул.Зиповская 14 кв.84']                                                                                | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='10554', password_hash='64efe5c1c19911f3dc7df442d929cddd')] | 20.05.2014  |
| ['Ольга Иванова']      | ['lilavaty79@mail.ru']            | ['79162670596']                | [Row(ip='188.123.237.9', date=None)]                                       | ['ул. Краснодарская д. 76 кв. 137', '109469 Москва ул. Краснодарская д. 76 кв. 137']                                                               | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='10691', password_hash='1ed71aeea3f83b5e8a52b4616ea20786')] | 22.11.2014  |
| ['Татьяна Савченко']   | ['zhuminskaya@inbox.ru']          | ['79269302948']                | [Row(ip='46.188.5.7', date=None)]                                          | ['Славянский бульвар д5 к.1', '121352 Москва Славянский бульвар д5 к.1']                                                                           | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='10810', password_hash='0e48ef901c11242289911f3d21f1926c')] | 25.03.2014  |
| ['Ксения Ковалёва']    | ['kseniya_kovaleva_2013@mail.ru'] | ['79140413561']                | [Row(ip='176.123.200.12', date=None)]                                      | ['Амурская обл г.Благовещенск ул.Мухина 87кв.6', '675 000 Благовещенск Амурская обл г.Благовещенск ул.Мухина 87кв.6']                              | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='11115', password_hash='d0ed0a6cf4848c2dd87d74c48c7341b1')] | 22.08.2014  |
| ['Вера Красовская']    | ['krasovskayavm@gmail.com']       | ['79388679510']                | [Row(ip='37.146.62.152', date=None)]                                       | ['п Российский ул Измаильская д 72', '350087 Краснодар п Российский ул Измаильская д 72']                                                          | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='11137', password_hash='321b4085169d85b89e4aa4cf71054a6e')] | 22.03.2021  |
| ['Ольга Конюхова']     | ['kolgavancouver@yahoo.com']      | ['74955430803']                | [Row(ip='194.186.75.11', date=None)]                                       | ['Тестовская 10', 'Москва Молодогвардейская 2 С 3']                                                                                                | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='1115', password_hash='e459ff7b49f85c77ba52430f1bc029d1')]  | 25.07.2011  |
| ['Вера Караугланова']  | ['altervita@list.ru']             | ['79660671000']                | [Row(ip='109.252.151.248', date=None), Row(ip='91.208.232.63', date=None)] | ['ул Заповедная д 16 к 3 кв 1', '125009 Москва Большой Кисловский пер д.13', 'Большой Кисловский пер д.13']                                        | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='11485', password_hash='da65cdfe625c488ea0d64f07c26cf417')] | 13.04.2022  |
| ['Людмила Кошелева']   | ['ludmila-graf@mail.ru']          | ['79607256919']                | [Row(ip='109.126.202.220', date=None)]                                     | ['ул. Горького д. 85-Б кв. 30', '600005 Владимир ул. Горького д. 85-Б кв. 30']                                                                     | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='11780', password_hash='1464dc452b320ce7cbfbb5dcfa843e30')] | 28.05.2014  |
| ['Татьяна Климовских'] | ['klimovskih_tanya@mail.ru']      | ['79265227745']                | [Row(ip='87.228.20.228', date=None)]                                       |                                                                                                                                                    | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='11869', password_hash='914bfa1dc9293e7f6286277294412a14')] | 04.06.2014  |
| ['Людмила Малушина']   | ['pazitifchik@list.ru']           | ['79851269068']                | [Row(ip='91.77.107.42', date=None)]                                        | ['Сретенский бульвар 61 подъезд 5 кв 52', '101000 Москва Сретенский бульвар 61 подъезд 5 кв 52']                                                   | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='12271', password_hash='b401e03ddb3a68303899449c18412286')] | 01.07.2014  |
| ['Кириченко Елена']    | ['kiritchenkoea@gmail.com']       | ['79265033454']                | [Row(ip='185.144.136.152', date=None)]                                     | ['проезд Павелецкий 3-й д 3', '115035 Москва Кадашевская набережная 30']                                                                           | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='12725', password_hash='827ccb0eea8a706c4c34a16891f84e7b')] | 31.08.2020  |
| ['Мария Перова']       | ['artdf.marie@gmail.com']         | ['79197210423']                | [Row(ip='89.207.94.139', date=None)]                                       | ['Ул.1812 Года 10 К.1Кв 58', '121170 Москва ул.1812 года 10 к.1кв 58']                                                                             | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='12817', password_hash='4792cbb52f0104713694b9c8a3490064')] | 04.08.2014  |
| ['Лина Тимохина']      | ['lina_team@yahoo.com']           | ['79039663155']                | [Row(ip='83.220.236.237', date=None)]                                      | ['ул. Большая Филевская д. 2', '121087 Москва ул. Большая Филевская д. 2']                                                                         | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='12938', password_hash='4051caba22d0913dc9659fa6b92f87eb')] | 12.08.2014  |
| ['Карина']             | ['selins@mail.ru']                | ['79160310124']                | [Row(ip='89.20.33.40', date=None), Row(ip='188.254.16.138', date=None)]    | ['пер Орликов д 3Б', '107139 Москва Орликов переулок 3Б', 'б-р Измайловский д 3']                                                                  | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='13178', password_hash='bb22d585272f2d5994e5bb7e937b3a79')] | 10.03.2022  |
| ['Пеньковская Юлия']   | ['juliasochi@inbox.ru']           | ['79183080787']                | [Row(ip='95.27.55.91', date=None), Row(ip='37.146.245.150', date=None)]    | ['г Сочи ул Карла Либкнехта д 13 кв 60', '354000 Сочи улица Карла Либкнехта 13 кв 60']                                                             | [Row(title='Hairpersona.ru', link='https://www.hairpersona.ru', id='13262', password_hash='809f34fc5fa0bf27d2d6d589845b5ad3')] | 26.11.2022  |
```