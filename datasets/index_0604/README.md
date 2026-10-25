# Parsetron results

## About row data

> - Code name: index_0604
> - File path: 20260326-122219-933-file-МОС ОСАГО июль 2022(1).csv
> - Total rows: 10532

### Schema
```
root
 |-- Системный номер: integer (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- город: string (nullable = true)
 |-- Телефон: string (nullable = true)
 |-- Госномер: string (nullable = true)
 |-- VIN: string (nullable = true)
 |-- Модель: string (nullable = true)
 |-- ,: string (nullable = true)

```

### Data sample
```
|   Системный номер | ФИО                                | Дата рождения   | город          |    Телефон | Госномер   | VIN               | Модель                 | ,   |
|------------------:|:-----------------------------------|:----------------|:---------------|-----------:|:-----------|:------------------|:-----------------------|:----|
|                 3 | САФРОНОВ ВЛАДИМИР ВИКТОРОВИЧ       | 14.06.1962      | г Серпухов     | 9036686616 | М024МХ790  | Z94PF815BNR039537 | Hyundai Creta CRETA    | ,   |
|                 4 | КОРОЛЕВА МАРИНА ГЕННАДЬЕВНА        | 12.10.1959      | г Москва       | 9161328017 | У926ХЕ799  | Z94PC815DNR041150 | Hyundai Creta CRETA    | ,   |
|                 5 | ВАРЛАМОВА ТАТЬЯНА НИКОЛАЕВНА       | 31.10.1972      | Московская обл | 9645102935 | М404МХ790  | Z94PC814BNR032168 | Hyundai Creta CRETA    | ,   |
|                 6 | НИЗАМОВА НАТАЛЬЯ РИНАТОВНА         | 13.09.1995      | г Москва       | 9151267030 | Т652УУ799  | Z94C251BBNR178253 | Kia RIO                | ,   |
|                 7 | ШАВИТОВ АЛЕКСЕЙ ВЛАДИМИРОВИЧ       | 10.05.1965      | Московская обл | 9162421618 | Т028ТА790  | Z94C241BANR263630 | Kia RIO RIO            | ,   |
|                 8 | КОМКОВ МАКСИМ ВЛАДИМИРОВИЧ         | 26.05.1970      | г Дубна        | 9037835255 | Н340МУ790  | Z8NTANT32ES157713 | Nissan X-Trail X-TRAIL | ,   |
|                 9 | ЛОСЕВА АННА СЕРГЕЕВНА              | 03.06.1987      | г Москва       | 9167006927 | Т977СС799  | Y4K8622Z9NB904338 | Geely Coolray COOLRAY  | ,   |
|                10 | ПРОКОФЬЕВА ОЛЕСЯ АЛЕКСЕЕВНА        | 04.04.1997      | г Реутов       | 9013312665 | С766МХ790  | Y4K8622Z4NB904246 | Geely Coolray COOLRAY  | ,   |
|                11 | КОРОТКОВ ДМИТРИЙ ВЛАДИСЛАВОВИЧ     | 12.07.1970      | г Москва       | 9199916764 | Н761РР799  | Y4K8622Z4NB903646 | Geely Coolray COOLRAY  | ,   |
|                12 | КОЧЕТКОВ АЛЕКСЕЙ ЮРЬЕВИЧ           | 01.11.1982      | г Ступино      | 9263053093 | У153ТА790  | XZGFF06AXNA324570 | Haval F7 F7            | ,   |
|                13 | СОЛОВЬЁВА НАДЕЖДА АЛЕКСЕЕВНА       | 23.03.1960      | Московская обл | 9035300164 | О805СС790  | XZGFF06A7NA326258 | Haval F7 F7            | ,   |
|                14 | ДОБРИНИН АЛЕКСЕЙ АЛЕКСЕЕВИЧ        | 09.07.1982      | г Москва       | 9296615207 | Н057ХХ799  | XZGFF06A5NA618846 | Haval, Прочие F7X      |     |
|                15 | ЕРМОЛЕНКО АЛЕКСАНДР ВЛАДИМИРОВИЧ   | 07.02.1965      | г Москва       | 9036119361 | У558РР799  | XZGFE04A8NA816620 | Haval ДЖОЛИОН          | ,   |
|                16 | СИНЕЛЬНИКОВ МАКСИМ ВАЛЕРЬЕВИЧ      | 24.07.1991      | г Москва       | 9671826650 | Т750УУ799  | XZGEE04AXNA816887 | Haval Jolion, - JOLION |     |
|                17 | КРАСИЛЬЩИКОВА ТАТЬЯНА ВЛАДИМИРОВНА | 29.09.1973      | г Москва       | 9055664455 | У436РР799  | XZGEE04A1NA815983 | Haval ДЖОЛИОН          | ,   |
|                18 | ЗАХАРОВ НАЗАР ФАРХОДОВИЧ           | 30.05.1993      | г Москва       | 9099997139 | Н106ХХ799  | XWEPH81ABM0055755 | Kia SPORTAGE SPORTAGE  | ,   |
|                19 | ДОЛГОВА ЛЮБОВЬ АЛЕКСАНДРОВНА       | 23.08.1989      | г Москва       | 9154772971 | Х041МХ797  | XWEFE41CBNC000042 | Kia Cerato CERATO      | ,   |
|                20 | ЧУСОВ ПАВЕЛ ГЕННАДЬЕВИЧ            | 23.11.1980      | г Москва       | 9055666643 | О571ХХ799  | XWEE3811CLC000182 | Kia СЕЛТОС             | ,   |
|                21 | ОБЫДЁННОВ ИГОРЬ ПЕТРОВИЧ           | 01.02.1969      | Московская обл | 9057018380 | Н302ТА790  | XWEE3811BNC008064 | Kia SELTOS             | ,   |
|                22 | СТЕПАНОВИЧ АНЖЕЛИКА ВЯЧЕСЛАВОВНА   | 10.08.1968      | г Москва       | 9031714637 | М302ИИ790  | XW8JC9NU9NH206619 | Skoda Karoq            | ,   |
```


## About final data
> - Total rows: 10523

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- vehicles: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = false)
 |    |    |-- model: string (nullable = true)
 |    |    |-- year: integer (nullable = true)
 |    |    |-- color: string (nullable = true)
 |    |    |-- number: string (nullable = true)
 |    |    |-- vin: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 100.00% |
| Address | 100.00% |
| Phones | 95.88% |
| Vehicles | 100.00% |



### Data sample
```
| names                                  | birth_date   | address            | phones          | vehicles                                                                                                                       |
|:---------------------------------------|:-------------|:-------------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------|
| ['Сафронов Владимир Викторович']       | 14.06.1962   | ['г Серпухов']     | ['79036686616'] | [Row(type=1, model='Hyundai Creta CRETA', year=None, color=None, number='М024МХ790', vin='Z94PF815BNR039537', comment=None)]   |
| ['Королева Марина Геннадьевна']        | 12.10.1959   | ['г Москва']       | ['79161328017'] | [Row(type=1, model='Hyundai Creta CRETA', year=None, color=None, number='У926ХЕ799', vin='Z94PC815DNR041150', comment=None)]   |
| ['Варламова Татьяна Николаевна']       | 31.10.1972   | ['Московская обл'] | ['79645102935'] | [Row(type=1, model='Hyundai Creta CRETA', year=None, color=None, number='М404МХ790', vin='Z94PC814BNR032168', comment=None)]   |
| ['Низамова Наталья Ринатовна']         | 13.09.1995   | ['г Москва']       | ['79151267030'] | [Row(type=1, model=None, year=None, color=None, number='Т652УУ799', vin='Z94C251BBNR178253', comment=None)]                    |
| ['Шавитов Алексей Владимирович']       | 10.05.1965   | ['Московская обл'] | ['79162421618'] | [Row(type=1, model=None, year=None, color=None, number='Т028ТА790', vin='Z94C241BANR263630', comment=None)]                    |
| ['Комков Максим Владимирович']         | 26.05.1970   | ['г Дубна']        | ['79037835255'] | [Row(type=1, model=None, year=None, color=None, number='Н340МУ790', vin='Z8NTANT32ES157713', comment=None)]                    |
| ['Лосева Анна Сергеевна']              | 03.06.1987   | ['г Москва']       | ['79167006927'] | [Row(type=1, model='Geely Coolray COOLRAY', year=None, color=None, number='Т977СС799', vin='Y4K8622Z9NB904338', comment=None)] |
| ['Прокофьева Олеся Алексеевна']        | 04.04.1997   | ['г Реутов']       | ['79013312665'] | [Row(type=1, model='Geely Coolray COOLRAY', year=None, color=None, number='С766МХ790', vin='Y4K8622Z4NB904246', comment=None)] |
| ['Коротков Дмитрий Владиславович']     | 12.07.1970   | ['г Москва']       | ['79199916764'] | [Row(type=1, model='Geely Coolray COOLRAY', year=None, color=None, number='Н761РР799', vin='Y4K8622Z4NB903646', comment=None)] |
| ['Кочетков Алексей Юрьевич']           | 01.11.1982   | ['г Ступино']      | ['79263053093'] | [Row(type=1, model='Haval F7 F7', year=None, color=None, number='У153ТА790', vin='XZGFF06AXNA324570', comment=None)]           |
| ['Соловьва Надежда Алексеевна']        | 23.03.1960   | ['Московская обл'] | ['79035300164'] | [Row(type=1, model='Haval F7 F7', year=None, color=None, number='О805СС790', vin='XZGFF06A7NA326258', comment=None)]           |
| ['Добринин Алексей Алексеевич']        | 09.07.1982   | ['г Москва']       | ['79296615207'] | [Row(type=1, model='Haval Прочие F7X', year=None, color=None, number='Н057ХХ799', vin='XZGFF06A5NA618846', comment=None)]      |
| ['Ермоленко Александр Владимирович']   | 07.02.1965   | ['г Москва']       | ['79036119361'] | [Row(type=1, model='Haval ДЖОЛИОН', year=None, color=None, number='У558РР799', vin='XZGFE04A8NA816620', comment=None)]         |
| ['Синельников Максим Валерьевич']      | 24.07.1991   | ['г Москва']       | ['79671826650'] | [Row(type=1, model='Haval Jolion - JOLION', year=None, color=None, number='Т750УУ799', vin='XZGEE04AXNA816887', comment=None)] |
| ['Красильщикова Татьяна Владимировна'] | 29.09.1973   | ['г Москва']       | ['79055664455'] | [Row(type=1, model='Haval ДЖОЛИОН', year=None, color=None, number='У436РР799', vin='XZGEE04A1NA815983', comment=None)]         |
| ['Захаров Назар Фарходович']           | 30.05.1993   | ['г Москва']       | ['79099997139'] | [Row(type=1, model=None, year=None, color=None, number='Н106ХХ799', vin='XWEPH81ABM0055755', comment=None)]                    |
| ['Долгова Любовь Александровна']       | 23.08.1989   | ['г Москва']       | ['79154772971'] | [Row(type=1, model=None, year=None, color=None, number='Х041МХ797', vin='XWEFE41CBNC000042', comment=None)]                    |
| ['Чусов Павел Геннадьевич']            | 23.11.1980   | ['г Москва']       | ['79055666643'] | [Row(type=1, model=None, year=None, color=None, number='О571ХХ799', vin='XWEE3811CLC000182', comment=None)]                    |
| ['Обыдннов Игорь Петрович']            | 01.02.1969   | ['Московская обл'] | ['79057018380'] | [Row(type=1, model=None, year=None, color=None, number='Н302ТА790', vin='XWEE3811BNC008064', comment=None)]                    |
| ['Степанович Анжелика Вячеславовна']   | 10.08.1968   | ['г Москва']       | ['79031714637'] | [Row(type=1, model='Skoda Karoq', year=None, color=None, number='М302ИИ790', vin='XW8JC9NU9NH206619', comment=None)]           |
```