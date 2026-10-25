# Parsetron results

## About row data

> - Code name: index_0134
> - File path: /media/user/TRANSCEND/Databases/index_0134/raw/BigSMM.ru - @StormInDatBase/users_info_preprocessed.csv
> - Total rows: 34338

### Schema
```
root
 |-- login: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- pass: string (nullable = true)
 |-- email: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- last_activity_date: timestamp (nullable = true)
 |-- phones: string (nullable = true)
 |-- qiwi1: long (nullable = true)
 |-- qiwi2: long (nullable = true)
 |-- yandex1: long (nullable = true)
 |-- yandex2: long (nullable = true)

```

### Data sample
```
| login        | first_name   | last_name    | pass                             | email                    | ip             | last_activity_date   | phones   |   qiwi1 |   qiwi2 |   yandex1 |   yandex2 |
|:-------------|:-------------|:-------------|:---------------------------------|:-------------------------|:---------------|:---------------------|:---------|--------:|--------:|----------:|----------:|
| danilbastard | Данил        | Куликов      | 29bbfef41fcf9f482ba2c4e8b0f4acb2 | danilbastard1@mail.ru    | 109.254.192.55 | NaT                  |          |     nan |     nan |       nan |       nan |
| ismail       | Ismail       | Raxmatov     | 85fdf2d864506ce1053607b5f0f0c5b8 | bonbon.ses@mail.ru       | 5.19.3.156     | NaT                  |          |     nan |     nan |       nan |       nan |
| CSGORAZER    | Nekit333     | Kekov        | e07f428d68d38764c0f8553561a229dc | Kicker-jenya@mail.ru     | 185.132.28.12  | NaT                  |          |     nan |     nan |       nan |       nan |
| youngjake    | Nick         | Skott        | f9e3973d777935a23ec2b6e746b21cfe | wolfhackgaming@gmail.com | 37.230.243.86  | NaT                  |          |     nan |     nan |       nan |       nan |
| evilmoto     | Кирилл       | Сафинков     | 897c8fde25c5cc5270cda61425eed3c8 | evil_moto@mail.ru        | 90.151.94.230  | 2024-02-06 20:13:07  |          |     nan |     nan |       nan |       nan |
| allen263     | Сергей       | Катышев      | 768c927b5a96f0a33efe5fc470b4b404 | allen_walker263@mail.ru  | 176.59.51.166  | NaT                  |          |     nan |     nan |       nan |       nan |
| H0yMFU       | Владислав    | Пупынин      | 62548964ddee8b78817bb5ee3599add1 | punyaaa007@gmail.com     | 87.224.252.52  | NaT                  |          |     nan |     nan |       nan |       nan |
| Santimw      |              |              | 1cea936d34f22460eebe15d2db9036f5 | santimw@gmail.com        | 95.25.205.221  | NaT                  |          |     nan |     nan |       nan |       nan |
| wingfield    | Владимир     | Путин        | a252d9f291a8d7b7c862c7eb71f7ddb7 | t.wingfield@yandex.com   | 46.246.119.226 | 2024-04-08 11:16:32  |          |     nan |     nan |       nan |       nan |
| Dimaradvin   | Дима         | Радзиховский | b23ef7d9ff93ea98faf6eaea4f792b1f | Dimaradvin@gmail.com     | 93.75.163.114  | NaT                  |          |     nan |     nan |       nan |       nan |
```


## About final data
> - Total rows: 30137

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- financials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- card_number: string (nullable = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Data sample
```
| names                 | emails                       | financials   | ips                                   | accounts                                                                                                                | phones   |
|:----------------------|:-----------------------------|:-------------|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------------|:---------|
| ['Куликов Данил']     | ['danilbastard1@mail.ru']    |              | [Row(ip='109.254.192.55', date=None)] | [Row(title='BigSMM', link='https://bigsmm.ru', login='danilbastard', password_hash='29bbfef41fcf9f482ba2c4e8b0f4acb2')] |          |
| ['Raxmatov Ismail']   | ['bonbon.ses@mail.ru']       |              | [Row(ip='5.19.3.156', date=None)]     | [Row(title='BigSMM', link='https://bigsmm.ru', login='ismail', password_hash='85fdf2d864506ce1053607b5f0f0c5b8')]       |          |
| ['Skott Nick']        | ['wolfhackgaming@gmail.com'] |              | [Row(ip='37.230.243.86', date=None)]  | [Row(title='BigSMM', link='https://bigsmm.ru', login='youngjake', password_hash='f9e3973d777935a23ec2b6e746b21cfe')]    |          |
| ['Сафинков Кирилл']   | ['evil_moto@mail.ru']        |              | [Row(ip='90.151.94.230', date=None)]  | [Row(title='BigSMM', link='https://bigsmm.ru', login='evilmoto', password_hash='897c8fde25c5cc5270cda61425eed3c8')]     |          |
| ['Катышев Сергей']    | ['allen_walker263@mail.ru']  |              | [Row(ip='176.59.51.166', date=None)]  | [Row(title='BigSMM', link='https://bigsmm.ru', login='allen263', password_hash='768c927b5a96f0a33efe5fc470b4b404')]     |          |
| ['Пупынин Владислав'] | ['punyaaa007@gmail.com']     |              | [Row(ip='87.224.252.52', date=None)]  | [Row(title='BigSMM', link='https://bigsmm.ru', login='H0yMFU', password_hash='62548964ddee8b78817bb5ee3599add1')]       |          |
| ['Путин Владимир']    | ['t.wingfield@yandex.com']   |              | [Row(ip='46.246.119.226', date=None)] | [Row(title='BigSMM', link='https://bigsmm.ru', login='wingfield', password_hash='a252d9f291a8d7b7c862c7eb71f7ddb7')]    |          |
| ['Радзиховский Дима'] | ['dimaradvin@gmail.com']     |              | [Row(ip='93.75.163.114', date=None)]  | [Row(title='BigSMM', link='https://bigsmm.ru', login='Dimaradvin', password_hash='b23ef7d9ff93ea98faf6eaea4f792b1f')]   |          |
| ['White Mitch']       | ['dimka71z@bk.ru']           |              | [Row(ip='95.139.175.78', date=None)]  | [Row(title='BigSMM', link='https://bigsmm.ru', login='WhiteCat', password_hash='b0b3e4f0f687b561c93c50590bbe7d39')]     |          |
| ['Rodionova Marina']  | ['res-mar@mail.ru']          |              | [Row(ip='139.47.4.93', date=None)]    | [Row(title='BigSMM', link='https://bigsmm.ru', login='resmar', password_hash='d659acc617ed323fe8438ab1f2be6876')]       |          |
```