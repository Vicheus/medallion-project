# Parsetron results

## About row data

> - Code name: index_0221
> - File path: /media/user/SAMSUNG/Databases/index_0221/raw/users_preprocessed.csv
> - Total rows: 681992

### Schema
```
root
 |-- username: string (nullable = true)
 |-- password: string (nullable = true)
 |-- email: string (nullable = true)
 |-- birthday: string (nullable = true)
 |-- ipaddress: string (nullable = true)
 |-- fbuserid: string (nullable = true)

```

### Data sample
```
| username      | password                         | email                      | birthday   | ipaddress    | fbuserid   |
|:--------------|:---------------------------------|:---------------------------|:-----------|:-------------|:-----------|
| iDS           | 83260d2ecbf022723ac72a4288ad969d | as@programist.ru           | 01-19-1977 |              |            |
| ToT           | 3c3224c7645d16fdcc3ef9a23f389ac1 | tot@klerk.ru               | 08-27-1972 |              | totttt     |
| qUeksBrefeges | 389820501d6622a37319a62062866bbd | hernefattag@gmail.com      |            | 46.105.72.28 |            |
| Lena          | 431d8b9d921d8a6c600ec836b3571fee | and@v-lazer.com            |            |              |            |
| irena         | 7f84615262c7fa86efe35ef9ef5c2efd | irena@rbkmail.ru           |            |              |            |
| SALDO.ru      | 2b323ceb709b74004e0e3e5ca344a1ee | saldo@saldo.ru             |            |              |            |
| Blondy        | 5be40e200b6b397cf74da7b551549ed2 | lena@kontrast.krasnodar.ru |            |              |            |
| remanika      | 7982d61d0c880b7954440838b85bb0f1 | remanika@rambler.ru        |            |              |            |
| lilit         | d23076aacfe53d555671b4970d44239b | zzanziver@mail.ru          |            |              |            |
| SnakE         | 9a5ff053a3ec4f59b8dc3ea70209502f | 1@1.1                      |            |              |            |
| Jenny         | 155aa699e5e06fc5002cfd0b63d7cfc8 | agorob@krasnodar.ru        |            |              |            |
| bogem         | 879009c803452b2a1119d031c6ee1f09 | bogomolov@raj.nornik       |            |              |            |
| qmax          | 34dd1abdc3f5e698dab084efadcb1e50 | Frolov@SvinSurance.ru      |            |              |            |
| Nica          | d1c57777dd52d43563e0300c08fa8d4b | pnica@mail.ru              |            |              |            |
| Lora          | 0b9ff2bd594cebc92419470304c078d3 | lora@headq.soyuz.ru        |            |              |            |
| Level         | 1b69410b56fe7625d9758e5500bff74f | snova_nam@pisem.net        |            |              |            |
| igankr        | d123b7f56c30f42d97443abce4f20fa6 | igankr@hotbox.ru           |            |              |            |
| DenG          | 1d3ca4ff122c6e75e257f65d8884abad | potanino-bk@yandex.ru      |            |              |            |
| 555555        | 686f944042cb261f10b2ed9ad9f74b24 | irnetta@rambler.ru         |            |              |            |
| kosta         | 271301c12571c67d101a92cbcd4a4fe5 | KOSTA@otkrytka.ru          |            |              |            |
```


## About final data
> - Total rows: 558013

### Schema
```
root
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```

### Data sample
```
| emails                                 | names                | ips                         | accounts                                                                                                                                           | socials   |
|:---------------------------------------|:---------------------|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| ['0000q02@scsmalls.com']               | ['Cribiadrahdak']    | [Row(ip='111.73.45.56')]    | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='0000q02@scsmalls.com', password_hash='4e563995e37df89a6254515db33be9a4')]               |           |
| ['00100-08@mail.ru']                   | ['Rus']              | [Row(ip='95.25.23.15')]     | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='00100-08@mail.ru', password_hash='5b66d2051010cdc48201bdd388991e25')]                   |           |
| ['002809@mail.ru']                     | ['Dtb']              | [Row(ip='84.51.96.237')]    | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='002809@mail.ru', password_hash='a59a2cbde2258e3e8e9724d09095b1b9')]                     |           |
| ['00phonecop8lwg86@gmail.com']         | ['Leadeliemboca']    | [Row(ip='91.210.106.111')]  | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='00phonecop8lwg86@gmail.com', password_hash='708192c3e95f8b29361f1b075c807f5d')]         |           |
| ['010apararehacker@gmail.com']         | ['Lelilefly']        | [Row(ip='216.152.245.251')] | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='010apararehacker@gmail.com', password_hash='58e2d089be8d503c8966e6bf6351acb7')]         |           |
| ['0123ugg006@anxmalls.com']            | ['Astethystelia']    | [Row(ip='110.86.189.70')]   | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='0123ugg006@anxmalls.com', password_hash='3de12756f3313c83bf0cf8e4c4ce8f5d')]            |           |
| ['0213cl006@cometoclmall.com']         | ['Agingotazop']      | [Row(ip='112.111.164.163')] | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='0213cl006@cometoclmall.com', password_hash='cd546c79aa3b9f47840b31f8b277b4d6')]         |           |
| ['0227chanel002@cometoclmall.com']     | ['Plaptolkinork']    | [Row(ip='110.82.174.209')]  | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='0227chanel002@cometoclmall.com', password_hash='c28fd9517d2a94cf20ccadffe82fcdf4')]     |           |
| ['0299365@mail.ru']                    | ['Mesa Verde']       | [Row(ip='62.152.80.177')]   | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='0299365@mail.ru', password_hash='c693421b1c6829f79c28f09d636a3a48')]                    |           |
| ['02zima12@mail.ru']                   | ['Nohkan']           | [Row(ip='80.240.60.27')]    | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='02zima12@mail.ru', password_hash='ea678909913945024af4a109daa6cecf')]                   |           |
| ['030464@ngs.ru']                      | ['Dorika']           | [Row(ip='87.241.239.227')]  | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='030464@ngs.ru', password_hash='69481356104946dc7fec497cf47b9254')]                      |           |
| ['0304mel@mail.ru']                    | ['Elenka Serebniti'] | [Row(ip='88.206.17.150')]   | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='0304mel@mail.ru', password_hash='016499f0f46aa7ea4aca40649a291cf8')]                    |           |
| ['0307pradaweb03@cometoclmall.com']    | ['Ulcerecippelm']    | [Row(ip='110.86.189.68')]   | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='0307pradaweb03@cometoclmall.com', password_hash='d0bc949d3a445ca97c1db70b68f747ea')]    |           |
| ['03081968@mail.ru']                   | ['Cemen']            | [Row(ip='89.109.179.13')]   | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='03081968@mail.ru', password_hash='40cd728f2cb5fe9c205a978244d61bb9')]                   |           |
| ['03myfloridalist8@gmail.com']         | ['Gollotnow']        | [Row(ip='91.210.106.111')]  | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='03myfloridalist8@gmail.com', password_hash='278aef85624819a5177ff97df169d7bb')]         |           |
| ['0625mk22@louisvuittonworldtour.com'] | ['Essegiast']        | [Row(ip='63.141.249.37')]   | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='0625mk22@louisvuittonworldtour.com', password_hash='249b822b7316ce7d6ccc3a7e01b6e84a')] |           |
| ['0625mk26@louisvuittonworldtour.com'] | ['Expintyinsisp']    | [Row(ip='198.2.218.145')]   | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='0625mk26@louisvuittonworldtour.com', password_hash='38ffa6e465d1a8ef0ed33d96ce94c1f9')] |           |
| ['0625mk77@pradahotonsale.com']        | ['Alconfons']        | [Row(ip='54.227.21.157')]   | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='0625mk77@pradahotonsale.com', password_hash='5c8b9cc98b80345822ce620bee546782')]        |           |
| ['07ladyart@mail.ru']                  | ['Ladyart']          | [Row(ip='89.189.191.30')]   | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='07ladyart@mail.ru', password_hash='c5c42c77a25c6fe92643332fec3942f3')]                  |           |
| ['07smartroutetour@gmail.com']         | ['Indequide']        | [Row(ip='91.210.106.111')]  | [Row(title='Клерк.ру', link='https://www.klerk.ru', login='07smartroutetour@gmail.com', password_hash='36666fe89332f28a207e39c26362f4d4')]         |           |
```