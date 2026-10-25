# Parsetron results

## About row data

> - Code name: index_0266
> - File path: /media/user/SAMSUNG/Databases/index_0266/raw/beeline_employers.csv
> - Total rows: 198518

### Schema
```
root
 |-- login: string (nullable = true)
 |-- city: string (nullable = true)
 |-- fio: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)

```

### Data sample
```
| login            | city      | fio                                | email                         | phone            |
|:-----------------|:----------|:-----------------------------------|:------------------------------|:-----------------|
| ShKurbangadzhiev | Астрахань | Курбангаджиев Шамиль Магомедович   | ShKurbangadzhiev@vimpelcom.ru | +7 961 056-28-83 |
| GBaybatirova     | Астрахань | Байбатирова Гульзамина Жумажановна | GBaybatirova@vimpelcom.ru     |                  |
| VATimofeev       | Астрахань | Тимофеев Владимир Андреевич        | VATimofeev@ast.beeline.ru     | +7 961 055-55-03 |
| SAsonov          | Астрахань | Асонов Сергей Николаевич           | SAsonov@ast.beeline.ru        |                  |
| RShafiev         | Астрахань | Шафиев Рубин Маратович             | RShafiev@ast.beeline.ru       |                  |
| AGGurbanova      | Астрахань | Гурбанова Аминат Гаджи кызы        | AGGurbanova@vimpelcom.ru      | +7 967 338-43-17 |
| EkMSokolova      | Астрахань | Соколова Екатерина Максимовна      | EkMSokolova@vimpelcom.ru      | +7 967 333-46-18 |
| VlaSeAndreev     | Астрахань | Андреев Владимир Сергеевич         | VlaSeAndreev@vimpelcom.ru     |                  |
| EKabysheva       | Астрахань | Кабышева Елена Михайловна          | EKabysheva@ast.beeline.ru     | +7 905 363-77-73 |
| TYulovskaya      | Астрахань | Юловская Тамара Владимировна       | TYulovskaya@vimpelcom.ru      | +7 967 825-00-58 |
| YuKitsenko       | Астрахань | Киценко Юрий Викторович            | YuKitsenko@vimpelcom.ru       |                  |
| INAndrianov      | Астрахань | Андрианов Илья Николаевич          | IAndrianov@ast.beeline.ru     | +7 906 457-07-07 |
| ALyubenko        | Астрахань | Любенко Алексей Александрович      | ALyubenko@vimpelcom.ru        | +7 988 175-80-94 |
| EGavrilin        | Астрахань | Гаврилин Евгений Павлович          | EGavrilin@vimpelcom.ru        | +7 909 373-00-55 |
| VMukhazhinova    | Астрахань | Мухажинова Валида Мажитовна        | VMukhazhinova@vimpelcom.ru    |                  |
| LNBespalova      | Астрахань | Беспалова Лариса Николаевна        | LNBespalova@ast.beeline.ru    | +7 960 856-70-03 |
| KKotlyarova      | Астрахань | Котлярова Ксения Николаевна        | KKotlyarova@ast.beeline.ru    |                  |
| BBezhanishvili   | Астрахань | Бежанишвили Бежан Александрович    | BBezhanishvili@vimpelcom.ru   | +7 937 822-20-07 |
| YuBocharnikova   | Астрахань | Бочарникова Юлия Петровна          | YuBocharnikova@vimpelcom.ru   |                  |
| DYalchigulov     | Астрахань | Ялчигулов Денис Зиннурович         | DYalchigulov@vimpelcom.ru     | +7 967 825-00-69 |
```


## About final data
> - Total rows: 197621

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Data sample
```
| names                                  | phones          | emails                            | address       |
|:---------------------------------------|:----------------|:----------------------------------|:--------------|
| ['Курбангаджиев Шамиль Магомедович']   | ['79610562883'] | ['shkurbangadzhiev@vimpelcom.ru'] | ['Астрахань'] |
| ['Байбатирова Гульзамина Жумажановна'] |                 | ['gbaybatirova@vimpelcom.ru']     | ['Астрахань'] |
| ['Тимофеев Владимир Андреевич']        | ['79610555503'] | ['vatimofeev@ast.beeline.ru']     | ['Астрахань'] |
| ['Асонов Сергей Николаевич']           |                 | ['sasonov@ast.beeline.ru']        | ['Астрахань'] |
| ['Шафиев Рубин Маратович']             |                 | ['rshafiev@ast.beeline.ru']       | ['Астрахань'] |
| ['Гурбанова Аминат Гаджи Кызы']        | ['79673384317'] | ['aggurbanova@vimpelcom.ru']      | ['Астрахань'] |
| ['Соколова Екатерина Максимовна']      | ['79673334618'] | ['ekmsokolova@vimpelcom.ru']      | ['Астрахань'] |
| ['Андреев Владимир Сергеевич']         |                 | ['vlaseandreev@vimpelcom.ru']     | ['Астрахань'] |
| ['Кабышева Елена Михайловна']          | ['79053637773'] | ['ekabysheva@ast.beeline.ru']     | ['Астрахань'] |
| ['Юловская Тамара Владимировна']       | ['79678250058'] | ['tyulovskaya@vimpelcom.ru']      | ['Астрахань'] |
| ['Киценко Юрий Викторович']            |                 | ['yukitsenko@vimpelcom.ru']       | ['Астрахань'] |
| ['Андрианов Илья Николаевич']          | ['79064570707'] | ['iandrianov@ast.beeline.ru']     | ['Астрахань'] |
| ['Любенко Алексей Александрович']      | ['79881758094'] | ['alyubenko@vimpelcom.ru']        | ['Астрахань'] |
| ['Гаврилин Евгений Павлович']          | ['79093730055'] | ['egavrilin@vimpelcom.ru']        | ['Астрахань'] |
| ['Мухажинова Валида Мажитовна']        |                 | ['vmukhazhinova@vimpelcom.ru']    | ['Астрахань'] |
| ['Беспалова Лариса Николаевна']        | ['79608567003'] | ['lnbespalova@ast.beeline.ru']    | ['Астрахань'] |
| ['Котлярова Ксения Николаевна']        |                 | ['kkotlyarova@ast.beeline.ru']    | ['Астрахань'] |
| ['Бежанишвили Бежан Александрович']    | ['79378222007'] | ['bbezhanishvili@vimpelcom.ru']   | ['Астрахань'] |
| ['Бочарникова Юлия Петровна']          |                 | ['yubocharnikova@vimpelcom.ru']   | ['Астрахань'] |
| ['Ялчигулов Денис Зиннурович']         | ['79678250069'] | ['dyalchigulov@vimpelcom.ru']     | ['Астрахань'] |
```