# Parsetron results

## About row data

> - File path: штатка от 22.07 .2024.csv
> - Total rows: 2728

### Schema
```
root
 |-- № пп: string (nullable = true)
 |-- В/звание: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- л/н: string (nullable = true)
 |-- в/ч: string (nullable = true)
 |-- полк: string (nullable = true)
 |-- Армия: string (nullable = true)
 |-- Дата прибытия: string (nullable = true)
 |-- Шифр: string (nullable = true)
 |--  : string (nullable = true)

```

### Data sample
```
|   № пп | В/звание          | ФИО                             | Дата рождения   | л/н       |   в/ч | полк               | Армия   | Дата прибытия   | Шифр     |     |
|-------:|:------------------|:--------------------------------|:----------------|:----------|------:|:-------------------|:--------|:----------------|:---------|:----|
|   1928 | рядовой           | Григорьев Александр Витальевич  | 10/04/1975      | ЕХ-764491 | 29684 | 1253 мсп 18А       | 18 А    |                 |          |     |
|      1 | полковник         | Пророченко Алексей Васильевич   | 02/05/1980      | Ф-799040  | 29333 | 1105 мсп (полк ВВ) | ЮВО     |                 | БАГДАД   |     |
|      2 | подполковник      | Поправко Алексей Борисович      | 14/03/1984      | Е-437728  | 29297 | 1008 мсп 6 мсд     | 3 АК    | 25/05/2024      | ЧЕРНОМОР |     |
|      3 | подполковник      | Истомин Владислав Владимирович  | 30/05/1978      | Ф-970864  | 95370 | 1430 мсп 58А       | 58 А    |                 | ИСТОРИК  |     |
|      5 | капитан           | Бородулин Валерий Александрович | 18/02/1995      | ВЕ-355047 | 33742 | 77 зрбр            | ЮВО     |                 | КАЗАХ    |     |
|      6 | лейтенант         | Стрельников Эдуард Сергеевич    | 07/11/1988      | Ф-009859  | 13204 | 154 ортбр ОсН      | ЮВО     |                 |          |     |
|      7 | подполковник      | Наливкин Александр Сергеевич    | 18/06/1978      | Ф-811178  | 29542 | 1152 мсп 58А       | 58 А    |                 | КЕДР     |     |
|      8 | капитан           | Петров Николай Юрьевич          | 06/01/1986      | Х-979742  | 63354 | 136 омсбр 58А      | 58 А    |                 |          |     |
|      9 | капитан           | Литош Артем Сергеевич           | 30/01/1987      | ВЕ-109345 | 73954 | управление 18А     | 18 А    | 09/06/2024      |          |     |
|     10 | капитан           | Шкред Артем Сергеевич           | 25/03/1996      | Ю-390579  | 91714 | 68 тп 150 мсд      | 8 А     |                 | ПЕРЕСВЕТ |     |
|     11 | капитан           | Дылгин Евгений Олегович         | 24/05/1987      | Х-514385  | 31955 | 133 бру 8А         | 8 А     |                 | ЗАРЯ     |     |
|     12 | майор             | Галайчук Виталий Викторович     | 29/04/1974      | У-675152  | 75394 | 503 мсп 19 мсд     | 58 А    |                 | КРИТИК   |     |
|     13 | старший лейтенант | Морозов Александр Николаевич    | 14/02/1973      | У-836042  | 83444 | 504 тп 51 А        | 51 А    |                 | ДЕД      |     |
|     14 | старшина          | Крицкий Юрий Андреевич          | 20/01/1994      | Х-722933  | 29293 | 1004 мсп 51 А      | 51 А    |                 |          |     |
|     15 | младший сержант   | Кондратюк Александр Сергеевич   | 01/12/1982      | АВ-452097 | 34638 | 1005 озрдн 51 А    | 51 А    |                 |          |     |
|     19 | прапорщик         | Кондрашин Никита Вячеславович   | 07/03/1988      | Э-155960  | 34638 | 1005 озрдн 51 А    | 51 А    |                 | ВОЛЧОК   |     |
|     26 | подполковник      | Симонов Юрий Анатольевич        | 02/01/1962      | С-076582  | 87043 | 935 артп 51 А      | 51 А    |                 | ЧАЛДОМ   |     |
|     27 | майор             | Абайдулин Варис Варисович       | 20/07/1978      | У-853687  | 57760 | 91 сапп            | ЮВО     |                 | ПЕГАС    |     |
|     28 | капитан           | Куркин Евгений Федорович        | 05/08/1988      | Э-104180  | 65363 | 28 обр РХБЗ        | ЮВО     |                 | ЗАНАВЕС  |     |
|     29 | майор             | Толкачев Сергей Леонидович      | 30/09/1975      | У-359930  | 16489 | 24 омедб 70 мсд    | 18 А    |                 | СКЛИФ    |     |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)
 |-- forces: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- tag_number: string (nullable = true)
 |    |    |-- unit_code: string (nullable = true)
 |    |    |-- unit_name: string (nullable = true)
 |    |    |-- callsign: string (nullable = true)
 |    |    |-- rank: string (nullable = true)
 |    |    |-- position: string (nullable = true)
 |    |    |-- mos_code: string (nullable = true)
 |    |    |-- category: integer (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 99.63% |
| Forces | 100.00% |
| Raw_metadata | 34.08% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                                   | birth_date   | forces                                                                                                                                                                                                            | raw_metadata                        | source_entity_id                                         |
|:----------------------------------------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|:---------------------------------------------------------|
| ['Айбазов Герман Казбекович']           | 09.01.1983   | [Row(tag_number='АВ739012', unit_code='12676', unit_name='18 А 126 обрБО', callsign=None, rank='сержант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | ['{"Дата прибытия": "26/06/2024"}'] | 02e5b547668fabed09cd856dd0c2789020c643bdca0031aa3b0df5e2 |
| ['Бобров Андрей Александрович']         | 25.11.1992   | [Row(tag_number='АВ847089', unit_code='42038', unit_name='51 А 114 омсбр', callsign=None, rank='рядовой', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | ['{"Дата прибытия": "13/06/2024"}'] | a0086bdf02a3e3a7911f00c2e67c79d42320a1e45ca5bd1e70d27e93 |
| ['Частухин Ярослав Владимирович']       | 22.06.1994   | [Row(tag_number='УК572283', unit_code='29593', unit_name='3 А 1194 мсп', callsign=None, rank='младший сержант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]       |                                     | f9bd6659966baedd6093f69d53e9dac26aa4c80d7e1249f50b7aa3a6 |
| ['Каримов Тимур Жанилевич']             | 06.05.1994   | [Row(tag_number='МТ371039', unit_code='42038', unit_name='51 А 114 омсбр', callsign=None, rank='рядовой', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | ['{"Дата прибытия": "09/06/2024"}'] | d3950583f4ef5b5dac18558077a16f1f7687f1c231f43087a4759b4b |
| ['Казаченко Данил Андреевич']           | 09.12.1995   | [Row(tag_number='МТ129755', unit_code='63354', unit_name='58 А 136 омсбр', callsign=None, rank='сержант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             |                                     | f3326b2f14db0542458a12049fecc7caa676ec286e93689e213d6b2f |
| ['Храптович Иван Владимирович']         | 01.11.2001   | [Row(tag_number='АВ845565', unit_code='42600', unit_name='51 А 110 омсбр', callsign=None, rank='рядовой', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | ['{"Дата прибытия": "26/06/2024"}'] | 944434716dbc6c9cfaa976386c0314e78e9b3ea818fbb4af8a072f43 |
| ['Нижельский Юрий Владимирович']        | 02.06.1971   | [Row(tag_number=None, unit_code='42038', unit_name='51 А 114 омсбр', callsign=None, rank='ефрейтор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                  | ['{"Дата прибытия": "17/06/2024"}'] | a0f780afeb03043868ec50e44103b2551db6e2a66a8f0d29c51f2894 |
| ['Гопп Александр Александрович']        | 24.01.1972   | [Row(tag_number='АБ000933', unit_code='26388', unit_name='3 А 88 омсбр', callsign=None, rank='младший сержант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]       |                                     | b1f4b064c0151d1f5244ae6ae4ffc00815571c552d8640bb636bdcc2 |
| ['Кузнецов Владимир Сергеевич']         | 29.10.1991   | [Row(tag_number='ЕХ996489', unit_code='33788', unit_name='51 А 580 огадн', callsign=None, rank='ефрейтор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]            | ['{"Дата прибытия": "17/06/2024"}'] | 0fa0ea6bbbd3d777543ff2c954e1eaaa3614a07e352a4d92d611519d |
| ['Савенко Иван Николаевич']             | 20.01.1963   | [Row(tag_number='МТ905456', unit_code='12269', unit_name='18 А 28 мсп 70 мсд', callsign=None, rank='рядовой', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]         |                                     | 1177e99b916898a64abd2f4329fc605004ed1ecddbfd695f5c8d1feb |
| ['Рашитбеков Нурмагомед Закарьяевич']   | 10.07.1999   | [Row(tag_number='УК860728', unit_code='1485', unit_name='49 А 34 омсбр г', callsign=None, rank='рядовой', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             |                                     | 300eec6e599b61e85423e99901233ec20c16a99fe284d8702dcc6a59 |
| ['Глухов Юрий Николаевич']              | 02.06.1974   | [Row(tag_number='У345011', unit_code='29601', unit_name='51 А 1219 мсп', callsign='Залив', rank='старший лейтенант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]  |                                     | 3ef890ad685631a5b0620b51358b47d372736cebad28ba925451cef1 |
| ['Варжинский Виталий Васильевич']       | 01.02.1981   | [Row(tag_number='АВ452830', unit_code='34482', unit_name='51 А 88 осп 114 бр', callsign=None, rank='младший сержант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)] | ['{"Дата прибытия": "26/06/2024"}'] | 68bb45944ac7f6d56aa377850a65d7dfd603c62686fc92fb046c6256 |
| ['Сорокин Алексей Замирович']           | 16.02.1987   | [Row(tag_number='АВ419913', unit_code='95384', unit_name='3 А 1443 мсп', callsign=None, rank='младший сержант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]       |                                     | ff2f2ba0495a5e8752852153acd7c676e12c920422f499ae4efcf609 |
| ['Копытцев Владислав Олегович']         | 10.05.1999   | [Row(tag_number='МТ713179', unit_code='43057', unit_name='58 А 429 мсп 19 мсд', callsign=None, rank='рядовой', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]        |                                     | 47f6a4fcbd3a38e64da63487874b4efb0f093855cb873989ad087ae8 |
| ['Царегородцев Станислав Владимирович'] | 20.12.1992   | [Row(tag_number='АБ114782', unit_code='41698', unit_name='51 А 9 омсбр', callsign=None, rank='младший сержант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]       | ['{"Дата прибытия": "17/06/2024"}'] | 8882671615804c473c5a326989f18e0904e5df4150b1bf80c8e176be |
| ['Дойников Глеб Николаевич']            | 03.07.1991   | [Row(tag_number='Ю709969', unit_code='29293', unit_name='51 А 1004 мсп', callsign=None, rank='ефрейтор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]              |                                     | 8c964204cfd932ea127bde59adb6a519dfd5f25f7a6f7f8b35c028b9 |
| ['Верещагин Денис Александрович']       | 25.07.1992   | [Row(tag_number='Ю645087', unit_code='34491', unit_name='51 А 98 осп', callsign=None, rank='рядовой', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                 |                                     | 56a0281ca224fc38adcb3c0ff4bc32dfc56bcc1b2b6a69f9ee530815 |
| ['Атутин Владимир Николаевич']          | 08.10.1981   | [Row(tag_number='АВ783963', unit_code='75394', unit_name='58 А 503 мсп 19 мсд', callsign=None, rank='рядовой', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]        | ['{"Дата прибытия": "10/07/2024"}'] | 6652e3c65191f92a17b7d1fb03545b1708d052099c984cd85c998a13 |
| ['Ротарь Сергей Дмитриевич']            | 24.12.1973   | [Row(tag_number='ВЕ168010', unit_code='16485', unit_name='18 А 346 обс 70 мсд', callsign=None, rank='рядовой', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]        |                                     | 8d858162c80c992741f3b0729c090dc8372f3647cbc1dea866bff75e |
```