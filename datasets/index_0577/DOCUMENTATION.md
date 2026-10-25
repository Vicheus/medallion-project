# Parsetron results

## About row data

> - File path: Xarakiri RU.csv
> - Total rows: 101447

### Schema
```
root
 |-- uid: integer (nullable = true)
 |-- address_ru: string (nullable = true)
 |-- apartment_ru: string (nullable = true)
 |-- house_ru: string (nullable = true)
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
 |-- phone: string (nullable = true)
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
 |-- address_hash: string (nullable = true)
 |-- parse_quality: integer (nullable = true)
 |-- geom: string (nullable = true)
 |-- district_ru: string (nullable = true)

```

### Data sample
```
|      uid | address_ru   | apartment_ru   | house_ru   | street_ru   | city_ru   | postcode   | region_ru   | normalized_address   | latitude   | longitude   | geocoding_confidence   | source_dataset   | organisation   | firstname_ru   | surname_ru   | middlename_ru   | fullname_ru                 | dob   | registrationdoc   | passport   | passport2   | passport3   | email                   | email2   | email3   | email4   |       phone | phone2   | phone3   | phone4   | ogrn   | ogrn2   | inn   | inn2   | kpp   | kpp2   | vehicle   | registranttype   | comments   | comments2   | relative_surname   | relative_firstname   | relative_middlename   | relative_dob   | relative_phone   | import_timestamp           | coordinates   | address2   | socialmedia1   | socialmedia2   | socialmedia3   | job_title   | employer   | vehicleplate   | vehicleregistration   | vehiclecolour   | snils   | documenttype   | activitysector   | ip   | datasetdate   | issuingoffice   | medcenter   | is_parsed   | country_ru   | building_ru   | address_hash   |   parse_quality | geom   | district_ru   |
|---------:|:-------------|:---------------|:-----------|:------------|:----------|:-----------|:------------|:---------------------|:-----------|:------------|:-----------------------|:-----------------|:---------------|:---------------|:-------------|:----------------|:----------------------------|:------|:------------------|:-----------|:------------|:------------|:------------------------|:---------|:---------|:---------|------------:|:---------|:---------|:---------|:-------|:--------|:------|:-------|:------|:-------|:----------|:-----------------|:-----------|:------------|:-------------------|:---------------------|:----------------------|:---------------|:-----------------|:---------------------------|:--------------|:-----------|:---------------|:---------------|:---------------|:------------|:-----------|:---------------|:----------------------|:----------------|:--------|:---------------|:-----------------|:-----|:--------------|:----------------|:------------|:------------|:-------------|:--------------|:---------------|----------------:|:-------|:--------------|
| 25813697 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | УТКИНА         |              |                 | УТКИНА                      |       |                   |            |             |             | dasha.u-19@mail.ru      |          |          |          | 79166836424 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25813831 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | ВИКТОРИЯ       |              |                 | ВИКТОРИЯ                    |       |                   |            |             |             | leksa892@rambler.ru     |          |          |          | 79613534815 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25814051 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | МАРИНА         |              | СЕРГЕЕВНА       | МАРИНА СЕРГЕЕВНА            |       |                   |            |             |             | bms0121@bk.ru           |          |          |          | 79263867212 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25786865 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | АНДРЕЙ         | ИВАНОВ       |                 | ИВАНОВ АНДРЕЙ               |       |                   |            |             |             | apavlad@rambler.ru      |          |          |          | 79607360154 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25814117 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | СУШКОВ         |              |                 | СУШКОВ                      |       |                   |            |             |             | oleg.sushckov@yandex.ru |          |          |          | 79179944414 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25787166 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | ОЛЬГА          |              |                 | ОЛЬГА                       |       |                   |            |             |             | e_vita@list.ru          |          |          |          | 79036477518 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25787168 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | ВИКТОР         | СИДОРОВ      | ИЛЬИЧ           | СИДОРОВ ВИКТОР ИЛЬИЧ        |       |                   |            |             |             | sidvik98@mail.ru        |          |          |          | 79687401735 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25814781 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | СТЕЛЛА         |              |                 | СТЕЛЛА                      |       |                   |            |             |             | black_star84@mail.ru    |          |          |          | 79030079777 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25814783 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | ШАМИЛОВА       | ЯНА          |                 | ШАМИЛОВА ЯНА                |       |                   |            |             |             | chakuch1@rambler.ru     |          |          |          | 79269262071 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25815054 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | ЕКАТЕРИНА      |              |                 | ЕКАТЕРИНА                   |       |                   |            |             |             | katty072007@bk.ru       |          |          |          | 79067291193 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25786870 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | АЛЕКСАНДР      | КИЧАГИН      | АНДРЕЕВИЧ       | КИЧАГИН АЛЕКСАНДР АНДРЕЕВИЧ |       |                   |            |             |             | klop20007@ya.ru         |          |          |          | 79295561691 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25815184 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | ВАЛЕРИЙ        |              |                 | ВАЛЕРИЙ                     |       |                   |            |             |             | valerij1502@mail.ru     |          |          |          | 79111775756 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25787290 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | САЛАЕВ         | АРМАН        |                 | САЛАЕВ АРМАН                |       |                   |            |             |             | mamedshah28@gmail.com   |          |          |          | 79856909010 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25787291 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | АЛИНА          | КРАПИВА      | ИГОРЕВНА        | КРАПИВА АЛИНА ИГОРЕВНА      |       |                   |            |             |             | krapiva_alina@list.ru   |          |          |          | 79969646355 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25848776 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | АЛЕКСАНДР      |              |                 | АЛЕКСАНДР                   |       |                   |            |             |             | sergei.bubka@rambler.ru |          |          |          | 79267090927 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25815901 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | ИВАН           |              |                 | ИВАН                        |       |                   |            |             |             | manaca96@mail.ru        |          |          |          | 79667563577 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25816112 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | АНДРЕЙ         |              | НИКОЛАЕВИЧ      | АНДРЕЙ НИКОЛАЕВИЧ           |       |                   |            |             |             | antri@inbox.ru          |          |          |          | 79096894422 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25816115 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | КРИСИНА        | ЕФИМОВА      |                 | ЕФИМОВА КРИСИНА             |       |                   |            |             |             | christina_90@bk.ru      |          |          |          | 79153609797 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25816459 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | БРАЖКИН        |              |                 | БРАЖКИН А. Б.               |       |                   |            |             |             | binituks@gmail.com      |          |          |          | 79031957919 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
| 25817365 |              |                |            |             |           |            |             |                      |            |             |                        | Xarakiri RU      |                | ЕВГЕНИЙ        |              |                 | ЕВГЕНИЙ                     |       |                   |            |             |             | 544355@list.ru          |          |          |          | 79096211498 |          |          |          |        |         |       |        |       |        |           |                  |            |             |                    |                      |                       |                |                  | 2025-06-14 16:55:07.238000 |               |            |                |                |                |             |            |                |                       |                 |         |                |                  |      |               |                 |             | True        |              |               |                |               0 |        |               |
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

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 83.62% |
| Emails | 99.97% |



### Data sample
```
| names                                | phones          | emails                            |
|:-------------------------------------|:----------------|:----------------------------------|
| ['Capt Igor Filyushin']              | ['79882457773'] | ['filyushini2003@mail.ru']        |
| ['Curbanov Laurentia']               |                 | ['lcurbanov@gmail.com']           |
| ['Kostina Olga Sergeevna']           | ['79671687026'] | ['olyakost_1990@mail.ru']         |
| ['Oleg']                             | ['79263573494'] | ['ob26061978@yandex.ru']          |
| ['Pivoshenko Oksana']                |                 | ['ksyha1969@yandex.ru']           |
| ['Vasily Korzhavin']                 | ['79654942055'] | ['lolouyhter34@gmail.com']        |
| ['Абакшина Ирина Александровна']     | ['79610173110'] | ['abakshina86@mail.ru']           |
| ['Абду Хамди']                       |                 | ['olga_hamdy@mail.ru']            |
| ['Абрамцова Татьяна Александровна']  | ['79277767467'] | ['t.a.abramcova@mail.ru']         |
| ['Авазов Артур Рустемович']          | ['79138846018'] | ['arturavazov@yandex.ru']         |
| ['Аверин Александр Сергеевич']       | ['79169461402'] | ['dirty_sasha@mail.ru']           |
| ['Авсецына Анастасия']               | ['79517661831'] | ['nastushenok1990@mail.ru']       |
| ['Агаджанова Марина Алексеевна']     | ['79263119378'] | ['lika.krasota19@yandex.ru']      |
| ['Агафонов Александр Александрович'] |                 | ['sanuch84@gmail.com']            |
| ['Айзин Михаил']                     |                 | ['sm8166@yandex.ru']              |
| ['Александр']                        | ['79055275390'] | ['hackkers@mail.ru']              |
| ['Александр']                        | ['79057314098'] | ['rassizm2002@mail.ru']           |
| ['Александр Грузин']                 |                 | ['tmbaby@nm.ru']                  |
| ['Александр Овчинников']             | ['79854124928'] | ['alexandrovchinnikov@yandex.ru'] |
| ['Алексеева Дарья Александровна']    | ['79136708344'] | ['plodojorka91@mail.ru']          |
```