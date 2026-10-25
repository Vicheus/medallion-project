# Parsetron results

## About row data

> - Code name: index_0372
> - File path: asi.ru.txt
> - Total rows: 571448

### Schema
```
root
 |-- Регион: string (nullable = true)
 |-- Город: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Имя: string (nullable = true)
 |-- Отчество: string (nullable = true)
 |-- Позиция: string (nullable = true)
 |-- Компания: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- Почта: string (nullable = true)

```

### Data sample
```
| Регион           | Город   | Фамилия    | Имя      | Отчество      | Позиция                                                   | Компания                                          |   Номер телефона | Почта                        |
|:-----------------|:--------|:-----------|:---------|:--------------|:----------------------------------------------------------|:--------------------------------------------------|-----------------:|:-----------------------------|
|                  |         | Моисеева   | Ольга    | Сергеевна     |                                                           |                                                   |      79206751210 | olga.moiseeva2020@mail.ru    |
|                  |         | Самойлов   | Алексей  | Александрович |                                                           |                                                   |      79853071747 | kainoneself@gmail.com        |
| Омская область   |         | Малюк      | Елена    | Анатольевна   | Педагог                                                   | Центр развития ребенка — детский сад              |      79136201227 | lovelypleams@inbox.ru        |
|                  |         | Шеремет    | Варвара  | Федоровна     |                                                           |                                                   |      79859511757 | varya.sheremet@yandex.ru     |
| Амурская область |         | Норкина    | Анна     | Владимировна  | начальник отдела дополнительного образования и воспитания | министерство образования и науки Амурской области |      79146180079 | annorkina@mail.ru            |
|                  |         | Шитенкова  | Анна     | Вячеславовна  |                                                           |                                                   |      79605092085 | ashitenkova@mail.ru          |
|                  |         | Рисаева    | Гульфина | Мухтабаровна  |                                                           |                                                   |      79274849725 | gulfina-06@mail.ru           |
|                  |         | Валяева    | Валерия  | Александровна |                                                           |                                                   |      79162836434 | valyaevavaleri@gmail.com     |
|                  |         | Ходова     | Анита    | Маирбеговна   |                                                           |                                                   |      79232958977 | anita-hodova@inbox.ru        |
|                  |         | Кулябина   | Алиса    |               |                                                           |                                                   |      79193903195 | akey.mail@yandex.ru          |
|                  |         | Кузнецов   | Никита   | Александрович |                                                           |                                                   |      79867392231 | good-fokys@yandex.ru         |
|                  |         | Гольдберг  | Юрий     | Максимович    |                                                           |                                                   |      79036109715 | ugoldm03@gmail.com           |
|                  |         | Барсукова  | Елена    |               |                                                           |                                                   |      79857696798 | lea1973@yandex.ru            |
|                  |         | Потапов    | Леонид   | Игоревич      |                                                           |                                                   |      79515118880 | me@leonidpotapov.com         |
|                  |         | Романова   | Марина   | Юрьевна       |                                                           |                                                   |      79684686003 | marinaromanova2003@yandex.ru |
|                  |         | Григорьева | Елена    | Ильинична     |                                                           |                                                   |      79631201073 | biz_on@list.ru               |
|                  |         | Леснова    | Юлия     | Хамзовна      |                                                           |                                                   |      79855689148 | lesnova_yuliya@mail.ru       |
|                  |         | Кузнецов   | Герман   |               |                                                           |                                                   |      79150515985 | gerkuzn@ya.ru                |
|                  |         | Валиева    | Нафиса   | Ленисовна     |                                                           |                                                   |      79027118772 | nafisalenva@gmail.com        |
|                  |         | Созарукова | Светлана | Аретовна      |                                                           |                                                   |      79380252995 | bossveta1@yandex.ru          |
```


## About final data
> - Total rows: 536222

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
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 97.63% |
| Phones | 94.76% |
| Address | 41.13% |
| Works | 2.46% |



### Data sample
```
| names                             | emails                        | phones          | address                 | works                                                                                                                                                                                      |
|:----------------------------------|:------------------------------|:----------------|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Атаев Зелимхан']                | ['ata-lana@yandex.ru']        | ['79295204710'] |                         |                                                                                                                                                                                            |
| ['Гонсалез Сергей']               | ['73zhenja@mail.ru']          | ['79250292891'] |                         |                                                                                                                                                                                            |
| ['Соколова Татьяна']              | ['atalz888@mail.ru']          | ['79653393222'] |                         |                                                                                                                                                                                            |
| ['Лаврёнов Олег']                 | ['ayavrik@inbox.ru']          | ['79503032412'] | ['Республика Хакасия']  | [Row(post=None, date_start=None, date_end=None, company='ЧОУ ЦДО Фюзис', address=None, comment=None)]                                                                                      |
| ['Кузнецов Мишка']                |                               | ['79175716819'] |                         |                                                                                                                                                                                            |
| ['Рябова Ольга']                  | ['svetar.1969@mail.ru']       | ['79505966853'] |                         |                                                                                                                                                                                            |
| ['Полухина Ксения']               |                               | ['79521713783'] |                         |                                                                                                                                                                                            |
| ['Базанова Людмила']              | ['lyudmila.bazanova@list.ru'] | ['79038328608'] |                         |                                                                                                                                                                                            |
| ['Березин Денис Сергеевич']       | ['den42b@mail.ru']            | ['79132883997'] |                         |                                                                                                                                                                                            |
| ['Волкогонова Юлия Валерьевна']   |                               | ['79132941032'] | ['Кемеровская область'] | [Row(post='Ведущий маркетолог', date_start=None, date_end=None, company='Муниципиальный некоммерческий Фонд поддержки малого предпринимательства г.Кемерово', address=None, comment=None)] |
| ['Белова Мария Андреевна']        | ['marka.ha-ha@yandex.ru']     | ['79537469042'] |                         |                                                                                                                                                                                            |
| ['Абушева Ольга Евгеньевна']      | ['alenka_1469@mail.ru']       | ['79227212121'] |                         |                                                                                                                                                                                            |
| ['Акулов Павел Владимирович']     | ['pa_sovetnik@bk.ru']         | ['79042899017'] |                         |                                                                                                                                                                                            |
| ['Аметов Эмиль Мамутович']        | ['iasg@mail.ru']              | ['79312882810'] |                         |                                                                                                                                                                                            |
| ['Антонова Мария Михайловна']     | ['npc@novprav.ru']            | ['79212043124'] |                         |                                                                                                                                                                                            |
| ['Ахметов Билал Хакимович']       | ['ahmetov@mail.ru']           | ['79047185424'] |                         |                                                                                                                                                                                            |
| ['Богданов Алексей Евгеньевич']   | ['consalt.yug@mail.ru']       | ['79618190424'] |                         |                                                                                                                                                                                            |
| ['Бочаров Николай Александрович'] | ['astrafkc@yandex.ru']        | ['79642542684'] |                         |                                                                                                                                                                                            |
| ['Бриндальский Петр Степанович']  | ['droazis@mail.ru']           | ['79224579888'] |                         |                                                                                                                                                                                            |
| ['Голубков Владимир Иванович']    | ['farmfab@rambler.ru']        | ['79236132079'] |                         |                                                                                                                                                                                            |
```