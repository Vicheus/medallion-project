# Parsetron results

## About row data

> - Code name: index_0452
> - File path: Сайт_аукциов_BidSpirit_06_2023.csv
> - Total rows: 2448

### Schema
```
root
 |-- Почта: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Номер телефона: long (nullable = true)

```

### Data sample
```
| Почта                     | ФИО                     |   Номер телефона |
|:--------------------------|:------------------------|-----------------:|
| rsbsever@gmail.com        | Сметанин Роман          |      79116774355 |
| nick_stark@bk.ru          | Григорьев Никита        |      79020501870 |
| igumnova@inbox.ru         | Игумноваильина Светлана |      79037230985 |
| gelagirenok@mail.ru       | Гиренок Гела            |      79500112333 |
| plus79119391600@gmail.com | Корягин Игор            |      79119391600 |
| s750001@yandex.ru         | Гришко Юрий             |      79265323047 |
| cyrill.book@yandex.ru     | Люлякин Кирилл          |      79163168042 |
| prokhnich@gmail.com       | Прохныч Инна            |      79252757492 |
| olga25021966@inbox.ru     | Ковалева Ольга          |      79046305225 |
| sogoyan@mail.ru           | Согоян Самсон           |      79859674999 |
| artmountain777@gmail.com  | Бенюх Андрей            |      79031778822 |
| seikosq@rambler.ru        | Рачков Александр        |      79228866880 |
| lordofsmirnov@aol.de      | Смирнов Антон           |      79312903731 |
| prosk91@gmail.com         | Проскурнин Андрей       |      79651664974 |
| arturpopov005@mail.ru     | Попов Артур             |      79818524986 |
| muaythai76@mail.ru        | Гарфункел Денис         |      79052128981 |
| intechtool@rambler.ru     | Шермелев Евгений        |      79290812764 |
| bogomazof67@mail.ru       | Богомазов Всеволод      |      79119810267 |
| spb3010@mail.ru           | Ка Сергей               |      79219353139 |
| box305@rambler.ru         | Лукин Владимир          |      79199665243 |
```


## About final data
> - Total rows: 1854

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
| Emails | 99.95% |
| Phones | 96.22% |



### Data sample
```
| names                     | emails                          | phones          |
|:--------------------------|:--------------------------------|:----------------|
| ['Кузнецов Денис']        | ['upmaslovka@gmail.com']        | ['79160611486'] |
| ['Доронина Алина']        | ['lina.doronina.71@mail.ru']    | ['79851361645'] |
| ['Большаков Александр']   | ['mitino588@yandex.ru']         | ['79162440923'] |
| ['Трапезников Игорь']     | ['sakvoyagesmolensk@yandex.ru'] | ['79206639964'] |
| ['Кассиа Пхилиппе']       | ['cassiap@yahoo.com']           | ['79651771843'] |
| ['Гаврилов Александр']    | ['museum01@mail.ru']            | ['79308728285'] |
| ['Анисимов Сергей']       | ['serg_agar@mail.ru']           | ['79158338118'] |
| ['Самоваров Дмитрий']     | ['samovarov@inbox.ru']          | ['79163928269'] |
| ['Максименко Константин'] | ['udaw68@yandex.ru']            | ['79149240599'] |
| ['Степанян Александр']    | ['altart@list.ru']              | ['79219090717'] |
| ['Ид Андрэй']             | ['andred@inbox.ru']             |                 |
| ['Виноградов Дмитрий']    | ['dnv.mobile@gmail.com']        | ['79091545217'] |
| ['Князев Александр']      | ['hhz_03rus@mail.ru']           | ['79818740759'] |
| ['Трошин Андрей']         | ['antroshin@gmail.com']         | ['79255260626'] |
| ['Гончаров Михаил']       | ['goncharov.m@me.com']          | ['79852200204'] |
| ['Хвостенко Мария']       | ['m.hvostenko@gmail.com']       | ['79036164188'] |
| ['Лаврененко Виктор']     | ['werca4e@mail.ru']             | ['79289111607'] |
| ['Чекунаев Борис']        | ['bob_ru@bk.ru']                | ['79273705435'] |
| ['Янев Георгий']          | ['rybolovik@mail.ru']           | ['79228550070'] |
| ['Бел Ари']               | ['imakarova@gmail.com']         | ['79851476350'] |
```