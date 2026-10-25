# Parsetron results

## About row data

> - File path: клиенты_osp_ru.csv
> - Total rows: 134221

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Телефон: string (nullable = true)
 |-- Должность: string (nullable = true)
 |-- Компания: string (nullable = true)

```

### Data sample
```
| ФИО                              | Почта                            | Телефон         | Должность                         | Компания                                                                                |
|:---------------------------------|:---------------------------------|:----------------|:----------------------------------|:----------------------------------------------------------------------------------------|
| Хворостов Александр Евгеньевич   | khvorostov@gmail.com             |                 | Аналитик                          |                                                                                         |
| Толмачев Владимир Павлович       | LSergeeva@tul.fsgs.ru            |                 | Аналитик                          | Территориальный Орган Федеральной Службы Государственной Статистики По Тульской Области |
| Жижин Максим                     | mail@fomsrt.ru                   |                 | Аналитик                          | Гу территориальный Фонд Обязательного Медицинского Страхования Республики Татарстан     |
| Антониади Людлмила Леонидовна    | kfs_all6@mail.ru                 | 77059776777     | <blank>                           |                                                                                         |
| Струнникова Ольга Евгеньевна     | olia.strunnikova@yandex.ru       | 79103923498     | Учитель Русского Языка Литературы | Мбоу Школа 7                                                                            |
| Долотов Алексей Александрович    | alexey.dolotov@pvc.ru            |                 | Аналитик                          | Ооо агентство Маркетинговых Коммуникаций                                                |
| Постика Анастасия                | pr@spbcioclub.ru                 |                 | Аналитик                          | Санкт-петербургский Клуб Ит-директоров spb Cio Club                                     |
| Мукашова Жаркынай Советбековна   | jmukashova@nbkr.kg               |                 | Аналитик                          | Национальный Банк Кыргызской Республики                                                 |
| Буланкин Валерий Борисович       | bulankin@mail.ru                 |                 | <blank>                           | Владимирский Государственный Университет                                                |
| Киселев Александр Александрович" | info@remer.su                    |                 | Аналитик                          | Ооо производственная Группа Ремер                                                       |
| Кудря Елена Петровна             | main@uralfd.ru                   |                 | Аналитик                          | Оао Коммерческий Банк Уральский Финансовый Дом                                          |
| Киселев Александр Александрович  | aleksandr.kiselev@remergroup.ru  |                 | Аналитик                          | Ооо производственная Группа Ремер                                                       |
| Ярченко Татьяна Михайловна       | kinzyagulova@list.ru             | 79228716516     | <blank>                           |                                                                                         |
| Орлова Светлана Павловна"        | orlova@smartfg.com               |                 | Аналитик                          | Зао совместное Предприятие евразия М4                                                   |
| Сорокин Олег Игоревич            | Oleg.Sorokin@nordea.ru           |                 | Аналитик                          | Оао Нордеа Банк Санкт-петербургский Филиал                                              |
| Драницына Ольга Михайловна       | olga.dranitsyna@mbr.ru           |                 | Аналитик                          | Зао Кб международный Банк Развития                                                      |
| Сенцов Андрей Сергеевич          | it@chtpz.ru                      |                 | Аналитик                          | Оао Челябинский Трубопрокатный Завод                                                    |
| Орлов Василий Александрович      | bug_itc_@esoo.ru                 |                 | Аналитик                          | Ооо Инженерно-технический Центр                                                         |
| Надежда Овчаренко                | nadezhda.ovcharenko@grayling.com | (495)788-6784   | <blank>                           | Cветлана Чижкова -директор По Маркетингу                                                |
| Андрияшин Михаил                 | secretary2@akvion.ru             | (495) 780-72-34 | Директор по ИТ (CIO)              |                                                                                         |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
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
| Emails | 99.78% |
| Phones | 36.00% |
| Works | 99.91% |



### Data sample
```
| names                               | emails                               | phones          | works                                                                                                                                                                                 |
|:------------------------------------|:-------------------------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Хворостов Александр Евгеньевич']  | ['khvorostov@gmail.com']             |                 | [Row(post='Аналитик', date_start=None, date_end=None, company=None, address=None, comment=None)]                                                                                      |
| ['Толмачев Владимир Павлович']      | ['lsergeeva@tul.fsgs.ru']            |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Территориальный Орган Федеральной Службы Государственной Статистики По Тульской Области', address=None, comment=None)] |
| ['Жижин Максим']                    | ['mail@fomsrt.ru']                   |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Гу территориальный Фонд Обязательного Медицинского Страхования Республики Татарстан', address=None, comment=None)]     |
| ['Антониади Людлмила Леонидовна']   | ['kfs_all6@mail.ru']                 |                 | [Row(post='blank', date_start=None, date_end=None, company=None, address=None, comment=None)]                                                                                         |
| ['Струнникова Ольга Евгеньевна']    | ['olia.strunnikova@yandex.ru']       | ['79103923498'] | [Row(post='Учитель Русского Языка Литературы', date_start=None, date_end=None, company='Мбоу Школа 7', address=None, comment=None)]                                                   |
| ['Долотов Алексей Александрович']   | ['alexey.dolotov@pvc.ru']            |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Ооо агентство Маркетинговых Коммуникаций', address=None, comment=None)]                                                |
| ['Постика Анастасия']               | ['pr@spbcioclub.ru']                 |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Санкт-петербургский Клуб Ит-директоров spb Cio Club', address=None, comment=None)]                                     |
| ['Мукашова Жаркынай Советбековна']  | ['jmukashova@nbkr.kg']               |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Национальный Банк Кыргызской Республики', address=None, comment=None)]                                                 |
| ['Буланкин Валерий Борисович']      | ['bulankin@mail.ru']                 |                 | [Row(post='blank', date_start=None, date_end=None, company='Владимирский Государственный Университет', address=None, comment=None)]                                                   |
| ['Киселев Александр Александрович'] | ['info@remer.su']                    |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Ооо производственная Группа Ремер', address=None, comment=None)]                                                       |
| ['Кудря Елена Петровна']            | ['main@uralfd.ru']                   |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Оао Коммерческий Банк Уральский Финансовый Дом', address=None, comment=None)]                                          |
| ['Киселев Александр Александрович'] | ['aleksandr.kiselev@remergroup.ru']  |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Ооо производственная Группа Ремер', address=None, comment=None)]                                                       |
| ['Ярченко Татьяна Михайловна']      | ['kinzyagulova@list.ru']             | ['79228716516'] | [Row(post='blank', date_start=None, date_end=None, company=None, address=None, comment=None)]                                                                                         |
| ['Орлова Светлана Павловна']        | ['orlova@smartfg.com']               |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Зао совместное Предприятие евразия М4', address=None, comment=None)]                                                   |
| ['Сорокин Олег Игоревич']           | ['oleg.sorokin@nordea.ru']           |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Оао Нордеа Банк Санкт-петербургский Филиал', address=None, comment=None)]                                              |
| ['Драницына Ольга Михайловна']      | ['olga.dranitsyna@mbr.ru']           |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Зао Кб международный Банк Развития', address=None, comment=None)]                                                      |
| ['Сенцов Андрей Сергеевич']         | ['it@chtpz.ru']                      |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Оао Челябинский Трубопрокатный Завод', address=None, comment=None)]                                                    |
| ['Орлов Василий Александрович']     | ['bug_itc_@esoo.ru']                 |                 | [Row(post='Аналитик', date_start=None, date_end=None, company='Ооо Инженерно-технический Центр', address=None, comment=None)]                                                         |
| ['Надежда Овчаренко']               | ['nadezhda.ovcharenko@grayling.com'] | ['74957886784'] | [Row(post='blank', date_start=None, date_end=None, company='Cветлана Чижкова -директор По Маркетингу', address=None, comment=None)]                                                   |
| ['Андрияшин Михаил']                | ['secretary2@akvion.ru']             | ['74957807234'] | [Row(post='Директор по ИТ CIO', date_start=None, date_end=None, company=None, address=None, comment=None)]                                                                            |
```