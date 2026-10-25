# Parsetron results

## About row data

> - File path: users_ru.csv
> - Total rows: 9833

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
|   regid | email                        | password                         | first_name   | last_name   | mobile       | country   | ipadd           |
|--------:|:-----------------------------|:---------------------------------|:-------------|:------------|:-------------|:----------|:----------------|
|   98806 | JoannLAllen@teleworm.us      | 4rt345 43                        | Joann        | Allen       | <blank>      | russia    | 162.158.90.116  |
|   99100 | mail@andreyber.ru            | 802ffd3e5c5cd2d027b8032476fa5b73 | Andrey       | Ber         | <blank>      | russia    | 172.68.182.6    |
|   99137 | irinajanina98@gmail.com      | e54f4aaf2fb578678a9c97a3cf345e5d | Irina        | Janina      | <blank>      | russia    | 172.68.10.126   |
|   99142 | steell-92@mail.ru            | e820bbb7a82d890d20156645ba84ae0f | Kirill       | Silin       | <blank>      | russia    | 172.68.246.148  |
|   99143 | udolgopol@gmail.com          | 5ab3300000b59b9bb444fc68887386f9 | Юрий         | Долгополов  | <blank>      | russia    | 162.158.111.189 |
|   99255 | gvgvgvg1978@gmail.com        | d48f6956c56bab8acd710b3896e2283f | andrey       | derkach     | <blank>      | russia    | 172.68.182.192  |
|   99353 | sahanovschi08@gmail.com      | eeee7338d5ea513bbdd91172a2aca0e5 | Andrei       | Sahanovschi | <blank>      | russia    | 172.68.245.117  |
|   99596 | efa2962@gmail.com            | d16c82717f5e95703bd52cb330ee392f | Sergey       | Tokarev     | <blank>      | russia    | 162.158.182.180 |
|   99845 | aleksej_belikov@mail.ru      | 355251d7aa4a8f91b71cecaa6c3030fc | aleksei      | belikov     | <blank>      | russia    | 172.68.238.162  |
|   99847 | zhuzhik.bee@gmail.com        | a0f85a7f0164cbb29fdb46a72517dfac | Yulia        | Kukhareva   | <blank>      | russia    | 162.158.92.78   |
|   99928 | mycsmru@gmail.com            | 1b248b9741f8387291981025e75ef61c | Alexsander   | Bykov       | <blank>      | russia    | 172.68.182.42   |
|   99954 | stepanov_oleg@list.ru        | 50a7bacfd32695eff3c25c69159c8bca | oleg         | stepanov    | <blank>      | russia    | 172.68.182.66   |
|  100042 | malyr2014@gmail.com          | ab6fe46572f736a763e2149b839b99f9 | Aleksandr    | Shepelev    | <blank>      | russia    | 162.158.183.97  |
|  100167 | expertmen75@gmail.com        | d2cfe372925e1c6e5bf132c1ba1f5795 | Dima         | Bandurin    | <blank>      | russia    | 172.68.11.169   |
|  100202 | kassavp1@gmail.com           | 37e03c36d5f2f804a90c502d63a0c1e2 | Alexander    | Evdoshenko  | <blank>      | russia    | 162.158.183.61  |
|  100254 | danilovevgeniy2016@gmail.com | b58c75bb23ae3a45446de5ba12c206fe | Евгений      | Данилов     | <blank>      | russia    | 172.68.10.186   |
|  100267 | fidarov67@mail.ru            | 3a9cee7ccf8a672cc71c55dbffd40a5d | Артур        | Фидаров     | <blank>      | russia    | 162.158.183.79  |
|  100325 | noviko1981@gmail.com         | 40ece2fbc88c61e86a5cdc102abab1d0 | Valery       | Novikov     | +79899550511 | russia    | 172.68.182.108  |
|  100384 | gud-tug@yandex.ru            | dcbfae0bad6d111112f38c1de88af6fb | Viktor       | Koshkin     | <blank>      | russia    | 172.68.11.103   |
|  100448 | sviridovgenadij88@gmail.com  | b0526b6fa5797f6286c17c08d72d7029 | genadij      | sviridov    | <blank>      | russia    | 172.68.182.210  |
```


## About final data

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
| Phones | 0.92% |
| Ips | 99.95% |
| Accounts | 100.00% |



### Data sample
```
| names                    | emails                           | phones          | ips                         | accounts                                                                                                                   |
|:-------------------------|:---------------------------------|:----------------|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| ['Allen Joann']          | ['joannlallen@teleworm.us']      |                 | [Row(ip='162.158.90.116')]  | [Row(title='Trident Crypto Fund', login='joannlallen@teleworm.us', password_hash='4rt345 43')]                             |
| ['Ber Andrey']           | ['mail@andreyber.ru']            |                 | [Row(ip='172.68.182.6')]    | [Row(title='Trident Crypto Fund', login='mail@andreyber.ru', password_hash='802ffd3e5c5cd2d027b8032476fa5b73')]            |
| ['Janina Irina']         | ['irinajanina98@gmail.com']      |                 | [Row(ip='172.68.10.126')]   | [Row(title='Trident Crypto Fund', login='irinajanina98@gmail.com', password_hash='e54f4aaf2fb578678a9c97a3cf345e5d')]      |
| ['Silin Kirill']         | ['steell-92@mail.ru']            |                 | [Row(ip='172.68.246.148')]  | [Row(title='Trident Crypto Fund', login='steell-92@mail.ru', password_hash='e820bbb7a82d890d20156645ba84ae0f')]            |
| ['Долгополов Юрий']      | ['udolgopol@gmail.com']          |                 | [Row(ip='162.158.111.189')] | [Row(title='Trident Crypto Fund', login='udolgopol@gmail.com', password_hash='5ab3300000b59b9bb444fc68887386f9')]          |
| ['Derkach Andrey']       | ['gvgvgvg1978@gmail.com']        |                 | [Row(ip='172.68.182.192')]  | [Row(title='Trident Crypto Fund', login='gvgvgvg1978@gmail.com', password_hash='d48f6956c56bab8acd710b3896e2283f')]        |
| ['Sahanovschi Andrei']   | ['sahanovschi08@gmail.com']      |                 | [Row(ip='172.68.245.117')]  | [Row(title='Trident Crypto Fund', login='sahanovschi08@gmail.com', password_hash='eeee7338d5ea513bbdd91172a2aca0e5')]      |
| ['Tokarev Sergey']       | ['efa2962@gmail.com']            |                 | [Row(ip='162.158.182.180')] | [Row(title='Trident Crypto Fund', login='efa2962@gmail.com', password_hash='d16c82717f5e95703bd52cb330ee392f')]            |
| ['Belikov Aleksei']      | ['aleksej_belikov@mail.ru']      |                 | [Row(ip='172.68.238.162')]  | [Row(title='Trident Crypto Fund', login='aleksej_belikov@mail.ru', password_hash='355251d7aa4a8f91b71cecaa6c3030fc')]      |
| ['Kukhareva Yulia']      | ['zhuzhik.bee@gmail.com']        |                 | [Row(ip='162.158.92.78')]   | [Row(title='Trident Crypto Fund', login='zhuzhik.bee@gmail.com', password_hash='a0f85a7f0164cbb29fdb46a72517dfac')]        |
| ['Bykov Alexsander']     | ['mycsmru@gmail.com']            |                 | [Row(ip='172.68.182.42')]   | [Row(title='Trident Crypto Fund', login='mycsmru@gmail.com', password_hash='1b248b9741f8387291981025e75ef61c')]            |
| ['Stepanov Oleg']        | ['stepanov_oleg@list.ru']        |                 | [Row(ip='172.68.182.66')]   | [Row(title='Trident Crypto Fund', login='stepanov_oleg@list.ru', password_hash='50a7bacfd32695eff3c25c69159c8bca')]        |
| ['Shepelev Aleksandr']   | ['malyr2014@gmail.com']          |                 | [Row(ip='162.158.183.97')]  | [Row(title='Trident Crypto Fund', login='malyr2014@gmail.com', password_hash='ab6fe46572f736a763e2149b839b99f9')]          |
| ['Bandurin Dima']        | ['expertmen75@gmail.com']        |                 | [Row(ip='172.68.11.169')]   | [Row(title='Trident Crypto Fund', login='expertmen75@gmail.com', password_hash='d2cfe372925e1c6e5bf132c1ba1f5795')]        |
| ['Evdoshenko Alexander'] | ['kassavp1@gmail.com']           |                 | [Row(ip='162.158.183.61')]  | [Row(title='Trident Crypto Fund', login='kassavp1@gmail.com', password_hash='37e03c36d5f2f804a90c502d63a0c1e2')]           |
| ['Данилов Евгений']      | ['danilovevgeniy2016@gmail.com'] |                 | [Row(ip='172.68.10.186')]   | [Row(title='Trident Crypto Fund', login='danilovevgeniy2016@gmail.com', password_hash='b58c75bb23ae3a45446de5ba12c206fe')] |
| ['Фидаров Артур']        | ['fidarov67@mail.ru']            |                 | [Row(ip='162.158.183.79')]  | [Row(title='Trident Crypto Fund', login='fidarov67@mail.ru', password_hash='3a9cee7ccf8a672cc71c55dbffd40a5d')]            |
| ['Novikov Valery']       | ['noviko1981@gmail.com']         | ['79899550511'] | [Row(ip='172.68.182.108')]  | [Row(title='Trident Crypto Fund', login='noviko1981@gmail.com', password_hash='40ece2fbc88c61e86a5cdc102abab1d0')]         |
| ['Koshkin Viktor']       | ['gud-tug@yandex.ru']            |                 | [Row(ip='172.68.11.103')]   | [Row(title='Trident Crypto Fund', login='gud-tug@yandex.ru', password_hash='dcbfae0bad6d111112f38c1de88af6fb')]            |
| ['Sviridov Genadij']     | ['sviridovgenadij88@gmail.com']  |                 | [Row(ip='172.68.182.210')]  | [Row(title='Trident Crypto Fund', login='sviridovgenadij88@gmail.com', password_hash='b0526b6fa5797f6286c17c08d72d7029')]  |
```