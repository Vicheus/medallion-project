# Parsetron results

## About row data

> - Code name: index_0451
> - File path: Магазин_сувениров_Сувенирка24_11_09_2022.csv
> - Total rows: 247

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Номер телефона: long (nullable = true)
 |-- Почта: string (nullable = true)

```

### Data sample
```
| ФИО                 |   Номер телефона | Почта                     |
|:--------------------|-----------------:|:--------------------------|
| Оханова Анна        |      7.90571e+10 | okhanova_anna@mail.ru     |
| Крейнес Ирина       |      7.92625e+10 | kreynes53@mail.ru         |
| Лариса Елканова     |      7.91882e+10 | Podarki-osetia@mail.ru    |
| Клюева Наталья      |      7.91032e+10 | alhimik79@mail.ru         |
| Грмова Наталья      |      7.92522e+10 | vargromova@mail.ru        |
| Михайлов Михаил     |      7.96236e+10 | 89169231904@mail.ru       |
| Черникова Елена     |      7.92639e+10 | finance@prismarealty.ru   |
| Крижановская Галина |      7.9163e+10  | krizhgalina@mail.ru       |
| Пономаренко Наташа  |    nan           | tamagosha@gmail.com       |
| Соня                |    nan           | u1511790655.3799@ab.cwe   |
| Пейович Светлана    |    nan           | S_bubamara@list.ru        |
| Легкова Александра  |      7.96521e+10 | Goddessvenera@yandex.ru   |
| Османова Анна       |      7.91619e+10 | Ere177@ya.ru              |
| Машкина Елена       |    nan           | emashkina04@gmail.com     |
| Спиридонова Татьяна |      7.92659e+10 | Spirid1984@rambler.ru     |
| Сухов Сергей        |      7.926e+10   | sergesukhov@narod.ru      |
| Трунова Анна        |      7.92692e+10 | Sovetnik.cniiag@gmail.com |
| Шалашникова Мария   |      7.92654e+10 | Maschunya80@rambler.ru    |
| Яковлев Дмитрий     |      7.90357e+10 | d_studio@inbox.ru         |
| Корешкова Регина    |    nan           | korezh25@mail.ru          |
```


## About final data
> - Total rows: 247

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
| Emails | 100.00% |
| Phones | 36.03% |



### Data sample
```
| names                    | emails                            | phones          |
|:-------------------------|:----------------------------------|:----------------|
| ['Потявин Никита']       | ['n.potyavin@rgau-msha.ru']       | ['79187508214'] |
| ['Кулагина Мария']       | ['maridancer@mail.ru']            |                 |
| ['Наталья Калиниченко']  | ['kalinicenkon6@gmail.com']       | ['79881541253'] |
| ['Макеева Елена']        | ['lena_agb@mail.ru']              |                 |
| ['Берсенева Светлана']   | ['svetlana.romina@gmail.com']     |                 |
| ['Фурсова Ася']          | ['afursova@u.university']         | ['79104536811'] |
| ['Капырин Артем']        | ['disciplest99@yandex.ru']        |                 |
| ['Жигунов Дмитрий']      | ['dkzhigunov@yandex.ru']          |                 |
| ['Крейнес Ирина']        | ['kreynes53@mail.ru']             | ['79262469151'] |
| ['Свистунова Софья']     | ['9107788@mail.ru']               |                 |
| ['Пархоменко Светлана']  | ['parxomenko.svetlana@gmail.com'] |                 |
| ['Михайлович Юрий']      | ['2075757@gmail.com']             | ['79262075757'] |
| ['Кочеткова Виктория']   | ['vikakochetkova96@gmail.com']    |                 |
| ['Косульникова Наталья'] | ['kosulnikova_n83@mail.ru']       |                 |
| ['Моисеев Владимир']     | ['moiseev767@mail.ru']            | ['79653626728'] |
| ['Соломатина Инна']      | ['innasolomatina@rambler.ru']     | ['79689485508'] |
| ['Урвачева Елена']       | ['urvacheva.elena@mail.ru']       |                 |
| ['Эксанова Камила']      | ['kama-mila777@mail.ru']          | ['79150639094'] |
| ['Даринская Вера']       | ['vera.v.ch@mail.ru']             |                 |
| ['Макаров Алексей']      | ['mob9265338181@gmail.com']       |                 |
```