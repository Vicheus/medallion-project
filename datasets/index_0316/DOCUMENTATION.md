# Parsetron results

## About row data

> - File path: allo-internet.ru-orders.txt
> - Total rows: 118957

### Schema
```
root
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- city: string (nullable = true)
 |-- address: string (nullable = true)

```

### Data sample
```
| name            | email                         |       phone | city   | address   |
|:----------------|:------------------------------|------------:|:-------|:----------|
| Валерик         | vizor@poiskovoeprodvigenie.ru |         777 |        |           |
| Валерик         | vizor@poiskovoeprodvigenie.ru |         777 |        |           |
| Василь Саницкий | vizor@site-bow.com            |     5454654 |        |           |
| Василь Саницкий | vizor@site-bow.com            |     5454654 |        |           |
| Василь Саницкий | vizor@site-bow.com            |     5454654 |        |           |
| Василь Саницкий | vizor@site-bow.com            |     5454654 |        |           |
| Василь Саницкий | vizor@site-bow.com            |     5454654 |        |           |
| орап            | 9097777@mail.ru               |     7856675 |        |           |
| орап            | 9097777@mail.ru               |     7856675 |        |           |
| орап            | 9097777@mail.ru               |     7856675 |        |           |
| Валерик         | vizor@site-bow.com            | 89042286452 |        |           |
| вапр            | 9097777@mail.ru               |       34543 |        |           |
| Ррр             | 9097777@mail.ru               |        5667 |        |           |
| Василь Саницкий | vizor@site-bow.com            |     5454654 |        |           |
| Валерик         | vizor@site-bow.com            | 89042286452 |        |           |
| Василь Саницкий | vizor@site-bow.com            |     5454654 |        |           |
| Василь Саницкий | vizor@site-bow.com            |     5454654 |        |           |
| ывп             | 9097777@mail.ru               |      325423 |        |           |
| ывп             | 9097777@mail.ru               |      325423 |        |           |
| ывп             | 9097777@mail.ru               |      325423 |        |           |
```


## About final data

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

```

### Data sample
```
| names               | emails                        | phones          | address   |
|:--------------------|:------------------------------|:----------------|:----------|
| ['Андрей']          | ['andrey-solodov@mail.ru']    | ['79104904454'] |           |
| ['Андрей']          | ['andreifortuna@mail.ru']     | ['79266652626'] |           |
| ['Михаил']          | ['acsidmi@gmail.com']         | ['79388691010'] |           |
| ['Рузиля Кашапова'] | ['rk@brightbox.ru']           | ['79036645174'] |           |
| ['Алена']           | ['vlasova@russcom.ru']        | ['79250261251'] |           |
| ['Николай']         | ['fcentr@mail.ru']            | ['79168019964'] |           |
| ['Павел']           | ['pahon_85@mail.ru']          | ['79067274468'] |           |
| ['Дмитрий']         | ['admin@veltime.ru']          | ['79772828404'] |           |
| ['Екатерина']       | ['korneva_katy@mail.ru']      | ['79166970273'] |           |
| ['Илья']            | ['clon251@rambler.ru']        | ['79269876789'] |           |
| ['Павел Харинов']   | ['kharinov@ya.ru']            | ['79267337004'] |           |
| ['Влад']            | ['pazkilla@gmail.com']        | ['79853328025'] |           |
| ['Юлия']            | ['urasovajuliya@gmail.com']   | ['79850009515'] |           |
| ['Ольга']           | ['olga.tarasova@zettains.ru'] | ['79037667678'] |           |
| ['Наталья']         | ['mrs.yurshina@gmail.com']    | ['79162062912'] |           |
| ['Elena']           | ['elena.tedy@yandex.ru']      | ['79060762996'] |           |
| ['Константин']      | ['ziminkonst@mail.ru']        | ['79160648089'] |           |
| ['Владимир']        | ['5869900@mail.ru']           |                 |           |
| ['Владимир']        | ['f-jenny@mail.ru']           | ['79263907204'] |           |
| ['Георгий']         | ['geontb@mail.ru']            | ['79859698897'] |           |
```