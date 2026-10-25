# Parsetron results

## About row data

> - File path: Ювелирный_магазин_Мона_2024.csv
> - Total rows: 7398

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Номер телефона: long (nullable = true)
 |-- Адрес: string (nullable = true)
 |-- Почта: string (nullable = true)

```

### Data sample
```
| ФИО        |   Номер телефона | Адрес   | Почта                           |
|:-----------|-----------------:|:--------|:--------------------------------|
| Рник Елена |              nan |         | lena-6687@mail.ru               |
| Наталья    |              nan |         | natali.ryzhaja2013@yandex.ru    |
| Кира       |              nan |         | kira7075@yandex.ru              |
| Гульнара   |              nan |         | gulhai@mail.ru                  |
| Елена      |              nan |         | lena_osheva@mail.ru             |
| Ника       |              nan |         | dom6260@yandex.ru               |
| Ольга      |              nan |         | pautina.pautinka@gmail.com      |
| Валентина  |              nan |         | zve333@yandex.ru                |
| Евгения    |              nan |         | bek_2007_07@mail.ru             |
| Светлана   |              nan |         | svetiksns@mail.ru               |
| Марина     |              nan |         | marina.popova@list.ru           |
| Лидия      |              nan |         | koroleva.marmeladnaya@yandex.ru |
| Нина       |              nan |         | nina_blinova_75@mail.ru         |
| Татьяна    |              nan |         | t-filipenko@mail.ru             |
| Надежда    |              nan |         | verevkina_@mail.ru              |
| Юлия       |              nan |         | kruckova0505@mail.ru            |
| Вася       |              nan |         | niko0-1@mail.ru                 |
| Алла       |              nan |         | vm22alla@mail.ru                |
| Виктория   |              nan |         | kejlviktoria@gmail.com          |
| Лариса     |              nan |         | lorik_1909_ya@mail.ru           |
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
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 78.70% |
| Phones | 97.13% |
| Address | 91.25% |



### Data sample
```
| names                            | emails                          | phones          | address                                                      |
|:---------------------------------|:--------------------------------|:----------------|:-------------------------------------------------------------|
| ['Александр']                    | ['alejanderez@gmail.com']       | ['79999896615'] | ['109000 Москва']                                            |
| ['Алина']                        | ['ayzanina@gmail.com']          | ['79826566992'] | ['194358 Санкт-Петербург Федора Абрамова 8 670']             |
| ['Альбина']                      | ['albina.kolody@yandex.ru']     | ['79787020328'] | ['298328 КЕРЧЬ Ягунова 19']                                  |
| ['Артур']                        |                                 | ['79017063774'] | ['Москва Гордейская 55']                                     |
| ['Боронина Ирина Владимировна']  |                                 | ['79202264778'] | ['397500 Бутурлиновка Маяковского 2']                        |
| ['Геннадий']                     | ['g.kalganov73@gmail.com']      | ['79117974714'] | ['190000 Санкт-Петербург']                                   |
| ['Евгений']                      | ['e.shifron@yandex.ru']         |                 |                                                              |
| ['Елена']                        | ['len4ik-i@yandex.ru']          | ['79042215005'] | ['169712 Усинск Молодежная 18 251']                          |
| ['Елена']                        | ['ekozlova@action-press.ru']    | ['79099661496'] | ['101000 МОСКВА Новодмитровская 5а стр8']                    |
| ['Елена']                        | ['bulakczurkan@mail.ru']        | ['79184804184'] |                                                              |
| ['Елена']                        | ['sokolova.liliana@bk.ru']      | ['79524186558'] | ['344045 Ростов-на-Дону']                                    |
| ['Есименко Наталья Анатольевна'] |                                 | ['79841790482'] | ['682375 Найхин Максима Пасара 24 2']                        |
| ['Ирина']                        | ['hop_i@mail.ru']               | ['79067489891'] | ['127543 Москва Корнейчука 58А 163']                         |
| ['Ирина']                        | ['golovanova.irina7@gmail.com'] | ['79139603690'] | ['644000 Омск']                                              |
| ['Ирина']                        | ['kipspb@inbox.ru']             | ['79215550593'] |                                                              |
| ['Кирилл']                       |                                 | ['79503756180'] | ['603000 Нижний Новгород Яна Фабрициуса 50']                 |
| ['Ковалева Диана Романовна']     |                                 | ['79219040222'] | ['190000 Санкт-Петербург Пражская 9 к.2 3']                  |
| ['Константин Гаврилович']        | ['konst.efimoff2011@yandex.ru'] | ['79055896839'] | ['109000 Москва 1-я Ямского поля 28.']                       |
| ['Лыкова Татьяна Валентиновна']  |                                 | ['79134447708'] | ['662600 Минусинск Утро-Сентябрьское 61 А к.2 16']           |
| ['Людмила']                      | ['popovich08071954@icloud.com'] | ['79098946742'] | ['675000 Благовещенск 675000 Благовещенск Дьяченко 5к1 кв8'] |
```