# Parsetron results

## About row data

> - File path: users_preprocessed.csv
> - Total rows: 16970

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- notification_type: string (nullable = true)
 |-- operation_id: string (nullable = true)
 |-- amount: double (nullable = true)
 |-- withdraw_amount: double (nullable = true)
 |-- currency: integer (nullable = true)
 |-- datetime: string (nullable = true)
 |-- sender: long (nullable = true)
 |-- codepro: integer (nullable = true)
 |-- label: string (nullable = true)
 |-- sha1_hash: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- firstname: string (nullable = true)
 |-- fathersname: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- city: string (nullable = true)
 |-- street: string (nullable = true)
 |-- building: string (nullable = true)
 |-- suite: string (nullable = true)
 |-- flat: string (nullable = true)
 |-- zip: integer (nullable = true)

```

### Data sample
```
|   id | notification_type   | operation_id       |   amount |   withdraw_amount |   currency | datetime            |   sender |   codepro | label   | sha1_hash                                | lastname      | firstname   | fathersname   | email                           |        phone | city                      | street            | building   |   suite |   flat |   zip |
|-----:|:--------------------|:-------------------|---------:|------------------:|-----------:|:--------------------|---------:|----------:|:--------|:-----------------------------------------|:--------------|:------------|:--------------|:--------------------------------|-------------:|:--------------------------|:------------------|:-----------|--------:|-------:|------:|
|    5 | p2p-incoming        | test-notification  |   278.8  |              0    |        643 | 2014-08-19 19:06:41 |      nan |         0 |         | 748dac527650dc667f9206139b97ecad6450810e |               |             |               |                                 |              |                           |                   |            |         |        |   nan |
|    6 | card-incoming       | 461868478504024012 |   382.2  |            390    |        643 | 2014-08-20 16:47:58 |      nan |         0 |         | 3b2a2603a44983372e3ca22f58ef5d8b6f062da0 | Колесникова   | Анна        | Павловна      | Kap1996@list.ru                 |  89219304065 | Санкт-Петербург           | Морской           | 11         |         |      7 |   nan |
|    7 | card-incoming       | 462197755774030012 |   382.2  |            390    |        643 | 2014-08-24 12:15:55 |      nan |         0 |         | 64062ea117c042e5bc317621d6cab0189f5c303a | Сайфутдинова  | Арина       | Николаевна    | makadibay@bk.ru                 | +79871463225 | Нефтекамск                | Ленина            | 64         |         |     53 |   nan |
|    8 | p2p-incoming        | 924570713766012017 |   388.06 |            390    |        643 | 2014-08-25 12:35:56 |      nan |         0 |         | 9bbcd5c4b5739539b95b821eae0327eeb6ec91be | Онучина       | Анастасия   | Геннадьевна   | nastyamakaron@gmail.com         |  89090163987 | Екатеринбург              | Шварца            | 16         |       1 |    132 |   nan |
|    9 | card-incoming       | 462296542621027012 |   382.2  |            390    |        643 | 2014-08-25 15:42:22 |      nan |         0 |         | c486322c1cb11f4e85ddecb0e92b3bedcbbc0853 | Гниденко      | Екатерина   | Владимировна  | Belochka592@mail.ru             |  89123840412 | Тобольск                  | 7а мкр-он         | 7б дом     |         |     27 |   nan |
|   10 | p2p-incoming        | 924767087564120025 |   388.06 |            390    |        643 | 2014-08-26 15:52:23 |      nan |         0 |         | 15f691d7c13443060bc96de4bdcc7c6de954fe5a | Нурмухамедова | Азиза       | Тимуровна     | aziza9731@mail.ru               |  89274000638 | Богатые Сабы              | М.Джалиля         | 20         |       2 |        |   nan |
|   11 | p2p-incoming        | 924768721050042017 |   388.06 |            390    |        643 | 2014-08-26 16:06:00 |      nan |         0 |         | d662a1943258224a3fb0d0720be7ddbca6cf2c4c | Гавриленко    | Кирилл      | Викторович    | kirill.gavrilenko2013@yandex.ru |  89616487941 | Балашов                   | 3-я Заводская     | 17         |         |        |   nan |
|   12 | card-incoming       | 462391866419071012 |   382.2  |            390    |        643 | 2014-08-26 18:11:06 |      nan |         0 |         | c305cbb80677a2a7c4771ef6cdcfafcf716d1e93 | Тарханов      | Илья        | Юрьевич       | tark_ilya@icloud.com            |  89670849323 | Видное                    | Ольховая          | 2          |         |    196 |   nan |
|   13 | card-incoming       | 462418212178010012 |   382.2  |            390    |        643 | 2014-08-27 01:30:12 |      nan |         0 |         | f3dc7ab02e44a9289e95da25e88063e3f369d921 | Тарханов      | Илья        | Юрьевич       | tark_ilya@icloud.com            |  89670849323 | Видное                    | Ольховая          | 2          |         |    196 |   nan |
|   14 | p2p-incoming        | 924932134560082009 |   388.06 |            390    |        643 | 2014-08-27 14:47:47 |      nan |         0 |         | c9c19bcf62b290998695707370eda09f43c318ea | Еделькина     | Анна        | Викторовна    | edelkina100@yandex.ru           |  89201631460 | Тверь                     | 1-й пр. Нестерова | 25/25      |         |        |   nan |
|   15 | p2p-incoming        | 924945204744034025 |   388.06 |            390    |        643 | 2014-08-27 16:36:42 |      nan |         0 |         | deef692d51a2d977862b0f7b4ac15eaed6517f68 | Комкова       | Анна        | Александровна | ann.komkova98@gmail.com         |  89152684077 | Москва                    | Островитянова     | 11         |         |    250 |   nan |
|   16 | p2p-incoming        | 924951211460006017 |   388.06 |            390    |        643 | 2014-08-27 17:26:45 |      nan |         0 |         | 72082930c87d2beddd65662afd54e521b893213e | Куликова      | Анастасия   | Алексеевна    | jemrey@yandex.ru                |  89533174531 | Обнинск                   | Гурьянова         | 7          |         |     58 |   nan |
|   17 | card-incoming       | 462531236521032012 |  1146.6  |           1170    |        643 | 2014-08-28 08:53:56 |      nan |         0 |         | 345a796906c65abe6a3f6d4fe527d5ef9d45006b | Матвеева      | Зоя         | Николаевна    | matveeva.zoya@gmail.com         | +79095404579 | Северск                   | Ленинградская     | 6          |         |    147 |   nan |
|   18 | p2p-incoming        | 925105120382188009 |   388.06 |            390    |        643 | 2014-08-28 14:49:20 |      nan |         0 |         | edf9975e687a803d7f108626c3f9926648e59301 | Заблоцкая     | Марианна    | Алексеевна    | marianna_96@mail.ru             |  89132687567 | Барнаул                   | Георгиева         | 16         |         |     99 |   nan |
|   19 | card-incoming       | 462570223208036012 |   382.2  |            390    |        643 | 2014-08-28 19:43:43 |      nan |         0 |         | f577cce3db644a9007f8a3202d706094af0e9b86 | Сайфутдинова  | Татьяна     | Викторовна    | sayfuttv@yandex.ru              |  89067753146 | Москва                    | п. Знамя Октября  | 20         |         |     20 |   nan |
|   20 | card-incoming       | 462577262574033012 |   382.2  |            390    |        643 | 2014-08-28 21:41:02 |      nan |         0 |         | 46141ceb8287b6229162f5d1f6bdccb48af39374 | Мурашева      | Елизавета   | Александровна | lizaveta071197@gmail.com        |  89818582528 | Санкт-Петербург,Ломоносов | Владимирская      | 30         |         |      1 |   nan |
|   21 | card-incoming       | 462744450183008012 |   382.2  |            390    |        643 | 2014-08-30 20:07:30 |      nan |         0 |         | 2febca2f0e9089ec0d8b3b1212901b17dd60fbd4 | Татаринова    | Ольга       | Вадимовна     | hedgehoc_in_fog@list.ru         |  89183236189 | Краснодар                 | им. Гоголя        | 64         |         |     10 |   nan |
|   22 | card-incoming       | 462825356934099012 |   382.2  |            390    |        643 | 2014-08-31 18:35:56 |      nan |         0 |         | d3ca31f72bd5ebe9175aedd7e018bc6ce59ce619 | Васильева     | Дарья       | Юрьевна       | dasholina97@yandex.ru           | +79163785038 | Москва                    | Бирюлевская       | 47         |         |    319 |   nan |
|   23 | p2p-incoming        | 926127246826014009 |   390    |            391.95 |        643 | 2014-09-03 12:47:03 |      nan |         0 |         | 4804f0e078c1a3c554fa6da24b1a1bd680775556 |               |             |               |                                 |              |                           |                   |            |         |        |   nan |
|   24 | card-incoming       | 463238379514047012 |   382.2  |            390    |        643 | 2014-09-05 13:19:39 |      nan |         0 |         | e729ad45d410ccfcc3de819915bb67ff928f71c7 | Барсукова     | Екатерина   | Андреевна     | fleapheat@rambler.ru            |  89191152296 | Еманжелинск               | Фрунзе            | 40         |         |     23 |   nan |
```

> - File path: payments_preprocessed.csv
> - Total rows: 16970

### Schema
```
root
 |-- firstname: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- fathersname: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- city: string (nullable = true)
 |-- street: string (nullable = true)
 |-- building: string (nullable = true)
 |-- flat: string (nullable = true)
 |-- zip: integer (nullable = true)

```

### Data sample
```
| firstname   | lastname      | fathersname   | email                           |        phone | city                      | street            | building   |   flat |   zip |
|:------------|:--------------|:--------------|:--------------------------------|-------------:|:--------------------------|:------------------|:-----------|-------:|------:|
|             |               |               |                                 |              |                           |                   |            |        |   nan |
| Анна        | Колесникова   | Павловна      | Kap1996@list.ru                 |  89219304065 | Санкт-Петербург           | Морской           | 11         |      7 |   nan |
| Арина       | Сайфутдинова  | Николаевна    | makadibay@bk.ru                 | +79871463225 | Нефтекамск                | Ленина            | 64         |     53 |   nan |
| Анастасия   | Онучина       | Геннадьевна   | nastyamakaron@gmail.com         |  89090163987 | Екатеринбург              | Шварца            | 16         |    132 |   nan |
| Екатерина   | Гниденко      | Владимировна  | Belochka592@mail.ru             |  89123840412 | Тобольск                  | 7а мкр-он         | 7б дом     |     27 |   nan |
| Азиза       | Нурмухамедова | Тимуровна     | aziza9731@mail.ru               |  89274000638 | Богатые Сабы              | М.Джалиля         | 20         |        |   nan |
| Кирилл      | Гавриленко    | Викторович    | kirill.gavrilenko2013@yandex.ru |  89616487941 | Балашов                   | 3-я Заводская     | 17         |        |   nan |
| Илья        | Тарханов      | Юрьевич       | tark_ilya@icloud.com            |  89670849323 | Видное                    | Ольховая          | 2          |    196 |   nan |
| Илья        | Тарханов      | Юрьевич       | tark_ilya@icloud.com            |  89670849323 | Видное                    | Ольховая          | 2          |    196 |   nan |
| Анна        | Еделькина     | Викторовна    | edelkina100@yandex.ru           |  89201631460 | Тверь                     | 1-й пр. Нестерова | 25/25      |        |   nan |
| Анна        | Комкова       | Александровна | ann.komkova98@gmail.com         |  89152684077 | Москва                    | Островитянова     | 11         |    250 |   nan |
| Анастасия   | Куликова      | Алексеевна    | jemrey@yandex.ru                |  89533174531 | Обнинск                   | Гурьянова         | 7          |     58 |   nan |
| Зоя         | Матвеева      | Николаевна    | matveeva.zoya@gmail.com         | +79095404579 | Северск                   | Ленинградская     | 6          |    147 |   nan |
| Марианна    | Заблоцкая     | Алексеевна    | marianna_96@mail.ru             |  89132687567 | Барнаул                   | Георгиева         | 16         |     99 |   nan |
| Татьяна     | Сайфутдинова  | Викторовна    | sayfuttv@yandex.ru              |  89067753146 | Москва                    | п. Знамя Октября  | 20         |     20 |   nan |
| Елизавета   | Мурашева      | Александровна | lizaveta071197@gmail.com        |  89818582528 | Санкт-Петербург,Ломоносов | Владимирская      | 30         |      1 |   nan |
| Ольга       | Татаринова    | Вадимовна     | hedgehoc_in_fog@list.ru         |  89183236189 | Краснодар                 | им. Гоголя        | 64         |     10 |   nan |
| Дарья       | Васильева     | Юрьевна       | dasholina97@yandex.ru           | +79163785038 | Москва                    | Бирюлевская       | 47         |    319 |   nan |
|             |               |               |                                 |              |                           |                   |            |        |   nan |
| Екатерина   | Барсукова     | Андреевна     | fleapheat@rambler.ru            |  89191152296 | Еманжелинск               | Фрунзе            | 40         |     23 |   nan |
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
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- actuality: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 97.86% |
| Emails | 99.20% |
| Address | 39.57% |
| Actuality | 100.00% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                                | phones          | emails                             | address                                                                  | actuality   | raw_metadata                                                                                                                                                                                                                                                                     |
|:-------------------------------------|:----------------|:-----------------------------------|:-------------------------------------------------------------------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Алла Жуковская Владиславовна']     | ['79067533104'] | ['krista6@mail.ru']                |                                                                          | 10.11.2014  | ['{"amount": "382.2", "withdraw_amount": "390.0", "notification_type": "card-incoming"}']                                                                                                                                                                                        |
| ['Анастасия Аллянова Юрьевна']       | ['79625929044'] | ['egbubblea@gmail.com']            |                                                                          | 04.02.2015  | ['{"amount": "293.02", "withdraw_amount": "299.0", "notification_type": "card-incoming"}']                                                                                                                                                                                       |
| ['Светлана Атабиева Юсуповна']       | ['79287070940'] | ['sharikmalika@yandex.ru']         |                                                                          | 19.04.2015  | ['{"amount": "363.83", "withdraw_amount": "365.65", "notification_type": "p2p-incoming"}']                                                                                                                                                                                       |
| ['Анна Липина Анатольевна']          | ['79210457796'] | ['lipina97@inbox.ru']              |                                                                          | 31.10.2014  | ['{"amount": "382.2", "withdraw_amount": "390.0", "notification_type": "card-incoming"}']                                                                                                                                                                                        |
| ['Наталия Букреева Станиславна']     | ['79104143183'] | ['dra3@yandex.ru']                 |                                                                          | 27.11.2014  | ['{"amount": "248.76", "withdraw_amount": "250.0", "notification_type": "p2p-incoming"}']                                                                                                                                                                                        |
| ['Анна Пакалова Анатольевна']        | ['79041199010'] | ['mobidic77@mail.ru']              | ['Иркутская область Казачинско-Ленский район п.Улькан Мира д. 1 кв. 39'] | 29.02.2016  | ['{"amount": "494.61", "withdraw_amount": "504.7", "notification_type": "card-incoming"}']                                                                                                                                                                                       |
| ['Даниил Соседов Станиславович']     | ['79885459590'] | ['danielblare88@gmail.com']        | ['Белая Калитва Машиностроителей д. 11 кв. 12']                          | 16.01.2016  | ['{"amount": "494.61", "withdraw_amount": "504.7", "notification_type": "card-incoming"}']                                                                                                                                                                                       |
| ['Инна Батова Амирхановна']          | ['79631656368'] | ['rezik999@bk.ru']                 |                                                                          | 01.11.2014  | ['{"amount": "382.2", "withdraw_amount": "390.0", "notification_type": "card-incoming"}']                                                                                                                                                                                        |
| ['Марина Котовская Викторовна']      | ['79217786471'] | ['kotovskii@bk.ru']                | ['Санкт- Петербург Шушары Ленсоветовский д. 21 кв. 58']                  | 14.09.2014  | ['{"amount": "382.2", "withdraw_amount": "390.0", "notification_type": "card-incoming"}']                                                                                                                                                                                        |
| ['Юрий Кулиш Павлович']              | ['79091526849'] | ['t7923007@yandex.ru']             |                                                                          | 03.11.2014  | ['{"amount": "388.06", "withdraw_amount": "390.0", "notification_type": "p2p-incoming"}']                                                                                                                                                                                        |
| ['Валерия Преподобная Витальевна']   | ['79266872530'] | ['v.prepodobnaya@yandex.ru']       | ['Москва Мичуринский пр-т д. 46 кв. 81']                                 | 27.02.2016  | ['{"amount": "494.61", "withdraw_amount": "504.7", "notification_type": "card-incoming"}']                                                                                                                                                                                       |
| ['Анна Лялина Александровна']        | ['79817096662'] | ['anna-lyalin@yandex.ru']          |                                                                          | 11.12.2016  | ['{"amount": "293.02", "withdraw_amount": "299.0", "notification_type": "card-incoming"}']                                                                                                                                                                                       |
| ['Максим Юрчин Викторович']          | ['79129189424'] | ['sil911@mail.ru']                 |                                                                          | 02.12.2014  | ['{"amount": "245.0", "withdraw_amount": "250.0", "notification_type": "card-incoming"}']                                                                                                                                                                                        |
| ['Татьяна Черевина Валентиновна']    | ['79060976409'] | ['cherevina@mail.ru']              |                                                                          | 07.04.2015  | ['{"amount": "464.32", "withdraw_amount": "473.8", "notification_type": "card-incoming"}', '{"amount": "207.94", "withdraw_amount": "212.18", "notification_type": "card-incoming"}', '{"amount": "301.81", "withdraw_amount": "307.97", "notification_type": "card-incoming"}'] |
| ['Артём Шарлаимов Андреевич']        | ['79530621810'] | ['sharlaimov.artem@mail.ru']       |                                                                          | 25.11.2014  | ['{"amount": "248.76", "withdraw_amount": "250.0", "notification_type": "p2p-incoming"}']                                                                                                                                                                                        |
| ['Елизавета Пугачева Александровна'] | ['79616363010'] | ['danya-mail@mail.ru']             |                                                                          | 11.01.2015  | ['{"amount": "382.2", "withdraw_amount": "390.0", "notification_type": "card-incoming"}']                                                                                                                                                                                        |
| ['Елена Алексеева Викторовна']       | ['79152585052'] | ['real1555@yandex.ru']             |                                                                          | 02.05.2015  | ['{"amount": "461.19", "withdraw_amount": "463.5", "notification_type": "p2p-incoming"}']                                                                                                                                                                                        |
| ['Ольга Стромило Владимировна']      | ['79284168018'] | ['olga_stromilo@mail.ru']          |                                                                          | 27.01.2015  | ['{"amount": "403.76", "withdraw_amount": "412.0", "notification_type": "card-incoming"}', '{"amount": "293.02", "withdraw_amount": "299.0", "notification_type": "card-incoming"}']                                                                                             |
| ['Артем Тюпов Витальевич']           | ['79688968400'] | ['artem3090@mail.ru']              |                                                                          | 10.05.2015  | ['{"amount": "245.0", "withdraw_amount": "250.0", "notification_type": "card-incoming"}']                                                                                                                                                                                        |
| ['Вероника Перзашкевич Юрьевна']     | ['79203190817'] | ['nika.v.strane.chudes@yandex.ru'] | ['216790 Руднянский райондеревня Красный Двор Микулинская д. 1']         | 12.09.2015  | ['{"amount": "494.61", "withdraw_amount": "504.7", "notification_type": "card-incoming"}']                                                                                                                                                                                       |
```