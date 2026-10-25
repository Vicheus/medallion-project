# Parsetron results

## About row data

> - Code name: index_0127
> - File path: /media/user/TRANSCEND/Databases/index_0127/raw/preprocessed/user_info_2_preprocessed.csv
> - Total rows: 65630

### Schema
```
root
 |-- USER_ID: string (nullable = true)
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
|   USER_ID | username     | password_hash                                                                                              | first_name   | last_name   | middle_name   | email                    | gender   |   phone | birth_date   |
|----------:|:-------------|:-----------------------------------------------------------------------------------------------------------|:-------------|:------------|:--------------|:-------------------------|:---------|--------:|:-------------|
|         1 | admin        | $6$w1X9HyJ9c75ZKHlM$hV16XAfWGQMJA1hC7q4rGexXJo8Y16XaoNGH7QL42dQFuW98kYHC7IANkBhrs.BzZXmoPZZY9jX8/NV0EoQrQ/ | Михаил       |             |               | ishekov@mail.ru          |          |     nan |              |
|         4 | +79323210924 | $e7VpW_3df3a8c2b49eebab7b748c0de8874c74a                                                                   | Инесса       |             |               | inessa.zelin91@mail.ru   |          |     nan |              |
|         6 | +79324707974 | 5nYuTs1Z67ea5dbcd3ab7dd85b9e734bb509a218                                                                   | Яна          |             |               | Yana_Kholomeeva@mail.ru  |          |     nan |              |
|         7 | +79116579050 | fZ7A63Wk74f841ff0e5c3b02d333c6428dd9bdca                                                                   | Арне         |             |               | arne.salo@mail.ru        |          |     nan |              |
|        17 | +79027002297 | ;i1UFm1,63286e7d0496cfd7a2c0b146db377e3b                                                                   | Елена        |             |               | elena.k8611@gmail.com    |          |     nan |              |
|        22 | +79600081215 | F1TQp5GA2fc4f59ca76e6d000f055560a1a41ad7                                                                   | виталий      |             |               | admin@mkcompany.ru       |          |     nan |              |
|        24 | +79226861633 | qbiy5APn0d6c970dd100016507e72d4fd60f23ef                                                                   | Анатолий     |             |               | ansobol55@yandex.ru      |          |     nan |              |
|        26 | +79115886772 | 5eKvSLdNb68fc032410f5d0e8286932bc879132e                                                                   | Дарья        |             |               | ko4urova.darya@yandex.ru |          |     nan |              |
|        27 | +79021989353 | VfKiugdYad05eb3cdc3e0f255874615a399acfd2                                                                   | Юлия         |             |               | djulia2010@mail.ru       |          |     nan |              |
|        33 | +79058730373 | #dB0!iC5b5162f24432eeac8b8b815f9e08b8a18                                                                   | Светлана     |             |               | selena11-82@mail.ru      |          |     nan |              |
```

> - Code name: index_0127
> - File path: /media/user/TRANSCEND/Databases/index_0127/raw/preprocessed/user_info_3_preprocessed.csv
> - Total rows: 49567

### Schema
```
root
 |-- USER_ID: integer (nullable = true)
 |-- name2: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- phone3: string (nullable = true)

```

### Data sample
```
|   USER_ID | name2                       | email2                  | phone3             |
|----------:|:----------------------------|:------------------------|:-------------------|
|     39816 | Евгений Ермолин             | DemzAZ@gmail.com        | +7 (911) 653-89-93 |
|      9067 | Белозерова Анна Анатольевна | belozerovaaa@inbox.ru   | +7 (911) 565-57-88 |
|        17 | Комиссарова Елена Павловна  | elena.k8611@gmail.com   | +7 (902) 700-22-97 |
|     38991 | Татьяна                     | kirill.bagrow@yandex.ru | +7 (911) 590-42-86 |
|     28968 | Яже                         | kirill.bagrow@yandex.ru | +7 (911) 659-18-52 |
|     10142 | Ольга Котова                | o.kotova@mkcompany.ru   | +7 (911) 564-01-94 |
|     29824 | Юлия                        | Yulik_07@list.ru        | +7 (906) 285-18-18 |
|     41847 | Дмитрий                     | Vilovaanna@gmail.com    | +7 (960) 013-80-91 |
|        27 | Косцова Юлия Павловна       | djulia2010@mail.ru      | +7 (902) 198-93-53 |
|     40805 | Нина Николаевна Вепрева     | sala-mandrra@mail.ru    | +7 (918) 918-03-20 |
```


## About final data
> - Total rows: 49106

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```

### Data sample
```
| names                                    | emails                     | phones          |   sex | birth_date   | accounts                                                                                                                                 |
|:-----------------------------------------|:---------------------------|:----------------|------:|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| ['Ольга']                                | ['2405_olga@mail.ru']      | ['79116752873'] |   nan |              | [Row(title='Добрая аптека', link='https://d-apteka.ru/', login='79116752873', password_hash='FwgRb0jU2336dc045b0279d359584976030606ee')] |
| ['Ольга', 'Ольга Александровна Козлова'] | ['poroduk@yandex.ru']      | ['79115636361'] |   nan |              | [Row(title='Добрая аптека', link='https://d-apteka.ru/', login='79115636361', password_hash='6dCIbZ7Obc8ff7a7cca00ca1244b47e90a2b641a')] |
| ['Ирина']                                | ['ira504010@rambler.ru']   | ['79539340958'] |   nan |              | [Row(title='Добрая аптека', link='https://d-apteka.ru/', login='79539340958', password_hash='wPXtPrRlb8fc933833bd8081255c8c230cef444e')] |
| ['Елена']                                | ['klin-l@mail.ru']         | ['79314095407'] |   nan |              | [Row(title='Добрая аптека', link='https://d-apteka.ru/', login='79314095407', password_hash='YAEodpI839db5fd5ccf86aed50fa5ce90e25b199')] |
| ['Наталья']                              | ['manej76@mail.ru']        | ['79115511983'] |   nan |              | [Row(title='Добрая аптека', link='https://d-apteka.ru/', login='79115511983', password_hash='pTmzj6Hffde7f5fbfb9c9dfa999d0835460448a7')] |
| ['Тамара']                               | ['ryghyk81@yandex.ru']     | ['79052937682'] |   nan |              | [Row(title='Добрая аптека', link='https://d-apteka.ru/', login='79052937682', password_hash='mfMzf4qE299389c809048894b854f834fe5a34ff')] |
| ['Людмила']                              | ['d.a.n84@mail.ru']        | ['79115692237'] |   nan |              | [Row(title='Добрая аптека', link='https://d-apteka.ru/', login='79115692237', password_hash='VlK5AKzB02c9d26b84ee199930f64a0e9e61b5a5')] |
| ['Ольга']                                | ['olga.galich@mail.ru']    | ['79021974193'] |   nan |              | [Row(title='Добрая аптека', link='https://d-apteka.ru/', login='79021974193', password_hash='jI6X0ldK20063a65f69737041c8acf50b76bd9cf')] |
| ['Екатерина']                            | ['tigrusha860627@mail.ru'] | ['79021994086'] |   nan |              | [Row(title='Добрая аптека', link='https://d-apteka.ru/', login='79021994086', password_hash='Tv}5nO]597526d59c445265b8730c61c4618b7c3')] |
| ['Переклад', 'Михаил Переклад']          | ['pereklad87@gmail.com']   | ['79062826445'] |   nan |              | [Row(title='Добрая аптека', link='https://d-apteka.ru/', login='79062826445', password_hash='1r3fqTYp838e1a4466c4ada5f779ef90ffb1c13c')] |
```