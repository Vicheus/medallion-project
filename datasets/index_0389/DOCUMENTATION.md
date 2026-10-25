# Parsetron results

## About row data

> - File path: perekrestok_ru.csv
> - Total rows: 1439999

### Schema
```
root
 |-- Номер карты: long (nullable = true)
 |-- Имя: string (nullable = true)
 |-- Отчество: string (nullable = true)
 |-- E-mail: string (nullable = true)
 |-- Телефон: string (nullable = true)
 |-- Баланс: string (nullable = true)

```

### Data sample
```
|      Номер карты | Имя        | Отчество       | E-mail                  |    Телефон |   Баланс |
|-----------------:|:-----------|:---------------|:------------------------|-----------:|---------:|
| 7789007029126486 | Ольга      | Анатольевна    | olga433@mail.ru         | 9852229796 |  2680053 |
| 7789007002925680 |            |                |                         | 9859232766 |   371279 |
| 7789007024982727 | Александр  | Михайлович     | alexgribkov@yahoo.com   | 9168137129 |   277250 |
| 7789007071535733 |            |                |                         | 9272601716 |   240004 |
| 7789007047816837 | Александр  | Валерьевич     | woody-05@mail.ru        | 9031548250 |   207328 |
| 7789007001954434 |            |                |                         | 9166759377 |   196289 |
| 7789007023983122 |            |                |                         | 9037220945 |   192431 |
| 7789007026718301 |            |                |                         | 9255172339 |   189547 |
| 7789007007396796 |            |                |                         | 9250222777 |   175465 |
| 7789007049730168 | Владислав  | Сергеевич      | vladgalant@mail.ru      | 9033067155 |   165859 |
| 7789007025767085 | Вера       | Константиновна | shvk2007@rambler.ru     | 9175239916 |   165763 |
| 7789007032481977 | Павел      | Алексеевич     | pavel@marakhovsky.com   | 9250037079 |   157845 |
| 7789007071452582 |            |                |                         | 9175220271 |   155746 |
| 7789007062233694 |            |                |                         | 9153686101 |   155714 |
| 7789007070946519 | Милен      | Алниловна      | milendavudova@yandex.ru | 9167452058 |   155057 |
| 7789007040150028 |            |                |                         | 9215615537 |   154464 |
| 7789005806108842 |            |                |                         | 9067479037 |   153153 |
| 7789007000788676 | Константин | Семенович      | uns57@mail.ru           | 9853647932 |   151176 |
| 7789007034892551 |            |                |                         | 9168744501 |   150537 |
| 7789007023105726 |            |                |                         | 9165387774 |   150402 |
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
 |-- accounts: array (nullable = true)
 |    |-- element: array (containsNull = false)
 |    |    |-- element: struct (containsNull = true)
 |    |    |    |-- title: string (nullable = false)
 |    |    |    |-- link: string (nullable = false)
 |    |    |    |-- client_card_number: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: array (containsNull = false)
 |    |    |-- element: string (containsNull = false)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.92% |
| Phones | 22.87% |
| Accounts | 100.00% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                       | emails                           | phones          | accounts                                                                                               | raw_metadata             |
|:----------------------------|:---------------------------------|:----------------|:-------------------------------------------------------------------------------------------------------|:-------------------------|
| ['Alexander']               | ['roscabsale@mail.ru']           |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007071781196')]] | [[]]                     |
| ['Alexey']                  | ['alexey0773@gmail.com']         | ['79262249509'] | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007062877706')]] | [['{"Баланс": "2813"}']] |
| ['Anton']                   | ['amukhinfly@gmail.com']         |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007069760996')]] | [['{"Баланс": "1292"}']] |
| ['Evgenia']                 | ['ozzy.ru@icloud.com']           |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007052677389')]] | [[]]                     |
| ['Rose Mananghaya']         | ['mananghayarose@yahoo.com']     |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007025450534')]] | [[]]                     |
| ['Slonova']                 | ['slonova_tanya@mail.ru']        |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007065194083')]] | [[]]                     |
| ['Абделлатиф Легдани']      | ['legdani@hotmail.com']          |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007046211568')]] | [[]]                     |
| ['Абдурасул Махмуткулович'] | ['rasul_1985-85@mail.ru']        |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007048163973')]] | [[]]                     |
| ['Агдас Хусаинович']        | ['agdas@mail.ru']                |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789005069333814')]] | [[]]                     |
| ['Азат Раисович']           | ['azat3003@yandex.ru']           |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007038941206')]] | [[]]                     |
| ['Азиза Шавкатовна']        | ['pechenushka@bk.ru']            |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007024465814')]] | [[]]                     |
| ['Айгуль Нажиповна']        | ['aigulmud@rambler.ru']          |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007044933445')]] | [[]]                     |
| ['Айжамал Чыныбекова']      | ['janim_1987@mail.ru']           |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007049595447')]] | [[]]                     |
| ['Айрат Анварович']         | ['al202k@gmail.com']             |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007044143698')]] | [[]]                     |
| ['Айрат Халисович']         | ['airat-karamov@mail.ru']        | ['79196892767'] | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007015404194')]] | [['{"Баланс": "5269"}']] |
| ['Айшат Адильхановна']      | ['ayshat2009@gmail.com']         |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007025934883')]] | [[]]                     |
| ['Алга Саналовна']          | ['sangadzhi-goryaeva@yandex.ru'] |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007045586010')]] | [[]]                     |
| ['Алевтина Викторовна']     | ['alevtina_shulga@mail.ru']      |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007013986614')]] | [[]]                     |
| ['Алевтина Юрьевна']        | ['alynkasochi@mail.ru']          | ['79183052018'] | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007068149217')]] | [['{"Баланс": "4399"}']] |
| ['Александр']               | ['braunze@mail.ru']              |                 | [[Row(title='Перекрёсток', link='https://www.perekrestok.ru', client_card_number='7789007075075587')]] | [[]]                     |
```