# Parsetron results

## About row data

> - File path: Войсковая часть 77984.csv
> - Total rows: 142

### Schema
```
root
 |-- Фамилмя, имя, отчество: string (nullable = true)
 |-- Воинское звание: string (nullable = true)
 |-- Личный номер: string (nullable = true)
 |-- Номер воинской части: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Наименование воинской части: string (nullable = true)
 |-- Подчиненность: string (nullable = true)

```

### Data sample
```
| Фамилмя, имя, отчество        | Воинское звание   | Личный номер   | Номер воинской части   | Дата рождения   | Наименование воинской части   | Подчиненность          |
|:------------------------------|:------------------|:---------------|:-----------------------|:----------------|:------------------------------|:-----------------------|
| Рязанов Алексей Борисович     | Капитан           | Ф-144420       | Войсковая часть 77984  | 05.09.1983      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Коротких Дмитрий Анатольевич  | Капитан           | Ф-764928       | Войсковая часть 77984  | 04.11.1977      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Наквасин Дмитрий Сергеевич    | Капитан           | Х-581771       | Войсковая часть 77984  | 06.10.1986      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Букало Сергей Васильевич      | Подполковник      | Ф-919204       | Войсковая часть 77984  | 15.12.1980      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Добровский Сергей Олегович    | Подполковник      | Ф-766000       | Войсковая часть 77984  | 07.05.1978      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Могилев Виталий Анатольевич   | Капитан           | У-823302       | Войсковая часть 77984  | 28.09.1978      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Алексеенко Олег Александрович | Лейтенант         | У-606335       | Войсковая часть 77984  | 08.12.1978      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Дементьев Андрей Николаевич   | Майор             | У-812125       | Войсковая часть 77984  | 16.10.1974      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Лаур Олег Владимирович        | Майор             | У-451627       | Войсковая часть 77984  | 10.01.1976      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Веденин Станислав Викторович  | Майор             | Т-916230       | Войсковая часть 77984  | 01.09.1971      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Мухин Сергей Владимирович     | Подполковник      | Т-756984       | Войсковая часть 77984  | 21.03.1969      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Смальков Виталий Николаевич   | Капитан           | У-852043       | Войсковая часть 77984  | 11.01.1977      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Рябикин Алексей Викторович    | Подполковник      | Ф-650715       | Войсковая часть 77984  | 01.01.1977      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Апханов Анатолий Георгиевич   | Капитан           | Х-094255       | Войсковая часть 77984  | 13.03.1982      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Бакуменко Евгений Геннадьевич | Майор             | Ф-342140       | Войсковая часть 77984  | 09.12.1977      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Баргин Сергей Викторович      | Подполковник      | У-968334       | Войсковая часть 77984  | 05.08.1976      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Безгин Денис Геннадьевич      | Майор             | У-838516       | Войсковая часть 77984  | 24.09.1975      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Белозеров Павел Николаевич    | Майор             | Ф-891021       | Войсковая часть 77984  | 05.04.1980      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Бовырин Андрей Евгеньевич     | Майор             | Ф-891024       | Войсковая часть 77984  | 25.05.1978      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
| Бойко Евгений Евгеньевич      | Капитан           | Ф-399736       | Войсковая часть 77984  | 11.08.1976      | 23 иап                        | 303 сад 11 А ВВС и ПВО |
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
| names                               | birth_date   | forces                                                                                                                                                                                                                        | source_entity_id                                         |
|:------------------------------------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| ['Еремеев Сергей Васильевич']       | 26.03.1984   | [Row(tag_number='Х838728', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Лейтенант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]         | c9e168ffb422710333c69733dd01911d9668db798f549258bcfef434 |
| ['Закутний Сергей Алексеевич']      | 07.07.1983   | [Row(tag_number='Ф144445', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Старший лейтенант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)] | c3d5d8157659790aa1014e47d30ecf1cd345f1321600677c4be5580e |
| ['Золотухин Владимир Анатольевич']  | 18.05.1978   | [Row(tag_number='У968888', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | b2b28cccd10360c43515d11b77efc220f569a124dc272c35da056bbc |
| ['Коновалов Андрей Николаевич']     | 10.11.1981   | [Row(tag_number='Ф868349', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | 42dcb7c4957d58b04c4773d5357350be674f6625f08832cebca352bb |
| ['Тименко Николай Михайлович']      | 23.04.1974   | [Row(tag_number='У346232', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | 50eacbf85eb58aae6fc52c8410980b5a97dd6535ab2c3b2df4678b68 |
| ['Роженцов Алексей Сергеевич']      | 21.06.1978   | [Row(tag_number='Ф692252', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | 9447d28ea18d98e1e34228e8be132a214160c7d2947e84f2f00fc1fd |
| ['Фролов Артем Игоревич']           | 20.01.1980   | [Row(tag_number='Ф969844', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | 318075cb72d5b0f52070e3e0b15acffcfe1c72a25285063448d53116 |
| ['Болдырев Андрей Николаевич']      | 27.02.1973   | [Row(tag_number='У396878', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | 274b8709add8302e6297811fddccc8d47ccf0c973478e1cb7412c06b |
| ['Спесивцев Евгений Александрович'] | 01.12.1978   | [Row(tag_number='Ф649806', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | 64e6ac11bac0b83f213de265d03dc14b38b651dd2c2dfd0c9e00c944 |
| ['Гуськов Максим Николаевич']       | 08.09.1977   | [Row(tag_number='У606732', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Лейтенант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]         | a02cea43da49176e3a21894fe094f138053c06eaf444644ada4b5c61 |
| ['Алексеенко Олег Александрович']   | 08.12.1978   | [Row(tag_number='У606335', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Лейтенант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]         | 522c07f0076f548b8c65803a859e45625934b59e8891760d7f846f44 |
| ['Букало Сергей Васильевич']        | 15.12.1980   | [Row(tag_number='Ф919204', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Подполковник', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]      | 85261da3074655c93b0371e27670507124bbe902564aaf4d3b7c93a8 |
| ['Баргин Сергей Викторович']        | 05.08.1976   | [Row(tag_number='У968334', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Подполковник', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]      | 4d5b90065313f031eb7f34c405c33dc46acc7bf73853605952c9ff25 |
| ['Шахимарданов Игорь Шамильевич']   | 19.01.1975   | [Row(tag_number='У071459', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | 670b75849dc2fae2f32a275212672706adcbcaaea0fa3a5accaf99d2 |
| ['Лобынцев Александр Анатольевич']  | 27.01.1977   | [Row(tag_number='Ф344857', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Подполковник', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]      | 16fa523ac804adb98e408561ec1cdffd7bdf1a809cfbfbb6b6c6f6a4 |
| ['Иванов Алексей Анатольевич']      | 25.04.1976   | [Row(tag_number='Ф799011', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Старший лейтенант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)] | 5b5ccfd85bea71fff841264387d5611a85972d6ba9464010d6cf85e3 |
| ['Поздняков Сергей Анатольевич']    | 07.12.1977   | [Row(tag_number='У823310', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | 1b22b799e04a07b8fd0e5ab71873b0cc5752d9dae8fecaa36b8f265a |
| ['Звягин Андрей Владимирович']      | 19.08.1978   | [Row(tag_number='Ф197736', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | fcc09606ad6916126b2d0c6aa7c64a132340228f16ec3df9187fe51e |
| ['Добровский Сергей Олегович']      | 07.05.1978   | [Row(tag_number='Ф766000', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Подполковник', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]      | dc5fd04acc1f8d819482a150e0410e8782abacd6e119e82e61901af8 |
| ['Диденко Андрей Александрович']    | 27.12.1977   | [Row(tag_number='У968813', unit_code='77984', unit_name='11 А ВВС и ПВО 303 сад 23 иап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | 7514f12f49652947e979155719ccbdbc3db18f299dd689bd9d97b6d9 |
```