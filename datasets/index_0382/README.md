# Parsetron results

## About row data

> - Code name: index_0382
> - File path: smeni-auto.ru.txt
> - Total rows: 19601

### Schema
```
root
 |-- Почта: string (nullable = true)
 |-- Имя: string (nullable = true)

```

### Data sample
```
| Почта                     | Имя           |
|:--------------------------|:--------------|
| bezhan.anatolii@yandex.ru | А натолии     |
| amir.order.kr@gmail.com   | А-МИР         |
| renault1283@mail.ru       | А.Г.Хагатрян  |
| sovin@sampo.ru            | Аnri          |
| Yunusovabu@mail.ru        | АБУ           |
| andreyt17@yandex.ru       | АВГЕО         |
| mng@avto-oil.su           | АВТО-ОЙЛ      |
| avto.rai@mail.ru          | АВТОЗАПЧАСТИ  |
| zebriwe@mail.ru           | АВТОРАЙ       |
| info@avtostreet16.ru      | АВТОСТРИТ     |
| mericep5@mail.ru          | АВтоГродно    |
| avuni1@rambler.ru         | АВуниверсалТО |
| alexander0038@mail.ru     | АДЕКСАНДР     |
| sergey_shr@mail.ru        | АДМИНИСТРАТОР |
| a333am99@ya.ru            | АК СОЮЗ       |
| reklamaakb@gmail.com      | АКБ-Энерго    |
| akk-star@bk.ru            | АККстар       |
| a754km@yandex.ru          | АЛЁНА         |
| sawuna@yandex.ru          | АЛЕКСАНДР     |
| kri125@rambler.ru         | АЛЕКСАНДР     |
```


## About final data
> - Total rows: 19491

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
| names                  | emails                         |
|:-----------------------|:-------------------------------|
| ['Авуниверсалто']      | ['avuni1@rambler.ru']          |
| ['Алекzандр']          | ['87074@mail.ru']              |
| ['Александр']          | ['sashaz301z@yandex.ru']       |
| ['Александр']          | ['auuto134@mail.ru']           |
| ['Александр']          | ['avto2088@mail.ru']           |
| ['Александр']          | ['manako.aleksandr@yandex.ru'] |
| ['Александр']          | ['051983@rambler.ru']          |
| ['Александр']          | ['razm385@mail.ru']            |
| ['Александр Наталья']  | ['pa51652@bk.ru']              |
| ['Александранастасия'] | ['auuto129@mail.ru']           |
| ['Алексей']            | ['pa10991@bk.ru']              |
| ['Алексей']            | ['maz192@yandex.ru']           |
| ['Алексей']            | ['n_alexey62@mail.ru']         |
| ['Алексей']            | ['pa51284@bk.ru']              |
| ['Анатолий']           | ['auuto314@yandex.ru']         |
| ['Андрей']             | ['auuto2@yandex.ru']           |
| ['Андрей']             | ['auto182@yandex.ru']          |
| ['Андрей']             | ['jemis72@yandex.ru']          |
| ['Андрей']             | ['khrupovandrei@yandex.ru']    |
| ['Андрей']             | ['auuto826@yandex.ru']         |
```