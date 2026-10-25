# Parsetron results

## About row data

> - Code name: index_0574
> - File path: *_output.csv
> - Total rows: 1362820

### Schema
```
root
 |-- uid: integer (nullable = true)
 |-- apartment_ru: string (nullable = true)
 |-- street_ru: string (nullable = true)
 |-- city_ru: string (nullable = true)
 |-- postcode: string (nullable = true)
 |-- region_ru: string (nullable = true)
 |-- normalized_address: string (nullable = true)
 |-- latitude: string (nullable = true)
 |-- longitude: string (nullable = true)
 |-- geocoding_confidence: string (nullable = true)
 |-- source_dataset: string (nullable = true)
 |-- organisation: string (nullable = true)
 |-- firstname_ru: string (nullable = true)
 |-- surname_ru: string (nullable = true)
 |-- middlename_ru: string (nullable = true)
 |-- fullname_ru: string (nullable = true)
 |-- dob: string (nullable = true)
 |-- registrationdoc: string (nullable = true)
 |-- passport: string (nullable = true)
 |-- passport2: string (nullable = true)
 |-- passport3: string (nullable = true)
 |-- email: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- email3: string (nullable = true)
 |-- email4: string (nullable = true)
 |-- phone: long (nullable = true)
 |-- phone2: string (nullable = true)
 |-- phone3: string (nullable = true)
 |-- phone4: string (nullable = true)
 |-- ogrn: string (nullable = true)
 |-- ogrn2: string (nullable = true)
 |-- inn: string (nullable = true)
 |-- inn2: string (nullable = true)
 |-- kpp: string (nullable = true)
 |-- kpp2: string (nullable = true)
 |-- vehicle: string (nullable = true)
 |-- registranttype: string (nullable = true)
 |-- comments: string (nullable = true)
 |-- comments2: string (nullable = true)
 |-- relative_surname: string (nullable = true)
 |-- relative_firstname: string (nullable = true)
 |-- relative_middlename: string (nullable = true)
 |-- relative_dob: string (nullable = true)
 |-- relative_phone: string (nullable = true)
 |-- import_timestamp: timestamp (nullable = true)
 |-- coordinates: string (nullable = true)
 |-- address2: string (nullable = true)
 |-- socialmedia1: string (nullable = true)
 |-- socialmedia2: string (nullable = true)
 |-- socialmedia3: string (nullable = true)
 |-- job_title: string (nullable = true)
 |-- employer: string (nullable = true)
 |-- vehicleplate: string (nullable = true)
 |-- vehicleregistration: string (nullable = true)
 |-- vehiclecolour: string (nullable = true)
 |-- snils: string (nullable = true)
 |-- documenttype: string (nullable = true)
 |-- activitysector: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- datasetdate: string (nullable = true)
 |-- issuingoffice: string (nullable = true)
 |-- medcenter: string (nullable = true)
 |-- is_parsed: boolean (nullable = true)
 |-- country_ru: string (nullable = true)
 |-- building_ru: string (nullable = true)
 |-- address_hash: long (nullable = true)
 |-- parse_quality: integer (nullable = true)
 |-- geom: string (nullable = true)
 |-- district_ru: string (nullable = true)

```

### Data sample
```
|      uid |   apartment_ru | street_ru         | city_ru   | postcode   | region_ru   | normalized_address   | latitude   | longitude   | geocoding_confidence   | source_dataset   | organisation   | firstname_ru   | surname_ru   | middlename_ru   | fullname_ru                    | dob   | registrationdoc   | passport   | passport2   | passport3   | email   | email2   | email3   | email4   |       phone | phone2   | phone3   | phone4   | ogrn   | ogrn2   | inn   | inn2   | kpp   | kpp2   | vehicle   | registranttype   | comments   | comments2   | relative_surname   | relative_firstname   | relative_middlename   | relative_dob   | relative_phone   | import_timestamp           | coordinates   | address2   | socialmedia1   | socialmedia2   | socialmedia3   | job_title   | employer   | vehicleplate   | vehicleregistration   | vehiclecolour   | snils   | documenttype   | activitysector   | ip   | datasetdate   | issuingoffice   | medcenter   | is_parsed   | country_ru   | building_ru                        |   address_hash |   parse_quality | geom   | district_ru   |
|---------:|---------------:|:------------------|:----------|:-----------|:------------|:---------------------|:-----------|:------------|:-----------------------|:-----------------|:---------------|:---------------|:-------------|:----------------|:-------------------------------|:------|:------------------|:-----------|:------------|:------------|:--------|:---------|:---------|:---------|------------:|:---------|:---------|:---------|:-------|:--------|:------|:-------|:------|:-------|:----------|:-----------------|:-----------|:------------|:-------------------|:---------------------|:----------------------|:---------------|:-----------------|:---------------------------|:--------------|:-----------|:---------------|:---------------|:---------------|:------------|:-----------|:---------------|:----------------------|:----------------|:--------|:---------------|:-----------------|:-----|:--------------|:----------------|:------------|:------------|:-------------|:-----------------------------------|---------------:|----------------:|:-------|:--------------|
| 24790567 |            111 | УЛ КОВАЛЕВА УЛДОМ |           |            |             |                      |            |             |                        | 1Casio 2024      |                | СЕРГЕЙ         | ЗАХАРЕНКО    | ЮРЬЕВИЧ         | ЗАХАРЕНКО СЕРГЕЙ ЮРЬЕВИЧ       |       |                   |            |             |             |         |          |          |          | 79035679677 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:00.273000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 24805952 |            369 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | ОЛЬГА          | ЧУКАЛОВСКАЯ  | ВЛАДИМИРОВНА    | ЧУКАЛОВСКАЯ ОЛЬГА ВЛАДИМИРОВНА |       |                   |            |             |             |         |          |          |          | 79037342093 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:00.273000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2365149185 |               1 |        |               |
| 24807555 |              7 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | ИРИНА          | САРКИСЯН     | ПЕТРОВНА        | САРКИСЯН ИРИНА ПЕТРОВНА        |       |                   |            |             |             |         |          |          |          | 79037454995 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:00.273000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 24807559 |             20 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | ЭДУАРД         | КРАСНИКОВ    | АЛЕКСЕЕВИЧ      | КРАСНИКОВ ЭДУАРД АЛЕКСЕЕВИЧ    |       |                   |            |             |             |         |          |          |          | 79037455233 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:00.273000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 24807561 |             26 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | АЛЕКСАНДР      | РУМЯНЦЕВ     | ВАЛЕРЬЕВИЧ      | РУМЯНЦЕВ АЛЕКСАНДР ВАЛЕРЬЕВИЧ  |       |                   |            |             |             |         |          |          |          | 79037455345 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:00.273000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 24740844 |             20 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | ЛАРИСА         | РОМАНОВА     | АНАТОЛЬЕВНА     | РОМАНОВА ЛАРИСА АНАТОЛЬЕВНА    |       |                   |            |             |             |         |          |          |          | 79001970984 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:00.273000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 24741997 |                |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | МАКСИМ         | БОБРОВ       | АНАТОЛЬЕВИЧ     | БОБРОВ МАКСИМ АНАТОЛЬЕВИЧ      |       |                   |            |             |             |         |          |          |          | 79004887692 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:00.273000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              | Борисовка 1-й кв-лдом -корпус 7    |     2295626707 |               1 |        |               |
| 24741998 |             36 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | АЛЕФТИНА       | ВОРОНКОВА    | СЕРГЕЕВНА       | ВОРОНКОВА АЛЕФТИНА СЕРГЕЕВНА   |       |                   |            |             |             |         |          |          |          | 79004892304 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:00.273000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 25092349 |              8 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | АЛЕКСАНДР      | СКОБЛИКОВ    | НИКОЛАЕВИЧ      | СКОБЛИКОВ АЛЕКСАНДР НИКОЛАЕВИЧ |       |                   |            |             |             |         |          |          |          | 79167971458 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:00.273000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     1837305885 |               1 |        |               |
| 25607663 |             13 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | ВЛАДИМИР       | ЦВЕТКОВ      | НИКОЛАЕВИЧ      | ЦВЕТКОВ ВЛАДИМИР НИКОЛАЕВИЧ    |       |                   |            |             |             |         |          |          |          | 79104260915 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 25607665 |              1 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | АНДРЕЙ         | КАБАНОВ      | ВЛАДИМИРОВИЧ    | КАБАНОВ АНДРЕЙ ВЛАДИМИРОВИЧ    |       |                   |            |             |             |         |          |          |          | 79104261107 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 25623907 |             93 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | ЮЛИЯ           | НОВИКОВА     | АЛЕКСАНДРОВНА   | НОВИКОВА ЮЛИЯ АЛЕКСАНДРОВНА    |       |                   |            |             |             |         |          |          |          | 79154741171 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2365149185 |               1 |        |               |
| 25623909 |             75 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | ОЛЕСЯ          | ЦЫХМАЙСТРУК  | АЛЕКСЕЕВНА      | ЦЫХМАЙСТРУК ОЛЕСЯ АЛЕКСЕЕВНА   |       |                   |            |             |             |         |          |          |          | 79154741599 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2365149185 |               1 |        |               |
| 25630040 |            536 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | СЕРГЕЙ         | КОНЬКОВ      | ВАСИЛЬЕВИЧ      | КОНЬКОВ СЕРГЕЙ ВАСИЛЬЕВИЧ      |       |                   |            |             |             |         |          |          |          | 79161408683 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 25630041 |             27 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | ЮЛИЯ           | БАРАНЕНКОВА  | ВАЛЕРЬЕВНА      | БАРАНЕНКОВА ЮЛИЯ ВАЛЕРЬЕВНА    |       |                   |            |             |             |         |          |          |          | 79161408764 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 25630043 |            101 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | ВИТАЛИЙ        | ЛИПСКИЙ      | АНАТОЛЬЕВИЧ     | ЛИПСКИЙ ВИТАЛИЙ АНАТОЛЬЕВИЧ    |       |                   |            |             |             |         |          |          |          | 79161409476 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 25630045 |              5 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | СЕРГЕЙ         | СОЛЕНКОВ     | ВИКТОРОВИЧ      | СОЛЕНКОВ СЕРГЕЙ ВИКТОРОВИЧ     |       |                   |            |             |             |         |          |          |          | 79161409546 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 25557320 |            110 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | ЕВГЕНИЙ        | ПАНОВ        | ВЛАДИМИРОВИЧ    | ПАНОВ ЕВГЕНИЙ ВЛАДИМИРОВИЧ     |       |                   |            |             |             |         |          |          |          | 79032305636 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 25557322 |             12 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | НИКОЛАЙ        | ВОРОБЬЕВ     | ВАСИЛЬЕВИЧ      | ВОРОБЬЕВ НИКОЛАЙ ВАСИЛЬЕВИЧ    |       |                   |            |             |             |         |          |          |          | 79032305841 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |                                    |     2295626707 |               1 |        |               |
| 25557325 |             28 |                   |           |            |             |                      |            |             |                        | 1Casio 2024      |                | СЕРГЕЙ         | СЕЛЕЗНЕВ     | ФЕДОРОВИЧ       | СЕЛЕЗНЕВ СЕРГЕЙ ФЕДОРОВИЧ      |       |                   |            |             |             |         |          |          |          | 79032306046 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 14:52:45.463000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              | Спартаковская улдом 7корпус -кв.28 |     2295626707 |               1 |        |               |
```


## About final data
> - Total rows: 1356294

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 100.00% |



### Data sample
```
| names                              | phones          |
|:-----------------------------------|:----------------|
| ['Ольховская Дарья Валерьевна']    | ['79634681350'] |
| ['Земцова Елена Владимировна']     | ['79031250117'] |
| ['Розанова Екатерина Алексеевна']  | ['79262547182'] |
| ['Зайцева Наталья Ивановна']       | ['79271550371'] |
| ['Буреева Алсу Камилевна']         | ['79272433527'] |
| ['Гитинова Марьям Гаджиевна']      | ['79282761703'] |
| ['Фомина Светлана Николаевна']     | ['79289682270'] |
| ['Абдуллаев Чархан Зайнулдинович'] | ['79633733810'] |
| ['Колмыков Сергей Николаевич']     | ['79067730474'] |
| ['Мальцева Олеся Андреевна']       | ['79068297372'] |
| ['Мальцева Людмила Ивановна']      | ['79085933400'] |
| ['Бобровский Борис Вениаминович']  | ['79153214066'] |
| ['Федоткин Виктор Иванович']       | ['79139520545'] |
| ['Поцелуев Евгений Александрович'] | ['79153481793'] |
| ['Дерягина Ульяна Викторовна']     | ['79104735241'] |
| ['Вайнбендер Сергей Федорович']    | ['79194693954'] |
| ['Новиков Владимир Борисович']     | ['79265096080'] |
| ['Хворых Дмитрий Михайлович']      | ['79268989977'] |
| ['Селиверстов Федор Алексеевич']   | ['79269019504'] |
| ['Бабичев Виктор Иванович']        | ['79293510971'] |
```