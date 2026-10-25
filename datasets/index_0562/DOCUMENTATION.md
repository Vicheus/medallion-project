# Parsetron results

## About row data

> - File path: clients_*.csv
> - Total rows: 7338586

### Schema
```
root
 |-- userInc: string (nullable = true)
 |-- Фамилия_кириллица: string (nullable = true)
 |-- Имя_кириллица: string (nullable = true)
 |-- Отчество_кириллица: string (nullable = true)
 |-- Фамилия_латиница: string (nullable = true)
 |-- Имя_латиница: string (nullable = true)
 |-- Отчество_латиница: string (nullable = true)
 |-- Обращение: string (nullable = true)
 |-- Пол: string (nullable = true)
 |-- Дата_рождения: string (nullable = true)
 |-- Страна_рождения: string (nullable = true)
 |-- Гражданство: string (nullable = true)
 |-- Тип_документа: string (nullable = true)
 |-- Серия_документа: string (nullable = true)
 |-- Номер_документа: string (nullable = true)
 |-- Документ_выдан: string (nullable = true)
 |-- Действителен_до: string (nullable = true)
 |-- Мобильный: string (nullable = true)
 |-- E-mail: string (nullable = true)

```

### Data sample
```
|   userInc | Фамилия_кириллица   | Имя_кириллица   | Отчество_кириллица   | Фамилия_латиница   | Имя_латиница   | Отчество_латиница   | Обращение   | Пол     | Дата_рождения   |   Страна_рождения |   Гражданство |   Тип_документа |   Серия_документа |   Номер_документа | Документ_выдан   | Действителен_до   |    Мобильный | E-mail                     |
|----------:|:--------------------|:----------------|:---------------------|:-------------------|:---------------|:--------------------|:------------|:--------|:----------------|------------------:|--------------:|----------------:|------------------:|------------------:|:-----------------|:------------------|-------------:|:---------------------------|
|  32549589 | DMITRIEV            | ALEKSEI         |                      | DMITRIEV           | ALEKSEI        |                     | MR          | Мужской | 22.12.1984      |                 2 |             2 |               3 |                66 |           7992634 | 18.03.2024       | 18.03.2029        | +79272140474 | annakilina89@yandex.ru     |
|  32549585 | KARPOV              | NIKOLAI         |                      | KARPOV             | NIKOLAI        |                     | MR          | Мужской | 17.12.1994      |                 2 |             2 |               3 |                67 |           3170246 | 16.10.2025       | 16.10.2030        | +79293795140 | komaroff71@inbox.ru        |
|  32549584 | ZHOROVA             | IRINA           |                      | ZHOROVA            | IRINA          |                     | MRS         | Женский | 12.05.1996      |                 2 |             2 |               3 |                77 |           4017753 | 08.07.2024       | 08.07.2034        | +79264279986 | komaroff71@inbox.ru        |
|  32549583 | ZLOBIN              | MAKAR           |                      | ZLOBIN             | MAKAR          |                     | MR          | Мужской | 20.08.2012      |                 2 |             2 |               3 |                73 |           4180636 | 26.05.2016       | 26.05.2026        | +79229537987 | ooostroidom2012@mail.ru    |
|  32549582 | ZLOBINA             | EVGENIIA        |                      | ZLOBINA            | EVGENIIA       |                     | MRS         | Женский | 22.08.1988      |                 2 |             2 |               3 |                77 |           2537792 | 16.02.2024       | 16.02.2034        | +79229537987 | ooostroidom2012@mail.ru    |
|  32549579 | LEONOVA             | OLESYA          |                      | LEONOVA            | OLESYA         |                     | MRS         | Женский | 02.04.1984      |                 2 |             2 |               3 |                76 |           6638116 | 16.02.2022       | 16.02.2032        | +79151865545 | SUTA@MAIL.RU               |
|  32549578 | LEONOV              | ILYA            |                      | LEONOV             | ILYA           |                     | MR          | Мужской | 16.03.1982      |                 2 |             2 |               3 |                76 |           5144451 | 31.07.2021       | 31.07.2031        | +79151865545 | SUTA@MAIL.RU               |
|  32549577 | GROMYSHEVA          | ANASTASIIA      |                      | GROMYSHEVA         | ANASTASIIA     |                     | MRS         | Женский | 16.04.2000      |                 2 |             2 |               3 |                77 |           1261100 | 31.08.2023       | 31.08.2033        | +79087827605 | kosmopolit31@yandex.ru     |
|  32549576 | BABICHEV            | STANISLAV       |                      | BABICHEV           | STANISLAV      |                     | MR          | Мужской | 13.03.1992      |                 2 |             2 |               3 |                76 |           6433942 | 27.01.2022       | 27.01.2032        | +79087827605 | kosmopolit31@yandex.ru     |
|  32549574 | SEVASTYANOVA        | ANASTASIYA      |                      | SEVASTYANOVA       | ANASTASIYA     |                     | MRS         | Женский | 20.10.1983      |                 2 |             2 |               3 |                76 |           6104730 | 06.12.2021       | 06.12.2031        | +79831354947 | paprika@inbox.ru           |
|  32549572 | BUTYRSKAIA          | VASILISA        |                      | BUTYRSKAIA         | VASILISA       |                     | CHD         | Женский | 28.01.2017      |                 2 |             2 |               3 |                75 |           8261069 | 26.06.2018       | 26.06.2028        | +79226633130 | ooostroidom2012@mail.ru    |
|  32549571 | BUTYRSKAIA          | NATALIIA        |                      | BUTYRSKAIA         | NATALIIA       |                     | MRS         | Женский | 20.08.1984      |                 2 |             2 |               3 |                75 |           8261104 | 26.06.2018       | 26.06.2028        | +79226633130 | ooostroidom2012@mail.ru    |
|  32549569 | SHIRSHIN            | BOGDAN          |                      | SHIRSHIN           | BOGDAN         |                     | MR          | Мужской | 30.11.2012      |                 2 |             2 |               3 |                75 |           8977944 | 17.08.2018       | 17.08.2028        | +79823890339 | ooostroidom2012@mail.ru    |
|  32549568 | KHASANOVA           | LINARA          |                      | KHASANOVA          | LINARA         |                     | MRS         | Женский | 16.10.1983      |                 2 |             2 |               3 |                75 |           8471412 | 13.07.2018       | 13.07.2028        | +79823890339 | ooostroidom2012@mail.ru    |
|  32549563 | PAVLOVSKAIA         | MARGARITA       |                      | PAVLOVSKAIA        | MARGARITA      |                     | MRS         | Женский | 04.03.1992      |                 2 |             2 |               3 |                75 |           5453328 | 18.07.2017       | 18.07.2027        | +74997000304 | bron@onlinetours.travel    |
|  32549562 | MAKSIMOV            | MAKSIM          |                      | MAKSIMOV           | MAKSIM         |                     | MR          | Мужской | 07.07.1987      |                 2 |             2 |               3 |                77 |           1039488 | 05.08.2023       | 05.08.2033        | +74997000304 | bron@onlinetours.travel    |
|  32549560 | PAVLOV              | VLADISLAV       |                      | PAVLOV             | VLADISLAV      |                     | MR          | Мужской | 07.11.1992      |                 2 |             2 |               3 |                76 |           0236141 | 14.03.2019       | 14.03.2029        | +79014290853 | touroperators@travelata.ru |
|  32549559 | METELEVA            | OLGA            |                      | METELEVA           | OLGA           |                     | MRS         | Женский | 08.08.1991      |                 2 |             2 |               3 |                67 |           1724219 | 16.04.2025       | 16.04.2030        | +79014290853 | touroperators@travelata.ru |
|  32549558 | VALEEVA             | FARIDA          |                      | VALEEVA            | FARIDA         |                     | MRS         | Женский | 08.05.1960      |                 2 |             2 |               3 |                77 |           2368923 | 01.02.2024       | 01.02.2034        | +79625755599 | island-travel@list.ru      |
|  32549557 | VALEEV              | FAIZ            |                      | VALEEV             | FAIZ           |                     | MR          | Мужской | 13.09.1959      |                 2 |             2 |               3 |                77 |           2352786 | 31.01.2024       | 31.01.2034        | +79625755599 | island-travel@list.ru      |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 99.62% |
| Documents | 100.00% |
| Raw_metadata | 85.22% |



### Data sample
```
| names                  | birth_date   | documents                                                                                                                      | raw_metadata                                                                                     |
|:-----------------------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| ['Aituarova Meruyert'] | 07.07.1976   | [Row(type=0, serial='10407639', country='KZ', date_issue='26.11.2015', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77477186541", "ТурОператор_E-mail": "m2@1tk.kz"}']                  |
| ['Akhmedov Maksat']    | 22.05.1997   | [Row(type=0, serial='17027865', country='KZ', date_issue='03.07.2024', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77000956006", "ТурОператор_E-mail": "onlinebooking@kaztour.kz"}']   |
| ['Aliyev Adyl']        | 19.09.1987   | [Row(type=0, serial='12720225', country='KZ', date_issue='13.11.2019', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77718662464", "ТурОператор_E-mail": "zoya1610@mail.ru"}']           |
| ['Bulanina Mariya']    | 07.05.2014   | [Row(type=0, serial='09959918', country='KZ', date_issue='27.05.2015', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77017111151", "ТурОператор_E-mail": "servet_travel@mail.ru"}']      |
| ['Burkitbayev Aibar']  | 06.07.1967   | [Row(type=0, serial='15156137', country='KZ', date_issue='13.02.2023', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77776772202", "ТурОператор_E-mail": "yuliya.kim.kayar@gmail.com"}'] |
| ['Galymgerey Serzhan'] | 23.12.2012   | [Row(type=0, serial='14438928', country='KZ', date_issue='20.05.2022', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_E-mail": "raytravel.kg@gmail.com"}']                                             |
| ['Grechman Alena']     | 23.06.1971   | [Row(type=0, serial='14209436', country='KZ', date_issue='04.04.2022', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77000956006", "ТурОператор_E-mail": "onlinebooking@kaztour.kz"}']   |
| ['Gyaurov Farkhat']    | 21.12.1981   | [Row(type=0, serial='15659141', country='KZ', date_issue='07.07.2023', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77478118426", "ТурОператор_E-mail": "d2@poehalisnami.com"}']        |
| ['Huseynova Nigar']    | 04.06.1998   | [Row(type=0, serial='03056145', country='KZ', date_issue=None, date_expire=None, authority=None, authority_code=None)]         |                                                                                                  |
| ['Kadyrbayeva Urzhan'] | 16.02.1984   | [Row(type=0, serial='14703498', country='KZ', date_issue='11.08.2022', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77786707178", "ТурОператор_E-mail": "onlinebooking@kaztour.kz"}']   |
| ['Kauanova Amina']     | 16.11.2001   | [Row(type=0, serial='11529258', country='KZ', date_issue='20.11.2017', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77778059316", "ТурОператор_E-mail": "onlinebooking@kaztour.kz"}']   |
| ['Kazakova Nadezhda']  | 17.03.1999   | [Row(type=0, serial='13437834', country='KZ', date_issue='26.03.2021', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77752980862", "ТурОператор_E-mail": "zhanatravel@gmail.com"}']      |
| ['Kenchimbay Bagdat']  | 07.06.1994   | [Row(type=0, serial='16072390', country='KZ', date_issue='31.10.2023', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77075930003", "ТурОператор_E-mail": "onlinebooking@kaztour.kz"}']   |
| ['Khassenov Syrym']    | 09.12.1973   | [Row(type=0, serial='16818960', country='KZ', date_issue='25.06.2019', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_E-mail": "charter@charter-c.ru"}']                                               |
| ['Kopteva Lyubov']     | 10.05.1960   | [Row(type=0, serial='10488105', country='KZ', date_issue='01.02.2016', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_E-mail": "oazis.tour@bk.ru"}']                                                   |
| ['Lavrova Alla']       | 29.11.1988   | [Row(type=0, serial='12695227', country='KZ', date_issue='01.11.2019', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77026740097", "ТурОператор_E-mail": "zimaleto.kz.2013@mail.ru"}']   |
| ['Makulova Ainur']     | 29.09.1969   | [Row(type=0, serial='12079065', country='KZ', date_issue=None, date_expire=None, authority=None, authority_code=None)]         |                                                                                                  |
| ['Mansurov Abzal']     | 22.12.2018   | [Row(type=0, serial='14096205', country='KZ', date_issue='12.01.2022', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77011678677", "ТурОператор_E-mail": "tourism4@transavia.kz"}']      |
| ['Mels Guldana']       | 04.11.2002   | [Row(type=0, serial='17038134', country='KZ', date_issue='13.07.2019', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_E-mail": "charter@charter-c.ru"}']                                               |
| ['Mukhanova Malika']   | 13.03.2001   | [Row(type=0, serial='16367679', country='KZ', date_issue='20.12.2023', date_expire=None, authority=None, authority_code=None)] | ['{"ТурОператор_Мобильный": "77000956006", "ТурОператор_E-mail": "onlinebooking@kaztour.kz"}']   |
```