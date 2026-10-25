# Parsetron results

## About row data

> - Code name: index_0215
> - File path: /media/user/SAMSUNG/Databases/index_0215/raw/premiumbonus.ru/users.csv
> - Total rows: 3668213

### Schema
```
root
 |-- Телефон: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- Пол: string (nullable = true)

```

### Data sample
```
|     Телефон | ФИО                       | Дата рождения   | Email                    | Пол    |
|------------:|:--------------------------|:----------------|:-------------------------|:-------|
| 79147740190 | Поступаева Ксения         | 27.05.1989      |                          |        |
| 79165118274 | Владимир                  |                 |                          |        |
| 79165118274 | Владимир                  | 12.10.1989      |                          |        |
| 79529584787 |                           |                 |                          | male   |
| 79653094982 |                           | 28.02.2014      |                          |        |
| 79834441904 | Егор                      | 21.04.1998      | Nesterovegor98@gmail.com | male   |
| 79277208047 |                           |                 |                          | male   |
| 79038202299 | татьяна                   | 18.05.1976      |                          | female |
| 79381267737 |                           |                 |                          | male   |
| 79520447840 |                           |                 |                          | male   |
| 79055352474 | Азалия                    | 01.01.1998      |                          | female |
| 79264460275 | светлана                  | 23.08.1968      |                          | female |
| 79262517634 | Роман                     | 05.04.1984      |                          | male   |
| 79165686310 | Громова Юлия Николаевна   |                 |                          | female |
| 79264926329 | Анна                      | 30.12.1981      |                          | female |
| 79773358976 |                           |                 |                          | male   |
| 79099166169 | Посторнок Ирина Сергеевна | 03.12.1974      |                          | female |
| 79163069424 | мария                     |                 |                          |        |
| 79778362451 | Александр                 | 01.04.1988      |                          | male   |
| 79815002271 |                           |                 |                          | male   |
```


## About final data
> - Total rows: 2226356

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)

```

### Data sample
```
| names                 | phones          | emails                        |   sex | birth_date   |
|:----------------------|:----------------|:------------------------------|------:|:-------------|
| ['.Юдакова Зинаида']  | ['79035251572'] |                               |     0 | 17.09.1972   |
| ['Alex']              | ['79036660094'] | ['alex@osmi.ru']              |     1 | 01.01.1980   |
| ['Alsu']              | ['79819515328'] |                               |     0 | 29.09.1999   |
| ['Andrei']            | ['79852281319'] |                               |     0 | 17.08.1972   |
| ['Andrey']            | ['79154795706'] |                               |     1 | 23.06.1976   |
| ['Andrey']            | ['79164502006'] |                               |     1 | 25.06.1985   |
| ['Andrey']            | ['79191393612'] | ['shakurov-92@mail.ru']       |     1 | 09.12.1992   |
| ['Anna Popova']       | ['79037180303'] | ['anna-design11@mail.ru']     |     0 | 30.10.1985   |
| ['Anny']              | ['79099200575'] |                               |     0 | 25.09.1998   |
| ['Anthonyjust']       | ['79219751616'] | ['applyfor@mail.ru']          |     1 | 18.09.1986   |
| ['Anton']             | ['79167229936'] | ['dinamick@yandex.ru']        |     1 | 31.08.1983   |
| ['Antoni']            | ['79045563210'] |                               |     1 | 02.09.1996   |
| ['Barbara']           | ['79859854143'] | ['484490ywxtuib2z@gmail.com'] |   nan |              |
| ['Betty']             | ['78406726725'] | ['860510xthueob3x@gmail.com'] |   nan |              |
| ['Betty']             | ['79618350673'] | ['900162bjmfuob3p@gmail.com'] |   nan |              |
| ['Bhbyf']             | ['79175393760'] |                               |     0 | 04.04.1960   |
| ['Cdtnkfyf']          | ['79169362377'] |                               |     0 | 12.07.2018   |
| ['Cdtnkfyf']          | ['79265375717'] |                               |     0 | 23.01.1974   |
| ['Celestia Princess'] | ['79511299097'] | ['belafon@mail.ru']           |     0 | 16.01.2002   |
| ['Cfyz']              | ['79672840702'] |                               |     1 | 26.07.1987   |
```