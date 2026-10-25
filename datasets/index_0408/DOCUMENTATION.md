# Parsetron results

## About row data

> - File path: gazon-trava.ru - @StormBaseAdapter.csv
> - Total rows: 22955

### Schema
```
root
 |-- date: string (nullable = true)
 |-- name: string (nullable = true)
 |-- text: string (nullable = true)
 |-- comment: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- adress: string (nullable = true)

```

### Data sample
```
| date                | name                             | text   | comment   | email                |       phone | adress                          |
|:--------------------|:---------------------------------|:-------|:----------|:---------------------|------------:|:--------------------------------|
| 07/01/2015 22:49:59 | Алексей                          |        |           |                      | 79168554525 |                                 |
| 08/01/2015 06:26:00 | аникина ирина евгеньевна         |        |           | iren1957@yandex.ru   | 79104803397 |                                 |
| 07/01/2015 21:54:20 | Боровкова Александра Анатольевна |        |           | furiousangel@bk.ru   | 79261506801 | Газопровод, дом 13 корп 1 кв 42 |
| 07/01/2015 22:20:11 | Мария                            |        |           |                      | 79197691290 |                                 |
| 07/01/2015 16:53:50 | ирина                            |        |           |                      | 79518478978 |                                 |
| 07/01/2015 20:54:38 | Анастасия                        |        |           |                      | 79161914949 |                                 |
| 06/01/2015 17:14:24 | Антон                            |        |           |                      | 79163452420 |                                 |
| 06/01/2015 02:17:55 | александр                        |        |           |                      | 79151103889 |                                 |
| 06/01/2015 01:27:04 | тимур                            |        |           |                      | 79197273312 |                                 |
| 06/01/2015 02:17:48 | Надежда Михайловнна Опарина      |        |           |                      | 79194578306 |                                 |
| 05/01/2015 04:19:24 | Индира                           |        |           |                      | 79091644547 |                                 |
| 04/01/2015 21:20:45 | Елена                            |        |           |                      | 79636351200 |                                 |
| 04/01/2015 16:34:15 | Галина Алексеевна                |        |           |                      | 79257060602 |                                 |
| 04/01/2015 15:37:44 | Софья                            |        |           |                      | 79060994152 |                                 |
| 03/01/2015 21:50:15 | Мороз Елена Алексеевна           |        |           |                      | 79519775816 |                                 |
| 03/01/2015 23:47:23 | Игорь                            |        |           |                      | 79636044009 |                                 |
| 03/01/2015 16:37:18 | юлия                             |        |           | julivv@yandex.ru     | 79160189665 |                                 |
| 03/01/2015 14:40:03 | Антон                            |        |           | intdep2005@yandex.ru | 79250112467 |                                 |
| 02/01/2015 15:32:46 | Наталья                          |        |           |                      | 79131062299 |                                 |
| 02/01/2015 17:57:23 | людмила                          |        |           |                      | 79031508786 |                                 |
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
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 95.47% |
| Emails | 66.99% |
| Address | 78.65% |
| Raw_metadata | 33.49% |
| Actuality | 38.41% |



### Data sample
```
| names                                  | phones          | emails                          | address                                                                    | raw_metadata                                                          | actuality   |
|:---------------------------------------|:----------------|:--------------------------------|:---------------------------------------------------------------------------|:----------------------------------------------------------------------|:------------|
| ['-Чернов Евгений Алексеевич']         | ['79185130934'] |                                 |                                                                            |                                                                       |             |
| ['Alenyshka Marysina']                 | ['79672537076'] | ['alenyshka6677@gmail.com']     |                                                                            | ['{"comment": "на 1704.вв"}']                                         | 04.12.2014  |
| ['Alexander Buyanov']                  | ['79859238534'] |                                 |                                                                            |                                                                       | 05.11.2020  |
| ['Alexandr']                           | ['79166198041'] |                                 |                                                                            |                                                                       | 06.06.2022  |
| ['Alsico.Ltdmail.Ru']                  | ['79104543060'] |                                 |                                                                            |                                                                       | 03.07.2023  |
| ['Amirbek Safarov']                    | ['79037878682'] | ['valentin-659@yandex.ru']      | ['Московская обл г Истра деревня Новодарьино д 24']                        |                                                                       |             |
| ['Amospavlovyandex.Ru']                | ['79040278103'] | ['amospavlov@yandex.ru']        | ['Проспект Мира 122 1']                                                    | ['{"text": "4956833228 телефон офиса для курьера"}']                  | 03.03.2020  |
| ['Anatoliy Rudichenko Vasilievich']    | ['79219336018'] | ['rav60@yandex.ru']             | ['Санкт-Петербургул.Фурштатская д. 43 пом. 12Н']                           |                                                                       | 03.06.2015  |
| ['Andrei Gromilov']                    | ['79264694494'] |                                 |                                                                            |                                                                       |             |
| ['Andreikarabanov']                    | ['79162094099'] | ['andrei_karabanov@mail.ru']    | ['Москва ул Молодогвардейская д 2 к 1']                                    |                                                                       |             |
| ['Andrey Vladimirovich Yadrikhinskiy'] | ['79212918651'] | ['yadrikhinskiy2010@yandex.ru'] | ['163000 обл. Архангельская г. Архангельск пр-кт. Троицкий д. 104 кв. 97'] | ['{"comment": "Доставка ТК в г. Архангельск до пункта самовывоза."}'] |             |
| ['Andrey Yakushev']                    | ['79228881008'] |                                 |                                                                            |                                                                       | 01.11.2020  |
| ['Aндрей']                             | ['79190134371'] |                                 |                                                                            |                                                                       |             |
| ['Baranow.Iiyandex.Ru']                | ['79037115564'] | ['baranow.ii@yandex.ru']        | ['Пехотная 3 кор 15']                                                      | ['{"text": "К заказу 18398"}']                                        | 08.01.2021  |
| ['Barros']                             | ['79161663544'] | ['jbarrosj@hotmail.com']        | ['Udalzova 73 Apt. 144']                                                   |                                                                       |             |
| ['Boris Uzunski']                      | ['79267855856'] | ['uzunski7@yandex.ru']          | ['ул. Новослободская д.3Первый етаж тц САФА отд. шапки']                   | ['{"comment": "на 19.12 Настя"}']                                     |             |
| ['Cергей']                             | ['79522353468'] |                                 |                                                                            | ['{"comment": "самовывоз"}']                                          | 03.11.2015  |
| ['Cергей']                             | ['79645789237'] |                                 | ['ул. Новочеремушкинская д.50']                                            |                                                                       |             |
| ['Damira Sulaimanova']                 | ['79265482026'] | ['sula84@bk.ru']                | ['Ул.можайское шоссе дом 39.кв 236']                                       | ['{"comment": "Я хочу ещё клещевит и муравьед не смогла добавить"}']  |             |
| ['Dimitri Popov']                      | ['79854184625'] | ['dimitri.a.popov@gmail.com']   | ['Vavilova 37A apt. 7']                                                    |                                                                       |             |
```