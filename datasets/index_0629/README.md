# Parsetron results

## About row data

> - Code name: index_0629
> - File path: ska.ru (20.08.2020).txt
> - Total rows: 69878

### Schema
```
root
 |-- Почта: string (nullable = true)
 |-- Имя: string (nullable = true)

```

### Data sample
```
| Почта                         | Имя       |
|:------------------------------|:----------|
| jsullivan@sdwndr.com          | Яша       |
| Sashayas1957@mail.ru          | Ястребков |
| Y.S.B.S@yandex.ru             | Ясиря     |
| asfil@bk.ru                   | Ярославна |
| Kyara76@yandex.ru             | Ярославна |
| yaroslava.komarenko@yandex.ru | Ярославна |
| reva.04@mail.ru               | Ярослава  |
| yaroslavaivanuyk@gmail.com    | Ярослава  |
| yaranozhko01@gmail.com        | Ярослава  |
| yaroslava_dyldin@mail.ru      | Ярослава  |
| Yaroslava_spb@inbox.ru        | Ярослава  |
| nikolreylui@gmail.com         | Ярослава  |
| jaroslawa.sidorova@yandex.ru  | Ярослава  |
| metalocalypse1010@gmail.com   | Ярослава  |
| potapovayar@mail.ru           | Ярослава  |
| yaroslava741@gmail.com        | Ярослава  |
| yroslava_96@mail.ru           | Ярослава  |
| Slava_mls@mail.ru             | Ярослава  |
| prokatimsya@yandex.ru         | Ярослав   |
| kiczul9700@mail.ru            | Ярослав   |
```


## About final data
> - Total rows: 68664

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |



### Data sample
```
| names         | emails                            |
|:--------------|:----------------------------------|
| ['Яша']       | ['jsullivan@sdwndr.com']          |
| ['Ястребков'] | ['sashayas1957@mail.ru']          |
| ['Ясиря']     | ['y.s.b.s@yandex.ru']             |
| ['Ярославна'] | ['asfil@bk.ru']                   |
| ['Ярославна'] | ['kyara76@yandex.ru']             |
| ['Ярославна'] | ['yaroslava.komarenko@yandex.ru'] |
| ['Ярослава']  | ['reva.04@mail.ru']               |
| ['Ярослава']  | ['yaroslavaivanuyk@gmail.com']    |
| ['Ярослава']  | ['yaranozhko01@gmail.com']        |
| ['Ярослава']  | ['yaroslava_dyldin@mail.ru']      |
| ['Ярослава']  | ['yaroslava_spb@inbox.ru']        |
| ['Ярослава']  | ['nikolreylui@gmail.com']         |
| ['Ярослава']  | ['jaroslawa.sidorova@yandex.ru']  |
| ['Ярослава']  | ['metalocalypse1010@gmail.com']   |
| ['Ярослава']  | ['potapovayar@mail.ru']           |
| ['Ярослава']  | ['yaroslava741@gmail.com']        |
| ['Ярослава']  | ['yroslava_96@mail.ru']           |
| ['Ярослава']  | ['slava_mls@mail.ru']             |
| ['Ярослав']   | ['prokatimsya@yandex.ru']         |
| ['Ярослав']   | ['kiczul9700@mail.ru']            |
```