# Parsetron results

## About row data

> - Code name: index_0216
> - File path: /media/user/SAMSUNG/Databases/index_0216/raw/astrovolga.ru.csv
> - Total rows: 1546121

### Schema
```
root
 |-- Почта: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- Роль: string (nullable = true)
 |-- Адрес: string (nullable = true)
 |-- Дата рождения: string (nullable = true)

```

### Data sample
```
| Почта                          | ФИО                              |   Номер телефона | Роль           | Адрес                                                                                | Дата рождения   |
|:-------------------------------|:---------------------------------|-----------------:|:---------------|:-------------------------------------------------------------------------------------|:----------------|
| CABINET_PARTNER                | CABINET_PARTNER                  |                  | administrator  |                                                                                      |                 |
| 123                            | 123                              |              123 | 123            |                                                                                      |                 |
| admin                          | admin                            |                  | administrator  |                                                                                      |                 |
| Agent                          | Agent                            |                  | ucsbot         | Самарская обл, Ставропольский р-н, село Ягодное                                      |                 |
| Agent2                         | Agent2                           |                  | administrator  |                                                                                      |                 |
| Balzer1@mail.ru_263            | Иван Сергеевич                   |      79277428387 | administrator  |                                                                                      |                 |
| oav@ads-soft.ru                | Ойнус Александр                  |                  | external       |                                                                                      |                 |
| lvoval@ads-soft.ru             | Львов Александр                  |                  | external       |                                                                                      |                 |
| test@astro-volga.ru            | Иванов Иван Иванович             |      79151234567 | operator       |                                                                                      |                 |
| KolesnikovaE_273               | Агенты                           |                  | operator.input |                                                                                      |                 |
| Call_Center_274                | Call_Center                      |                  | administrator  |                                                                                      |                 |
| Kolesnikova                    | Колесникова Е.А.                 |                  | administrator  |                                                                                      |                 |
| Haliullina                     | Халиуллина А.Я.                  |                  | administrator  | 443084, Самарская обл, Самара г, Ново-Вокзальная ул, дом № 217, квартира 191         |                 |
| kiv@poveren.biz                | ИП Коршикова Ирина Владимировна  |                  | administrator  | 170518, Тверская обл, Калининский р-н, Кривцово д, дом № 27                          |                 |
| magazin@poveren.biz_278        | Стеблин Евгений Александрович    |      79014883506 | operator       | г Тверь, пр-кт Ленина                                                                |                 |
| dobrovolka@poveren.biz_279     | Ксенофонтова Кристина Алексеевна |      79014883506 | operator       | г Тверь, пр-кт Ленина, д 2                                                           |                 |
| olgakrylova.tver@yandex.ru_290 | Крылова Ольга Борисовна          |      79014883506 | operator       | г Тверь                                                                              |                 |
| ser-broshan@bk.ru              | Брощан Геннадий Петрович         |      79014883506 | operator       | Тверская обл, г Лихославль, ул Советская, д 49                                       |                 |
| NLPozin@mail.ru                | Позина Светлана Владимировна     |                  | operator       | 172840, Тверская обл, Торопецкий р-н, Торопец г, Карла Маркса ул, дом № 44, корпус 3 |                 |
| nbsk-bologoe@mail.ru_293       | Курушин Денис                    |      79014883506 | operator       | Тверская обл, г Бологое                                                              |                 |
```


## About final data
> - Total rows: 1279370

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
 |-- birth_date: string (nullable = true)

```

### Data sample
```
| names                                | phones   | emails                                  | address                                                                                         | birth_date   |
|:-------------------------------------|:---------|:----------------------------------------|:------------------------------------------------------------------------------------------------|:-------------|
| ['Абакумов Артур Сергеевич']         |          | ['vfapfu@bk.ru']                        |                                                                                                 |              |
| ['Абакумов Валерий']                 |          | ['bratenkina@astrovolga.ru']            | ['445044 Россия Самарская обл г Тольятти Автозаводский р-н ул Автостроителей д 54 кв 100']      |              |
| ['Абанин Борис']                     |          | ['vekghina_ylia@mail.ru']               | ['Россия 601545 Владимирская обл Гусь-Хрустальный р-н разъезд Золотковский ул Пионерская д 23'] |              |
| ['Абанкин Александр']                |          | ['omega162@mail.ru']                    | ['Россия 390026 Рязанская обл г Рязань ул Стройкова д 25 кв 129']                               |              |
| ['Абанов Дмитрий']                   |          | ['menayshkina@magns.ru']                | ['Россия 390044 Рязанская обл г Рязань ул Великанова д 12 к 1 кв 31']                           |              |
| ['Абаньков Николай']                 |          | ['fbghtjh@mail.ru']                     | ['446858 Россия Самарская обл Челно-Вершинский р-н село Девлезеркино ул Лесная д 5 кв 2']       |              |
| ['Абасов Тигран Даниялович']         |          | ['egooxu@mailto.plus']                  |                                                                                                 |              |
| ['Абатаев Абдул-Малик Ахмадович']    |          | ['uwvab74@mailto.plus']                 |                                                                                                 |              |
| ['Абатова Айман']                    |          | ['kamzeeva.palmira@mail.ru']            | ['461980 Россия Оренбургская обл Первомайский р-н поселок Первомайский ул Мирная д 16 кв 7']    |              |
| ['Абашев Ильяс Исмагильевич']        |          | ['ilyasabashev8@gmail.com']             |                                                                                                 |              |
| ['Аббасмирзоев Новрузбек Дамирович'] |          | ['novruzbeg.kuysun.74@mail.ru']         |                                                                                                 |              |
| ['Аббасов Дунямалы Агамалы Оглы']    |          | ['gsvbsbsnsn@mail.ru']                  |                                                                                                 |              |
| ['Абдеев Вахив']                     |          | ['bachmanowa@yandex.ru']                | ['Россия 446015 Самарская обл г Сызрань ул Нахимова д 13 кв 40']                                |              |
| ['Абдраманов Джафер']                |          | ['dema2662@mail.ru']                    | ['296162 Россия респ Крым Джанкойский р-н село Чайкино ул Сивашская д 12']                      |              |
| ['Абдрахимов Ильнур']                |          | ['shanhai45@mail.ru']                   | ['Россия 641089 Курганская обл Сафакулевский р-н деревня Максимовка ул Братьев Михолап д 16']   |              |
| ['Абдрязяков Руслан Надирович']      |          | ['bilevo6629@agrolivana.com']           |                                                                                                 |              |
| ['Абдукеримов Ырысбек Муктарович']   |          | ['kerimsbek@mail.ru']                   |                                                                                                 |              |
| ['Абдулаев Ахмед Лабазанович']       |          | ['ukpr1@inbox.ru']                      |                                                                                                 |              |
| ['Абдулаев Магомед Алимович']        |          | ['maomedabdulayev94-94-94gogo@mail.ru'] |                                                                                                 |              |
| ['Абдулаева Ашура Магомедовна']      |          | ['mhj.an.ua.ry.2023@gmail.com']         |                                                                                                 |              |
```