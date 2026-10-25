# Parsetron results

## About row data

> - Code name: index_0148
> - File path: /home/user/Documents/data/index_0148/raw/admins_preprocessed.csv
> - Total rows: 146

### Schema
```
root
 |-- name: string (nullable = true)
 |-- phone: long (nullable = true)
 |-- cell_phone: long (nullable = true)
 |-- email: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- telegram_id: long (nullable = true)

```

### Data sample
```
| name                         |   phone |   cell_phone | email           | email2   |   telegram_id |
|:-----------------------------|--------:|-------------:|:----------------|:---------|--------------:|
| abills                       |     nan |          nan |                 |          | nan           |
| System user                  |     nan |          nan |                 |          | nan           |
| admin                        |     nan |          nan |                 |          |   2.1742e+08  |
| Мазур В.Л.                   |     nan |          nan | boom@kct.net.ua |          | nan           |
|                              |     nan |          nan |                 |          | nan           |
| Подлесная Д.Ю.               |     nan |          nan |                 |          |   1.53585e+08 |
| Каракчеев Максим             |     nan |          nan |                 |          | nan           |
| Лариса Дмитриевна            |     nan |          nan |                 |          | nan           |
| Женя Каменка                 |     nan |          nan |                 |          | nan           |
| Игорь                        |     nan |          nan |                 |          | nan           |
| Анна Раковец (старая учетка) |     nan |          nan |                 |          | nan           |
| Никишин Александр            |     nan |          nan |                 |          | nan           |
| Чернов Александр             |     nan |          nan |                 |          | nan           |
| Роял Алиев                   |     nan |          nan |                 |          | nan           |
| Майоров Николай              |     nan |          nan |                 |          | nan           |
| Котов Евгений                |     nan |          nan |                 |          | nan           |
| Пшеничников Сергей           |     nan |          nan |                 |          | nan           |
| Евгений Однолько             |     nan |          nan |                 |          | nan           |
| Роман Романский              |     nan |          nan |                 |          | nan           |
| Фетиев Ленур                 |     nan |          nan |                 |          | nan           |
```

> - Code name: index_0148
> - File path: /home/user/Documents/data/index_0148/raw/users_preprocessed.csv
> - Total rows: 51039

### Schema
```
root
 |-- last_name: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- email: string (nullable = true)
 |-- zip: string (nullable = true)
 |-- city: string (nullable = true)
 |-- address_street: string (nullable = true)
 |-- address_build: string (nullable = true)
 |-- address_flat: string (nullable = true)
 |-- reg_address: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- pasport_num: string (nullable = true)
 |-- pasport_date: string (nullable = true)
 |-- pasport_grant: string (nullable = true)
 |-- telegram_id: long (nullable = true)
 |-- email2: string (nullable = true)
 |-- cell_phone: string (nullable = true)
 |-- phone2: string (nullable = true)

```

### Data sample
```
| last_name   | first_name   | middle_name   |       phone | email           | zip   | city           | address_street       | address_build   |   address_flat | reg_address   | birth_date   |   pasport_num | pasport_date   | pasport_grant   |   telegram_id | email2                    |   cell_phone |      phone2 |
|:------------|:-------------|:--------------|------------:|:----------------|:------|:---------------|:---------------------|:----------------|---------------:|:--------------|:-------------|--------------:|:---------------|:----------------|--------------:|:--------------------------|-------------:|------------:|
|             |              |               | 79780042030 |                 |       | Мой адрес СССР |                      | 1537            |             15 |               | 1970-01-01   |               | 0000-00-00     |                 |   7.41239e+07 |                           |  79780042030 | 79780042030 |
|             |              |               |             |                 |       |                |                      |                 |                |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |              |             |
|             |              |               |             |                 |       |                | 156                  | 4/2             |              0 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |            4 |             |
| Черный      | Андрей       | Андреевич     |             |                 |       |                | 149                  | 1773            |              0 |               | 1970-01-01   |               | 0000-00-00     |                 |   1.27534e+08 |                           |  79788490585 |             |
| Громовой    | Константин   | Петрович      |             |                 |       |                | 107                  | 1456            |              3 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |  79788131599 |             |
| Дерюгин     | Савва        | Викторович    | 79788245137 |                 |       |                | 96                   | 3               |              0 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |              | 79788245137 |
| Мазур       | Вадим        | Леонидович    | 79788087078 | boom@kct.net.ua |       |                | 95                   | 1342            |                |               | 1970-01-01   |               | 0000-00-00     |                 |   2.01169e+08 | boom@kct.net.ua           |              |             |
| Анаколов    | Никита       | Сергевич      | 79788146552 |                 |       |                | 25                   | 24              |             26 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |              | 79788146552 |
| Чуфас       | Наталья      | Павловна      |             |                 |       |                | 89                   | 62              |              1 |               | 1970-01-01   |               | 0000-00-00     |                 |   7.4899e+07  |                           |  79788649389 | 79787460091 |
| Котова      | Наталья      | Николаевна    | 79780400047 |                 |       |                | 167                  | 5               |             12 |               | 1970-01-01   |    3914813193 | 2015-01-19     |                 | nan           |                           |  79789762620 | 79787685692 |
| Блюм        | Александр    | Юрьевич       |             |                 |       |                | Крымчакский переулок | 15              |             16 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |              |             |
| Леонов      | Евгений      | Олегович      | 79788102878 |                 |       |                | 9                    | 17              |              0 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |              | 79788102878 |
| Луконина    | Лилия        | Павловна      | 79787417529 |                 |       |                | 89                   | 50              |              7 |               | 1970-01-01   |               | 0000-00-00     |                 |   5.52953e+08 |                           |              | 79787417529 |
| Коломиец    | Владимир     | Иванович      | 79787658064 |                 |       |                | 42                   | 65а             |              0 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |              | 79787658064 |
|             | Дмитрий      | Юрьевич       |             |                 |       |                | 517                  | 16              |              0 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |  79787805866 |             |
| Лепих       | Владислав    | Олегович      | 79788558563 |                 |       |                | 166                  | 1914            |              3 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           | Vladislav.lepih@yandex.ru |              | 79788558563 |
| Цветков     | Алексей      | Валерьевич    |             |                 |       |                | 167                  | 3               |             15 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |  79787440790 |             |
| Пойда       | Светлана     | Анатодьевна   |             |                 |       |                | Ефремова             | 18              |             17 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |              |             |
| Сидоренко   | Лариса       | Николаевна    |             |                 |       |                | Студенческая         | 5               |              8 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |              |             |
| Предыбайло  | Анатолий     | Александрович |             |                 |       |                | Чехова               | 57              |              4 |               | 1970-01-01   |               | 0000-00-00     |                 | nan           |                           |              |             |
```

> - Code name: index_0148
> - File path: /home/user/Documents/data/index_0148/raw/companies_preprocessed.csv
> - Total rows: 15

### Schema
```
root
 |-- name: string (nullable = true)
 |-- phone: long (nullable = true)
 |-- tax_number: long (nullable = true)
 |-- address: string (nullable = true)
 |-- bank_account: decimal(20,0) (nullable = true)
 |-- bank_name: string (nullable = true)

```

### Data sample
```
| name                                                                                     |         phone |    tax_number | address   |   bank_account | bank_name                                                                     |
|:-----------------------------------------------------------------------------------------|--------------:|--------------:|:----------|---------------:|:------------------------------------------------------------------------------|
| ЖСК «ЗАЛЕСЬЕИНВЕСТСТРОЙ»                                                                 |   7.97873e+10 |   9.10203e+09 |           |    4.07038e+19 | "АО ""БАНК ЧБРР"""                                                            |
| ООО «КРЭЛКОМ»                                                                            |   7.97856e+10 |   9.10203e+09 |           |    4.07028e+19 | ПАО РНКБ                                                                      |
| ООО «Интерфин»                                                                           |   7.36523e+10 |   9.10202e+09 |           |    4.07028e+19 | АО «ГЕНБАНК»                                                                  |
| ГБУ РК «Крымская ГГМЭ»                                                                   |   7.36523e+10 |   9.10205e+09 |           |    3.22464e+18 | Отделение Республика Крым Банка России//УФК по Республике Крым г. Симферополь |
| МБОУ «СОШ № 5» г. Симферополя                                                            |   7.36523e+10 |   9.10207e+09 |           |    4.07018e+19 | Отделение Республика Крым Банка России//УФК по Республике Крым г. Симферополь |
| ООО «ПАРТНЕР ЮГ»                                                                         |   7.97804e+10 |   9.10224e+09 |           |    4.07028e+19 | АО «ГЕНБАНК»                                                                  |
| "Магазины ""Товары для дома"""                                                           |   7.97884e+10 | nan           |           |                |                                                                               |
| ИП Ницецкая Екатерина Владимировна                                                       |   7.97885e+10 |   9.10607e+11 |           |    4.08028e+19 | ПАО РНКБ                                                                      |
| ООО «КРЫМ ОЙЛ»                                                                           |   7.97804e+10 |   9.105e+09   |           |    4.07028e+19 | АО «Генбанк» г.Симферополь                                                    |
| ГУП РК «Вода Крыма»                                                                      | nan           | nan           |           |                |                                                                               |
| ИП Копылова Лидия Николаевна                                                             |   7.97877e+10 |   9.10215e+11 |           |    4.08028e+19 | ЮГО-ЗАПАДНЫЙ БАНК ПАО СБЕРБАНК                                                |
| ИП Алиев Насими Агиф Оглы                                                                |   7.97865e+10 |   9.10218e+11 |           |    4.08028e+19 | ПАО РНКБ                                                                      |
| ИП Муслимов Руслан Арсенович                                                             |   7.97877e+10 |   9.10227e+11 |           |    4.08028e+19 | "Филиал ""Центральный"" Банка ВТБ (ПАО) г. Москва "                           |
| ООО «Дизель»                                                                             | nan           |   5.19008e+09 |           |    4.07028e+19 | Санкт-Петербургский филиал АО «АЛЬФА-БАНК»                                    |
| "МКУ ""Центр по обеспечению деятельности бюджетных учреждений городского округа Судак""" | nan           |   9.10812e+09 |           |                |                                                                               |
```


## About final data
> - Total rows: 44954

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- financials: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- invoice_number: string (nullable = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```

### Data sample
```
| names                            | emails                            | phones                         | birth_date   | documents                                                                                                                                                                                            | address                                                     | financials   | socials                                                           |
|:---------------------------------|:----------------------------------|:-------------------------------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------|:-------------|:------------------------------------------------------------------|
| ['Борисова Мария Николаевна']    |                                   | ['79788167485', '79781653863'] | 01.01.1970   | [Row(type=0, serial='3914460806', country='RUS', date_issue='30.01.2014', date_expire=None, authority=None, authority_code=None)]                                                                    |                                                             |              |                                                                   |
| ['Ким Игорь Сергеевич']          |                                   | ['79787582013']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              | [Row(title='Telegram', id='1578355080', link=None, comment=None)] |
| ['Сулейманов Эмиль Исметович']   |                                   | ['79788425787']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Таран Владимир Александрович'] | ['vladimir.taran.1982@yandex.ru'] | ['79788320334']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Смолякова Елена Евгеньевна']   |                                   | ['79787685988', '79787685989'] | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Газизова Юлия Александровна']  |                                   | ['79788441547', '79787698406'] | 01.01.1970   | [Row(type=0, serial='3914610619', country='RUS', date_issue='20.01.2017', date_expire=None, authority='Отдел УФМС по РК и г. Севастополю в Центральном районе г. Симферополя', authority_code=None)] | ['Республика Крым г. Симферополь ул. Гавена д. 105 кв. 51'] |              |                                                                   |
| ['Народицкая Элина Анатольевна'] |                                   | ['79788468026']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Оленник Ирина Ивановна']       |                                   | ['79787536107']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Зенин Сергей Александрович']   |                                   | ['79787508636']                |              | [Row(type=0, serial='3922684407', country='RUS', date_issue='22.01.2022', date_expire=None, authority='МВД по Республике Крым', authority_code=None)]                                                | ['РоссияРеспублика Крым ул. Гавена д. 99 кв.20']            |              |                                                                   |
| ['Самойлова Татьяна Николаевна'] | ['heavy_hoplite@mail.ru']         | ['79787297969', '79787579405'] | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Дыбская Любовь Федоровна']     |                                   | ['79780318893']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Ермаков Василий Алексеевич']   |                                   | ['79787194337']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Козак Роман Иосипович']        |                                   | ['79788696488']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Дмитрий']                      |                                   | ['79787110647', '79784540229'] | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Третьяков Олег Юрьевич']       |                                   | ['79787914640']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Ецкевич Таиса Владимировна']   |                                   | ['79787380645']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Литвиненко Валерия Борисовна'] |                                   | ['79787139733']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Фхмедова Нияра Февзиевна']     |                                   | ['79782590700', '79788724835'] | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Семирог Галина Николаевна']    |                                   | ['79788985330']                | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              |                                                                   |
| ['Федотов Владимир Васильевич']  |                                   | ['79788545647', '79788532230'] | 01.01.1970   |                                                                                                                                                                                                      |                                                             |              | [Row(title='Telegram', id='461393176', link=None, comment=None)]  |
```