# Parsetron results

## About row data

> - Code name: index_0336
> - File path: shop-clothing.ru.txt
> - Total rows: 932012

### Schema
```
root
 |-- Имя: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Номер телефона: string (nullable = true)

```

### Data sample
```
| Имя          | Фамилия      | Почта                         |   Номер телефона |
|:-------------|:-------------|:------------------------------|-----------------:|
| Татьяна      | Никитина     | NikitinaTA@melonfashion.ru    |      79313137380 |
| Ильнур       | Габдрахманов | maililnur@gmail.com           |      79851486474 |
| Инна         | Иванова      | ivanna-iv@yandex.ru           |      79262869003 |
| Ольга        | Кочеткова    | kassiromk@yandex.ru           |      79057306408 |
| Виолетта     | Манжола      | manvioletta@yandex.ru         |      79043427208 |
| Александра   | Якорева      | 2482710@gmail.com             |      79177893377 |
| Ирина        | Андреева     | i.n.andreeva@mail.ru          |      79162093680 |
| Tatiana      | Dudareva     | 360xl@mail.ru                 |      79206007888 |
| Ирина        | Почалкина    | irini-77@mail.ru              |      79262354456 |
| Анастасия    | Черепанова   | nastaskak@yandex.ru           |      79506374203 |
| Елена        | Петрова      | elena73720@yandex.ru          |      79046441107 |
| Евгения      | Шевцова      | evshevcova@yandex.ru          |      79167015850 |
| Ольга        | Крячко       | intarsiya@yandex.ru           |      79187440460 |
| Анюта        | Сеидова      | seidowa79@mail.ru             |      79265727669 |
| Elena        | PRUSAKOVA    | prysia@inbox.ru               |      79263611471 |
| Галина       | Гончарова    | clementmarti@yandex.ru        |      79051162102 |
| Пользователь | Сайта        | natasha721@yandex.ru          |      79627401232 |
| Наталья      | Сашко        | nds-2109@mail.ru              |      79049957723 |
| Татьяна      | Семетчиева   | tatyana.semetchieva@yandex.ru |      79034171481 |
| Ирина        | Шипачева     | shipachiowa@mail.ru           |      79384855235 |
```


## About final data
> - Total rows: 930553

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
| Emails | 99.96% |
| Phones | 99.79% |


### Data sample
```
| names                                     | emails                             | phones          |
|:------------------------------------------|:-----------------------------------|:----------------|
| ['Давыдова Елизавета']                    | ['ladybird-1@yandex.ru']           | ['79108888183'] |
| ['Макарова Инна']                         | ['innamak21@mail.ru']              | ['79296783154'] |
| ['Мартынова Ольга']                       | ['olgamar2006@mail.ru']            | ['79216171363'] |
| ['Жаркова Анна']                          | ['anka.aleksandrovna@yandex.ru']   | ['79209231064'] |
| ['Пользователь Сайта Пользователь Сайта'] | ['luntik777777@mail.ru']           | ['79174535323'] |
| ['Минашкина Елена']                       | ['alenamingol@yandex.ru']          | ['79057707332'] |
| ['Колтыгина Светлана']                    | ['swetaaaa@mail.ru']               | ['79258725007'] |
| ['Б Татьяна']                             | ['babina-tanya@yandex.ru']         | ['79039071554'] |
| ['Соколовская Елена']                     | ['elena.sokolovskaya1990@mail.ru'] | ['79266972373'] |
| ['Журбенко Ольга']                        | ['riksbk82@mail.ru']               | ['79286052129'] |
| ['Олейник Олеся']                         | ['ohiha82@mail.ru']                | ['79602665040'] |
| ['Чичурова Любовь']                       | ['lubenka21@mail.ru']              | ['79503786918'] |
| ['Сайта Пользователь']                    | ['katya.kovalyova.90@mail.ru']     | ['79186253764'] |
| ['Кульченко Нина']                        | ['blackki@mail.ru']                | ['79062393035'] |
| ['Чернова Наталья']                       | ['chernova.n-kursk@mail.ru']       | ['79155130777'] |
| ['Чиркова Татьяна']                       | ['tan.chirckova@yandex.ru']        | ['79042325706'] |
| ['Алла']                                  | ['bejart@yandex.ru']               | ['79164475086'] |
| ['Петракова Светлана']                    | ['petrulka2012@yandex.ru']         | ['79261960163'] |
| ['Горбачева Людмила']                     | ['stolarova-m@mail.ru']            | ['79213089630'] |
| ['Цыпкина Татьяна']                       | ['v_sexygirl1@rambler.ru']         | ['79178971461'] |
```