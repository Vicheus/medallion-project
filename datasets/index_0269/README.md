# Parsetron results

## About row data

> - Code name: index_0269
> - File path: vezetvsem-user_profile.txt
> - Total rows: 1618733

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- user_id: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- title: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone_home: string (nullable = true)
 |-- phone_office: string (nullable = true)
 |-- phone_mobile: string (nullable = true)
 |-- phone_fax: string (nullable = true)
 |-- icq: string (nullable = true)
 |-- skype: string (nullable = true)
 |-- birthday: string (nullable = true)

```

### Data sample
```
|   id |   user_id | first_name   | last_name   | middle_name   | title      | email                        | phone_home   |   phone_office | phone_mobile   | phone_fax   | icq   | skype   | birthday   |
|-----:|----------:|:-------------|:------------|:--------------|:-----------|:-----------------------------|:-------------|---------------:|:---------------|:------------|:------|:--------|:-----------|
|  303 |       291 | Юля          | Иванова     | NULL          | NULL       | yulua_ivanova_1988@bk.ru     | NULL         |   +79281073796 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  304 |       292 | Юля          | Иванова     | NULL          | NULL       | yulya_ivanova_1988@bk.ru     | NULL         |   +79281073796 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  305 |       293 | Марина       | Орская      | NULL          | NULL       | tastyboom@yandex.ru          | NULL         |   +79281073796 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  306 |       294 | Владислав    | Шумченко    | NULL          | NULL       | gonzalis89@mail.ru           | NULL         |                | 99287635330    | NULL        | NULL  | NULL    | NULL       |
|  307 |       295 | Катя         | Семакова    | NULL          | NULL       | k-semakova@rambler.ru        | NULL         |   +79281073796 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  308 |       296 | Владислав    | Шумченко    | NULL          | NULL       | gonzalis98@mail.ru           | NULL         |              0 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  309 |       297 | Ольга        | Романова    | NULL          | NULL       | olga.romanova.65@mail.ru     | NULL         |   +79281733180 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  310 |       298 | Максим       | Дыркин      | NULL          | Дыркин     | mdyrkin@bk.ru                | NULL         |   +79281073796 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  311 |       299 | Сергей       | Колычев     | NULL          | Колычев    | kolichev.sergei@yandex.ru    | NULL         |                | +79081785000   | NULL        | NULL  | NULL    | NULL       |
|  312 |       300 | Олег         | Краснов     | NULL          | NULL       | oleg_krasnovv@rambler.ru     | NULL         |   +79281733180 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  313 |       301 | Владимир     | Крылов      | NULL          | NULL       | krylov-00@list.ru            | NULL         |   +79281733180 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  314 |       302 | Анатолий     | Степанов    | NULL          | NULL       | toly.stepanov1973@yandex.ru  | NULL         |   +79281733180 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  315 |       303 | Сергей       | Белоусов    | NULL          | Фортуна    | fortuna-fortuna@inbox.ru     | NULL         |   +79281733180 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  316 |       304 | Игорь        | Давыдов     | NULL          |            | i-davydov@bk.ru              | NULL         |   +79281073796 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  318 |       306 | Феликс       | Пеликс      | NULL          |            | felix.khachatrian@gmail.com  | NULL         |                | 71234123133    | NULL        | NULL  | NULL    | NULL       |
|  319 |       307 | Эдуард       | Сом         | NULL          | Сом        | som.edik@yandex.ru           | NULL         |   +79281073796 | NULL           | NULL        | NULL  | NULL    | NULL       |
|  321 |       309 | Сергей       | Серый       | NULL          | Серый С.Л. | l565470@yandex.ru            | NULL         |                | 89612887420    | NULL        | NULL  | NULL    | NULL       |
|  322 |       310 | ООООООоо     | Фффффф      | NULL          | 123        | vahagn.grigoryan@gmail.com   | NULL         |                | +77878778987   | NULL        | NULL  | NULL    | NULL       |
|  323 |       311 | ООООООоо     | Фффффф      | NULL          | NULL       | vahagn.grigoryan1@gmail.com  | NULL         |                | +74569874565   | NULL        | NULL  | NULL    | NULL       |
|  324 |       312 | Ваагн        | Григорян    | NULL          | NULL       | vahagn.grigoryan11@gmail.com | NULL         |                | +77899878998   | NULL        | NULL  | NULL    | NULL       |
```

> - Code name: index_0269
> - File path: vezetvsem-users.txt
> - Total rows: 1618691

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- username: string (nullable = true)
 |-- password: string (nullable = true)
 |-- email: string (nullable = true)
 |-- last_ip: string (nullable = true)
 |-- last_login: string (nullable = true)

```

### Data sample
```
|   id | username            | password                           | email                       | last_ip        | last_login          |
|-----:|:--------------------|:-----------------------------------|:----------------------------|:---------------|:--------------------|
|  291 | Юльчик              | $1$YHvSCLzS$VDwNEqdl1MUNQY95PZBq2. | yulua_ivanova_1988@bk.ru    | 213.138.87.4   | NULL                |
|  292 | Юльчикк             | $1$gWWy3/c8$9k9sIxeL38UpwBq/pOGLb0 | dawoyano@yandex.ru          | 89.108.86.162  | 2017-05-23 13:30:20 |
|  293 | Мариша              | $1$SHgcWNoI$xkcw14HVGB8s2jPtzsWTv1 | tastyboom@yandex.ru         | 213.138.87.4   | 2011-07-21 13:34:32 |
|  294 | Gonzalis            | $1$PrwfbBNN$HdcfjLZyt5H6rqF3Gb3jv1 | gonzalis89@mail.ru          | 93.81.179.86   | NULL                |
|  295 | Kate                | $1$XzLj6sqo$7rgkr17xa3Vp7ApEpeuTW. | k-semakova@rambler.ru       | 213.138.87.4   | 2011-07-05 15:49:15 |
|  296 | Gonzalis89          | $1$1twzXOlJ$/ahThS38cLk.tuPhhgr5G/ | gonzalis98@mail.ru          | 93.81.179.86   | 2011-07-05 14:08:09 |
|  297 | Оля                 | $1$.xV2YgKU$G7MKdMEftwwI39zsMkyG/. | olga.romanova.65@mail.ru    | 176.9.36.241   | 2012-02-29 10:18:50 |
|  298 | Maks                | $1$veryBigS$ZRW9szO0N.qn0tuGF4nyW. | mdyrkin@bk.ru               | 94.77.141.16   | 2015-07-30 00:07:23 |
|  299 | Серега              | $1$veryBigS$m0FJK44.S/iBtZgkYIV9f1 | kolichev.sergei@yandex.ru   | 193.169.25.11  | 2016-02-15 13:37:12 |
|  300 | Oleg                | $1$GmlDYmYr$9Po4ucyvbBe.drGjgJeK60 | oleg_krasnovv@rambler.ru    | 213.138.87.4   | 2011-08-08 08:36:54 |
|  301 | Вова                | $1$oj0s.9wt$hPn7i5LPSzDw.JbwYFa/71 | krylov-00@list.ru           | 213.138.77.62  | 2011-09-05 08:06:24 |
|  302 | Толян               | $1$Db8rWMvy$9.ctp69ORjvRxK1.ZKpR21 | toly.stepanov1973@yandex.ru | 213.138.83.20  | 2011-08-23 20:21:15 |
|  303 | Фортуна             | $1$veryBigS$h0bcu2RCeINbgHppFvRWV. | fortuna-fortuna@inbox.ru    | 176.9.36.241   | 2012-01-10 09:36:06 |
|  304 | Игорек              | $1$l7Nn2lE.$C7bgA9OTLI6Ham5603hzv0 | i-davydov@bk.ru             | 213.138.87.4   | 2011-08-10 14:58:37 |
|  306 | felisitto           | $1$ELIotLJ.$SVU8Er52uKdU.f91qLKNa. | felix.khachatrian@gmail.com | 212.144.20.222 | 2013-01-15 13:39:41 |
|  307 | Эдик                | $1$yOu6i0iG$GesNCF/F22wFV9mwAqjGK/ | som.edik@yandex.ru          | 213.138.87.4   | 2011-07-21 14:03:21 |
|  308 | kozlov@vezetvsem.ru | $1$veryBigS$pSaG5Ii5RqzNO/YjLm/f30 | kozlov@vezetvsem.ru         | 37.142.165.136 | 2022-06-03 18:33:07 |
|  309 | Караван             | $1$veryBigS$QyuxnjuQMdZIsXZIL0XLu. | l565470@yandex.ru           | 80.80.98.136   | 2018-01-30 10:19:19 |
|  310 | vgrigory10          | $1$9/2xxjxB$btybsK7.BrhQfbUDqKWd.1 | vahagn.grigoryan@gmail.com  | 31.23.36.222   | 2015-12-04 23:49:20 |
|  311 | vgrigory11          | $1$S0Le63lg$8P299GKiVB/3olcXpOzra/ | vahagn.grigoryan1@gmail.com | 195.250.88.232 | 2011-07-11 12:56:21 |
```


## About final data
> - Total rows: 1560569

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```



### Data sample
```
| names                        | emails                        | phones          | birth_date   | socials   | ips                                           | accounts                                                                                                                             |
|:-----------------------------|:------------------------------|:----------------|:-------------|:----------|:----------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| ['A Elena']                  | ['e20005@mail.ru']            | ['79632917614'] |              |           | [Row(ip='84.241.194.40', date='12.12.2020')]  | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='e20005', password_hash='$1$veryBigS$uUpHV/W4yHqK0.t3dQvUj1')]          |
| ['Abdulaev Sultan']          | ['abdulaev-1977@bk.ru']       | ['79898767481'] |              |           | [Row(ip='95.153.133.211', date='18.09.2020')] | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='Sultan77', password_hash='$1$veryBigS$Z2fUCjEJTBhlD6QgVMlWf/')]        |
| ['Actis Projects Llc Антон'] | ['info@actis.kz']             |                 |              |           | [Row(ip='178.89.84.243', date='03.03.2016')]  | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='info666', password_hash='$1$veryBigS$PX1GSn5rwhT0TU2DGQ1Lp.')]         |
| ['Adrian']                   | ['adrian_28@mail.ru']         | ['79373995244'] | 28.01.1981   |           | [Row(ip='85.140.1.225', date='15.08.2016')]   | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='adrian', password_hash='$1$veryBigS$X8D.X2oKoa6r1u0f71QCx0')]          |
| ['Aibek']                    | ['www.bazhikov@gmail.com']    |                 |              |           | [Row(ip='0.0.0.0', date=None)]                | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='www.bazhikov', password_hash='$1$veryBigS$4SIlbDlb7d2e50hEUwJ6i/')]    |
| ['Alecsandr']                | ['38914040@mail.ru']          | ['79269666073'] |              |           | [Row(ip='95.211.172.177', date=None)]         | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='user117516', password_hash='$1$veryBigS$mYfh5y2xNT9wlExE.vJUW/')]      |
| ['Aleksei']                  | ['norcobigfoot056@gmail.com'] |                 |              |           | [Row(ip='79.98.72.244', date='02.05.2021')]   | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='norcobigfoot056', password_hash='$1$veryBigS$BF4Cd0UZcL3Z1N0rFPhow0')] |
| ['Alesandro']                | ['alesandro13@ukr.net']       |                 |              |           | [Row(ip='46.211.98.228', date='27.09.2017')]  | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='alesandro13', password_hash='$1$veryBigS$5cpNNIX2rKyoTUbPtLeA70')]     |
| ['Alex']                     | ['aitd77@yandex.ru']          | ['79081096926'] |              |           | [Row(ip='176.59.206.69', date='25.01.2019')]  | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='aitd77', password_hash='$1$veryBigS$3Zw7r2m28U0bZB3vKaCsH1')]          |
| ['Alex']                     | ['van525@yandex.ru']          | ['79093795051'] |              |           | [Row(ip='0.0.0.0', date=None)]                | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='van525', password_hash='$1$veryBigS$4uO6hur.Iiuc4YmyUUMPl1')]          |
| ['Alex']                     | ['vanor1@mail.ru']            | ['79189016578'] |              |           | [Row(ip='89.16.104.48', date='05.10.2017')]   | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='vanor1', password_hash='$1$veryBigS$YwFz3WUNCMrxu42dznqYl1')]          |
| ['Alex']                     | ['lc27@ya.ru']                | ['79897250100'] |              |           | [Row(ip='0.0.0.0', date=None)]                | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='lc27', password_hash='$1$veryBigS$LDA3SFNwzTLTB7B1jGST0/')]            |
| ['Alexander']                | ['kasatka4444@mail.ru']       |                 |              |           | [Row(ip='188.191.0.4', date='17.10.2021')]    | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='kasatka4444', password_hash='$1$veryBigS$hMAySOAgmKa0Pa5hi1WPw/')]     |
| ['Alexander']                | ['n2mb4rxi1i@gmail.com']      | ['79999813164'] |              |           | [Row(ip='176.107.246.12', date='29.03.2021')] | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='n2mb4rxi1i', password_hash='$1$veryBigS$ZqYO8PCoVcoGl4RnFvBXL.')]      |
| ['Alexandr']                 | ['alexandr.chereh@gmail.com'] |                 |              |           | [Row(ip='68.34.151.77', date='09.05.2016')]   | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='alexandr.chereh', password_hash='$1$veryBigS$yaGsUohfgqohpd403Jage.')] |
| ['Alexandr']                 | ['ply.alexandr@yandex.ru']    | ['79192534577'] |              |           | [Row(ip='95.179.116.49', date='09.01.2017')]  | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='ply.alexandr', password_hash='$1$veryBigS$pmt1wUIFtZOVAnU7yPUug.')]    |
| ['Alexey']                   | ['hoom@inbox.ru']             | ['79037240412'] |              |           | [Row(ip='0.0.0.0', date=None)]                | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='hoom', password_hash='$1$veryBigS$dbQ0OMTNrZuMAotCZ0iAX/')]            |
| ['Alexey']                   | ['m9262104617@gmail.com']     | ['79789209433'] |              |           | [Row(ip='176.195.35.13', date='26.05.2016')]  | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='m9262104617', password_hash='$1$veryBigS$PWgGT4HaFSuJHcJKiFd0j1')]     |
| ['Alexsandra']               | ['sandrita507@gmail.com']     |                 |              |           | [Row(ip='0.0.0.0', date=None)]                | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='sandrita507', password_hash='$1$veryBigS$8KmFQFEFSz1fxpeNqkluw1')]     |
| ['Alim']                     | ['au@gdematerial.ru']         | ['79264802756'] |              |           | [Row(ip='193.81.100.92', date='04.03.2016')]  | [Row(title='Везёт Всем', link='https://vezetvsem.ru/', login='au', password_hash='$1$veryBigS$pwRbeP0OEUv/j6DDf4CGh.')]              |
```