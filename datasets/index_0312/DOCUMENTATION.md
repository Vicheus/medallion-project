# Parsetron results

## About row data

> - File path: users_devices_preprocessed.csv
> - Total rows: 71188

### Schema
```
root
 |-- dmid: integer (nullable = true)
 |-- dua: string (nullable = true)

```

### Data sample
```
|   dmid | dua                                                                                                                                          |
|-------:|:---------------------------------------------------------------------------------------------------------------------------------------------|
|  73807 | Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36                                       |
|  73811 | Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36                                 |
|  73814 | Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko                                                                                |
|  24932 | Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)                                                                       |
|  47320 | Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36                                 |
|  16798 | Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)                                                                       |
|  41697 | Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36 OPR/34.0.2036.50 (Edition Yx) |
|  73832 | Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.23 Safari/537.36                                        |
|  73585 | Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36                                       |
|  17420 | Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36 OPR/31.0.1889.99               |
|  64508 | Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36 OPR/34.0.2036.50                      |
|  54827 | Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko                                                                         |
|  71666 | Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko                                                                   |
|  13652 | Mozilla/5.0 (Windows NT 6.0; rv:43.0) Gecko/20100101 Firefox/43.0                                                                            |
|    898 | Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 YaBrowser/15.12.1.6475 Safari/537.36          |
|  32221 | Mozilla/5.0 (Windows NT 5.0; rv:12.0) Gecko/20100101 Firefox/12.0                                                                            |
|  52115 | Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko                                                                                |
|  41503 | Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36                                       |
|  59942 | Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36                                 |
|  28554 | Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko                                                                         |
```

> - File path: members_preprocessed.csv
> - Total rows: 108477

### Schema
```
root
 |-- member_id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- ip_address: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- last_activity: integer (nullable = true)
 |-- members_pass_hash: string (nullable = true)
 |-- vk_id: string (nullable = true)
 |-- profession: string (nullable = true)
 |-- sex: string (nullable = true)
 |-- city: string (nullable = true)
 |-- full_name: string (nullable = true)

```

### Data sample
```
|   member_id | name               | email                    | ip_address      | birth_date   |   last_activity | members_pass_hash                                            | vk_id   | profession           | sex   | city       | full_name   |
|------------:|:-------------------|:-------------------------|:----------------|:-------------|----------------:|:-------------------------------------------------------------|:--------|:---------------------|:------|:-----------|:------------|
|           1 | CDS                | management@metrologu.ru  | 81.201.254.82   |              |      1749560397 | $2y$10$km19uZ6oQbm010CGy8yegOInc/I.biXHsuzN2nyIRYDvAjLwJsw3G |         | Главный редактор     | муж   | Тюмень     |             |
|           2 | Гл. метролог       | rk84@mail.ru             | 94.181.221.153  | 1984-4-27    |      1749531593 | $2y$10$Ez9mxKCyP3D7z7GJVKlUoeRB/KRfwXFY4.B8omBTGe9AD7oHxbMLy |         | инженер-метролог     | муж   | Тюмень     |             |
|           3 | Metr               | ds@cherednicov.ru        | 92.255.165.73   | 1978-6-10    |      1741971674 | $2y$10$gUWX7e9LJa.RUZQIq9Wnx.055f6pJSTKxhY40OgiAkuhHymDIOGYu |         | инженер-метролог РТИ |       | Тюмень     |             |
|           5 | ПГСер              | kanyukovm@mail.ru        | 92.255.165.73   | 0-0-0        |      1310894742 | cf575b5f4b139771b3f625ad670e7707                             |         |                      |       |            |             |
|           7 | MSrv               | srvmd@yandex.ru          | 217.118.79.36   | 0-0-0        |      1442254327 | f4ab8f5133b6e1740e4861b251dff37a                             |         | инженер              | муж   | Челябинск  |             |
|           8 | Alexey             | alex325@list.ru          | 217.118.79.38   |              |      1318225290 | fbab123c5f4d50d50b80c3d7d58be063                             |         |                      |       |            |             |
|           9 | Иванов В.А.        | ivannvaa@mail.ru         | 92.255.162.15   |              |      1317926136 | fad630e3291547e2642e805674a5698f                             |         |                      |       |            |             |
|          10 | Mindoz             | mindozzz@rdkmail.ru      | 94.181.216.74   |              |      1678184222 | $2y$10$oRozg0.SvDb7qy/ep348EOomXAOW7b.vkIGek5/CW9r3lWKaDQApm |         |                      |       |            |             |
|          11 | LabIgr             | lalab@mail2k.ru          | 94.181.216.74   |              |      1310802041 | a99ad73a2c5152b8343b2982984a423c                             |         |                      |       |            |             |
|          12 | rmetr              | roman_arh@inbox.ru       | 212.46.221.248  | 0-5-22       |      1749537427 | $2y$10$gMWduaWkqhTJGp8RXu0xnuYQV7OaO4IeAuzSjX8YKDcp2dheYD.Rm |         | метролог             | муж   |            | Роман       |
|          13 | ATP                | atrrt@gmail.com          | 217.118.83.143  |              |      1318176143 | e21af2ac0a540071239d7a1226f58894                             |         |                      |       |            |             |
|          15 | light              | borislavskay@ngs.ru      | 217.117.84.62   | 0-0-0        |      1527678958 | $2a$13$FpEwudyUZOrXoHFyBJDxoelxA8HbY/d3DVcHL0jcRiSowzQlGaNZW |         |                      | жен   |            |             |
|          17 | Docent             | andrei-docent_77@mail.ru | 217.118.83.141  |              |      1586631788 | $2y$10$TQ8zHl/KEFy2RguR60ZD2u5Z1ZUfnbYcoUAFDXvvMCerxervF.Wz. |         |                      |       |            |             |
|          18 | nik                | nik13131313@yandex.ru    | 85.26.183.11    |              |      1435158194 | 84eddc82b36f544c8bcf7cffa867dab0                             |         |                      |       |            |             |
|          20 | MMM                | preilov@mailin.ru        | 217.195.217.38  |              |      1310296082 | caae5da92a017c3001e9c1211b6b8e60                             |         |                      |       |            |             |
|          21 | Kovica             | ko_victory@sibmail.com   | 213.183.106.251 | 1985-1-1     |      1437711823 | 0a9a35fbae9991ab1a2479b9d38355a3                             |         |                      | жен   | Tomsk      |             |
|          23 | механик            | kravcovaa_17@mail.ru     | 77.235.200.18   |              |      1741164869 | $2y$10$skP57T9nSQ2/lBrd0nMy0.cijEbeLeMOue1j6R.TdM.K54.u98ta2 |         |                      |       |            |             |
|          25 | Alekseitkachenko72 | tkachenko_alekse@mail.ru | 212.124.13.17   | 1972-1-28    |      1317235190 | ece816bd57ddb93c7d7066ad4cbbe066                             |         |                      | муж   | Ивановская |             |
|          27 | Metrob             | info@metrob.ru           | 82.119.159.152  | 0-0-0        |      1357644411 | 2681e60a9e4d92e709cb992468de4344                             |         |                      |       |            |             |
|          28 | Алекс              | sidelnikov_a_a@mail.ru   | 82.151.112.109  |              |      1509440577 | $2a$13$S9kg0mbgPFN3VfqACt6b4uFPM0CLA37NlQ5pbfbfKF.Bgeof2z5y6 |         |                      |       |            |             |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- actuality: string (nullable = true)
 |-- emails: array (nullable = true)
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
 |-- devices: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- action: string (nullable = false)
 |    |    |-- user_agent: string (nullable = true)
 |    |    |-- date: void (nullable = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)

```

### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 3.06% |
| Sex | 1.54% |
| Address | 52.17% |
| Actuality | 100.00% |
| Emails | 100.00% |
| Accounts | 100.00% |
| Works | 73.66% |
| Devices | 22.11% |
| Ips | 100.00% |


### Data sample
```
| names                              | birth_date   |   sex | address             | actuality   | emails                          | accounts                                                                                                                                                                      | works                                                                                                      | devices                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | ips                                            |
|:-----------------------------------|:-------------|------:|:--------------------|:------------|:--------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------|
| ['Verhniy']                        |              |   nan |                     | 20.10.2020  | ['drovosekov@ntu18.ru']         | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='verhniy', password_hash='$2y$10$r67dMFA919SWTteHAAuVKeU66xu7r0cvv8oVL0qXeHpZVIliVZWQK')]           |                                                                                                            | [Row(action='Login', user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 YaBrowser/18.1.1.839 Yowser/2.5 Safari/537.36', date=None)]                                                                                                                                                                                                                                                                                                  | [Row(ip='78.85.38.44', date='20.10.2020')]     |
| ['Зауре']                          |              |   nan |                     | 12.04.2018  | ['aig-2009@mail.ru']            | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='зауре', password_hash='$2a$13$kwOlwEfsxF6GJSJRcl9szut7XU/UOTSDJyW784Gv4bhKuZuZpqD5K')]             |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='178.88.226.202', date='12.04.2018')]  |
| ['Xkatelijnex', 'Екатерина']       |              |   nan | ['Санкт-Петербург'] | 09.08.2018  | ['ekaterinaboitsowa@gmail.com'] | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='xkatelijnex', password_hash='$2a$13$jJ3Yltw2oZYFJdKU1tfVkup0zmY7LnfK8JT/6kFHL0s7yBQgbvdi.')]       |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='94.25.229.73', date='09.08.2018')]    |
| ['Иван М']                         |              |   nan |                     | 18.03.2019  | ['ivanmyakota@mail.ru']         | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='Иван М', password_hash='$2y$10$V/WCiSwPDyggqSAwgaRjIOONrB11kbBVKpz4vww0FbHIykrIx4zxS')]            |                                                                                                            | [Row(action='Login', user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', date=None)]                                                                                                                                                                                                                                                                                                                             | [Row(ip='80.70.230.81', date='18.03.2019')]    |
| ['Alifer']                         |              |   nan |                     | 11.04.2018  | ['a1ifer@yandex.ru']            | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='alifer', password_hash='$2a$13$L2TJUtc5WEQncIwqXqTW9OEBdU0Bl8QPZdjHqSocmmimWlr8yaYLy')]            |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='92.255.101.98', date='11.04.2018')]   |
| ['Pdv']                            |              |   nan |                     | 26.05.2020  | ['dpetlitskiy@gmail.com']       | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='pdv', password_hash='$2y$10$R8LmSLqUlXsl0JqkpkzIEuZvU3KUHgeWIb/rB0vDD0jcsP9Twctq6')]               |                                                                                                            | [Row(action='Login', user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0', date=None)]                                                                                                                                                                                                                                                                                                                                                                  | [Row(ip='95.167.7.60', date='26.05.2020')]     |
| ['Алексей']                        |              |   nan | ['Москва']          | 20.08.2018  | ['podkop1@yandex.ru']           | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='Podkop1990', password_hash='$2a$13$7HOzo0fisluRyNVp1AQTAelf0zqs.U0ohVnQaycKB/5QZp9uU8TKC')]        |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='83.220.239.200', date='20.08.2018')]  |
| ['Александромск']                  |              |   nan |                     | 18.07.2023  | ['mr.efimov89@mail.ru']         | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='АлександрОмск', password_hash='$2y$10$e5gjPlEIrGeI1uFjXRfVVe4nwi4e.boS3gW/8y2bP4..SBU8ZRJKe')]     |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='92.127.155.82', date='18.07.2023')]   |
| ['Олеся Васина', 'Олеся Олеговна'] |              |   nan | ['Истра']           | 23.09.2021  | ['lesia55510@mail.ru']          | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='Олеся Васина', password_hash='$2y$10$8Lbdk13ININx6NeBExR1k.nG1mk14uR36iBZVWHBeDIu2nWKhB1Aq')]      | [Row(post='Инженер- метролог', date_start=None, date_end=None, company=None, address=None, comment=None)]  | [Row(action='Login', user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36', date=None)]                                                                                                                                                                                                                                                                                                                            | [Row(ip='176.62.184.134', date='23.09.2021')]  |
| ['Евгений Оск']                    |              |   nan |                     | 14.10.2019  | ['dipsler@yandex.ru']           | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='Евгений ОСК', password_hash='$2y$10$cbIu2MvEVAKsm5kuDYCEluK64Xovwc73NmsvS4iOOd6uYDCHVcV/O')]       |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='193.16.208.4', date='14.10.2019')]    |
| ['Ksenija']                        |              |   nan |                     | 08.06.2018  | ['ksenijaoparina@mail.ru']      | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='ksenija@', password_hash='$2a$13$CHtiKhLf3gnVaixryPCs7uldgWVBqYyeP/RY/ir7AdvC8Dm1Gw4Ty')]          |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='178.155.4.172', date='08.06.2018')]   |
| ['Сергей Метролог', 'Сергей']      |              |   nan | ['Воронеж']         | 12.12.2022  | ['srybachev@kwsystems.ru']      | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='Сергей Метролог', password_hash='$2y$10$hPdp99HcDNFWXYoaygzB2uPlHRJ1HXAaOhntK2bg5oG9837NZzFyu')]   | [Row(post='Инженер испытатель', date_start=None, date_end=None, company=None, address=None, comment=None)] |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='188.235.7.82', date='12.12.2022')]    |
| ['Дмитрий Маломыр']                |              |   nan |                     | 15.12.2019  | ['dmitrii_meshalkin@mail.ru']   | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='Дмитрий (маломыр)', password_hash='$2y$10$I0etzuGnUfBBUO.RnIqHJ.WZN.hoqAMy0.Ks.1WgAYpzAwIgdsVTe')] |                                                                                                            | [Row(action='Login', user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', date=None), Row(action='Login', user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36', date=None), Row(action='Login', user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', date=None)] | [Row(ip='80.83.234.206', date='15.12.2019')]   |
| ['Vosamoilenko']                   |              |   nan |                     | 14.06.2018  | ['vosamoilenko@gmail.com']      | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='VOSamoilenko', password_hash='$2a$13$LXy578QIbW59GRlS7KgqSOj0vUiPDSaXYeKT3Xckw6d5f9yC8s9JG')]      |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='31.200.196.68', date='14.06.2018')]   |
| ['Weedthecatz']                    |              |   nan |                     | 16.07.2018  | ['nickmisis1@gmail.com']        | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='weedthecatz', password_hash='$2a$13$Fh8qrtaBEoQdFxBWF56jFu9/z.ck6MI9bQnalCjkx4DIBe2AT61AO')]       |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='188.235.137.183', date='16.07.2018')] |
| ['Rdgroupltd']                     |              |   nan |                     | 05.07.2018  | ['ceo@rdgroupltd.com']          | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='RDGROUPLTD', password_hash='$2a$13$XNvBnfy00ODvzcK3m59RluCXxGnaJoiQR364ZLWRgNgB9iClFh5B2')]        |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='37.18.254.180', date='05.07.2018')]   |
| ['Василий Петрович']               |              |   nan | ['Москва']          | 16.07.2018  | ['prolex93@gmail.com']          | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='Василий555', password_hash='$2a$13$ZVpkAuSEyKsIlwG6L3eSdeOn4NgrKOsoV8YON4btHNZ3FdhaCFh9W')]        | [Row(post='Почтальон', date_start=None, date_end=None, company=None, address=None, comment=None)]          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='94.25.169.28', date='16.07.2018')]    |
| ['Тамара Нестеренко']              |              |   nan |                     | 16.07.2018  | ['tomomusik@mail.ru']           | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='Тамара Нестеренко', password_hash='$2a$13$6lMWhG90tpkZvWYX8GcNpeXNuCbyIv1aZ2PK1fc7E2GueIiqx6MOW')] |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='212.119.164.254', date='16.07.2018')] |
| ['Пашка']                          |              |   nan |                     | 18.07.2018  | ['dani210683@mail.ru']          | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='Пашка', password_hash='$2a$13$j88KP5Ecznk549wmOG56p.ALxjF..gKU0LohOYO1.llED06vOqPoG')]             |                                                                                                            | [Row(action='Login', user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 YaBrowser/18.6.1.770 Yowser/2.5 Safari/537.36', date=None)]                                                                                                                                                                                                                                                                                                         | [Row(ip='109.120.45.19', date='18.07.2018')]   |
| ['Nikitametrolog']                 |              |   nan |                     | 25.07.2018  | ['gladkih572@gmail.com']        | [Row(title='Главный форум метрологов', link='https://metrologu.ru', login='nikita_metrolog', password_hash='$2a$13$HjZhpyGZT4apwAuCl5BZn.QDF73H2krFlZhknXX6PrQbkQwrXHU2i')]   |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Row(ip='83.139.159.43', date='25.07.2018')]   |
```