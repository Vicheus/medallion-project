# Parsetron results

## About row data

> - Code name: index_0633
> - File path: orders - @bd_bereza.csv
> - Total rows: 11773

### Schema
```
root
 |-- Id: string (nullable = true)
 |-- UserID: integer (nullable = true)
 |-- Sum: integer (nullable = true)
 |-- Info: string (nullable = true)
 |-- Status: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Phone: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- Address: string (nullable = true)
 |-- Delivery: string (nullable = true)
 |-- Payment: string (nullable = true)
 |-- Last_Name: string (nullable = true)
 |-- Middle_Name: string (nullable = true)
 |-- Comment: string (nullable = true)
 |-- Discount: integer (nullable = true)

```

### Data sample
```
|    Id |   UserID |   Sum | Info   |   Status | Name                          | Phone           | Email                            | Address   | Delivery   | Payment   | Last_Name   | Middle_Name   | Comment   |   Discount |
|------:|---------:|------:|:-------|---------:|:------------------------------|:----------------|:---------------------------------|:----------|:-----------|:----------|:------------|:--------------|:----------|-----------:|
|  6120 |        0 |  3750 |        |        0 | ященко мария сергеевна        | 89242808215     | pinelopa666777@mail.ru           |           |            |           |             |               |           |          0 |
|  1562 |        0 |  3360 |        |        0 | Яшина Татьяна                 | 8-982-917-85-37 | duke182@mail.ru                  |           |            |           |             |               |           |          0 |
| 11033 |        0 |  3320 |        |        0 | Яшин Антон Викторович         | 79242532169     | tire2009@gmail.com               |           |            |           |             |               |           |          0 |
|  1901 |        0 |   490 |        |        0 | Яшин  Альберт Юрьевич         | 89092750435     | yashin.albert-33@mail.ru         |           |            |           |             |               |           |          0 |
|  9575 |        0 |  8520 |        |        0 | Ячевская Ольга Александровна  | +7 925 5897458  | ve8ko@mail.ru                    |           |            |           |             |               |           |          0 |
|  3616 |      889 |  1380 |        |        0 | Ячевская  Ольга               | 8-925-589-74-58 | ve8ko@mail.ru                    |           |            |           |             |               |           |          0 |
| 10952 |        0 |  3920 |        |        0 | Яцышина Ольга Николаевна      | 79788089369     | olga.yacyshina@mail.ru           |           |            |           |             |               |           |          0 |
|  6566 |        0 |   270 |        |        0 | Яценко Александр Викторович   | 79507743403     | levija@mail.ru                   |           |            |           |             |               |           |          0 |
|  1910 |        0 |  3800 |        |        0 | Яхонтов Евгений Владимирович  | 89220534567     | 9220534567@mail.ru               |           |            |           |             |               |           |          0 |
|  1911 |        0 |  1250 |        |        0 | Яхонтов Евгений Владимирович  | 89220534567     | 9220534567@mail.ru               |           |            |           |             |               |           |          0 |
|  3584 |      879 |  2400 |        |        0 | Яхина Ирина Валерьевна        | 89320503167     | irina.yakhina84@mail.ru          |           |            |           |             |               |           |          0 |
| 11589 |        0 |     0 |        |        0 | Яхин александр викторович     | 89219465545     | 9465545@mail.ru                  |           |            |           |             |               |           |          0 |
|  1422 |        0 |  1120 |        |        0 | ярцева ольга владимировна     | 89129447373     | yartseva444@mai.ru               |           |            |           |             |               |           |          0 |
|  1487 |      430 |  2960 |        |        0 | Яруллин Айдар Магфурович      | 89148685133     | aidar-magadn@mail.ru             |           |            |           |             |               |           |          0 |
|  8676 |        0 |  2200 |        |        0 | Ярощук Анастасия Николаевна   | 79148560962     | nastya-yaroshuk@mail.ru          |           |            |           |             |               |           |          0 |
|  4687 |        0 |  2863 |        |        0 | Ярошенко Яков Николаевич      | 79028571643     | Jarick89@mail.ru                 |           |            |           |             |               |           |          0 |
|   778 |        0 |  2100 |        |        0 | Ярославцева Ольга Николаевна  | 89241952772     | samodelkina2008@yandex.ru        |           |            |           |             |               |           |          0 |
|  8559 |        0 |  1400 |        |        0 | Ярославцева Наталия Сергеевна | 89265404031     | yaroslavtseva.nataliya@gmail.com |           |            |           |             |               |           |          0 |
|  7208 |        0 |  4460 |        |        0 | ярков юрий владимирович       | 79028287037     | yariy1986@mail.ru                |           |            |           |             |               |           |          0 |
|  2872 |        0 |   400 |        |        0 | Яр Сергей Станиславович       | 89807446064     | senay81@mail.ru                  |           |            |           |             |               |           |          0 |
```


## About final data
> - Total rows: 7265

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 97.77% |
| Emails | 99.67% |
| Address | 0.50% |



### Data sample
```
| names                                 | phones          | emails                         | address   |
|:--------------------------------------|:----------------|:-------------------------------|:----------|
| ['Глухов Константин Олегович']        | ['79031026332'] | ['kotik001@bk.ru']             |           |
| ['Юлия']                              | ['79031588358'] | ['grigorieva@bk.ru']           |           |
| ['Каёта Анастасия Владимировна']      | ['79037370567'] | ['kayota-av@mail.ru']          |           |
| ['Константин']                        | ['79037406687'] | ['kseleznev@yandex.ru']        |           |
| ['Заднепровская Наталья Викторовна']  | ['79043448688'] | ['natasa19741974@mail.ru']     |           |
| ['Екатерина']                         | ['79104345865'] | ['kather-1@yandex.ru']         |           |
| ['Кабанова Татьяна Геннадьевна']      | ['79115825940'] | ['tatyanakab@yandex.ru']       |           |
| ['Строченкова Ольга Николаевна']      | ['79121183240'] | ['o.strochenkova@mail.ru']     |           |
| ['Белоногова Ирина']                  | ['79126393346'] | ['ir.belonogova@yandex.ru']    |           |
| ['Шерстянкин Сергей Григорьевич']     | ['79130594334'] | ['sergeyshg@mail.ru']          |           |
| ['Краморенко Геннадий Геннадеьвич']   | ['79138465125'] | ['genrik65@mail.ru']           |           |
| ['Бадиков Дмитрий Геннадьевич']       | ['79154838083'] | ['blikov1987@mail.ru']         |           |
| ['Корнеев Владимир Сергеевич']        | ['79162175650'] | ['vsk74@rambler.ru']           |           |
| ['Геннадий']                          | ['79162930731'] | ['gennadiy.savenko@rt.ru']     |           |
| ['Максим']                            | ['79165466692'] | ['kozlovms@mail.ru']           |           |
| ['Сотникова Ольга Александровна']     | ['79167359860'] | ['britaniknfl@mail.ru']        |           |
| ['Балахонцев Павел Александрович']    | ['79172920414'] | ['pashka_lange@mail.ru']       |           |
| ['Воронкова Ирина Сергеевна']         | ['79192205557'] | ['voronkova.irina.89@mail.ru'] |           |
| ['Гусева Людмила Сергеевна']          | ['79204480394'] | ['gusls@mail.ru']              |           |
| ['Гладконогих Алексей Александрович'] | ['79217255351'] | ['leshei13@mail.ru']           |           |
```