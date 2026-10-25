# Parsetron results

## About row data

> - File path: users_utf8.csv
> - Total rows: 12063

### Schema
```
root
 |-- us_id: integer (nullable = true)
 |-- us_key: string (nullable = true)
 |-- us_sex: string (nullable = true)
 |-- us_city: string (nullable = true)
 |-- us_pass: string (nullable = true)
 |-- us_bdate: date (nullable = true)
 |-- us_email: string (nullable = true)
 |-- us_fraza: string (nullable = true)
 |-- us_login: string (nullable = true)
 |-- us_active: boolean (nullable = true)
 |-- us_points: integer (nullable = true)
 |-- us_region: string (nullable = true)
 |-- us_comment: string (nullable = true)
 |-- us_country: string (nullable = true)
 |-- us_regtime: integer (nullable = true)
 |-- us_website: string (nullable = true)
 |-- us_comment2: string (nullable = true)
 |-- us_lasttime: string (nullable = true)
 |-- us_last_name: string (nullable = true)
 |-- us_po_design: string (nullable = true)
 |-- us_first_name: string (nullable = true)
 |-- us_time_onsite: string (nullable = true)
 |-- us_uvedomleniya: boolean (nullable = true)

```

### Data sample
```
|   us_id | us_key                           | us_sex   | us_city         | us_pass                          | us_bdate   | us_email                   | us_fraza             | us_login   | us_active   |   us_points | us_region           | us_comment   | us_country   |   us_regtime | us_website   | us_comment2                 | us_lasttime   | us_last_name   | us_po_design   | us_first_name   | us_time_onsite   | us_uvedomleniya   |
|--------:|:---------------------------------|:---------|:----------------|:---------------------------------|:-----------|:---------------------------|:---------------------|:-----------|:------------|------------:|:--------------------|:-------------|:-------------|-------------:|:-------------|:----------------------------|:--------------|:---------------|:---------------|:----------------|:-----------------|:------------------|
|      10 | 5231e7f9e4f347ecafb2c8afcb0c2192 | male     | Москва          | 1e93615b9c793e4fce2f6c8ebde83e61 | 1985-10-01 | vlad_g@bk.ru               | <blank>              | sloganbase | True        |        4957 | Московская область  | <blank>      | RU           |   1154075385 | <blank>      | копирайтер                  | 1322131602    | Лебедев        | 0              | Влад.           | 568881           | False             |
|      12 | 4553775a2d2aa2f17d463711e9190f01 | male     | Златоуст        | 70efe3b38d65f85cd28d25a0193583c3 | 1900-01-01 | liliputin7@list.ru         | <blank>              | asd777     | True        |          45 | Челябинская область | <blank>      | RU           |   1154698753 | <blank>      | <blank>                     | 1182002401    | Власов         | 0              | Евгений         | 144895           | True              |
|      13 | b1cfe578687aeed71894b9713834426c | female   | Самара          | 72c7204bd7fa89087951902cbd997032 | 1984-01-19 | paanda@list.ru             | NULL                 | Paanda     | True        |           1 | 63                  | NULL         | RU           |   1156154126 | NULL         | менеджер по рекламе         | 1167305494    | Иванова        | NULL           | Ирина           | 1405             | False             |
|      14 | 82e4f252277237ff4fed4c1a7e846c96 | male     | СПб             | c21546f9c08a185fa14c04f884a6cd69 | 1980-01-14 | nizavi@mail.ru             | NULL                 | psyhos     | True        |           0 | <blank>             | NULL         | RU           |   1156162342 | NULL         | копирайтер                  | NULL          | <blank>        | NULL           | Ян              | NULL             | False             |
|      15 | 8a71552d88e6b2f43ffadffca0e639b9 | female   | <blank>         | 1bc4794167d77cbfadd1ad88744501f9 | 1954-05-04 | sumbeka@bk.ru              | <blank>              | OLGERD     | True        |           0 | <blank>             | <blank>      | RU           |   1156183717 | <blank>      | Маркетолог                  | 0             | <blank>        | 0              | <blank>         | 0                | False             |
|      17 | cf3f9cdef3b7d92b3df75a37ab91962d | male     | Moskva          | e24a52691f9bd7fbd96595a0be3914fd | 1951-02-02 | serafimpanov@gmail.com     | <blank>              | admin      | True        |           1 | Moskva              | NULL         | RU           |   1156222526 | NULL         | FreeMan                     | 1730165491    | FreeMan        | NULL           | Gordon          | 565              | False             |
|      19 | 5638c909a49f9fffed8d85ae874a38ec | male     | Москва          | 8dddd5c939abf0e6eba0924fb4003fb4 | 1987-07-26 | timofeev@novalink.ru       | Hakuna Matata        | bedlam     | True        |        3765 | <blank>             | NULL         | RU           |   1156323491 | NULL         | <blank>                     | 1193922138    | Тимофеев       | NULL           | Денис           | 58974            | False             |
|      20 | 13d6d6812e80e822f32c385638ae8dba | male     | <blank>         | 77a2702e90613635d5558260f35a146f | 1979-12-25 | vladimir.shpak@gmail.com   | NULL                 | Vladimir   | True        |           0 | <blank>             | NULL         | UA           |   1156499269 | NULL         | <blank>                     | 1156499425    | Шпак           | NULL           | Владимир        | 130              | False             |
|      21 | 267d364335a5028f9965dad0f42f61f1 | male     | Смоленск        | e480b8334ad3befc364acddaf61a2433 | 1980-09-14 | dmitry_plus@mail.ru        | NULL                 | dmitry     | True        |           0 | Центральный         | NULL         | RU           |   1156507041 | NULL         | <blank>                     | 1158908429    | Плющенков      | NULL           | Дмитрий         | 220              | False             |
|      22 | 3b60b57a89c0d32826457ea005e74a3a | male     | Москва          | 9ccdce97b114ee496d6aca90f0d3d28f | 1984-02-23 | venix@yandex.ru            | NULL                 | Gannibal   | True        |           0 | Москва              | NULL         | RU           |   1156586402 | NULL         | Москва                      | NULL          | Барка          | NULL           | Ганнибал        | NULL             | False             |
|      23 | afa027e9f2bdda3677f6261566527d5e | female   | Магнитогорск    | acf18718611c0d0762fbf3af976e66b6 | 1963-08-03 | sv@personal.mgn.ru         | NULL                 | svetlana   | True        |           0 | Уральский           | NULL         | RU           |   1156734920 | NULL         | преподаватель               | 1156846505    | Власовец       | NULL           | Светлана        | 627              | False             |
|      24 | 0241cc2cfdca74b4273bc377893441e4 | male     | Москва          | 5283712ede64c84b0da607a71029655b | 1958-11-20 | vkonovalov@languagelink.ru | NULL                 | Konovalov  | True        |           0 | <blank>             | NULL         | RU           |   1156754776 | NULL         | <blank>                     | 1156755315    | Коновалов      | NULL           | Вадим           | 368              | False             |
|      25 | fa49d30d27e91938a566980a475b90f8 | male     | Москва          | 2d70e68830ca79459e5561b1e899e966 | 1951-03-30 | galanichev@mail.ru         | АстАрожно! Акрашено! | AlexGrand  | True        |           0 | <blank>             | NULL         | RU           |   1156766963 | NULL         | Инженер                     | 1156953751    | Галаничев      | NULL           | Александр       | 431              | False             |
|      26 | b1bc905ac497a1bdc21e3bbf10775899 | male     | <blank>         | 5062c98ec105fac1357552a1dd9b078e | 1969-01-03 | diego@i.ua                 | NULL                 | MadCat     | True        |           0 | <blank>             | NULL         | RU           |   1156773019 | NULL         | <blank>                     | 1211877279    | <blank>        | NULL           | <blank>         | 1296             | False             |
|      27 | 5cf83d43e7a31a78bb60dd7b124beaa8 | male     | <blank>         | f91d425d4dbfb0b3967b8b25c44ec2e1 | 1979-10-04 | rochester@inbox.ru         | <blank>              | Vermeil    | True        |           0 | <blank>             | NULL         | RU           |   1156781359 | NULL         | <blank>                     | 1182771506    | <blank>        | NULL           | <blank>         | 3929             | False             |
|      28 | 46d236f0ab4e827b3222391e465a7731 | female   | <blank>         | d37a4881607c11da4c6c8b8dc31e8c76 | 1976-01-01 | bo-ba-o-by@mail.ru         | NULL                 | Alevtina   | True        |           0 | <blank>             | NULL         | RU           |   1156788378 | NULL         | <blank>                     | 1156788657    | Fust           | NULL           | Alevtina        | 201              | False             |
|      29 | 6ac593890095c837a0fcca0703b635e8 | female   | Москва          | e957d2442d71a50e4a63d09ff69af227 | 1983-06-06 | petrova@fromru.com         | NULL                 | petrova    | True        |           0 | <blank>             | NULL         | RU           |   1156854925 | NULL         | копирайтер                  | 1157887899    | Петрова        | NULL           | Галина          | 2913             | False             |
|      30 | a6290a52919be63d0c81b6e94c707b66 | male     | Москва          | cef0846313a3faff4abb01948afc0a0a | 1972-03-17 | marketolog2005@yandex.ru   | NULL                 | FlyFish    | True        |           0 | <blank>             | NULL         | RU           |   1156855815 | NULL         | маркетолог, копирайтер      | 1156856683    | Морозова       | NULL           | Елена           | 145              | False             |
|      31 | 312e9b0d6af9ce0433004dd94fe4f2ce | male     | <blank>         | 771ba085935d5b1c543aafb2936cea91 | 1969-06-29 | songmaker@mail.ru          | NULL                 | songmaker  | True        |         170 | <blank>             | NULL         | RU           |   1156917132 | NULL         | <blank>                     | 1156939321    | Выхин          | NULL           | Дмитрий         | 3067             | False             |
|      32 | 47b4a358cbbc0975c6ed47a7c8c1e75f | female   | Санкт-Петербург | 36388794be2cf5f298978498ff3c64a2 | 1980-12-16 | angel-med@yandex.ru        | NULL                 | angela     | True        |           0 | <blank>             | NULL         | RU           |   1156922190 | NULL         | менедджер отдела маркетинга | 1156928312    | Рыбакова       | NULL           | Анжела          | 292              | False             |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- addresses: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- raw: string (nullable = false)
 |    |    |-- address: string (nullable = true)
 |    |    |-- location: struct (nullable = true)
 |    |    |    |-- region_type: string (nullable = true)
 |    |    |    |-- region_value: string (nullable = true)
 |    |    |    |-- settlement_region_type: string (nullable = true)
 |    |    |    |-- settlement_region_value: string (nullable = true)
 |    |    |    |-- settlement_type: string (nullable = true)
 |    |    |    |-- settlement_value: string (nullable = true)
 |    |    |    |-- street_type: string (nullable = true)
 |    |    |    |-- street_value: string (nullable = true)
 |    |    |    |-- house: string (nullable = true)
 |    |    |    |-- flat: string (nullable = true)
 |    |    |    |-- floor: string (nullable = true)
 |    |    |    |-- office: string (nullable = true)
 |    |    |    |-- corpus: string (nullable = true)
 |    |    |    |-- coordinates: array (nullable = true)
 |    |    |    |    |-- element: double (containsNull = true)
 |    |    |    |-- coord_detalization_lvl: integer (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 99.99% |
| Sex | 100.00% |
| Emails | 100.00% |
| Address | 72.00% |
| Addresses | 30.05% |
| Accounts | 99.99% |
| Raw_metadata | 55.30% |



### Data sample
```
| names                   | birth_date   |   sex | emails                         | address                          | addresses                                                                                                                                                                                                                                                                                                                                                                                                                 | accounts                                                                                                                      | raw_metadata                                                     |
|:------------------------|:-------------|------:|:-------------------------------|:---------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------|
| ['Лебедев Влад.']       | 01.10.1985   |     1 | ['vlad_g@bk.ru']               | ['Московская область Москва']    | [Row(type=1, raw='Московская область Москва', address='область Московская город Москва', location=Row(region_type='область', region_value='Московская', settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] | [Row(title='sloganbase', link='https://sloganbase.ru', login='sloganbase', password_hash='1e93615b9c793e4fce2f6c8ebde83e61')] | ['{"us_comment2": "копирайтер"}']                                |
| ['Власов Евгений']      |              |     1 | ['liliputin7@list.ru']         | ['Челябинская область Златоуст'] | [Row(type=1, raw='Челябинская область Златоуст', address='область Челябинская', location=Row(region_type='область', region_value='Челябинская', settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                | [Row(title='sloganbase', link='https://sloganbase.ru', login='asd777', password_hash='70efe3b38d65f85cd28d25a0193583c3')]     |                                                                  |
| ['Иванова Ирина']       | 19.01.1984   |     0 | ['paanda@list.ru']             | ['63 Самара']                    | [Row(type=1, raw='63 Самара', address='город Самара', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Самара', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                 | [Row(title='sloganbase', link='https://sloganbase.ru', login='Paanda', password_hash='72c7204bd7fa89087951902cbd997032')]     | ['{"us_comment2": "менеджер по рекламе"}']                       |
| ['Freeman Gordon']      | 02.02.1951   |     1 | ['serafimpanov@gmail.com']     | ['Moskva Moskva']                |                                                                                                                                                                                                                                                                                                                                                                                                                           | [Row(title='sloganbase', link='https://sloganbase.ru', login='admin', password_hash='e24a52691f9bd7fbd96595a0be3914fd')]      | ['{"us_comment2": "FreeMan"}']                                   |
| ['Тимофеев Денис']      | 26.07.1987   |     1 | ['timofeev@novalink.ru']       | ['Москва']                       | [Row(type=1, raw='Москва', address='город Москва', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                    | [Row(title='sloganbase', link='https://sloganbase.ru', login='bedlam', password_hash='8dddd5c939abf0e6eba0924fb4003fb4')]     | ['{"us_fraza": "Hakuna Matata"}']                                |
| ['Шпак Владимир']       | 25.12.1979   |     1 | ['vladimir.shpak@gmail.com']   |                                  |                                                                                                                                                                                                                                                                                                                                                                                                                           | [Row(title='sloganbase', link='https://sloganbase.ru', login='Vladimir', password_hash='77a2702e90613635d5558260f35a146f')]   |                                                                  |
| ['Плющенков Дмитрий']   | 14.09.1980   |     1 | ['dmitry_plus@mail.ru']        | ['Центральный Смоленск']         | [Row(type=1, raw='Центральный Смоленск', address='город Смоленск', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Смоленск', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                  | [Row(title='sloganbase', link='https://sloganbase.ru', login='dmitry', password_hash='e480b8334ad3befc364acddaf61a2433')]     |                                                                  |
| ['Барка Ганнибал']      | 23.02.1984   |     1 | ['venix@yandex.ru']            | ['Москва Москва']                | [Row(type=1, raw='Москва Москва', address='город Москва', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                             | [Row(title='sloganbase', link='https://sloganbase.ru', login='Gannibal', password_hash='9ccdce97b114ee496d6aca90f0d3d28f')]   | ['{"us_comment2": "Москва"}']                                    |
| ['Власовец Светлана']   | 03.08.1963   |     0 | ['sv@personal.mgn.ru']         | ['Уральский Магнитогорск']       | [Row(type=1, raw='Уральский Магнитогорск', address='город Магнитогорск', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Магнитогорск', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                        | [Row(title='sloganbase', link='https://sloganbase.ru', login='svetlana', password_hash='acf18718611c0d0762fbf3af976e66b6')]   | ['{"us_comment2": "преподаватель"}']                             |
| ['Коновалов Вадим']     | 20.11.1958   |     1 | ['vkonovalov@languagelink.ru'] | ['Москва']                       | [Row(type=1, raw='Москва', address='город Москва', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                    | [Row(title='sloganbase', link='https://sloganbase.ru', login='Konovalov', password_hash='5283712ede64c84b0da607a71029655b')]  |                                                                  |
| ['Галаничев Александр'] | 30.03.1951   |     1 | ['galanichev@mail.ru']         | ['Москва']                       | [Row(type=1, raw='Москва', address='город Москва', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                    | [Row(title='sloganbase', link='https://sloganbase.ru', login='AlexGrand', password_hash='2d70e68830ca79459e5561b1e899e966')]  | ['{"us_fraza": "АстАрожно Акрашено", "us_comment2": "Инженер"}'] |
| ['Fust Alevtina']       | 01.01.1976   |     0 | ['bo-ba-o-by@mail.ru']         |                                  |                                                                                                                                                                                                                                                                                                                                                                                                                           | [Row(title='sloganbase', link='https://sloganbase.ru', login='Alevtina', password_hash='d37a4881607c11da4c6c8b8dc31e8c76')]   |                                                                  |
| ['Петрова Галина']      | 06.06.1983   |     0 | ['petrova@fromru.com']         | ['Москва']                       | [Row(type=1, raw='Москва', address='город Москва', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                    | [Row(title='sloganbase', link='https://sloganbase.ru', login='petrova', password_hash='e957d2442d71a50e4a63d09ff69af227')]    | ['{"us_comment2": "копирайтер"}']                                |
| ['Морозова Елена']      | 17.03.1972   |     1 | ['marketolog2005@yandex.ru']   | ['Москва']                       | [Row(type=1, raw='Москва', address='город Москва', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                    | [Row(title='sloganbase', link='https://sloganbase.ru', login='FlyFish', password_hash='cef0846313a3faff4abb01948afc0a0a')]    | ['{"us_comment2": "маркетолог копирайтер"}']                     |
| ['Выхин Дмитрий']       | 29.06.1969   |     1 | ['songmaker@mail.ru']          |                                  |                                                                                                                                                                                                                                                                                                                                                                                                                           | [Row(title='sloganbase', link='https://sloganbase.ru', login='songmaker', password_hash='771ba085935d5b1c543aafb2936cea91')]  |                                                                  |
| ['Рыбакова Анжела']     | 16.12.1980   |     0 | ['angel-med@yandex.ru']        | ['Санкт-Петербург']              | [Row(type=1, raw='Санкт-Петербург', address='город Санкт-петербург', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Санкт-петербург', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                         | [Row(title='sloganbase', link='https://sloganbase.ru', login='angela', password_hash='36388794be2cf5f298978498ff3c64a2')]     | ['{"us_comment2": "менедджер отдела маркетинга"}']               |
| ['Kovalenko Sergey']    | 18.12.1981   |     1 | ['sergey86k@yandex.ru']        | ['Центральный Москва']           | [Row(type=1, raw='Центральный Москва', address='город Москва', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                        | [Row(title='sloganbase', link='https://sloganbase.ru', login='Sergey86K', password_hash='ade24734e9d3dbeff4cfa77ec57a43f0')]  | ['{"us_comment2": "PR менеджер"}']                               |
| ['Котова Ирина']        | 27.12.1981   |     0 | ['sweet-tooth@bk.ru']          | ['Москва']                       | [Row(type=1, raw='Москва', address='город Москва', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                    | [Row(title='sloganbase', link='https://sloganbase.ru', login='Digifund', password_hash='270554615e85dca3520136238e46a513')]   | ['{"us_comment2": "копирайтер"}']                                |
| ['Александр']           | 14.08.1991   |     1 | ['antik.91@mail.ru']           | ['Москва']                       | [Row(type=1, raw='Москва', address='город Москва', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                    | [Row(title='sloganbase', link='https://sloganbase.ru', login='Antik_Ru', password_hash='6ba66730f397e76bedfa65e8395ff248')]   |                                                                  |
| ['Рябец Игорь']         | 08.11.1954   |     1 | ['constanta7@mail.ru']         | ['Москва']                       | [Row(type=1, raw='Москва', address='город Москва', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type='город', settlement_value='Москва', street_type=None, street_value=None, house=None, flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))]                                                    | [Row(title='sloganbase', link='https://sloganbase.ru', login='constanta7', password_hash='ff941a4b9121f6424abfc374da61905c')] |                                                                  |
```