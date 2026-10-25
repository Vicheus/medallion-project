# Parsetron results

## About row data

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Москва_3.7M/Водители_8.9к.csv
> - Total rows: 8901

### Schema
```
root
 |-- id: string (nullable = true)
 |-- name: string (nullable = true)
 |-- family: string (nullable = true)
 |-- sec_fam: string (nullable = true)
 |-- phone: long (nullable = true)
 |-- delet: integer (nullable = true)
 |-- factory_id: integer (nullable = true)
 |-- shift: integer (nullable = true)
 |-- transport_type: integer (nullable = true)
 |-- allowed_to_get_gsm_task: integer (nullable = true)
 |-- transport: integer (nullable = true)
 |-- master_id: string (nullable = true)

```

### Data sample
```
|   id | name     | family    | sec_fam       |       phone |   delet |   factory_id |   shift |   transport_type |   allowed_to_get_gsm_task |   transport | master_id   |
|-----:|:---------|:----------|:--------------|------------:|--------:|-------------:|--------:|-----------------:|--------------------------:|------------:|:------------|
|    2 | Иван     | Иванов    |               | 79111111111 |       1 |            2 |       1 |                1 |                         0 |           1 |             |
|    3 | Анатолий | Павлов    | Александрович | 79851548064 |       1 |            3 |       1 |                1 |                         0 |           1 |             |
|    4 | Сергей   | Луговин   | Александрович | 79252767939 |       1 |            2 |       1 |                1 |                         0 |           1 |             |
|    5 | Юрий     | Рощункин  |               | 79778090089 |       1 |            2 |       1 |                1 |                         0 |           1 |             |
|    6 | Владимир | Волошин   |               | 79057471018 |       1 |            3 |       1 |                1 |                         0 |           1 |             |
|    7 | Николай  | Сазонов   | Андреевич     | 79264085703 |       1 |            6 |       1 |                1 |                         0 |           1 |             |
|    8 | Юля      | Баннова   |               | 79254958757 |       1 |            3 |       1 |                1 |                         0 |           1 |             |
|    9 | Андрей   | Петров    | Валерьевич    | 79117337170 |       1 |            3 |       1 |                1 |                         0 |           1 |             |
|   10 | Дмитрий  | Мельников | Валерьевич    | 79164339554 |       1 |            3 |       1 |                1 |                         0 |           1 |             |
|   11 | Анатолий | Грибков   | Игоревич      | 79105766069 |       1 |            3 |       1 |                1 |                         0 |           1 |             |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Санкт-Петербург_22.4М/Водители2_26к.csv
> - Total rows: 26023

### Schema
```
root
 |-- id: string (nullable = true)
 |-- name: string (nullable = true)
 |-- family: string (nullable = true)
 |-- sec_fam: string (nullable = true)
 |-- phone: long (nullable = true)
 |-- delet: integer (nullable = true)
 |-- factory_id: integer (nullable = true)
 |-- shift: integer (nullable = true)
 |-- transport_type: integer (nullable = true)
 |-- allowed_to_get_gsm_task: integer (nullable = true)
 |-- transport: integer (nullable = true)
 |-- master_id: string (nullable = true)

```

### Data sample
```
|   id | name       | family    | sec_fam   |       phone |   delet |   factory_id |   shift |   transport_type |   allowed_to_get_gsm_task |   transport | master_id   |
|-----:|:-----------|:----------|:----------|------------:|--------:|-------------:|--------:|-----------------:|--------------------------:|------------:|:------------|
|    1 | Антон      | Макиенко  |           | 79215739212 |       1 |            1 |       0 |                0 |                         0 |           1 |             |
|    2 | Сергей     | Глазков   |           | 79214435224 |       1 |            1 |       0 |                0 |                         0 |           1 |             |
|    3 | Азис       | Умаров    |           | 79117295747 |       1 |            1 |       0 |                0 |                         0 |           1 |             |
|    4 | Николай    | Строганов |           | 79215699115 |       1 |            1 |       0 |                0 |                         0 |           1 |             |
|    5 | Константин | Сединикин |           | 79500109344 |       1 |            1 |       0 |                0 |                         0 |           1 |             |
|    6 | Эдуард     | Исмаилов  |           | 79500033323 |       1 |            1 |       0 |                0 |                         0 |           1 |             |
|    7 | Алик       | Хакимов   |           | 79523874215 |       1 |            1 |       0 |                0 |                         0 |           1 |             |
|    8 | Эдуард     | Гараев    |           | 79526662642 |       1 |            1 |       0 |                0 |                         0 |           1 |             |
|    9 | Алексей    | Потемкин  |           | 89110100137 |       1 |            1 |       0 |                0 |                         0 |           1 |             |
|   10 | Асхат      | Аппаков   |           | 79523884411 |       1 |            1 |       0 |                0 |                         0 |           1 |             |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Санкт-Петербург_22.4М/Водители_39.9к.csv
> - Total rows: 39969

### Schema
```
root
 |-- full_name: string (nullable = true)
 |-- master_id: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- phone_conveted: long (nullable = true)

```

### Data sample
```
| full_name                        | master_id                            |       phone |   phone_conveted |
|:---------------------------------|:-------------------------------------|------------:|-----------------:|
| Мусин Дмитрий Валерьевич         | 0dd6eaca-766f-11e5-83ea-3085a91123a0 | 79110011911 |      79110011911 |
| Петрашевский Владимир Георгиевич | 17216afc-8ae2-11e6-85eb-3085a91123a0 | 79119539192 |      79119539192 |
| Сосняков Алексей Игоревич        | 3455d390-8aa0-11e8-9491-00155d61c801 | 79111707055 |      79111707055 |
| Силонов Сергей Сергеевич         | f3d9e4e0-8aa2-11e8-9491-00155d61c801 | 79967640552 |      79967640552 |
| Стариков Кирилл Александрович    | f8904f01-8aa3-11e8-9491-00155d61c801 | 79006464150 |      79006464150 |
| Чайка Петр Геннадьевич           | b5a3292a-8aa4-11e8-9491-00155d61c801 | 79500458170 |      79500458170 |
| Кузнецов Никита Сергеевич        | 9bf72e7d-8b35-11e8-9491-00155d61c801 | 79112304213 |      79112304213 |
| Матюхин Александр Александрович  | c028f73e-8b61-11e8-9492-00155d61c801 | 79111136693 |      79111136693 |
| Грицай Александра Анатольевна    | 4c0fe85f-8bec-11e8-9492-00155d61c801 | 79213058082 |      79213058082 |
| Иогансон Никита Борисович        | 4bc9ac4a-8bf0-11e8-9492-00155d61c801 | 79818108662 |      79818108662 |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Сочи_1.1М/Водители_770.csv
> - Total rows: 768

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- family: string (nullable = true)
 |-- sec_fam: string (nullable = true)
 |-- phone: long (nullable = true)
 |-- delet: integer (nullable = true)
 |-- factory_id: integer (nullable = true)
 |-- shift: integer (nullable = true)
 |-- transport_type: integer (nullable = true)
 |-- allowed_to_get_gsm_task: integer (nullable = true)
 |-- transport: integer (nullable = true)
 |-- master_id: string (nullable = true)

```

### Data sample
```
|    id | name      | family     | sec_fam      |       phone |   delet |   factory_id |   shift |   transport_type |   allowed_to_get_gsm_task |   transport | master_id                            |
|------:|:----------|:-----------|:-------------|------------:|--------:|-------------:|--------:|-----------------:|--------------------------:|------------:|:-------------------------------------|
| 11780 | Тест      | Тест       | Тест         | 79046309745 |       1 |         3000 |       1 |                1 |                         1 |           1 |                                      |
| 11781 | Виталий   | Багалей    | Владимирович | 79676442610 |       1 |         3000 |       1 |                1 |                         0 |           1 | 98F74F43-3DF6-11EB-AE33-001DD8B71D36 |
| 11782 | Ксения    | Садилова   | Дмитриевна   | 79323329091 |       1 |         3000 |       1 |                1 |                         0 |           0 | 98F74F41-3DF6-11EB-AE33-001DD8B71D36 |
| 11783 | Игорь     | Шургая     | Бадриевич    | 79181062520 |       1 |         3000 |       1 |                1 |                         0 |           1 | 92F7E804-3DF6-11EB-AE33-001DD8B71D36 |
| 11784 | Евгений   | Папиян     | Алексеевич   | 79528237303 |       1 |         3000 |       1 |                1 |                         0 |           1 | 98F74F3F-3DF6-11EB-AE33-001DD8B71D36 |
| 11785 | Альберт   | Узунян     | Яковлевич    | 79183070590 |       1 |         3000 |       1 |                1 |                         0 |           1 | 98F74F35-3DF6-11EB-AE33-001DD8B71D36 |
| 11786 | Ашот      | Чамян      | Арутович     | 79186020999 |       1 |         3000 |       1 |                1 |                         0 |           1 | 92F7E7FE-3DF6-11EB-AE33-001DD8B71D36 |
| 11787 | Владислав | Мигут      | Генадьевич   | 79825469013 |       1 |         3000 |       1 |                1 |                         0 |           1 | 35CA5579-3DF5-11EB-AE33-001DD8B71D36 |
| 11788 | Павел     | Тарасов    | Анатольевич  | 79654655414 |       1 |         3000 |       1 |                1 |                         0 |           1 | 98F74F37-3DF6-11EB-AE33-001DD8B71D36 |
| 11789 | Диана     | Григорьева | Сергеевна    | 79531122352 |       1 |         3000 |       1 |                1 |                         0 |           0 | 8C814B2E-3DF6-11EB-AE33-001DD8B71D36 |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Москва_3.7M/Пользователи_2.4к.csv
> - Total rows: 2481

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- family: string (nullable = true)
 |-- role: integer (nullable = true)
 |-- phone: string (nullable = true)
 |-- note: string (nullable = true)
 |-- password: string (nullable = true)
 |-- deleted: integer (nullable = true)

```

### Data sample
```
|   id | name           | family                      |   role | phone   | note   | password                         |   deleted |
|-----:|:---------------|:----------------------------|-------:|:--------|:-------|:---------------------------------|----------:|
|    1 | robot          | робот                       |      0 |         |        | 8a8ab7d990f30e2d4c46a6e96f4754db |         1 |
|    2 | market         | Доста маркет                |      0 |         |        | 8a8ab7d990f30e2d4c46a6e96f4754db |         1 |
|    3 | artem          | Плотницкий Артем            |      1 |         |        | 827ccb0eea8a706c4c34a16891f84e7b |         1 |
|    4 | mikheev        | Михеев Никита Владиславович |     32 |         |        | bc1a1b4e566a7d1010bca363faea973c |         0 |
|    6 | vowa           | Влaдимир                    |     49 |         |        | 86393c627d04c72d2bbe3ae609539068 |         1 |
|   26 | zaharov        | Захаров Андрей Павлович     |     49 |         |        | 3d91e9bba626067c78a2a007256f4e0d |         0 |
|   29 | obzvon         | Обзвон                      |      1 |         |        | 54321                            |         1 |
|   38 | gosha          | Поляков Георгий Алексеевич  |     49 |         |        | e168c08b6e8baf76b57f800b3449e3fc |         0 |
|   70 | Зубарева Тина  | Зубарева Тина Вячеславовна  |     49 |         |        | e34ed8c0a62603b53fac588a00fc0c20 |         0 |
|   75 | Юрьева Татьяна | Юрьева Татьяна              |      0 |         |        | 21218cca77804d2ba1922c33e0151105 |         1 |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Санкт-Петербург_22.4М/Пользователи_2к.csv
> - Total rows: 3251

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- family: string (nullable = true)
 |-- role: integer (nullable = true)
 |-- phone: string (nullable = true)
 |-- note: string (nullable = true)
 |-- password: string (nullable = true)
 |-- deleted: integer (nullable = true)

```

### Data sample
```
|   id | name           | family                      |   role | phone   | note   | password                         |   deleted |
|-----:|:---------------|:----------------------------|-------:|:--------|:-------|:---------------------------------|----------:|
|    1 | robot          | робот                       |      0 |         |        | 8a8ab7d990f30e2d4c46a6e96f4754db |         1 |
|    2 | market         | Доста маркет                |      0 |         |        | 8a8ab7d990f30e2d4c46a6e96f4754db |         1 |
|    3 | artem          | Плотницкий Артем            |      1 |         |        | 827ccb0eea8a706c4c34a16891f84e7b |         1 |
|    4 | mikheev        | Михеев Никита Владиславович |     67 |         |        | bc1a1b4e566a7d1010bca363faea973c |         0 |
|    6 | vowa           | Влaдимир                    |     56 |         |        | 86393c627d04c72d2bbe3ae609539068 |         1 |
|   26 | zaharov        | Захаров Андрей Павлович     |     56 |         |        | 3d91e9bba626067c78a2a007256f4e0d |         0 |
|   29 | obzvon         | Обзвон                      |      1 |         |        | 54321                            |         1 |
|   38 | gosha          | Поляков Георгий Алексеевич  |     56 |         |        | e168c08b6e8baf76b57f800b3449e3fc |         0 |
|   70 | зубарева       | Зубарева Тина               |      5 |         |        | fcea920f7412b5da7be0cf42b8c93759 |         1 |
|   75 | Юрьева Татьяна | Юрьева Татьяна              |      0 |         |        | 21218cca77804d2ba1922c33e0151105 |         1 |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Сочи_1.1М/Пользователи_1.8к.csv
> - Total rows: 1868

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- name: string (nullable = true)
 |-- family: string (nullable = true)
 |-- role: integer (nullable = true)
 |-- phone: string (nullable = true)
 |-- note: string (nullable = true)
 |-- password: string (nullable = true)
 |-- deleted: integer (nullable = true)

```

### Data sample
```
|   id | name           | family                      |   role | phone   | note   | password                         |   deleted |
|-----:|:---------------|:----------------------------|-------:|:--------|:-------|:---------------------------------|----------:|
|    1 | robot          | робот                       |      0 |         |        | 8a8ab7d990f30e2d4c46a6e96f4754db |         1 |
|    2 | market         | Доста маркет                |      0 |         |        | 8a8ab7d990f30e2d4c46a6e96f4754db |         1 |
|    3 | artem          | Плотницкий Артем            |      1 |         |        | 827ccb0eea8a706c4c34a16891f84e7b |         1 |
|    4 | mikheev        | Михеев Никита Владиславович |     32 |         |        | bc1a1b4e566a7d1010bca363faea973c |         0 |
|    6 | vowa           | Влaдимир                    |     49 |         |        | 86393c627d04c72d2bbe3ae609539068 |         1 |
|   26 | zaharov        | Захаров Андрей Павлович     |     49 |         |        | 3d91e9bba626067c78a2a007256f4e0d |         0 |
|   29 | obzvon         | Обзвон                      |      1 |         |        | 54321                            |         1 |
|   38 | gosha          | Поляков Георгий Алексеевич  |     49 |         |        | e168c08b6e8baf76b57f800b3449e3fc |         0 |
|   70 | Зубарева Тина  | Зубарева Тина Вячеславовна  |     49 |         |        | e34ed8c0a62603b53fac588a00fc0c20 |         0 |
|   75 | Юрьева Татьяна | Юрьева Татьяна              |      0 |         |        | 21218cca77804d2ba1922c33e0151105 |         1 |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Москва_3.7M/Адрес_клиентов_9.3к.csv
> - Total rows: 9393

### Schema
```
root
 |-- id: string (nullable = true)
 |-- id_client: string (nullable = true)
 |-- street: string (nullable = true)
 |-- building: string (nullable = true)
 |-- housing: string (nullable = true)
 |-- flat: string (nullable = true)
 |-- parade: string (nullable = true)
 |-- floor: string (nullable = true)
 |-- intercomcode: string (nullable = true)
 |-- adress_note: string (nullable = true)
 |-- adress_name: string (nullable = true)
 |-- adress_type: string (nullable = true)
 |-- housing_type: string (nullable = true)
 |-- longitude: integer (nullable = true)
 |-- latitude: string (nullable = true)

```

### Data sample
```
|   id |   id_client | street              | building   | housing   |   flat |   parade |   floor | intercomcode   | adress_note                             | adress_name    |   adress_type | housing_type   |   longitude | latitude   |
|-----:|------------:|:--------------------|:-----------|:----------|-------:|---------:|--------:|:---------------|:----------------------------------------|:---------------|--------------:|:---------------|------------:|:-----------|
|    2 |         154 | Коммуны             | 44         | 1         |     71 |        2 |       7 | 71             |                                         | Дом            |             0 |                |         nan |            |
|    3 |         170 | Подводника Кузьмина | 16         |           |     34 |        4 |       4 |                |                                         |                |             1 |                |         nan |            |
|    4 |         115 | Белышева            | 5/6        |           |   2408 |       21 |      19 | 2408           |                                         | Белышева       |             0 |                |         nan |            |
|    5 |         186 | Новороссийская      | 25         | 1         |    254 |        4 |       5 | 230в           |                                         | Новороссийская |             0 |                |         nan |            |
|    6 |         265 | Мми                 | иии        | иит       |        |          |         |                | Пми                                     | Мм             |             0 |                |         nan |            |
|    7 |         147 | тихомировп          | 12         | 1         |     20 |        1 |       6 | 20             |                                         | тихомировп     |             0 |                |         nan |            |
|    8 |         493 | Мии                 | итт        |           |        |          |         |                |                                         | Мии            |             0 |                |         nan |            |
|    9 |         416 | Шипиловская         | 62/1       |           |    169 |        4 |       7 | 169            |                                         | Домулечка      |             0 |                |         nan |            |
|   26 |         344 | Борисовка           | 20а        |           |    622 |        8 |       9 | 622            |                                         | Борисовка      |             0 |                |         nan |            |
|   27 |         763 | Зарайская           | 47         | 1         |     17 |        1 |       3 | 13к0303        | Звонка в дверь нет, звонить по телефону | Дом            |             0 |                |         nan |            |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Москва_3.7M/Заказы_3.2M.csv
> - Total rows: 3851399

### Schema
```
root
 |-- id: string (nullable = true)
 |-- id_client: string (nullable = true)
 |-- id_user_in: string (nullable = true)
 |-- id_user_out: string (nullable = true)
 |-- driver: string (nullable = true)
 |-- status: string (nullable = true)
 |-- adress: string (nullable = true)
 |-- note_adress: string (nullable = true)
 |-- sum: string (nullable = true)
 |-- sdacha: string (nullable = true)
 |-- count_person: string (nullable = true)
 |-- skidka: string (nullable = true)
 |-- dat_add: string (nullable = true)
 |-- dat: string (nullable = true)
 |-- time_: string (nullable = true)
 |-- subitems: string (nullable = true)
 |-- factory: string (nullable = true)
 |-- ingridients: string (nullable = true)
 |-- actions: string (nullable = true)
 |-- delivery: string (nullable = true)
 |-- pay: string (nullable = true)
 |-- enter: string (nullable = true)
 |-- website: string (nullable = true)
 |-- advertisement_id: string (nullable = true)
 |-- corporate_group_id: string (nullable = true)
 |-- callback: string (nullable = true)
 |-- origin: string (nullable = true)
 |-- house_number: string (nullable = true)
 |-- building_number: string (nullable = true)
 |-- appartment_number: string (nullable = true)
 |-- appartment_type: string (nullable = true)
 |-- street: string (nullable = true)
 |-- intercom: string (nullable = true)
 |-- entrance: string (nullable = true)
 |-- longitude: string (nullable = true)
 |-- latitude: string (nullable = true)
 |-- building_type: string (nullable = true)
 |-- floor: string (nullable = true)
 |-- ts: string (nullable = true)
 |-- db_status: string (nullable = true)
 |-- sync_status: string (nullable = true)
 |-- preorder: string (nullable = true)
 |-- RV: string (nullable = true)
 |-- delivery_date: string (nullable = true)
 |-- spread_date: string (nullable = true)
 |-- autoProcess: string (nullable = true)
 |-- autoDone: string (nullable = true)
 |-- trayProcess: string (nullable = true)
 |-- origin_version: string (nullable = true)
 |-- IsPaidDeliveryPolygon: string (nullable = true)
 |-- IsInvoicePrinted: string (nullable = true)
 |-- IsProcessedByRoutingOnFront: string (nullable = true)
 |-- cells: string (nullable = true)
 |-- OnlineCheck: string (nullable = true)
 |-- PromoCode: string (nullable = true)
 |-- FacadeFactoryId: string (nullable = true)
 |-- IsSubstituteManufactory: string (nullable = true)
 |-- IsOnlineCheckPrinted: string (nullable = true)
 |-- FacadeOrderId: string (nullable = true)
 |-- FacadeUserId: string (nullable = true)
 |-- ExcludeCutlery: string (nullable = true)
 |-- ExcludeVIS: string (nullable = true)
 |-- RegionId: string (nullable = true)
 |-- PaymentToolId: string (nullable = true)
 |-- version: string (nullable = true)
 |-- order_system_id: string (nullable = true)
 |-- IsSbpPayment: string (nullable = true)
 |-- PaymentRequestCode: string (nullable = true)
 |-- dat_add_utc: string (nullable = true)
 |-- delivery_date_utc: string (nullable = true)

```

### Data sample
```
| id               | id_client                                    |   id_user_in |   id_user_out |   driver | status                  | adress                                                                 | note_adress                                  | sum          | sdacha             |   count_person |   skidka | dat_add                 | dat        |   time_ | subitems                         |   factory | ingridients      |   actions | delivery   | pay          |   enter |   website |   advertisement_id | corporate_group_id   |   callback | origin   | house_number   | building_number   | appartment_number   | appartment_type   | street   | intercom   | entrance   | longitude   | latitude   | building_type           | floor                   |   ts |   db_status |   sync_status | preorder   | RV   | delivery_date           | spread_date   |   autoProcess |   autoDone |   trayProcess | origin_version   |   IsPaidDeliveryPolygon |   IsInvoicePrinted |   IsProcessedByRoutingOnFront | cells   |   OnlineCheck |   PromoCode | FacadeFactoryId                      | IsSubstituteManufactory              |   IsOnlineCheckPrinted | FacadeOrderId                        | FacadeUserId                         |   ExcludeCutlery | ExcludeVIS              | RegionId                             | PaymentToolId           |   version | order_system_id                      |   IsSbpPayment | PaymentRequestCode   | dat_add_utc             | delivery_date_utc       |
|:-----------------|:---------------------------------------------|-------------:|--------------:|---------:|:------------------------|:-----------------------------------------------------------------------|:---------------------------------------------|:-------------|:-------------------|---------------:|---------:|:------------------------|:-----------|--------:|:---------------------------------|----------:|:-----------------|----------:|:-----------|:-------------|--------:|----------:|-------------------:|:---------------------|-----------:|:---------|:---------------|:------------------|:--------------------|:------------------|:---------|:-----------|:-----------|:------------|:-----------|:------------------------|:------------------------|-----:|------------:|--------------:|:-----------|:-----|:------------------------|:--------------|--------------:|-----------:|--------------:|:-----------------|------------------------:|-------------------:|------------------------------:|:--------|--------------:|------------:|:-------------------------------------|:-------------------------------------|-----------------------:|:-------------------------------------|:-------------------------------------|-----------------:|:------------------------|:-------------------------------------|:------------------------|----------:|:-------------------------------------|---------------:|:---------------------|:------------------------|:------------------------|
| 17               | 8                                            |          534 |             0 |        0 | 5                       | Москва, Ясный проезд, 34к1 кв 12                                       |                                              |              |                    |                |          |                         |            |         |                                  |           |                  |           |            |              |         |           |                    |                      |            |          |                |                   |                     |                   |          |            |            |             |            |                         |                         |      |             |               |            |      |                         |               |               |            |               |                  |                         |                    |                               |         |               |             |                                      |                                      |                        |                                      |                                      |                  |                         |                                      |                         |           |                                      |                |                      |                         |                         |
| Метро: Бибирево" | Отзвон - встретят.                           |          547 |             0 |        0 | 0.0                     | 2017-03-23 14:18:14.475                                                | 2017-03-23                                   | 1518         | 1297=1,399=1       |              2 |          |                         | 0          |       0 | 0                                |         1 | 0                |           | 1          | Phone        |         |           |                    |                      |            |          |                |                   |                     |                   |          |            |            |             |            | ���                    | 2017-03-23 15:18:00.000 |      |           0 |             0 |            |      |                         |               |               |            |             0 |                  |                         |                  0 |                             1 |         |               |           0 | 0                                    | FFC3B528-2D1E-441D-9E66-3BA147804370 |                        | 312905696                            | 4C746DE0-6EE4-4E81-A86B-9052EAE777DD |                0 |                         | 2017-03-23 11:18:14.475              | 2017-03-23 12:18:00.000 |           |                                      |                |                      |                         |                         |
| 18               | 9                                            |          124 |             0 |        0 | 6                       | тест                                                                   | Причина отказа: тест                         | 39           | 0                  |              0 |        0 | 2017-03-23 14:43:15.791 | 2017-03-23 |    1541 | 865=1                            |         3 |                  |           | 0          | 0            |       0 |         1 |                  0 |                      |          1 | Phone    |                |                   |                     |                   |          |            |            |             |            |                         |                         |      |             |               |            | ��� | 2017-03-23 15:41:00.000 |               |             0 |          0 |               |                  |                         |                    |                               |         |             0 |             |                                      | 0                                    |                      1 |                                      |                                      |                0 | 0                       | FFC3B528-2D1E-441D-9E66-3BA147804370 |                         | 312905697 | 5C676E00-FB11-45E4-A4B7-69777D1F5F1A |              0 |                      | 2017-03-23 11:43:15.791 | 2017-03-23 12:41:00.000 |
| 19               | 10                                           |          627 |             0 |        0 | 6                       | ул. FGHFGH, д. xfgfdf                                                  | Причина отказа: Клиент не отвечал на звонки. | 2418         | 0                  |              0 |        0 | 2017-03-23 15:57:28.000 | 2017-03-23 |    2000 | 1053=1,145=1,1182=1,1297=1,399=2 |         3 | 5;1182;22=2:23=2 |           | 0          | 0            |       1 |         1 |                  0 |                      |          1 | Android  |                |                   |                     |                   |          |            |            |             |            |                         |                         |      |             |               |            | ��� | 2017-03-23 20:00:00.000 |               |             0 |          0 |               |                  |                         |                    |                               |         |             0 |             |                                      | 0                                    |                      1 |                                      |                                      |                0 | 0                       | FFC3B528-2D1E-441D-9E66-3BA147804370 |                         | 312905698 | ED19A41C-AA16-4120-B08E-3D9BA0482F67 |              0 |                      | 2017-03-23 12:57:28.000 | 2017-03-23 17:00:00.000 |
| 20               | 8                                            |          498 |             0 |        0 | 6                       | Москва, Ясный проезд, 34к1 кв 12                                       |                                              |              |                    |                |          |                         |            |         |                                  |           |                  |           |            |              |         |           |                    |                      |            |          |                |                   |                     |                   |          |            |            |             |            |                         |                         |      |             |               |            |      |                         |               |               |            |               |                  |                         |                    |                               |         |               |             |                                      |                                      |                        |                                      |                                      |                  |                         |                                      |                         |           |                                      |                |                      |                         |                         |
| Метро: Бибирево" | Причина отказа: Клиент не отвечал на звонки. |          436 |             0 |        0 | 0.0                     | 2017-03-23 16:37:32.024                                                | 2017-03-23                                   | 1735         | 1309=1,675=1       |              2 |          |                         | 0          |       0 | 2                                |         1 | 0                |           | 1          | DeliveryClub |         |           |                    |                      |            |          |                |                   |                     |                   |          |            |            |             |            | ���                    | 2017-03-23 17:35:00.000 |      |           0 |             0 |            |      |                         |               |               |            |             0 |                  |                         |                  0 |                             1 |         |               |           0 | 0                                    | FFC3B528-2D1E-441D-9E66-3BA147804370 |                        | 312905699                            | 17904D5B-A4AA-454D-9B19-92302AC24A9E |                0 |                         | 2017-03-23 13:37:32.024              | 2017-03-23 14:35:00.000 |           |                                      |                |                      |                         |                         |
| 21               | 11                                           |          498 |             0 |        0 | 5                       | Ясный проезд, 26 к1                                                    |                                              |              |                    |                |          |                         |            |         |                                  |           |                  |           |            |              |         |           |                    |                      |            |          |                |                   |                     |                   |          |            |            |             |            |                         |                         |      |             |               |            |      |                         |               |               |            |               |                  |                         |                    |                               |         |               |             |                                      |                                      |                        |                                      |                                      |                  |                         |                                      |                         |           |                                      |                |                      |                         |                         |
| Метро: Бибирево" | Причина отказа: Передумал.                   |          725 |             0 |        0 | 0.0                     | 2017-03-23 16:43:21.236                                                | 2017-03-23                                   | 1741         | 226=1,1155=1,620=1 |              2 |          |                         | 0          |       0 | 2                                |         1 | 0                |           | 1          | DeliveryClub |         |           |                    |                      |            |          |                |                   |                     |                   |          |            |            |             |            | ���                    | 2017-03-23 17:41:00.000 |      |           0 |             0 |            |      |                         |               |               |            |             0 |                  |                         |                  0 |                             1 |         |               |           0 | 0                                    | FFC3B528-2D1E-441D-9E66-3BA147804370 |                        | 312905700                            | 07692B4A-447E-43D8-B9A6-4E135769781A |                0 |                         | 2017-03-23 13:43:21.236              | 2017-03-23 14:41:00.000 |           |                                      |                |                      |                         |                         |
| 22               | 12                                           |          627 |             0 |        3 | 5                       | б-р Волжский, Москва, Дом: 13, Парадная: 12, Домофон: , Эт: 3, Кв: 445 | м.Текстильщики                               |              |                    |                |          |                         |            |         |                                  |           |                  |           |            |              |         |           |                    |                      |            |          |                |                   |                     |                   |          |            |            |             |            |                         |                         |      |             |               |            |      |                         |               |               |            |               |                  |                         |                    |                               |         |               |             |                                      |                                      |                        |                                      |                                      |                  |                         |                                      |                         |           |                                      |                |                      |                         |                         |
| Сайт:"           | 497                                          |            0 |             0 |        0 | 2017-03-23 20:24:36.000 | 2017-03-23                                                             | 2129                                         | 1289=1,399=1 | 3                  |                |          | 0                       | 0          |       1 | 1                                |         0 |                  |         0 | Website    |              |         |           |                    |                      |            |          |                |                   |                     |                   |          |            |            |             | ���       | 2017-03-23 21:29:00.000 |                         |    0 |           0 |               |            |      |                         |               |               |          0 |               |                  |                       0 |                  1 |                               |         |             0 |           0 | FFC3B528-2D1E-441D-9E66-3BA147804370 |                                      |              312905701 | DF9F0607-70E0-4EC0-BBD1-B1D3B03AB262 | 0                                    |                  | 2017-03-23 17:24:36.000 | 2017-03-23 18:29:00.000              |                         |           |                                      |                |                      |                         |                         |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Санкт-Петербург_22.4М/Заказы_19.9М.csv
> - Total rows: 19947555

### Schema
```
root
 |-- id: string (nullable = true)
 |-- id_client: string (nullable = true)
 |-- id_user_in: string (nullable = true)
 |-- id_user_out: string (nullable = true)
 |-- driver: string (nullable = true)
 |-- status: string (nullable = true)
 |-- adress: string (nullable = true)
 |-- note_adress: string (nullable = true)
 |-- sum: string (nullable = true)
 |-- sdacha: string (nullable = true)
 |-- count_person: string (nullable = true)
 |-- skidka: string (nullable = true)
 |-- dat_add: string (nullable = true)
 |-- dat: string (nullable = true)
 |-- time_: string (nullable = true)
 |-- subitems: string (nullable = true)
 |-- factory: string (nullable = true)
 |-- ingridients: string (nullable = true)
 |-- actions: string (nullable = true)
 |-- delivery: string (nullable = true)
 |-- pay: string (nullable = true)
 |-- enter: string (nullable = true)
 |-- website: string (nullable = true)
 |-- advertisement_id: string (nullable = true)
 |-- corporate_group_id: string (nullable = true)
 |-- callback: string (nullable = true)
 |-- origin: string (nullable = true)
 |-- house_number: string (nullable = true)
 |-- building_number: string (nullable = true)
 |-- appartment_number: string (nullable = true)
 |-- appartment_type: string (nullable = true)
 |-- street: string (nullable = true)
 |-- intercom: string (nullable = true)
 |-- entrance: string (nullable = true)
 |-- longitude: string (nullable = true)
 |-- latitude: string (nullable = true)
 |-- building_type: string (nullable = true)
 |-- floor: string (nullable = true)
 |-- ts: string (nullable = true)
 |-- db_status: string (nullable = true)
 |-- sync_status: string (nullable = true)
 |-- preorder: string (nullable = true)
 |-- delivery_date: string (nullable = true)
 |-- RV: string (nullable = true)
 |-- spread_date: string (nullable = true)
 |-- autoProcess: string (nullable = true)
 |-- autoDone: string (nullable = true)
 |-- trayProcess: string (nullable = true)
 |-- origin_version: string (nullable = true)
 |-- IsPaidDeliveryPolygon: string (nullable = true)
 |-- IsInvoicePrinted: string (nullable = true)
 |-- IsProcessedByRoutingOnFront: string (nullable = true)
 |-- cells: string (nullable = true)
 |-- OnlineCheck: string (nullable = true)
 |-- PromoCode: string (nullable = true)
 |-- FacadeFactoryId: string (nullable = true)
 |-- IsSubstituteManufactory: string (nullable = true)
 |-- IsOnlineCheckPrinted: string (nullable = true)
 |-- FacadeOrderId: string (nullable = true)
 |-- FacadeUserId: string (nullable = true)
 |-- ExcludeCutlery: string (nullable = true)
 |-- ExcludeVIS: string (nullable = true)
 |-- RegionId: string (nullable = true)
 |-- PaymentToolId: string (nullable = true)
 |-- version: string (nullable = true)
 |-- order_system_id: string (nullable = true)
 |-- IsSbpPayment: string (nullable = true)
 |-- PaymentRequestCode: string (nullable = true)
 |-- dat_add_utc: string (nullable = true)
 |-- delivery_date_utc: string (nullable = true)

```

### Data sample
```
| id                   |   id_client |   id_user_in |   id_user_out |   driver | status                  | adress                                             | note_adress                                           | sum         |   sdacha |   count_person |   skidka | dat_add                 | dat        |   time_ | subitems                              |   factory | ingridients   | actions                           | delivery   |   pay |   enter |   website |   advertisement_id | corporate_group_id   |   callback | origin   | house_number   | building_number   | appartment_number   | appartment_type   | street                  | intercom   | entrance   | longitude   | latitude                | building_type   | floor   | ts                      |   db_status |   sync_status | preorder   | delivery_date           | RV       | spread_date   |   autoProcess |   autoDone | trayProcess   | origin_version   |   IsPaidDeliveryPolygon |   IsInvoicePrinted | IsProcessedByRoutingOnFront   | cells   |   OnlineCheck |   PromoCode | FacadeFactoryId                      |   IsSubstituteManufactory |   IsOnlineCheckPrinted | FacadeOrderId                        |   FacadeUserId |   ExcludeCutlery | ExcludeVIS              | RegionId                             | PaymentToolId   |    version | order_system_id                      |   IsSbpPayment | PaymentRequestCode   | dat_add_utc             | delivery_date_utc       |
|:---------------------|------------:|-------------:|--------------:|---------:|:------------------------|:---------------------------------------------------|:------------------------------------------------------|:------------|---------:|---------------:|---------:|:------------------------|:-----------|--------:|:--------------------------------------|----------:|:--------------|:----------------------------------|:-----------|------:|--------:|----------:|-------------------:|:---------------------|-----------:|:---------|:---------------|:------------------|:--------------------|:------------------|:------------------------|:-----------|:-----------|:------------|:------------------------|:----------------|:--------|:------------------------|------------:|--------------:|:-----------|:------------------------|:---------|:--------------|--------------:|-----------:|:--------------|:-----------------|------------------------:|-------------------:|:------------------------------|:--------|--------------:|------------:|:-------------------------------------|--------------------------:|-----------------------:|:-------------------------------------|---------------:|-----------------:|:------------------------|:-------------------------------------|:----------------|-----------:|:-------------------------------------|---------------:|:---------------------|:------------------------|:------------------------|
| 456158               |      219521 |          437 |             0 |        0 | 6                       | ул. 3 ЛИНИЯ ВО, д. 38, кв. 3                       | Причина отказа: сбой программы                        | 999         |        0 |              0 |        0 | 2016-03-25 07:21:00.000 | 2016-03-25 |    1118 | 399=1                                 |        15 |               | 1;52=1:703=1:972=1;               | 0          |     0 |       1 |         1 |                    |                      |          1 | Phone    |                |                   |                     |                   |                         |            |            |             |                         |                 |         | 2017-11-13 09:51:02.151 |           3 |             0 |            | 2016-03-25 11:18:00.000 |     U*> |               |             0 |          0 |               |                  |                         |                    |                               |         |             0 |             |                                      |                         0 |                      1 |                                      |                |                0 | 0                       | D9091F4C-997A-457C-A128-44D522C99FFB |                 | 1427515966 | E63A6781-72AB-40F9-ABC1-3C96056D1E73 |              0 |                      | 2016-03-25 04:21:00.000 | 2016-03-25 08:18:00.000 |
| 497488               |      227794 |          303 |             0 |     1321 | 5                       | ул. Малая БАЛКАНСКАЯ, д. 20, кв. 64,пар. 1, эт. 13 | Android: Пирог в подарок. В лифте нажать на 12-й этаж | 999         |        0 |              0 |        0 | 2016-04-08 05:38:00.000 | 2016-04-08 |    1808 | 399=1                                 |         8 |               | 1;721=1:703=1:848=1;,42;0=0;90=1; | 0          |     0 |       1 |         1 |                    |                      |          1 | Phone    |                |                   |                     |                   |                         |            |            |             |                         |                 |         | 2017-11-13 09:51:02.151 |           3 |             0 |            | 2016-04-08 18:08:00.000 |     U*? |               |             0 |          0 |               |                  |                         |                    |                               |         |             0 |             |                                      |                         0 |                      1 |                                      |                |                0 | 0                       | D9091F4C-997A-457C-A128-44D522C99FFB |                 | 1427515967 | A167632F-5777-4F67-881A-FE3EA69F882C |              0 |                      | 2016-04-08 02:38:00.000 | 2016-04-08 15:08:00.000 |
| 526651               |      201286 |          288 |             0 |     1366 | 5                       | ул. БОРОВАЯ МУРИНО, д. 16                          | Android: . Отзвон - встретят.  Оплата онлайн.         | 1417        |        0 |              0 |        0 | 2016-06-02 21:46:00.000 | 2016-04-29 |    1100 | 1074=1,1031=1,1013=1,399=1            |        13 |               |                                   | 0          |     1 |       1 |         1 |                  1 |                      |          1 | Phone    |                |                   |                     |                   |                         |            |            |             |                         |                 |         | 2017-11-09 22:41:22.970 |             |               |            | 2016-04-29 11:00:00.000 |     U*J |               |             0 |          0 |               |                  |                         |                    |                               |         |             0 |             |                                      |                         0 |                      1 |                                      |                |                0 | 0                       | D9091F4C-997A-457C-A128-44D522C99FFB |                 | 1427515978 | 4AD5C548-F605-4A8B-A13D-B02418809887 |              0 |                      | 2016-06-02 18:46:00.000 | 2016-04-29 08:00:00.000 |
| 582313               |      262598 |          456 |             0 |        0 | 6                       | ул. БОРОВАЯ УЛ. ПОС. МУРИНО, д. 16                 | Причина отказа: некорректный номер                    | 827         |        0 |              0 |        0 | 2016-06-02 20:14:00.000 | 2016-06-02 |    2310 | 1074=1,990=1,644=1                    |        13 |               |                                   | 0          |     0 |       1 |         1 |                  0 |                      |          1 | Phone    |                |                   |                     |                   |                         |            |            |             |                         |                 |         | 2017-11-09 22:41:22.970 |             |               |            | 2016-06-02 23:10:00.000 |     U*T |               |             0 |          0 |               |                  |                         |                    |                               |         |             0 |             |                                      |                         0 |                      1 |                                      |                |                0 | 0                       | D9091F4C-997A-457C-A128-44D522C99FFB |                 | 1427515988 | 50F8722E-2336-4689-95D8-3B72545D1FE8 |              0 |                      | 2016-06-02 17:14:00.000 | 2016-06-02 20:10:00.000 |
| 582330               |      201286 |          247 |             0 |     1781 | 5                       | ул. БОРОВАЯ УЛ. ПОС. МУРИНО, д. 16                 | Отзвон - встретят.  Оплата онлайн.                    | 1375        |        0 |              0 |        0 | 2016-06-02 20:26:00.000 | 2016-06-02 |    2230 | 1074=1,1163=1,990=1,981=1,982=1,399=1 |        13 |               |                                   | 0          |     1 |       1 |         1 |                  1 |                      |          1 | Phone    |                |                   |                     |                   |                         |            |            |             |                         |                 |         | 2017-11-09 22:41:22.970 |             |               |            | 2016-06-02 22:30:00.000 |     U*U |               |             0 |          0 |               |                  |                         |                    |                               |         |             0 |             |                                      |                         0 |                      1 |                                      |                |                0 | 0                       | D9091F4C-997A-457C-A128-44D522C99FFB |                 | 1427515989 | 169A69CE-14B9-4223-B588-82359D36EC59 |              0 |                      | 2016-06-02 17:26:00.000 | 2016-06-02 19:30:00.000 |
| 931278               |      370916 |          627 |             0 |     2421 | 5                       | Ул. разъезжая, Дом: 3, Домофон: 2131, Эт: 3, Кв: 2 | м.Достоевская                                         |             |          |                |          |                         |            |         |                                       |           |               |                                   |            |       |         |           |                    |                      |            |          |                |                   |                     |                   |                         |            |            |             |                         |                 |         |                         |             |               |            |                         |          |               |               |            |               |                  |                         |                    |                               |         |               |             |                                      |                           |                        |                                      |                |                  |                         |                                      |                 |            |                                      |                |                      |                         |                         |
| Сайт:                |             |              |               |          |                         |                                                    |                                                       |             |          |                |          |                         |            |         |                                       |           |               |                                   |            |       |         |           |                    |                      |            |          |                |                   |                     |                   |                         |            |            |             |                         |                 |         |                         |             |               |            |                         |          |               |               |            |               |                  |                         |                    |                               |         |               |             |                                      |                           |                        |                                      |                |                  |                         |                                      |                 |            |                                      |                |                      |                         |                         |
| Отель                |             |              |               |          |                         |                                                    |                                                       |             |          |                |          |                         |            |         |                                       |           |               |                                   |            |       |         |           |                    |                      |            |          |                |                   |                     |                   |                         |            |            |             |                         |                 |         |                         |             |               |            |                         |          |               |               |            |               |                  |                         |                    |                               |         |               |             |                                      |                           |                        |                                      |                |                  |                         |                                      |                 |            |                                      |                |                      |                         |                         |
| Отзвон - встретят. " |         599 |         1000 |             0 |        0 | 2016-11-09 00:00:01.000 | 2016-11-09                                         | 102                                                   | 703=1,399=1 |        1 |                |          | 0                       | 0          |       1 | 1                                     |         0 |               | 1                                 | Website    |       |         |           |                    |                      |            |          |                |                   |                     |                   | 2017-11-09 22:41:22.970 |            |            |             | 2016-11-09 01:02:00.000 |     U*b        |         | 0                       |           0 |               |            |                         |          |               |               |          0 |               |                  |                       0 |                  1 |                               |         |             0 |           0 | D9091F4C-997A-457C-A128-44D522C99FFB |                           |             1427516002 | 41FD2636-EB30-462F-AF2F-A19896A74C7C |              0 |                  | 2016-11-08 21:00:01.000 | 2016-11-08 22:02:00.000              |                 |            |                                      |                |                      |                         |                         |
| 931279               |      370917 |          627 |             0 |     2403 | 5                       | улица Морской Пехоты, 6к2                          | м.Автово                                              |             |          |                |          |                         |            |         |                                       |           |               |                                   |            |       |         |           |                    |                      |            |          |                |                   |                     |                   |                         |            |            |             |                         |                 |         |                         |             |               |            |                         |          |               |               |            |               |                  |                         |                    |                               |         |               |             |                                      |                           |                        |                                      |                |                  |                         |                                      |                 |            |                                      |                |                      |                         |                         |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Сочи_1.1М/Заказы_927к.csv
> - Total rows: 927256

### Schema
```
root
 |-- id: string (nullable = true)
 |-- id_client: string (nullable = true)
 |-- id_user_in: string (nullable = true)
 |-- id_user_out: string (nullable = true)
 |-- driver: string (nullable = true)
 |-- status: string (nullable = true)
 |-- adress: string (nullable = true)
 |-- note_adress: string (nullable = true)
 |-- sum: string (nullable = true)
 |-- sdacha: string (nullable = true)
 |-- count_person: string (nullable = true)
 |-- skidka: string (nullable = true)
 |-- dat_add: string (nullable = true)
 |-- dat: string (nullable = true)
 |-- time_: string (nullable = true)
 |-- subitems: string (nullable = true)
 |-- factory: string (nullable = true)
 |-- ingridients: string (nullable = true)
 |-- actions: string (nullable = true)
 |-- delivery: string (nullable = true)
 |-- pay: string (nullable = true)
 |-- enter: string (nullable = true)
 |-- website: string (nullable = true)
 |-- advertisement_id: string (nullable = true)
 |-- corporate_group_id: string (nullable = true)
 |-- callback: string (nullable = true)
 |-- origin: string (nullable = true)
 |-- house_number: string (nullable = true)
 |-- building_number: string (nullable = true)
 |-- appartment_number: string (nullable = true)
 |-- appartment_type: string (nullable = true)
 |-- street: string (nullable = true)
 |-- intercom: string (nullable = true)
 |-- entrance: string (nullable = true)
 |-- longitude: string (nullable = true)
 |-- latitude: string (nullable = true)
 |-- building_type: string (nullable = true)
 |-- floor: string (nullable = true)
 |-- ts: string (nullable = true)
 |-- db_status: string (nullable = true)
 |-- sync_status: string (nullable = true)
 |-- preorder: integer (nullable = true)
 |-- RV: string (nullable = true)
 |-- delivery_date: string (nullable = true)
 |-- spread_date: string (nullable = true)
 |-- autoProcess: string (nullable = true)
 |-- autoDone: string (nullable = true)
 |-- trayProcess: string (nullable = true)
 |-- origin_version: string (nullable = true)
 |-- IsPaidDeliveryPolygon: string (nullable = true)
 |-- IsInvoicePrinted: string (nullable = true)
 |-- IsProcessedByRoutingOnFront: string (nullable = true)
 |-- cells: string (nullable = true)
 |-- OnlineCheck: string (nullable = true)
 |-- PromoCode: string (nullable = true)
 |-- FacadeFactoryId: string (nullable = true)
 |-- IsSubstituteManufactory: string (nullable = true)
 |-- IsOnlineCheckPrinted: string (nullable = true)
 |-- FacadeOrderId: string (nullable = true)
 |-- FacadeUserId: string (nullable = true)
 |-- ExcludeCutlery: string (nullable = true)
 |-- ExcludeVIS: string (nullable = true)
 |-- RegionId: string (nullable = true)
 |-- PaymentToolId: string (nullable = true)
 |-- version: string (nullable = true)
 |-- order_system_id: string (nullable = true)
 |-- IsSbpPayment: string (nullable = true)
 |-- PaymentRequestCode: string (nullable = true)
 |-- dat_add_utc: string (nullable = true)
 |-- delivery_date_utc: string (nullable = true)

```

### Data sample
```
| id   | id_client               | id_user_in                    |   id_user_out |   driver |   status | adress                  | note_adress                                                        |   sum |   sdacha | count_person   | skidka   | dat_add                 | dat        |   time_ | subitems                                               |   factory | ingridients   |   actions |   delivery | pay                                  | enter                                |   website | advertisement_id                     | corporate_group_id                   |   callback | origin                  | house_number            | building_number         | appartment_number   | appartment_type   | street               | intercom   | entrance   |   longitude |   latitude | building_type   | floor   | ts   | db_status   | sync_status   |   preorder | RV   | delivery_date   | spread_date   | autoProcess   | autoDone   | trayProcess   | origin_version   | IsPaidDeliveryPolygon   | IsInvoicePrinted   | IsProcessedByRoutingOnFront   | cells   | OnlineCheck   | PromoCode   | FacadeFactoryId   | IsSubstituteManufactory   | IsOnlineCheckPrinted   | FacadeOrderId   | FacadeUserId   | ExcludeCutlery   | ExcludeVIS   | RegionId   | PaymentToolId   | version   | order_system_id   | IsSbpPayment   | PaymentRequestCode   | dat_add_utc   | delivery_date_utc   |
|:-----|:------------------------|:------------------------------|--------------:|---------:|---------:|:------------------------|:-------------------------------------------------------------------|------:|---------:|:---------------|:---------|:------------------------|:-----------|--------:|:-------------------------------------------------------|----------:|:--------------|----------:|-----------:|:-------------------------------------|:-------------------------------------|----------:|:-------------------------------------|:-------------------------------------|-----------:|:------------------------|:------------------------|:------------------------|:--------------------|:------------------|:---------------------|:-----------|:-----------|------------:|-----------:|:----------------|:--------|:-----|:------------|:--------------|-----------:|:-----|:----------------|:--------------|:--------------|:-----------|:--------------|:-----------------|:------------------------|:-------------------|:------------------------------|:--------|:--------------|:------------|:------------------|:--------------------------|:-----------------------|:----------------|:---------------|:-----------------|:-------------|:-----------|:----------------|:----------|:------------------|:---------------|:---------------------|:--------------|:--------------------|
| 2    | 427124                  | 1                             |             0 |        0 |        6 | ул. Гудаутская, 3       | IOS:  Причина отказа: Оформил по ошибке. Тест Причина отказа: тест |  1100 |     1500 | 0              | 0.0      | 2020-12-14 19:26:10.443 | 2020-12-14 |    2011 | 3078=1,3100=1,3101=1,399=1                             |      3000 |               |           |          0 | 0                                    | 1                                    |         1 |                                      |                                      |          0 | Ios                     | 3                       |                         |                     |                   | ул. Гудаутская       |            |            |     39.9098 |    43.4497 |                 |         |      |             |               |          0 |      |                 |               |               |            |               |                  |                         |                    |                               |         |               |             |                   |                           |                        |                 |                |                  |              |            |                 |           |                   |                |                      |               |                     |
| ^�  | 2020-12-14 20:11:00.000 | 2020-12-14 19:46:10.000 +0300 |             1 |        0 |          | Ios 3.6.1               | 0                                                                  |       |        1 | "[""16""]"     | 0        |                         | 3000       |       0 | 0                                                      |           |               |         0 |          0 | 1EEDD247-AE30-40CF-B15F-28FE855DE251 |                                      | 173980699 | F058E122-2C34-4C0A-AB3D-1966A5A1B9D9 | 0                                    |            | 2020-12-14 16:26:10.443 | 2020-12-14 17:11:00.000 |                         |                     |                   |                      |            |            |             |            |                 |         |      |             |               |        nan |      |                 |               |               |            |               |                  |                         |                    |                               |         |               |             |                   |                           |                        |                 |                |                  |              |            |                 |           |                   |                |                      |               |                     |
| 3    | 427127                  | 6865                          |             0 |        0 |        5 | ул. Гастелло, 40        | Самовывоз Без оплаты.                                              |  3475 |        0 | 0              | 0.0      | 2020-12-15 11:38:26.890 | 2020-12-15 |    1300 | 3071=1,3074=1,3083=1,2762=1,3104=1,3116=1,2894=1,399=3 |      3000 |               |           |          0 | 2                                    | 0                                    |         1 |                                      | 1145                                 |          1 | Phone                   | 40                      |                         |                     |                   | ул. Гастелло         |            |            |             |            |                 |         |      |             |               |          1 |      |                 |               |               |            |               |                  |                         |                    |                               |         |               |             |                   |                           |                        |                 |                |                  |              |            |                 |           |                   |                |                      |               |                     |
| ^�   | 2020-12-15 13:00:00.000 |                               |             1 |        0 |          |                         | 0                                                                  |       |          | "[""15""       | ""17""]" | 0                       |            |         | 0                                                      |         0 |               |           |          0 | 0                                    | 1EEDD247-AE30-40CF-B15F-28FE855DE251 |           | 173980700                            | E4BF7D3E-7165-4134-8364-CEC59B4BAF14 |          0 |                         | 2020-12-15 08:38:26.890 | 2020-12-15 10:00:00.000 |                     |                   |                      |            |            |             |            |                 |         |      |             |               |        nan |      |                 |               |               |            |               |                  |                         |                    |                               |         |               |             |                   |                           |                        |                 |                |                  |              |            |                 |           |                   |                |                      |               |                     |
| 4    | 427127                  | 6865                          |             0 |        0 |        5 | ул. Гастелло, 40        | Самовывоз Без оплаты.                                              |  3575 |        0 | 0              | 0.0      | 2020-12-15 11:43:36.706 | 2020-12-15 |    1300 | 3073=1,3074=1,3083=1,2762=1,3104=1,3116=1,2851=1,399=3 |      3000 |               |           |          0 | 2                                    | 0                                    |         1 |                                      | 1145                                 |          1 | Phone                   | 40                      |                         |                     |                   | ул. Гастелло         |            |            |             |            |                 |         |      |             |               |          1 |      |                 |               |               |            |               |                  |                         |                    |                               |         |               |             |                   |                           |                        |                 |                |                  |              |            |                 |           |                   |                |                      |               |                     |
| ^�   | 2020-12-15 13:00:00.000 |                               |             1 |        0 |          |                         | 0                                                                  |       |          | "[""16""       | ""18""]" | 0                       |            |         | 0                                                      |         0 |               |           |          0 | 0                                    | 1EEDD247-AE30-40CF-B15F-28FE855DE251 |           | 173980701                            | A193F4BC-0FA3-47AE-A8E5-5EB7E9426689 |          0 |                         | 2020-12-15 08:43:36.706 | 2020-12-15 10:00:00.000 |                     |                   |                      |            |            |             |            |                 |         |      |             |               |        nan |      |                 |               |               |            |               |                  |                         |                    |                               |         |               |             |                   |                           |                        |                 |                |                  |              |            |                 |           |                   |                |                      |               |                     |
| 5    | 427129                  | 430                           |             0 |        0 |        6 | ул. Гастелло, 40        | Сайт:Новый сайт: Причина отказа: Передумал. тест                   |  1680 |     2000 | 0              | 0.0      | 2020-12-15 14:43:11.120 | 2020-12-15 |    1528 | 13=1,2957=1,3023=1,3088=1,399=2                        |         9 |               |           |          0 | 0                                    | 1                                    |         1 |                                      |                                      |          1 | Website                 | 40                      |                         |                     |                   | ул. Гастелло         |            |            |     39.9171 |    43.449  |                 |         |      |             |               |          0 |      |                 |               |               |            |               |                  |                         |                    |                               |         |               |             |                   |                           |                        |                 |                |                  |              |            |                 |           |                   |                |                      |               |                     |
| ^�   | 2020-12-15 15:28:00.000 | 2020-12-15 15:03:11.000 +0300 |             0 |        0 |          | Website 4.0.7           | 0                                                                  |       |        1 |                | 0        |                         | 3000       |       0 | 0                                                      |           |               |         0 |          0 | 1EEDD247-AE30-40CF-B15F-28FE855DE251 |                                      | 173980702 | DB632C9E-DFF5-41A1-81CD-778F89A891A3 | 0                                    |            | 2020-12-15 11:43:11.120 | 2020-12-15 12:28:00.000 |                         |                     |                   |                      |            |            |             |            |                 |         |      |             |               |        nan |      |                 |               |               |            |               |                  |                         |                    |                               |         |               |             |                   |                           |                        |                 |                |                  |              |            |                 |           |                   |                |                      |               |                     |
| 6    | 427128                  | 1                             |             0 |        0 |        6 | пер. Демократический, 5 | IOS:  Причина отказа: тест Оформил по ошибке.                      |  1650 |     2000 | 0              | 0.0      | 2020-12-15 15:06:13.340 | 2020-12-15 |    1551 | 3077=1,3084=1,3088=1,2894=1,399=2                      |      3000 |               |           |          0 | 0                                    | 1                                    |         1 |                                      |                                      |          0 | Ios                     | 5                       |                         |                     |                   | пер. Демократический |            |            |     39.9257 |    43.4238 |                 |         |      |             |               |          0 |      |                 |               |               |            |               |                  |                         |                    |                               |         |               |             |                   |                           |                        |                 |                |                  |              |            |                 |           |                   |                |                      |               |                     |
| ^�   | 2020-12-15 15:51:00.000 | 2020-12-15 15:26:13.000 +0300 |             1 |        0 |          | Ios 3.6.1               | 0                                                                  |       |        1 | "[""17""]"     | 0        |                         | 3000       |       0 | 0                                                      |           |               |         0 |          0 | 1EEDD247-AE30-40CF-B15F-28FE855DE251 |                                      | 173980703 | 92E27CF5-EF59-43A2-8DCB-81F99953AD55 | 0                                    |            | 2020-12-15 12:06:13.340 | 2020-12-15 12:51:00.000 |                         |                     |                   |                      |            |            |             |            |                 |         |      |             |               |        nan |      |                 |               |               |            |               |                  |                         |                    |                               |         |               |             |                   |                           |                        |                 |                |                  |              |            |                 |           |                   |                |                      |               |                     |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Москва_3.7M/Клиенты_440к.csv
> - Total rows: 697968

### Schema
```
root
 |-- id: string (nullable = true)
 |-- name: string (nullable = true)
 |-- card: string (nullable = true)
 |-- count: string (nullable = true)
 |-- sum: string (nullable = true)
 |-- note: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- street: string (nullable = true)
 |-- email: string (nullable = true)
 |-- corporate_group_id: string (nullable = true)
 |-- corporate_day_budget: string (nullable = true)
 |-- create_date: string (nullable = true)
 |-- RV: string (nullable = true)
 |-- version: string (nullable = true)
 |-- client_origin: string (nullable = true)

```

### Data sample
```
| id             | name              | card   |   count | sum                     | note                        |       phone | street                                                    | email   | corporate_group_id   |   corporate_day_budget | create_date             | RV       |   version | client_origin   |
|:---------------|:------------------|:-------|--------:|:------------------------|:----------------------------|------------:|:----------------------------------------------------------|:--------|:---------------------|-----------------------:|:------------------------|:---------|----------:|:----------------|
| 8              | Георгий           |        |      24 | 31504                   | Наш сотрудник.              | 79112948042 | пр-д Научный, 17, кв/оф , пар , д-фон , этаж              |         |                      |                      0 | 2017-03-22 10:30:31.524 |     A=� | 306265475 | Phone           |
| 9              | Тест              |        |      23 | 18955                   |                             | 79117337170 | Фестиваль                                                 |         |                      |                      0 | 2017-03-23 14:43:15.572 |     A%� | 306259450 | Phone           |
| 10             | Клиент            |        |       1 | 2418                    | нет                         | 79999999945 | ул. FGHFGH, д. xfgfdf                                     |         |                      |                      0 | 2017-03-23 15:57:28.162 |     ;�e | 305897061 | Android         |
| 11             | Никита            |        |      61 | 70186                   | . Пред.заказ. Наш сотрудник | 79650700101 | ул. Коломенская, 12 к1, кв/оф 184, пар 3, д-фон , этаж 11 |         |                      |                  10000 | 2017-03-23 16:43:21.221 |     =%N | 305997134 | DeliveryClub    |
| 12             | Екатерина         |        |      30 | 37731                   | к вокам вилки               | 79166140404 | ул. Мосфильмовская, 74 Б                                  |         |                      |                      0 | 2017-03-23 20:23:06.915 |     C�� | 306444221 | Site            |
| 13             | Алексей           |        |       1 | 457                     |                             | 79686901692 | Краснодонская улица, 3к2                                  |         |                      |                        |                         |          |           |                 |
| Квартира: 195" |                   |        |       0 | 2017-03-24 09:43:06.670 |     @�l                    |   306228076 | DeliveryClub                                              |         |                      |                        |                         |          |           |                 |
| 14             | Александра/Герман |        |       3 | 4610                    | Количество персон: 1        | 79168248707 | проезд Шокальского, 3к1                                   |         |                      |                        |                         |          |           |                 |
| Квартира: 268" |                   |        |       0 | 2017-03-24 10:06:33.629 |     =o�                    |   306016208 | DeliveryClub                                              |         |                      |                        |                         |          |           |                 |
| 15             | Михаил            |        |       1 | 1357                    | 215896001.                  | 79119932702 | Ул:Минеральная  Д:13 К:А Кв:                              |         |                      |                      0 | 2017-03-24 14:12:12.716 |     BD | 306320196 | Ios             |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Санкт-Петербург_22.4М/Клиенты_2.4М.csv
> - Total rows: 2470004

### Schema
```
root
 |-- id: string (nullable = true)
 |-- name: string (nullable = true)
 |-- card: string (nullable = true)
 |-- count: string (nullable = true)
 |-- sum: string (nullable = true)
 |-- note: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- street: string (nullable = true)
 |-- email: string (nullable = true)
 |-- corporate_group_id: string (nullable = true)
 |-- corporate_day_budget: string (nullable = true)
 |-- create_date: string (nullable = true)
 |-- RV: string (nullable = true)
 |-- version: string (nullable = true)
 |-- client_origin: string (nullable = true)

```

### Data sample
```
|   id | name     | card   |   count |   sum | note                                                                     |       phone | street                                                                 | email   | corporate_group_id   |   corporate_day_budget | create_date             | RV       | version    | client_origin   |
|-----:|:---------|:-------|--------:|------:|:-------------------------------------------------------------------------|------------:|:-----------------------------------------------------------------------|:--------|:---------------------|-----------------------:|:------------------------|:---------|:-----------|:----------------|
|    2 | Сергей   |        |       1 |   999 |                                                                          | 79118289154 |                                                                        |         |                      |                      0 | 2013-03-16 16:17:25.076 |     N&m? | 1311141183 |                 |
|    3 | Павел    |        |      20 | 28637 | 1051815438 Пред.заказ.                                                   | 79811813654 | Адмиралтейский проезд, д 1                                             |         |                      |                      0 | 2013-03-17 17:37:15.381 |     S2�� | 1395828917 | Ios             |
|    4 | Артём    |        |     114 | 57979 | Наш сотрудник. Лыба Артем Алексеевич КД на Ш. Революции +7 911 935-02-11 | 79119350211 | ш. Революции, 69 лит. А                                                |         |                      |                      0 | 2013-03-18 08:41:09.425 |     S�  | 1394078492 | Phone           |
|    5 | Владимир |        |       2 |  2879 |                                                                          | 79117521112 | ул.Ялтинская   д.4                                                     |         |                      |                      0 | 2013-03-18 08:55:44.127 |     N�~ | 1310557310 |                 |
|    6 | Георгий  |        |       1 |   999 |                                                                          | 79522047071 |                                                                        |         |                      |                      0 | 2013-03-18 09:16:19.252 |     N1� | 1311883799 |                 |
|    7 | Дмитрий  |        |       5 |  7262 | . Пред.заказ                                                             | 79052147763 | Расстанная ул., 2/2, кв/оф 616, этаж 6                                 |         |                      |                      0 | 2013-03-18 09:18:07.506 |     S#E | 1394820370 | Site            |
|    8 | Сергей   |        |       0 |     0 | город:Санкт-Петербург                                                    | 79119724214 | ул Карпинского, д 33 к 1, кв/оф 254, пар 3, д-фон 254, этаж 7          |         |                      |                      0 | 2013-03-18 09:35:33.635 |     S    | �m         | 1395452525      |
|    9 | Ирина    |        |       1 |   698 |                                                                          | 79117279231 | п. Парголово ул. Николая Рубцова, 9, кв/оф 307, пар 3, д-фон , этаж 10 |         |                      |                      0 | 2013-03-18 09:40:08.104 |     S    | �n         | 1395452526      |
|   10 | Алексей  |        |       1 |  1740 | В Подарок творог-картофель 0,8                                           | 79052188992 |                                                                        |         |                      |                      0 | 2013-03-18 09:40:48.629 |     N&� | 1311116485 |                 |
|   11 | Светлана |        |       1 |  2360 | сдача с 5000.                                                            | 79117883818 |                                                                        |         |                      |                      0 | 2013-03-18 09:43:34.710 |     N"V� | 1310873240 |                 |
```

> - Code name: index_0042
> - File path: Dostaevsky.ru_07.2023_3.1M/Сочи_1.1М/Клиенты_187к.csv
> - Total rows: 187145

### Schema
```
root
 |-- id: string (nullable = true)
 |-- name: string (nullable = true)
 |-- card: string (nullable = true)
 |-- count: string (nullable = true)
 |-- sum: string (nullable = true)
 |-- note: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- street: string (nullable = true)
 |-- email: string (nullable = true)
 |-- corporate_group_id: string (nullable = true)
 |-- corporate_day_budget: string (nullable = true)
 |-- create_date: string (nullable = true)
 |-- RV: string (nullable = true)
 |-- version: string (nullable = true)
 |-- client_origin: timestamp (nullable = true)

```

### Data sample
```
| id     | name      | card   |   count |   sum | note           |       phone | street                                               | email         | corporate_group_id   |   corporate_day_budget | create_date             | RV   | version   | client_origin   |
|:-------|:----------|:-------|--------:|------:|:---------------|------------:|:-----------------------------------------------------|:--------------|:---------------------|-----------------------:|:------------------------|:-----|:----------|:----------------|
| 427122 | Эдвардас  |        |       5 |  8394 |                | 79046309745 | ул. Невская, 16, кв/оф 123, пар 1, д-фон 123, этаж 2 |               |                      |                      0 | 2020-11-17 14:13:29.130 |      |           | NaT             |
| ��    | 168136423 |        |         |       |                |             |                                                      |               |                      |                        |                         |      |           | NaT             |
| 427123 | тест      |        |       9 | 14865 | ТЕСТОВЫЙ ЗАКАЗ | 79111111111 | ул. Даргомыжского, 8Б                                |               |                      |                      0 | 2020-12-09 17:48:19.503 |      |           | NaT             |
| @0�    | 171978992 | Phone  |         |       |                |             |                                                      |               |                      |                        |                         |      |           | NaT             |
| 427124 | Георгий   |        |       0 |     0 | . Пред.заказ   | 79112899077 | ул. Новая Заря д 7                                   | xcosx@mail.ru |                      |                      0 | 2020-12-12 13:18:16.486 |      |           | NaT             |
| V��    | 173462474 | Ios    |         |       |                |             |                                                      |               |                      |                        |                         |      |           | NaT             |
| 427125 | Кирилл    |        |       0 |     0 |                | 79879915981 | ул. Авиационная, 30, кв/оф 1, пар 1, д-фон , этаж 1  |               |                      |                      0 | 2020-12-12 14:57:08.023 |      |           | NaT             |
| @��    | 172002475 | Site   |         |       |                |             |                                                      |               |                      |                        |                         |      |           | NaT             |
| 427126 | Раджана   |        |       0 |     0 | . Пред.заказ   | 79819140809 | ул. Приреченская, 4, кв/оф , пар , д-фон , этаж      |               |                      |                      0 | 2020-12-12 18:44:19.913 |      |           | NaT             |
| PX    | 168185944 |        |         |       |                |             |                                                      |               |                      |                        |                         |      |           | NaT             |
```


## About final data
> - Total rows: 3003457

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- password: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Data sample
```
| names                     | emails                        | phones          | accounts                                                                                                           | address                                                                                                                                                                                                                                        |
|:--------------------------|:------------------------------|:----------------|:-------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['. Кд Гамзаев Заги']     |                               | ['79167778613'] | [Row(title='DOSTAЕВСКИЙ — Доставка еды - Достаевский', link='https://dostaevsky.ru', id='560678', password=None)]  |                                                                                                                                                                                                                                                |
| ['.Hbq']                  | ['yuri2710@yandex.ru']        | ['79313064741'] | [Row(title='DOSTAЕВСКИЙ — Доставка еды - Достаевский', link='https://dostaevsky.ru', id='1816667', password=None)] | ['пр. Лиговский 92 Г', 'ул. Савушкина 133 к3 квоф 5 пар 1 этаж 2', 'пр. Лиговский 92 лит. Г', 'пр. Лиговский, 92 лит. Г, кв/оф , пар , д-фон , этаж']                                                                                          |
| ['A Shchitkovkaia']       | ['zheltyj.drackon@gmail.com'] | ['79516435666'] | [Row(title='DOSTAЕВСКИЙ — Доставка еды - Достаевский', link='https://dostaevsky.ru', id='1672522', password=None)] | ['ул. Корнеева 6 квоф 28 пар 1 этаж 7', 'ул. Маршала Говорова 47', 'Корнеева 6 квоф 28 этаж 7', 'ул. Корнеева, 6, кв/оф 28, пар 1, д-фон , этаж 7']                                                                                            |
| ['A Songerlaynen']        |                               | ['79522337998'] | [Row(title='DOSTAЕВСКИЙ — Доставка еды - Достаевский', link='https://dostaevsky.ru', id='1620332', password=None)] | ['дор. Муринская 14 к3 квоф 156', 'пр. Героев 26 к1 квоф 156 пар 1 этаж 7', 'пр. Героев, 26 к1, кв/оф 156, пар 1, этаж 7']                                                                                                                     |
| ['Aa.Mezencevagmail.Com'] |                               | ['79111291195'] | [Row(title='DOSTAЕВСКИЙ — Доставка еды - Достаевский', link='https://dostaevsky.ru', id='716567', password=None)]  | ['пер Лыжный Санкт-Петербург д 4 к 1 кв 183 пар 2 д-фон этаж 10', 'пер Лыжный, Санкт-Петербург, д 4, к 1, кв 183, пар 2, д-фон , этаж 10']                                                                                                     |
| ['Abbos']                 |                               | ['79633230167'] | [Row(title='DOSTAЕВСКИЙ — Доставка еды - Достаевский', link='https://dostaevsky.ru', id='523997', password=None)]  | ['Всеволожский р-н деревня Кудрово ул Английская 1 квоф 111 пар 2 этаж 11', 'ул. ПРОСПЕКТ МЕТАЛЛИСТОВ д. 82 кв. 349', 'УлОзерная Д3 К Кв87 Санкт-Петербург', 'Всеволожский р-н, деревня Кудрово, ул Английская, 1, кв/оф 111, пар 2, этаж 11'] |
| ['Abderrahman']           |                               | ['79967841463'] | [Row(title='DOSTAЕВСКИЙ — Доставка еды - Достаевский', link='https://dostaevsky.ru', id='2031693', password=None)] | ['Санкт-Петербург улица Хлопина 13к1']                                                                                                                                                                                                         |
| ['Abdo']                  |                               | ['79667597185'] | [Row(title='DOSTAЕВСКИЙ — Доставка еды - Достаевский', link='https://dostaevsky.ru', id='974398', password=None)]  | ['поселок Парголово ул Валерия Гаврилина д 3 к 1 квоф 497 этаж 13', 'ул Хлопина д 13 к 1', 'ул Хлопина, д 13 к 1']                                                                                                                             |
| ['Abdulla']               |                               | ['79657845769'] | [Row(title='DOSTAЕВСКИЙ — Доставка еды - Достаевский', link='https://dostaevsky.ru', id='715359', password=None)]  | ['Хлопина 13 к 1', 'ул Хлопина д 13 к 1', 'ул Хлопина д 13 к 1 квоф 22-3', 'ул Хлопина д 13 к 1 квоф 22 пар 1 этаж 7', 'ул Хлопина д 13 к 1 квоф 22', 'ул Хлопина, д 13 к 1, кв/оф 22, пар 1, этаж 7']                                         |
| ['Abdurazzoq']            |                               | ['79312530193'] | [Row(title='DOSTAЕВСКИЙ — Доставка еды - Достаевский', link='https://dostaevsky.ru', id='1057718', password=None)] | ['г. Санкт-Петербург', 'ул. Рентгена 10', 'пр. Просвещения, 53 к1, кв/оф , пар , д-фон , этаж']                                                                                                                                                |
```