# Parsetron results

## About row data

> - File path: ru_cdek_contragent_30m_2022.csv
> - Total rows: 30128968

### Schema
```
root
 |-- names: string (nullable = true)
 |-- address: string (nullable = true)
 |-- phones: string (nullable = true)
 |-- emails: string (nullable = true)

```

### Data sample
```
| names                                                                           | address                                  | phones          | emails                        |
|:--------------------------------------------------------------------------------|:-----------------------------------------|:----------------|:------------------------------|
| ['Yegorov Aleksey Olegovich', 'Егоров Алексей Олегович"}']                      | None                                     | ['7000000000']  | None                          |
| ['Klever-pak', 'Клевер-пак']                                                    | Краснодарский край, ЯХОНТОВАЯ, д. 2, 313 | None            | ['info@klever-pack123.ru']    |
| ['Voytsakovskiy Aleksandr Nikolayevich', 'Войцаковский Александр Николаевич"}'] | None                                     | ['79130954000'] | None                          |
| ['Dunav Fedor Fedorovich', 'Дунав Федор Федорович"}']                           | None                                     | ['79510000505'] | None                          |
| ['Nadezhda Kudrina', 'Надежда Кудрина"}']                                       | None                                     | ['79266011913'] | None                          |
| ['Moskalev Sergey Anatolyevich', 'Москалев Сергей Анатольевич"}']               | None                                     | ['79102421001'] | None                          |
| ['Zhivayeva Mariya Aleksandrovna', '\\"живаева Мария Александровна\\""}']       | None                                     | ['79213022962'] | None                          |
| ['Bystrov Oleg Nikolayevich', 'Быстров Олег Николаевич"}']                      | None                                     | ['79262699201'] | None                          |
| ['Polikarpov Maksim', 'Поликарпов Максим']                                      | None                                     | ['79869058102'] | None                          |
| ['Merkulenko Dmitriy Aleksandrovich', 'Меркуленко Дмитрий Александрович']       | None                                     | ['79787778047'] | None                          |
| ['Malashenko Lyudmila', 'Малашенко Людмила']                                    | None                                     | ['79113938007'] | None                          |
| ['Krakhaleva Yelena Sergeyevna', 'Крахалева Елена Сергеевна"}']                 | None                                     | ['79126066261'] | None                          |
| ['Nazarova Yelena Stanislavovna', 'Назарова Елена Станиславовна"}']             | None                                     | ['79639147194'] | None                          |
| ['Verkhozina Viktoriya Nikolayevna', 'Верхозина Виктория Николаевна']           | None                                     | ['79501245203'] | None                          |
| ['Zudilkin Artm Maksimovich', 'Зудилкин Артём Максимович']                      | None                                     | ['79016616960'] | ['zudilkinartem@internet.ru'] |
| ['Kim Olga Konstantinovna', 'Ким Ольга Константиновна']                         | None                                     | ['79182987216'] | None                          |
| ['Nikitina Svetlana Yevgenyevna', 'Никитина Светлана Евгеньевна"}']             | None                                     | ['79092832425'] | None                          |
| ['Kolomiyets A S', 'Коломиец А С"}']                                            | None                                     | ['79678999009'] | None                          |
| ['Kulygin Aleksey Vladimirovich', 'Кулыгин Алексей Владимирович"}']             | None                                     | ['79235277302'] | None                          |
| ['Serafishko Andrey', 'Серафишко Андрей']                                       | None                                     | ['79539788979'] | None                          |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- addresses: array (nullable = true)
 |    |-- element: struct (containsNull = true)
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
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)

```



### Data sample
```
| names                                                                    | address                          | addresses                                                                                                                                                                                                                                                                                                                                                                                           | emails                 | phones          |
|:-------------------------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|:----------------|
| ['Peters Sergey Vilgelmovich', 'Петерс Сергей Вильгельмович']            |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79508616773'] |
| ['Корнеев Андрей Сергеевич', 'Korneyev Andrey Sergeyevich']              |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79372199333'] |
| ['Карагодин Владимир Юрьевич', 'Karagodin Vladimir Yuryevich']           |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79313871986'] |
| ['Чугаев Александр Геннадьевич', 'Chugayev Aleksandr Gennadyevich']      |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79397800854'] |
| ['Pisarenko Anton Sergeyevich', 'Писаренко Антон Сергеевич']             |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79211335287'] |
| ['Коробейников Артём Валерьевич', 'Korobeynikov Artm Valeryevich']       |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79081992624'] |
| ['Смирнова Вера Константиновна', 'Smirnova Vera Konstantinovna']         |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79296717723'] |
| ['Bichurina Anna Vladimirovna', 'Бичурина Анна Владимировна']            |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79048340777'] |
| ['Polulyakh Zakhar Sergeyevich', 'Полулях Захар Сергеевич']              |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79852388587'] |
| ['Иoнов Влaдимир Рудольфович', 'Ionov Vladimir Rudolfovich']             |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79045954631'] |
| ['Telyukh Andrey Anatolyevich', 'Телюх Андрей Анатольевич']              |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79227496115'] |
| ['Ооо Пмз', 'Ooo Pmz']                                                   |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79273940318'] |
| ['Mednikov Andrey Viktorovich', 'Медников Андрей Викторович']            | ['ул. Кирова д. 3A павильон 35'] | [Row(type=1, raw='ул. Кирова д. 3A павильон 35', address='улица Кирова дом 3а', location=Row(region_type=None, region_value=None, settlement_region_type=None, settlement_region_value=None, settlement_type=None, settlement_value=None, street_type='улица', street_value='Кирова', house='3а', flat=None, floor=None, office=None, corpus=None, coordinates=None, coord_detalization_lvl=None))] | ['o.gostyaeva@wmt.ru'] | ['79168263143'] |
| ['Andreyev Sergey Anatolyevich', 'Андреев Сергей Анатольевич']           | ['16 А Мкр. Д. 66 22']           | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79173556611'] |
| ['Михеев Андрей Валерьевич', 'Mikheyev Andrey Valeryevich']              |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79138105471'] |
| ['Леонова Анастасия Александровна', 'Leonova Anastasiya Aleksandrovna']  |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79030171005'] |
| ['Рябчиков Сергей Викторович', 'Ryabchikov Sergey Viktorovich']          |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79203448098'] |
| ['Alekseyeva Valeriya Vyacheslavovna', 'Алексеева Валерия Вячеславовна'] |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79164089670'] |
| ['Davyda Sergey Aleksandrovich', 'Давыда Сергей Александрович']          |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79397005377'] |
| ['Kaygorodov Yuriy Viktorovich', 'Кайгородов Юрий Викторович']           |                                  | [None]                                                                                                                                                                                                                                                                                                                                                                                              |                        | ['79969462878'] |
```