# Parsetron results

## About row data

> - File path: cdek.shopping.csv
> - Total rows: 19839

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- password: string (nullable = true)
 |-- avatar: string (nullable = true)
 |-- dob: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- remember_token: string (nullable = true)
 |-- created_at: timestamp (nullable = true)
 |-- updated_at: timestamp (nullable = true)
 |-- confirmed_at: string (nullable = true)
 |-- email_verify_token: string (nullable = true)
 |-- is_vendor: integer (nullable = true)
 |-- vendor_verified_at: string (nullable = true)
 |-- status: string (nullable = true)
 |-- has_agreements: integer (nullable = true)

```

### Data sample
```
|   id | name                            | email                       | password                                                     | avatar   | dob        | phone        | remember_token                                               | created_at          | updated_at          | confirmed_at        | email_verify_token   |   is_vendor | vendor_verified_at   | status    |   has_agreements |
|-----:|:--------------------------------|:----------------------------|:-------------------------------------------------------------|:---------|:-----------|:-------------|:-------------------------------------------------------------|:--------------------|:--------------------|:--------------------|:---------------------|------------:|:---------------------|:----------|-----------------:|
|   11 | Vika                            | pm@cdek.market.ru           | $2y$10$RhGhRPh7qwRYnPSy33764OpM3e5AAWpf4pOX51Vz7FIiUYVO1c0xW | \t       | \t         | \t           | \t                                                           | 2022-04-19 20:08:13 | 2022-04-19 20:08:13 | 2022-04-19 16:08:13 | \t                   |           0 | \t                   | activated |                0 |
|   13 | Фисенко Павел Юрьевич           | fyftyssenko@gmail.com       | $2y$10$/uvxOODV/q6lPEYKkXj34OK664PJCFX7zaJd3Oo6udtyTwV.kcRdq | \t       | 1988-09-14 | +79775317292 | Jh0NrYpkON4JCoMufecumnPXOS6JLPFhSe1ItBfp0TGuCJ0ZGLkH9Ggq5Kz0 | 2022-04-25 13:39:55 | 2022-08-11 17:28:25 | \t                  | \t                   |           0 | \t                   | activated |                0 |
|   14 | Дмитрий                         | pivovarov.dmitriy@gmail.com | $2y$10$1GPTcD2kzOdUjPNExUi3.u0LEeOpcXdnFBuTOgwFynDwyyGPjZpmi | \t       | \t         | +79122178096 | VoMlhQ4w2MckpXY9bVInNOtFgjPv2q4abIQ5yNb4CL7oIXqPkMnOFoeKmU4k | 2022-04-25 17:42:32 | 2022-04-25 17:42:32 | \t                  | \t                   |           0 | \t                   | activated |                0 |
|   15 | Микуцкая Виктория Александровна | pm@cdek.market              | $2y$10$sdgKQ7MKeh0XegUlVz4yD.bUCrCTquE.PKVwodqRhoGzxfaySan0m | \t       | 2000-02-08 | \t           | O5wmdmvpd2Yj2isTTKKmE43hbTWS9ysO3ixXnZnOUu6hd3icNX3aOqZr4n3r | 2022-04-26 00:17:43 | 2022-08-10 18:05:34 | 2022-04-25 20:17:43 | \t                   |           0 | \t                   | activated |                1 |
|   16 | Дмитрий                         | d.pivovarov@cdek.market     | $2y$10$nMG6KrqRZZRlyq6r8Ohl9eblBxN735tBpCEX/kGQMJ/EOCqcYj.tK | \t       | \t         | +79122178096 | B5RGgpFZOvhApIZsmk4CoYxahS6GH0sF2nh1LHw41UF8K8K5HaEmjH2tLDYu | 2022-04-26 01:25:55 | 2022-04-26 01:25:55 | \t                  | \t                   |           0 | \t                   | activated |                0 |
|   17 | Евгений                         | E-shishoff@yandex.ru        | $2y$10$HFhC4kUw8AwQ5MyLgJVBgeQdTvVFwApRAGATt8zfw0LvRImWBXgem | \t       | 1985-06-24 | 89030254443  | kNQV2nvjZKqQT3Vve1JeUxtiFGDe5VqALQxLcwVnuuYSwotLOhbDVJ50vutb | 2022-04-27 14:36:07 | 2022-08-09 16:15:34 | \t                  | \t                   |           0 | \t                   | activated |                0 |
|   18 | Михайлов Андрей Андреевич       | Rassvet787898@gmail.com     | $2y$10$nHmdS42QfUiKNs3HQKEa/efSmaky1dJWBwpXE.GDaDrEVUTHUXONa | \t       | 1992-02-09 | +79281808844 | 4LbyIeMfpLruyCXTQEgeunaFycYhEFwEzCTJq3Gv1zaiI2WksoZMg88ZY5U1 | 2022-04-28 16:50:55 | 2022-06-19 16:24:00 | 2022-04-28 12:50:55 | \t                   |           0 | \t                   | activated |                0 |
|   19 | Мехтизаде Джахангир Ришад оглы  | mekhtizade@gmail.com        | $2y$10$amB3VOU5EGClqxG8P31udefw3APB1UaJoo.j1TW/XOQZT5P4Uyn4K | \t       | 1960-05-31 | 89510970853  | uj1SJLbFugJXi8SGK9RjzLQmyw5Ipllh1HJUf1YqRKSxJD8BwNBkFBTo23AX | 2022-04-30 00:31:37 | 2022-04-30 00:34:12 | 2022-04-29 20:31:37 | \t                   |           0 | \t                   | activated |                0 |
|   20 | Ирина Малащенко                 | malashchenkoirina@yandex.ru | $2y$10$IB/TlJfu/e0dwWix2SQUdeAsC868hB35e420g6KCVef2Wn3EXl1xG | \t       | \t         | \t           | \t                                                           | 2022-04-30 05:03:34 | 2022-04-30 05:03:34 | 2022-04-30 01:03:34 | \t                   |           0 | \t                   | activated |                0 |
|   21 | Дмитртй                         | dk06@bk.ru                  | $2y$10$Tb9QtJxnrjcFibQIQDm3VeaRWDqbqCQwgASUThGaIfrmEZTKUcRFe | \t       | \t         | \t           | \t                                                           | 2022-04-30 18:21:30 | 2022-04-30 18:21:30 | 2022-04-30 14:21:30 | \t                   |           0 | \t                   | activated |                0 |
|   22 | Оксана                          | o.levina@cdek.ru            | $2y$10$n3uZnFVHbn5sF5fnySP/jO8YKXHNYNK5BiVgBgoNAilWH5M5popSm | \t       | \t         | \t           | \t                                                           | 2022-04-30 19:31:46 | 2022-04-30 19:31:46 | 2022-04-30 15:31:46 | \t                   |           0 | \t                   | activated |                0 |
|   23 | Константин                      | Kostyan_ix@bk.ru            | $2y$10$L5WBdfUqawPBsGAuV7yM7.BJ5d8f1bEQwWMEUUoBah8VFCsvSefi. | \t       | \t         | \t           | \t                                                           | 2022-04-30 19:55:49 | 2022-04-30 19:55:49 | 2022-04-30 15:55:49 | \t                   |           0 | \t                   | activated |                0 |
|   24 | Вячеслав                        | v.buzykanov@cdek.ru         | $2y$10$sFRW/eY1GJzotzbk3.bYkumLoTh9yHETm646pgrkUxnUI4eg8oiEu | \t       | \t         | \t           | \t                                                           | 2022-04-30 21:12:42 | 2022-04-30 21:12:42 | 2022-04-30 17:12:42 | \t                   |           0 | \t                   | activated |                0 |
|   25 | Наталья Сергеевна Евстратова    | evstratova.rostov@yandex.ru | $2y$10$Mu25A8ZCSoeIbIsnCWvAAOvMty9edVH3OIqaj17sa4R/lmEDklAZS | \t       | 1975-01-04 | +79281375860 | 7dkXBVy1fi8RDfVMwCs4k8Wjs1DOwsevUfSb0MzdfNmd5RYQZIV11VaAYUts | 2022-04-30 22:09:51 | 2022-07-14 13:00:46 | 2022-04-30 18:09:51 | \t                   |           0 | \t                   | activated |                0 |
|   26 | Муромцев Иван Николаевич        | zona.ivan@myttk.ru          | $2y$10$k390PUcwl43E0gt6g1biN.M5fV8k2IGUvySYRHOMVU13hZGPXLYmi | \t       | 1985-09-17 | +79040724032 | \t                                                           | 2022-05-01 12:10:48 | 2022-05-01 12:12:32 | 2022-05-01 08:10:48 | \t                   |           0 | \t                   | activated |                0 |
|   27 | Люция                           | krematorilife@mail.ru       | $2y$10$tBNjIpP.FeKhgQafDRRgu.z2SoSQjYZz6ZHjJ.6D7UOques.t12B2 | \t       | \t         | \t           | \t                                                           | 2022-05-01 15:02:48 | 2022-05-01 15:02:48 | 2022-05-01 11:02:48 | \t                   |           0 | \t                   | activated |                0 |
|   28 | Ольга Денисова                  | dir-sochi@cdek.ru           | $2y$10$99uQXigQPLoW6/hBBgMK7OVop.LZRhv22yRgY7SlRFY2i/Yd6fa8W | \t       | \t         | \t           | \t                                                           | 2022-05-01 15:22:30 | 2022-05-01 15:22:30 | 2022-05-01 11:22:30 | \t                   |           0 | \t                   | activated |                0 |
|   29 | Федосеев Леонид Валерьевич      | levva82@mail.ru             | $2y$10$XNwPIp47O0AIA7oZ0vUkbuPtAjb5nz74VzcHGJyWhUWjzuZbKVeTm | \t       | \t         | \t           | \t                                                           | 2022-05-01 19:01:33 | 2022-05-01 19:01:33 | 2022-05-01 15:01:33 | \t                   |           0 | \t                   | activated |                0 |
|   30 | Олег                            | dudarenko17@gmail.com       | $2y$10$nUxRI1b82C..pHcWYMmKreQKUw0alxwjqqI6ZWCgjFyAXhNXiQxOu | \t       | \t         | \t           | \t                                                           | 2022-05-02 01:28:47 | 2022-05-02 01:28:47 | 2022-05-01 21:28:47 | \t                   |           0 | \t                   | activated |                0 |
|   31 | Дмитрий                         | vieraloverps@gmail.com      | $2y$10$UqMsTM7q6p7D/DhrUO4CReBeQU2mIYGLu847R3KmRLs8bXPsHiW0q | \t       | \t         | \t           | \t                                                           | 2022-05-02 09:19:09 | 2022-05-02 09:19:09 | 2022-05-02 05:19:09 | \t                   |           0 | \t                   | activated |                0 |
```


## About final data

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
 |    |    |-- password_hash: string (nullable = true)
 |    |    |-- id: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 27.61% |
| Emails | 99.88% |
| Birth_date | 0.00% |
| Accounts | 100.00% |
| Actuality | 100.00% |



### Data sample
```
| names                               | phones          | emails                         | birth_date   | accounts                                                                                                                                            | actuality   |
|:------------------------------------|:----------------|:-------------------------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Фарид']                           | ['79644580675'] | ['azarituru1996@gmail.com']    |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$B8cuDcztcqInppA3jneiC.iUDA8XFn1gzxlTfhtnEyw/gLwGTZQWy', id='305')]  | 09.05.2022  |
| ['Алексей']                         | ['79374417844'] | ['alexey.bahmetiev@mail.ru']   |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$solxB2Az6As2CZLP3rutr.29ypMzhg0K.vD8nF65ahtMvlCZHXNFe', id='444')]  | 07.05.2022  |
| ['Хализев Михаил Евгеньевич']       | ['79959162053'] | ['exomicky53@gmail.com']       |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$AU5Mu2cmhAWAzTavNDpY8u5Y8CH0G59htaOxzRm0TGCRVat0sipgG', id='471')]  | 07.05.2022  |
| ['Печников Александр Валерьевич']   | ['79277583166'] | ['pechnikow@gmail.com']        |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$MArXEEsmh.EZrRktqyaV3O/krlKVy.Zsa2IHssobu90KSpVNVoZKi', id='629')]  | 07.05.2022  |
| ['Новохацкий Сергей Александрович'] | ['79497176666'] | ['shakhta12@gmail.com']        |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$NjVXzN0w13.RYCbLkQ0gSOqgqgcsUC7FqS49yT4SAfRbFv9X5OLLS', id='646')]  | 07.05.2022  |
| ['Артем']                           |                 | ['aurironbg@gmail.com']        |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$mwjJoPVZjfT51p.HHoNWh.HAoMsZmjYUel.5ucJOT3wSalPVdT60C', id='1238')] | 07.05.2022  |
| ['Sergey']                          |                 | ['damnednax@mail.ru']          |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$PolEj385fvTDTOhO5oD1meNELaDtUUUxyRC803mcP7Yi9MNSzxUy2', id='1862')] | 08.05.2022  |
| ['Александр']                       |                 | ['sasha.1997@list.ru']         |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$XcJ93ocfB3Jd2iN9t1PymOYXjhKTpwD6rISBr6RW5L6lbKtLldYbS', id='2242')] | 08.05.2022  |
| ['Павел']                           | ['79224777888'] | ['bot309@ya.ru']               |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$1zZL6xjNSIdCr5.tNKhpBOVsMVN7.5aNX2u2eZZL71RuWjsdcjbrC', id='2319')] | 08.05.2022  |
| ['Гапчук Владимир Викторович']      | ['79146501928'] | ['vlgapchuk@bk.ru']            |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$euvuQgNUVPOLx.cJw0BMmutNFqnBxQ2mWY.G3t26Sm43jbmstDPe.', id='2774')] | 08.05.2022  |
| ['Барашов Виктор']                  |                 | ['v.barashov@cdek.ru']         |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$3jWH/XxJDoup.JpWA3cUA.kpVBOE.UA6t98fZoeM9XZwurNR9MQsq', id='2829')] | 08.05.2022  |
| ['Александров Даниил Михайлович']   | ['79788164589'] | ['danielemontana94@yandex.ru'] |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$L1z0tnXStGrnzWtGzqJEm.CoQXpkKlZdJA/Dqk1G0iKUXYSpjd2eC', id='3066')] | 08.05.2022  |
| ['Леонид']                          |                 | ['leonidasfan@yandex.ru']      |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$0r9Jk3.UZTWrmmRYWjSEr.8FYpz5a9DvKwx//VyPEOpTK8QrpAcI2', id='3555')] | 08.05.2022  |
| ['Roman']                           | ['79892970179'] | ['morrq1@gmail.com']           |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$ZJz.VUlADyYOBCOZc16eUOakO5lvuRomecoQKKhYwan/Ihm98n1TG', id='3882')] | 08.05.2022  |
| ['Александр']                       |                 | ['aleksandr2483@gmail.com']    |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$N3S48CfUV/.bIKgTCcL9KuR.cmC0GXTzg/vYq7rYntAKlI4Qsh.cq', id='3903')] | 08.05.2022  |
| ['Зеленяев Сергей Евгеньевич']      | ['79266378484'] | ['sergey_zelenyaev@mail.ru']   |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$pzvo9gQzGmVmRg65tUdtfeyhwUHmjsFSJZltM71LbISQzmHXgz7qW', id='3982')] | 08.05.2022  |
| ['Ирина Чепурнова']                 |                 | ['pro100irisk@mail.ru']        |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$fkvo.gb6k3dAuPZPLnk3oOp3PenK2LcmMLLKg7sNFp8hIqsBbyJTi', id='4188')] | 08.05.2022  |
| ['Сергей']                          |                 | ['sergik_e_75@mail.ru']        |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$LrGwxBLwEX6wm7VGS5boiOufcVUbTVoEI1ioeQU8dA9.Zv8N7E5Tq', id='4242')] | 08.05.2022  |
| ['Александр']                       |                 | ['alex281198@yandex.ru']       |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$Jig6cyCQwQ846SwiS5gyFOw4xjmOgmWY2GQN6eMtm688VMbKClVga', id='4420')] | 08.05.2022  |
| ['Кирилл']                          | ['79168272225'] | ['kirykvs@mail.ru']            |              | [Row(title='CDEK shopping', link='https://cdek.shopping', password_hash='$2y$10$50VELn4eHc/yuiIRO/ROdui8LMU26l1XfymHG21TouzEqZybQCHPG', id='4477')] | 08.05.2022  |
```