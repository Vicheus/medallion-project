# Parsetron results

## About row data

> - File path: 136_msbr.csv
> - Total rows: 4575

### Schema
```
root
 |-- №: string (nullable = true)
 |-- Должность: string (nullable = true)
 |-- В_звание: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Личный номер: string (nullable = true)
 |-- Подразделение: string (nullable = true)
 |-- Развернутое подразделение: string (nullable = true)

```

### Data sample
```
| №   | Должность                                                                             | В_звание    | ФИО                             | Дата рождения   | Личный номер   | Подразделение   | Развернутое подразделение   |
|:----|:--------------------------------------------------------------------------------------|:------------|:--------------------------------|:----------------|:---------------|:----------------|:----------------------------|
| п/п |                                                                                       |             |                                 |                 |                |                 |                             |
| .   |                                                                                       |             |                                 |                 |                | управление      | командование                |
| 1   | Командир бригады                                                                      | полковник   | Демурчиев Роман Герадотович     | 30.08.1976      | У-882856       | управление      | командование                |
| 2   | Заместитель командира бригады                                                         | полковник   | Александров Алексей Николаевич  | 22.07.1982      | Х-119984       | управление      | командование                |
| 3   | Заместитель командира бригады                                                         | полковник   | Панфилов Евгений Анатольевич    | 14.08.1977      | Ф-592747       | управление      | командование                |
| 4   | Помощник командира бригады по физической подготовке - начальник физической подготовки | майор       | Меджидов Анварбек Бадрудинович  | 07.08.1978      | Ф-006855       | управление      | командование                |
| .   |                                                                                       |             |                                 |                 |                | управление      | штаб                        |
| 5   | Начальник штаба - заместитель командира бригады                                       | полковник   | Исайкин Виктор Иванович         | 22.11.1981      | Х-227688       | управление      | штаб                        |
| 6   | Заместитель начальника штаба по службе войск и безопасности военной службы            | майор       | Додельцев Дмитрий Николаевич    | 09.04.1988      | Х-527327       | управление      | штаб                        |
| .   |                                                                                       |             |                                 |                 |                | управление      | штаб                        |
| 7   | Заместитель начальника штаба - начальник отделения                                    | майор       | Артамонов Александр Анатольевич | 17.08.1986      | Х-976265       | управление      | штаб                        |
| 8   | Заместитель начальника отделения                                                      | капитан     | Вуколов Алексей Вячеславович    | 01.10.1988      | Э-929817       | управление      | штаб                        |
| 9   | Старший помощник начальника отделения                                                 | капитан     | Цыплаков Михаил Валерьевич      | 28.11.1989      | Э-051408       | управление      | штаб                        |
| 10  | Старший помощник начальника отделения (по математическому моделированию)              | майор       | Сахаров Дмитрий Сергеевич       | 02.04.1986      | Х-584026       | управление      | штаб                        |
| 11  | Помощник начальника отделения                                                         | сержант к/с | Маньков Артем Геннадьевич       | 12.11.1988      | Ю-043508       | управление      | штаб                        |
| 12  | Оператор (по математическому моделированию)                                           | рядовой с/с | Хамидулин Артем Олегович        | 21.07.1995      | РА-273812      | управление      | штаб                        |
| 13  | Чертежник                                                                             | рядовой к/с | Ревенко Сергей Александрович    | 07.11.1999      | РА-249633      | управление      | штаб                        |
| .   |                                                                                       |             |                                 |                 |                | управление      | штаб                        |
| 14  | Заместитель начальника штаба - начальник отделения                                    | капитан     | Казаков Вячеслав Петрович       | 05.11.1989      | Х-132908       | управление      | штаб                        |
| 15  | Старший офицер                                                                        | капитан     | Маслов Владимир Владимирович    | 09.11.1990      | Х-511414       | управление      | штаб                        |
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
| Birth_date | 99.85% |
| Forces | 100.00% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                                 | birth_date   | forces                                                                                                                                                                                                                                                            | source_entity_id                                         |
|:--------------------------------------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| ['Зайцев Андрей Дмитриевич']          | 23.03.1988   | [Row(tag_number='Х686685', unit_code=None, unit_name='136 мотострелковая бригада бмо ар вти', callsign=None, rank='капитан', position='Командир роты', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                               | 114333bbcfb7fbf1fab124dcc21bca71722c90d6506df281511db7b0 |
| ['Галкин Владимир Врежевич']          | 06.02.2002   | [Row(tag_number='РА273078', unit_code=None, unit_name='136 мотострелковая бригада ком. рота', callsign=None, rank='рядовой', position='Регулировщик - радиотелефонист', mos_code=None, category=2, date_start=None, date_end=None, comment=None)]                 | 3df129438e469f0368bbf051729ebd83590e7b76fd08eadc49b3cf1d |
| ['Горностаев Олег Дмитриевич']        | 12.05.1999   | [Row(tag_number='РА271984', unit_code=None, unit_name='136 мотострелковая бригада рб ргр', callsign=None, rank='рядовой', position='Разведчик - радиотелефонист', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                       | 738063224066fd011786554b5feb6d1ac0231f84c3fe950df8341a7b |
| ['Магомедов Магомед Идрисович']       | 25.06.1988   | [Row(tag_number='СУ050386', unit_code=None, unit_name='136 мотострелковая бригада тб 1 тр', callsign=None, rank='сержант', position='Командир танка', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                                   | 759bcc3e50cf2226d17ad5d0538a48deebb5cba289db579eafbfef25 |
| ['Черниговский Юрий Александрович']   | 27.10.1990   | [Row(tag_number='ЕХ593275', unit_code=None, unit_name='136 мотострелковая бригада ррэб', callsign=None, rank='ст. лейтенант', position='Командир взвода', mos_code=None, category=None, date_start=None, date_end=None, comment=None)]                            | 86513d8608a23455614afc5b1ff5f7774049ef80206bf857d6051c1c |
| ['Ирасханов Магомедсаид Ирасханович'] | 14.06.1986   | [Row(tag_number='ВС424809', unit_code=None, unit_name='136 мотострелковая бригада ррхбз', callsign=None, rank='сержант', position='Командир отделения', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                                 | 8805ed18196aa4da4691386955817bb0aa2749315d5d6f645690255f |
| ['Мутаев Руслан Камилович']           | 20.04.1993   | [Row(tag_number='ВС164284', unit_code=None, unit_name='136 мотострелковая бригада реадн 2 реабатр', callsign=None, rank='мл. сержант', position='Водитель - заряжающий', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                | af09caed28888b0336e9a7fa959e231226552af0efa07a7759911617 |
| ['Магомедов Магомед Гамзатович']      | 12.02.1989   | [Row(tag_number='СУ050336', unit_code=None, unit_name='136 мотострелковая бригада тб во', callsign=None, rank='сержант', position='Водитель', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                                           | f8efe0c018d2d07ed0537da6be03ce32f1b02b0c5ba0c209de51ae7f |
| ['Гамзатов Магомедгусейн Гаджиевич']  | 01.01.1979   | [Row(tag_number='ЕХ519146', unit_code=None, unit_name='136 мотострелковая бригада бмо ар пг', callsign=None, rank='сержант', position='Старший водитель - заправщик', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                   | 03fe2114e796ec5e884388889c830909589b21875596fd074ffab1d1 |
| ['Асланов Мирза Асланович']           | 09.09.1981   | [Row(tag_number='Ф037009', unit_code=None, unit_name='136 мотострелковая бригада 1 мсб минбат', callsign=None, rank='сержант', position='Командир миномета', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                            | 16323dd32154d2f46ea58b68b4f416bc6475e2957875f2dc4786f69c |
| ['Романенко Александр Андреевич']     | 08.12.1998   | [Row(tag_number='ВС482038', unit_code=None, unit_name='136 мотострелковая бригада рб 1 рр', callsign=None, rank='ефрейтор', position='Наводчик оператор', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                               | 8589724dace1ae9418ae24b8f2e446a023f36e730dd7abef1e88284c |
| ['Гаджиев Нажмутдин Курбанович']      | 20.08.1988   | [Row(tag_number='СУ050391', unit_code=None, unit_name='136 мотострелковая бригада 2 мсб 6 мср', callsign=None, rank='мл. сержант', position='Гранатометчик', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                            | 8ef0617c24e2de6ca93a2bf368bfb1abb494da9040e2a6c8bc380b06 |
| ['Шихалиев Забит Абдулмуслимович']    | 31.08.1981   | [Row(tag_number='ЕХ574573', unit_code=None, unit_name='136 мотострелковая бригада 3 мсб минбат', callsign=None, rank='рядовой', position='Водитель', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                                    | ae986f2529c61497e7826d7592e5209a125a6760c2f353f5be5a633c |
| ['Кривоножкин Павел Владимирович']    | 25.04.1987   | [Row(tag_number='Э893764', unit_code=None, unit_name='136 мотострелковая бригада здн 1 зрбатр', callsign=None, rank='сержант', position='Командир машины', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                              | e069cf3c69b9580448ca74b37da3e80256a527744da5da4cf144f085 |
| ['Сварыч Николай Юрьевич']            | 28.04.1992   | [Row(tag_number='ЕХ507558', unit_code=None, unit_name='136 мотострелковая бригада 1 гсадн 3 гсабатр', callsign=None, rank='мл. сержант', position='Командир отделения - топогеодезист', mos_code=None, category=1, date_start=None, date_end=None, comment=None)] | 4ec5956227c4ecf15287f18b5b42a8d5a614851f32e1c2db2987d423 |
| ['Таов Алим Мухамедович']             | 03.02.1988   | [Row(tag_number='Э276462', unit_code=None, unit_name='136 мотострелковая бригада бс рс пу', callsign=None, rank='сержант', position='Командир отделения', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                               | 7c1fda55b0903fa7c9611875de092f5212f9c833531938d759735cde |
| ['Сигрийчук Анна Ашотовна']           | 22.12.1987   | [Row(tag_number='ВС216506', unit_code=None, unit_name='136 мотострелковая бригада зрдн втр', callsign=None, rank='рядовой', position='Оператор - радиотелефонист', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]                      | d723aa53821b9ef8fdf596bcac1928be3a326f92f611fe836731bcaf |
| ['Шихаев Изамутдин Садрутдинович']    | 16.09.1978   | [Row(tag_number='Ф108644', unit_code=None, unit_name='136 мотострелковая бригада исб иср', callsign=None, rank='сержант', position='Заместитель командира взвода - командир отделения', mos_code=None, category=1, date_start=None, date_end=None, comment=None)] | 2c97826c7e6e11db5eb6c5e6e54bacfd05ae365cec2ccdb853ce62c7 |
| ['Дибиров Юсуп Гимбатович']           | 25.06.1976   | [Row(tag_number='Ф108734', unit_code=None, unit_name='136 мотострелковая бригада 1 мсб вс', callsign=None, rank='рядовой', position='Механик - водитель - гранатометчик', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]               | 6dc0568aef7e162f94e9e0c703c4a784fa72153a5ed44150a259d672 |
| ['Курбанов Султанмурад Алимурадович'] | 07.07.1978   | [Row(tag_number='СУ050186', unit_code=None, unit_name='136 мотострелковая бригада 2 гсадн ву д', callsign=None, rank='мл. сержант', position='Старший разведчик - дальномерщик', mos_code=None, category=1, date_start=None, date_end=None, comment=None)]        | 86954eb61c74ff3f0811310131296bf92dcc2963eb4cda3a4997c7e8 |
```