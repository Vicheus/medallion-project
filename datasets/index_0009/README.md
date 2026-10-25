# Parsetron results

## About row data

> - Code name: index_0009
> - File path: cdek.market.csv
> - Total rows: 100000

### Schema
```
root
 |-- user_id: integer (nullable = true)
 |-- status: string (nullable = true)
 |-- user_type: string (nullable = true)
 |-- user_login: string (nullable = true)
 |-- referer: string (nullable = true)
 |-- is_root: string (nullable = true)
 |-- company_id: integer (nullable = true)
 |-- last_login: integer (nullable = true)
 |-- timestamp: integer (nullable = true)
 |-- password: string (nullable = true)
 |-- salt: string (nullable = true)
 |-- firstname: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- company: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- fax: string (nullable = true)
 |-- url: string (nullable = true)
 |-- tax_exempt: string (nullable = true)
 |-- lang_code: string (nullable = true)
 |-- birthday: string (nullable = true)
 |-- purchase_timestamp_from: string (nullable = true)
 |-- purchase_timestamp_to: integer (nullable = true)
 |-- responsible_email: integer (nullable = true)
 |-- last_passwords: string (nullable = true)
 |-- password_change_timestamp: integer (nullable = true)
 |-- api_key: string (nullable = true)
 |-- telegram_token: string (nullable = true)
 |-- notify_time: string (nullable = true)
 |-- is_phone_confirmed: string (nullable = true)
 |-- cdek_onesignal_subscr: string (nullable = true)

```

### Data sample
```
|   user_id | status   | user_type   | user_login           | referer   | is_root   |   company_id |   last_login |   timestamp | password                         | salt          | firstname     | lastname   | company      | email                |       phone | fax   | url   | tax_exempt   | lang_code   |   birthday |   purchase_timestamp_from |   purchase_timestamp_to |   responsible_email | last_passwords                   |   password_change_timestamp | api_key   | telegram_token   | notify_time   | is_phone_confirmed   | cdek_onesignal_subscr   |
|----------:|:---------|:------------|:---------------------|:----------|:----------|-------------:|-------------:|------------:|:---------------------------------|:--------------|:--------------|:-----------|:-------------|:---------------------|------------:|:------|:------|:-------------|:------------|-----------:|--------------------------:|------------------------:|--------------------:|:---------------------------------|----------------------------:|:----------|:-----------------|:--------------|:---------------------|:------------------------|
|         1 | A        | A           | admin                |           | N         |            0 |   1660590901 |  1535381001 | d09e171ed0f29869272de89e36ac99d0 | 0H|TVFT6K2    | Bot           | market     | Simtech      | bot@cdek.market      | 71231231321 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan | 93fde8d969074f909f437c82d57605fa |                  1648122349 |           |                  |               | N                    | N                       |
|         3 | A        | C           | customer             |           | N         |            0 |   1643088107 |  1535381001 | 91ec1f9324753048c0096d036a694f86 |               | Customer      | Customer   |              | customer@example.com | 77777777777 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           0 |           |                  |               | N                    | N                       |
|         5 | A        | V           | vendor               |           | Y         |            1 |            0 |  1535381001 | 7c3613dba5171cb6027c67835dd3b9d4 |               | Vendor        | Vendor     | ACME Corp    | vendor@example.com   | 55555555555 | test  | test  | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
|        10 | A        | V           | vendor2              |           | N         |            1 |            0 |  1535381001 | d3e5836ab51f732e7388bdd0b18576b8 | lq:@KSi=:c    | Администратор | Simtech    | Simtech      | g_bill@example.com   | 55555555555 | test  | test  | N            | ru          |          0 |                         0 |                       0 |                 nan | 7c3613dba5171cb6027c67835dd3b9d4 |                  1535702381 |           |                  |               | N                    | N                       |
|        11 | A        | V           | cd@example.com       |           | Y         |            3 |            0 |  1535381001 | b79305a31209c58c5f2a842393cbfd73 | 3B-*zNCIJ>    | Администратор | Мой диск   | Мой диск     | cd@example.com       |             |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           0 |           |                  |               | N                    | N                       |
|        12 | A        | V           | megaton@example.com  |           | Y         |            4 |            0 |  1535381001 | f43b2f0988677b895dca70098cd80873 | Ss%*=:!YW^    | Администратор | Мегатон    | Мегатон      | megaton@example.com  |             |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           0 |           |                  |               | N                    | N                       |
|        13 | A        | V           | dmoknigi@example.com |           | Y         |            5 |            0 |  1535381001 | 35465df83fde38a634637b0733ed8116 | {B$f(0k{7#    | Администратор | Дом книги  | Дом книги    | dmoknigi@example.com |             |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan | d524f547e27662fbc6d4423fd6a3d960 |                  1537187090 |           |                  |               | N                    | N                       |
|        14 | A        | V           | vdd@example.com      |           | Y         |            6 |            0 |  1535381001 | 1142100879646c9ec40bc9575a0d715a | ;POBsznw`m    |               |            | Всё для дома | vdd@example.com      |             |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan | c042c0d933eb3cb02820838d847dabc5 |                  1537271705 |           |                  |               | N                    | N                       |
|        15 | A        | V           | jet@example.com      |           | Y         |            7 |            0 |  1535381001 | 63d4dd01a6f6d260b5c1b56789fe4d14 | 8&!K?BW&+V    |               |            | Гаджет       | jet@example.com      |             |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan | 7a0bb0cc1550e1739c71b0636623ec17 |                  1537271736 |           |                  |               | N                    | N                       |
|        16 | A        | V           | sport@example.com    |           | Y         |            8 |            0 |  1535381001 | a481111e2dd555941465209d81298877 | 5U2){bbb#B    | Администратор | Мир спорта | Мир спорта   | sport@example.com    |             |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan | e9237ecaca450605330e687fec038beb |                  1537271391 |           |                  |               | N                    | N                       |
|        17 | A        | C           | user_13              |           | N         |            0 |            0 |  1535381001 | 6115563da275d7e3848bc66c4b5a7f36 | ZW^=jrrQf)    | Анна          | Петрова    |              | user1@example.com    | 79270132651 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
|        18 | A        | C           | user_14              |           | N         |            0 |            0 |  1535381001 | ac5e694f6a4505698c7c84c471486397 | *]p&?cZbPK    | Мария         | Иванова    |              | user2@example.com    | 79031523621 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
|        19 | A        | C           | user_15              |           | N         |            0 |            0 |  1535381001 | ae049d6a48fb3ae26aac0f2d126a5c18 | """'4p9\H{14" | Ольга         | Григорьева |              | user3@example.com    | 79085542361 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
|        20 | A        | C           | user_16              |           | N         |            0 |            0 |  1535381001 | addde66d6167e14359072052054b4a14 | b<T8xDnoR:    | Николай       | Ворошилов  |              | user4@example.com    | 79275232101 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
|        21 | A        | C           | user_17              |           | N         |            0 |            0 |  1535381001 | 34a9b5e063b6be00ca18437effdbef34 | Bs|L\(aMJ}    | Мария         | Родникова  |              | user5@example.com    | 79035452102 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
|        22 | A        | C           | user_18              |           | N         |            0 |            0 |  1535381001 | e883b192091d6bdd6b1bcdc302f52b98 | (?EKpaA(;i    | Елена         | Михайлова  |              | user6@example.com    | 79241251044 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
|        23 | A        | C           | user_19              |           | N         |            0 |            0 |  1535381001 | ecd1788b7c602f5b1dbc66923e911315 | 7%TRrgB\Bw    | Надежда       | Ефимова    |              | user7@example.com    | 79023221458 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
|        24 | A        | C           | user_24              |           | N         |            0 |            0 |  1535381001 | 2dd17996015086d65cfde508df0035ce | [!K+?D]z!n    | Алексей       | Маслов     |              | user9@example.com    | 79032125622 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
|        25 | A        | C           | user_25              |           | N         |            0 |            0 |  1535381001 | c3e50b167960978ee88c79a5761be876 | [n97wj-v8(    | Александр     | Афонин     |              | user10@example.com   |             |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
|        26 | A        | C           | user_26              |           | N         |            0 |            0 |  1535381001 | 58a69734d301e5e0faf18cbaa9651930 | 0[)<D|c0rZ    | Наташа        | Лисицина   |              | user8@example.com    | 79515441352 |       |       | N            | ru          |          0 |                         0 |                       0 |                 nan |                                  |                           1 |           |                  |               | N                    | N                       |
```


## About final data
> - Total rows: 43817

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |    |    |-- id: string (nullable = true)
 |-- actuality: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 87.58% |
| Emails | 98.90% |
| Birth_date | 0.00% |
| Accounts | 67.37% |
| Actuality | 96.93% |
| Raw_metadata | 0.88% |



### Data sample
```
| names                 | phones          | emails                          | birth_date   | accounts                                                                                                                                              | actuality   | raw_metadata   |
|:----------------------|:----------------|:--------------------------------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|:---------------|
| ['Пятанина Лариса']   | ['79161526484'] | ['hello@my-bijou.ru']           |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_69', password_hash='3bdc00ab1601cb42de538849c11f50db', id='69')]                   | 04.08.2020  |                |
| ['Китюшко Валерия']   | ['79780921118'] | ['info@elins-svarka.ru']        |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_107', password_hash='de824b9aa01f03c9c3e3832f592a9d6e', id='107')]                 | 25.12.2018  |                |
| ['Калинин Евгений']   | ['79263337555'] | ['bymobile.ru@gmail.com']       |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_220', password_hash='738975ea4aa63526dc933fed14134b6c', id='220')]                 | 08.04.2022  |                |
| ['Носиков Станислав'] |                 | ['stas_nosikov@mail.ru']        |              | [Row(title='CDEK market', link='https://cdek.market/', login='stas_nosikov@mail.ru', password_hash='209efda2dacd32612ab0a74801aebade', id='336')]     | 26.02.2019  |                |
| ['Гайнуллин Рафаэль'] | ['79301701040'] | ['elnino83@mail.ru']            |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_762', password_hash='a0ce9805e06b546c348c09afd871fc83', id='762')]                 | 04.04.2019  |                |
| ['Федин Вадим']       | ['79673250102'] | ['money_biz@mail.ru']           |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_954', password_hash='d09fb2d5edef571579849fd5cbb484be', id='954')]                 | 18.02.2019  |                |
| ['Рамильевич Руслан'] | ['79312050201'] | ['info@alfasvet.pro']           |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_1431', password_hash='11b043f34c53ea47295340a9a803b53a', id='1431')]               | 03.06.2019  |                |
| ['Erertert Tdutyb']   | ['79684122798'] | ['enerbol@mail.ru']             |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_3538', password_hash='76d2f35ee5a950e28880e240c57f0fbd', id='3538')]               | 28.07.2020  |                |
| ['Барсуков Антон']    | ['79651340029'] | ['aaronb83@mail.ru']            |              | [Row(title='CDEK market', link='https://cdek.market/', login='aaronb83@mail.ru', password_hash='38604abfe9c66e9abcf94bf8ce04a65c', id='4128')]        | 05.03.2019  |                |
| ['Панов Антон']       | ['79219660262'] | ['9660262@gmail.com']           |              | [Row(title='CDEK market', link='https://cdek.market/', login='9660262@gmail.com', password_hash='b53e8ff48a6bcccf4a00ece1980ca68c', id='4205')]       | 05.03.2019  |                |
| ['Юсупова Елизавета'] | ['79000286029'] | ['zerichelizaveta@mail.ru']     |              | [Row(title='CDEK market', link='https://cdek.market/', login='zerichelizaveta@mail.ru', password_hash='24b51fa5b03fd2755ff069b2afba4b0d', id='5678')] | 19.03.2019  |                |
| ['Блинов Игорь']      |                 | ['igor.blinov@buyon.ru']        |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_6863', password_hash='6cd8d91f70a81f333f2c187d6d9e3d3a', id='6863')]               | 20.05.2019  |                |
| ['Тортик Тобольский'] |                 | ['tobpower@ya.ru']              |              | [Row(title='CDEK market', link='https://cdek.market/', login='tobpower@ya.ru', password_hash='b759a29bb18a2adcf069f78b44423d6a', id='6985')]          | 08.04.2019  |                |
| ['Головкин Андрей']   | ['78126037700'] | ['andrey@dtlshop.ru']           |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_9583', password_hash='0b31cb8ed3eae15bc2296fd4aecf52d4', id='9583')]               | 23.05.2019  |                |
| ['Полина Беляева']    |                 | ['nat@yandex.ru']               |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_9945', password_hash='929431827c80b32ea5daa4adc0ddce88', id='9945')]               | 25.05.2019  |                |
| ['Воложанин Максим']  |                 | ['max333max1@rambler.ru']       |              | [Row(title='CDEK market', link='https://cdek.market/', login='max333max1@rambler.ru', password_hash='019ccbc74c1e0262510ed12d020767d9', id='10684')]  | 29.05.2019  |                |
| ['Донцов Никита']     | ['79817580198'] | ['spectropt@yandex.ru']         |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_10818', password_hash='d8d4648d15b34740448bb29e5d26c3a1', id='10818')]             | 01.10.2019  |                |
| ['Фетисова Светлана'] | ['79106456539'] | ['6408002@mail.ru']             |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_12914', password_hash='4d25fa0233f6d93643ca1bda7972b288', id='12914')]             | 25.06.2019  |                |
| ['Комарова Наталья']  | ['79811975360'] | ['spbkoma@mail.ru']             |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_12992', password_hash='e0f07070fe8c047378f519df80fe15d5', id='12992')]             | 23.10.2019  |                |
| ['Тонких Елена']      | ['79284437742'] | ['tonkikh.elena1987@gmail.com'] |              | [Row(title='CDEK market', link='https://cdek.market/', login='user_13950', password_hash='783ad959dde1f5e0af7c5ad52ab052cc', id='13950')]             | 11.07.2019  |                |
```