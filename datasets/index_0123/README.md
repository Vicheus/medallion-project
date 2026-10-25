# Parsetron results

## About row data

> - Code name: index_0123
> - File path: /media/user/TRANSCEND/Databases/index_0123/raw/user_info_1_preprocessed.csv
> - Total rows: 23

### Schema
```
root
 |-- USER_ID: integer (nullable = true)
 |-- country: string (nullable = true)
 |-- education: string (nullable = true)
 |-- job: string (nullable = true)
 |-- city_region: string (nullable = true)

```

### Data sample
```
|   USER_ID | country   | education                 | job       | city_region     |
|----------:|:----------|:--------------------------|:----------|:----------------|
|         0 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|    179081 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|    129926 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|    101401 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|     64965 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|     66757 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|     56966 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|     47219 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|      4413 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|     33984 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|     24256 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|     19000 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|      6135 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|      2120 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|      1388 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|         7 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|         1 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|    220966 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|    128885 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
|    213742 | РФ        | Среднее фарм. образование | Фармацевт | Санкт-Петербург |
```

> - Code name: index_0123
> - File path: /media/user/TRANSCEND/Databases/index_0123/raw/user_info_2_preprocessed.csv
> - Total rows: 239245

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
 |-- birth_date: string (nullable = true)
 |-- client_card_number: long (nullable = true)
 |-- phone2: long (nullable = true)

```

### Data sample
```
|   USER_ID | username          | password_hash                                                                                              | first_name   | last_name   | middle_name   | email                     | gender   | phone   | birth_date   |   client_card_number |      phone2 |
|----------:|:------------------|:-----------------------------------------------------------------------------------------------------------|:-------------|:------------|:--------------|:--------------------------|:---------|:--------|:-------------|---------------------:|------------:|
|        15 | +7 (911) 092-1715 | $6$fdrti7yQ24xCLjOS$t.WGzz5eH8IMqA4x86I90L82MEQfpbj5OQ4XTBhp1tmGPWRMf78maZLvWmLdYbMBco.tSBpbJDrB/thQEPaG.1 | Евгений      | Ярошенко    | Александрович | yaroshenko@aptekanevis.ru | M        |         | 1979-03-08   |        8880015937582 | 79110921715 |
|        26 | +7 (953) 542-1041 | 3^pDw0{Y319f8a2de26687828ca6ec06869937af                                                                   | Константин   | Филин       | Валерьевич    | filin-kv@mail.ru          | M        |         | 1973-03-31   |        8880011522058 | 79535421041 |
|        43 | +7 (921) 313-6119 | |7dZ~eF219c8677ea2fdb44dabda7bbc1c670260                                                                   | Евгений      | Старостенко |               | starostenko.e@gmail.com   | M        |         | 1985-05-20   |        8880010112113 | 79213136119 |
|        46 | +7 (911) 208-6015 | $6$w6i319aBWKzNtruG$dG3vP5Yu7QCNX2zjXHLSm0HtKaBeqsKlDDUj3xzaYBtrUS/8tV/wc/.B3OCIQ0N9tCT6ZgABqzdnEC3/OMq951 | Ирина        | Мурзайкина  | Борисовна     | murzaikina@yandex.ru      | F        |         | 1965-11-14   |        8880015654380 | 79112086015 |
|        56 | +7 (921) 330-1919 | fN3!7wT|b825b3c7ee86b4e4970c4c13ee463823                                                                   | Денис        | Коротков    | Евгеньевич    | denkorotkov@yandex.ru     | M        |         | 1973-09-03   |        8880015567475 | 79213301919 |
|        99 | +7 (950) 047-4117 | $6$WIM9IiSrJeVanLJf$y8pQVjsdkd.bk04Yu51GgdScPVHM4obohHMB8t20mCrfvZj601JBWUz2ZAVTZ7SvBfumseDkbePfEVjDKHp9L/ | Ксения       | Анисимова   | Викторовна    | bublikova.87@mail.ru      | F        |         | 1987-12-24   |        8880005844289 | 79500474117 |
|       397 | +7 (911) 434-4597 | $6$DdDF84GQlkSRJlWq$sWV1VAJ6tvk3IDqX4mt.wqSOJZLBsO30.oUFKNRM3hr7JJkroDI7bWYGbI8ZxlHsmKfgj4fv7k.5TOu3eLaQi/ | Валерий      | Андреев     | Васильевич    | drug051@rambler.ru        | M        |         | 1969-01-04   |        8880014210143 | 79114344597 |
|       511 | +7 (953) 822-8466 | nQ?2#M1x0140e0fb42ee627ac903ed1c77586552                                                                   | Ксения       | Овсянникова | Сергеевна     | ksenia.ovs@gmail.com      | F        |         | 1988-08-13   |        8880011545194 | 79538228466 |
|       517 | +7 (911) 946-2995 | $6$3quTJub5Y5CAoNgl$9nQoh07YNBsIzRudLa6g6csQkLQ/PeHKnUEjeu06yxMmkTokm8FVg2AnxQD9Gi/Lbcgt3CdLOBwqflrXcf9wr/ | Александр    | Малышев     | Дмитриевич    | ulme@rambler.ru           | M        |         | 1986-08-22   |        8880012222872 | 79119462995 |
|       529 | +7 (904) 632-9564 | $6$UT9ZCIk39tim4v3d$PmI9XqCA3.FZ1HFl484qBdAZ9e4S2A/3MMQG/XvaRQd9tCR9fNi/2ZYJJwd0IR99xDTaAMVGusaydAlgY/zwZ/ | Вадим        | Рокицкий    | Иванович      | virok@mail.ru             | M        |         | 1967-09-21   |        8880014963087 | 79046329564 |
|       563 | +7 (960) 213-9086 | $6$nAJjMV1v4OLppFTJ$1iaPRBmqjyvJWSEiJBoVChY46c91z0RFgGODPCxS05JKGNco0/h/QikEathxmYJkNyNqji73VKIXLJ1GZfd430 | -не указано- |             |               | kisska-shef@mail.ru       |          |         |              |        8880010011492 | 79602139086 |
|       583 | +7 (911) 724-2483 | $6$qHi8i6slMFHp0vyS$A3UBAH2QcwllY0d0IiPuYxbfoJw6sA5MrtEElS/YTZyZ8MfDtei6dGyAXJMqKPiBkQUqIN5N/E9qTxbRNN.AK. | Алексей      | Смирнов     | Николаевич    | toptygin@list.ru          | M        |         | 2022-02-21   |        8880012525560 | 79117242483 |
|       620 | +7 (952) 370-5432 | $6$wxtHb5i3Cp0cqV3k$Rzrttn2RQ92nls0g/gsksaYfMA1939uersZcVFYdb1ile8fPpMLElhEmzkrV25X7MlobV2c7dOff4pWwI8rcW/ | Сергей       | Героев      | Александрович | sageroev@gmail.com        | M        |         | 1989-10-16   |        8880017700429 | 79523705432 |
|       760 | +7 (904) 557-0026 | $6$6bg6rZVvkFc41X5E$zM4SSowv88Q2hDlj2h4QUthuzot8cQlaUd8hqrK4wITEmQ9yTH1uoUOZ/.v..e3SRRtjgGjgUUJ9dAMh2Izq.1 | Роман        | Герасимов   |               | nevskiy22@mail.ru         | M        |         | 1978-10-20   |        8880003614983 | 79045570026 |
|       853 | +7 (911) 402-1975 | $6$8BGw2dF0abU7dPbd$CepgRnRYwzUHTAGmnqpGqrIEdTRCcldGcMjj8F/KkIRYRKuoEo5PKVtBjPUNfv9tPdrjd7xQfsh0syJ1rAoE81 | Леонид       | Пасютин     | Анатольевич   | 79114021975@yandex.ru     | M        |         | 1975-07-07   |        8880010866658 | 79114021975 |
|       985 | +7 (921) 943-4991 | vW>8&2cAe50b9b056def28db574c2be6abc16057                                                                   | Наталья      | Ткачева     | Викторовна    | 007.97@mail.ru            | F        |         | 1971-09-20   |        8880015627186 | 79219434991 |
|      1016 | +7 (932) 050-1512 | $6$0z4RjROthEnF8ZH5$UP1SQTMo0HfF2nSbOxp4f4xcFn4vEobAW3wQdumu9FzEUDnFuvzxbaZR2rQLjbOPYjjVe9koiwYrsJ7uJo0tb/ | -не указано- |             |               | mamosik@inbox.ru          |          |         |              |        8880010062494 | 79320501512 |
|      1020 | +7 (921) 381-2296 | $6$gwTHUWHvj6VK6OlK$syLxR8ZPoPKF1JdBcTfqnhPtBdh9hRO4jq/WwrK5YqkI5UM.dbDINczJ/vO5G1SI1okZvnVTb5HcLyOoVieLx1 | Арсен        | Белов       | Львович       | belov.arsen@gmail.com     | M        |         | 1974-09-08   |        8880016724198 | 79213812296 |
|      1024 | +7 (951) 660-8784 | $6$6o8I3BBFY0ixY7dH$o0UcyNMxyKN87RfmTGidkNjv7Ygnfy7sIrpCtChg8fbuvKgPDazuwCzYoF.kkeEd.lrA9ywHsvvVWv.Krf4QS/ | Анна         | Захарова    |               | adokuchaeva2008@yandex.ru | F        |         | 1986-06-27   |        8880012080380 | 79516608784 |
|      1211 | +7 (981) 948-0144 | $6$sEbzTTnSUXF2qSb7$H5K7C97odfdMHqvaKcDFdeBVx/SoD6lrJXzsx0OmmTGXW5dSh1B35cgtKOmt4te9NpQ5ReQYQTP1pFavovlGU1 | ГАЛИНА       | Кудрина     | Витальеана    | galinka-69@bk.ru          | F        |         | 1969-07-03   |        8880017480185 | 79819480144 |
```

> - Code name: index_0123
> - File path: /media/user/TRANSCEND/Databases/index_0123/raw/user_info_3_preprocessed.csv
> - Total rows: 159103

### Schema
```
root
 |-- USER_ID: string (nullable = true)
 |-- name2: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- phone3: string (nullable = true)
 |-- address: string (nullable = true)
 |-- address_longitude: double (nullable = true)
 |-- address_latitude: double (nullable = true)
 |-- floor: string (nullable = true)
 |-- flat: string (nullable = true)
 |-- phone4: string (nullable = true)

```

### Data sample
```
|   USER_ID | name2           | email2                         |      phone3 | address                                                                                                          |   address_longitude |   address_latitude | floor   | flat   | phone4   |
|----------:|:----------------|:-------------------------------|------------:|:-----------------------------------------------------------------------------------------------------------------|--------------------:|-------------------:|:--------|:-------|:---------|
|       291 | Павел Суворов   | pasu@nav-it.ru                 | 79811883938 | """Аптека НЕВИС"", 198320, Санкт-Петербург г, Красное Село г, Красногородская ул, дом № 17, корпус 1"            |                 nan |                nan |         |        |          |
|       463 |                 | olgacv2009@rambler.ru          | 79817428560 | """Аптека НЕВИС (Сбербанк)"", 197755, Санкт-Петербург г, Лисий Нос п, Межевая ул, дом № 1"                       |                 nan |                nan |         |        |          |
|       258 |                 | alexspb.06@gmail.com           | 79216347807 | """Аптека НЕВИС"", 196602, Санкт-Петербург г, Пушкин г, Кадетский б-р, дом № 24"                                 |                 nan |                nan |         |        |          |
|       483 |                 | Yulia0879@yandex.ru            | 79814000177 | """Аптека НЕВИС (ТК Лотос-центр)"", 185003, Карелия Респ, Петрозаводск г, Правды ул, дом № 38, корпус б"         |                 nan |                nan |         |        |          |
|       507 |                 | baruzdin.aleck@yandex.ru       | 79117083035 | г. Кронштадт, ул. Флотская,    д. 27                                                                             |                 nan |                nan |         |        |          |
|       533 | Иван Ушаков     | ushakoff-ivan@mail.ru          | 79111837705 | """Аптека НЕВИС"", 187032, Ленинградская обл, Тосненский р-н, Тельмана п, дом № 16"                              |                 nan |                nan |         |        |          |
|       539 |                 | nastja-nm@yandex.ru            | 79218806209 | """Аптека НЕВИС"", 197342, Санкт-Петербург г, Торжковская ул, дом № 1"                                           |                 nan |                nan |         |        |          |
|       540 |                 | sukhanovg@mail.ru              | 79217687678 | """Аптека НЕВИС"", 191119, Санкт-Петербург г, Боровая ул, дом № 18, корпус 1"                                    |                 nan |                nan |         |        |          |
|       552 |                 | fierce_panda@mail.ru           | 79531694353 | """Аптека НЕВИС"", 188542, Ленинградская обл, Сосновый Бор г, Красных Фортов ул, дом № 37, корпус А"             |                 nan |                nan |         |        |          |
|       568 |                 | brein594@rambler.ru            | 79633043401 | """Аптека НЕВИС (ЖК Ласточкино гнездо)"", 193149, Санкт-Петербург г, Русановская ул, дом № 15"                   |                 nan |                nan |         |        |          |
|       571 |                 | nadasak@rambler.ru             | 79219460932 | """Аптека НЕВИС"", 191186, Санкт-Петербург г, Канала Грибоедова наб, дом № 28/1"                                 |                 nan |                nan |         |        |          |
|       584 |                 | maibachduonghq@gmail.com       | 79616105332 | """Аптека НЕВИС"", 197342, Санкт-Петербург г, Торжковская ул, дом № 1"                                           |                 nan |                nan |         |        |          |
|       593 |                 | esmaltseva@yandex.ru           | 79219980753 | """Аптека НЕВИС (Андреевкий рынок, Универсам Магнит)"", 199034, Санкт-Петербург г, Большой В.О. пр-кт, дом № 18" |                 nan |                nan |         |        |          |
|       587 |                 | eabelyaeva@mail.ru             | 79111337839 | """Аптека НЕВИС (Универсам  Магнит)"", 198207, Санкт-Петербург г, Зины Портновой ул, дом № 1, корпус 3"          |                 nan |                nan |         |        |          |
|       598 |                 | larisa.chistyakova.64@inbox.ru | 79522329749 | """Аптека НЕВИС"", 188800, Ленинградская обл, Выборгский р-н, Выборг г, Ленина пр-кт, дом № 6"                   |                 nan |                nan |         |        |          |
|       610 |                 | sergant-volk@yandex.ru         | 79213103054 | """Аптека НЕВИС"", 197342, Санкт-Петербург г, Торжковская ул, дом № 1"                                           |                 nan |                nan |         |        |          |
|       613 |                 | olj.kosterina@mail.ru          | 79619190348 | """Аптека НЕВИС"", 197342, Санкт-Петербург г, Торжковская ул, дом № 1"                                           |                 nan |                nan |         |        |          |
|       614 |                 | nsp-91@list.ru                 | 79110019101 | """Аптека НЕВИС"", 196641, Санкт-Петербург г, Металлострой п, Центральная ул, дом № 10"                          |                 nan |                nan |         |        |          |
|       626 | Дмитрий Горскин | gorskindman@gmail.com          | 79990595279 | """Аптека НЕВИС"", 194100, Санкт-Петербург г, Кантемировская ул, дом № 24"                                       |                 nan |                nan |         |        |          |
|       628 |                 | svmaslennikov@yandex.ru        | 79119166944 | """Аптека НЕВИС"", 190005, Санкт-Петербург г, Измайловский пр-кт, дом № 31"                                      |                 nan |                nan |         |        |          |
```


## About final data
> - Total rows: 131711

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
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- educations: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = true)
 |    |    |-- level: integer (nullable = true)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |    |    |-- client_card_number: string (nullable = true)
 |-- coordinates: array (nullable = true)
 |    |-- element: array (containsNull = false)
 |    |    |-- element: float (containsNull = true)

```

### Data sample
```
| names                                              | emails                         | phones          | address                                                                                                                        |   sex | birth_date   | works   | educations   | accounts                                                                                                                                                                                                                                              | coordinates                               |
|:---------------------------------------------------|:-------------------------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------|------:|:-------------|:--------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------|
| ['Яна']                                            | ['yana0504@mail.ru']           | ['79112101641'] | ['Аптека НЕВИС Санкт-Петербург г Стачек пр-кт дом 15']                                                                         |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (911) 210-1641', password_hash='$6$Zgiax9ra8aGhdnQd$BPQT1c22y.F5kdMjInIoL3KVMZSUyZqxUlB2SectVzIROXpffzgnjAKPUmdd4/lG0PPraXZvgOmZrlNpeLbgM/', client_card_number=None)]            |                                           |
| ['Конкина Юлия', 'Юлия']                           | ['kate9421@mail.ru']           | ['79675724163'] | ['Россия Санкт-Петербург проспект Косыгина 9к2 кв. 383']                                                                       |     0 | 21.01.1994   |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (967) 572-4163', password_hash='$6$60V7zDwpXnD4nD8m$biExjTkOyKoM07WFO.qvphZoS070N8SUTHWjqlEBdnGdaDFE./wDhazbwnPEfa6m5rY0mj3X26W9DSrz68EFW0', client_card_number=None)]            | [[59.94134521484375, 30.469928741455078]] |
| ['Елена']                                          | ['levsirokov@gmail.com']       | ['79523610240'] | ['Аптека НЕВИС Ленинградская область Всеволожский р-н Янино-1 д Шоссейная ул корпус 34г']                                      |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (952) 361-0240', password_hash='$6$M6jxC3fcxi7qFER2$RcWX/MFmab1ukeBXSU.qenEqIjdlJ8t4hnNGlNmaNhhap0kL1yyNLvYH7olvQov1I7ohD4X5isNyOYc20eyJ6.', client_card_number=None)]            |                                           |
| ['Прохорова Елена Николаевна', 'Елена Прохорова']  | ['eva1987ne@gmail.com']        | ['79045154959'] | ['Аптека НЕВИС Санкт-Петербург г Орджоникидзе ул дом 52']                                                                      |     0 | 17.01.1987   |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (904) 515-4959', password_hash='$6$8krIVvfMW00Y2Hjc$5NMmqP.yRYkKX3792X8hEvw.REV.o7lgrifDA0Q4nbG1NN0q0VB6lIn/eibaGqx7d2YKgvyn56vo/beKUdiv1.', client_card_number='8880016009226')] |                                           |
| ['Екатерина']                                      | ['ekaterina_star.9@mail.ru']   | ['79108316160'] | ['Аптека НЕВИС Супремаркет Перекресток Санкт-Петербург г Карбышева ул дом 9']                                                  |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (910) 831-6160', password_hash='$6$sUwRKVph7EN79HOs$M7PLXQ5k000UtMc4/W.rpKoNlMvanD.IxC01utS6TCwtrGHycW8LAKhlK/8tts3x0sQUm6mu7xoRCtSZE3t.f.', client_card_number=None)]            |                                           |
| ['Анна']                                           |                                | ['79052702760'] | ['Аптека НЕВИС Санкт-Петербург г Савушкина ул дом 132 корпус 2']                                                               |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (905) 270-2760', password_hash='$6$3tCYj7XJdMeUiQP1$24z7o.K.ukqucnLnLj/zGGMAMOQKg2h01eZeTRfOcSfYSf0Nd.T2kTo20R72KdADhNL3QjFCFvBumUUzbT9Z/.', client_card_number=None)]            |                                           |
| ['Екатерина']                                      | ['veirikekat@mail.ru']         | ['79052003784'] | ['Аптека Невис Санкт-Петербург г Ярослава Гашека ул дом 6 корпус 2']                                                           |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (905) 200-3784', password_hash='$6$g12s7GNS30Na3wjI$Z.g.f8driZ0Vfai4yid8vOaco.iD/WA5t6q9OFwJmgTu1c0NUvuyq8tdyJQBfJ9fxS5avo5azEiJzrdEnxaKE1', client_card_number=None)]            |                                           |
| ['Максим']                                         |                                | ['79029109509'] | ['Аптека НЕВИС Санкт-Петербург г Большой П.С. пр-кт дом 43']                                                                   |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (902) 910-9509', password_hash='$6$lH2qvAmYqlEc7IhR$MjpQUaaYGG.WFs0mt0eYQPUzwfTLsZ5P2ky7JGfrWMyBCaQE8j2xoSAIgkC8or.XViKDVVohKdG6MWFQTZ1R/.', client_card_number=None)]            |                                           |
| ['Екатерина']                                      | ['e.nester.spb@mail.ru']       | ['79215729679'] | ['Аптека НЕВИС Универсам Магнит Ленинградская область Гатчинский р-н Коммунар г Садовая ул дом 3']                             |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (921) 572-9679', password_hash='$6$abdm9N9C5R3lvU6h$sKun1JRhqPNW3jT5iYfysOQCXdP1giTa4cNmmMSMIdWLzR8zTnxbpl8z6MweM21l8OuIAgm3cmVK/hsn4zdZ.1', client_card_number=None)]            |                                           |
| ['Слуцкая Татьяна Анатольевна', 'Татьяна Слуцкая'] | ['tanushka_zayka@mail.ru']     | ['79112495039'] | ['Аптека Невис енинградская обл Приозерский р-н Сосново п Ленинградская ул 117В']                                              |     0 | 03.01.1987   |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (911) 249-5039', password_hash='$6$ZyBbVTDglEOL5iEv$4WpRvrrQJdFGNfSjdK0vd0vp9GwWj9LxwdRZlDxBxk4Mrq.97275JPjqMrSDiMlSFIeFYbzOWc8vajJhnQxjW.', client_card_number=None)]            |                                           |
| ['Анастасия']                                      | ['nastasia.chagina@yandex.ru'] | ['79215876850'] | ['Аптека НЕВИС Санкт-Петербург г Савушкина ул дом 132 корпус 2']                                                               |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (921) 587-6850', password_hash='$6$D3xBdow8TTkMAHXF$yWPokdTcwzPUtIf/qRAerniFyidmYY68ZPnVy8qRfJr1O6r2cARSGEFhtQKD2XJy46EpTkuHHASvbSAFk/5iD0', client_card_number=None)]            |                                           |
| ['Денис']                                          | ['denhh@mail.ru']              | ['79313648501'] | ['Россия Санкт-Петербург Заусадебная улица 37В']                                                                               |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (931) 364-8501', password_hash='$6$sH8wizOp5lnVtf5K$GybxaKbSd2Ruuctz5WGzI6fySzXs7HinOFAIYuOhOULgo4DJPNSyNOnHpRYZ273xm9uziOud7hMxNcTQlT58a0', client_card_number=None)]            | [[59.98942565917969, 30.262760162353516]] |
| ['Татьяна']                                        | ['alisia_86@mail.ru']          | ['79046018559'] | ['Аптека НЕВИС Санкт-Петербург г Маршала Захарова ул дом 21']                                                                  |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (904) 601-8559', password_hash='$6$CjRGnlf5IwLG7Q9Z$tJhZ.Ow98RxSLu6okEWbqV2F/hvgqEVO7czuCR6FN2ZhDlGaCh4WibRUfIPAcLLQWkcWamRYwQ7hyHZ7Hx0O3.', client_card_number=None)]            |                                           |
| ['Лариса']                                         | ['belkowa.lara@yandex.ru']     | ['79214250634'] | ['Аптека НЕВИС Санкт-Петербург г Маршала Захарова ул дом 21']                                                                  |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (921) 425-0634', password_hash='$6$pK8Rhzo2kU7dEXMu$PAdyJ/m79CgxJR3B5xXsqJ5kANJsCZ84wm1NbL6xg7CimTFKVQX.JPmZZ6kyzMvnzBQx/xN3DMo28pGYpMWYm1', client_card_number=None)]            |                                           |
| ['Галина']                                         |                                | ['79216535614'] | ['Аптека НЕВИС Санкт-Петербург г Маршала Захарова ул дом 21']                                                                  |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (921) 653-5614', password_hash='$6$dKkAS7p8t5gqiF3U$vrLUvSar4r/j0S0aZyXi5qFDn1mSGUf2vxgZDcWU7Qo6tU91seCAZuoOAOC5mUizeKm28QdcN/qe7cl5rxRzP0', client_card_number=None)]            |                                           |
| ['Галина']                                         | ['gandrosuk@mail.ru']          | ['79111613392'] | ['Аптека НЕВИС ТК Фиолент Санкт-Петербург г Ленинский пр-кт дом 100 корпус 1']                                                 |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (911) 161-3392', password_hash='$6$H8uvoJ30QVCVWsQ8$Cqh.OpgeiOg9HO7sTr27gW4RNVQ5ldxr2H7D1k.bWWB8cX74I9wXECSnLsT26NbUY98l80VQfFI2nrZ5Y5mWz/', client_card_number=None)]            |                                           |
| ['Дмитрий']                                        | ['kengarion@yandex.ru']        | ['79112196916'] | ['Аптека ЛенОблФарм Универсам Пятерочка Санкт-Петербург г Большая Пороховская ул дом 50']                                      |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (911) 219-6916', password_hash='$6$wCBJWrtlH0XVtoIF$rMAyPl5EFZa3oMjjuf7KxbWsq2OpwVchOxh2mUlGrfGx4DYDaJp0fGTLKqrWqpKpHo3MBDcNgxa/ind./nROV.', client_card_number=None)]            |                                           |
| ['Татьяна']                                        | ['murt@bk.ru']                 | ['79052800634'] | ['Аптека НЕВИС Рынок Ленинградская область Кировский р-н Шлиссельбург г Затонная ул дом 2']                                    |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (905) 280-0634', password_hash='$6$ZuYED8C24RAonK66$KNghnlvG0Uk0TkY7uloaCILuXk28IWDiUcakCkdcImxSdcRd1ZOeUPmYhugyNAEg4nVV.shRPucUc/bL4Qh3w/', client_card_number=None)]            |                                           |
| ['Надежда']                                        | ['pashtet2771@yandex.ru']      | ['79119680492'] | ['Аптека НЕВИС Супремаркет Перекресток Санкт-Петербург г Карбышева ул дом 9']                                                  |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (911) 968-0492', password_hash='$6$MLq2Q4T3MRj5WbHU$0fZjM4z3tDDEnVl525wCjNmUtoRfOaUOiZn9AbGdfiNGOXKkG5u0qWIynm6kVGzxzQsh80P15.tZmP6kYMUu//', client_card_number=None)]            |                                           |
| ['Ольга Трофимовна']                               | ['olgama143@mail.ru']          | ['79119949363'] | ['Аптека НЕВИС вход с ул. Кронверкская д.5 Супермаркет Перекресток Санкт-Петербург г Каменноостровский пр-кт дом 10 корпус м'] |   nan |              |         |              | [Row(title='Аптека Невис', link='https://aptekanevis.ru/', login='7 (911) 994-9363', password_hash='$6$WJnqmdJlLWmFwOEb$Kmt4nbm/TMThMVWNEn1z2QWaAGJ2R4waouOOs0adFs6i8GyJaVnpp2c/.ZmcMHV1Exxvn4JxNcCxfNMQZmIDd/', client_card_number=None)]            |                                           |
```