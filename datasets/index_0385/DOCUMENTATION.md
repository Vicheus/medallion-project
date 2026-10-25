# Parsetron results

## About row data

> - File path: burgerheroes.ru.csv
> - Total rows: 76243

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- address_id: string (nullable = true)
 |-- sex: string (nullable = true)
 |-- birth: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: long (nullable = true)
 |-- name: string (nullable = true)
 |-- remark: string (nullable = true)
 |-- surname: string (nullable = true)
 |-- crm_card: string (nullable = true)
 |-- password: string (nullable = true)
 |-- created_at: timestamp (nullable = true)
 |-- updated_at: timestamp (nullable = true)
 |-- crm_password: string (nullable = true)

```

### Data sample
```
|   id | address_id   | sex   | birth   | email                          |       phone | name      | remark   | surname   | crm_card   | password                         | created_at          | updated_at          | crm_password   |
|-----:|:-------------|:------|:--------|:-------------------------------|------------:|:----------|:---------|:----------|:-----------|:---------------------------------|:--------------------|:--------------------|:---------------|
|   49 | NULL         | male  | NULL    | NULL                           | 79296035770 | Ольга     | NULL     | NULL      | NULL       | f84b89bcf33c161bdaa19c925928f74d | 2020-08-07 11:09:30 | 2020-08-07 11:09:30 | NULL           |
|   50 | NULL         | male  | NULL    | valentine.mitrofanov@gmail.com | 79197760289 | Валентин  | NULL     | NULL      | 1000011    | cadee88ca0c7c9650dc4380fd51a742a | 2020-08-10 09:32:05 | 2020-11-13 17:36:40 | 27361          |
|   61 | NULL         | male  | NULL    | NULL                           | 79050489091 | Настя     | NULL     | NULL      | 1039857    | 676c0c9be43fd984c92b0ecfdab3c0d9 | 2020-09-28 16:27:29 | 2020-11-14 20:23:03 | 39145          |
|   65 | NULL         | male  | NULL    | p.rabchevski@gmail.com         | 79199979472 | Петр      | NULL     | NULL      | 1012614    | 2806c23dbff477d1a3911b012d7db02a | 2020-10-07 00:17:58 | 2021-09-20 21:58:02 | 16025          |
|   66 | NULL         | male  | NULL    | valerierait@gmail.com          | 79652977988 | валерия   | NULL     | NULL      | 1008112    | 2a5330b86bb7eb4ec7eacb3712cda893 | 2020-10-09 22:11:44 | 2021-11-02 16:03:55 | 77026          |
|   67 | NULL         | male  | NULL    | NULL                           | 79105640778 | Сергей    | NULL     | NULL      | NULL       | 125c4d3d18ddcfddeb16a31139d218d0 | 2020-10-09 22:46:49 | 2020-10-09 22:46:49 | 94674          |
|   68 | NULL         | male  | NULL    | skyn1fe@gmail.com              | 79999228077 | Ruslan    | NULL     | NULL      | 1002272    | 7923940dede5bbccb83d8403960bcfd4 | 2020-10-10 01:07:19 | 2020-11-13 12:27:56 | 78832          |
|   69 | NULL         | male  | NULL    | NULL                           | 79959051785 | Татьяна   | NULL     | NULL      | NULL       | f8df2ca542378b6f3fe9c525f1d844f8 | 2020-10-10 02:06:46 | 2020-10-10 02:06:46 | 78432          |
|   70 | NULL         | male  | NULL    | NULL                           | 79859057825 | Андрей    | NULL     | NULL      | 1040319    | e5ded0be7bbaf0e297caa2d09642c661 | 2020-10-10 10:18:30 | 2023-02-26 12:51:49 | 90563          |
|   71 | NULL         | male  | NULL    | NULL                           | 79163653714 | Анастасия | NULL     | NULL      | 1040320    | 95f499940a14e0624914b5a05dee63c5 | 2020-10-10 10:56:19 | 2023-02-26 12:53:05 | 47673          |
|   72 | NULL         | male  | NULL    | NULL                           | 79163232626 | Вячеслав  | NULL     | NULL      | NULL       | cfa37ea299061248adb9c9b895ecfd85 | 2020-10-10 13:24:05 | 2020-10-10 13:24:05 | 54676          |
|   73 | NULL         | male  | NULL    | NULL                           | 79152822008 | Олеся     | NULL     | NULL      | NULL       | 75ecc7815c90984683f5428c68f09933 | 2020-10-10 13:35:54 | 2020-10-10 13:35:54 | 82353          |
|   74 | NULL         | male  | NULL    | korneeva99@mail.ru             | 79250108564 | Olga      | NULL     | NULL      | 1000052    | 766c277615f96f99d3f7ed6ed3307bbc | 2020-10-10 13:44:14 | 2020-11-23 14:45:20 | 55827          |
|   75 | NULL         | male  | NULL    | NULL                           | 79850178874 | Антон     | NULL     | NULL      | NULL       | 21ab18a30c7c31a3e939bebe2ca55cb6 | 2020-10-10 13:51:50 | 2020-10-10 13:51:50 | 62314          |
|   76 | NULL         | male  | NULL    | NULL                           | 79637737913 | Лейла     | NULL     | NULL      | NULL       | ce1585548af13d60697a39d274869dc8 | 2020-10-10 14:13:27 | 2020-10-10 14:13:27 | 71552          |
|   77 | NULL         | male  | NULL    | NULL                           | 79175458135 | Евгений   | NULL     | NULL      | NULL       | ad2c7bc5576a11bf1515a540862af2d6 | 2020-10-10 14:31:27 | 2020-10-10 14:31:27 | 41283          |
|   78 | NULL         | male  | NULL    | perezegor@icloud.com           | 79162025758 | Егор      | NULL     | NULL      | 1033699    | 7bbadfd20ac20bf891e24f1e16eb4eca | 2020-10-10 15:06:24 | 2021-01-16 16:13:40 | 99758          |
|   79 | NULL         | male  | NULL    | mariaschool@bk.ru              | 79190406020 | Мария     | NULL     | NULL      | 1037797    | e0501dd4a84df989ef1664ea7eb22adb | 2020-10-10 15:12:40 | 2020-12-13 18:46:13 | 94854          |
|   80 | NULL         | male  | NULL    | belks.98@mail.ru               | 79998484049 | Анастасия | NULL     | NULL      | 1000153    | 99f6a934a7cf277f2eaece8e3ce619b2 | 2020-10-10 16:23:30 | 2022-12-22 13:56:57 | 11013          |
|   81 | NULL         | male  | NULL    | NULL                           | 79854900608 | Стас      | NULL     | NULL      | 1040330    | 47751950afeac8d6e92962c690667e0f | 2020-10-10 16:37:07 | 2020-11-21 18:05:48 | 77694          |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Sex | 100.00% |
| Phones | 100.00% |
| Accounts | 100.00% |
| Actuality | 100.00% |



### Data sample
```
| names                |   sex | phones          | accounts                                                                                                                                          | actuality   |
|:---------------------|------:|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Сергей']           |     1 | ['79032454155'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='NULL', password_hash='c79bb048121bbc1d20d79c6b83ef17b5')]                      | 10.10.2020  |
| ['Даниил']           |     1 | ['79045836949'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='Vikhrov.d@mail.ru', password_hash='9375084629cd055e6b819053bc9714de')]         | 11.10.2020  |
| ['Кирилл']           |     1 | ['79261552198'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='NULL', password_hash='0ac1bdd41792e3b82ed318e2adf62ef1')]                      | 16.10.2021  |
| ['Andrey']           |     1 | ['79374721510'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='davlyaev@gmail.com66524', password_hash='dea8f4099d73382ff4eb973529375e63')]   | 13.10.2020  |
| ['Екатерина']        |     1 | ['79057688007'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='katefrommoon@gmail.com', password_hash='9815cef307a57884d9563e8037cda496')]    | 25.07.2023  |
| ['Иван']             |     1 | ['79255067787'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='NULL', password_hash='468df2874368dc8fc93a74a0977cfba5')]                      | 16.10.2020  |
| ['Анастасия']        |     1 | ['79264283236'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='Astupko@gmail.com', password_hash='83475238709616235c8d155c95629c02')]         | 25.10.2020  |
| ['Мария']            |     1 | ['79856231013'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='Mary_Morsova@bk.ru', password_hash='94faf91ced3043d9738ed92f354f23d1')]        | 31.10.2020  |
| ['Роман']            |     1 | ['79268571467'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='romagolnev@gmail.com', password_hash='a95c40505b26d14572fa13eb4f2e7fe0')]      | 31.10.2020  |
| ['Эльман']           |     1 | ['79652686568'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='emil159719@gmail.com', password_hash='aad92567225d700b4408b63e7fe0f9c8')]      | 31.10.2020  |
| ['Лилия']            |     1 | ['79107503233'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='lilia.andreyashkina@ya.ru', password_hash='441d9b1d721e29971edc93bca39bf497')] | 13.08.2021  |
| ['Наталья']          |     1 | ['79037385838'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='Italy-01@yandex.ru', password_hash='61dede89ddccbec715c89d7f409658d6')]        | 05.11.2020  |
| ['Никита']           |     1 | ['79998033567'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='wearo@yandex.ru', password_hash='6c714999e23482178f39ffb77647f8a8')]           | 07.11.2020  |
| ['Максим']           |     1 | ['79272006661'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='Chipcd911@mail.ru', password_hash='759dd4c674f0643b11bb9d1adff6e928')]         | 09.11.2020  |
| ['Александр']        |     1 | ['79153503766'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='komadynkoalex@yandex.ru', password_hash='caca95c5de87163f12e038d05eb7b555')]   | 13.11.2020  |
| ['Анастасия']        |     1 | ['79771975107'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='ansolovyeva@mail.ru', password_hash='5a8a0f2779706d8eff072fa34acfb143')]       | 26.01.2021  |
| ['Филлип']           |     1 | ['79651585391'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='krash.me@hotmail.com', password_hash='593a5897c7e61892028b751da337a193')]      | 26.11.2020  |
| ['Елизавета']        |     1 | ['79151168614'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='lizasobol09@gmail.com', password_hash='8e054c9fb4824539ea93499ea3fafb06')]     | 20.11.2020  |
| ['Tatiana Shkarova'] |     1 | ['79165555254'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='kartina80@mail.ru', password_hash='73aec7e7e29aa475859412e028df8d77')]         | 21.11.2020  |
| ['Михаил']           |     1 | ['79250080415'] | [Row(title='Burger Heroes', link='https://burgerheroes.ru', login='red.khar@mail.ru', password_hash='6a600c968f4e6a843dcaf600c1694e42')]          | 22.11.2020  |
```