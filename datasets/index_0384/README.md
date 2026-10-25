# Parsetron results

## About row data

> - Code name: index_0384
> - File path: sport-marafon.ru (04.2023).txt
> - Total rows: 340072

### Schema
```
root
 |-- Имя: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Социальная сеть: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- Адрес: string (nullable = true)
 |-- Дата рождения: string (nullable = true)

```

### Data sample
```
| Имя                        | Почта                      | Социальная сеть                          |   Номер телефона | Адрес                                     | Дата рождения   |
|:---------------------------|:---------------------------|:-----------------------------------------|-----------------:|:------------------------------------------|:----------------|
| Вершинин Вячеслав Петрович | photovvp@yandex.ru         |                                          |      79028581296 |                                           |                 |
| Павел                      | poninpaul@mail.ru          |                                          |      79031882200 |                                           |                 |
| Hermosaqcw                 | fjptly009+def012@gmail.com |                                          |                  |                                           |                 |
| Александр                  | muratov71@mail.ru          |                                          |                  |                                           |                 |
| Звонцов Алексей            | zvo@inbox.ru               |                                          |      79025566323 |                                           |                 |
| Биккулова Алена Сергеевна  | bikkulova@bk.ru            |                                          |      79262691921 |                                           |                 |
| Перфильев Алексей Юрьевич  | moscow2006@gmail.com       |                                          |      79162014984 | Пресненская наб. 10 блок С                |                 |
| Лукина Ольга Николаевна    | olay393@mail.ru            |                                          |      79265662980 | Спортивная 38 17                          |                 |
| Нина                       | usmanovanine@yandex.ru     | http://www.facebook.com/214933189433198  |                  |                                           |                 |
| Елена                      | balerina@inbox.ru          |                                          |      79150175644 |                                           |                 |
| Никита Шмырёв              | nikita.shmyrev@yandex.ru   |                                          |      74993482409 |                                           |                 |
| Алексей                    | andronov.a@icloud.com      |                                          |      79037897540 |                                           |                 |
| Ларкина Ольга Анатольевна  | larkina.olga75@gmail.com   |                                          |      79776288412 | 1ый нагатинский проезд д.11 корп.2 кв.531 |                 |
| Геннадий Лысов             | gennadiy.lysov@bigmir.net  |                                          |      74996772342 |                                           |                 |
| вася                       | ggggggg@yandex.ru          |                                          |                  |                                           |                 |
| Казнадий Иван Владимирович | ikaznady@gmail.com         |                                          |      79246796543 |                                           |                 |
| Артур Гайдуков             | artur.gaydukov@yandex.ru   |                                          |      74994033496 |                                           |                 |
| Евгения                    | redberre@gmail.com         |                                          |      79268760821 |                                           | 1986.07.21      |
| Anna                       | annafome@gmail.com         | http://www.facebook.com/1315498065253180 |                  |                                           |                 |
| Болотов Павел Сергеевич    | rock_n_roll_star@mail.ru   |                                          |      79312647411 | Московский пр д.91 оф.702                 |                 |
```


## About final data
> - Total rows: 318683

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 10.19% |
| Phones | 83.77% |
| Emails | 99.34% |
| Address | 26.66% |
| Socials | 2.93% |



### Data sample
```
| names                                 | birth_date   | phones          | emails                           | address                                                        | socials                                                                                         |
|:--------------------------------------|:-------------|:----------------|:---------------------------------|:---------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| ['Кафтанов Валерий Валентинович']     | 21.10.1971   | ['79606719285'] | ['izobnovret@mail.ru']           |                                                                |                                                                                                 |
| ['Смирнов Александр Павлович']        |              | ['79207454106'] | ['karel2211@mail.ru']            | ['Сегодня пр-т маршала Жукова 75 стр 1. Участок ТСБ Гормост.'] |                                                                                                 |
| ['Сергей Колосов']                    |              | ['74994040295'] | ['sergey.kolosov@gmail.com']     |                                                                |                                                                                                 |
| ['Юрченков Олег Михайлович']          |              | ['79519136499'] | ['oleg20061964@mail.ru']         |                                                                |                                                                                                 |
| ['Антонина']                          |              | ['79150984067'] | ['davydko.a@mail.ru']            |                                                                |                                                                                                 |
| ['Кирилл']                            |              | ['79653004500'] | ['popykhov@gmail.com']           |                                                                |                                                                                                 |
| ['Фазлуктинова Александра Радиковна'] | 25.08.1999   | ['79148780038'] | ['nyankosesnei@gmail.com']       |                                                                |                                                                                                 |
| ['Dmitry Rusakov']                    |              | ['79645667762'] | ['travels.chronicles@gmail.com'] |                                                                |                                                                                                 |
| ['Петр Лавров']                       |              | ['79654059742'] | ['petrlavrov@inbox.ru']          | ['Новохохловская улица 23 с1 бизнес центр']                    |                                                                                                 |
| ['Белогрудов Дмитрий Леонидович']     |              | ['79147096462'] | ['fomichu@mail.ru']              |                                                                |                                                                                                 |
| ['Григорий']                          | 19.08.1972   | ['79151875055'] | ['grigorykozlov@mail.ru']        |                                                                |                                                                                                 |
| ['Кондрашкин Андрей Геннадиевич']     |              | ['79788033710'] | ['kondr714a@gmail.com']          | ['60 лет СССР д.7 кв.3']                                       |                                                                                                 |
| ['Реутов Сергей Сергеевич']           | 06.10.1978   | ['79247828000'] | ['dja_kamchatka@mail.ru']        |                                                                |                                                                                                 |
| ['Зуев Олег Борисович']               |              | ['79600702295'] | ['fisher.pike@mail.ru']          | ['проспект Хасана Туфана д.30 кв.49']                          |                                                                                                 |
| ['Куликова Татьяна Олеговна']         |              | ['79164811409'] | ['tania.84@list.ru']             |                                                                |                                                                                                 |
| ['Гриша Машинский']                   |              | ['79687320092'] | ['spacewolf59@gmail.com']        |                                                                |                                                                                                 |
| ['Elena']                             |              |                 | ['gmalven@gmail.com']            |                                                                | [Row(title='Facebook', id=None, link='http://www.facebook.com/1893240030765901', comment=None)] |
| ['Александр Ак']                      |              | ['79169395980'] | ['pticacondor@yandex.ru']        | ['Мск Потаповский Пер 10 48']                                  |                                                                                                 |
| ['Антон']                             |              | ['79255069782'] | ['anton.doronin@mail.ru']        |                                                                |                                                                                                 |
| ['Студенков Александр Викторович']    | 13.06.1984   |                 | ['jamn@mail.ru']                 |                                                                |                                                                                                 |
```