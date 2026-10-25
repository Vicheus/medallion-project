# Parsetron results

## About row data

> - Code name: index_0261
> - File path: /media/user/SAMSUNG/Databases/index_0261/raw/utair_ru.csv
> - Total rows: 522459

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- Телефон (норм): string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Паспорт / ID: decimal(21,0) (nullable = true)
 |-- documents1: string (nullable = true)
 |-- documents0: string (nullable = true)
 |-- Адрес (город): string (nullable = true)
 |-- Адрес (регион): string (nullable = true)
 |-- Адрес (страна): string (nullable = true)
 |-- Адрес (улица, дом): string (nullable = true)
 |-- _c11: string (nullable = true)

```

### Data sample
```
| ФИО                                  | Email                        |   Телефон (норм) | Дата рождения   |   Паспорт / ID | documents1   | documents0   | Адрес (город)      | Адрес (регион)   | Адрес (страна)   | Адрес (улица, дом)                       | _c11   |
|:-------------------------------------|:-----------------------------|-----------------:|:----------------|---------------:|:-------------|:-------------|:-------------------|:-----------------|:-----------------|:-----------------------------------------|:-------|
| Бельская Ольга Александровна         | belskaya.olga84@yandex.ru    |      79028199010 | 01.06.1984      |    6.70992e+09 |              |              | Ханты-Мансийск     |                  | RUS              | Строителей Д.105А, кв 8                  |        |
| Dobyko Alena Aleksandrovna           |                              |      79110204439 | 02.07.1988      |                |              |              |                    |                  |                  |                                          |        |
| Белкина Ольга Вячеславовна           | squirrel7887@icloud.com      |      79154600817 | 15.02.1980      |                |              |              |                    |                  |                  |                                          |        |
| Обозный Василий Анатольевич          | vasyao@mail.ru               |                  | 01.07.1975      |                |              |              |                    |                  |                  |                                          |        |
| Kushnarev Aleksei                    | as89262505180@gmail.com      |      79262505180 | 06.05.1982      |                |              |              |                    |                  |                  |                                          |        |
| Брылёва Анастасия Сергеевна          | abryleva9119171707@gmail.com |      79119171707 | 28.09.1988      |                |              |              | г Санкт-Петербург  |                  | RUS              | ул. Пулковская, д. 11                    |        |
| Куприяшкина Ирина Владимировна       | iren-med@yandex.ru           |      79108890102 | 20.07.1979      |                |              |              |                    |                  |                  |                                          |        |
| Витяев Михаил Павлович               | mihailvityaev@inbox.ru       |      79687950573 | 09.01.1991      |                |              |              |                    |                  |                  |                                          |        |
| Залесский Евгений Владиславович      | jekanefteks@mail.ru          |      79054125363 | 04.07.1968      |                |              |              |                    |                  |                  |                                          |        |
| Осетрова Ирина Андреевна             | arina-petrova-73@mail.ru     |      79197509952 | 17.08.1969      |                |              |              | г Минеральные Воды |                  | RUS              | Минераловодский р-н, ул. Пушкина, д. 103 |        |
| Орпанен Анжела                       | angela@orpanen.ru            |                  | 10.04.1967      |                |              |              |                    |                  |                  |                                          |        |
| Орлова Веста                         | vestik585@gmail.com          |                  | 05.09.1985      |                |              |              |                    |                  |                  |                                          |        |
| Гаджимирзаев Джамалудин Зиябутинович | jamal216@mail.ru             |      79266666774 | 21.06.1995      |                |              |              |                    |                  |                  |                                          |        |
| Хачатрян Мартун Арамович             |                              |      79031422266 | 07.03.1952      |                |              |              |                    |                  |                  |                                          |        |
| Идрисова Елена Николаевна            |                              |      79604304613 | 02.12.1986      |                |              |              |                    |                  |                  |                                          |        |
| Maamieva Saadet                      | alesker@inbox.ru             |      79688842040 | 27.12.1993      |                |              |              |                    |                  |                  |                                          |        |
| Фадеева Наталья Александровна        | fadeevana@mail.ru            |      79256683208 | 26.12.1976      |                |              |              | г Москва           |                  | RUS              | ул. Академика Комарова, д. 1А, кв. 48    |        |
| Нугуманов Ильдар Хазинурович         |                              |      79659236219 | 16.09.1994      |                |              |              |                    |                  |                  |                                          |        |
| Burda Yegor                          | burdayegor@gmail.com         |      79152868934 | 15.09.1994      |                |              |              |                    |                  |                  |                                          |        |
| Дрокова Елизавета Евгеньевна         | liza-drokova@mail.ru         |      79645112224 | 17.02.1997      |                |              |              |                    |                  |                  |                                          |        |
```


## About final data
> - Total rows: 506218

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)

```

### Data sample
```
| names                                    | phones          | emails                           | birth_date   | address                                                           | documents                                                                                                                 |
|:-----------------------------------------|:----------------|:---------------------------------|:-------------|:------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| ['Бельская Ольга Александровна']         | ['79028199010'] | ['belskaya.olga84@yandex.ru']    | 01.06.1984   | ['RUS Ханты-Мансийск Строителей Д.105А кв 8']                     | [Row(type=0, serial='6709922852', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| ['Dobyko Alena Aleksandrovna']           | ['79110204439'] |                                  | 02.07.1988   |                                                                   |                                                                                                                           |
| ['Белкина Ольга Вячеславовна']           | ['79154600817'] | ['squirrel7887@icloud.com']      | 15.02.1980   |                                                                   |                                                                                                                           |
| ['Обозный Василий Анатольевич']          |                 | ['vasyao@mail.ru']               | 01.07.1975   |                                                                   |                                                                                                                           |
| ['Kushnarev Aleksei']                    | ['79262505180'] | ['as89262505180@gmail.com']      | 06.05.1982   |                                                                   |                                                                                                                           |
| ['Брылёва Анастасия Сергеевна']          | ['79119171707'] | ['abryleva9119171707@gmail.com'] | 28.09.1988   | ['RUS г Санкт-Петербург ул. Пулковская д. 11']                    |                                                                                                                           |
| ['Куприяшкина Ирина Владимировна']       | ['79108890102'] | ['iren-med@yandex.ru']           | 20.07.1979   |                                                                   |                                                                                                                           |
| ['Витяев Михаил Павлович']               | ['79687950573'] | ['mihailvityaev@inbox.ru']       | 09.01.1991   |                                                                   |                                                                                                                           |
| ['Залесский Евгений Владиславович']      | ['79054125363'] | ['jekanefteks@mail.ru']          | 04.07.1968   |                                                                   |                                                                                                                           |
| ['Осетрова Ирина Андреевна']             | ['79197509952'] | ['arina-petrova-73@mail.ru']     | 17.08.1969   | ['RUS г Минеральные Воды Минераловодский р-н ул. Пушкина д. 103'] |                                                                                                                           |
| ['Орпанен Анжела']                       |                 | ['angela@orpanen.ru']            | 10.04.1967   |                                                                   |                                                                                                                           |
| ['Орлова Веста']                         |                 | ['vestik585@gmail.com']          | 05.09.1985   |                                                                   |                                                                                                                           |
| ['Гаджимирзаев Джамалудин Зиябутинович'] | ['79266666774'] | ['jamal216@mail.ru']             | 21.06.1995   |                                                                   |                                                                                                                           |
| ['Хачатрян Мартун Арамович']             | ['79031422266'] |                                  | 07.03.1952   |                                                                   |                                                                                                                           |
| ['Идрисова Елена Николаевна']            | ['79604304613'] |                                  | 02.12.1986   |                                                                   |                                                                                                                           |
| ['Maamieva Saadet']                      | ['79688842040'] | ['alesker@inbox.ru']             | 27.12.1993   |                                                                   |                                                                                                                           |
| ['Фадеева Наталья Александровна']        | ['79256683208'] | ['fadeevana@mail.ru']            | 26.12.1976   | ['RUS г Москва ул. Академика Комарова д. 1А кв. 48']              |                                                                                                                           |
| ['Нугуманов Ильдар Хазинурович']         | ['79659236219'] |                                  | 16.09.1994   |                                                                   |                                                                                                                           |
| ['Burda Yegor']                          | ['79152868934'] | ['burdayegor@gmail.com']         | 15.09.1994   |                                                                   |                                                                                                                           |
| ['Дрокова Елизавета Евгеньевна']         | ['79645112224'] | ['liza-drokova@mail.ru']         | 17.02.1997   |                                                                   |                                                                                                                           |
```