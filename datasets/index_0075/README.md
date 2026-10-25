# Parsetron results

## About row data

> - Code name: index_0075
> - File path: tvoe-users.csv
> - Total rows: 2268634

### Schema
```
root
 |-- ID: string (nullable = true)
 |-- TIMESTAMP_X: string (nullable = true)
 |-- LOGIN: string (nullable = true)
 |-- PASSWORD: string (nullable = true)
 |-- ACTIVE: string (nullable = true)
 |-- NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- LAST_LOGIN: string (nullable = true)
 |-- PERSONAL_PHONE: string (nullable = true)

```

### Data sample
```
|   ID | TIMESTAMP_X         | LOGIN                           | PASSWORD                                                                                                   | ACTIVE   | NAME         | LAST_NAME     | EMAIL                           | LAST_LOGIN          | PERSONAL_PHONE     |
|-----:|:--------------------|:--------------------------------|:-----------------------------------------------------------------------------------------------------------|:---------|:-------------|:--------------|:--------------------------------|:--------------------|:-------------------|
|    1 | 2022-08-30 16:39:14 | fake                            | $6$4Q19PXsWMrYGIXaa$qQBCdB4onnjvWpwwqOdsk1ljlHnbcFCkU516shRBPj1e25ZBbE8YcfYjgwP5.kJ5vjYX74Ar/oHQoEsYM..4Q. | Y        | fake         | fake          | def@legacy.ru                   | 2023-05-05 10:47:48 | 79099090900        |
|    2 | 2022-09-06 14:58:10 | anonymous_Accg0qhjo@example.com | cs0xPdpB082abb6f16fa51eac409bfe65b87b680                                                                   | Y        | пользователь | Анонимный     | anonymous_Accg0qhjo@example.com | NULL                |                    |
|    3 | 2022-10-12 12:35:15 | admin@tvoe.ru                   | $6$lkEB1HLzHjPHIN94$lrPDlwY.CsxgejAgTWY/JO7j9E6g2HshHP//EEi8zHFVqBG9jD5IzkpTgECQVttVuKgLVb42CeF.JK3XCAobD0 | Y        | Дмитрий      | Серяков       | admin@tvoe.ru                   | 2021-03-29 16:08:40 | +7 (906) 731-37-76 |
|    4 | 2023-01-10 12:42:48 | dmitri.seryakov@yandex.ru       | pL{7)oY916034d17ccc7210a68cbc4d9471003e6                                                                   | Y        |              | 123           | dmitri.seryakov@yandex.ru       | 2023-03-14 16:13:28 | +79067313776       |
|    6 | 2023-05-17 15:04:56 | k.shokhirev@cloudpayments.ru    | $6$Is1rTpS6sYAx7vU4$81KEKDPYs.sNZLnE9NUGShVJ4pz..TSs/xhFeUgJYQhbWOZhKYu5uckTtKqMCC12MNIPlrtw2NtHJKJYVXAJW/ | Y        |              | Тест          | k.shokhirev@cloudpayments.ru    | 2022-06-24 13:58:04 | 79999999999        |
|    7 | 2022-07-21 16:54:04 | shoxirev@mail.ru                | JRZShGG2a0f27847d21ef309f3766ce1d1d0def2                                                                   | Y        | тест         | Кирилл        | shoxirev@mail.ru                | 2022-06-05 12:59:24 | +7 (922) 562-90-90 |
|    8 | 2022-08-30 16:39:27 | valyenti@yandex.ru              | 8XZGWBy428bf5ac9be043b44863eecfd637d14f6                                                                   | Y        | Валентина    | Родионова     | valyenti@yandex.ru              | 2020-10-05 15:19:22 | 79151084759        |
|    9 | 2022-08-25 14:15:53 | a.chernyshev@tvoe.ru            | $6$r6i3VF4258hN4VWh$h8DZPgta3td9f3pJyV1ncA1xOCoohV71mQz4l4yvZSBuAUvvFtUwl4Xga2r/UaUsruInx6Qi2n5DMUkei.ol2. | Y        | Артем        | Чернышев      | a.chernyshev@tvoe.ru            | 2022-03-14 10:53:04 | +7 (926) 967-47-04 |
|   10 | 2022-08-30 16:39:52 | e.tretyakov@cloudpayments.ru    | 3l3d3TnB3ea353fc9dd111a1b45f6110b6318980                                                                   | Y        | NULL         | test          | e.tretyakov@cloudpayments.ru    | NULL                | 79251212121        |
|   11 | 2022-08-30 16:39:56 | e.tretyakov@cloudpayments.ru    | Qwqmil4w0de4f72fe5f4d0c46f9d99a6cc051b51                                                                   | Y        | test         | Cloudpayments | e.tretyakov@cloudpayments.ru    | 2020-10-06 10:24:32 | 79263846504        |
|   12 | 2022-08-30 16:39:30 | ne--pravda@yandex.ru            | hGxjoI5r666de3f73126a635f2eeefe6ef9e1eec                                                                   | Y        | Ирина        | Серякова      | ne--pravda@yandex.ru            | 2020-10-11 18:14:25 | 79161818251        |
|   13 | 2022-08-30 16:38:51 | 123mnbn@gmail.com               | OfFwg7vNc224cb4be28551d4f0f53f4fbb438f3d                                                                   | Y        |              | оллр          | 123mnbn@gmail.com               | 2020-10-09 12:20:19 | 78787887788        |
|   14 | 2022-08-30 16:40:24 | test@test.ru                    | qk442mjc7f00f1e0ea68142c795bd4aa3e93f41e                                                                   | Y        |              | Тестов        | test@test.ru                    | 2020-10-09 16:40:21 | 79534410650        |
|   15 | 2022-08-30 16:41:10 | shopmanager@tvoe.ru             | olfokLjW0e53228eaae661d7e11596ebc03dcafd                                                                   | Y        |              |               | shopmanager@tvoe.ru             | 2020-12-15 10:08:45 | 79999999997        |
|   17 | 2022-08-30 16:39:58 | vladimir.savritsky@gmail.com    | $6$nRckZtG2nDscDUan$/jgGtx9YT.ajV6Dhw46dT1olHC3X3OR4WMFUtHEGnGAE7hInD10jwo359QGGf318hSrRnMfJWn2G8/LIELRB/. | Y        |              | Владимир      | vladimir.savritsky@gmail.com    | 2020-12-21 12:10:17 | 79266881333        |
|   19 | 2022-08-30 16:39:59 | sdf@sdfsdf.ru                   | $6$0XoX96yG2UIYmgRm$n0VNvZK8giwI3Akz.ZBebQWvDQS7kWynHXsUUlIejt95S3JkdpnmYJc5ygw2HpHkp4m31NeKFflbQ4SwlH1MP. | Y        |              | Тест          | sdf@sdfsdf.ru                   | 2021-01-22 12:17:48 | 79268882342        |
|   20 | 2022-09-05 15:52:00 | u.fomin@tvoe.ru                 | $6$xYC4NIRGFHhZHsPP$ZVZisAT0lidFRK1GTzxj8yOmOky.J81a96OS/lYUVD0wPYdLBp02kqP8OSsYioamz7spdK4tEX9cI.VKyW8q./ | Y        |              |               | u.fomin@tvoe.ru                 | 2021-06-30 19:43:07 | +7 (999) 999-99-99 |
|   23 | 2022-08-25 14:14:47 | d.samoilov@tvoe.ru              | $6$EW2d9yLDPqXa0gFg$OB.2LXyI7MvJ3md2UOXMYaKQdxle/3.lhlsFGfI6Ib1308rJ2jM9aBktSpXcKAwc3xFilexiDxZbg40OzCcti1 | Y        | Дмитрий      | Самойлов      | d.samoilov@tvoe.ru              | 2021-12-16 08:53:40 | +7 (925) 754-94-84 |
|   24 | 2022-08-30 16:41:10 | telbukhov@air.agency            | $6$twQs9sC3Ojtmx5V9$eSSfKNdQn5r0UGkWQWKOZfPNMgDwzPiAkpCs4jMEmDX70scwMaYxtDAoDNpXtgX190HUtlRC.SjxjHSDTKv1g/ | Y        |              |               | telbukhov@air.agency            | 2021-04-25 17:07:35 | 79999999998        |
|   25 | 2022-08-25 14:15:44 | fominu@gmail.com                | $6$63gzXd7l7xHBDueQ$4gPKYfmnE0Krum5ZMLRjgubCyrPCNEIJ5sOXi6B3tlZttFEUJSltTUE5Mf0DI6Gvc/M4eA1qQ9CtnjiAyN4aH/ | Y        |              |               | fominu@gmail.com                | 2022-05-26 16:35:52 | +7 (965) 305-04-04 |
```


## About final data
> - Total rows: 2174782

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
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
| Emails | 99.76% |
| Phones | 99.66% |
| Accounts | 100.00% |
| Actuality | 87.24% |



### Data sample
```
| names                    | emails                           | phones          | accounts                                                                                                                                                                                                                                | actuality   |
|:-------------------------|:---------------------------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Fake Fake']            | ['def@legacy.ru']                |                 | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='fake', password_hash='$6$4Q19PXsWMrYGIXaa$qQBCdB4onnjvWpwwqOdsk1ljlHnbcFCkU516shRBPj1e25ZBbE8YcfYjgwP5.kJ5vjYX74Ar/oHQoEsYM..4Q.')]                         | 05.05.2023  |
| ['Серяков Дмитрий']      | ['admin@tvoe.ru']                | ['79067313776'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='admin@tvoe.ru', password_hash='$6$lkEB1HLzHjPHIN94$lrPDlwY.CsxgejAgTWY/JO7j9E6g2HshHP//EEi8zHFVqBG9jD5IzkpTgECQVttVuKgLVb42CeF.JK3XCAobD0')]                | 29.03.2021  |
| ['Родионова Валентина']  | ['valyenti@yandex.ru']           | ['79151084759'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='valyenti@yandex.ru', password_hash='8XZGWBy428bf5ac9be043b44863eecfd637d14f6')]                                                                             | 05.10.2020  |
| ['Чернышев Артем']       | ['a.chernyshev@tvoe.ru']         | ['79269674704'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='a.chernyshev@tvoe.ru', password_hash='$6$r6i3VF4258hN4VWh$h8DZPgta3td9f3pJyV1ncA1xOCoohV71mQz4l4yvZSBuAUvvFtUwl4Xga2r/UaUsruInx6Qi2n5DMUkei.ol2.')]         | 14.03.2022  |
| ['Серякова Ирина']       | ['ne--pravda@yandex.ru']         | ['79161818251'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='ne--pravda@yandex.ru', password_hash='hGxjoI5r666de3f73126a635f2eeefe6ef9e1eec')]                                                                           | 11.10.2020  |
| ['Оллр']                 | ['123mnbn@gmail.com']            |                 | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='123mnbn@gmail.com', password_hash='OfFwg7vNc224cb4be28551d4f0f53f4fbb438f3d')]                                                                              | 09.10.2020  |
| ['Владимир']             | ['vladimir.savritsky@gmail.com'] | ['79266881333'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='vladimir.savritsky@gmail.com', password_hash='$6$nRckZtG2nDscDUan$/jgGtx9YT.ajV6Dhw46dT1olHC3X3OR4WMFUtHEGnGAE7hInD10jwo359QGGf318hSrRnMfJWn2G8/LIELRB/.')] | 21.12.2020  |
| ['Самойлов Дмитрий']     | ['d.samoilov@tvoe.ru']           | ['79257549484'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='d.samoilov@tvoe.ru', password_hash='$6$EW2d9yLDPqXa0gFg$OB.2LXyI7MvJ3md2UOXMYaKQdxle/3.lhlsFGfI6Ib1308rJ2jM9aBktSpXcKAwc3xFilexiDxZbg40OzCcti1')]           | 16.12.2021  |
| ['Наталья']              | ['nata.varzina2010@yandex.ru']   | ['79250876966'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='nata.varzina2010@yandex.ru', password_hash='$6$w8613cfe27RM379q$z8z8PNMnrdg9IrYPeUOXn2PdQA9jupUOMnIY4bUtb83R.V2qg9.WlKHivpIcPnS4HDVMfJ7I84oe1omZkpTQn/')]   |             |
| ['Джайчибеков Дархан']   | ['art-brand.kz@mail.ru']         |                 | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='art-brand.kz@mail.ru', password_hash='$6$YBdJ0XxZgh8gQ1Tf$EHDf6ozIbv3bRXU3HAvaQs8lIbxknB8wGaIgKBB1.a8HLlYXRwBVGlbEBe4xj8pRQX8MKAHPZKmEcvR0uWZ3J1')]         |             |
| ['Тараканова Людмила']   | ['19891020m@gmail.com']          | ['79130236995'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='19891020m@gmail.com', password_hash='$6$AsMbWI4w26ZK6pp7$Cr1Ml8nMF7S6Ts/6ypZLG2ZL/KtNzG4k8K5ytZ63BiV5rD12V8fuq7POGzBbOXfSHytPzZsfAJzXfCB/8U1zK/')]          |             |
| ['Целовальникова Дарья'] | ['dl_c@mail.ru']                 | ['79871887348'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='dl_c@mail.ru', password_hash='$6$cu15CUTzAqQCbaul$fsxSClvP7fO0SXHRLJckZ5GFGUIRNEkvKAJv/GuHuBDWWB.Hii3j1Fni8UxnU/dzKCn0okMt7R4RtylucRuyr/')]                 |             |
| ['Сафонова Эльмира']     | ['bagira310387@yandex.ru']       | ['79503133168'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='bagira310387@yandex.ru', password_hash='$6$fgZn5x10JLh92ZCR$TL8/AwliL5ubj43FRgTvFvOQtaur/GsFAGrdYTEvhUetB/o8XvdX8PhgJn//GJ8wNBlQYP/fYbStIVgaHBku30')]       |             |
| ['Панфилов Вячеслав']    | ['0909zero0909@gmail.com']       | ['79032363712'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='0909zero0909@gmail.com', password_hash='$6$KDPpj4MiRY8tyxmu$hhCS77P5Jz8twee2xF5FzH0Hf3mLYdxZXHIQ5lroaRJ7GruI3CUJv4PK.QXDUewa.DJ/yLHhSv7TGB9D4nfx80')]       |             |
| ['Ельчанинова Варвара']  | ['elchaninova99@bk.ru']          | ['79276522474'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='elchaninova99@bk.ru', password_hash='$6$b6uQFviJgCuBGvbi$ftPIqbb/JDgLcvroaH1Tq7h8d4DXcm6vjRI.HQiPEK0p0.tZcDSofU4xSHEA8nhiy/4M9sHxYZ1K9Oz3xpSg3.')]          |             |
| ['Крыгир Лилия']         | ['lilia.krygir@mail.ru']         | ['79166054621'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='lilia.krygir@mail.ru', password_hash='$6$ZJkrjlpkpeoH3PiR$ylC.hyECEWnQV3r/Q7moMCjnopAPVDnUA9CuzOiiIVNCuBUvOSDczYTIfbsqXwGdEcrbXU45ebeYGD9djPRYI0')]         | 21.05.2021  |
| ['Полина Парфёнова']     | ['polina.parfenova.06@inbox.ru'] | ['79527724091'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='polina.parfenova.06', password_hash='$6$LKZp1ZZqtmNK4hrD$1EZJNa2E2TlsI.ZeJT2PVhZQ6l1riHQkJzdHN4U6xl5o2NcFjIgMOPbGyldGOqpmKrHtWVJghLgJ9YkwUddSw/')]          | 15.05.2023  |
| ['Калугин Артём']        | ['kaluginartem546@gmail.com']    | ['79643450898'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='kaluginartem546@gmail.com', password_hash='$6$EhYh46NfD5MMHCcl$bVPP4sI.WyalZGCYiGZWBqkDYNHQCBIpVZ.GdjBp8gXUS1YIi4FoCQZ9CAfALUromfsh0RsY9A3eg3Kh30EEH/')]    | 17.09.2022  |
| ['Бикитеева Ксения']     | ['ksyups19@gmail.com']           | ['79510609146'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='ksyups19@gmail.com', password_hash='$6$Hg09Z2IANW6AXTii$TilVRq6pDYr2VojfbPKqTmQkXTj34mE15eWwZbxOPfYUg2bJuX21eykq5vorFLDgQsi3.yyxw2/77wY2kk9BS0')]           |             |
| ['Гонозова Дарья']       | ['daragonozova@gmail.com']       | ['79586657187'] | [Row(title='ТВОЕ - интернет-магазин одежды', link='https://tvoe.ru', login='Daragonozova@gmail.com', password_hash='$6$V9LGgGbO6lH0McUO$qFQDjPT5NHHfBHWSWPKOM/E/5yipXh8rmPfFUmtGB9QYjeteICHe85VAfMLsZVlAa7lzpTNnrusSN2xkJ8xfN.')]       |             |
```