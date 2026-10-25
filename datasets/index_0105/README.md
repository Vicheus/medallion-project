# Parsetron results

## About row data

> - Code name: index_0105
> - File path: /media/user/TRANSCEND/Databases/index_0105/raw/helix2023.csv
> - Total rows: 1008369

### Schema
```
root
 |-- last_name: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- sex: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)

```

### Data sample
```
| last_name   | first_name   | middle_name   | birth_date   | sex     | email                  |       phone |
|:------------|:-------------|:--------------|:-------------|:--------|:-----------------------|------------:|
| ДЕНИСЕНКО   | МАКСИМ       | ВЛАДИМИРОВИЧ  | 1977-10-14   | Мужской | mdeniss@gmail.com      |             |
| ЮЛИЯ        | СНАГОВСКАЯ   | НИКОЛАЕВНА    | 1977-04-17   | Женский | snagovskii@mail.ru     | 79219416505 |
| АБРАМОВА    | ОЛЬГА        | АЛЕКСАНДРОВНА | 1984-04-02   | Женский | abraolga@mail.ru       | 79219586404 |
| БУЗИКОВА    | ИРИНА        | ВЛАДИМИРОВНА  | 1985-09-04   | Женский | irine_post@mail.ru     | 79216390223 |
| СОПОВА      | ОЛЬГА        | ВЛАДИСЛАВОВНА | 1976-03-26   | Женский | olyasopova@ya.ru       |             |
| ПЕТРОВА     | ИННА         | АЛЕКСАНДРОВНА | 1988-04-07   | Женский | petrovainnaa@gmail.com | 79533492311 |
| ЗАГОРИЙ     | ЕЛЕНА        | ЛЕОНИДОВНА    | 1973-10-28   | Женский | elena1994_02@mail.ru   | 79218839281 |
| ШМОЛДАЕВ    | КОНСТАНТИН   | ГРИГОРЬЕВИЧ   | 1987-04-01   | Мужской | k.shmoldaev@gmail.com  | 79215755445 |
| КОТОК       | МАРИЯ        | СЕРГЕЕВНА     | 1983-02-10   | Женский | mari_555@mail.ru       | 79215799881 |
| МОРОЗЬКО    | ЕКАТЕРИНА    | ИГОРЕВНА      | 1984-08-31   | Женский | vip.kate@mail.ru       | 79117504577 |
```


## About final data
> - Total rows: 1007011

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
 |-- sex: integer (nullable = true)

```

### Data sample
```
| names                               | phones          | emails                     | birth_date   |   sex |
|:------------------------------------|:----------------|:---------------------------|:-------------|------:|
| ['Денисенко Максим Владимирович']   |                 | ['mdeniss@gmail.com']      | 14.10.1977   |     1 |
| ['Юлия Снаговская Николаевна']      | ['79219416505'] | ['snagovskii@mail.ru']     | 17.04.1977   |     0 |
| ['Абрамова Ольга Александровна']    | ['79219586404'] | ['abraolga@mail.ru']       | 02.04.1984   |     0 |
| ['Бузикова Ирина Владимировна']     | ['79216390223'] | ['irine_post@mail.ru']     | 04.09.1985   |     0 |
| ['Сопова Ольга Владиславовна']      |                 | ['olyasopova@ya.ru']       | 26.03.1976   |     0 |
| ['Петрова Инна Александровна']      | ['79533492311'] | ['petrovainnaa@gmail.com'] | 07.04.1988   |     0 |
| ['Загорий Елена Леонидовна']        | ['79218839281'] | ['elena1994_02@mail.ru']   | 28.10.1973   |     0 |
| ['Шмолдаев Константин Григорьевич'] | ['79215755445'] | ['k.shmoldaev@gmail.com']  | 01.04.1987   |     1 |
| ['Коток Мария Сергеевна']           | ['79215799881'] | ['mari_555@mail.ru']       | 10.02.1983   |     0 |
| ['Морозько Екатерина Игоревна']     | ['79117504577'] | ['vip.kate@mail.ru']       | 31.08.1984   |     0 |
```