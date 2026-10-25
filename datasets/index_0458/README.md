# Parsetron results

## About row data

> - Code name: index_0458
> - File path: Магазин_техники_Pro-Katalog_02_2023.csv
> - Total rows: 4060

### Schema
```
root
 |-- Почта: string (nullable = true)
 |-- ФИО: string (nullable = true)

```

### Data sample
```
| Почта                       | ФИО                |
|:----------------------------|:-------------------|
| tuxaob@gmail.com            | Дмитрий            |
| tuxahob@gmail.com           | Дмитрий            |
| tuxahob@yandex.ru           | Дмитрий            |
| miha00783@mail.ru           | Михаил             |
| moi.utube@gmail.com         | Олег               |
| vahno@mailto.plus           | Vahno@Mailto.Plus  |
| mihal2003mts@mail.ru        | Михаил             |
| CAYJXT@yandex.ru            | Аноним             |
| xarbasnax@gmail.com         | Максим             |
| bizyaev_pasha@mail.ru       | Павел              |
| stalkerkiller1996@gmail.com | Федор              |
| media@pro-katalog.ru        | Олег               |
| kpnctajlnk@gmail.com        | Ярмакс             |
| aanazarov1407@mail.ru       | Артем Назаров      |
| glebtytuk@gmail.com         | Глеб Юрьевич Тытюк |
| penser@bk.ru                | Геннадий           |
| vladsa76@Yandex.ru          | Влад               |
| yustensagaz@gmail.com       | Степан             |
| bybliy70@gmail.com          | Юрий               |
| zzz4.71@mail.ru             | Максим Николаевич  |
```


## About final data
> - Total rows: 3769

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
| names                        | emails                             |
|:-----------------------------|:-----------------------------------|
| ['Эдуард']                   | ['edwxrep@mail.ru']                |
| ['Анатолий']                 | ['tolik112233445567@gmail.com']    |
| ['Артем']                    | ['artyom.nizovtsev1337@gmail.com'] |
| ['Сергей Богданович Марчук'] | ['smarcuk21@gmail.com']            |
| ['Александр']                | ['lysenko288974@mail.ru']          |
| ['Сергэй']                   | ['of-standart@yandex.ru']          |
| ['Михаил Персов']            | ['mihailpersov@gmail.com']         |
| ['Радислав Горбачев']        | ['fens@bk.ru']                     |
| ['Александр']                | ['nidl@list.ru']                   |
| ['Андрей Кусакин']           | ['cusakinandrei@yandex.ru']        |
| ['Волт']                     | ['vova_volt@mail.ru']              |
| ['Алексей']                  | ['gordeev_1515@mail.ru']           |
| ['Тимур']                    | ['jaxbax10@mail.ru']               |
| ['Кирилл']                   | ['info.yakovlev@yandex.ru']        |
| ['Фомич']                    | ['rifatrik@gmail.com']             |
| ['Максим Цуриков']           | ['gurarufer@gmail.com']            |
| ['Иван']                     | ['bobrovvanaakautn@gmail.com']     |
| ['Cергей Анатольевич']       | ['s.a.muminov61@mail.ru']          |
| ['Плазма']                   | ['artembabosev@gmail.com']         |
| ['Даня']                     | ['reserk58@gmail.com']             |
```