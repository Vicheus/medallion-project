# Parsetron results

## About row data

> - File path: aliexpress_ru.csv
> - Total rows: 192668

### Schema
```
root
 |-- billFirstName: string (nullable = true)
 |-- billLastName: string (nullable = true)
 |-- ordersUserId: string (nullable = true)
 |-- orderUserEmail: string (nullable = true)
 |-- shipCity: string (nullable = true)
 |-- shipCountry: string (nullable = true)
 |-- shipFirstName: string (nullable = true)
 |-- shipLastName: string (nullable = true)
 |-- shipPhone: string (nullable = true)
 |-- shippingMethodOrig: string (nullable = true)
 |-- shipState: string (nullable = true)
 |-- shipStreet1: string (nullable = true)
 |-- shipStreet2: string (nullable = true)
 |-- shipZip: string (nullable = true)
 |-- trackNumber: string (nullable = true)

```

### Data sample
```
| billFirstName   | billLastName          | ordersUserId          | orderUserEmail             | shipCity              | shipCountry   | shipFirstName   | shipLastName          |   shipPhone | shippingMethodOrig                    | shipState                          | shipStreet1                                         | shipStreet2                             |   shipZip | trackNumber          |
|:----------------|:----------------------|:----------------------|:---------------------------|:----------------------|:--------------|:----------------|:----------------------|------------:|:--------------------------------------|:-----------------------------------|:----------------------------------------------------|:----------------------------------------|----------:|:---------------------|
| Svetlana        | Zamaleeva             | Svetlana Zamaleeva    | support@suntekstore.ca     | Kachkanar             | RU            | Svetlana        | Zamaleeva             | 79045449521 | Standard                              | Sverdlovskaya obl                  | mkr 4-y, d 50, kv 49                                |                                         |    624351 | SFC1WCFF019091837060 |
| Гусаров         | Сергей Викторович     | Sergey Gusarov        | aliexpress@szecommerce.com | Moscow                | RU            | ГуcaPoв         | CePгeй                |  9030365176 | AliExpress Standard Shipping          | Moscow                             | BиктoPoвич , Coфьи Кoвaлeвcкoй                      | 10 кopп.1 кв44                          |    127411 | SFC2WCFF019091837833 |
| Петров          | Антон Алексеевич      | ANTON PETROV          | aliexpress@szecommerce.com | Peno                  | RU            | ПeтPoв          | Aнтoн Aлeкceeвич      |  9109340754 | AliExpress Saver Shipping             | Tverskaya oblast                   | Пeнo                                                | улицa Poдинa, д. 15, кв. 2              |    172770 | SFC2WCFF019091839183 |
| Korolev         | Dmitriy Valerievich   | Dima k                | aliexpress@szecommerce.com | Ulyanovsk             | RU            | Korolev         | Dmitriy Valerievich   |  9020088664 | China Post Ordinary Small Packet Plus | Ulyanovskaya oblast                | prospect Aviastroitelei  dom 7                      | kv 177                                  |    432064 | SFC2WCFF019092020359 |
| Dobrovolskaya   | Marina Vasilievna     | Natalia Dobrovolskaya | aliexpress@szecommerce.com | Saranskoe             | RU            | Dobrovolskaya   | Marina Vasilievna     |  9052451311 | AliExpress Standard Shipping          | Kaliningradskaya oblast            | Novaya 3-1                                          |                                         |    238640 | SFC2WCFF019091839192 |
| Anna            | Novitskaya            | Anna Novitskaya       | support@suntekstore.ca     | poselok Borisovka     | RU            | Anna            | Novitskaya            | 79202030577 | Standard                              | Belgorodskaya obl, Borisovskiy r-n | per Degtyareva, d 3                                 |                                         |    309340 | SFC1WCFF019091839566 |
| Inessa          | Impolitova            | Inessa Impolitova     | support@suntekstore.ca     | Krasnoyarsk           | RU            | Inessa          | Impolitova            | 79131870828 | Standard                              | Krasnoyarskiy kray                 | Yaryginskaya nab, d. 21, kv. 138                    |                                         |    660012 | SFC1WCFF019091839863 |
| Aleksey         | Akatev                | Aleksey Akatev        | support@suntekstore.ca     | Dedovsk               | RU            | Aleksey         | Akatev                | 79267476074 | Standard                              | Moskovskaya obl, Istrinskiy r-n    | ul Kosmonavta Komarova, d. 1, kv. 58                |                                         |    143530 | SFC1WCFF019091839809 |
| Smirnova        | Yulia Aleksandrovna   | Julia Smirnova        | aliexpress@szecommerce.com | Moscow                | RU            | Smirnova        | Yulia Aleksandrovna   |  9165152647 | AliExpress Saver Shipping             | Moscow                             | Litvina-Sedogo St 1/11,Central Administrative Okrug | 24                                      |    123317 | SFC2WCFF01909194294  |
| Ostrogorsky     | Alexey Ivanovitch     | aleksey ostrogorsky   | aliexpress@szecommerce.com | Volgograd             | RU            | Ostrogorsky     | Alexey Ivanovitch     | 89275214458 | AliExpress Standard Shipping          | Volgogradskaya oblast              | Marshal Zhukov Avenue 127                           | apartment 37                            |    400048 | SFC2WCFF019091850778 |
| Glukhov         | Vladimir Viktorovich  | Vladimir Glukhov      | aliexpress@szecommerce.com | Moscow                | RU            | Glukhov         | Vladimir Viktorovich  |  9262111955 | AliExpress Saver Shipping             | Moscow                             | Altufevskoe highway, 89-314                         |                                         |    127576 | SFC2WCFF019091840649 |
| Sergey          | Surkov Evgen'evich    | Sergey Surkov         | aliexpress@szecommerce.com | Nizhny Novgorod       | RU            | Sergey          | Surkov Evgen'evich    |  9290452107 | AliExpress Saver Shipping             | Nizhegorodskaya oblast             | Ulitsa Mel'nikova-Pecherskogo                       | 1-18                                    |    603057 | SFC2WCFF019091841811 |
| Gantsen         | Viktoria Vladimirovna | Viktoriya Gantsen     | aliexpress@szecommerce.com | Magnitogorsk          | RU            | Gantsen         | Viktoria Vladimirovna |  9630970400 | AliExpress Saver Shipping             | Chelyabinskaya oblast              | Eniseiskaya                                         | 33                                      |    455000 | SFC2WCFF019091841783 |
| Алексей         | Панкратов             | Aleksey Pankratov     | aliexpress@szecommerce.com | Podolsk               | RU            | Aлeкceй         | ПaнкPaтoв             |  9262030022 | AliExpress Standard Shipping          | Moskovskaya oblast                 | Климoвcк                                            | пpocпeкт 50-лeтия Oктябpя, д.20, кв.124 |    142181 | SFC2WCFF019091841810 |
| Anastasiya      | Shakhova              | Anastasiya Shakhova   | support@suntekstore.ca     | Kaluga                | RU            | Anastasiya      | Shakhova              | 79641423216 | Standard                              | Kaluzhskaya obl                    | ul Guryanova, d. 18, korp. 2, kv. 179               |                                         |    248029 | SFC1WCFF019091842204 |
| Igor            | Kalevatov             | Igor Kalevatov        | support@suntekstore.ca     | Kursk                 | RU            | Igor            | Kalevatov             | 79611903011 | Standard                              | Kurskaya obl                       | ul Pavlunovskogo, d. 108                            |                                         |    305040 | SFC1WCFF019091842221 |
| Olga            | Utina                 | Olga Utina            | support@suntekstore.ca     | Moskva                | RU            | Olga            | Utina                 | 79169522533 | Standard                              | Moskva                             | Shmitovskiy proezd, d. 44, kv. 21                   |                                         |    123290 | SFC1WCFF019091842336 |
| Ekaterina       | Kozyukova             | Ekaterina Kozyukova   | support@suntekstore.ca     | selo Verkh-Rozhdestvo | RU            | Ekaterina       | Kozyukova             | 79223170384 | Standard                              | Permskiy kray, Chastinskiy r-n     | ul Kabakova gora, d. 12, kv. 2                      |                                         |    617183 | SFC1WCFF019091842463 |
| Павел           | Касьянов              | Павел Касьянов        | support@suntekstore.ca     | Bлaдивocтoк           | RU            | Пaвeл           | Кacьянoв              | 79149703323 | Standard                              | Приморский край                    | улицa Aдмиpaлa Cмиpнoвa, 18 кв. 27                  |                                         |    690911 | SFC2WCFF019091842549 |
| Татьяна         | Полонская             | Татьяна Полонская     | support@suntekstore.ca     | Bronnezhskaya Oblast  | RU            | Taтьянa         | Пoлoнcкaя             | 89009625927 | Standard                              | .                                  | New Home.  Central street 7 sq. 33                  |                                         |    396310 | SFC2WCFF019091851642 |
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
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 49.81% |
| Emails | 50.19% |
| Address | 49.81% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                               | phones   | emails                         | address   | raw_metadata                                                                                               |
|:------------------------------------|:---------|:-------------------------------|:----------|:-----------------------------------------------------------------------------------------------------------|
| ['Zamaleeva Svetlana']              |          | ['support@suntekstore.ca']     |           | ['{"shippingMethodOrig": "Standard", "trackNumber": "SFC1WCFF019091837060"}']                              |
| ['Сергей Викторович Гусаров']       |          | ['aliexpress@szecommerce.com'] |           | ['{"shippingMethodOrig": "AliExpress Standard Shipping", "trackNumber": "SFC2WCFF019091837833"}']          |
| ['Антон Алексеевич Петров']         |          | ['aliexpress@szecommerce.com'] |           | ['{"shippingMethodOrig": "AliExpress\xa0Saver\xa0Shipping", "trackNumber": "SFC2WCFF019091839183"}']       |
| ['Dmitriy Valerievich Korolev']     |          | ['aliexpress@szecommerce.com'] |           | ['{"shippingMethodOrig": "China Post Ordinary Small Packet Plus", "trackNumber": "SFC2WCFF019092020359"}'] |
| ['Marina Vasilievna Dobrovolskaya'] |          | ['aliexpress@szecommerce.com'] |           | ['{"shippingMethodOrig": "AliExpress Standard Shipping", "trackNumber": "SFC2WCFF019091839192"}']          |
| ['Novitskaya Anna']                 |          | ['support@suntekstore.ca']     |           | ['{"shippingMethodOrig": "Standard", "trackNumber": "SFC1WCFF019091839566"}']                              |
| ['Impolitova Inessa']               |          | ['support@suntekstore.ca']     |           | ['{"shippingMethodOrig": "Standard", "trackNumber": "SFC1WCFF019091839863"}']                              |
| ['Akatev Aleksey']                  |          | ['support@suntekstore.ca']     |           | ['{"shippingMethodOrig": "Standard", "trackNumber": "SFC1WCFF019091839809"}']                              |
| ['Yulia Aleksandrovna Smirnova']    |          | ['aliexpress@szecommerce.com'] |           | ['{"shippingMethodOrig": "AliExpress\xa0Saver\xa0Shipping", "trackNumber": "SFC2WCFF01909194294"}']        |
| ['Alexey Ivanovitch Ostrogorsky']   |          | ['aliexpress@szecommerce.com'] |           | ['{"shippingMethodOrig": "AliExpress Standard Shipping", "trackNumber": "SFC2WCFF019091850778"}']          |
| ['Vladimir Viktorovich Glukhov']    |          | ['aliexpress@szecommerce.com'] |           | ['{"shippingMethodOrig": "AliExpress\xa0Saver\xa0Shipping", "trackNumber": "SFC2WCFF019091840649"}']       |
| ["Surkov Evgen'Evich Sergey"]       |          | ['aliexpress@szecommerce.com'] |           | ['{"shippingMethodOrig": "AliExpress\xa0Saver\xa0Shipping", "trackNumber": "SFC2WCFF019091841811"}']       |
| ['Viktoria Vladimirovna Gantsen']   |          | ['aliexpress@szecommerce.com'] |           | ['{"shippingMethodOrig": "AliExpress\xa0Saver\xa0Shipping", "trackNumber": "SFC2WCFF019091841783"}']       |
| ['Панкратов Алексей']               |          | ['aliexpress@szecommerce.com'] |           | ['{"shippingMethodOrig": "AliExpress Standard Shipping", "trackNumber": "SFC2WCFF019091841810"}']          |
| ['Shakhova Anastasiya']             |          | ['support@suntekstore.ca']     |           | ['{"shippingMethodOrig": "Standard", "trackNumber": "SFC1WCFF019091842204"}']                              |
| ['Kalevatov Igor']                  |          | ['support@suntekstore.ca']     |           | ['{"shippingMethodOrig": "Standard", "trackNumber": "SFC1WCFF019091842221"}']                              |
| ['Utina Olga']                      |          | ['support@suntekstore.ca']     |           | ['{"shippingMethodOrig": "Standard", "trackNumber": "SFC1WCFF019091842336"}']                              |
| ['Kozyukova Ekaterina']             |          | ['support@suntekstore.ca']     |           | ['{"shippingMethodOrig": "Standard", "trackNumber": "SFC1WCFF019091842463"}']                              |
| ['Касьянов Павел']                  |          | ['support@suntekstore.ca']     |           | ['{"shippingMethodOrig": "Standard", "trackNumber": "SFC2WCFF019091842549"}']                              |
| ['Полонская Татьяна']               |          | ['support@suntekstore.ca']     |           | ['{"shippingMethodOrig": "Standard", "trackNumber": "SFC2WCFF019091851642"}']                              |
```