# Parsetron results

## About row data

> - Code name: index_0417
> - File path: cleaned.csv
> - Total rows: 73546782

### Schema
```
root
 |-- id: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- name: string (nullable = true)
 |-- password: string (nullable = true)
 |-- country: string (nullable = true)
 |-- currency: string (nullable = true)
 |-- role: string (nullable = true)
 |-- activity: string (nullable = true)
 |-- time_registration: string (nullable = true)
 |-- birthday: string (nullable = true)
 |-- passport: string (nullable = true)
 |-- address: string (nullable = true)
 |-- passport_by: string (nullable = true)
 |-- partner_key: string (nullable = true)
 |-- last_ip: string (nullable = true)
 |-- last_ip_country: string (nullable = true)
 |-- tg_id: string (nullable = true)
 |-- timezone: string (nullable = true)
 |-- hash_id: string (nullable = true)
 |-- note: string (nullable = true)
 |-- poker_nickname: string (nullable = true)
 |-- firstdeposit_time: string (nullable = true)
 |-- bk_type: string (nullable = true)
 |-- deposits_calc_count: string (nullable = true)
 |-- deposits_calc_time: string (nullable = true)
 |-- regulated_domain_id: string (nullable = true)
 |-- tenant_id: string (nullable = true)

```

### Data sample
```
| id   | email                            | phone           | name                       | password                                                           | country   | currency   | role   | activity   | time_registration     | birthday      | passport   | address   | passport_by   | partner_key       | last_ip           | last_ip_country   | tg_id    | timezone   | hash_id   | note   | poker_nickname   | firstdeposit_time     | bk_type   | deposits_calc_count   | deposits_calc_time    | regulated_domain_id   | tenant_id   |
|:-----|:---------------------------------|:----------------|:---------------------------|:-------------------------------------------------------------------|:----------|:-----------|:-------|:-----------|:----------------------|:--------------|:-----------|:----------|:--------------|:------------------|:------------------|:------------------|:---------|:-----------|:----------|:-------|:-----------------|:----------------------|:----------|:----------------------|:----------------------|:----------------------|:------------|
| `id` | `email`                          | `phone`         | `name`                     | `password`                                                         | `country` | `currency` | `role` | `activity` | `time_registration`   | `birthday`    | `passport` | `address` | `passport_by` | `partner_key`     | `last_ip`         | `last_ip_country` | `tg_id`  | `timezone` | `hash_id` | `note` | `poker_nickname` | `firstdeposit_time`   | `bk_type` | `deposits_calc_count` | `deposits_calc_time`  | `regulated_domain_id` | `tenant_id` |
| 1    | 'cto@1win.pro'                   | '52999999991'   | 'Добавил параметр userId ' | '99b8daa6e3989db69cf421b6a5b25ff8e8a1726d6c785bda59b631b6280f7786' | 'ru'      | 'RUB'      | 3      | 0          | '2017-08-28 19:04:21' | 1044039120    | ''         | ''        | ''            | ''                | '82.102.74.185'   | 'cy'              | NULL     | -3         | NULL      | '-'    | 'fe0dor'         | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 2    | 'remezzov@gmail.com'             | '52999999992'   | 'Изменил параметр userId ' | '07a289e900c0383da870e58dd9b7835cccc98e3dc16a8dcdfbedca90711c8dd2' | 'ru'      | 'RUB'      | 1      | 0          | '2017-08-25 22:17:25' | 1012503120    | ''         | ''        | ''            | ''                | '217.66.157.70'   | 'ru'              | NULL     | -3         | NULL      | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 3    | 'ulyevg@gmail.com'               | '+79312080768'  | 'Гриша Земельный'          | 'dd83d30a745a562c0d29dcdb4cb5149003f884ec8d678f3a4eaaedb041ea7963' | 'ru'      | 'VIETH'    | 3      | 0          | '2017-06-08 18:28:24' | 690843600000  | ''         | ''        | ''            | ''                | '82.102.65.189'   | 'cy'              | NULL     | -3         | NULL      | NULL   | 'repka'          | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 4    | 'root@root.ru'                   | '+77777777'     | 'Alex'                     | '49c5065cfdfd226ab54670153021a500d400299edab056a6fba940fc99735306' | 'ru'      | 'RUB'      | 3      | 0          | '2017-07-20 00:35:45' | 646689600000  | ''         | ''        | ''            | ''                | '212.23.211.69'   | 'ru'              | NULL     | -3         | NULL      | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 5    | 'qqhellokitty1@gmail.com'        | '380681750095'  | 'Сергей'                   | 'ff683dc7924fb163885c8f685ee3c04a9b9772da37139f72c7e23f0e6a155398' | 'ru'      | 'INR'      | 3      | 0          | '2017-08-03 18:36:20' | 730846800000  | ''         | ''        | ''            | ''                | '213.149.188.176' | 'cy'              | 28493564 | -3         | NULL      | NULL   | 'ddrsftyghjj'    | '2022-12-09 22:43:15' | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 6    | 'klimilan22@gmail.com'           | '+380638333050' | 'Егор'                     | '140d3c394ee04980cc3914f80f2bfaa56e4627f4b0c39520e868e6420602cfe7' | 'ru'      | 'RUB'      | 1      | 0          | '2017-08-04 16:05:21' | 0             | ''         | ''        | ''            | ''                | '193.34.94.22'    | 'ua'              | NULL     | -3         | NULL      | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 7    | 'mironros@gmail.com'             | '+380634877659' | 'Дмитрий'                  | 'fc695aafe4d38fe455e90bdf685a970e62e19fa7c0cee23668b7ae2cac40cb4d' | 'ru'      | 'RUB'      | 1      | 0          | '2017-06-06 22:12:09' | 0             | ''         | ''        | ''            | ''                | '213.110.145.144' | 'ua'              | NULL     | NULL       | NULL      | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 8    | 'ravilchik_95@mail.ru'           | '+79059322436'  | 'Равиль'                   | 'e7d38db4d8c465be23c0edff2a5b5e0855086fcb8b7b5c577f8680f540d615b1' | 'ru'      | 'RUB'      | 1      | 0          | '2017-06-07 17:39:35' | 806864400000  | ''         | ''        | ''            | 'ZcExVzY0ThdcOX8' | ''                | 'ru'              | NULL     | NULL       | 55        | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 9    | 'bbrlz@mail.ru'                  | '+79119452969'  | 'Артем'                    | 'fc9d961d52d7751dcb1da56cca757bc77724ed339b55b398ce8daa282f9d0bc0' | 'ru'      | 'RUB'      | 1      | 0          | '2017-08-07 15:28:47' | 718923600000  | ''         | ''        | ''            | 'ZcExVzY0ThdcOX8' | '91.204.150.176'  | 'ru'              | NULL     | NULL       | 55        | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 10   | 'negmat331987@mail.ru'           | '+79676358315'  | 'Негмат'                   | 'bc43dec0565b5d662002af5011d703d530c7d0afe406ef87b1af1ac91295ede0' | 'ru'      | 'RUB'      | 1      | 0          | '2017-06-07 17:44:33' | 374612400000  | ''         | ''        | ''            | 'ZcExVzY0ThdcOX8' | ''                | 'ru'              | NULL     | NULL       | 55        | NULL   | NULL             | '2022-11-20 16:53:34' | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 11   | 'aakh1955@bk.ru'                 | '89992027789'   | 'Айбулат'                  | '99d29ff906f2065617eca25b79f10cde6b92b923b873a2abfe54fc6680aa05cf' | 'ru'      | 'RUB'      | 1      | 0          | '2017-08-10 16:26:33' | 703713600000  | ''         | ''        | ''            | ''                | '92.62.121.102'   | 'in'              | NULL     | -3         | NULL      | NULL   | 'VAdiM777'       | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 12   | 'lidel3@bk.ru'                   | '+79992230420'  | 'OG3'                      | 'c92ef6f4916ea5b1351935ad9265b4d14dbd10f57758a1254812b545282b9c17' | 'ru'      | 'RUB'      | 1      | 0          | '2017-06-07 18:19:32' | 813186000000  | ''         | ''        | ''            | ''                | '193.56.113.32'   | 'fi'              | NULL     | -3         | NULL      | NULL   | 'ogkush33333333' | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 13   | 'otabekrixsieb@gmail.com'        | '+79637808091'  | 'Murad'                    | '9050d010ff981c2a3f3ada2348324043f4953ffb0324f88b7e8d697d5ed0dbf4' | 'ru'      | 'RUB'      | 1      | 0          | '2017-06-07 18:25:42' | 838414800000  | ''         | ''        | ''            | 'ZcExVzY0ThdcOX8' | ''                | 'ru'              | NULL     | NULL       | 55        | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 14   | 'Thebestofthebest1313@yandex.ru' | '+79787383550'  | 'Алексей'                  | 'e98903a7a0572dffbc0cd68f20581ad86c1e951bd1962358d4d68a6577c7a5e9' | 'ru'      | 'RUB'      | 1      | 0          | '2017-06-07 19:38:16' | 408402000000  | ''         | ''        | ''            | 'ZcExVzY0ThdcOX8' | ''                | 'ru'              | NULL     | NULL       | 55        | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 15   | 'maikl1922@bk.ru'                | '+79645046137'  | 'Михаил'                   | '3cd026487277043faa748ea2f0d5c15cb0c41d01b5c9c1494ee7f6f92d22699a' | 'ru'      | 'RUB'      | 1      | 0          | '2017-06-07 19:42:01' | 484261200000  | ''         | ''        | ''            | 'ZcExVzY0ThdcOX8' | ''                | 'ru'              | NULL     | NULL       | 55        | NULL   | NULL             | '2024-07-28 16:22:12' | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 16   | 'fara7887@mail.ru'               | '+998933970492' | 'Фарход'                   | 'c2ba6a2a29ff8d0cbfa58ca305f945993a6ef8e6e02a8ef887154a97e14805bb' | 'uz'      | 'RUB'      | 1      | 0          | '2017-06-07 19:43:20' | 268254000000  | ''         | ''        | ''            | 'ZcExVzY0ThdcOX8' | ''                | 'ru'              | NULL     | NULL       | 55        | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 17   | 'sham-vlad@mail.ru'              | '+79603882547'  | 'Влад'                     | '171867f0c888c0995c80d4aa2d3125f2831d06481a6da0c540ede55465c8a3e0' | 'ru'      | 'RUB'      | 1      | 0          | '2017-06-07 19:52:32' | 250801200000  | ''         | ''        | ''            | 'AVeOaXcuK03Vi6q' | ''                | 'ru'              | NULL     | NULL       | 56        | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 18   | 'Sam.rabotaa@mail.ru'            | '+79627026350'  | 'AleXYoRkE19'              | 'ebd5bd2b33f304c3c4b2f46348eb41399ae4f8cf0084ea046b8cbb16deecee5d' | 'ru'      | 'RUB'      | 1      | 0          | '2017-06-07 19:57:11' | 490046400000  | ''         | ''        | ''            | 'ZcExVzY0ThdcOX8' | '89.113.98.111'   | 'ru'              | NULL     | -3         | 55        | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
| 19   | 'djentelmen.akbar.jon@yandex.ru' | '+79631478871'  | 'Акба'                     | '49440677c657c2d673a3cc0a0769a4153d9dcb5fff0f6071e8c9dc2da9824a2c' | 'ru'      | 'RUB'      | 1      | 0          | '2017-06-07 20:32:04' | 1494709200000 | ''         | ''        | ''            | 'ZcExVzY0ThdcOX8' | ''                | 'ru'              | NULL     | NULL       | 55        | NULL   | NULL             | NULL                  | '1win'    | 0                     | '2021-09-16 13:11:57' | 0                     | 1           |
```


## About final data
> - Total rows: 5631591

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |    |    |-- id: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |-- actuality: string (nullable = true)

```



### Data sample
```
| names               | phones          | emails                              | address   | socials   | accounts                                                                                                                                                                              | documents   | birth_date   | ips                         | actuality   |
|:--------------------|:----------------|:------------------------------------|:----------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|:-------------|:----------------------------|:------------|
| ['Фарход']          |                 | ['fara7887@mail.ru']                |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='fara7887@mail.ru', password_hash='c2ba6a2a29ff8d0cbfa58ca305f945993a6ef8e6e02a8ef887154a97e14805bb', id='16')]                 |             |              |                             | 16.09.2021  |
| ['Nurbek']          | ['77716373812'] | ['nurbek_1226@mail.ru']             |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='nurbek_1226@mail.ru', password_hash='80cf38e3da076273583f1b3176f942b1695a771c982f28db92c17cceb5d146d7', id='24')]              |             |              |                             | 16.09.2021  |
| ['Exolon']          |                 | ['stalker6788@gmail.com']           |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='stalker6788@gmail.com', password_hash='02f142777f41ffcbc9a8017606570827c98e1223f70a0534e9700b6c8356b659', id='44')]            |             |              | [Row(ip='188.217.161.200')] | 16.09.2021  |
| ['Афруз']           |                 | ['afruz.nishonov@mail.ru']          |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='afruz.nishonov@mail.ru', password_hash='7c2b079cf2b1afb9e23c933326f2579a5384b99e2f71014b2da2b1f050f656cd', id='66')]           |             |              |                             | 16.09.2021  |
| ['Куттыгул Шерхан'] | ['77479135091'] | ['sherkhankz@mail.ru']              |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='Sherkhankz@mail.ru', password_hash='e51002cd9c10c321e26cb27ec6627241e6b9bfda4c0785ace6ea6d7773aa74f5', id='71')]               |             |              |                             | 16.09.2021  |
| ['Влад']            | ['77084867143'] | ['vlad.leonovich@mail.ru']          |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='Vlad.leonovich@mail.ru', password_hash='27898f216641a67f3a468590ce409e4431131c2217546969b7fd75546005dad1', id='105')]          |             |              | [Row(ip='185.61.218.65')]   | 16.09.2021  |
| ['Роман']           | ['77078203036'] | ['roma_futbol.99@list.ru']          |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='roma_futbol.99@list.ru', password_hash='a72d3a791ba9ab45ea3d2ff6672c272aae611d3f7eb493b7cfe8b9aedb61fcd7', id='114')]          |             |              |                             | 16.09.2021  |
| ['Маэстро']         | ['77758861696'] | ['meirlanbaidilda21@gmail.com']     |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='meirlanbaidilda21@gmail.com', password_hash='f55a7ec588f81d42622caba5240d90070e52deccf50804d624b17b46f9a7c51f', id='138')]     |             |              |                             | 16.09.2021  |
| ['Арман']           | ['77712503821'] | ['dreamerarm@mail.ru']              |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='dreamerarm@mail.ru', password_hash='b37440e6edd2597a8c2437d3e878dcd4c9e333358c79886d372b5c98bc46b657', id='142')]              |             |              | [Row(ip='134.228.157.193')] | 16.09.2021  |
| ['Зокир']           |                 | ['zokir1983.n@gmail.com']           |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='zokir1983.n@gmail.com', password_hash='d05f71f0ab319e7090c31567ab180f5df5b9eaea54afd7f9bf7d0473c0203627', id='147')]           |             |              |                             | 16.09.2021  |
| ['Сардор']          |                 | ['mn48jumabaev.sardor95@gmail.com'] |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='mn48jumabaev.sardor95@gmail.com', password_hash='22faf92b1f001a3078a92f36c1afc2511f1613d6848d0db97498ebc0e04ced37', id='172')] |             |              |                             | 16.09.2021  |
| ['Roland']          | ['77477545426'] | ['mr.adyoha@gmail.com']             |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='mr.adyoha@gmail.com', password_hash='ec3ba1130b5e327f6ff901a3057e37d38be56100aac6eafa5bb6015aeaba27dd', id='191')]             |             |              |                             | 16.09.2021  |
| ['Даврон']          |                 | ['t770@bk.ru']                      |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='T770@bk.ru', password_hash='0ab14c70a3d8eaf7d200de1d1ecd84fdb3c738981d789431ddb99e7f8f5f1617', id='215')]                      |             |              | [Row(ip='217.8.47.213')]    | 16.09.2021  |
| ['Александр']       | ['77052602389'] | ['fix0011@yandex.ru']               |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='fix0011@yandex.ru', password_hash='e7ce1fa1255239bc6d93bea92077c00af3e22a7393d7ca75c0e352cc041c4c5b', id='218')]               |             |              | [Row(ip='45.144.31.63')]    | 16.09.2021  |
| ['Шокан']           | ['77759970456'] | ['shoka_13.96@mail.ru']             |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='shoka_13.96@mail.ru', password_hash='8ee30d96014c6dea7a1e529571394f706c125f710b2d3530a277eca2532d1b0a', id='271')]             |             |              |                             | 16.09.2021  |
| ['Шахзод']          | ['77476684351'] | ['s-ayap@mail.ru']                  |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='s-ayap@mail.ru', password_hash='9dbba013f5fa3d5da22cf6364762925e98924e263b4b62497b319af8d74b8bb9', id='316')]                  |             |              | [Row(ip='87.243.17.116')]   | 16.09.2021  |
| ['Даурен']          | ['77055661869'] | ['zholzhanov-bekzat@mail.ru']       |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='zholzhanov-bekzat@mail.ru', password_hash='a08414aec35f195815cc4d2bbb2d17ce8a2579dbe99b84fe4a31bdb4894bf6df', id='354')]       |             |              | [Row(ip='95.57.23.4')]      | 16.09.2021  |
| ['Жумагазы']        |                 | ['zsatbay@bk.ru']                   |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='zsatbay@bk.ru', password_hash='30071253f2ef61fadb3487984a4149d8fabb59646e17ac725edeb5fa7fe9ab83', id='375')]                   |             |              | [Row(ip='80.89.201.36')]    | 16.09.2021  |
| ['Владимир']        | ['77079217096'] | ['warlait@mail.ru']                 |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='warlait@mail.ru', password_hash='cc84243a942dd9a37ef3f29354ffb38f5e609f54fe748d9483c4f92aa2e46913', id='403')]                 |             |              |                             | 16.09.2021  |
| ['Виталий']         | ['77051364778'] | ['vitas2899@mail.ru']               |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='vitas2899@mail.ru', password_hash='d8141bfe62413a8505468f24e9263b0049875c5636a864800bf8f99ef0cb4ec0', id='449')]               |             |              | [Row(ip='196.196.203.124')] | 16.09.2021  |
```