# Parsetron results

## About row data

> - Code name: index_0508
> - File path: rbt_ru_2022.csv
> - Total rows: 477250

### Schema
```
root
 |-- e-mail: string (nullable = true)
 |-- Телефон: long (nullable = true)
 |-- Фамилия Имя: string (nullable = true)

```

### Data sample
```
| e-mail                          |     Телефон | Фамилия Имя               |
|:--------------------------------|------------:|:--------------------------|
| sten989@gmail.com               | 79173030520 | Саламатов Станислав       |
| salamatik85@gmail.com           | 79172002005 | Саламатов Николай         |
| pachkordkonektorovich@gmail.com | 79173219212 | Тихонов Максим            |
| shpak04.05.12@gmail.com         | 79603572097 | Шпак Александр            |
| reschikova22.05.12@gmail.com    | 79053294428 | Резчикова Светлана        |
| nina19621963@gmail.com          | 79270293601 | Тихонова Нина             |
| ungurianu64@gmail.com           | 79276217473 | Унгуряну Виктор           |
| ozeroo83@gmail.com              | 79372477529 | Родин Андрей              |
| chigirinskiy1984@gmail.com      | 79198306212 | Чигиринский Александр     |
| yur.pichugin@gmail.com          | 79042449002 | Пичугин Юрий              |
| sorokinaleksey1957@gmail.com    | 79198340615 | Сорокин Алексей Сергеевич |
| iskaliev.s@gmail.com            | 79270557293 | Искалиев Самат            |
| natylja2012@gmail.com           | 79042449003 | Пичугина Наталия          |
| alekseyko81@yahoo.com           | 79198232636 | Поляков Алексей           |
| logach.andrey@gmail.com         | 79033809204 | Логач Андрей              |
| dims537903@gmail.com            | 79033287903 | заботалкина марина        |
| sibir101177@gmail.com           | 79179893149 | истомин сергей            |
| lelyzis01@gmai.com              | 79271211262 | Зис Ольга                 |
| angel89372214622@gmail.com      | 79027101114 | Медведева Елена           |
| saharovkos@yahoo.com            | 79372251404 | Сахаров Константин        |
```


## About final data
> - Total rows: 477144

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 99.98% |
| Emails | 99.99% |



### Data sample
```
| names                           | phones          | emails                       |
|:--------------------------------|:----------------|:-----------------------------|
| ['Шатуло Альбина']              | ['79134524304'] | ['albina250440@gmail.com']   |
| ['Буряков Сергей']              | ['79270711555'] | ['bursk2010@gmail.com']      |
| ['Митрофанова Елена']           | ['79293997621'] | ['lenmitr@gmail.com']        |
| ['Гусельников Владимир']        | ['79132442747'] | ['guselnikof@gmail.com']     |
| ['Новоселова Ирина Дмитриевна'] | ['79068747775'] | ['novoselid57@gmail.com']    |
| ['Пугачёва Нина']               | ['79141955761'] | ['pugachevasuper@yahoo.com'] |
| ['Канюков Сергей']              | ['79125848751'] | ['kansermmm@gmail.com']      |
| ['Курандина Мария']             | ['79223452558'] | ['dick911@list.ru']          |
| ['Крылов Дмитрий']              | ['79242305428'] | ['dmalkr@gmail.com']         |
| ['Бубнов Андрей']               | ['79275105241'] | ['anb0103@gmail.com']        |
| ['Горбунова Ирина']             | ['79199431049'] | ['mmmgorbunova@yahoo.com']   |
| ['Кобелев Александр']           | ['79512098203'] | ['alex15111974@gmail.com']   |
| ['Филиппова Оксана']            | ['79029288058'] | ['rodina2003@gmail.com']     |
| ['Одинцева Ольга']              | ['79516166282'] | ['odinolya@gmail.com']       |
| ['Мязин Максим']                | ['79183386438'] | ['max03vm@gmail.com']        |
| ['Орловская Татьяна']           | ['79139360370'] | ['orlovska2012@gmail.com']   |
| ['Ибрагимов Олег']              | ['79281165077'] | ['ibra.olega@yandex.ru']     |
| ['Симоненко Татьяна']           | ['79233409950'] | ['66simona19@gmail.com']     |
| ['Зотова Лариса']               | ['79628531447'] | ['zotova7575@gmail.com']     |
| ['Глебова Валентина']           | ['79048365453'] | ['glebova.vf@gmail.com']     |
```