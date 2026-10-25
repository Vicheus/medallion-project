# Parsetron results

## About row data

> - Code name: index_0126
> - File path: /media/user/TRANSCEND/Databases/index_0126/raw/preprocessed/users_info_1_preprocessed.csv
> - Total rows: 959598

### Schema
```
root
 |-- USER_ID: string (nullable = true)
 |-- username: string (nullable = true)
 |-- password_hash: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- birth_date: date (nullable = true)
 |-- email2: string (nullable = true)

```

### Data sample
```
|   USER_ID | username             | password_hash                            | first_name            | last_name    | middle_name   | email                | gender   | phone          | birth_date   | email2   |
|----------:|:---------------------|:-----------------------------------------|:----------------------|:-------------|:--------------|:---------------------|:---------|:---------------|:-------------|:---------|
|        25 | megorov              | 9bf0194b6092fb9eccca7842d46cf726         | Максим                | Егоров       |               | m@e.ru               |          |                |              |          |
|        26 | mgavrilov            | 6fa2f6f37a42e9f30eb23ffc241e483d         | Михаил                | Гаврилов     | Александрович | gavrilov@nanocad.ru  | M        |                | 1964-12-08   |          |
|        27 | agrachevsky          | 37f8fba89c891b434c58a21ac9018ebd         | Андрей                | Грачевский   |               | a@g.ru               |          |                |              |          |
|       114 | nano2                | 4db3d36bbdbae359ba0c324af280900d         |                       |              |               | epanin@nanocad.ru    |          |                |              |          |
|      7653 | nano3                | db3b72136f1557d45ea9fc7f3acde245         |                       |              |               | test@etest.ru        |          |                |              |          |
|      7654 | nanoMAG@mail.ru      | 3c386dd4a40a6acdfc5e14f742f77807         | Михаил                | Гаврилов     | Александрович | nanomag@mail.ru      |          |                |              |          |
|      7655 | mczag@mail.ru        | 25f9e794323b453885f5181f1b624d0b         |                       |              |               | mczag@mail.ru        |          |                |              |          |
|      7656 | 111111test@mail.ru   | cec803a4b375d4a0543b904c3ed9cfcf         | Максим                | Егоров       |               | 111111test@mail.ru   | M        | 6556565        | 1975-01-01   |          |
|      7657 | studio@maiski.com    | 3efd3a6b1ce4c7c05fa12e0262582368         | Всеволод Валентинович | Майский      |               | studio@maiski.com    | M        | 8-000-0000000  |              |          |
|      7658 | kozinov@csoftcom.com | 1&uG8d{N10c50f1edfa1a33a69f49afee9e0eba6 | Иван                  | Козинов      | Викторович    | kozinov@csoftcom.com | M        | +7 926 4005174 | 1986-03-02   |          |
|      7659 | tdms@csoft.ru        | 25f9e794323b453885f5181f1b624d0b         |                       |              |               | tdms@csoft.ru        |          |                |              |          |
|      7660 | nanomag2@mail.ru     | 3c386dd4a40a6acdfc5e14f742f77807         | sdfgd                 | sdfg         |               | nanomag2@mail.ru     |          | 1344           |              |          |
|      7661 | gavrilov@nanocad.ru  | efb98609bbf3738a1593f53d41735ce9         |                       |              |               | gavrilov@nanocad.ru  |          |                |              |          |
|      7662 | tm-22@list.ru        | -v7QE5<q47da90d64a7be4219254660a0e0fb0c3 |                       |              |               | tm-22@list.ru        |          |                |              |          |
|      7663 | support@nanocad.ru   | 15c3aa6784ae44515aaf529ff8ab70b4         |                       |              |               | support@nanocad.ru   |          |                |              |          |
|      7664 | yuravv@list.ru       | n9Y{Pd}6c0137731b0e7fd6344edb471d2cd6c27 | Юрий                  | Валентинович | Выхватенко    | yuravv@list.ru       |          |                |              |          |
|      7665 | kaparov@csoft.ru     | \N5uVo^05cdd66354336899809a5f33d29b665dd | Сергей                | Капаров      | Михайлович    | kaparov@csoft.ru     |          |                | 1975-11-20   |          |
|      7666 | max@nanocad.ru       | I9^q7[dV8f6d1386522199696423ba2de9484b87 | Максим                | Егоров       |               | max@nanocad.ru       |          |                |              |          |
|      7667 | seva@maiski.com      | 3D=i0>Tff255b2dc06539d836a9d32909181aa89 |                       |              |               | seva@maiski.com      |          |                |              |          |
|      7668 | polpasha@mail.ru     | 20daca1f904cce33ef89b6bf4bd9dfe4         |                       |              |               | polpasha@mail.ru     |          |                |              |          |
```

> - Code name: index_0126
> - File path: /media/user/TRANSCEND/Databases/index_0126/raw/preprocessed/users_info_2_preprocessed.csv
> - Total rows: 2844

### Schema
```
root
 |-- USER_ID: string (nullable = true)
 |-- name2: string (nullable = true)
 |-- email3: string (nullable = true)
 |-- phone2: string (nullable = true)
 |-- address: string (nullable = true)
 |-- send_address: string (nullable = true)
 |-- address2: string (nullable = true)
 |-- phone3: string (nullable = true)
 |-- name3: string (nullable = true)

```

### Data sample
```
|   USER_ID | name2                                                                                                   | email3                     | phone2          | address                                                                | send_address                                                              | address2   | phone3              | name3                             |
|----------:|:--------------------------------------------------------------------------------------------------------|:---------------------------|:----------------|:-----------------------------------------------------------------------|:--------------------------------------------------------------------------|:-----------|:--------------------|:----------------------------------|
|      7729 | Юрьевич Александр Скрипальщиков                                                                         | mcad@inbox.ru              |                 |                                                                        |                                                                           |            |                     |                                   |
|      7844 | Слинкин Филипп Сергеевич                                                                                | iliorik@mail.ru            | 9048722205      |                                                                        |                                                                           |            |                     |                                   |
|     15911 | simonyan artak spartakovich                                                                             | eroartak@rambler.ru        | 89506237069     |                                                                        |                                                                           |            |                     |                                   |
|      7848 | Михайлович Сергей Терентьев                                                                             | sterentev@bk.ru            |                 |                                                                        |                                                                           |            |                     |                                   |
|     16383 | Якушев Евгений Валерьевич                                                                               | apk-master@ya.ru           | 8 7232 222 047  |                                                                        |                                                                           |            |                     |                                   |
|      7900 | Иванович Сергей Марьянченко                                                                             | viking2000@mail.ru         |                 |                                                                        |                                                                           |            |                     |                                   |
|     11340 | Петрохимекалс                                                                                           | lowyagin@petrochemicals.ru |                 | 400075 Российская Федерация Волгоград Краснополянская 74А              | Российская Федерация                                                      |            | 8(8442)35-12-40     | Ловягин Денис Владимирович        |
|     17029 | Татаринцев Сергей Михайлович                                                                            | serg2406@mail.ru           | 89281456921     |                                                                        |                                                                           |            |                     |                                   |
|     17192 | Саблин Олег Васильевич                                                                                  | olegsablin08@rambler.ru    | 8 918 552 6713  |                                                                        |                                                                           |            |                     |                                   |
|     17691 | Патута Олег Ростиславович                                                                               | oleg.patuta@gmail.com      | +38-0512-559425 |                                                                        |                                                                           |            |                     |                                   |
|     17587 | "Открытое акционерное общество ""Научно-изыскательское проектно-конструкторское бюро ""Строительство""" | nipkb@mail.ru              |                 | 105005, г. Москва Елизаветинский пер. 6                                | 143913 г. Балашиха мкрю Гагарина д.19 кв 102                              |            | +7(916)505-9119     | Нещадимов Виктор Александрович    |
|      9874 | Николаевич Сергей Балакший                                                                              | sergebn@mail.ru            |                 |                                                                        |                                                                           |            |                     |                                   |
|     16466 | Овсянников Олег Александрович                                                                           | mariijal@mail.ru           | +79615140087    |                                                                        |                                                                           |            |                     |                                   |
|     17388 | Ядринский машиностроительный завод                                                                      | mashzavod21@mail.ru        |                 | 429060, ЧР, г.Ядрин, ул. 30-лет Победы, д.6                            | 429060, ЧР, г.Ядрин, ул. 30-лет Победы, д.6                               |            | 83547-22271         | ВЯЧЕСЛАВ ТОЛСТОВ                  |
|     18216 | Герасимов Александр Евгеньевич                                                                          | agerevg@rol.ru             | 910 431-09-23   |                                                                        |                                                                           |            |                     |                                   |
|     18025 | "ОАО ""Лесосибирский порт"""                                                                            | demina@primatls.ru         |                 | 662549, г.Лесосибирск, Красноярского края, ул. Енисейская, 28          | 662549, г.Лесосибирск, Красноярского края, ул. Енисейская, 28             |            | (39145) 4-24-10     | Семенов Олег Игоревич             |
|     18241 | "Закрытое акционерное общество ""Атис"""                                                                | kalin@atis.yaroslavl.ru    |                 | 150000,  г. Ярославль, ул. Революционная, д.9а                         | 150000,  г. Ярославль, ул. Революционная, д.9а                            |            | 8-4852-31-45-33     | Калин Александр Валентинович      |
|     18656 | Потороча Сергей Валентинович                                                                            | serggorin94@gmail.com      | +79192020762    |                                                                        |                                                                           |            |                     |                                   |
|     18721 | "Общество с ограниченной ответственностью ""ИнтелтехПроект"""                                           | inteltechproject@gmail.com |                 | 455000 Челябинская обл., г. Магнитогорск, ул. Калинина, д. 77, оф. 115 | 455039 Челябинская обл., г. Магнитогорск,ул. Вокзальная, д. 134/1, кв. 39 |            | (351) 906 - 53 - 14 | Мухаметзянов Алексей Газимзянович |
|      9413 | Малышев Анатолий Игоревич                                                                               | poligon@nightmail.ru       |                 |                                                                        |                                                                           |            |                     |                                   |
```


## About final data
> - Total rows: 749479

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```

### Data sample
```
| names                             | emails                    | phones          | address                                            |   sex | birth_date   | accounts                                                                                                                                                                |
|:----------------------------------|:--------------------------|:----------------|:---------------------------------------------------|------:|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Егоров Максим']                 | ['m@e.ru']                |                 |                                                    |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='megorov', password_hash='9bf0194b6092fb9eccca7842d46cf726')]                        |
| ['Гаврилов Михаил Александрович'] | ['gavrilov@nanocad.ru']   |                 |                                                    |     1 | 08.01.1964   | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='mgavrilov', password_hash='6fa2f6f37a42e9f30eb23ffc241e483d')]                      |
| ['Грачевский Андрей']             | ['a@g.ru']                |                 |                                                    |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='agrachevsky', password_hash='37f8fba89c891b434c58a21ac9018ebd')]                    |
| ['Гаврилов Михаил Александрович'] | ['nanomag@mail.ru']       | ['74956458626'] | ['121359 Москваул. Маршала Тимошенко д.17 корп.1'] |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='nanoMAG@mail.ru', password_hash='3c386dd4a40a6acdfc5e14f742f77807')]                |
| ['Егоров Максим']                 | ['111111test@mail.ru']    |                 |                                                    |     1 | 01.01.1975   | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='111111test@mail.ru', password_hash='cec803a4b375d4a0543b904c3ed9cfcf')]             |
| ['Майский Всеволод Валентинович'] | ['studio@maiski.com']     |                 |                                                    |     1 |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='studio@maiski.com', password_hash='3efd3a6b1ce4c7c05fa12e0262582368')]              |
| ['Козинов Иван Викторович']       | ['kozinov@csoftcom.com']  | ['79264005174'] |                                                    |     1 | 02.01.1986   | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='kozinov@csoftcom.com', password_hash='1&uG8d{N10c50f1edfa1a33a69f49afee9e0eba6')]   |
| ['Sdfg Sdfgd']                    | ['nanomag2@mail.ru']      |                 |                                                    |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='nanomag2@mail.ru', password_hash='3c386dd4a40a6acdfc5e14f742f77807')]               |
| ['Валентинович Юрий Выхватенко']  | ['yuravv@list.ru']        |                 |                                                    |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='yuravv@list.ru', password_hash='n9Y{Pd}6c0137731b0e7fd6344edb471d2cd6c27')]         |
| ['Капаров Сергей Михайлович']     | ['kaparov@csoft.ru']      |                 |                                                    |   nan | 20.01.1975   | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='kaparov@csoft.ru', password_hash='\\N5uVo^05cdd66354336899809a5f33d29b665dd')]      |
| ['Егоров Максим']                 | ['max@nanocad.ru']        | ['74956458626'] | ['Российская Федерация']                           |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='max@nanocad.ru', password_hash='I9^q7[dV8f6d1386522199696423ba2de9484b87')]         |
| ['Титов Сергей Васильевич']       | ['titovsem@rambler.ru']   |                 |                                                    |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='titovsem@rambler.ru', password_hash='6H+rf7W:9e9e8ed7053a6dc808e9db20c3e3a6ce')]    |
| ['Долгих Михаил Викторович']      | ['mike_iceman@mail.ru']   | ['74732521883'] |                                                    |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='mike_iceman@mail.ru', password_hash='5V!d#0Mie158fa4a3d3c943dae5c077e2b9708cb')]    |
| ['Радужан Антон Александрович']   | ['roomofangel@mail.ru']   |                 |                                                    |   nan | 28.01.1987   | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='roomofangel@mail.ru', password_hash='_nM4aN~11af5213a1a45ccb872792c14175c94b2')]    |
| ['Егоров Максим Станиславович']   | ['egorov_m_s@mail.ru']    |                 |                                                    |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='egorov_m_s@mail.ru', password_hash='0fae7920daa51649b2213e9642bdf4b1')]             |
| ['Свинарчук Алексей Леонидович']  | ['alexsv14@mail.ru']      | ['73833357703'] |                                                    |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='alexsv14@mail.ru', password_hash='e^2C5Xt+2db1eb62e44cc5e422beed93845f6e60')]       |
| ['Иванович Григорий Шевченко']    | ['grigoryotts@yandex.ru'] |                 |                                                    |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='grigoryotts@yandex.ru', password_hash='M5z)\\J4ma4f4c257945c0176cd878be206c35a3d')] |
| ['Донгузов Эдуард Александрович'] | ['eddon@mail.ru']         | ['79659189835'] |                                                    |   nan | 13.01.1981   | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='eddon@mail.ru', password_hash='9]tA%8mRf957ae8467db1e2cfc4331c603de451a')]          |
| ['Лаптев Вадим Владимирович']     | ['vadim_laptev@mail.ru']  |                 |                                                    |   nan |              | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='vadim_laptev@mail.ru', password_hash='4258fe59de66b65bd11583cd868207b3')]           |
| ['Александрович Алексей Ожован']  | ['ozhovan@gmail.com']     |                 |                                                    |   nan | 27.01.1977   | [Row(title='Официальный сайт компании Нанософт', link='https://nanocad.ru/', login='ozhovan@gmail.com', password_hash='uL]2oN#1e185a43d8c6abfaad92fbee0ff574728')]      |
```