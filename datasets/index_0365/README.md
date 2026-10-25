# Parsetron results

## About row data

> - Code name: index_0365
> - File path: fon_bet_2021.csv
> - Total rows: 253032

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Номер телефона: long (nullable = true)

```

### Data sample
```
| ФИО                  | Почта                      |   Номер телефона |
|:---------------------|:---------------------------|-----------------:|
| Константин           | T-XX@rambler.ru            |      79168181123 |
| Евгений Викторов     | evictorov@gmail.com        |      79165169802 |
| Стрелец Олег         | 9236862@mail.ru            |      79119236862 |
| bhjdfhi              | georg293@mail.ru           |      79629040162 |
| Иванов Борис         | aries.elein@rambler.ru     |      79045221999 |
| Резяпова Юлия        | littletrouble21@rambler.ru |      79269130755 |
| Анна                 | cheese_cat@mail.ru         |      79162474347 |
| Анна Чуйкина         | vesna095@yandex.ru         |      79265811093 |
| Ксения Крюкова       | neytron@hotmail.ru         |      79877890698 |
| Дербуш Екатерина     | Katrinderbush@yandex.ru    |      79533550715 |
| Лена                 | LenaVita@rambler.ru        |      79163564050 |
| Александр            | met82@rambler.ru           |      79111978730 |
| Иван                 | gruz89@inbox.ru            |      79117615466 |
| Веселовский Анатолий | tolan_a_v@mail.ru          |      79263982957 |
| Рыбаков Артем        | julx@front.ru              |      79264493399 |
| Сергей Боев          | vet-73@mail.ru             |      79603750441 |
| asif                 | sifac2@mail.ru             |      79163373140 |
| Демичев Игорь        | mr.y@bk.ru                 |      79215754480 |
| Ксения Никифорова    | Kody_ks@mail.ru            |      79055711340 |
| Анастасия            | angels84@rambler.ru        |      79039750736 |
```


## About final data
> - Total rows: 248708

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
| Emails | 99.88% |
| Phones | 99.99% |



### Data sample
```
| names                    | emails                         | phones          |
|:-------------------------|:-------------------------------|:----------------|
| ['Константин']           | ['t-xx@rambler.ru']            | ['79168181123'] |
| ['Евгений Викторов']     | ['evictorov@gmail.com']        | ['79165169802'] |
| ['Стрелец Олег']         | ['9236862@mail.ru']            | ['79119236862'] |
| ['Bhjdfhi']              | ['georg293@mail.ru']           | ['79629040162'] |
| ['Иванов Борис']         | ['aries.elein@rambler.ru']     | ['79045221999'] |
| ['Резяпова Юлия']        | ['littletrouble21@rambler.ru'] | ['79269130755'] |
| ['Анна']                 | ['cheese_cat@mail.ru']         | ['79162474347'] |
| ['Анна Чуйкина']         | ['vesna095@yandex.ru']         | ['79265811093'] |
| ['Ксения Крюкова']       | ['neytron@hotmail.ru']         | ['79877890698'] |
| ['Дербуш Екатерина']     | ['katrinderbush@yandex.ru']    | ['79533550715'] |
| ['Лена']                 | ['lenavita@rambler.ru']        | ['79163564050'] |
| ['Александр']            | ['met82@rambler.ru']           | ['79111978730'] |
| ['Иван']                 | ['gruz89@inbox.ru']            | ['79117615466'] |
| ['Веселовский Анатолий'] | ['tolan_a_v@mail.ru']          | ['79263982957'] |
| ['Рыбаков Артем']        | ['julx@front.ru']              | ['79264493399'] |
| ['Сергей Боев']          | ['vet-73@mail.ru']             | ['79603750441'] |
| ['Asif']                 | ['sifac2@mail.ru']             | ['79163373140'] |
| ['Демичев Игорь']        | ['mr.y@bk.ru']                 | ['79215754480'] |
| ['Ксения Никифорова']    | ['kody_ks@mail.ru']            | ['79055711340'] |
| ['Анастасия']            | ['angels84@rambler.ru']        | ['79039750736'] |
```