# Parsetron results

## About row data

> - Code name: index_0179
> - File path: /media/user/SAMSUNG/Databases/index_0179/raw/chitai-gorod.ru (05.2023).txt
> - Total rows: 9800677

### Schema
```
root
 |-- Логин: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Имя: string (nullable = true)
 |-- Отчество: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Город: string (nullable = true)

```

### Data sample
```
| Логин               | Почта                        | Фамилия     | Имя                               | Отчество      |   Номер телефона | Дата рождения   | Город                                        |
|:--------------------|:-----------------------------|:------------|:----------------------------------|:--------------|-----------------:|:----------------|:---------------------------------------------|
| anna2607201         | ludmilavoskovykh@yandex.ru   | Восковых    | Людмила                           | Андреевна     |      79232145717 | 1992.06.09      | Город Москва                                 |
| katya               | luckylifek@gmail.com         | Богданова   | Екатерина                         |               |      79213295640 | 1988.12.28      | Город Воронеж, Воронежская Область           |
| ilyana              | sh.lidiya@rambler.ru         | Геращенко   | Иляна                             |               |                  | 1983.05.16      | Город Москва                                 |
| pindyurina          | pindyurina@bookcentre.ru     | Коля        | Коля                              |               |                  | 1951.01.01      | Город Пенза, Пензенская Область              |
| paparampan          | paramonov@bookcentre.ru      | Парамонов   | Антон                             | Николаевич    |                  | 1987.06.12      | Город Москва                                 |
| optimiz             | marykin@bookcentre.ru        |             |                                   |               |                  |                 |                                              |
| project             | project@internetpromotion.ru | Данилевский | Александр                         |               |                  | 1951.01.01      |                                              |
| lidiya36            | shiryaeva.l@bookcentre.ru    | Ширяева     | Лидия                             |               |                  | 1951.01.01      |                                              |
| Volka               | vvinogradskiy@bookcentre.ru  |             | Vinogradskiy Vladimir Alekseevich |               |                  | 1965.01.01      | Город Москва                                 |
| infunx              | infunx@gmail.com             | Д           | Алексей                           |               |                  | 1983.06.24      |                                              |
| yakovlevj           | triamm@gmail.com             | Яковлев     | Евгений                           | Эдуардович    |      79224824587 | 1990.06.20      | Город Санкт-Петербург                        |
| nata-yarm           | nata-yarm@mail.ru            | Воронежцева | Наталья                           |               |      79603461063 | 1951.01.01      | Город Саратов, Саратовская Область           |
| Yulka               | ivanovajuli1007@mail.ru      | Иванова     | Юлия                              | Ивановна      |      79125870548 | 1987.07.10      | Город Пермь, Пермский Край                   |
| edmeya              | edmeya@gmail.com             | Полищук     | Альфия                            | Наильевна     |                  | 1987.04.22      |                                              |
| vasenjova           | 44034403@mail.ru             | Кузнецова   | Валерия                           |               |      79610742054 | 1994.10.08      | Город Волгоград, Волгоградская Область       |
| baranovaira@mail.ru | baranovaira@mail.ru          | Сатаева     | Ирина                             | Александровна |      79092871054 | 1984.08.23      | Город Нижний Новгород, Нижегородская Область |
| itam                | burlakova.marina@gmail.com   | Бурлакова   | Марина                            |               |      79039505764 | 1990.10.05      | Город Томск, Томская Область                 |
| rtyn-1985           | a.m.lisyutin@yandex.ru       | Лисютин     | Антон                             | Михайлович    |      79137723117 | 1985.09.27      | Город Новосибирск, Новосибирская Область     |
| imotoff             | imoto@list.ru                | Мелентьева  | Анна                              | Геннадьевна   |      79058206396 | 1985.06.14      | Город Тюмень, Тюменская Область              |
| Vanderloge          | dearjdancer@gmail.com        | Кислицин    | Михаил                            | Андреевич     |      79068237429 | 1987.05.16      | Город Тюмень, Тюменская Область              |
```


## About final data
> - Total rows: 9448970

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Data sample
```
| names                                  | emails                       | phones          | birth_date   | address                                         |
|:---------------------------------------|:-----------------------------|:----------------|:-------------|:------------------------------------------------|
| ['Письменова Анастасия Александровна'] | ['pismenova@gmail.com']      | ['79185941008'] |              |                                                 |
| ['Елена Гамалей Владимировна']         | ['lgamaley@mail.ru']         |                 |              |                                                 |
| ['Оглодина Наталия Викторовна']        | ['n_ogin@mail.ru']           | ['79161741456'] |              | ['Город Москва']                                |
| ['Андрюшин Владислав Олегович']        | ['v.andrushin@mail.ru']      | ['79270371407'] |              |                                                 |
| ['Войтенко Александр Эдуардович']      | ['alvo2000@mail.ru']         | ['79026037505'] |              | ['Город Челябинск Челябинская Область']         |
| ['Токарева Ольга Васильевна']          | ['azarova-helga@rambler.ru'] | ['79068224929'] |              | ['Город Тюмень Тюменская Область']              |
| ['Шарафутдинов Булат Эльфатович']      | ['bulat-sh8@yandex.ru']      | ['79274370728'] |              | ['Город Набережные Челны Республика Татарстан'] |
| ['Звягина Ольга']                      | ['ozvyagina@yotateam.com']   | ['79232280152'] |              |                                                 |
| ['Дорогина Елена']                     | ['lenysik1991d@yandex.ru']   |                 |              | ['Город Москва']                                |
| ['Фёдоров Сергей']                     | ['ffserega@yandex.ru']       |                 |              |                                                 |
| ['Никитин Владимир']                   | ['imitatordei@mail.ru']      |                 |              | ['Город Москва']                                |
| ['Штирц Людмила Вячеславовна']         | ['sobyanina_luda@mail.ru']   | ['79026392940'] |              | ['Город Соликамск Пермский Край']               |
| ['Ульянова Ольга Львовна']             | ['abra_kehdabra@mail.ru']    |                 |              |                                                 |
| ['Дунаев Сергей']                      | ['duno1477@rambler.ru']      |                 |              |                                                 |
| ['Юламанова Ильсияр']                  | ['ilsi21@mail.ru']           |                 |              |                                                 |
| ['Нисенгауз Наталья Давидовна']        | ['natkanisengauz@mail.ru']   | ['79108755856'] |              | ['Город Нижний Новгород Нижегородская Область'] |
| ['Егорова Евгения Кирилловна']         | ['eeniya@ya.ru']             | ['79267268352'] |              | ['Город Одинцово Московская Область']           |
| ['Тимашова Анна']                      | ['854@inbox.ru']             |                 |              | ['Город Ставрополь Ставропольский Край']        |
| ['Бобылев Николай Николаевич']         | ['nikolai-bjbylev@mail.ru']  | ['79039040770'] |              | ['Город Белокуриха Алтайский Край']             |
| ['Сенькова Марина Анатольевна']        | ['mainstream84@yandex.ru']   | ['79091769148'] |              | ['Город Курган Курганская Область']             |
```