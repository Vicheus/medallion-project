# Parsetron results

## About row data

> - Code name: index_0710
> - File path: Войсковая часть 78018.csv
> - Total rows: 91

### Schema
```
root
 |-- Фамилия, имя, отчество: string (nullable = true)
 |-- Воинское звание: string (nullable = true)
 |-- Личный номер: string (nullable = true)
 |-- Номер воинской части: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Наименование воинской части: string (nullable = true)
 |-- Подчиненность: string (nullable = true)

```

### Data sample
```
| Фамилия, имя, отчество           | Воинское звание   | Личный номер   | Номер воинской части   | Дата рождения   | Наименование воинской части   | Подчиненность          |
|:---------------------------------|:------------------|:---------------|:-----------------------|:----------------|:------------------------------|:-----------------------|
| Астанин Игорь Сергеевич          | Майор             | У-823272       | Войсковая часть 78018  | 5/30/1978       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Чехляев Вячеслав Владиславович   | Подполковник      | У-968393       | Войсковая часть 78018  | 10/6/1975       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Глушак Александр Александрович   | Подполковник      | У-969185       | Войсковая часть 78018  | 4/28/1975       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Ахметшин Радиф Фаридович         | Майор             | У-732214       | Войсковая часть 78018  | 3/25/1974       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Бурнашов Валерий Николаевич      | Майор             | У-512550       | Войсковая часть 78018  | 9/9/1972        | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Вострецов Александр Иванович     | Старший лейтенант | Ф-799314       | Войсковая часть 78018  | 1/19/1980       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Дивин Артем Владимирович         | Капитан           | Ф-095868       | Войсковая часть 78018  | 8/11/1980       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Дорошенко Сергей Георгиевич      | Майор             | Т-602517       | Войсковая часть 78018  | 12/16/1973      | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Каничев Сергей Александрович     | Капитан           | У-904596       | Войсковая часть 78018  | 2/7/1975        | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Клюев Юрий Вячеславович          | Капитан           | Л-904502       | Войсковая часть 78018  | 2/22/1972       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Макаренко Андрей Николаевич      | Капитан           | Ф-692243       | Войсковая часть 78018  | 8/18/1978       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Плаксин Юрий Васильевич          | Полковник         | У-513228       | Войсковая часть 78018  | 10/27/1973      | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Семениченко Евгений Владимирович | Майор             | У-512479       | Войсковая часть 78018  | 4/8/1972        | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Стальмаков Сергей Васильевич     | Майор             | У-838327       | Войсковая часть 78018  | 1/10/1975       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Яркин Олег Викторович            | Подполковник      | Ф-891265       | Войсковая часть 78018  | 8/12/1981       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Андреев Андрей Александрович     | Подполковник      | У-968333       | Войсковая часть 78018  | 4/25/1976       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Бражников Алексей Николаевич     | Капитан           | Т-602447       | Войсковая часть 78018  | 1/15/1974       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Зарипов Альберт Анварович        | Капитан           | М-261536       | Войсковая часть 78018  | 7/30/1972       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Кутуков Андрей Петрович          | Майор             | Ф-897081       | Войсковая часть 78018  | 12/10/1978      | 18 шап                        | 303 сад 11 А ВВС и ПВО |
| Лазарев Юрий Петрович            | Подполковник      | Ф-208952       | Войсковая часть 78018  | 7/19/1980       | 18 шап                        | 303 сад 11 А ВВС и ПВО |
```


## About final data
> - Total rows: 91

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
| ['Сметанин Юрий Анатольевич']       | 15.10.1972   | [Row(tag_number='У460821', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | 1d451de0b58390b8d3231660bcde682e30e7616164493d6e6130d41a |
| ['Дубов Евгений Анатольевич']       | 18.05.1976   | [Row(tag_number='Т896417', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | 3ecad00f49191250e8c9251eabda243fbaee0d55fe185bb6ae9508d9 |
| ['Конорев Александр Владимирович']  | 26.08.1973   | [Row(tag_number='Т914895', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | f94e26e581e559ed00244450b1ee36f13f6cbc143ed16bf3aca13ebd |
| ['Бурнашов Валерий Николаевич']     | 09.09.1972   | [Row(tag_number='У512550', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | 2ae0a1f460a176224994ce82c52479504153c84d3318fbcb4d960254 |
| ['Борисенко Борис Борисович']       | 30.05.1983   | [Row(tag_number='Ф144537', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | c55ce41472915fc4b579ae0fe024dfff3ea6af911084bb4f93b1993d |
| ['Иванов Сергей Николаевич']        | 28.12.1974   | [Row(tag_number='У968296', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Старший лейтенант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)] | 271cb87a698ab05b736980b9cc5a1c4243496a515fd1f61df867bbce |
| ['Сатаров Станислав Владиславович'] | 05.08.1976   | [Row(tag_number='У812266', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | 503c32d9faed8787331546289cfe3f57b111ee69cf4f488219a46f73 |
| ['Лазарев Юрий Петрович']           | 19.07.1980   | [Row(tag_number='Ф208952', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Подполковник', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]      | e8bc8cad56e145d98bc310ac9e2baa1b05ca0beffc174534e54d5762 |
| ['Соловьев Сергей Владимирович']    | 25.10.1974   | [Row(tag_number='У660831', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | a5a7a2717245ae8405dd2da1d0c4b39b32896136472c0235b34cf3b0 |
| ['Бандалак Эдуард Васильевич']      | 04.03.1973   | [Row(tag_number='У564913', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Подполковник', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]      | f25a26c88064da194af62028e2fbf76e4bb20c4820b49c5438fdf80f |
| ['Полторак Максим Николаевич']      | 07.08.1969   | [Row(tag_number='У153436', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Подполковник', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]      | cb4211ae4ad59604cf315f35e337960108c6f2c7bff590a120a0c914 |
| ['Карапыш Сергей Владимирович']     | 25.08.1989   | [Row(tag_number='Х692787', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Старший лейтенант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)] | 716613d6782d60e9199ae9fe72e6d64fb50aea6c9670e035b9d3a881 |
| ['Клюев Юрий Вячеславович']         | 22.02.1972   | [Row(tag_number='Л904502', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | 92e3ac89c76525110f84acf34d5df0c4fc02052d15f333dbe0b34cdf |
| ['Шубин Сергей Александрович']      | 18.10.1980   | [Row(tag_number='Ф095735', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | 031e87c096feee78ad3f7bd9256f0f8b78c6f976cb1871387b21d431 |
| ['Белухин Сергей Владимирович']     | 05.06.1976   | [Row(tag_number='Ф739045', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | 89152d8953846aeec45ceba9a136a94d19fdeb88517b0d3c862a4594 |
| ['Анфёров Дмитрий Сергеевич']       | 01.05.1977   | [Row(tag_number='Т896642', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | c04c9f423c7033a0c63c5556edf55126ada4f797be28cff26c5b260b |
| ['Приходько Дмитрий Сергеевич']     | 09.01.1979   | [Row(tag_number='Ф969434', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | ae1b835d4d702d2f1755548a497c5d11320d9e74ccd4d5a99913e155 |
| ['Сочин Александр Юрьевич']         | 10.02.1982   | [Row(tag_number='Ф868516', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Капитан', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]           | b469177b44110a842b0bbf58c72dd6e5f1faa1e1950cfa73064f9fdd |
| ['Жуковский Евгений Валерьевич']    | 16.09.1989   | [Row(tag_number='Ю007674', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Лейтенант', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]         | 6bb513db16b6129b7e39814406a6017ab49c42dc3ed2218a4e651d1f |
| ['Князев Сергей Валерьевич']        | 25.12.1979   | [Row(tag_number='Ф095927', unit_code='78018', unit_name='11 А ВВС и ПВО 303 сад 18 шап', callsign=None, rank='Майор', position=None, mos_code=None, category=None, date_start=None, date_end=None, comment=None)]             | 643e98ebf1e878ae47b538c7d22385d97b6f2185fc5ced5b43e1bfc8 |
```