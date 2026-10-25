# Parsetron results

## About row data

> - Code name: index_0090
> - File path: Ренессанс_Страхование_preprocessed.csv
> - Total rows: 737666

### Schema
```
root
 |-- name: string (nullable = true)
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- EMAIL: string (nullable = true)

```

### Data sample
```
| name                         | login                                         | password                                 | phone   | EMAIL                    |
|:-----------------------------|:----------------------------------------------|:-----------------------------------------|:--------|:-------------------------|
| Краснов Виктор               | krasnovvy@gmail.com                           | Df2~!4Ov2074d12412e621d595f780c445a1c840 |         | krasnovvy@gmail.com      |
| Иванов Максим Александрович  | PersArea_33ac982c-5424-434c-b9dc-1c95d23439e9 | 9QSX9z6G487fb3b4c41c0cec4ec444cbe588b767 |         | ivanovda@ads-soft.ru     |
| Львов Алексаднр              | PersArea_d41968bf-7a90-4139-bda2-30eaa3ab32b4 | 0YRNVANK9592a285c4a2019590a38113e3e829ee |         | lvoval@ads-soft.ru       |
| Александр Александр          | PersArea_b9ff171e-caa4-43ac-acc1-2bdb17276d24 | Fah2uTRR8e96861d9a2264736fd42c8910b0e9c0 |         | lvovalex92@gmail.com     |
| Приписнов Валентин           | PersArea_6e702672-afb4-4e20-b6e6-bcd49ec62efe | F7Rv3rdt4e9e20cad2c2a104077f21bc5a8a16f4 |         | valentinpri93@gmail.com  |
|                              | PersArea_2cc893df-eb4e-43f4-990f-fd4dc9d631fa | xNzciXOY0b254c71f3ce0610184b1c0f339a56dd |         | mail@web-slon.ru         |
| Майоров Александр Викторович | PersArea_93c996b6-1688-4b17-935b-969b6b82a013 | 8P2PmCibad748c39f1df62c78bfbd31b5ca09b24 |         | ekovarskaya@renins.com   |
| Карпова Ольга                | PersArea_60f6f1ec-d4e8-4458-8fea-1e35330a5304 | k6myx1Fp1d05fc93f6b2c7d8386ff1dd1faf1b8f |         | okarpova2@renins.com     |
| Щетинская Вера Александровна | PersArea_9cfdcc33-ce13-42ee-8364-a2f92d209272 | bnHFPAr59b2cca75403a2ca53f3f335117aaba1e |         | shetinsky.ivan@yandex.ru |
| Заводин Николай Викторович   | PersArea_1c31ac82-48dc-4873-b8ed-44662f2cbe8c | 3QGk5MxN1e5da4fd04745f82303a2d6b601053ad |         | s.nata37@yandex.ru       |
```


## About final data
> - Total rows: 308382

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

```

### Data sample
```
| names                               | emails   | phones          | accounts                                                                                                                                 |
|:------------------------------------|:---------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| ['Жидяевская Вероника Геннадьевна'] |          | ['79651083386'] | [Row(title='Ренессанс страхование', link='https://www.renins.ru', login=None, password_hash='t{0K,c9Fbe45b3a2710ec11883d93b2a1ecffddb')] |
| ['Егорова Анна']                    |          | ['79687159062'] | [Row(title='Ренессанс страхование', link='https://www.renins.ru', login=None, password_hash='5EDSx8vY51315bdf22b7e0420d10c2cfe2c4c9b8')] |
| ['Малышев Константин Рудольфович']  |          | ['79162950655'] | [Row(title='Ренессанс страхование', link='https://www.renins.ru', login=None, password_hash='3FRglCOk9d43ce765cde8623433088c042451dc1')] |
| ['Паршин Вадим Николаевич']         |          | ['79023800396'] | [Row(title='Ренессанс страхование', link='https://www.renins.ru', login=None, password_hash='AgG6VLpFf5aca96dd80761e18fc11ee5ac44a9c3')] |
| ['Ватеичкин Денис Геннадьевич']     |          | ['79610799192'] | [Row(title='Ренессанс страхование', link='https://www.renins.ru', login=None, password_hash='9x8FDsUO74a601bd79b914ed46273705fdf8bfec')] |
| ['Локтионов Николай Владимирович']  |          | ['79001231950'] | [Row(title='Ренессанс страхование', link='https://www.renins.ru', login=None, password_hash='IBv5RZqh020a72bbaa3d6073f29f11bb82b27a54')] |
| ['Терехов Виктор Иванович']         |          | ['79065920234'] | [Row(title='Ренессанс страхование', link='https://www.renins.ru', login=None, password_hash='DL9GEstt178b677d208a05a847f5c88c88165049')] |
| ['Абрамов Сергей Павлович']         |          | ['79271612246'] | [Row(title='Ренессанс страхование', link='https://www.renins.ru', login=None, password_hash='WGvD2DE553b5d36398a98c6425477e1b6d2da4ae')] |
| ['Гудков Дмитрий Геннадьевич']      |          | ['79093252573'] | [Row(title='Ренессанс страхование', link='https://www.renins.ru', login=None, password_hash='j2duj4T40749f849e952bbeb41ee654fbefd9034')] |
| ['Митричев Сергей Викторович']      |          | ['79265842241'] | [Row(title='Ренессанс страхование', link='https://www.renins.ru', login=None, password_hash='604s2eofdc43861b39d33e460f59716252ec448f')] |
```