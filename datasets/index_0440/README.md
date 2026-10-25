# Parsetron results

## About row data

> - Code name: index_0440
> - File path: osk-ins.ru (2023).txt
> - Total rows: 676173

### Schema
```
root
 |-- Почта: string (nullable = true)
 |-- Номер телефона: long (nullable = true)
 |-- ФИО: string (nullable = true)

```

### Data sample
```
| Почта                     |   Номер телефона | ФИО                            |
|:--------------------------|-----------------:|:-------------------------------|
| zzzzzzzzzzz201721@mail.ru |    nan           | Щербакова Юлия Александровна   |
| zzzzzzzzz540@mail.ru      |      7.98415e+10 |                                |
| zzzzzzz_1918@mail.ru      |    nan           | Политаев Михаил                |
| zzzzzmmmmm200328@mail.ru  |      7.90146e+10 | Троц Антон Михайлович          |
| zzzzz2022zzzzz@mail.ru    |      7.92444e+10 | Глушак Любовь Евгеньевна       |
| zzzzz2001@list.ru         |      7.9294e+10  |                                |
| zzzzz0rr0@yandex.ru       |      7.96332e+10 |                                |
| zzzzz0rr000@gmail.com     |      7.90066e+10 |                                |
| zzzzz-evgeniy-1986@bk.ru  |    nan           | Коровин Евгений                |
| zzzzqqwqwqwqw@bk.ru       |      7.96008e+10 | Абдурахманов Висита Махмудович |
| zzzzhuckoff@yandex.ru     |    nan           | Жуков Пётр Николаевич          |
| zzzzhdanov@yandex.ru      |      7.96124e+10 | ЖДАНОВ АЛЕКСАНДР ЕВГЕНЬЕВИЧ    |
| zzzzaur.1saev@yandex.ru   |      7.26551e+10 | Исаев Заур Магомедович         |
| zzzzapro@yandex.ru        |    nan           | Шахрудинов Шамиль Магомедович  |
| zzzz_zzz_17@mail.ru       |      7.92281e+10 | ЛЕОНОВ СЕРГЕЙ АНАТОЛЬЕВИЧ      |
| zzzz55op@yandex.ru        |      7.91762e+10 | Гришин Сергей Михайлович       |
| zzzz42@mail.ru            |      7.90391e+10 |                                |
| zzzz200773@mail.ru        |      7.93717e+10 | Плотников Михаил Александрович |
| zzzz111xxxx@mail.ru       |      7.98823e+10 | Гасанов Абдула Исрапилович     |
| zzzxumukzzz@gmail.com     |      7.98723e+10 | Парфёнов Владимир Леонидович   |
```


## About final data
> - Total rows: 566510

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
| Emails | 99.95% |
| Phones | 59.54% |



### Data sample
```
| names                                | emails                          | phones          |
|:-------------------------------------|:--------------------------------|:----------------|
| ['Журавлева Людмила Николаевна']     | ['zzjuravleva@yandex.ru']       | ['79649805867'] |
| ['Зулькарняева Руфия Иршатовна']     | ['zylryf@yandex.ru']            | ['79276130895'] |
| ['Величко Сергей Владимирович']      | ['zveli4cko@yandex.ru']         | ['79289074142'] |
| ['Зырянов Евгений Николаевич']       | ['zuriyanovevgenii@yandex.ru']  | ['79524589838'] |
| ['Ефимов Павел Владимрович']         | ['zumma-1@mail.ru']             | ['79501502460'] |
| ['Зубов Андрей Анатольевич']         | ['zubovaa@progress-it.ru']      | ['79277419607'] |
| ['Цырендоржиева Зоригма Витальевна'] | ['zts45hieva@yandex.ru']        | ['79097467238'] |
| ['Лян Чжэньго']                      | ['zs.iu@bk.ruf']                | ['79285858963'] |
| ['Зарипов Руслан Фанисович']         | ['zrf05121989@mail.ru']         | ['79879647309'] |
| ['Зозуля Кирилл Сергеевич']          | ['zozulya.kirilka@yandex.ru']   | ['79003392567'] |
| ['Кодзов Хадис Борисович']           | ['zowanvntgr@rover.info']       | ['79365070791'] |
| ['Зотя Василе']                      | ['zoteavasile888@gmail.com']    | ['79269240150'] |
| ['Козлова Любовь Викторовна']        | ['zorinaolga345@gmail.com']     | ['79276100192'] |
| ['Франчук Сергей Александрович']     | ['zoom_12072022-2@mail.ru']     | ['79842671473'] |
| ['Заидова Любовь Николаевна']        | ['zln12041991@mail.ru']         | ['79178247971'] |
| ['Максимов Владимир Станиславович']  | ['zimogomghd@fexpost.com']      | ['79183885631'] |
| ['Зимнухова Галина Александровна']   | ['zimnuhova_ga@mail.ru']        | ['79297140227'] |
| ['Бирючкова Марианна Юрьевна']       | ['zhurup@yandex.ru']            | ['79170167779'] |
| ['Придиус Анастасия Александровна']  | ['zhukanin86@mail.ru']          | ['79503807605'] |
| ['Дактанов Жоомарт Маматович']       | ['zhoomart.daktanov@yandex.ru'] | ['79751843520'] |
```