# Parsetron results

## About row data

> - Code name: index_0125
> - File path: /media/user/TRANSCEND/Databases/index_0125/raw/preprocessed/*.csv
> - Total rows: 7200360

### Schema
```
root
 |-- ID: string (nullable = true)
 |-- LOGIN: string (nullable = true)
 |-- PASSWORD: string (nullable = true)
 |-- NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- PERSONAL_GENDER: string (nullable = true)
 |-- PERSONAL_PHONE: string (nullable = true)
 |-- PERSONAL_STREET: string (nullable = true)
 |-- PERSONAL_CITY: string (nullable = true)
 |-- PERSONAL_STATE: string (nullable = true)
 |-- WORK_COMPANY: string (nullable = true)
 |-- PERSONAL_BIRTHDAY: string (nullable = true)
 |-- SECOND_NAME: string (nullable = true)

```

### Data sample
```
|      ID | LOGIN                                 | PASSWORD                                 | NAME     | LAST_NAME   | EMAIL                                 | PERSONAL_GENDER   | PERSONAL_PHONE    | PERSONAL_STREET   | PERSONAL_CITY   | PERSONAL_STATE   | WORK_COMPANY   | PERSONAL_BIRTHDAY   | SECOND_NAME   |
|--------:|:--------------------------------------|:-----------------------------------------|:---------|:------------|:--------------------------------------|:------------------|:------------------|:------------------|:----------------|:-----------------|:---------------|:--------------------|:--------------|
| 8349991 | 444438j8hqkvim6h1716@mail.pampadu.com | qLN1Vx2044551b2b09f944ab19c3813f4947f681 | Леонид   | Парменов    | 444438j8hqkvim6h1716@mail.pampadu.com |                   | 79248942717       |                   |                 |                  |                | 1977-10-13          | Сергеевич     |
| 8349990 | nuxydo@mailto.plus                    | clRKJbJx57a0c6b4047dbb0a8e0fd408005f4f00 | АНАТОЛИЙ | ХАНБАБАБЕВ  | nuxydo@mailto.plus                    |                   | +79143795949      |                   |                 |                  |                | 1947-06-23          | МИРЗАБАБАЕВИЧ |
| 8349989 | 538karpova@mail.ru                    | 7rnymvJ41df8735f375a6fdf579b9100cd5a5153 | Алёна    | Карпова     | 538karpova@mail.ru                    |                   | +7(983) 418-03-54 |                   |                 |                  |                | 1983-06-21          | Михайловна    |
| 8349988 | panina.olga@mail.ru                   | 1qNrPuEe7b038eeef65ca84b3297ce5227d45c14 | Геннадий | Панин       | panina.olga@mail.ru                   |                   | +79263283363      |                   |                 |                  |                | 1962-09-05          | Евгеньевич    |
| 8349987 | Opalubovv@gmail.com                   | OtWauQ9ub15963241b6c553f78d454b22f709aed | Любовь   | Опарина     | opalubovv@gmail.com                   |                   | +79533065107      |                   |                 |                  |                | 1980-11-10          | Валерьевна    |
| 8349986 | ulya.gostraya.86@bk.ru                | dtLZ0mIo44fce8925b8f3e9e7f3962a61086be6e | Ульяна   | Гострая     | ulya.gostraya.86@bk.ru                |                   | +79280533055      |                   |                 |                  |                | 1986-11-05          | Анатольевна   |
| 8349985 | order-232152857@insmail3.sravni.ru    | 0F1tn9ky07ba1bd4581135ad695eeb8912a7fc60 | ТИМОФЕЙ  | НОСОВ       | order-232152857@insmail3.sravni.ru    |                   | 79167559781       |                   |                 |                  |                | 1976-11-23          | ВЛАДИМИРОВИЧ  |
| 8349984 | 6044513_2575876@osago.rosfines.ru     | u7HtdKwK0ef9cb6fa05f52b493a8c7514ff9c384 | Сергей   | Никонов     | 6044513_2575876@osago.rosfines.ru     |                   | 79263593009       |                   |                 |                  |                | 1981-05-10          | Михайлович    |
| 8349983 | tolyantolmach@gmail.com               | X0uv6dMN42f4abd628357829f90fbf2a3e187a1c | Анатолий | Толмачёв    | tolyantolmach@gmail.com               |                   | +79242111316      |                   |                 |                  |                | 1990-09-17          | Вячеславович  |
| 8349982 | order-232152458@insmail3.sravni.ru    | bxSzA0TZ133d6b75cc189521cce3c0d83657f3c1 | ТИМОФЕЙ  | НОСОВ       | order-232152458@insmail3.sravni.ru    |                   | 79167559781       |                   |                 |                  |                | 1976-11-23          | ВЛАДИМИРОВИЧ  |
```


## About final data
> - Total rows: 6870503

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
| names                                 | emails                                    | phones          | address   |   sex | birth_date   | works   | accounts                                                                                                                                                       |
|:--------------------------------------|:------------------------------------------|:----------------|:----------|------:|:-------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Парменов Леонид Сергеевич']         | ['444438j8hqkvim6h1716@mail.pampadu.com'] | ['79248942717'] |           |   nan | 13.01.1977   |         | [Row(title='АО СОГАЗ', link='https://www.sogaz.ru/', login='444438j8hqkvim6h1716@mail.pampadu.com', password_hash='qLN1Vx2044551b2b09f944ab19c3813f4947f681')] |
| ['Ханбабабев Анатолий Мирзабабаевич'] | ['nuxydo@mailto.plus']                    | ['79143795949'] |           |   nan | 23.01.1947   |         | [Row(title='АО СОГАЗ', link='https://www.sogaz.ru/', login='nuxydo@mailto.plus', password_hash='clRKJbJx57a0c6b4047dbb0a8e0fd408005f4f00')]                    |
| ['Карпова Алёна Михайловна']          | ['538karpova@mail.ru']                    | ['79834180354'] |           |   nan | 21.01.1983   |         | [Row(title='АО СОГАЗ', link='https://www.sogaz.ru/', login='538karpova@mail.ru', password_hash='7rnymvJ41df8735f375a6fdf579b9100cd5a5153')]                    |
| ['Панин Геннадий Евгеньевич']         | ['panina.olga@mail.ru']                   | ['79263283363'] |           |   nan | 05.01.1962   |         | [Row(title='АО СОГАЗ', link='https://www.sogaz.ru/', login='panina.olga@mail.ru', password_hash='1qNrPuEe7b038eeef65ca84b3297ce5227d45c14')]                   |
| ['Опарина Любовь Валерьевна']         | ['opalubovv@gmail.com']                   | ['79533065107'] |           |   nan | 10.01.1980   |         | [Row(title='АО СОГАЗ', link='https://www.sogaz.ru/', login='Opalubovv@gmail.com', password_hash='OtWauQ9ub15963241b6c553f78d454b22f709aed')]                   |
| ['Гострая Ульяна Анатольевна']        | ['ulya.gostraya.86@bk.ru']                | ['79280533055'] |           |   nan | 05.01.1986   |         | [Row(title='АО СОГАЗ', link='https://www.sogaz.ru/', login='ulya.gostraya.86@bk.ru', password_hash='dtLZ0mIo44fce8925b8f3e9e7f3962a61086be6e')]                |
| ['Носов Тимофей Владимирович']        | ['order-232152857@insmail3.sravni.ru']    | ['79167559781'] |           |   nan | 23.01.1976   |         | [Row(title='АО СОГАЗ', link='https://www.sogaz.ru/', login='order-232152857@insmail3.sravni.ru', password_hash='0F1tn9ky07ba1bd4581135ad695eeb8912a7fc60')]    |
| ['Никонов Сергей Михайлович']         | ['6044513_2575876@osago.rosfines.ru']     | ['79263593009'] |           |   nan | 10.01.1981   |         | [Row(title='АО СОГАЗ', link='https://www.sogaz.ru/', login='6044513_2575876@osago.rosfines.ru', password_hash='u7HtdKwK0ef9cb6fa05f52b493a8c7514ff9c384')]     |
| ['Толмачёв Анатолий Вячеславович']    | ['tolyantolmach@gmail.com']               | ['79242111316'] |           |   nan | 17.01.1990   |         | [Row(title='АО СОГАЗ', link='https://www.sogaz.ru/', login='tolyantolmach@gmail.com', password_hash='X0uv6dMN42f4abd628357829f90fbf2a3e187a1c')]               |
| ['Носов Тимофей Владимирович']        | ['order-232152458@insmail3.sravni.ru']    | ['79167559781'] |           |   nan | 23.01.1976   |         | [Row(title='АО СОГАЗ', link='https://www.sogaz.ru/', login='order-232152458@insmail3.sravni.ru', password_hash='bxSzA0TZ133d6b75cc189521cce3c0d83657f3c1')]    |
```