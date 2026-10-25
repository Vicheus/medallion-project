# Parsetron results

## About row data

> - File path: planzala.ru.txt
> - Total rows: 32616

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- Почта: string (nullable = true)

```

### Data sample
```
| ФИО               |   Номер телефона | Почта                      |
|:------------------|-----------------:|:---------------------------|
|                   |      74444444444 | 123@jkjkljklm.ru           |
|                   |                  | 1@1.com                    |
|                   |      79205481516 | 5158158@rgfdhd.tg          |
|                   |      78515552520 | hgc@mail.ru                |
|                   |                  | kop10@mail.ru              |
|                   |      78950902183 | nether_666@mail.ru         |
|                   |      71123123123 | test@test.ru               |
| Алексей           |      79190709976 | lility@mail.ru             |
| Даниил            |      79509115698 | Daniil_Lomako@rambler.ru   |
| Марина            |      79100773797 | kleo_sta@mail.ru           |
| Мария             |      79534261554 | maria270891@gmail.com      |
| Никита            |      79109446489 | shnl@inbox.ru              |
| Abramova Valeriia |      78915681997 | 79156819970@yandex.ru      |
| Afanasev Daniil   |      78953428127 | daniilafanasev69@gmail.com |
| Alberto Uglietti  |      79605996995 | albeugli@tin.it            |
| Alekseev Aleksey  |      79605194622 | koloyar40@gmail.com        |
| Alina Alina       |      79207475410 | 150889@inbox.ru            |
| Aliyev Elnur      |      79105887533 | elnuraliev99@yahoo.com     |
| An Hyogen         |      79109452547 | davidan6911@gmail.com      |
| Andriyanova Elena |      79066203399 | marlen_86@mail.ru          |
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


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 94.38% |
| Emails | 79.60% |



### Data sample
```
| names                   | phones          | emails                           |
|:------------------------|:----------------|:---------------------------------|
| ['Aliyev Elnur']        | ['79105887533'] | ['elnuraliev99@yahoo.com']       |
| ['Lukyanova Ekaterina'] | ['79157895555'] | ['klukyanova@me.com']            |
| ['Аблезова Минара']     | ['79105535945'] | ['minaret-25@yandex.ru']         |
| ['Абрамовa Мария']      | ['79051890699'] | ['masya-pretty@list.ru']         |
| ['Автономова Ирина']    | ['79509277656'] | ['irishka0607@yandex.ru']        |
| ['Агуреева Евгения']    | ['79207793525'] | ['ihtia1212@gmail.com']          |
| ['Амосов Николай']      | ['79109414372'] | ['nik_am@inbox.ru']              |
| ['Бажинов Алексей']     | ['79056245855'] | ['axis365@mail.ru']              |
| ['Барсукова Ирина']     | ['79531979118'] | ['denegkeena@mail.ru']           |
| ['Батова Анна']         | ['79109418773'] | ['anna5580@yandex.ru']           |
| ['Безжон Владислав']    | ['79202765626'] | ['tula393@yandex.ru']            |
| ['Березовская Алина']   | ['79509162013'] | ['asakuraalinsia@gmail.com']     |
| ['Борковская Ольга']    | ['79167231553'] | ['shirly666@ya.ru']              |
| ['Волкова Ольга']       | ['79629598998'] | ['olga84561@mail.ru']            |
| ['Гвоздева Анна']       | ['79534222234'] | ['gvozdevaanna9891@gmail.com']   |
| ['Голиков Илья']        | ['79509218958'] | ['ilysha.tula@gmail.com']        |
| ['Гурова Юлия']         | ['79534402250'] | ['solnce-yuliya@mail.ru']        |
| ['Дементьев Вадим']     | ['79207905139'] | ['vad.dementiev515@yandex.ru']   |
| ['Демченкова Елена']    | ['79639339394'] | ['demchenkova.lelya@mail.ru']    |
| ['Думнова Вероника']    | ['79207405557'] | ['dumnovaveronika494@gmail.com'] |
```