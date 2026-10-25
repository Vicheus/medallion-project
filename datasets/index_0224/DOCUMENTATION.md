# Parsetron results

## About row data

> - Code name: index_0224
> - File path: /media/user/SAMSUNG/Databases/index_0224/raw/users_preprocessed.csv
> - Total rows: 43264

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- username: string (nullable = true)
 |-- password_hash: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- birth_date: date (nullable = true)
 |-- city: string (nullable = true)
 |-- street: string (nullable = true)

```

### Data sample
```
|   ID | username     | password_hash                            | first_name   | last_name   | middle_name   | email                         | gender   |       phone | birth_date   | city   | street         |
|-----:|:-------------|:-----------------------------------------|:-------------|:------------|:--------------|:------------------------------|:---------|------------:|:-------------|:-------|:---------------|
|    1 | admin_zimnie | 8j+TvM5\2ba481332a628ac89116d4f8440d4b1b | Сергей       | Мокочунин   |               | smak22@yandex.ru              | F        | 89168094104 | 1982-11-09   | Москва |                |
|   12 | susljak      | _jA97Rh.1a7139ee06279abb45d3189258bd5a99 | евгений      |             |               | susljak@rambler.ru            | M        |             |              | Москва | Новослободская |
|   18 | toomielsors  | VHz0YtLn808ad4c277a07031482ec256c9d4c602 | toomielsors  | toomielsors | toomielsors   | vevaemaiblep433@yandex.ru     |          |             |              |        |                |
|   19 | lewnoible    | NNN5vqoDca1c34c7af8a9d10f0070dcc1cd846ed | lewnoible    | lewnoible   | lewnoible     | chooggilt@hotmail.com         |          |             |              |        |                |
|   20 | prepterne    | beNp0Inp27172cfa9690b6f79ad45d0de7b69b92 | prepterne    | prepterne   | prepterne     | flouppover33444@hotmail.com   |          |             |              |        |                |
|   21 | susljak1     | JUWKNYSJ89b0328eba9c8969f86706cf7696f929 | Е.Д.         | Суслин      |               | susljak@rambler.ru            |          |             |              |        |                |
|   22 | alipopfre    | KF77loSnfce16c40703b7d62950000575808cb3d | alipopfre    | alipopfre   | alipopfre     | alipopfre@hotmail.com         |          |             |              |        |                |
|   23 | Demkayake    | 3hQbmfiq9564ea670ac2a47d8671db99906dbc30 | Demkayake    | Demkayake   | Demkayake     | rghrtwaer@shoeonlineblog.com  |          |             |              |        |                |
|   24 | MuffermFrof  | 99BYHu5S050c6e997b3d21d37d052ebe452c6a48 | MuffermFrof  | MuffermFrof | MuffermFrof   | erhtrhwqa@shoeonlineblog.com  |          |             |              |        |                |
|   25 | akastrel     | nzWqS1IN6c2d232c8139b15cd75bde7b880a9640 |              | Артем       |               | akastrel@gmail.com            |          |             |              |        |                |
|   26 | sadesign823  | QzU2DMxCa0cfab3f1f503f239c839ddc7067fdd3 |              | Алексей     |               | sadesign823@gmail.com         |          |             |              |        |                |
|   27 | Goxfagiox    | Voaabix13cfc815fe39cd2dad244fc5775b10c00 | Goxfagiox    | Goxfagiox   | Goxfagiox     | newfefs@hotmail.com           |          |             |              |        |                |
|   28 | Fayzullin-MR | rR5aAuKm35a4e12629b6cc0879881490ccfbd505 | Марат        | Файзуллин   |               | fayzullin-mr@yandex.ru        |          |             |              |        |                |
|   29 | kozlovdn     | ShI3o5Wi73e4cd821f1c31e19cc7f0863dec2cfb | Денис        | Козлов      |               | kozlovdn@yandex.ru            |          |             |              |        |                |
|   30 | rossignol09  | O.5zQ#7w4daa5ed3339385c9fd4f6d622f94a076 | Артур        | Узденов     |               | rossignol09@mail.ru           |          |             |              |        |                |
|   31 | 5421539      | YjPKcgzc672d27a95bef667fa392e51896482fa4 | Николай      | Куприянов   |               | 5421539@mail.ru               |          |             |              |        |                |
|   32 | polinakr21   | 5SVwYucQ423315ef82810b7a5f3d59d3e60e995c | Полина       | Лабинцева   |               | polinakr21@mail.ru            |          |             |              |        |                |
|   33 | Plabintseva  | g0hrpMsq24dcfe6b0c9aeafe21a03acf73693bfa | Александра   | Никольская  |               | plabintseva@galleryk.ru       |          |             |              |        |                |
|   34 | zakharovsky  | IB0hbwb590c4811a93c7d5a801dfc636537cdbdd |              | Владислав   |               | zakharovsky@mediaselection.ru |          |             |              |        |                |
|   35 | Angeminokax  | HnXXxKJg9eeae1430bca45f714f783be1accbbbd | Angeminokax  | Angeminokax | Angeminokax   | angemino2013@hotmail.com      |          |             |              |        |                |
```

> - Code name: index_0224
> - File path: /media/user/SAMSUNG/Databases/index_0224/raw/order_props_preprocessed.csv
> - Total rows: 158446

### Schema
```
root
 |-- user_id: integer (nullable = true)
 |-- prop_code: string (nullable = true)
 |-- prop_value: string (nullable = true)

```

### Data sample
```
|   user_id | prop_code   | prop_value                   |
|----------:|:------------|:-----------------------------|
|        12 | ADDRESS     | Абв                          |
|        21 | fio         | Суслин Е.Д.                  |
|        21 | nomer_tel   | 8916111111                   |
|        21 | e-mail      | susljak@rambler.ru           |
|        21 | ADDRESS     | Новосущевская                |
|        25 | fio         | Артем                        |
|        25 | nomer_tel   | 89104273640                  |
|        25 | e-mail      | akastrel@gmail.com           |
|        25 | ADDRESS     | кибальчича 11/1 кв 61        |
|        26 | fio         | Алексей                      |
|        26 | nomer_tel   | 8 921 4397338                |
|        26 | e-mail      | sadesign823@gmail.com        |
|        26 | ADDRESS     | СПб                          |
|        28 | fio         | Файзуллин Марат              |
|        28 | nomer_tel   | 89851813446                  |
|        28 | e-mail      | Fayzullin-MR@yandex.ru       |
|        28 | ADDRESS     | Сумской проезд д.4/3, кв.140 |
|        29 | fio         | Козлов Денис                 |
|        29 | nomer_tel   | 8-916-185-75-49              |
|        29 | e-mail      | kozlovdn@yandex.ru           |
```


## About final data
> - Total rows: 36763

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
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)

```

### Data sample
```
| names                                                    | emails                                           | phones          | accounts                                                                                                                                           | address                                       |   sex |
|:---------------------------------------------------------|:-------------------------------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------|------:|
| ['Дзюба Михаил', 'Дзюба Михаил Николаевич']              | ['dzmihail@yandex.ru']                           | ['79859231206'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='dzmihail', password_hash='O1b3jLvIcb442872e44d70e047d70ee920b12de2')]                   |                                               |   nan |
| ['Масленников Сергей', 'Масленников Сергей Геннадьевич'] | ['sergey.kucher@me.com']                         | ['79622739070'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='sergey.kucher', password_hash='TsGrgGLz3e0eb4a030b67ff5e01e3c7fd9e73d17')]              | ['Самовывоз']                                 |   nan |
| ['Рязанов Евгений', 'Рязанов Евгений Петрович']          | ['john-rembo2007@ya.ru']                         | ['79155791688'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='John-rembo20071', password_hash='neoW2cHG29d8abecd076af8b19142676050461cb')]            |                                               |   nan |
| ['Суслин Евгений']                                       | ['suslin90@gmail.com']                           |                 | [Row(title='Zimnie', link='https://www.zimnie.com', login='suslin90@gmail.com', password_hash='kxsUZkfVbac87abebac0dac8e44e1c78e4b587bc')]         |                                               |   nan |
| ['Стеблен Андрей']                                       | ['info@zimnie.com']                              | ['79166848998'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='buyer1453479266vE', password_hash='NckXnl5m07843c95f3fbd36e31e7165785bb551e')]          | ['ул Русаковская дом 31 пятая секция кв 302'] |   nan |
| ['Чуличкова Евгения', 'Чуличкова Евгения Владимировна']  | ['evg.chulichkova@mail.ru']                      | ['79222166461'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='evg.chulichkova', password_hash='XJf86R1b7fb9e7b33ad1ad311e737facbc4c48e3')]            |                                               |   nan |
| ['Князева Еи']                                           | ['2knnyazeva@rambler.ru']                        | ['79161408025'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='2knnyazeva', password_hash='wqkMAIhue450123fa6dd063ff84c3be964904895')]                 | ['Крылатские холмы 39-1-201']                 |   nan |
| ['Валуйский']                                            | ['valuiskiy.s@mail.ru']                          | ['79185566878'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='valuiskiy.s', password_hash='IxVwecujfb6f23d9de018345afb7924eee23a986')]                |                                               |   nan |
| ['Юлия']                                                 | ['ynaz@yandex.ru']                               | ['79167403849'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='ynaz', password_hash=':e7HUb8!250d91fcdbc03bb1cae59f0b1cb7b1a0')]                       | ['ул Кибальчича д 2 кор 4 кв 53']             |   nan |
| ['Максим']                                               | ['foeniculum@mail.ru']                           | ['79055883360'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='foeniculum1', password_hash='v5O!!0xAa2ba4689523c6bb8c6b67cd4059bdee9')]                |                                               |   nan |
| ['Панов Владимир']                                       | ['zhanna.panova.1964@mail.ru']                   |                 | [Row(title='Zimnie', link='https://www.zimnie.com', login='zhanna.panova.1964@mail.ru', password_hash='UXio6e6xbe3c2358ba418b14642d823cd7f39827')] |                                               |   nan |
| ['Зуева Наталья', 'Зуева Наталья Владимировна']          | ['zueva76@mail.ru']                              | ['79219563305'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='zueva761', password_hash='6s?M;T5p664a78f536660a72508aa56312736cb5')]                   |                                               |   nan |
| ['Авакян Гамлет', 'Авакян Гамлет Врежович']              | ['avakyan12@mail.ru']                            | ['79152913207'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='avakyan12', password_hash='HdRyaJAf0b216b902e2ad3aebe4d47b260ec9196')]                  | ['ул. Кузнецкий мост 19 стр.2 оф. 301']       |   nan |
| ['Легостаев Владимир', 'Легостаев Владимир Леонидович']  | ['legostaevvl@gmail.com']                        | ['79036268657'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='LegostaevVL', password_hash='vnig5KAce8c60a928a6e631f6e1cbe9f87cb100a')]                | ['1-Ая Улица Ямского Поля Д.17 Стр.12']       |   nan |
| ['Виторова Виктория']                                    | ['info@zimnie.com', 'user1488477340@zimnie.com'] | ['79212366940'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='user1488477340', password_hash='YIO69WMqe909056e551f93e10f450c18c3fbc180')]             |                                               |   nan |
| ['Мамонов Спартак', 'Мамонов Спартак Маратович']         | ['spartakma@list.ru']                            | ['79046260498'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='spartakma', password_hash='mV0n2uWa4535d8c369a97a5ed25bfad2f94128d2')]                  |                                               |   nan |
| ['Марункевич Валерий', 'Марункевич Валерий Юрьевич']     | ['marunkevich67@mail.ru']                        | ['79056597284'] | [Row(title='Zimnie', link='https://www.zimnie.com', login='marunkevich67', password_hash='eOz6CaLVb7f0278f913f0f2daad98eb547a74ec9')]              |                                               |   nan |
| ['Dvacowefsqt Dvacowefs']                                | ['pr21@black-stones.ru']                         |                 | [Row(title='Zimnie', link='https://www.zimnie.com', login='DvaCowefs', password_hash='9HXm8NX81124e8e73f0ca00eb306430ffda69813')]                  |                                               |   nan |
| ['Dannycrazycl Dannycrazy']                              | ['materi-deti@i.ua']                             |                 | [Row(title='Zimnie', link='https://www.zimnie.com', login='DannyCrazy', password_hash='NtTPpQD650467d3969d26456150328ebd7486e0f')]                 |                                               |   nan |
| ['Aatmocksmoonst Aatmocksmoon']                          | ['quonahquee@bestmailonline.com']                |                 | [Row(title='Zimnie', link='https://www.zimnie.com', login='Aatmocksmoon', password_hash='BO9lPZZlc9d318bf6d6936a373e673b77da280f2')]               |                                               |   nan |
```