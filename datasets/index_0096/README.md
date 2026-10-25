# Parsetron results

## About row data

> - Code name: index_0096
> - File path: SberPravo_user.csv
> - Total rows: 120901

### Schema
```
root
 |-- id: string (nullable = true)
 |-- email: string (nullable = true)
 |-- email_constraint: string (nullable = true)
 |-- email_verified: string (nullable = true)
 |-- enabled: string (nullable = true)
 |-- federation_link: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- realm_id: string (nullable = true)
 |-- username: string (nullable = true)
 |-- created_timestamp: long (nullable = true)
 |-- service_account_client_link: string (nullable = true)
 |-- not_before: integer (nullable = true)

```

### Data sample
```
| id                                   | email                       | email_constraint                     | email_verified   | enabled   | federation_link   | first_name     | last_name   | realm_id   | username                    |   created_timestamp | service_account_client_link   |   not_before |
|:-------------------------------------|:----------------------------|:-------------------------------------|:-----------------|:----------|:------------------|:---------------|:------------|:-----------|:----------------------------|--------------------:|:------------------------------|-------------:|
| 7949780a-ede7-4c88-a39e-73d7139c2a51 |                             | 7ba79114-fdbf-4f89-bcb2-0fc4cef38ba6 | f                | t         |                   | Иван           | Иванов      | master     | +79851112245                |       1599473182321 |                               |            0 |
| bb6a830c-9202-4269-88bc-82e86fee56dd | sudakova.i.fe@sberbank.ru   | sudakova.i.fe@sberbank.ru            | t                | t         |                   | Ирина Судакова |             | master     | sudakova.i.fe@sberbank.ru   |       1629695770003 |                               |            0 |
| 6d6a0745-75ff-448c-b2e4-d649a686aeac | dyakova.lawyer@bk.ru        | dyakova.lawyer@bk.ru                 | f                | t         |                   | Екатерина      |             | master     | dyakova.lawyer@bk.ru        |       1629992255065 |                               |            0 |
| 53952685-3fd0-4304-979f-74147f615224 |                             | be8b5bbc-179c-4a3c-a9a3-4aad28949808 | f                | t         |                   | Анзор          |             | master     | +79652200552                |       1631363298752 |                               |            0 |
| 0657ac85-c63f-489e-8b0f-62366c6f5f9d |                             |                                      | f                | t         |                   | Leonid         | Mogilevskiy | master     | +79852527976                |       1597922297510 |                               |            0 |
| efc2cbad-840e-44b6-8b92-dcc1ef0bf873 |                             | e7bf7363-8f7d-402a-a5d9-4ce1df9f931d | f                | t         |                   | Мария          |             | master     | +79154656155                |       1630586609766 |                               |            0 |
| a0cab916-7dcb-4794-b509-af348fdd0fae | ivan.solotenkov@mail.ru     | ivan.solotenkov@mail.ru              | t                | t         |                   | ivan           |             | master     | ivan.solotenkov@mail.ru     |       1631363436284 |                               |            0 |
| f9b85ebb-d6c9-4620-b1c2-8bf785ebd53b | shakhov-e131@yandex.ru      | shakhov-e131@yandex.ru               | t                | t         |                   | Артем          |             | master     | shakhov-e131@yandex.ru      |       1630668266960 |                               |            0 |
| b5f9ac5e-2744-41c2-a494-3536a432e003 | solnug@mail.ru              | solnug@mail.ru                       | t                | t         |                   | АНАСТАСИЯ      | БУШМАН      | master     | solnug@mail.ru              |       1631610696398 |                               |            0 |
| 7e74423b-5de7-43a7-b534-6fbcafad02de | anov.an@list.ru             | anov.an@list.ru                      | t                | t         |                   | Тесленко       | Андрей      | master     | anov.an@list.ru             |       1631359697330 |                               |            0 |
| 24e810fc-f621-45ac-b827-619ad8203ae7 | advokat@advokat.com         | advokat@advokat.com                  | f                | t         |                   | advokat        | advokat     | master     | advokat@advokat.com         |       1600086775813 |                               |            0 |
| 44f5e9c7-1f26-4e5c-94be-96aa6557cc22 | a.kardanov@mail.ru          | a.kardanov@mail.ru                   | t                | t         |                   | Анзор          |             | master     | a.kardanov@mail.ru          |       1631363610635 |                               |            0 |
| 34b881f9-e0ab-4042-8340-4805de9f5717 | y.korukhova@ya.ru           | y.korukhova@ya.ru                    | t                | t         |                   | ЮЛИЯ           | КОРУХОВА    | master     | y.korukhova@ya.ru           |       1631437821442 |                               |            0 |
| 223f2d2c-3d66-4549-b4a8-cb0ecdab507d | denis-teryaev@yandex.ru     | denis-teryaev@yandex.ru              | t                | t         |                   | ДЕНИС          | ТЕРЯЕВ      | master     | denis-teryaev@yandex.ru     |       1631610700431 |                               |            0 |
| 8cc4605e-6feb-4ab2-85bf-2cfae173b8ac | popova.popovatv@yandex.ru   | popova.popovatv@yandex.ru            | t                | t         |                   | ТАТЬЯНА        | ПОПОВА      | master     | popova.popovatv@yandex.ru   |       1631595180588 |                               |            0 |
| db0ba93c-1c79-4122-b9fb-88b8aa3f4fdc |                             | a946a7c0-281b-4f0f-bb09-c85ba5f0897c | f                | t         |                   | Анастасия      |             | master     | +79295005126                |       1631610209883 |                               |            0 |
| d82f08fd-9d8f-4e51-9a4f-14347a43aaf1 |                             | 7ce3538f-d531-4b3f-99ce-eeca7c21f8c5 | f                | t         |                   | Максим         |             | master     | +79276168772                |       1631610594931 |                               |            0 |
| d3fe66e3-3846-4b86-91df-f5739b0106aa | lawyer04@amulex.ru          | lawyer04@amulex.ru                   | f                | t         |                   | Юридическая    |             | master     | lawyer04@amulex.ru          |       1630485043942 |                               |   1674217384 |
| 840d7d06-4523-4cd1-b45e-da536b4c2c8c | lena.pozdnyakova.94@mail.ru | lena.pozdnyakova.94@mail.ru          | t                | t         |                   | ЕЛЕНА          | ЗЫБЕНКО     | master     | lena.pozdnyakova.94@mail.ru |       1631610595030 |                               |            0 |
| 4928a7ed-4281-4f9b-9f7a-ec950cd55dee | juliamart2013@yandex.ru     | juliamart2013@yandex.ru              | t                | t         |                   | Юлия           |             | master     | juliamart2013@yandex.ru     |       1631610618835 |                               |            0 |
```

> - Code name: index_0096
> - File path: SberPravo_user2.csv
> - Total rows: 119343

### Schema
```
root
 |-- id: string (nullable = true)
 |-- email: string (nullable = true)
 |-- birthdate: string (nullable = true)
 |-- user_types_id: string (nullable = true)
 |-- islive: string (nullable = true)
 |-- bonuses: string (nullable = true)
 |-- account: integer (nullable = true)
 |-- avatar: string (nullable = true)
 |-- suppliers_id: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- locality: string (nullable = true)
 |-- legal_entity: integer (nullable = true)
 |-- comment: string (nullable = true)
 |-- registration_date: date (nullable = true)
 |-- full_access: string (nullable = true)

```

### Data sample
```
| id                                   | email                      | birthdate   | user_types_id   | islive   | bonuses   |   account | avatar   | suppliers_id   | first_name        | last_name    | middle_name   | locality   |   legal_entity | comment   | registration_date   | full_access   |
|:-------------------------------------|:---------------------------|:------------|:----------------|:---------|:----------|----------:|:---------|:---------------|:------------------|:-------------|:--------------|:-----------|---------------:|:----------|:--------------------|:--------------|
| 9c2fad20-48d5-4311-8a9b-73fa99b37544 |                            |             |                 |          |           |       nan |          |                | Дуйэн исполнитель | Ис           |               |            |            nan |           | 2021-08-22          | f             |
| 966fa8e9-7207-49fc-8503-d051ea3bb1c5 | uly.test1@yandex.ru        |             |                 |          |           |       nan |          |                | Ульяна            |              |               |            |            nan |           | 2021-08-26          | f             |
| 1f0e04c5-b5d0-4e70-bdce-c339343a8bdf |                            |             |                 |          |           |       nan |          |                | Мадина            |              |               |            |            nan |           | 2021-09-03          | f             |
| cb285145-2134-4475-834b-7e4b54527090 | t.bobohanova@gmail.com     | 1988-05-31  |                 |          |           |       nan |          |                | Тамара            | Бобохонова   | Владимировна  |            |            nan |           | 2021-09-03          | f             |
| d472f5ad-d3ca-4a48-8a2d-4d733c0b4435 | zakazchikova.2021@mail.ru  |             |                 |          |           |       nan |          |                | Марина            |              |               |            |            nan |           | 2021-09-10          | f             |
| d98f4bac-f5ec-4c3e-9ae2-fd980a348665 | lawyer07@amulex.ru         | 1980-01-01  |                 |          |           |       nan |          |                | Юридическая       | Национальная | Служба        |            |            nan |           | 2021-09-01          | t             |
| 2af8fb4d-627c-46e5-9b9c-1a66c3bb5968 | 4shulga@gmail.com          |             |                 |          |           |       nan |          |                | СЕРГЕЙ            | ШУЛЬГА       |               |            |            nan |           | 2021-09-11          | f             |
| da8a7268-a7fa-4c74-a301-9f67b8c50213 | lawyer15@amulex.ru         | 1980-01-01  |                 |          |           |       nan |          |                | Юридическая       | Национальная | Служба        |            |            nan |           | 2021-09-01          | t             |
| ba42a722-af51-4855-bca5-903aeaf306ad | obaalu@mail.ru             |             |                 |          |           |       nan |          |                | ОЛЕГ              | БАУЛИН       |               |            |            nan |           | 2021-09-11          | f             |
| a07a972a-f0c6-477c-906c-f357f759bc06 | ilya@agienko.ru            |             |                 |          |           |       nan |          |                | Илья              |              |               |            |            nan |           | 2021-09-11          | f             |
| dae1ed15-17d2-415f-b1f7-ddda3df93ac3 |                            |             |                 |          |           |       nan |          |                | ИринаС            |              |               |            |            nan |           | 2021-09-13          | f             |
| 42d07340-a86a-4102-a241-396c6346f1b5 | tolmacheov@narod.ru        |             |                 |          |           |       nan |          |                | ИГОРЬ             | ТОЛМАЧЕВ     |               |            |            nan |           | 2021-09-14          | f             |
| 53da8f9c-6d17-474b-a2d2-eea303b8e9a7 | vladimir.kirishev@mail.ru  |             |                 |          |           |       nan |          |                | ВЛАДИМИР          | КИРИШЕВ      |               |            |            nan |           | 2021-09-14          | f             |
| ef957fa1-c3bd-4d32-929f-51505f97911b | juchkova.2012@gmail.com    |             |                 |          |           |       nan |          |                | ЮЛИЯ              | ЖУЧКОВА      |               |            |            nan |           | 2021-09-14          | f             |
| 71f6be80-5212-4eec-a197-0120faa2228a | genlok1995@mail.ru         | 1995-01-08  |                 |          |           |       nan |          |                | МИХАИЛ            | ИГНАТОВ      | Владимирович  |            |            nan |           | 2021-09-14          | f             |
| 8dcfd913-0f88-4d09-ac2c-f0d98b9e49ab |                            |             |                 |          |           |       nan |          |                | АНДРЕЙ            | КОБОЗЕВ      |               |            |            nan |           | 2021-09-14          | f             |
| 4a9ff6f5-f57f-4feb-b966-9a2992138a73 | ustimenko98@gmail.com      |             |                 |          |           |       nan |          |                | НИКИТА            | УСТИМЕНКО    |               |            |            nan |           | 2021-09-14          | f             |
| 6b3439d8-63f1-4bd2-ae0d-2c5929b02fc0 | aristov.2011@gmail.com     |             |                 |          |           |       nan |          |                | АЛЕКСАНДР         | АРИСТОВ      |               |            |            nan |           | 2021-09-14          | f             |
| b8ece0ed-0265-4d69-b26a-ba79cdc903d9 | aekalutskaya@sberbank.ru   |             |                 |          |           |       nan |          |                | Анастасия         |              |               |            |            nan |           | 2021-09-14          | f             |
| 77d6481f-ca77-4e5c-b531-7a5d9712534a | gudkov.p.aleks@sberbank.ru |             |                 |          |           |       nan |          |                | Павел             |              |               |            |            nan |           | 2021-09-14          | f             |
```

> - Code name: index_0096
> - File path: SberPravo_userphone.csv
> - Total rows: 115360

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- phone: long (nullable = true)
 |-- phone_type: integer (nullable = true)
 |-- users_id: string (nullable = true)
 |-- preferred: string (nullable = true)
 |-- description: string (nullable = true)

```

### Data sample
```
|   id |       phone |   phone_type | users_id                             | preferred   | description   |
|-----:|------------:|-------------:|:-------------------------------------|:------------|:--------------|
|  146 | 79274314255 |            1 | 6da1a628-2e87-479c-a4fc-b59a33cd2ac7 | t           |               |
|  143 | 79819478283 |            1 | 84f33582-90c4-45de-a478-8d9f56296e0e | t           |               |
|  144 | 79151120993 |            1 | 900d5cfa-df32-4036-a95e-cd69167b29e0 | t           |               |
|  142 | 79061293539 |            1 | ec01c811-89fa-4c58-91ed-98ec3f7517c9 | t           |               |
|  145 | 79169738141 |            1 | fb8b64e0-6d64-4dd4-b616-5709cb9be7c0 | t           |               |
|  147 | 79250061163 |            1 | cf814cb3-2480-4473-b451-119e34aa69bf | t           |               |
|  148 | 79998045931 |            1 | 245cf1af-0ffe-4907-9c1b-27f430ad0802 | t           |               |
|  149 | 79210998064 |            1 | e8a896f6-6d7f-42a6-927e-c6ad7bf8a9ec | t           |               |
|  150 | 79999694520 |            1 | d4e659b3-ea87-47d4-ab20-7a64747509d2 | t           |               |
|  151 | 79119266062 |            1 | 0280cfb3-e78f-4c1a-a5f2-358598eda04c | t           |               |
|  152 | 79169738836 |            1 | c1a3c94b-6b17-46a8-a0b3-e44c76418ebe | t           |               |
|  153 | 79110197248 |            1 | 61c35f72-6695-4ffb-b9cb-d66929d3fc9a | t           |               |
|  154 | 79067020276 |            1 | ed412c68-2426-41d2-8ac8-587ca490fb6f | t           |               |
|  155 | 79272635761 |            1 | abe9298d-b254-4ff0-86b6-0da57e4a1747 | t           |               |
|  156 | 79998045931 |            1 | 2dee4dc2-2913-40d3-8842-cbfb5c90238e | t           |               |
|  157 | 79817592545 |            1 | be5fe36b-6b82-44a1-8fae-8dd4a7cb0614 | t           |               |
|  158 | 79057544066 |            1 | cb285145-2134-4475-834b-7e4b54527090 | t           |               |
|  159 | 79252304642 |            1 | 1f0e04c5-b5d0-4e70-bdce-c339343a8bdf | t           |               |
|  160 | 79998613935 |            1 | c7b83cea-33b3-4a75-8a5c-78939920115c | t           |               |
|  161 | 79779711778 |            1 | d39e5a9f-a204-4c67-80b6-57f2f35b0cfb | t           |               |
```


## About final data
> - Total rows: 236213

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 60.04% |
| Phones | 96.55% |
| Birth_date | 1.11% |
| Accounts | 50.30% |
| Actuality | 49.64% |



### Data sample
```
| names                | emails                           | phones          | birth_date   | accounts                                                                                    | actuality   |
|:---------------------|:---------------------------------|:----------------|:-------------|:--------------------------------------------------------------------------------------------|:------------|
| ['Ирина Судакова']   | ['sudakova.i.fe@sberbank.ru']    |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='sudakova.i.fe@sberbank.ru')]    |             |
| ['Екатерина']        | ['dyakova.lawyer@bk.ru']         |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='dyakova.lawyer@bk.ru')]         |             |
| ['Ivan']             | ['ivan.solotenkov@mail.ru']      |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='ivan.solotenkov@mail.ru')]      |             |
| ['Артем']            | ['shakhov-e131@yandex.ru']       |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='shakhov-e131@yandex.ru')]       |             |
| ['Бушман Анастасия'] | ['solnug@mail.ru']               | ['79188076224'] |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='solnug@mail.ru')]               |             |
| ['Андрей Тесленко']  | ['anov.an@list.ru']              | ['79852171733'] |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='anov.an@list.ru')]              |             |
| ['Advokat Advokat']  | ['advokat@advokat.com']          |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='advokat@advokat.com')]          |             |
| ['Анзор']            | ['a.kardanov@mail.ru']           |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='a.kardanov@mail.ru')]           |             |
| ['Корухова Юлия']    | ['y.korukhova@ya.ru']            | ['79151087650'] |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='y.korukhova@ya.ru')]            |             |
| ['Теряев Денис']     | ['denis-teryaev@yandex.ru']      | ['79268798814'] |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='denis-teryaev@yandex.ru')]      |             |
| ['Попова Татьяна']   | ['popova.popovatv@yandex.ru']    | ['79505253050'] |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='popova.popovatv@yandex.ru')]    |             |
| ['Анастасия']        |                                  | ['79295005126'] |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='+79295005126')]                 |             |
| ['Максим']           |                                  | ['79276168772'] |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='+79276168772')]                 |             |
| ['Юридическая']      | ['lawyer04@amulex.ru']           |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='lawyer04@amulex.ru')]           |             |
| ['Зыбенко Елена']    | ['lena.pozdnyakova.94@mail.ru']  | ['79167435394'] |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='lena.pozdnyakova.94@mail.ru')]  |             |
| ['Юлия']             | ['juliamart2013@yandex.ru']      |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='juliamart2013@yandex.ru')]      |             |
| ['Юридическая']      | ['lawyer02@amulex.ru']           |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='lawyer02@amulex.ru')]           |             |
| ['Макарова Галина']  | ['makarova.g.aleks@sberbank.ru'] |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='makarova.g.aleks@sberbank.ru')] |             |
| ['Юридическая']      | ['lawyer05@amulex.ru']           |                 |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='lawyer05@amulex.ru')]           |             |
| ['Горчаков Никита']  | ['arsykers@gmail.com']           | ['79261547831'] |              | [Row(title='СберПраво', link='https://sberpravo.ru', login='arsykers@gmail.com')]           |             |
```