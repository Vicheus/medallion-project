# Parsetron results

## About row data

> - Code name: index_0383
> - File path: mira1.ru (04.2023).txt
> - Total rows: 328640

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Номер телефона: long (nullable = true)
 |-- Почта: string (nullable = true)

```

### Data sample
```
| ФИО                                  |   Номер телефона | Почта                          |
|:-------------------------------------|-----------------:|:-------------------------------|
| Копылов                              |      79180120960 | kopylov@krd.kassy.ru           |
| Пурин Александр Юрьевич              |      79091648789 | geh123@ya.ru                   |
| Андрей Васильевич Краюшников         |      79160179462 | act1901@mail.ru                |
| Краюшников Андрей Васильевич         |      79160179462 | act1901@mail.ru                |
| Петров Иван Сидорович                |      74954491313 | office@tonline.su              |
| Навроцкая Мария Олеговна             |      79165040950 | m.navrotskaya@mail.ru          |
| Броканова Диана Аллаяровна           |      79267157836 | diana.alieva1991@ya.ru         |
| Басистая Екатерина                   |      79162799384 | basistaya_ekaterina@bk.ru      |
| Асеева Елена Евгеньевна              |      79284264884 | info@asseeva.it                |
| Веретельная                          |      79271242221 | v.irina784@mail.ru             |
| Барский Павел Анатольевич            |      79520591468 | dalenski@bk.ru                 |
| Калинина Дарья                       |      79031206361 | dashli@list.ru                 |
| Захарова Юлия Александровна          |      79269312004 | aom.ea45@yandex.ru             |
| Анатолити Ольга                      |      79060795669 | 0795669@gmail.com              |
| Иванов                               |      79119873736 | green@mail.ru                  |
| Иванов Иван Иванович                 |      79992341111 | no@yandex.ru                   |
| Белобровская Вероника Сергеевна      |      79850467711 | veronika_bielobrovska@inbox.ru |
| Расова Елена Евгеньевна              |      79009798374 | elrasova@mail.ru               |
| Алексеев Александр Владимирович      |      79852269655 | alexeev42@gmail.com            |
| Mакарова Иллирия Константин Ютиновна |      79858241721 | kidfox69@mail.ru               |
```


## About final data
> - Total rows: 327742

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


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 99.45% |
| Emails | 99.98% |



### Data sample
```
| names                                   | phones          | emails                           |
|:----------------------------------------|:----------------|:---------------------------------|
| ['Пудовкина Вероника Петровна']         | ['79228189626'] | ['sputnik-buguruslan@yandex.ru'] |
| ['Дербин']                              | ['79500069500'] | ['stason.jha@gmail.com']         |
| ['Купарева Юлия Сергеевна']             | ['79296823668'] | ['fluff_15@mail.ru']             |
| ['Примаков Виталий Юрьевич']            | ['79104162109'] | ['vitek175@gmail.com']           |
| ['Aleksandra Platonova']                | ['79035301511'] | ['school@storm-kite.com']        |
| ['Пахомова Наталья Николаевна']         | ['79152357716'] | ['natalya-pahomova@mail.ru']     |
| ['Кондратенкова Наталья Александровна'] | ['79060943757'] | ['nkondratenkova@yandex.ru']     |
| ['Ирина Анатольевна Герасимович']       | ['79057620995'] | ['abcd2277@yndex.ru']            |
| ['Варя Свиридова']                      | ['79268272176'] | ['barbarasviridova@gmail.com']   |
| ['Ларин Антон Маратович']               | ['79067765793'] | ['anton-larin@yandex.ru']        |
| ['Галина']                              | ['79114416763'] | ['samodurova.gala@yandex.ru']    |
| ['Белецкая Полина Владимировна']        | ['79879235070'] | ['limitedsolution@yahoo.com']    |
| ['Тихий Александр Евгеньевич']          | ['79183065442'] | ['alex8415@yandex.ru']           |
| ['Черепанов Антон']                     | ['79107727252'] | ['cherepanofff@mail.ru']         |
| ['Евгения Викторовна Заморова']         | ['79165453903'] | ['jane-lvenok@bk.ru']            |
| ['Садовин Константин Владимирович']     | ['79100968806'] | ['sadovin.k.v@gmail.com']        |
| ['Апостолова Оксана Николаевна']        | ['79153971782'] | ['oksanaa80@mail.ru']            |
| ['Полянская Валерия Александровна']     | ['79156712360'] | ['valerkapolyanskaya@mail.ru']   |
| ['Dmitriy Karavaev']                    | ['79295372237'] | ['karavaev110@gmail.com']        |
| ['Каневская']                           | ['79163867079'] | ['itner@yandex.ru']              |
```