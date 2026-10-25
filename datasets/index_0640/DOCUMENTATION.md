# Parsetron results

## About row data

> - File path: users_by_members.csv
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

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 0.84% |
| Emails | 100.00% |
| Ips | 99.86% |
| Accounts | 100.00% |



### Data sample
```
| names                     | phones           | emails                                           | ips                         | accounts                                                                                                                                                    |
|:--------------------------|:-----------------|:-------------------------------------------------|:----------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Bysy Bsu']              |                  | ['tr.a.n.thaitongcaugiay012.34567890@gmail.com'] | [Row(ip='27.67.132.21')]    | [Row(title='123RF', link='https://www.123rf.com/', login='Tr.a.n.thaitongcaugiay012.34567890@gmail.com', password_hash='de929b872e736cc0666b6ed6897a982b')] |
| ['Hgyw Hgd']              |                  | ['nguye.nchith.anhdongda1234567890@gmail.com']   | [Row(ip='27.67.191.181')]   | [Row(title='123RF', link='https://www.123rf.com/', login='nguye.nchith.anhdongda1234567890@gmail.com', password_hash='3e0ff45a305ab0f34918dfa9bc75b5c6')]   |
| ['Hysy Hwf']              |                  | ['t.ran.t.haitongcaugiay012345.67890@gmail.com'] | [Row(ip='27.67.33.3')]      | [Row(title='123RF', link='https://www.123rf.com/', login='t.ran.t.haitongcaugiay012345.67890@gmail.com', password_hash='f540515ced6e9d6b09b1a9e073214bb4')] |
| ['Lazarev Stanislav']     |                  | ['lsg17392@mail.ru']                             | [Row(ip='172.68.245.237')]  | [Row(title='123RF', link='https://www.123rf.com/', login='lsg17392@mail.ru', password_hash='d2c31ff83260472178c2dea1428b3e1a')]                             |
| ['Liaukovich Aliaksandr'] |                  | ['levkovichsanya89@gmail.com']                   | [Row(ip='46.53.183.77')]    | [Row(title='123RF', link='https://www.123rf.com/', login='levkovichsanya89@gmail.com', password_hash='21ef102e369ae46588d5f4b4ffb3563c')]                   |
| ['Porin Victor']          |                  | ['porin00@inbox.ru']                             | [Row(ip='176.60.128.186')]  | [Row(title='123RF', link='https://www.123rf.com/', login='porin00@inbox.ru', password_hash='21f8d1c5e116ca78e1057e43cc58eac5')]                             |
| ['Smirnov Sergei']        |                  | ['bymer.8990@mail.ru']                           | [Row(ip='212.20.7.184')]    | [Row(title='123RF', link='https://www.123rf.com/', login='bymer.8990@mail.ru', password_hash='8098f18346da5ce17141e15081427146')]                           |
| ['Vershin Foper']         |                  | ['foperv@bk.ru']                                 | [Row(ip='176.60.132.64')]   | [Row(title='123RF', link='https://www.123rf.com/', login='foperv@bk.ru', password_hash='df0b347f756bddbcc360de83d1469460')]                                 |
| ['Volchovich Ihar']       |                  | ['svytik2017v@mail.ru']                          | [Row(ip='172.68.244.128')]  | [Row(title='123RF', link='https://www.123rf.com/', login='svytik2017v@mail.ru', password_hash='88ca80df2d72dbebcef83a756c323da1')]                          |
| ['Boone Troy']            |                  | ['murrayonstent@cheapmailhosting.pw']            | [Row(ip='72.234.5.161')]    | [Row(title='123RF', link='https://www.123rf.com/', login='murrayonstent@cheapmailhosting.pw', password_hash='c2c7419dfa29691e64cc691a5ef9df6d')]            |
| ['Lee Krystal']           |                  | ['winifredsx16@bk.ru']                           | [Row(ip='190.167.126.103')] | [Row(title='123RF', link='https://www.123rf.com/', login='winifredsx16@bk.ru', password_hash='dd073b5e6c684810dd35db0a9e63832d')]                           |
| ['Ropov Dima']            |                  | ['drop.o@bk.ru']                                 | [Row(ip='176.60.132.199')]  | [Row(title='123RF', link='https://www.123rf.com/', login='drop.o@bk.ru', password_hash='4ee8515cd1a36491f8884d65fe741f06')]                                 |
| ['Gat Natali']            |                  | ['vipntl81@gmail.com']                           | [Row(ip='194.158.205.190')] | [Row(title='123RF', link='https://www.123rf.com/', login='vipntl81@gmail.com', password_hash='54da9fb516a0263f240e553b77c090e8')]                           |
| ['Huey Bsf']              |                  | ['m.a.i.hongphongdongdahn12345678.90@gmail.com'] | [Row(ip='27.67.21.113')]    | [Row(title='123RF', link='https://www.123rf.com/', login='m.a.i.hongphongdongdahn12345678.90@gmail.com', password_hash='a95aa44766a8e63c0db905f04d549ab7')] |
| ['Husy Bsg']              |                  | ['x.aqua.ngminhkienxuong1234567.890@gmail.com']  | [Row(ip='27.67.186.229')]   | [Row(title='123RF', link='https://www.123rf.com/', login='X.aqua.ngminhkienxuong1234567.890@gmail.com', password_hash='7dbef66534209feb51b3ef1b1d4b2f3a')]  |
| ['Hvfy Guvf']             |                  | ['linhduonglanngo.cba001234567890@gmail.com']    | [Row(ip='27.67.142.46')]    | [Row(title='123RF', link='https://www.123rf.com/', login='linhduonglanngo.cba001234567890@gmail.com', password_hash='f540515ced6e9d6b09b1a9e073214bb4')]    |
| ['Strijak Tamara']        |                  | ['tamroviya@gmail.com']                          | [Row(ip='172.68.244.152')]  | [Row(title='123RF', link='https://www.123rf.com/', login='tamroviya@gmail.com', password_hash='e7f79739c1f5bc285f7962f40deefd82')]                          |
| ['Ugh Ty']                |                  | ['c.o.ngtymaysonghong00123456789.0@gmail.com']   | [Row(ip='27.67.187.89')]    | [Row(title='123RF', link='https://www.123rf.com/', login='c.o.ngtymaysonghong00123456789.0@gmail.com', password_hash='af0d45f5272d3a55498d18f8a0903fc4')]   |
| ['Aleinikau Yury']        | ['375257944551'] | ['krishnalila03@gmail.com']                      | [Row(ip='172.68.10.36')]    | [Row(title='123RF', link='https://www.123rf.com/', login='krishnalila03@gmail.com', password_hash='ab27849af85db26d0fd79f8da0f72af8')]                      |
| ['Brezhnev Petja']        |                  | ['petechka_brezhnev@mail.ru']                    | [Row(ip='176.60.128.119')]  | [Row(title='123RF', link='https://www.123rf.com/', login='petechka_brezhnev@mail.ru', password_hash='5de8eccd5c47ce512d9fa39f6a28dae5')]                    |
```