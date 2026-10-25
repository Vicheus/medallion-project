# Parsetron results

## About row data

> - Code name: index_0350
> - File path: клиенты_sapato_ru.csv
> - Total rows: 1027782

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Телефон: long (nullable = true)
 |-- Адрес: string (nullable = true)

```

### Data sample
```
| ФИО           | Почта                   |       Телефон | Адрес                                           |
|:--------------|:------------------------|--------------:|:------------------------------------------------|
| Егор          | hiroshi@inbox.ru        | nan           | Москва                                          |
| Вася          | k.u.k.l.a08@mail.ru     | nan           | Москва                                          |
| Макс          | maksimchik.84@mail.ru   | nan           | Санкт-Петербург,                                |
| Ирина         | irinica@mail.ru         | nan           | Москва                                          |
| Элина         | kicccka@list.ru         | nan           | Москва, Полоцкая                                |
| Ника          | nika_0805@mail.ru       | nan           | Москва                                          |
| Натали        | lisa1989gr@mail.ru      | nan           | Нижний Новгород                                 |
| Марина        | bubnovich@yandex.ru     | nan           | Самара                                          |
| Евгений       | zhekasam@email.ru       |   7.92774e+10 | Самара, 16 квартал                              |
| Артемка       | yar-nihilist@yandex.ru  |   7.9807e+10  | Ярославль                                       |
| Eлена         | torpedo79@mail.ru       | nan           | Нижний Новгород                                 |
| Ящукова Дарья | fantom85.85@bk.ru       | nan           | Тюмень                                          |
| Ящук Юлия     | yul763@narod.ru         |   7.91642e+10 | Москва, Москва, Алма-Атинская, д.3 к. 2 кв. 237 |
| Ящук Татьяна  | tatyanayashuk@gmail.com | nan           | Москва                                          |
| Ящук Сергей   | serdho2009@yandex.ru    | nan           | Краснодар                                       |
| Ящук Сергей   | horror234@yandex.ru     | nan           | Москва                                          |
| Ящук Сергей   | yaschuk@list.ru         |   7.90316e+10 | Москва, Москва, Кировоградская, 12              |
| Ящук Настя    | kisa77777707@rambler.ru |   7.91186e+10 | Калининград                                     |
| Ящук Лена     | yashuke@mail.ru         | nan           | Москва                                          |
| Ящук Елена    | nastusha-11@yndex.ru    | nan           | Москва                                          |
```


## About final data
> - Total rows: 1010040

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.97% |
| Phones | 24.63% |
| Address | 97.45% |



### Data sample
```
| names                  | emails                       | phones          | address                                            |
|:-----------------------|:-----------------------------|:----------------|:---------------------------------------------------|
| ['Яшнова Анна']        | ['fujinann@mail.ru']         | ['79041913667'] | ['Ульяновск']                                      |
| ['Яценко Ирина']       | ['irysevich@mail.ru']        | ['79261877886'] | ['Москва Мичуринский пр-т Олимпийская деревня 13'] |
| ['Ярославцев Евгений'] | ['filin73.73@mail.ru']       | ['79200545424'] | ['Нижний Новгород']                                |
| ['Яркин Алексей']      | ['kettle_2001@mail.ru']      | ['79601346341'] | ['Воронеж']                                        |
| ['Яна Соколова']       | ['soyana@list.ru']           | ['79523841277'] | ['Санкт-Петербург']                                |
| ['Ямалтдинов Альберт'] | ['albertyam@yandex.ru']      | ['79026925260'] | ['Сургут Когалым ленинградская 4158']              |
| ['Яковлев Дмитрий']    | ['reklama-05@mail.ru']       | ['79119878709'] | ['Санкт-Петербург Федюнинского 3']                 |
| ['Яковлев Андрей']     | ['and1220033@yandex.ru']     | ['79042845701'] | ['Липецк']                                         |
| ['Явойш Елена']        | ['elen302@yandex.ru']        | ['79082836111'] | ['Смоленск']                                       |
| ['Ющенко Елена']       | ['yushenko73@mail.ru']       | ['79082716662'] | ['Санкт-Петербург Сысольская 7']                   |
| ['Юшков Глеб']         | ['gl-yushkov@mail.ru']       | ['79296080103'] | ['Москва красностуденческий проезд 21']            |
| ['Юрченко Роман']      | ['3dperspective@mail.ru']    | ['79060665032'] | ['Москва']                                         |
| ['Юрий']               | ['litovchenko-y@mail.ru']    | ['79162801208'] | ['Москва Короленко 9']                             |
| ['Юля Григорьева']     | ['juliya_grigoreva@mail.ru'] | ['79231693824'] | ['Барнаул']                                        |
| ['Юля']                | ['n.tzaritza2010@yandex.ru'] | ['79608404291'] | ['Тольятти']                                       |
| ['Юлия Юлия']          | ['amadeus2222@mail.ru']      | ['79067495056'] | ['Москва Носовихинское ш.']                        |
| ['Юлия Шатропова']     | ['mulya72rus@mail.ru']       | ['79220048227'] | ['Пермь']                                          |
| ['Юлия Спирина']       | ['yuse4ka_73@mail.ru']       | ['79876307319'] | ['Ульяновск']                                      |
| ['Юлия Перегудова']    | ['yulia0828@mail.ru']        | ['79132622015'] | ['Барнаул']                                        |
| ['Юлия Нанаенко']      | ['madman911@mail.ru']        | ['79515669109'] | ['Воронеж']                                        |
```