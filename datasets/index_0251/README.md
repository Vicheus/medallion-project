# Parsetron results

## About row data

> - Code name: index_0251
> - File path: /home/user/Documents/data/index_0251/raw/familyspace_ru.csv
> - Total rows: 7685607

### Schema
```
root
 |-- n"email": string (nullable = true)
 |-- password: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- maiden_name: string (nullable = true)
 |-- _c6: string (nullable = true)

```

### Data sample
```
| n"email"             | password                         | first_name   | last_name   | middle_name   | maiden_name   | _c6   |
|:---------------------|:---------------------------------|:-------------|:------------|:--------------|:--------------|:------|
| georgy@shabashev.ru  | 29c7726263da5fcfbd914768eafe80b4 | Георгий      | Шабашев     | Александрович | Шабашов       |       |
|                      |                                  | Александр    | Шабашев     | Павлович      |               |       |
| av-zharkov@yandex.ru | b478c3654f894728698dde9de46d123d | Алексей      | Жарков      | Владимирович  |               |       |
|                      |                                  | Елена        | Шабашева    | Васильевна    | Заренина      |       |
|                      |                                  |              |             |               |               |       |
|                      |                                  | Тамара       | Жаркова     | Николаевна    |               |       |
| vv-zharkov@yandex.ru | aebbbe214bf3a1dc564033055c30c1aa | Владимир     | Жарков      | Васильевич    |               |       |
|                      |                                  | Инна         | Колчина     | Владимировна  | Жаркова       |       |
| zubenator@gmail.com  | d8578edf8458ce06fbc5bb76a58c5ca4 | Александр    | Зубарев     | Федорович     |               |       |
| aermina@mail.ru      | 6f66faea7ceb8304fe89f4fb97203696 | Анна         | Лещинская   | Юрьевна       | Ерёмина       |       |
| wr-alphaX@yandex.ru  | 08fb22f1949620c2a579e8b7a4031b8a | Анатолий     | Бакшеев     | Станиславович |               |       |
|                      |                                  | Юрий         | Ерёмин      | Андреевич     |               |       |
|                      |                                  | Татьяна      | Ерёмина     | Михайловна    |               |       |
|                      |                                  | Елена        | Школьнова   | Юрьевна       |               |       |
|                      |                                  | Алексей      | Ерёмин      | Юрьевич       |               |       |
|                      |                                  |              |             |               |               |       |
| ivan@romanov.nnov.ru | 9f8c239e9fa7b6f90285fc4ef77c7f2d | Иван         | Романов     | Александрович |               |       |
|                      |                                  | Вера         | Романова    | Николаевна    |               |       |
|                      |                                  | Раиса        | Захарченко  | Тихоновна     | Попова        |       |
|                      |                                  | Агриппина    | Попова      | Петровна      | Ургапова      |       |
```


## About final data
> - Total rows: 1434730

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```

### Data sample
```
| names                                 | emails                       | accounts                                                                                                                                             |
|:--------------------------------------|:-----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Шабашев Георгий Александрович']     | ['georgy@shabashev.ru']      | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='georgy@shabashev.ru', password_hash='29c7726263da5fcfbd914768eafe80b4')]      |
| ['Жарков Алексей Владимирович']       | ['av-zharkov@yandex.ru']     | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='av-zharkov@yandex.ru', password_hash='b478c3654f894728698dde9de46d123d')]     |
| ['Жарков Владимир Васильевич']        | ['vv-zharkov@yandex.ru']     | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='vv-zharkov@yandex.ru', password_hash='aebbbe214bf3a1dc564033055c30c1aa')]     |
| ['Зубарев Александр Федорович']       | ['zubenator@gmail.com']      | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='zubenator@gmail.com', password_hash='d8578edf8458ce06fbc5bb76a58c5ca4')]      |
| ['Лещинская Анна Юрьевна']            | ['aermina@mail.ru']          | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='aermina@mail.ru', password_hash='6f66faea7ceb8304fe89f4fb97203696')]          |
| ['Бакшеев Анатолий Станиславович']    | ['wr-alphax@yandex.ru']      | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='wr-alphax@yandex.ru', password_hash='08fb22f1949620c2a579e8b7a4031b8a')]      |
| ['Романов Иван Александрович']        | ['ivan@romanov.nnov.ru']     | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='ivan@romanov.nnov.ru', password_hash='9f8c239e9fa7b6f90285fc4ef77c7f2d')]     |
| ['Колчин Алексей Вячеславович']       | ['alexey_kolchin@yahoo.com'] | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='alexey_kolchin@yahoo.com', password_hash='7d2918da9b2079b11488817872133bce')] |
| ['Пупкин Иван Васильевич']            | ['andreistas@yandex.ru']     | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='andreistas@yandex.ru', password_hash='ff48e4cd37a9c7a2010b6ecf43512698')]     |
| ['Петрова Анна Игоревна']             | ['diona-go@mail.ru']         | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='diona-go@mail.ru', password_hash='29b9c26a50b95b22fc89c175d8b82531')]         |
| ['Apalachy Apalachy Apalachy']        | ['kenji-2007@yandex.ru']     | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='kenji-2007@yandex.ru', password_hash='85f99165d60d7b985436bea643de6e13')]     |
| ['Мищенко Валерий Владимирович']      | ['sixpence@mail.ru']         | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='sixpence@mail.ru', password_hash='27385860148d04797a6585ad887dc290')]         |
| ['Евтеева Ольга Валерьевна']          | ['o.evteeva@mail.ru']        | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='o.evteeva@mail.ru', password_hash='925d7518fc597af0e43f5606f9a51512')]        |
| ['Александрова Инесса Владиславовна'] | ['inessa@pilotik.ru']        | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='inessa@pilotik.ru', password_hash='83b751a79d983368e9ab8f39d018cccb')]        |
| ['Евтеева Евгения Сергеевна']         | ['jaena@mail.ru']            | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='jaena@mail.ru', password_hash='95ddc519cb59d79df805d27ab6dddc18')]            |
| ['Алексеева Наталья Владимировна']    | ['ncherry2003@mail.ru']      | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='ncherry2003@mail.ru', password_hash='88abfd078061fe0a30684649319fcde4')]      |
| ['Евтеев Павел Сергеевич']            | ['pashavesna@mail.ru']       | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='pashavesna@mail.ru', password_hash='201f5e53a16b8e40d2776dd6fce80e8c')]       |
| ['Илиев Павел Иванович']              | ['pavel.iliev@mail.ru']      | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='pavel.iliev@mail.ru', password_hash='5719ba50ad8dc4d843c56afc693d5641')]      |
| ['Шакирова Анна Арсеновна']           | ['anna.shakirova@gmail.com'] | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='anna.shakirova@gmail.com', password_hash='760df2de870a25a8dbe7d393ad3faf30')] |
| ['Княгинин Дмитрий Валентинович']     | ['knyaz@aaanet.ru']          | [Row(title='Familyspace', link='https://familyspace.ru/login/', login='knyaz@aaanet.ru', password_hash='daa14caeacb081b59b1a7a409d086a71')]          |
```