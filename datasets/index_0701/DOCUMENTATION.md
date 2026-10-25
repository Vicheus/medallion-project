# Parsetron results

## About row data

> - File path: 111_brigade_dnr.csv
> - Total rows: 288

### Schema
```
root
 |-- Должность по штату: string (nullable = true)
 |-- Воинское звание: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Дата рождения: string (nullable = true)

```

### Data sample
```
| Должность по штату                                                      | Воинское звание   | ФИО                            | Дата рождения   |
|:------------------------------------------------------------------------|:------------------|:-------------------------------|:----------------|
| Командир батальона                                                      | Подполковник      | Степанов  Александр  Сергеевич | 3/2/1973        |
| Заместитель командира батальона по материально-техническому обеспечению | Капитан           | Емельченко Василий Анатольевич | 1/5/1972        |
| Начальник штаба–заместитель командира батальона                         | Майор             | Яшин Игорь Иванович            | 12/6/1969       |
| Заместитель начальника штаба                                            | старший лейтенант | Черняев Виталий Федорович      | 12/8/1966       |
| Инструктор                                                              | Рядовой           | Кравцов Андрей Геннадьевич     | 10/18/1994      |
| Командир роты                                                           | старший лейтенант | Панчишин Андрей Ростиславович  | 12/24/1964      |
| Заместитель командира роты                                              | старший лейтенант | Жебокрицкий Игорь Леонидович   | 10/30/1966      |
| Старшина                                                                | Рядовой           | Рябченко Владимир Викторович   | 11/2/1967       |
| Фельдшер                                                                | Рядовой           | Лемешко Илья Владимирович      | 7/4/1983        |
| Радиотелефонист                                                         | младший сержант   | Карпенко Александр Анатольевич | 11/7/1969       |
| Огнеметчик                                                              | рядовой           | Якин Евгений Николаевич        | 1/25/1989       |
| Командир взвода                                                         | Лейтенант         | Журбей Роман Сергеевич         | 12/13/1979      |
| Старший водитель                                                        | Ефрейтор          | Алехин Виталий Николаевич      | 9/25/1972       |
| Снайпер                                                                 | Рядовой           | Добушевский Василий Васильевич | 11/12/1984      |
| Стрелок-радиотелефонист                                                 | Рядовой           | Номеровский Роман Васильевич   | 6/6/1986        |
| Заместитель командира взвода-командир отделения                         | Рядовой           | Архипов Геннадий Васильевич    | 1/13/1971       |
| Старший стрелок                                                         | Рядовой           | Бубнов Александр Сергеевич     | 6/2/1987        |
| Пулеметчик                                                              | Рядовой           | Сарбей Георгий Георгиевич      | 5/20/1975       |
| Гранатометчик                                                           | Рядовой           | Кузуб Виталий Павлович         | 3/23/1984       |
| Стрелок-помощник гранатометчика                                         | Рядовой           | Потебенько Илья Игоревич       | 12/10/1992      |
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
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 100.00% |
| Forces | 100.00% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                               | birth_date   | forces                                                                                                                                                                                                                                     | source_entity_id                                         |
|:------------------------------------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| ['Полшков Николай Александрович']   | 05.05.1989   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Сержант', position='Командир отделения-гранатометчик', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                | fa6c1d5c57147b14c104eca3d89d73f885d7facc6219d0d6cf9a05a5 |
| ['Сарбей Георгий Георгиевич']       | 20.05.1975   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Пулеметчик', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                                      | 9905b5ecb2ae5fae7a16d4565c32fa3de199dbd5205eabcce5615622 |
| ['Кравцов Андрей Геннадьевич']      | 18.10.1994   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Инструктор', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                                      | ef7069d329913a24e9021976e5c8df2cc9ea9af84ebb72579a0229b1 |
| ['Тищенко Алексей Вячеславович']    | 05.02.1976   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Стрелок-помощник гранатометчика', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                 | 2652d01f89927ef6c1de9b2b2bd8d7dae24ae91f484add57a530a329 |
| ['Полях Михаил Геннадьевич']        | 16.10.1982   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Стрелок-помощник гранатометчика', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                 | f8e276a408270994898b426e2f5e14632a4dc229f62479bfaf9043dd |
| ['Бахмов Денис Сергеевич']          | 07.06.1984   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Повар', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                                           | 16fdb9b33bacfc628bae91ee028b6efefb754dbb28149a285e00f4b8 |
| ['Чуприна Сергей Юрьевич']          | 14.08.1986   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Стрелок', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                                         | ee901c1001b516116533015735f9a1c91e8b0b9b611efefa9c2e3342 |
| ['Баранич Андрей Михайлович']       | 11.08.1987   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Старший водитель', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                                | 5374d6ad19231e09033daa1537602692bd3550e5ed4e2455ef9cbae3 |
| ['Кудрявцев Алексей Александрович'] | 05.12.1976   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='старший лейтенант', position='Командир роты', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                         | da3cb94009d1e977294e61ebb30ad30e641e040983e23d21d8f10ac3 |
| ['Кучеровский Евгений Анатольевич'] | 12.05.1981   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Сержант', position='Заместитель командира взвода-командир отделения', mos_code=None, category=None, date_start=None, date_end=None, comment=None)] | f671d1e1711ad1a896a1895a179d94f760ca6740840da016bdc51210 |
| ['Иванов Алексей Сергеевич']        | 28.11.1983   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Водитель-радиотелефонист', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                        | a821a03da352976441e6cc61f05233d49e8b84e44120766a212bb5f0 |
| ['Ковтун Виталий Юрьевич']          | 31.05.1992   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Телефонист-линейный надсмотрщик', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                 | e4413dec1f334230f8ba91549e705adf9e160980cf6dda76dcac6f48 |
| ['Афанасьев Андрей Александрович']  | 15.07.1970   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Номер расчета', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                                   | 13790074d1743f7a9ea5c52e00f5d87f5b34ffce101e8b8143c5b194 |
| ['Паниотов Николай Леонидович']     | 15.05.1980   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Гранатометчик', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                                   | d90490e24223f042d188ae02c10fdeb7a190cb5285f2521734d57913 |
| ['Архипов Геннадий Васильевич']     | 13.01.1971   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Заместитель командира взвода-командир отделения', mos_code=None, category=None, date_start=None, date_end=None, comment=None)] | 951f51e7d0108bead0d185a26b622409444810fc7370644c5b061fd8 |
| ['Косинов Денис Васильевич']        | 08.10.1978   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Номер расчета', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                                   | 90e78ae53a878fca11087db014e60475e5669df5f7337ce7e697ac9c |
| ['Раткевич Владимир Леонтьевич']    | 10.01.1951   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Стрелок-помощник гранатометчика', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                 | 240a7768cf5c694f665938cfd325956690da012a85b8d7fdaf4afd9e |
| ['Степанов Александр Сергеевич']    | 02.03.1973   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Подполковник', position='Командир батальона', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                         | 184d80af2e42d47c0f7852c43a7aad0d95e6361e53a3088dac9b28e2 |
| ['Воробкалов Леонид Владимирович']  | 13.02.1970   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='Рядовой', position='Водитель-радиотелефонист', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                        | 1b412fee36c8ef0433a582cefa2c3a0d82dc247e187d87f660d85c93 |
| ['Карпенко Александр Анатольевич']  | 07.11.1969   | [Row(tag_number=None, unit_code=None, unit_name='111 бригада ДНР', callsign=None, rank='младший сержант', position='Радиотелефонист', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                         | 1ad3593faac852b027dddd539a3f7b14defd8420b8d4e6298795df59 |
```