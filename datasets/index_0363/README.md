# Parsetron results

## About row data

> - Code name: index_0363
> - File path: клиенты_voen_torg_ru.csv
> - Total rows: 31904

### Schema
```
root
 |-- Имя: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Телефон: string (nullable = true)

```

### Data sample
```
| Имя                          | Фамилия                    | Почта                         |     Телефон |
|:-----------------------------|:---------------------------|:------------------------------|------------:|
| Юлия Тимергалиева Наубатовна |                            | Juliana_13j@mail.ru           | 79224648339 |
| МаринаАлександровна Бегичева |                            | mar303@yandex.ru              |             |
| Самойлов Андрей Вячеславович |                            | camandv@mail.ru               | 78952074307 |
| Людмила Сергеевна Петровская |                            | kaizer2077@yandex.ru          |             |
| Ильинский Михаил Геннадиевич |                            | ilinskiy95@mail.ru            | 79118225380 |
| киргетов александр петрович  |                            | saha.kirgetov@yandex.ru       |             |
| Татьяна Петровна Мартьянова  |                            | Tatyana200814@yandex.ru       | 79619614967 |
| Назаров Сергей Владимирович  |                            | snazarov1975@mail.ru          | 79169585746 |
| Капустин Аркадий Борисович   | Капустин                   | Barbrady83@yandex.ru          | 79093621073 |
| Кирилл Сергеевич Грошенков   |                            | kirsg@yandex.ru               |             |
| Киселева Елена Анатольевна   | Киселева Елена Анатольевна | damka-210783@mail.ru          | 79028144934 |
| Соколова Мария Геннадьевна   | 45 03 495 391              | mashuk2307@yandex.ru          | 79262319297 |
| Сергеева-Шукшина Виолетта    | Алексеевна                 | 03447681@mail.ru              | 79777830940 |
| Спецобъединение Юго Запад    |                            | tlazareva@spets.ru            | 79152600514 |
| ходыкин Владимир егорович    |                            | wladimir.xodiki@qmail.com     | 79237463620 |
| Виктор Михайлович Маленко    |                            | viktor_malenko@mail.ru        |             |
| Александра Александровна     | Бедрова                    | mironov-bedrova@yandex.ru     | 79778871547 |
| Владимир Шумилов Шумилов     |                            | shumilovvladimirinn@yandex.ru |             |
| тертычный юрий федорович     | Тертычный                  | вичfor.georg@yandex.ru        |             |
| Благовещенскова Вероника     | Владимировна               | blagoveshenskova@mail.ru      | 79050635660 |
```


## About final data
> - Total rows: 28660

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.50% |
| Phones | 74.81% |



### Data sample
```
| names                                     | emails                            | phones          |
|:------------------------------------------|:----------------------------------|:----------------|
| ['Юлия Тимергалиева Наубатовна']          | ['juliana_13j@mail.ru']           | ['79224648339'] |
| ['Маринаалександровна Бегичева']          | ['mar303@yandex.ru']              |                 |
| ['Самойлов Андрей Вячеславович']          | ['camandv@mail.ru']               |                 |
| ['Людмила Сергеевна Петровская']          | ['kaizer2077@yandex.ru']          |                 |
| ['Ильинский Михаил Геннадиевич']          | ['ilinskiy95@mail.ru']            | ['79118225380'] |
| ['Киргетов Александр Петрович']           | ['saha.kirgetov@yandex.ru']       |                 |
| ['Татьяна Петровна Мартьянова']           | ['tatyana200814@yandex.ru']       | ['79619614967'] |
| ['Назаров Сергей Владимирович']           | ['snazarov1975@mail.ru']          | ['79169585746'] |
| ['Капустин Капустин Аркадий Борисович']   | ['barbrady83@yandex.ru']          | ['79093621073'] |
| ['Кирилл Сергеевич Грошенков']            | ['kirsg@yandex.ru']               |                 |
| ['Киселева Елена Анатольевна']            | ['damka-210783@mail.ru']          | ['79028144934'] |
| ['Алексеевна Сергеева-Шукшина Виолетта']  | ['03447681@mail.ru']              | ['79777830940'] |
| ['Спецобъединение Юго Запад']             | ['tlazareva@spets.ru']            | ['79152600514'] |
| ['Ходыкин Владимир Егорович']             | ['wladimir.xodiki@qmail.com']     | ['79237463620'] |
| ['Виктор Михайлович Маленко']             | ['viktor_malenko@mail.ru']        |                 |
| ['Бедрова Александра Александровна']      | ['mironov-bedrova@yandex.ru']     | ['79778871547'] |
| ['Владимир Шумилов Шумилов']              | ['shumilovvladimirinn@yandex.ru'] |                 |
| ['Владимировна Благовещенскова Вероника'] | ['blagoveshenskova@mail.ru']      | ['79050635660'] |
| ['Гудков Гудков Сергей Витальевич']       | ['advokatgudkov@yandex.ru']       | ['79139161632'] |
| ['Леонидов Юрий Георгиевич']              | ['breiz@yandex.ru']               | ['79166266866'] |
```