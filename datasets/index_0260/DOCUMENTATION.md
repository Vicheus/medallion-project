# Parsetron results

## About row data

> - File path: 1click_ru.csv
> - Total rows: 1048134

### Schema
```
root
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)

```

### Data sample
```
| name               | email                          |       phone |
|:-------------------|:-------------------------------|------------:|
| Николай            | nikolaytolstikhin@gmail.com    | 79138804207 |
| Андрей             | andrej.bogdanov1967@gmail.ru   | 79235417840 |
| Анастасия          | redaqac1992@mail.ru            | 79689581243 |
| артем              | langepas1963@mail.ru           | 79825589314 |
| Сальников Владимир | vs5457721@gmail.com            | 79225457721 |
| Минаев ла          | doktor17@rambler.ru            | 79689430494 |
| косенкова татьяна  | tanuhka-74@mail.ru             | 79225430077 |
| Александр          | igorsmilentejs@bk.ru           | 79689357848 |
| шахин нихат        | sahinihat@gmail.com            | 79689330472 |
| яковлев александр  | yakovlevs81@mail.ru            | 79225351984 |
| ЯКОВЛЕВА ОЛЕСЯ     | viktorias8@rambitr.ru          | 79225351984 |
| Ягофаров Раиль     | kamillochka3@rambler.ru        | 79225343809 |
| Пашко Игорь        | nbashokpa@rambler.ru           | 79825632507 |
| Саша               | qasa777@mail.ru                | 79251607188 |
| Александр          | trans.logist@bk.ru             | 79689323886 |
| Изольда            | info@stkparma.ru               | 79225187401 |
| Эльмира            | kremleva_elmirochka@rambler.ru | 79046617990 |
| БОГДАН             | klen1605@mail.ru               | 79689300925 |
| логинов максим     | grabitel.duh@gmail.com         | 79225082254 |
| логинов максим     | winged-scorpion@mail.ru        | 79225082254 |
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

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.90% |
| Phones | 69.78% |



### Data sample
```
| names                | emails                           | phones          |
|:---------------------|:---------------------------------|:----------------|
| ['Abakumov Vadim']   | ['vadbim.abakumov.1985@mail.ru'] | ['79275014940'] |
| ['Abbos']            | ['raftem@inbox.ru']              | ['79037003003'] |
| ['Abbos']            | ['mirabbos9y@gmail.com']         | ['79779550620'] |
| ['Abclogistic']      | ['web@abc-logistic.ru']          | ['74956401173'] |
| ['Abduaziz']         | ['abdoolaziz@mail.ru']           | ['79295242707'] |
| ['Abdul']            | ['alieff77@yandex.ru']           | ['79060586666'] |
| ['Abdula']           | ['mm-88@bk.ru']                  | ['79289898751'] |
| ['Abdullaev Sunnat'] | ['sweet.-.boy@mail.ru']          | ['79677673880'] |
| ['Abdullah']         | ['missis.marar@yandex.ru']       | ['79670220324'] |
| ['Abramov Artem']    | ['ed.abramyan2012@yandex.ru']    | ['79776816259'] |
| ['Abushaev Rushan']  | ['rushanabushaev@gmail.com']     | ['79273755770'] |
| ['Adam']             | ['aldonov53@gmail.com']          | ['79999617795'] |
| ['Adel']             | ['adrl.beik@mail.ru']            | ['79998167622'] |
| ['Adelya']           | ['9999502@mail.ru']              | ['79853106011'] |
| ['Adsff']            | ['aaaaa@dsdsds.ru']              | ['79069129146'] |
| ['Advokat']          | ['london-riga@mail.ru']          | ['79657938606'] |
| ['Adxam']            | ['atxam1994@mail.ru']            | ['79002460197'] |
| ['Afradita']         | ['afradita8888@mail.ru']         | ['79505623708'] |
| ['Afypbkm']          | ['fanzil.faza.avto@yandex.ru']   | ['79656633366'] |
| ['Agata']            | ['agata.detkova@yandex.ru']      | ['79521770106'] |
```