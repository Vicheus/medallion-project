# Parsetron results

## About row data

> - Code name: index_0500_mailru_2022
> - File path: xaa.csv
> - Total rows: 19999999

### Schema
```
root
 |-- email: string (nullable = true)
 |-- phone: long (nullable = true)
 |-- id: integer (nullable = true)

```

### Data sample
```
| email                     |        phone |   id |
|:--------------------------|-------------:|-----:|
| yaugen.puntus@mail.ru     | 375256336453 |    1 |
| yaugenrepeckii@mail.ru    | 375445622010 |    2 |
| yaugenrepik@mail.ru       | 375445622010 |    3 |
| yaugen_r@list.ru          | 375295299981 |    4 |
| yaugen_romanchuk@mail.ru  | 375295299981 |    5 |
| yaugen_senkou@mail.ru     | 375295943943 |    6 |
| yaugen.shestak.99@mail.ru | 375299439277 |    7 |
| yaugensukach1986@mail.ru  |  79805018321 |    8 |
| yaugensukach2009@mail.ru  |  79805018321 |    9 |
| yaugen.sysov.91@mail.ru   | 375299764978 |   10 |
| yaugen.sysov.91@mail.ru   | 375444704804 |   11 |
| yaugenusvovkovich@mail.ru | 375293323468 |   12 |
| yaugen.vasko@mail.ru      | 375444986074 |   13 |
| yaugen.vaycyuhen@mail.ru  | 375299183105 |   14 |
| yaugen.wot@mail.ru        | 375299963863 |   15 |
| yaugen.yashkou.92@mail.ru | 375336244328 |   16 |
| yaugeny.bannov@mail.ru    |  79048048500 |   17 |
| yaugenzenko94@mail.ru     | 375447763629 |   18 |
| yaugen.zhdanau@inbox.ru   |  79117593464 |   19 |
| yaugenz@mail.ru           | 375299141564 |   20 |
```


## About final data
> - Total rows: 14157294

### Schema
```
root
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)

```



### Data sample
```
| emails                    | phones          |
|:--------------------------|:----------------|
| ['yauk11@mail.ru']        | ['79081001867'] |
| ['yauk1996@mail.ru']      | ['79233729967'] |
| ['yaukeduard@mail.ru']    | ['79199347268'] |
| ['yaukhman@bk.ru']        | ['79511832878'] |
| ['ya_ulibka@mail.ru']     | ['79606997406'] |
| ['ya_unik@mail.ru']       | ['79236439215'] |
| ['ya-uran1989@bk.ru']     | ['79519504762'] |
| ['yaurov1999@mail.ru']    | ['79204408652'] |
| ['yaurova76@mail.ru']     | ['79069407829'] |
| ['yausaneva@mail.ru']     | ['79119645896'] |
| ['yaushev97@mail.ru']     | ['79524674760'] |
| ['yausheva.vera@mail.ru'] | ['79207220578'] |
| ['ya.usup77@mail.ru']     | ['79608998197'] |
| ['yauza75@mail.ru']       | ['79629971950'] |
| ['ya.uzbek1990@mail.ru']  | ['79602582796'] |
| ['yav063@mail.ru']        | ['79198095776'] |
| ['yav_07@list.ru']        | ['79087939777'] |
| ['yav-1960-yav@mail.ru']  | ['79277927479'] |
| ['yav197419@mail.ru']     | ['79224828555'] |
| ['yav-1976@mail.ru']      | ['79027688791'] |
```