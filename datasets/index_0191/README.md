# Parsetron results

## About row data

> - Code name: index_0191
> - File path: /media/user/SAMSUNG/Databases/index_0191/raw/users_preprocessed.csv
> - Total rows: 4459

### Schema
```
root
 |-- NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- SECOND_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- PERSONAL_PHONE: string (nullable = true)
 |-- LOGIN: string (nullable = true)
 |-- PASSWORD: string (nullable = true)

```

### Data sample
```
| NAME                              | LAST_NAME   | SECOND_NAME   | EMAIL                   | PERSONAL_PHONE   | LOGIN                   | PASSWORD                                 |
|:----------------------------------|:------------|:--------------|:------------------------|:-----------------|:------------------------|:-----------------------------------------|
| Individ                           |             |               | im@belagro.com          |                  | admin                   | 3~bKT5o!a1ee18c20def23bcafbc39d36daf896e |
| Александр                         | Черный      | Павлович      | ac@belagro.com          | +7-495-580 63 73 | ac@belagro.com          | 2yF*uK8,55abaeae06500799f41d9e3904995c36 |
| YA.Sharnina                       |             |               | YA.Sharnina@belagro.com |                  | YA.Sharnina@belagro.com | 5m@J5w[S0b2468817c2ba70ee53e624667e91ce3 |
| Дмитрий                           | Косяков     |               | d1m0n06@mail.ru         | +7-909-1557534   | d1m0n06@mail.ru         | mKVRX10h881897b74f29db6a35c675ad11a49c29 |
| ИП Кузьменко Сергей Александрович | Кузьменко   |               | ne-on007@mail.ru        | 80296782825      | ne-on007@mail.ru        | KX3dbF1C9a72ee7a0ae64b30311894f2cdec8be5 |
| игорь                             | целуйко     |               | ihar.tsaluika@yandex.ru | +375445103342    | ihar.tsaluika@yandex.ru | ScvS4sDK66cea02cd987b1bb06d2ee99215b46c0 |
| Brucetep                          | Brucetep    |               | brucespess@mail.ru      | 87567516247      | brucespess@mail.ru      | cGu66Akfac07a9cbfc2db806aace7299493b9f3a |
| Александр                         | черный      |               | nighton@yandex.ru       | +375447725001    | nighton@yandex.ru       | Yen8oHeH32e4b417b80a9aa0c5484b160a83e017 |
| Александр                         | черный      |               | 22nighton@yandex.ru     | +375447725001    | 22nighton@yandex.ru     | 136Vsv6M558a7cfc167bc793f189482292b6ec8f |
| губич                             | артем       |               | artsiomhubich@mail.ru   | +375333666075    | artsiomhubich@mail.ru   | aHwsz7oN9b945858c5207b6d5b647a68fd32c3b9 |
| VikaSENroK                        | VikaSENroK  |               | vikagda@mail.ru         | 86154927446      | vikagda@mail.ru         | 2TWL5Ri67c402b9835ca6a3de82c450c6208f61c |
| Дмитрий                           | Кевра       |               | kevra.90@mail.ru        | 80259177475      | kevra.90@mail.ru        | blpt0nuH377650e73b66f4ef922cc0bc92ea3973 |
| MarikaGNLK                        | MarikaGNLK  |               | marinatem90@mail.ru     | 86783219995      | marinatem90@mail.ru     | RS4cYkT5cb7254f547a6477e52e4cad1d2bf16e4 |
| Юрий                              | Ростовский  |               | bisauto@tut.by          | +375292182609    | bisauto@tut.by          | Cngz3wKN6182d17ca4495569fc055d6b659be698 |
| Константин                        | Гурин       |               | Kostgurin@yandex.ru     | +79620823640     | Kostgurin@yandex.ru     | G3CyOKnQ85f6a3b0e15430dc83da979ec12502b8 |
| Удалить                           | Тест        |               | afsa@addf.ru            | 13123123123123   | afsa@addf.ru            | 7qTbcKIg7bc57ae9873c148e69b036aabb336f29 |
| SSfordihano                       | SSfordihano |               | pr16@black-stones.ru    | 84464858162      | pr16@black-stones.ru    | jfrU4hTH89af0619b8dbce93f3d7b596b9508c76 |
| Sailippsymn                       | Sailippsymn |               | r8974jjil@gmail.com     | 88664422845      | r8974jjil@gmail.com     | rEwyaT68fc714a8703b7addf8bf0d6ca468f1378 |
| Олег                              | Пузиновский |               | apk.kgk@mail.ru         | 80295076659      | apk.kgk@mail.ru         | ,Hr3L0i=b92f12a7c95b61234951d49c63ffaec1 |
| benkunmoM                         | benkunmoM   |               | bbenkunsenko@gmail.com  | 82253434853      | bbenkunsenko@gmail.com  | ha8Rto6bb5af2a8c557f8d83b1027b21fc318578 |
```


## About final data
> - Total rows: 4400

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
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
| names                                           | phones           | emails                      | accounts                                                                                                                                      |
|:------------------------------------------------|:-----------------|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| ['Individ']                                     |                  | ['im@belagro.com']          | [Row(title='Белагро', link='https://1belagro.by', login='admin', password_hash='3~bKT5o!a1ee18c20def23bcafbc39d36daf896e')]                   |
| ['Черный Александр Павлович']                   |                  | ['ac@belagro.com']          | [Row(title='Белагро', link='https://1belagro.by', login='ac@belagro.com', password_hash='2yF*uK8,55abaeae06500799f41d9e3904995c36')]          |
| ['Ya.Sharnina']                                 |                  | ['ya.sharnina@belagro.com'] | [Row(title='Белагро', link='https://1belagro.by', login='YA.Sharnina@belagro.com', password_hash='5m@J5w[S0b2468817c2ba70ee53e624667e91ce3')] |
| ['Косяков Дмитрий']                             |                  | ['d1m0n06@mail.ru']         | [Row(title='Белагро', link='https://1belagro.by', login='d1m0n06@mail.ru', password_hash='mKVRX10h881897b74f29db6a35c675ad11a49c29')]         |
| ['Кузьменко Ип Кузьменко Сергей Александрович'] | ['375296782825'] | ['ne-on007@mail.ru']        | [Row(title='Белагро', link='https://1belagro.by', login='ne-on007@mail.ru', password_hash='KX3dbF1C9a72ee7a0ae64b30311894f2cdec8be5')]        |
| ['Целуйко Игорь']                               | ['375445103342'] | ['ihar.tsaluika@yandex.ru'] | [Row(title='Белагро', link='https://1belagro.by', login='ihar.tsaluika@yandex.ru', password_hash='ScvS4sDK66cea02cd987b1bb06d2ee99215b46c0')] |
| ['Brucetep Brucetep']                           |                  | ['brucespess@mail.ru']      | [Row(title='Белагро', link='https://1belagro.by', login='brucespess@mail.ru', password_hash='cGu66Akfac07a9cbfc2db806aace7299493b9f3a')]      |
| ['Черный Александр']                            | ['375447725001'] | ['nighton@yandex.ru']       | [Row(title='Белагро', link='https://1belagro.by', login='nighton@yandex.ru', password_hash='Yen8oHeH32e4b417b80a9aa0c5484b160a83e017')]       |
| ['Черный Александр']                            | ['375447725001'] | ['22nighton@yandex.ru']     | [Row(title='Белагро', link='https://1belagro.by', login='22nighton@yandex.ru', password_hash='136Vsv6M558a7cfc167bc793f189482292b6ec8f')]     |
| ['Артем Губич']                                 | ['375333666075'] | ['artsiomhubich@mail.ru']   | [Row(title='Белагро', link='https://1belagro.by', login='artsiomhubich@mail.ru', password_hash='aHwsz7oN9b945858c5207b6d5b647a68fd32c3b9')]   |
| ['Vikasenrok Vikasenrok']                       |                  | ['vikagda@mail.ru']         | [Row(title='Белагро', link='https://1belagro.by', login='vikagda@mail.ru', password_hash='2TWL5Ri67c402b9835ca6a3de82c450c6208f61c')]         |
| ['Кевра Дмитрий']                               | ['375259177475'] | ['kevra.90@mail.ru']        | [Row(title='Белагро', link='https://1belagro.by', login='kevra.90@mail.ru', password_hash='blpt0nuH377650e73b66f4ef922cc0bc92ea3973')]        |
| ['Marikagnlk Marikagnlk']                       |                  | ['marinatem90@mail.ru']     | [Row(title='Белагро', link='https://1belagro.by', login='marinatem90@mail.ru', password_hash='RS4cYkT5cb7254f547a6477e52e4cad1d2bf16e4')]     |
| ['Ростовский Юрий']                             | ['375292182609'] | ['bisauto@tut.by']          | [Row(title='Белагро', link='https://1belagro.by', login='bisauto@tut.by', password_hash='Cngz3wKN6182d17ca4495569fc055d6b659be698')]          |
| ['Гурин Константин']                            |                  | ['kostgurin@yandex.ru']     | [Row(title='Белагро', link='https://1belagro.by', login='Kostgurin@yandex.ru', password_hash='G3CyOKnQ85f6a3b0e15430dc83da979ec12502b8')]     |
| ['Ssfordihano Ssfordihano']                     |                  | ['pr16@black-stones.ru']    | [Row(title='Белагро', link='https://1belagro.by', login='pr16@black-stones.ru', password_hash='jfrU4hTH89af0619b8dbce93f3d7b596b9508c76')]    |
| ['Sailippsymn Sailippsymn']                     |                  | ['r8974jjil@gmail.com']     | [Row(title='Белагро', link='https://1belagro.by', login='r8974jjil@gmail.com', password_hash='rEwyaT68fc714a8703b7addf8bf0d6ca468f1378')]     |
| ['Пузиновский Олег']                            | ['375295076659'] | ['apk.kgk@mail.ru']         | [Row(title='Белагро', link='https://1belagro.by', login='apk.kgk@mail.ru', password_hash=',Hr3L0i=b92f12a7c95b61234951d49c63ffaec1')]         |
| ['Benkunmom Benkunmom']                         |                  | ['bbenkunsenko@gmail.com']  | [Row(title='Белагро', link='https://1belagro.by', login='bbenkunsenko@gmail.com', password_hash='ha8Rto6bb5af2a8c557f8d83b1027b21fc318578')]  |
| ['Лютова Инесса']                               | ['375296594107'] | ['iniva100@mail.ru']        | [Row(title='Белагро', link='https://1belagro.by', login='iniva100@mail.ru', password_hash='9!rDIl3[e94b8051ee55fff863b25cccc39b0a47')]        |
```