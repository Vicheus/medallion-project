# Parsetron results

## About row data

> - File path: клиенты_ProPostuplenie_ru.csv
> - Total rows: 497278

### Schema
```
root
 |-- Электронная почта: string (nullable = true)
 |-- Имя пользователя: string (nullable = true)
 |-- Телефон: string (nullable = true)
 |-- Кто: string (nullable = true)
 |-- Номер класса: integer (nullable = true)

```

### Data sample
```
| Электронная почта          | Имя пользователя   | Телефон                | Кто     |   Номер класса |
|:---------------------------|:-------------------|:-----------------------|:--------|---------------:|
| deathsoul95@mail.ru        | Яэль Сахаровская   | +7 (906) 335 - 35 - 39 | student |            nan |
| yael18@mail.ru             | Яэль Косарева      | +7 (926) 677 - 97 - 49 | child   |             10 |
| rgjuli@yandex.ru           | Яэль Валциньш      | +7 (911) 843 - 31 - 43 | child   |              8 |
| myrensiy@mail.ru           | Ящиков Мария       | +7 (960) 269 - 03 - 68 | parent  |             11 |
| Yashenko.natali@yandex.ru  | Ященко Наталья     | +7 (916) 594 - 62 - 29 | parent  |              7 |
| beblack903@gmail.com       | Ященко Анастасия   | +7 (708) 531 - 23 - 81 | child   |             11 |
| yashukhin98@gmai.com       | Яшухин Никита      | +7 (912) 033 - 98 - 33 | child   |             11 |
| yyarik2104@gmail.com       | Яшуков Ярослав     | +7 (910) 915 - 30 - 06 | child   |             11 |
| yashuginaMV@wsr.ru         | Яшугина Марина     | +7 (913) 202 - 40 - 86 | parent  |              9 |
| an.yashkov@gmail.com       | Яшков Анатолий     | +7 (911) 102 - 32 - 29 | parent  |             11 |
| 8092050@bk.ru              | Яшкирдык Нуркила   | +7 (999) 666 - 88 - 93 | child   |             11 |
| fpk2@mail.ru               | Яшкин Петр         |                        | child   |             11 |
| peterduvrovsky@yandex.ru   | Яшкин Дементий     | +7 (911) 338 - 76 - 87 | child   |             11 |
| dredded7@gmail.com         | Яшка Фёдоров       | +7 (951) 172 - 91 - 70 | child   |              9 |
| YULA-9981@list.ru          | Яшина Юлия         | +7 (912) 051 - 32 - 11 | parent  |              9 |
| tata78.00@mail.ru          | Яшина Наталья      | +7 (920) 015 - 65 - 80 | parent  |             10 |
| Yashinamasha2006@gmail.com | Яшина Мария        | +7 (977) 297 - 65 - 58 | child   |              1 |
| yashina.nina30@yandex.ru   | Яшина Мария        | +7 (911) 344 - 53 - 92 | child   |             10 |
| 89162703737@mail.ru        | Яшина Елена        | +7 (916) 270 - 37 - 37 | parent  |             11 |
| key_keyk@mail.ru           | Яшина Екатерина    | +7 (951) 999 - 89 - 17 | child   |             10 |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- children: boolean (nullable = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Children | 100.00% |
| Phones | 93.50% |
| Emails | 99.97% |



### Data sample
```
| names                | children   | phones          | emails                         |
|:---------------------|:-----------|:----------------|:-------------------------------|
| ['Яэль Сахаровская'] | False      | ['79063353539'] | ['deathsoul95@mail.ru']        |
| ['Яэль Косарева']    | False      | ['79266779749'] | ['yael18@mail.ru']             |
| ['Яэль Валциньш']    | False      | ['79118433143'] | ['rgjuli@yandex.ru']           |
| ['Ящиков Мария']     | True       | ['79602690368'] | ['myrensiy@mail.ru']           |
| ['Ященко Наталья']   | True       | ['79165946229'] | ['yashenko.natali@yandex.ru']  |
| ['Ященко Анастасия'] | False      |                 | ['beblack903@gmail.com']       |
| ['Яшухин Никита']    | False      | ['79120339833'] | ['yashukhin98@gmai.com']       |
| ['Яшуков Ярослав']   | False      | ['79109153006'] | ['yyarik2104@gmail.com']       |
| ['Яшугина Марина']   | True       | ['79132024086'] | ['yashuginamv@wsr.ru']         |
| ['Яшков Анатолий']   | True       | ['79111023229'] | ['an.yashkov@gmail.com']       |
| ['Яшкирдык Нуркила'] | False      | ['79996668893'] | ['8092050@bk.ru']              |
| ['Яшкин Петр']       | False      |                 | ['fpk2@mail.ru']               |
| ['Яшкин Дементий']   | False      | ['79113387687'] | ['peterduvrovsky@yandex.ru']   |
| ['Яшка Фёдоров']     | False      | ['79511729170'] | ['dredded7@gmail.com']         |
| ['Яшина Юлия']       | True       | ['79120513211'] | ['yula-9981@list.ru']          |
| ['Яшина Наталья']    | True       | ['79200156580'] | ['tata78.00@mail.ru']          |
| ['Яшина Мария']      | False      | ['79772976558'] | ['yashinamasha2006@gmail.com'] |
| ['Яшина Мария']      | False      | ['79113445392'] | ['yashina.nina30@yandex.ru']   |
| ['Яшина Елена']      | True       | ['79162703737'] | ['89162703737@mail.ru']        |
| ['Яшина Екатерина']  | False      | ['79519998917'] | ['key_keyk@mail.ru']           |
```