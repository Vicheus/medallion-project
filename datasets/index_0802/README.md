# Parsetron results

## About row data

> - Code name: index_0802
> - File path: vipavenue-users.csv
> - Total rows: 365406

### Schema
```
root
 |-- id: string (nullable = true)
 |-- name: string (nullable = true)
 |-- surname: string (nullable = true)
 |-- phone_number: string (nullable = true)
 |-- email: string (nullable = true)
 |-- user_city: string (nullable = true)
 |-- birthday: string (nullable = true)
 |-- bonus_points_balance: string (nullable = true)
 |-- loyalty_card: string (nullable = true)
 |-- device_uuid: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- clothes_size: string (nullable = true)
 |-- clothes_size_id: string (nullable = true)
 |-- shoes_size: string (nullable = true)
 |-- shoes_size_id: string (nullable = true)

```

### Data sample
```
|     id | name     | surname     |   phone_number | email                      | user_city       | birthday   |   bonus_points_balance | loyalty_card   | device_uuid                          | gender   | clothes_size   | clothes_size_id   | shoes_size   | shoes_size_id        |
|-------:|:---------|:------------|---------------:|:---------------------------|:----------------|:-----------|-----------------------:|:---------------|:-------------------------------------|:---------|:---------------|:------------------|:-------------|:---------------------|
|  14193 | ярослава | NULL        |    79092174282 | zuikinaj@mail.ru           | Москва          | NULL       |                   1394 | default        | f3f4ce81-18d9-4545-92b9-470304437f4d | f        | 42             | 643028            | 37,38        | 643040,643042        |
|  19615 | Ярослава | Врубель     |    79128008820 | NULL                       | Екатеринбург    | NULL       |                   1000 | default        | 26db4974-b20d-4ece-a0a6-5a8e1786f41e | f        | 50             | 643032            | NULL         | NULL                 |
|  59076 | Ярослава | тимофеева   |    79115217095 | NULL                       | Москва          | 1968-01-17 |                   1379 | default        | 0000d074-f925-4fbe-aa3a-bae17d6e0a96 | f        | NULL           | NULL              | 36,37        | 643038,643040        |
|  80678 | Ярослава | Старцева    |    79126897578 | asika6016@yandex.ru        | Екатеринбург    | 1994-12-22 |                   1852 | default        | a7d7cbb4-423f-4fc6-a0c0-0a72f95e8b09 | NULL     | NULL           | NULL              | 37.5         | 643041               |
| 117754 | Ярослава | Лобанова    |    79854769217 | NULL                       | Москва          | 1993-06-29 |                   1780 | default        | dbcc496d-9e78-47a0-bf59-4900b594014f | f        | NULL           | NULL              | NULL         | NULL                 |
| 141703 | Ярослава | NULL        |    79184840411 | NULL                       | Санкт-Петербург | 2000-12-06 |                   1332 | default        | cd16d67c-2245-4032-80e4-4d8b7d36e207 | f        | 36,38          | 978022,978204     | NULL         | NULL                 |
| 165087 | ярослава | карпенко    |    79177232384 | zhmelevayara@gmail.com     | Краснодар       | NULL       |                  30662 | silver         | be86c5a0-f0d2-4d80-b1ad-7123c50e3441 | f        | 44,46          | 643029,643030     | 36,37,38     | 643038,643040,643042 |
| 172073 | Ярослава | NULL        |    79190352172 | sokolova.yaroslava@mail.ru | Москва          | 1998-04-19 |                   1792 | default        | 092d2cf5-faaa-4f53-8f80-bf780b3c1fe7 | f        | NULL           | NULL              | NULL         | NULL                 |
| 187770 | Ярослава | NULL        |    79109777827 | yaroslava_69@list.ru       | Москва          | NULL       |                   1000 | default        | cc694390-f0c7-4d2e-a378-4d73b9abbe06 | NULL     | 46,48          | 643030,977766     | 36,37        | 643038,643040        |
| 198942 | Ярослава | NULL        |    79175179106 | NULL                       | Москва          | NULL       |                   1826 | default        | d74f4524-d202-46c7-8a85-cb6755fa0248 | f        | 44,46          | 643029,643030     | 36.5,37.5    | 643039,643041        |
| 198989 | Ярослава | колесникова |    79046285327 | yaroslava_vlad@mail.ru     | Москва          | NULL       |                      0 | default        | b27ae5fc-47b6-40d4-a282-33c4c3a2b76b | f        | 44             | 643029            | 38           | 643042               |
| 202064 | ярослава | NULL        |    79286251545 | sl.semenchukova@mail.ru    | Ростов-на-Дону  | 1997-06-07 |                   9938 | bronze         | 5fbf7b9c-b30a-4b16-868f-ffee8bde5a70 | f        | NULL           | NULL              | NULL         | NULL                 |
| 213323 | Ярослава | Панкратова  |    79639998586 | NULL                       | Москва          | NULL       |                   1000 | default        | b118e5ba-4894-4b38-abb2-1b1180218a75 | f        | 54,56          | 643251,643069     | NULL         | NULL                 |
| 218005 | Ярослава | бас         |    79600346327 | yasya-kazan2@mail.ru       | Казань          | 1971-03-09 |                   2774 | default        | ff455d97-dd1f-436a-94e3-d26f0fec6654 | NULL     | NULL           | NULL              | NULL         | NULL                 |
| 220554 | Ярослава | NULL        |    79995814478 | NULL                       | Челябинск       | 1991-09-02 |                  12039 | bronze         | 2b6ec91a-d588-4526-94a1-142022cdee75 | NULL     | 38             | 978204            | NULL         | NULL                 |
| 225690 | ярослава | NULL        |    79035457088 | NULL                       | Москва          | 1985-07-08 |                   2331 | default        | d2ffd55b-f7a9-4188-8d3a-7c09e45472c2 | NULL     | 40             | 643027            | 38,39        | 643042,643044        |
| 227618 | Ярослава | NULL        |    79213254756 | NULL                       | Санкт-Петербург | NULL       |                   1415 | default        | c0129788-c9b5-4721-bdee-c5d63f254182 | NULL     | 42,44          | 643028,643029     | 38,39        | 643042,643044        |
| 279025 | Ярослава | NULL        |    79265776915 | NULL                       | Москва          | NULL       |                   2021 | default        | b3e89ee7-48a7-40b3-b01f-b9e0dd64069c | NULL     | NULL           | NULL              | NULL         | NULL                 |
| 296684 | Ярослава | NULL        |    79253609698 | NULL                       | Москва          | NULL       |                   2723 | default        | e04e7f89-856f-47ae-b8d4-98602d7444b0 | NULL     | NULL           | NULL              | NULL         | NULL                 |
| 311003 | Ярослава | NULL        |    79119459407 | NULL                       | Санкт-Петербург | NULL       |                   2231 | default        | e9582284-8637-42f8-adc1-15806436ccd7 | NULL     | NULL           | NULL              | NULL         | NULL                 |
```


## About final data
> - Total rows: 145388

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Sex | 70.06% |
| Birth_date | 44.34% |
| Phones | 99.94% |
| Emails | 32.75% |
| Address | 99.97% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                   |   sex | birth_date   | phones          | emails                   | address             | source_entity_id                                         |
|:------------------------|------:|:-------------|:----------------|:-------------------------|:--------------------|:---------------------------------------------------------|
| ['Adyakin Aleksandr']   |     1 | 26.09.1961   | ['79376543701'] |                          | ['Самара']          | cdc9994a2f55e68437ad451c5ba56e15624af75cf86038bc24ac7f6e |
| ['Akbasheva Gulnara']   |     0 | 10.01.1969   | ['79177990075'] |                          | ['Уфа']             | 447062315315d939e78465d0fba7e429cf6da0c6e1a0d9dd1ffb3fb7 |
| ['Akimochkina Elena']   |     0 |              | ['79237021011'] |                          | ['Новосибирск']     | d4f8862445a57ea2bdfa8d29f3d7dc833a1c096fc48e7e260b965475 |
| ['Aksenova Ekaterina']  |     0 |              | ['79134554604'] | ['aks_kat@mail.ru']      | ['Новосибирск']     | 8a49013007719646c9cde41088ac94e9c072fb1aaef47f106bf0bda6 |
| ['Asdf']                |   nan | 01.01.1990   | ['79722936758'] | ['user117266@yandex.ru'] | ['Москва']          | 01942183462116484383dee508b5d5b53236ae8111a8bf56c961f94e |
| ['Babenko Ekaterina']   |   nan | 08.04.1979   | ['79064149069'] |                          | ['Ростов-на-Дону']  | 58a845343827f5c9ce86b6ddd362aa254fca455a9146c9d95b9eeb78 |
| ['Baykov Aleksey']      |     1 | 12.03.1956   | ['79212165066'] |                          | ['Санкт-Петербург'] | 87adae9ccff07a34b19008da9f1a5da8c94ef3e1f721a4fd5a96fadd |
| ['Bazilevich Vladimir'] |     1 | 13.05.1958   | ['79853839307'] |                          | ['Москва']          | 06613c3912840e4387c94ce71814e3efdba889598f26319f74d6bd69 |
| ['Bogdanova Marina']    |   nan |              | ['79045551818'] |                          | ['Санкт-Петербург'] | 93e76c3df3ba91e306c2d7cf7d99aa1beb0844fdcb5539684fea09f7 |
| ['Boytsov Evgeniy']     |     1 |              | ['79267264674'] |                          | ['Москва']          | d6c62444483d34be347096b1c1948d6321beea73ffc6925bf846209f |
| ['Chernovolov Mikhail'] |     1 | 22.08.1981   | ['79219764234'] |                          | ['Санкт-Петербург'] | e08c440b89ba16a7dd7326542bdaf665b125d0c3611690308705c184 |
| ['Churilova Marina']    |     0 | 21.09.1969   | ['79857842624'] |                          | ['Москва']          | 08aa203ad2ea08f34ac82ce0789eded46a40a18318e83005a721cf99 |
| ['Danilov Vyacheslav']  |   nan |              | ['79529183277'] |                          | ['Новосибирск']     | 5ea41bc5af62c936a58a8d062ca8de5c8a8deeb7dc80ac8cd4e6f339 |
| ['Dikarev Evgeniy']     |   nan |              | ['79267394217'] | ['dik.e.s@mail.ru']      | ['Москва']          | f20adef424d502ec66236a06a62c4f7585f2cbb1d78d32f2e191d900 |
| ['Dzoblaev Alan']       |   nan | 02.08.1968   | ['79188245678'] | ['letka555@mail.ru']     | ['Сочи']            | 0182dc73469485c34f69f09903d4b1158fb313a8ceb3deeedae03246 |
| ['Gasanov Ramiz']       |     1 | 26.12.1994   | ['79853182625'] |                          | ['Москва']          | 4ee38950a08df8ace36347bc46ceed422715a612fd5980752bb3d699 |
| ['Golubets Oleg']       |   nan |              | ['79183715082'] |                          | ['Краснодар']       | f1c58516b116ac569de3ea2817e71b01ad2167bf6b56ff5726bba5fd |
| ['Gonova Elena']        |     0 |              | ['79108781244'] |                          | ['Нижний Новгород'] | d48320ba89ade7293c31700b900d68e45b9ea90fac1f43084eda491a |
| ['Gordova Olesya']      |     0 | 10.12.1991   | ['79897162645'] | ['g0rd0va@yandex.ru']    | ['Ростов-на-Дону']  | a1b1355191109f251735d787731f7d22a0ee5848bc54bd7acc78670f |
| ['Grigoryan Artur']     |   nan |              | ['79217567604'] |                          | ['Санкт-Петербург'] | 98161aa0562ec66ecd957fb406cdce08d1f8748ca11b997f4a21adb7 |
```