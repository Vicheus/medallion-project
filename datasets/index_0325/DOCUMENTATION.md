# Parsetron results

## About row data

> - File path: zarina.ru (09.2023).txt
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

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Data sample
```
| names                    | phones          | emails                            |
|:-------------------------|:----------------|:----------------------------------|
| ['Никитина Татьяна']     | ['79313137380'] | ['nikitinata@melonfashion.ru']    |
| ['Габдрахманов Ильнур']  | ['79851486474'] | ['maililnur@gmail.com']           |
| ['Иванова Инна']         | ['79262869003'] | ['ivanna-iv@yandex.ru']           |
| ['Кочеткова Ольга']      | ['79057306408'] | ['kassiromk@yandex.ru']           |
| ['Манжола Виолетта']     | ['79043427208'] | ['manvioletta@yandex.ru']         |
| ['Якорева Александра']   | ['79177893377'] | ['2482710@gmail.com']             |
| ['Андреева Ирина']       | ['79162093680'] | ['i.n.andreeva@mail.ru']          |
| ['Dudareva Tatiana']     | ['79206007888'] | ['360xl@mail.ru']                 |
| ['Почалкина Ирина']      | ['79262354456'] | ['irini-77@mail.ru']              |
| ['Черепанова Анастасия'] | ['79506374203'] | ['nastaskak@yandex.ru']           |
| ['Петрова Елена']        | ['79046441107'] | ['elena73720@yandex.ru']          |
| ['Шевцова Евгения']      | ['79167015850'] | ['evshevcova@yandex.ru']          |
| ['Крячко Ольга']         | ['79187440460'] | ['intarsiya@yandex.ru']           |
| ['Сеидова Анюта']        | ['79265727669'] | ['seidowa79@mail.ru']             |
| ['Prusakova Elena']      | ['79263611471'] | ['prysia@inbox.ru']               |
| ['Гончарова Галина']     | ['79051162102'] | ['clementmarti@yandex.ru']        |
| ['Сайта Пользователь']   | ['79627401232'] | ['natasha721@yandex.ru']          |
| ['Сашко Наталья']        | ['79049957723'] | ['nds-2109@mail.ru']              |
| ['Семетчиева Татьяна']   | ['79034171481'] | ['tatyana.semetchieva@yandex.ru'] |
| ['Шипачева Ирина']       | ['79384855235'] | ['shipachiowa@mail.ru']           |
```