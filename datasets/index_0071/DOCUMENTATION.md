# Parsetron results

## About row data

> - File path: skyeng.ru.txt
> - Total rows: 7442069

### Schema
```
root
 |-- Имя: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Часовой пояс: string (nullable = true)
 |-- Адрес: string (nullable = true)
 |-- Страна: string (nullable = true)
 |-- Skype: string (nullable = true)
 |-- Логин: string (nullable = true)

```

### Data sample
```
| Имя                   | Фамилия               | Почта                                                  |   Номер телефона | Дата рождения   | Часовой пояс   | Адрес                                   | Страна   | Skype          | Логин                                                  |
|:----------------------|:----------------------|:-------------------------------------------------------|-----------------:|:----------------|:---------------|:----------------------------------------|:---------|:---------------|:-------------------------------------------------------|
|                       |                       | huaweiuprk@gmail.com                                   |                  |                 |                |                                         |          |                | huaweiuprk@gmail.com                                   |
| Testwshaashkid        |                       | testneworderwshaashkid9684948@guerrillamail.com        |      79238191776 |                 |                | Красноярский край                       | RU       | skypeNorZoi    | testneworderwshaashkid9684948@guerrillamail.com        |
|                       |                       | yana-stepanenko-2002@mail.ru                           |                  |                 |                |                                         |          |                | yana-stepanenko-2002@mail.ru                           |
| TestjulkentutorNaN    | Testgulbartutornu     | testolympregjulkentutornan2120850@guerrillamail.com    |      79899740258 |                 |                | Ставропольский край                     | RU       |                | testolympregjulkentutornan2120850@guerrillamail.com    |
| Testclyheild          | Testtowmulld          | skyengtests+testsuclyheild866@gmail.com                |      79675939235 | 1990.01.12      |                | Санкт-Петербург и Ленинградская область | RU       | MatBenskype    | skyengtests+testsuclyheild866@gmail.com                |
| Testdadrosmondrtinput | Testdadkshschdrtinput | testolympregdadrosmondrtinput9897313@guerrillamail.com |      79983194698 |                 |                |                                         | RU       |                | testolympregdadrosmondrtinput9897313@guerrillamail.com |
| Testxvcwincordad      |                       | testxvcwincordad4@guerrillamail.com                    |      79741286500 |                 |                |                                         | RU       |                | papers2467                                             |
| Testxvckidwincorjun   |                       | testxvcwincordad4@guerrillamail.com                    |      79741286500 | 2001.04.07      |                |                                         | RU       |                | testxvcwincordad4@guerrillamail.com                    |
| Testdrtrosmonkid      | Testdrtkshschkid      |                                                        |                  | 2005.08.01      |                |                                         |          |                | produced6635                                           |
| Али                   | Мисиров               | misirov.aleihan@yandex.ru                              |      79047940101 |                 |                | Нижегородская область                   | RU       | livevaqifmaisu | misirov.aleihan@yandex.ru                              |
| Testjulkennukid       | Testgulbarnukid       |                                                        |                  |                 |                |                                         |          |                | doll2889                                               |
| Мария                 |                       | maria.elmeeva@gmail.com                                |      79500202676 |                 |                | Санкт-Петербург и Ленинградская область | RU       | mary19015      | maria.elmeeva@gmail.com                                |
|                       |                       | julija-vojjtova@mail.ru                                |                  |                 |                |                                         |          |                | julija-vojjtova@mail.ru                                |
|                       |                       | elimesovtimur@gmail.com                                |                  |                 |                |                                         |          |                | elimesovtimur@gmail.com                                |
| Валя                  | Ушакова               | valyaushakova@mail.ru                                  |                  |                 |                |                                         |          |                | 189e3da1-014d-430b-a36a-b250c10777de                   |
| Testtchqqrlacsal      | Testtchqqrkihchr      | testtchqqrlacsal1@guerrillamail.com                    |      79871423974 |                 |                | Республика Башкортостан                 | RU       |                | testtchqqrlacsal1@guerrillamail.com                    |
| Testvvjandjerdad      |                       | testvvjandjerdad4@guerrillamail.com                    |      79922216014 |                 |                | Пермский край                           | RU       |                | vacuum7106                                             |
| Testvvjkidandjerjun   |                       | testvvjandjerdad4@guerrillamail.com                    |      79922216014 | 2001.04.07      |                | Пермский край                           | RU       |                | testvvjandjerdad4@guerrillamail.com                    |
| Bota                  |                       | balbota_94@mail.ru                                     |      79003621825 |                 |                | Брянская область                        | RU       | livebalbota_94 | balbota_94@mail.ru                                     |
| Testaditya            | Testritchie           |                                                        |                  |                 |                |                                         |          |                | chart7318                                              |
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
 |-- birth_date: string (nullable = true)
 |-- address: string (nullable = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 85.38% |
| Phones | 81.17% |
| Birth_date | 0.00% |
| Address | 0.00% |
| Socials | 0.00% |



### Data sample
```
| names                    | emails                           | phones          | birth_date   | address   | socials   |
|:-------------------------|:---------------------------------|:----------------|:-------------|:----------|:----------|
| ['- Белова Лиза']        | ['lizok2008belov@gmail.com']     |                 |              |           |           |
| ['-Ибраева Асель']       | ['aish.ibrayeva@icloud.com']     |                 |              |           |           |
| ['-Клименко -Никита']    |                                  | ['79150662020'] |              |           |           |
| ['-Смоленцева Марина']   | ['marina_novikova_72@bk.ru']     | ['79814317913'] |              |           |           |
| ['-Стульнева Екатерина'] | ['stulneva.ekaterina@gmail.com'] | ['79776283505'] |              |           |           |
| ['-Сысуева Ксения']      | ['sysuevaksenia118@gmail.com']   | ['79520770564'] |              |           |           |
| ['.. Bdfy']              | ['fomin.ivan2000@mail.ru']       | ['79250342432'] |              |           |           |
| ['.. Daria']             | ['daria.lipovaya@gmail.com']     | ['79854538390'] |              |           |           |
| ['.. Антон']             | ['a.popov@adwise.ru']            | ['79257274575'] |              |           |           |
| ['.Звонить В Ск Егор']   | ['bk515@live.ru']                | ['79250211885'] |              |           |           |
| ['A Abdurahman Samira']  | ['samira29382@gmail.com']        |                 |              |           |           |
| ['A Alexander']          | ['alexonglobe@gmail.com']        | ['79150035076'] |              |           |           |
| ['A Alexey']             | ['kenwood2004@list.ru']          | ['79136080034'] |              |           |           |
| ['A Mario']              | ['mariogiovanniarce@gmail.com']  |                 |              |           |           |
| ['A Natasha']            | ['nattttttttasha@gmail.com']     | ['79772992982'] |              |           |           |
| ['A Pavel']              | ['pashaavlasev@gmail.com']       |                 |              |           |           |
| ['A Prasath']            | ['aprasath1092@gmail.com']       |                 |              |           |           |
| ['A Remzi']              | ['040390.dk@gmail.com']          |                 |              |           |           |
| ['A Timur']              | ['t.arkhanguelsky@gmail.com']    | ['79999674372'] |              |           |           |
| ['A Van']                | ['teweya1952@quick-mail.cc']     | ['79771023212'] |              |           |           |
```