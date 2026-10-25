# Parsetron results

## About row data

> - File path: Eyekraft.csv
> - Total rows: 1048575

### Schema
```
root
 |-- uid: integer (nullable = true)
 |-- address_ru: string (nullable = true)
 |-- apartment_ru: string (nullable = true)
 |-- house_ru: string (nullable = true)
 |-- street_ru: string (nullable = true)
 |-- city_ru: string (nullable = true)
 |-- postcode: integer (nullable = true)
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
 |-- snils: double (nullable = true)
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
|      uid | address_ru           | apartment_ru   |   house_ru | street_ru   | city_ru              |   postcode | region_ru   | normalized_address   | latitude   | longitude   | geocoding_confidence   | source_dataset   | organisation   | firstname_ru   | surname_ru   | middlename_ru   | fullname_ru                        | dob        | registrationdoc   |   passport | passport2   | passport3   | email   | email2   | email3   | email4   |       phone | phone2   | phone3   | phone4   | ogrn   | ogrn2   | inn   | inn2   | kpp   | kpp2   | vehicle   | registranttype   | comments   | comments2   | relative_surname   | relative_firstname   | relative_middlename   | relative_dob   | relative_phone   | import_timestamp           | coordinates   | address2   | socialmedia1   | socialmedia2   | socialmedia3   | job_title   | employer   | vehicleplate   | vehicleregistration   | vehiclecolour   |   snils | documenttype   | activitysector   | ip   | datasetdate   | issuingoffice   | medcenter   | is_parsed   | country_ru   | building_ru   |   address_hash |   parse_quality | geom   | district_ru   |
|---------:|:---------------------|:---------------|-----------:|:------------|:---------------------|-----------:|:------------|:---------------------|:-----------|:------------|:-----------------------|:-----------------|:---------------|:---------------|:-------------|:----------------|:-----------------------------------|:-----------|:------------------|-----------:|:------------|:------------|:--------|:---------|:---------|:---------|------------:|:---------|:---------|:---------|:-------|:--------|:------|:-------|:------|:-------|:----------|:-----------------|:-----------|:------------|:-------------------|:---------------------|:----------------------|:---------------|:-----------------|:---------------------------|:--------------|:-----------|:---------------|:---------------|:---------------|:------------|:-----------|:---------------|:----------------------|:----------------|--------:|:---------------|:-----------------|:-----|:--------------|:----------------|:------------|:------------|:-------------|:--------------|---------------:|----------------:|:-------|:--------------|
| 75727174 | Сургут               |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                |                |              |                 |                                    | 27/03/1996 |                   |            |             |             |         |          |          |          | 79224538808 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727176 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                |                |              |                 |                                    |            |                   |  308880665 |             |             |         |          |          |          | 79186420901 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727180 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                | БАКТЫКАН       | МЕЙМАНАЛИЕВА | ШАРЫПБЕКОВНА    | МЕЙМАНАЛИЕВА БАКТЫКАН ШАРЫПБЕКОВНА | 13/05/1975 |                   |            |             |             |         |          |          |          | 79146420324 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727181 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                |                |              |                 |                                    | 27/10/1968 |                   |            |             |             |         |          |          |          | 79085951713 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727182 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                | ВЛАДИМИР       | ГРУДИНСКИЙ   | АЛЕКСАНДРОВИЧ   | ГРУДИНСКИЙ ВЛАДИМИР АЛЕКСАНДРОВИЧ  | 18/01/2018 |                   |            |             |             |         |          |          |          | 79166953020 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727178 | Чехов Ленина 1       |                |          1 |             | Чехов Ленина 1       |        nan |             | Чехов Ленина 1       |            |             |                        | Eyekraft         |                | АЛЕКСАНДР      | СУЕТИН       |                 | АЛЕКСАНДР СУЕТИН                   | 02/03/1982 |                   |            |             |             |         |          |          |          | 79161231998 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |    3.51398e+09 |               1 |        |               |
| 75727185 | Иманбаева 101        |                |        101 |             | Иманбаева 101        |        nan |             | Иманбаева 101        |            |             |                        | Eyekraft         |                |                |              |                 |                                    | 04/10/1999 |                   |            |             |             |         |          |          |          | 77072970343 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |    7.53973e+09 |               1 |        |               |
| 75727186 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                |                |              |                 |                                    | 05/06/1967 |                   |            |             |             |         |          |          |          | 79174727888 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727187 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                | ПЕЛАГЕЯ        | ЛЕОНОВА      | СЕРГЕЕВНА       | ЛЕОНОВА ПОЛИНА СЕРГЕЕВНА           | 03/09/2002 |                   |            |             |             |         |          |          |          | 79002119088 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727188 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                |                |              |                 |                                    | 31/10/2006 |                   |            |             |             |         |          |          |          | 79133836929 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727189 | Россия               |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                |                |              |                 |                                    | 17/10/1961 |                   |            |             |             |         |          |          |          | 79262176569 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727190 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                | МИХАИЛ         | РЯБИНИН      | ДМИТРИЕВИЧ      | РЯБИНИН МИХАИЛ ДМИТРИЕВИЧ          | 26/01/1998 |                   |            |             |             |         |          |          |          | 79164051083 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727191 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                | ВЛАДИМИР       | КАШИРИН      | МИХАЙЛОВИЧ      | КАШИРИН ВЛАДИМИР МИХАЙЛОВИЧ        | 18/08/1974 |                   |            |             |             |         |          |          |          | 79043789897 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727192 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                | ЧАСТНОЕ        | ЛИЦО         | ЧЛ              | ЧАСТНОЕ ЛИЦО ЧЛ                    | 15/05/2001 |                   |            |             |             |         |          |          |          | 79243055991 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727193 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                |                |              |                 |                                    | 25/10/1969 |                   |            |             |             |         |          |          |          | 79272612064 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727194 | Москва Люблинская 59 |                |         59 |             | Москва Люблинская 59 |        nan | МОСКВА      | Москва Люблинская 59 |            |             |                        | Eyekraft         |                | ЖАННА          | ИВАНОВА      |                 | ЖАННА ИВАНОВА                      | 11/08/1984 |                   |            |             |             |         |          |          |          | 79168602388 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |    1.06846e+09 |               1 |        |               |
| 75727196 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                | МОСОЛИТИНА     | ЯНА          |                 | МОСОЛИТИНА ЯНА                     | 13/01/1989 |                   |            |             |             |         |          |          |          | 79258050837 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727197 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                | АЛЕКСАНДР      | БЫКОВ        |                 | БЫКОВ АЛЕКСАНДР                    | 02/04/1984 |                   |            |             |             |         |          |          |          | 79177125099 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727198 |                      |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                |                |              |                 |                                    | 30/05/1962 |                   |            |             |             |         |          |          |          | 79067671625 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
| 75727199 | Челябинск            |                |            |             |                      |        nan |             |                      |            |             |                        | Eyekraft         |                | ЕЛЕНА          | КОДИНА       | НИКОЛАЕВНА      | КОДИНА ЕЛЕНА НИКОЛАЕВНА            | 23/12/1994 |                   |            |             |             |         |          |          |          | 79193278327 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 21:49:12.287000 |               |            |                |                |                |             |            |                |                       |                 |     nan |                |                  |      |               |                 |             | True        |              |               |  nan           |               0 |        |               |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 81.87% |
| Phones | 100.00% |
| Emails | 0.68% |
| Address | 41.93% |
| Documents | 9.28% |



### Data sample
```
| names                                  | birth_date   | phones          | emails   | address                                                      | documents                                                                                                                 |
|:---------------------------------------|:-------------|:----------------|:---------|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| ['- Анастасия']                        | 04.03.2002   | ['79166375557'] |          | ['Москва']                                                   |                                                                                                                           |
| ['- Елена']                            | 01.01.1981   | ['79161359384'] |          |                                                              |                                                                                                                           |
| ['- Рафаэль -']                        | 03.08.1971   | ['79221883838'] |          | ['Березовский Загвозкина 76']                                |                                                                                                                           |
| ['- Татьяна -']                        | 11.01.1958   | ['79164839624'] |          | ['Москва Кутузовский 3895']                                  |                                                                                                                           |
| ['-Кулев Евгений Владимирович-']       |              | ['79222539254'] |          |                                                              |                                                                                                                           |
| ['-Леонов Сергей-']                    |              | ['79160779259'] |          |                                                              |                                                                                                                           |
| ['Afonina Olga Vladimirovna']          | 25.05.1983   | ['79055408211'] |          |                                                              |                                                                                                                           |
| ['Aleksandr Kanatov']                  | 15.07.1992   | ['79242676720'] |          |                                                              |                                                                                                                           |
| ['Aleksandr Sergeevich Ekimov']        | 26.08.1994   | ['79195072417'] |          |                                                              |                                                                                                                           |
| ['Alekseeva Anna Leonidovna']          | 21.08.1988   | ['79294038558'] |          | ['Хабаровск Федеративная 1']                                 |                                                                                                                           |
| ['Aleksey Borisov']                    | 17.11.1988   | ['79241868106'] |          |                                                              |                                                                                                                           |
| ['Aleshina Tatiana Nikolaevna']        | 26.05.1983   | ['79022230114'] |          | ['Ярославль']                                                |                                                                                                                           |
| ['Alexander Tarassenko Vladimirovich'] |              | ['79161817776'] |          |                                                              |                                                                                                                           |
| ['Alexey Anatolievich Korolchuk']      |              | ['79153844032'] |          | ['Россия Москва ул Бойцовая 4 37 3 1 6']                     | [Row(type=0, serial='4508324515', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |
| ['Alexey Dmitrievich Tsimbalist']      | 17.10.1990   | ['79150313222'] |          | ['город Москва улица Горчакова дом 1 корпус 1 квартира 100'] |                                                                                                                           |
| ['Alexey Oshchepkov']                  | 29.08.1977   | ['79029158915'] |          |                                                              |                                                                                                                           |
| ['Alimova Natalya Nikolaevna']         | 11.07.1982   | ['79035606363'] |          |                                                              |                                                                                                                           |
| ['Andreeva Irina Evgenevna']           | 03.01.2018   | ['79270274721'] |          |                                                              |                                                                                                                           |
| ['Andrey Vladimirovich Zimovin']       | 21.07.1977   | ['79133048871'] |          | ['Кемерово']                                                 |                                                                                                                           |
| ['Anna Ventsel']                       | 10.03.1968   | ['79262328388'] |          |                                                              |                                                                                                                           |
```