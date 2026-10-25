# Parsetron results

## About row data

> - Code name: index_0364
> - File path: клиенты_smarthome_rt_ru_12_2021.csv
> - Total rows: 680697

### Schema
```
root
 |-- Почта: string (nullable = true)
 |-- Телефон: long (nullable = true)
 |-- IP текущей авторизации: string (nullable = true)
 |-- IP последней авторизации: string (nullable = true)
 |-- ФИО: string (nullable = true)

```

### Data sample
```
| Почта                                        |     Телефон | IP текущей авторизации   | IP последней авторизации   | ФИО                                 |
|:---------------------------------------------|------------:|:-------------------------|:---------------------------|:------------------------------------|
| elena.feoktistova.08.08.2015kaktus@gmail.com | 79963460508 |                          |                            | Феоктистова Елена Дмитриевна        |
| aleksandr.konovalov.012345543210@gmail.com   | 79960192863 |                          |                            | Коновалов Александр Александрович   |
| nikitina.tatyana.nikolaevna1973@gmail.com    | 79156438737 |                          |                            | Никитина Татьяна Николаевна         |
| konstantin.petrovich.sidelnikov@gmail.com    | 79148116417 |                          |                            | Константин Сидельников Петрович     |
| aleksandr.musihin.qwerty7654321@gmail.com    | 79001210072 |                          |                            | Мусихин Александр Сергеевич         |
| sokolovantonyurevich27.6.1979@internet.ru    | 79003121998 |                          |                            | Соколов Антон Юрьевич               |
| ninichuk.vladimir.alexandrovich@gmail.com    | 79512206575 |                          |                            | Ниничук Владимир Александрович      |
| filatov.dmitrii.igorevich.1992@gmail.com     | 79185774710 |                          |                            | Филатов Дмитрий Игоревич            |
| kirill207207207207207207207207@gmail.com     | 79614896787 |                          |                            | Гукасян Ирина Сергеевна             |
| kristinavitalievnamarinina7654@gmail.com     | 79182103800 |                          |                            | Маринина Елена Александровна        |
| ekaterinalepitanova89002831027@gmail.com     | 79530955919 |                          |                            | Лепитанова Екатерина Александровна  |
| elizavetamelnikova-volkova1996@yandex.ru     | 79375946030 |                          |                            | Мельникова Елизавета Юрьевна        |
| vitkovskaya.vitkovskaya-natali@yandex.ru     | 79162640805 |                          |                            | Витковская Наталья Ринатовна        |
| halanskiy.andrey2019halanskiy@yandeks.ru     | 79186864556 |                          |                            | Халанский Андрей Александрович      |
| missis.samoilova-anastasia2016@yandex.ru     | 79611348218 |                          |                            | Самойлова Анастасия Дмитриевна      |
| novikoff161170-andrey.nowickov@yandex.ru     | 79156374704 | 212.3.130.183            | 95.158.255.174             | Новиков Андрей Сергеевич            |
| ivietatejinicaangelvkedahadida@gmail.com     | 79064094643 |                          |                            | Бряслова Варвара Андреевна          |
| xoliqov.muhammadyusufbarselona@gmail.com     | 79015153017 |                          |                            | Холиков Мухаммаюсуф Абдулхамид Угли |
| d.martinenko.dmitri.martinenko@gmail.com     | 79954031341 | 176.59.33.42             | 176.59.33.42               | Мартыненко Дмитрий Александрович    |
| drozhzhina.drozhzhinanatalya77@yandex.ru     | 79183799116 |                          |                            | Цыба Николай Васильевич             |
```


## About final data
> - Total rows: 678604

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: void (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.66% |
| Phones | 98.67% |
| Ips | 5.67% |



### Data sample
```
| names                                   | emails                                           | phones          | ips                                                                       |
|:----------------------------------------|:-------------------------------------------------|:----------------|:--------------------------------------------------------------------------|
| ['Феоктистова Елена Дмитриевна']        | ['elena.feoktistova.08.08.2015kaktus@gmail.com'] | ['79963460508'] |                                                                           |
| ['Коновалов Александр Александрович']   | ['aleksandr.konovalov.012345543210@gmail.com']   | ['79960192863'] |                                                                           |
| ['Никитина Татьяна Николаевна']         | ['nikitina.tatyana.nikolaevna1973@gmail.com']    | ['79156438737'] |                                                                           |
| ['Константин Сидельников Петрович']     | ['konstantin.petrovich.sidelnikov@gmail.com']    | ['79148116417'] |                                                                           |
| ['Мусихин Александр Сергеевич']         | ['aleksandr.musihin.qwerty7654321@gmail.com']    | ['79001210072'] |                                                                           |
| ['Соколов Антон Юрьевич']               | ['sokolovantonyurevich27.6.1979@internet.ru']    | ['79003121998'] |                                                                           |
| ['Ниничук Владимир Александрович']      | ['ninichuk.vladimir.alexandrovich@gmail.com']    | ['79512206575'] |                                                                           |
| ['Филатов Дмитрий Игоревич']            | ['filatov.dmitrii.igorevich.1992@gmail.com']     | ['79185774710'] |                                                                           |
| ['Гукасян Ирина Сергеевна']             | ['kirill207207207207207207207207@gmail.com']     | ['79614896787'] |                                                                           |
| ['Маринина Елена Александровна']        | ['kristinavitalievnamarinina7654@gmail.com']     | ['79182103800'] |                                                                           |
| ['Лепитанова Екатерина Александровна']  | ['ekaterinalepitanova89002831027@gmail.com']     | ['79530955919'] |                                                                           |
| ['Мельникова Елизавета Юрьевна']        | ['elizavetamelnikova-volkova1996@yandex.ru']     | ['79375946030'] |                                                                           |
| ['Витковская Наталья Ринатовна']        | ['vitkovskaya.vitkovskaya-natali@yandex.ru']     | ['79162640805'] |                                                                           |
| ['Халанский Андрей Александрович']      | ['halanskiy.andrey2019halanskiy@yandeks.ru']     | ['79186864556'] |                                                                           |
| ['Самойлова Анастасия Дмитриевна']      | ['missis.samoilova-anastasia2016@yandex.ru']     | ['79611348218'] |                                                                           |
| ['Новиков Андрей Сергеевич']            | ['novikoff161170-andrey.nowickov@yandex.ru']     | ['79156374704'] | [Row(ip='212.3.130.183', date=None), Row(ip='95.158.255.174', date=None)] |
| ['Бряслова Варвара Андреевна']          | ['ivietatejinicaangelvkedahadida@gmail.com']     | ['79064094643'] |                                                                           |
| ['Холиков Мухаммаюсуф Абдулхамид Угли'] | ['xoliqov.muhammadyusufbarselona@gmail.com']     | ['79015153017'] |                                                                           |
| ['Мартыненко Дмитрий Александрович']    | ['d.martinenko.dmitri.martinenko@gmail.com']     | ['79954031341'] | [Row(ip='176.59.33.42', date=None)]                                       |
| ['Цыба Николай Васильевич']             | ['drozhzhina.drozhzhinanatalya77@yandex.ru']     | ['79183799116'] |                                                                           |
```