# Parsetron results

## About row data

> - Code name: index_0080
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
> - Total rows: 3852529

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
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```



### Data sample
```
| names               | phones          | emails                             | address   | socials   | accounts                                                                                                                                                                            | documents   | birth_date   | ips                        | actuality   | raw_metadata                                                      |
|:--------------------|:----------------|:-----------------------------------|:----------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|:-------------|:---------------------------|:------------|:------------------------------------------------------------------|
| ['Гриша Земельный'] | ['79312080768'] | ['ulyevg@gmail.com']               |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='ulyevg@gmail.com', password_hash='dd83d30a745a562c0d29dcdb4cb5149003f884ec8d678f3a4eaaedb041ea7963', id='3')]                |             |              | [Row(ip='82.102.65.189')]  | 08.06.2017  | ['{"poker_nickname": "repka", "bk_type": "1win"}']                |
| ['Alex']            |                 | ['root@root.ru']                   |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='root@root.ru', password_hash='49c5065cfdfd226ab54670153021a500d400299edab056a6fba940fc99735306', id='4')]                    |             |              | [Row(ip='212.23.211.69')]  | 20.07.2017  | ['{"bk_type": "1win"}']                                           |
| ['Равиль']          | ['79059322436'] | ['ravilchik_95@mail.ru']           |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='ravilchik_95@mail.ru', password_hash='e7d38db4d8c465be23c0edff2a5b5e0855086fcb8b7b5c577f8680f540d615b1', id='8')]            |             |              |                            | 07.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Артем']           | ['79119452969'] | ['bbrlz@mail.ru']                  |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='bbrlz@mail.ru', password_hash='fc9d961d52d7751dcb1da56cca757bc77724ed339b55b398ce8daa282f9d0bc0', id='9')]                   |             |              | [Row(ip='91.204.150.176')] | 07.08.2017  | ['{"bk_type": "1win"}']                                           |
| ['Негмат']          | ['79676358315'] | ['negmat331987@mail.ru']           |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='negmat331987@mail.ru', password_hash='bc43dec0565b5d662002af5011d703d530c7d0afe406ef87b1af1ac91295ede0', id='10')]           |             |              |                            | 07.06.2017  | ['{"firstdeposit_time": "2022-11-20 165334", "bk_type": "1win"}'] |
| ['Murad']           | ['79637808091'] | ['otabekrixsieb@gmail.com']        |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='otabekrixsieb@gmail.com', password_hash='9050d010ff981c2a3f3ada2348324043f4953ffb0324f88b7e8d697d5ed0dbf4', id='13')]        |             |              |                            | 07.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Алексей']         | ['79787383550'] | ['thebestofthebest1313@yandex.ru'] |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='Thebestofthebest1313@yandex.ru', password_hash='e98903a7a0572dffbc0cd68f20581ad86c1e951bd1962358d4d68a6577c7a5e9', id='14')] |             |              |                            | 07.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Михаил']          | ['79645046137'] | ['maikl1922@bk.ru']                |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='maikl1922@bk.ru', password_hash='3cd026487277043faa748ea2f0d5c15cb0c41d01b5c9c1494ee7f6f92d22699a', id='15')]                |             |              |                            | 07.06.2017  | ['{"firstdeposit_time": "2024-07-28 162212", "bk_type": "1win"}'] |
| ['Влад']            | ['79603882547'] | ['sham-vlad@mail.ru']              |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='sham-vlad@mail.ru', password_hash='171867f0c888c0995c80d4aa2d3125f2831d06481a6da0c540ede55465c8a3e0', id='17')]              |             |              |                            | 07.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Акба']            | ['79631478871'] | ['djentelmen.akbar.jon@yandex.ru'] |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='djentelmen.akbar.jon@yandex.ru', password_hash='49440677c657c2d673a3cc0a0769a4153d9dcb5fff0f6071e8c9dc2da9824a2c', id='19')] |             |              |                            | 07.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Григорий']        | ['79523091333'] | ['belovgrigoriy1986@gmail.com']    |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='belovgrigoriy1986@gmail.com', password_hash='41bdf0d387cd8b9869cd42887c8dd385be600b2bac41310afe04a332ca1b3194', id='20')]    |             |              |                            | 07.06.2017  | ['{"firstdeposit_time": "2023-05-12 210513", "bk_type": "1win"}'] |
| ['Timur']           | ['79172425029'] | ['2hatab@mail.ru']                 |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='2hatab@mail.ru', password_hash='283b8cacce5639f12726b9a4e81f299c7e1db7153fec7843192c781a3f2cca71', id='21')]                 |             |              | [Row(ip='178.20.29.136')]  | 07.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Андрей']          |                 | ['19proshka.vyalyi82@mail.ru']     |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='19proshka.vyalyi82@mail.ru', password_hash='c75d3ef10df1cddeb402d6cc33050fc0343a49a99f5c482c11c3069b8286d05d', id='22')]     |             |              |                            | 07.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Андрей']          | ['79831740009'] | ['suhoday22@gmail.com']            |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='suhoday22@gmail.com', password_hash='af46f271558297f721313759470694f9194a52d1248c43867b538b491cb00e36', id='23')]            |             |              |                            | 07.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Nurbek']          |                 | ['nurbek_1226@mail.ru']            |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='nurbek_1226@mail.ru', password_hash='80cf38e3da076273583f1b3176f942b1695a771c982f28db92c17cceb5d146d7', id='24')]            |             |              |                            | 07.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Хосров']          | ['79992491206'] | ['koshtoyan97@bk.ru']              |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='koshtoyan97@bk.ru', password_hash='3de3a12faf15d098cac480aaced4a43008ce75a8161723e2d91cb5b0988fdcc2', id='25')]              |             |              | [Row(ip='177.174.115.97')] | 08.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Виталий']         | ['79601811359'] | ['mrkarnal@bk.ru']                 |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='mrkarnal@bk.ru', password_hash='dc9689da818675413281991864eeef7b5df97948cc6a00cef135a8c08452fe95', id='26')]                 |             |              |                            | 08.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Игореша']         | ['79148949722'] | ['igoreha-strahov@mail.ru']        |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='igoreha-strahov@mail.ru', password_hash='b39017c531e54bce1bbe10d847142128b9f6486aab8d0bba1225e9136a9b2d15', id='28')]        |             |              |                            | 08.06.2017  | ['{"bk_type": "1win"}']                                           |
| ['Andrey']          |                 | ['kikot040684@gmail.com']          |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='kikot040684@gmail.com', password_hash='72d458ca8dfead75d10314dd63738155cc24bed67b4b11535a8978384645856e', id='29')]          |             |              | [Row(ip='175.157.206.82')] | 08.06.2017  | ['{"firstdeposit_time": "2023-10-07 020643", "bk_type": "1win"}'] |
| ['Александр']       | ['79994650013'] | ['konev54@yandex.ru']              |           |           | [Row(title='1Win', link='https://www.p218.ru/', login='konev54@yandex.ru', password_hash='fb8c0339e494131cf0c27fcf7d4095da765b0d34b0531d341765b11608fd5030', id='30')]              |             |              | [Row(ip='117.195.70.39')]  | 08.06.2017  | ['{"bk_type": "1win"}']                                           |
```