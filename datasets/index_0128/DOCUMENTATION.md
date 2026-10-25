# Parsetron results

## About row data

> - Code name: index_0128
> - File path: /media/user/TRANSCEND/Databases/index_0128/raw/preprocessed/users_info_1_preprocessed.csv
> - Total rows: 5076

### Schema
```
root
 |-- USER_ID: integer (nullable = true)
 |-- username: string (nullable = true)
 |-- password_hash: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- phone: long (nullable = true)
 |-- birth_date: date (nullable = true)

```

### Data sample
```
|   USER_ID | username               | password_hash                                                                                              | first_name             | last_name   | middle_name   | email                           | gender   |           phone | birth_date   |
|----------:|:-----------------------|:-----------------------------------------------------------------------------------------------------------|:-----------------------|:------------|:--------------|:--------------------------------|:---------|----------------:|:-------------|
|         1 | admin                  | $6$JyLLsGgUQNi1ZN7L$LUh.bTi3uuhw22xGY8sfymDr7NZ9tgJgpTHqoyLcpkkyEdJAc9oay8GWOpRoVvhH15UsqUcDzPX.nn7n/5YsY1 | Михаил                 | Ветров      |               | vetrov_m@web-maxima.ru          |          |     7.90337e+10 |              |
|         9 | bagrov_v               | IKoxiJwb88c9071de37e7a2054d804a8a01cc819                                                                   | Виктор                 | Багров      |               | bagrov_v@yandex.ru              |          |   nan           |              |
|        10 | usopov_r@web-maxima.ru | j8W]K1,ee53e7566b1970a92df01d91ab5e5e4e8                                                                   | Ратмир                 | Юсупов      |               | usopov_r@web-maxima.ru          |          |   nan           |              |
|        13 | sdfsdfsdfsds@binka.me  | F&t3/5cF24267fff529df33339d3ba066c03aa2f                                                                   | Петр                   | Петров      |               | sdfsdfsdfsds@binka.me           |          |   nan           |              |
|        15 | dautov.r@web-maxima.ru | 1i/V5aR=fbb5c84fd393d23e5d9250adcdf6ef4f                                                                   | Рустам                 | Даутов      |               | dautov.r@web-maxima.ru          |          |   nan           |              |
|        16 | cozaf@p33.org          | }1oIG9+q00daaffdae9b52fb4ae303c8d1f40d65                                                                   | 111                    | 1111        |               | cozaf@p33.org                   |          |   nan           |              |
|        17 | anonymous_fbx68o08b    | Yeh8UZHo32b67bdceceeb784438683a931e5ec53                                                                   | Анонимный пользователь |             |               | anonymous_fbx68o08b@example.com |          |   nan           |              |
|        20 | p.dubovickiy@ya.ru     | WIZaBXmq717946fcf38a569a5fc848922e193d16                                                                   | Павел                  | Дубовицкий  |               | p.dubovickiy@ya.ru              |          |   nan           |              |
|        21 | belsmet@mailr.ru       | dbbwcl2Qefe6201942281c99f78316ff0d2fdc32                                                                   | v                      | 12312312    |               | belsmet@mail.ru                 |          | 33323           |              |
|        22 | cowojadizi             | Wk271kje4aeae6d2a954a9fd9af2fe3e794239f7                                                                   | Михаил                 | Ветров      |               | cowojadizi@doanart.com          |          |     7.90337e+10 |              |
```

> - Code name: index_0128
> - File path: /media/user/TRANSCEND/Databases/index_0128/raw/preprocessed/users_info_2_preprocessed.csv
> - Total rows: 3782

### Schema
```
root
 |-- USER_ID: string (nullable = true)
 |-- name2: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- phone2: string (nullable = true)
 |-- address: string (nullable = true)
 |-- company: string (nullable = true)
 |-- company_addr: string (nullable = true)

```

### Data sample
```
|   USER_ID | name2                    | email2                         | phone2                  | address                      | company       | company_addr   |
|----------:|:-------------------------|:-------------------------------|:------------------------|:-----------------------------|:--------------|:---------------|
|         1 | Тестович тест Тест       | vladimir_yudin@web-maxima.ru   | 89871111111             | ул. тестовая дом корень из 2 | ООО Василек   | юрадрес        |
|         8 |                          | sdfsdfsfsdfsdf@dsfsdfsdfsdf.ru | +7 (555) 555-55-55      | ываываываываываыв            |               |                |
|         9 |                          | bagrov_v@yandex.ru             | +7 (987) 882-99-84      | 60 лет октября, 34           |               |                |
|        11 |                          | vetrov_m@web-maxima.ru         | +7 (111) 111-11-11      | 1111111111                   |               |                |
|        12 |                          | vetrov_m@web-maxima.ru         | 11111111111             | уца фы фыв                   |               |                |
|        13 |                          | sdfsdfsdfsds@binka.me          | +7 (888) 888-88-88      |                              |               |                |
|        15 |                          | dautov.r@web-maxima.ru         | 89998989789879789879789 | всесоюзная 9                 | рога и копыта | пушкина        |
|        18 | 1111111111               | aaaaaaaaaa@sssssssssss.ru      | 33333333333333          | аааааааааааааааааа           |               |                |
|        22 | Ветров Михаил Алексеевич | cowojadizi@doanart.com         | 89033677000             | элеваторная 2                |               |                |
|        23 | 1111111                  | wfsdfgsd@wqrwefd.ru            | 111111111               | 2222222222222                |               |                |
```


## About final data
> - Total rows: 3694

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
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```

### Data sample
```
| names                                         | emails                                                     | phones                         | address                          |   sex | birth_date   | works                                                                                                      | accounts                                                                                                                                                                                                        |
|:----------------------------------------------|:-----------------------------------------------------------|:-------------------------------|:---------------------------------|------:|:-------------|:-----------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Ветров Михаил']                             | ['vetrov_m@web-maxima.ru', 'vladimir_yudin@web-maxima.ru'] | ['79033677231', '79871111111'] | ['Ул. Тестовая Дом Корень Из 2'] |   nan |              | [Row(post=None, date_start=None, date_end=None, company='ООО Василек', address='Юрадрес', comment=None)]   | [Row(title='Магазин игрушек Лимпопо', link='https://limpopo56.ru/', login='admin', password_hash='$6$JyLLsGgUQNi1ZN7L$LUh.bTi3uuhw22xGY8sfymDr7NZ9tgJgpTHqoyLcpkkyEdJAc9oay8GWOpRoVvhH15UsqUcDzPX.nn7n/5YsY1')] |
| ['Багров Виктор']                             | ['bagrov_v@yandex.ru']                                     | ['79878829984']                | ['60 Лет Октября 34']            |   nan |              |                                                                                                            | [Row(title='Магазин игрушек Лимпопо', link='https://limpopo56.ru/', login='bagrov_v', password_hash='IKoxiJwb88c9071de37e7a2054d804a8a01cc819')]                                                                |
| ['Петров Петр']                               | ['sdfsdfsdfsds@binka.me']                                  |                                |                                  |   nan |              |                                                                                                            | [Row(title='Магазин игрушек Лимпопо', link='https://limpopo56.ru/', login='sdfsdfsdfsds@binka.me', password_hash='F&t3/5cF24267fff529df33339d3ba066c03aa2f')]                                                   |
| ['Даутов Рустам']                             | ['dautov.r@web-maxima.ru']                                 |                                | ['Всесоюзная 9']                 |   nan |              | [Row(post=None, date_start=None, date_end=None, company='рога и копыта', address='Пушкина', comment=None)] | [Row(title='Магазин игрушек Лимпопо', link='https://limpopo56.ru/', login='dautov.r@web-maxima.ru', password_hash='1i/V5aR=fbb5c84fd393d23e5d9250adcdf6ef4f')]                                                  |
| ['Ветров Михаил', 'Ветров Михаил Алексеевич'] | ['cowojadizi@doanart.com']                                 | ['79033677000']                | ['Элеваторная 2']                |   nan |              |                                                                                                            | [Row(title='Магазин игрушек Лимпопо', link='https://limpopo56.ru/', login='cowojadizi', password_hash='Wk271kje4aeae6d2a954a9fd9af2fe3e794239f7')]                                                              |
| ['Фуавыаыв']                                  | ['adsfgsd@wedsadsa.com']                                   |                                | ['235423453245']                 |   nan |              |                                                                                                            | [Row(title='Магазин игрушек Лимпопо', link='https://limpopo56.ru/', login='adsfgsd', password_hash='O8yNCH59a99c83257b1cc8f66d938cd0ff19712a')]                                                                 |
| ['Ref']                                       | ['test444@binka.me']                                       |                                | ['Fafasfaf']                     |   nan |              |                                                                                                            | [Row(title='Магазин игрушек Лимпопо', link='https://limpopo56.ru/', login='test444', password_hash='O9QAOFGKd3c132bbc4ce1460f1781c3b62ce55ff')]                                                                 |
| ['Михаил Ветров']                             | ['vetrov_m@web-maxima.ru']                                 |                                | ['Hjkhjkhjkhjkhjk']              |   nan |              |                                                                                                            |                                                                                                                                                                                                                 |
| ['Рустам']                                    | ['dautov.r@web-maxima.ru']                                 |                                | ['Tqtqwt']                       |   nan |              |                                                                                                            | [Row(title='Магазин игрушек Лимпопо', link='https://limpopo56.ru/', login='dautov.r', password_hash='mY4pvke43f340c769ebf333308a2afbadc81c7d2')]                                                                |
| ['Ветров М']                                  | ['tonisak@p33.org']                                        | ['79033677231']                |                                  |   nan |              |                                                                                                            |                                                                                                                                                                                                                 |
```