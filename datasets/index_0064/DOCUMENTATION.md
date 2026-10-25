# Parsetron results

## About row data

> - Code name: index_0064
> - File path: KupiVIP/KupiVIP.ru 4.2kk.txt
> - Total rows: 4244657

### Schema
```
root
 |-- birth_date: string (nullable = true)
 |-- email: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- city: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- additional_phone: string (nullable = true)

```

### Data sample
```
| birth_date   | email                           | first_name   | last_name   | city        | phone              | additional_phone   |
|:-------------|:--------------------------------|:-------------|:------------|:------------|:-------------------|:-------------------|
| 1900-01-01   | ?                               | Ирина        | Григорьева  | ?           | +7 (951) 096-28-29 |                    |
| 1900-01-01   | !cherry-baby@mail.ru            | Марина       | Дубровина   | Yoshkar-ola |                    |                    |
| 1900-01-01   | !gjrexa2003@mail.ru             | Кира         | Лемах       |             |                    |                    |
| 1900-01-01   | ***ludmila***@mail.ru           | Людмила      | Гальянова   |             |                    |                    |
| 1900-01-01   | **anita**@lina.ru               | Анет         | Вартанян    |             |                    |                    |
| 1900-01-01   | *elena34*@meil.ru               | Елена        | Чикова      |             |                    |                    |
| 1900-01-01   | *elena@yandex.ru                | елена        | казанцева   | Khabarovsk  |                    |                    |
| 1900-01-01   | *kity168@rambler.ru             | *Екатерина   | *Сорокина   | Kemerovo    |                    |                    |
| 1900-01-01   | *mixeevakaterina2009@rambler.ru | *Екатерина   | * Михеева   | Nyagan      |                    |                    |
| 1900-01-01   | -------ruslan_0890.90@mail.ru   | Клава        | Виноградова |             |                    |                    |
```

> - Code name: index_0064
> - File path: KupiVIP/kupi_vip_*.csv
> - Total rows: 4244693

### Schema
```
root
 |-- id: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- email: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- unknown_field_1: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- city: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- additional_phone: string (nullable = true)
 |-- unknown_field_2: string (nullable = true)

```

### Data sample
```
| id     | birth_date    | email                          | first_name        | unknown_field_1   | last_name      | city   | phone    | additional_phone     | unknown_field_2   |
|:-------|:--------------|:-------------------------------|:------------------|:------------------|:---------------|:-------|:---------|:---------------------|:------------------|
| Код    | Поле1         | Поле2                          | Поле3             | Поле4             | Поле5          | Поле6  | Поле7    | Поле8                | Поле9             |
| 31     | (NULL         | hlljdhkghjhgf@lkjlkjgddcbnm.fr | 'cvbnm'           | b'0'              | 'vbnm          | '      |          | '+7 (123) 123-45-66' | ''                |
| 3845   | ('1982-01-18' | yxo8585@mail.ru                | 'fcz'             | b'0'              | 'hji           | '      |          | NULL                 | NULL              |
| 8573   | ('1984-08-24' | nastenok.84@inbox.ru           | 'Настена'         | b'0'              | '              | '      | 'Moscow' | NULL                 | NULL              |
| 13760  | ('1985-07-20' | gnom55ru@yandex.ru             | 'Rolex'           | b'0'              | '              | '      | 'Moscow' | '+7 (916) 275-64-00' | NULL              |
| 109142 | ('1929-02-01' | bbuurroo@gmail.com             | 'glb.nLBVjg<>CNK' | b'0'              | 'lixatnckghzbk | '      | NULL     | NULL                 | NULL              |
| 135021 | ('1989-11-15' | ck199@mail.ru                  | 'Ярик'            | b'0'              | '              | '      | NULL     | NULL                 | NULL              |
| 297342 | ('1977-08-31' | varduhi_77@mail.ru             | 'вардуи'          | b'0'              | 'саргсян       | '      | NULL     | NULL                 | NULL              |
| 311333 | (NULL         | pashapri123@mail.ru            | 'Павел'           | b'0'              | '0             | '      | NULL     | NULL                 | NULL              |
| 318485 | ('1988-02-13' | filippova88@bk.ru              | '                 | Авария'           | b'0'           | '      | '        | NULL                 | NULL              |
```


## About final data
> - Total rows: 6633313

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Data sample
```
| names                    | phones          | emails                   | birth_date   | address              |
|:-------------------------|:----------------|:-------------------------|:-------------|:---------------------|
| ['Григорьева Ирина']     | ['79510962829'] |                          |              |                      |
| ['Волкова Ольга']        |                 | ['0-0-0-0-0-0-@mail.ru'] |              | ['Kurgan']           |
| ['Слудчик Слудчик']      |                 | ['0-0-0-0-0-23@mail.ru'] |              |                      |
| ['Кунгурова Ольга']      |                 | ['0-0-0-k@mail.ru']      |              |                      |
| ['Александрова Татьяна'] |                 | ['0-0-001@mail.ru']      |              | ['Moscow']           |
| ['Енькова Алёна']        |                 | ['0-00@inbox.ru']        |              | ['Saint Petersburg'] |
| ['Соков Сергей']         |                 | ['0-01987@mail.ru']      |              |                      |
| ['Оксана']               |                 | ['0-2121@yandex.ru']     |              |                      |
| ['Челяев Саша']          |                 | ['0-4ilik-0@mail.ru']    |              |                      |
| ['Кутищева Кристина']    |                 | ['0-5-0-4@mail.ru']      |              |                      |
```