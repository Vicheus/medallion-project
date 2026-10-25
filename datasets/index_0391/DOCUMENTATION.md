# Parsetron results

## About row data

> - File path: iglobe_clean.csv
> - Total rows: 795764

### Schema
```
root
 |-- LastName: string (nullable = true)
 |-- FirstName: string (nullable = true)
 |-- Phone: string (nullable = true)
 |-- Email: string (nullable = true)

```

### Data sample
```
| LastName     | FirstName   |       Phone | Email                             |
|:-------------|:------------|------------:|:----------------------------------|
| Какулин      | Андрей      | 79198391869 | kakulin.andrei@yandex.ru          |
| Датий        | Сергей      | 79686852575 | nastya-datij@mail.ru              |
| Смирнова     | Анна        | 79117947007 | lounici.anna@gmail.com            |
| Михралиева   | Сафура      | 79282199839 | zari.m98@mail.ru                  |
| Кичигина     | Ксения      | 79814472940 | kichigina.ki@gmail.com            |
| Воробьева    | Наталья     | 79824702667 | natalyayrievnavorobieva@yandex.ru |
| Кузнецова    | Дарья       | 79207833967 | elena2014.kuznetsowa@yandex.ru    |
| Харьков      | Сергей      | 79260218926 | svharkow@mail.ru                  |
| Борисова     | Галина      | 79164408651 | vbirf1@bk.ru                      |
| Потапушин    | Николай     | 79167850779 | rak20844@gmail.com                |
| Тимонина     | Алёна       | 79119193338 | talena4@yandex.ru                 |
| Комиссаренко | Роман       | 79204440411 | klien@mail.ru                     |
| Пушкина      | Людмила     | 79212065593 | max.m.ivanov@gmail.com            |
| Асирян       | Карине      | 79629537999 | asiryan1@mail.ru                  |
| Агафонов     | Даниил      | 79500242424 | talena4@yandex.ru                 |
| Макарова     | Екатерина   | 79217582556 | 25121312wk03@mail.ru              |
| Мотова       | Елена       | 79023080529 | leladas@yandex.ru                 |
| Shatko       | TATIANA     | 79219726818 | roditeli1@hotmail.com             |
| Ружинская    | Ольга       | 79787037992 | Sansanich2@i.ua                   |
| Потехина     | Александра  |  9175479442 | Veraforever@gmail.com             |
```


## About final data

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
| Emails | 89.01% |
| Phones | 99.45% |



### Data sample
```
| names                   | emails                                | phones          |
|:------------------------|:--------------------------------------|:----------------|
| ['Какулин Андрей']      | ['kakulin.andrei@yandex.ru']          | ['79198391869'] |
| ['Датий Сергей']        | ['nastya-datij@mail.ru']              | ['79686852575'] |
| ['Смирнова Анна']       | ['lounici.anna@gmail.com']            | ['79117947007'] |
| ['Михралиева Сафура']   | ['zari.m98@mail.ru']                  | ['79282199839'] |
| ['Кичигина Ксения']     | ['kichigina.ki@gmail.com']            | ['79814472940'] |
| ['Воробьева Наталья']   | ['natalyayrievnavorobieva@yandex.ru'] | ['79824702667'] |
| ['Кузнецова Дарья']     | ['elena2014.kuznetsowa@yandex.ru']    | ['79207833967'] |
| ['Харьков Сергей']      | ['svharkow@mail.ru']                  | ['79260218926'] |
| ['Борисова Галина']     | ['vbirf1@bk.ru']                      | ['79164408651'] |
| ['Потапушин Николай']   | ['rak20844@gmail.com']                | ['79167850779'] |
| ['Тимонина Алёна']      | ['talena4@yandex.ru']                 | ['79119193338'] |
| ['Комиссаренко Роман']  | ['klien@mail.ru']                     | ['79204440411'] |
| ['Пушкина Людмила']     | ['max.m.ivanov@gmail.com']            | ['79212065593'] |
| ['Асирян Карине']       | ['asiryan1@mail.ru']                  | ['79629537999'] |
| ['Агафонов Даниил']     | ['talena4@yandex.ru']                 | ['79500242424'] |
| ['Макарова Екатерина']  | ['25121312wk03@mail.ru']              | ['79217582556'] |
| ['Мотова Елена']        | ['leladas@yandex.ru']                 | ['79023080529'] |
| ['Shatko Tatiana']      | ['roditeli1@hotmail.com']             | ['79219726818'] |
| ['Ружинская Ольга']     | ['sansanich2@i.ua']                   | ['79787037992'] |
| ['Потехина Александра'] | ['veraforever@gmail.com']             | ['79175479442'] |
```