# Parsetron results

## About row data

> - File path: metro-cc.ru.csv
> - Total rows: 2736739

### Schema
```
root
 |-- DATE_CREATE: string (nullable = true)
 |-- ID: integer (nullable = true)
 |-- CARD: decimal(22,0) (nullable = true)
 |-- NAME: string (nullable = true)
 |-- PHONE: string (nullable = true)
 |-- EMAIL: string (nullable = true)

```

### Data sample
```
| DATE_CREATE         |      ID |        CARD | NAME                | PHONE          | EMAIL                          |
|:--------------------|--------:|------------:|:--------------------|:---------------|:-------------------------------|
| 01.01.2022 00:47:03 | 9804929 | 6.43013e+21 | Глеб Ильдеров       | +7(911)5725167 | gleb01062006b@gmail.com        |
| 01.01.2022 00:47:23 | 9804930 | 6.4301e+21  | Ирина Уварова       | +7(921)4363633 | inuvarova@mail.ru              |
| 01.01.2022 00:50:16 | 9804931 | 6.43011e+21 | Флера Салахиева     | +7(918)8536056 | fliora14@gmail.com             |
| 01.01.2022 00:54:50 | 9804932 | 6.43011e+21 | Юрий Малышкин       | +7(967)4970517 | jonermas@mail.ru               |
| 01.01.2022 00:57:39 | 9804933 | 6.43013e+21 | Андрей Коробцов     | +7(896)1025479 | vinipyh9915@gmail.com          |
| 01.01.2022 00:57:47 | 9804934 | 6.4301e+21  | Екатерина Кудряшова | +7(950)0387238 | Shykud@gmail.com               |
| 01.01.2022 00:59:32 | 9804935 | 6.43011e+21 | руслан дубинин      | +7(917)1797250 | j.o.k.e.r_86@mail.ru           |
| 01.01.2022 01:02:39 | 9804936 | 6.43013e+21 | Ирина Каузан        | +7(910)3614188 | kauzan90@gmail.com             |
| 01.01.2022 01:07:03 | 9804937 | 6.43011e+21 | Юсуфали Азизов      | +7(962)0973647 | zainab199052@gmail.com         |
| 01.01.2022 01:10:22 | 9804938 | 6.43011e+21 | Наталья Котелевская | +7(918)7467010 | katerina.ktlvskaya47@gmail.com |
| 01.01.2022 01:10:50 | 9804939 | 6.43011e+21 | Маргарита Васянина  | +7(906)2361115 | ritakgd90@gmail.com            |
| 01.01.2022 01:19:42 | 9804940 | 6.4301e+21  | Ольга  Лопатина     | +7(985)5594888 | lopatina.o.m@mail.ru           |
| 01.01.2022 01:21:44 | 9804941 | 6.43011e+21 | Сергей Филин        | +7(920)3610206 | sfilin841@gmail.com            |
| 01.01.2022 01:24:02 | 9804942 | 6.4301e+21  | Роман Минкин        | +7(903)7634747 | minkin_roman@mail.ru           |
| 01.01.2022 01:26:15 | 9804943 | 6.43011e+21 | алексей зайцев      | +7(961)4112727 | alekseizaicev@gmail.ru         |
| 01.01.2022 01:41:07 | 9804944 | 6.43011e+21 | Дмитрий Григорьев   | +7(919)6367856 | grishaotec2010@rambler.ru      |
| 01.01.2022 01:59:05 | 9804945 | 6.43011e+21 | тамара рябова       | +7(913)1753071 | leito-to@ya.ru                 |
| 01.01.2022 01:59:13 | 9804946 | 6.43011e+21 | алёна дмитриева     | +7(929)7876550 | dmitrieva_as@rambler.ru        |
| 01.01.2022 02:26:05 | 9804947 | 6.43011e+21 | Артем Коновалов     | +7(982)7326538 | artem2222368@gmail.com         |
| 01.01.2022 02:31:40 | 9804948 | 6.43013e+21 | Александр Лысехин   | +7(953)3588898 | fdafe.asd@yandex.ru            |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- client_card_number: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 99.88% |
| Emails | 99.98% |
| Accounts | 100.00% |
| Actuality | 0.00% |



### Data sample
```
| names                   | phones          | emails                             | accounts                                                                           | actuality   |
|:------------------------|:----------------|:-----------------------------------|:-----------------------------------------------------------------------------------|:------------|
| ['Глеб Ильдеров']       | ['79115725167'] | ['gleb01062006b@gmail.com']        | [Row(title='Карта лояльности METRO', client_card_number='6430130800174152011708')] |             |
| ['Ирина Уварова']       | ['79214363633'] | ['inuvarova@mail.ru']              | [Row(title='Карта лояльности METRO', client_card_number='6430104000186436011723')] |             |
| ['Флера Салахиева']     | ['79188536056'] | ['fliora14@gmail.com']             | [Row(title='Карта лояльности METRO', client_card_number='6430106100139116011743')] |             |
| ['Юрий Малышкин']       | ['79674970517'] | ['jonermas@mail.ru']               | [Row(title='Карта лояльности METRO', client_card_number='6430107000190010011765')] |             |
| ['Андрей Коробцов']     |                 | ['vinipyh9915@gmail.com']          | [Row(title='Карта лояльности METRO', client_card_number='6430133700193281011737')] |             |
| ['Екатерина Кудряшова'] | ['79500387238'] | ['shykud@gmail.com']               | [Row(title='Карта лояльности METRO', client_card_number='6430103700210937011750')] |             |
| ['Руслан Дубинин']      | ['79171797250'] | ['j.o.k.e.r_86@mail.ru']           | [Row(title='Карта лояльности METRO', client_card_number='6430105500180529011787')] |             |
| ['Ирина Каузан']        | ['79103614188'] | ['kauzan90@gmail.com']             | [Row(title='Карта лояльности METRO', client_card_number='6430130800174558011784')] |             |
| ['Юсуфали Азизов']      | ['79620973647'] | ['zainab199052@gmail.com']         | [Row(title='Карта лояльности METRO', client_card_number='6430106300185732011770')] |             |
| ['Наталья Котелевская'] | ['79187467010'] | ['katerina.ktlvskaya47@gmail.com'] | [Row(title='Карта лояльности METRO', client_card_number='6430107000190345011760')] |             |
| ['Маргарита Васянина']  | ['79062361115'] | ['ritakgd90@gmail.com']            | [Row(title='Карта лояльности METRO', client_card_number='6430105600185599011740')] |             |
| ['Ольга Лопатина']      | ['79855594888'] | ['lopatina.o.m@mail.ru']           | [Row(title='Карта лояльности METRO', client_card_number='6430103700211284011713')] |             |
| ['Сергей Филин']        | ['79203610206'] | ['sfilin841@gmail.com']            | [Row(title='Карта лояльности METRO', client_card_number='6430107600186074011757')] |             |
| ['Роман Минкин']        | ['79037634747'] | ['minkin_roman@mail.ru']           | [Row(title='Карта лояльности METRO', client_card_number='6430104800189640011799')] |             |
| ['Алексей Зайцев']      | ['79614112727'] | ['alekseizaicev@gmail.ru']         | [Row(title='Карта лояльности METRO', client_card_number='6430105800164653011708')] |             |
| ['Дмитрий Григорьев']   | ['79196367856'] | ['grishaotec2010@rambler.ru']      | [Row(title='Карта лояльности METRO', client_card_number='6430106600172794011757')] |             |
| ['Тамара Рябова']       | ['79131753071'] | ['leito-to@ya.ru']                 | [Row(title='Карта лояльности METRO', client_card_number='6430106800197835011730')] |             |
| ['Алёна Дмитриева']     | ['79297876550'] | ['dmitrieva_as@rambler.ru']        | [Row(title='Карта лояльности METRO', client_card_number='6430107000189966011722')] |             |
| ['Артем Коновалов']     | ['79827326538'] | ['artem2222368@gmail.com']         | [Row(title='Карта лояльности METRO', client_card_number='6430107700117567011700')] |             |
| ['Александр Лысехин']   | ['79533588898'] | ['fdafe.asd@yandex.ru']            | [Row(title='Карта лояльности METRO', client_card_number='6430130900167938011796')] |             |
```