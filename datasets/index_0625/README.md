# Parsetron results

## About row data

> - Code name: index_0625
> - File path: users_by.csv
> - Total rows: 1957

### Schema
```
root
 |-- regid: integer (nullable = true)
 |-- email: string (nullable = true)
 |-- password: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- mobile: string (nullable = true)
 |-- country: string (nullable = true)
 |-- ipadd: string (nullable = true)

```

### Data sample
```
|   regid | email                         | password                         | first_name   | last_name       | mobile        | country   | ipadd           |
|--------:|:------------------------------|:---------------------------------|:-------------|:----------------|:--------------|:----------|:----------------|
|   99391 | natnnelly@gmail.com           | 11a8a15ab73371b1137e213941c8623a | Nat & Nelly  | - Helping Team! | <blank>       | belarus   | 172.68.246.70   |
|  100712 | krishnalila03@gmail.com       | ab27849af85db26d0fd79f8da0f72af8 | Yury         | Aleinikau       | +375257944551 | belarus   | 172.68.10.36    |
|  101438 | veronikapestritsina@yandex.by | 7b7d0b14cadd8f6f4be9076d63588863 | Andrei       | Pestritsin      | <blank>       | belarus   | 172.68.244.212  |
|  102347 | sandrinio29@gmail.com         | 8b71981131a8508dab84579fb23e5f16 | Aliaksandr   | Khakhlou        | <blank>       | belarus   | 172.68.246.148  |
|  103024 | ferdinandzxzz@gmail.com       | 5860080702f199a1d877a7de48e2449b | Aliaksandr   | Radziukevich    | <blank>       | belarus   | 172.68.244.68   |
|  103128 | chddmitriy@gmail.com          | 125b55719382bd10c9728ebce68ebbc0 | dmitriy      | chechulin       | <blank>       | belarus   | 172.68.245.9    |
|  104278 | shishov.nikitka@gmail.com     | 0668ba748facb263ff3eedabc62511fd | Nikita       | Shishov         | <blank>       | belarus   | 172.68.245.63   |
|  104657 | digitalliders@gmail.com       | 3f8cd173fd8bf4c1d0452e6df053da81 | Dmitry       | Yanchuk         | <blank>       | belarus   | 172.68.245.231  |
|  104685 | maliaroff@gmail.com           | 5f081c0c642cc250cde82066d539bed9 | Siarhei      | Maliarou        | <blank>       | belarus   | 162.158.114.6   |
|  104811 | svytik2017v@mail.ru           | 88ca80df2d72dbebcef83a756c323da1 | Ihar         | Volchovich      | <blank>       | belarus   | 172.68.244.128  |
|  104865 | bristol252@gmail.com          | 16cdefd98fc606f1bd32d7740833e7c6 | Elena        | Powarowa        | +375333511233 | belarus   | 172.68.244.62   |
|  104948 | reds.brest@gmail.com          | 8c59f345a2bce629307bc3f82e362f4e | Kirill       | Mironov         | <blank>       | belarus   | 162.158.114.72  |
|  105129 | dr.e-timo@yandex.by           | 25881d40494de9ddfc4c99a86070380a | Yauheni      | Dzidukh         | <blank>       | belarus   | 172.68.244.98   |
|  105522 | mitranor@yandex.by            | e13d7f6af0c718c1ec52af1faaaff5a4 | Mikhail      | Kapychka        | <blank>       | belarus   | 172.68.246.178  |
|  105563 | artem67311@gmail.com          | f18dd0cd895ee8ef1a103d2070e1e1cf | Artsiom      | Seniukovich     | <blank>       | belarus   | 162.158.114.102 |
|  105597 | mashalevickay1@gmail.com      | eaec7877a8766b9ed24a9e16328041c1 | Maryia       | Liavitskaya     | <blank>       | belarus   | 172.68.244.80   |
|  105712 | nick.nemcov@gmail.com         | f2f1b5a61b558dd9cd061a4da4f50051 | Aliaksei     | Trunou          | <blank>       | belarus   | 172.68.244.158  |
|  105746 | toliy2012@list.ru             | a17e79c3ba71837c58cb8dc06537b179 | Anatol       | Filanovich      | <blank>       | belarus   | 172.68.244.128  |
|  106164 | zeleniy70@gmail.com           | 199f3ef0a67a26b5e9c8a2870a4271b8 | Gennadiy     | Basharimov      | <blank>       | belarus   | 172.68.245.123  |
|  106351 | koliank89@gmail.com           | ff8dfd580284d24a58f5d3a92bf5fb33 | nickolai     | nolt            | <blank>       | belarus   | 172.68.10.174   |
```


## About final data
> - Total rows: 1515

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |
| Phones | 0.79% |
| Ips | 99.87% |
| Accounts | 100.00% |



### Data sample
```
| names                       | emails                            | phones           | ips                         | accounts                                                                                                                    |
|:----------------------------|:----------------------------------|:-----------------|:----------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| ['Helping Team Nat Nelly']  | ['natnnelly@gmail.com']           |                  | [Row(ip='172.68.246.70')]   | [Row(title='Trident Crypto Fund', login='natnnelly@gmail.com', password_hash='11a8a15ab73371b1137e213941c8623a')]           |
| ['Aleinikau Yury']          | ['krishnalila03@gmail.com']       | ['375257944551'] | [Row(ip='172.68.10.36')]    | [Row(title='Trident Crypto Fund', login='krishnalila03@gmail.com', password_hash='ab27849af85db26d0fd79f8da0f72af8')]       |
| ['Pestritsin Andrei']       | ['veronikapestritsina@yandex.by'] |                  | [Row(ip='172.68.244.212')]  | [Row(title='Trident Crypto Fund', login='veronikapestritsina@yandex.by', password_hash='7b7d0b14cadd8f6f4be9076d63588863')] |
| ['Khakhlou Aliaksandr']     | ['sandrinio29@gmail.com']         |                  | [Row(ip='172.68.246.148')]  | [Row(title='Trident Crypto Fund', login='sandrinio29@gmail.com', password_hash='8b71981131a8508dab84579fb23e5f16')]         |
| ['Radziukevich Aliaksandr'] | ['ferdinandzxzz@gmail.com']       |                  | [Row(ip='172.68.244.68')]   | [Row(title='Trident Crypto Fund', login='ferdinandzxzz@gmail.com', password_hash='5860080702f199a1d877a7de48e2449b')]       |
| ['Chechulin Dmitriy']       | ['chddmitriy@gmail.com']          |                  | [Row(ip='172.68.245.9')]    | [Row(title='Trident Crypto Fund', login='chddmitriy@gmail.com', password_hash='125b55719382bd10c9728ebce68ebbc0')]          |
| ['Shishov Nikita']          | ['shishov.nikitka@gmail.com']     |                  | [Row(ip='172.68.245.63')]   | [Row(title='Trident Crypto Fund', login='shishov.nikitka@gmail.com', password_hash='0668ba748facb263ff3eedabc62511fd')]     |
| ['Yanchuk Dmitry']          | ['digitalliders@gmail.com']       |                  | [Row(ip='172.68.245.231')]  | [Row(title='Trident Crypto Fund', login='digitalliders@gmail.com', password_hash='3f8cd173fd8bf4c1d0452e6df053da81')]       |
| ['Maliarou Siarhei']        | ['maliaroff@gmail.com']           |                  | [Row(ip='162.158.114.6')]   | [Row(title='Trident Crypto Fund', login='maliaroff@gmail.com', password_hash='5f081c0c642cc250cde82066d539bed9')]           |
| ['Volchovich Ihar']         | ['svytik2017v@mail.ru']           |                  | [Row(ip='172.68.244.128')]  | [Row(title='Trident Crypto Fund', login='svytik2017v@mail.ru', password_hash='88ca80df2d72dbebcef83a756c323da1')]           |
| ['Powarowa Elena']          | ['bristol252@gmail.com']          | ['375333511233'] | [Row(ip='172.68.244.62')]   | [Row(title='Trident Crypto Fund', login='bristol252@gmail.com', password_hash='16cdefd98fc606f1bd32d7740833e7c6')]          |
| ['Mironov Kirill']          | ['reds.brest@gmail.com']          |                  | [Row(ip='162.158.114.72')]  | [Row(title='Trident Crypto Fund', login='reds.brest@gmail.com', password_hash='8c59f345a2bce629307bc3f82e362f4e')]          |
| ['Dzidukh Yauheni']         | ['dr.e-timo@yandex.by']           |                  | [Row(ip='172.68.244.98')]   | [Row(title='Trident Crypto Fund', login='dr.e-timo@yandex.by', password_hash='25881d40494de9ddfc4c99a86070380a')]           |
| ['Kapychka Mikhail']        | ['mitranor@yandex.by']            |                  | [Row(ip='172.68.246.178')]  | [Row(title='Trident Crypto Fund', login='mitranor@yandex.by', password_hash='e13d7f6af0c718c1ec52af1faaaff5a4')]            |
| ['Seniukovich Artsiom']     | ['artem67311@gmail.com']          |                  | [Row(ip='162.158.114.102')] | [Row(title='Trident Crypto Fund', login='artem67311@gmail.com', password_hash='f18dd0cd895ee8ef1a103d2070e1e1cf')]          |
| ['Liavitskaya Maryia']      | ['mashalevickay1@gmail.com']      |                  | [Row(ip='172.68.244.80')]   | [Row(title='Trident Crypto Fund', login='mashalevickay1@gmail.com', password_hash='eaec7877a8766b9ed24a9e16328041c1')]      |
| ['Trunou Aliaksei']         | ['nick.nemcov@gmail.com']         |                  | [Row(ip='172.68.244.158')]  | [Row(title='Trident Crypto Fund', login='nick.nemcov@gmail.com', password_hash='f2f1b5a61b558dd9cd061a4da4f50051')]         |
| ['Filanovich Anatol']       | ['toliy2012@list.ru']             |                  | [Row(ip='172.68.244.128')]  | [Row(title='Trident Crypto Fund', login='toliy2012@list.ru', password_hash='a17e79c3ba71837c58cb8dc06537b179')]             |
| ['Basharimov Gennadiy']     | ['zeleniy70@gmail.com']           |                  | [Row(ip='172.68.245.123')]  | [Row(title='Trident Crypto Fund', login='zeleniy70@gmail.com', password_hash='199f3ef0a67a26b5e9c8a2870a4271b8')]           |
| ['Nolt Nickolai']           | ['koliank89@gmail.com']           |                  | [Row(ip='172.68.10.174')]   | [Row(title='Trident Crypto Fund', login='koliank89@gmail.com', password_hash='ff8dfd580284d24a58f5d3a92bf5fb33')]           |
```