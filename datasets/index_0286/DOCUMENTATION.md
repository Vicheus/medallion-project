# Parsetron results

## About row data

> - Code name: index_0286
> - File path: /home/user/Documents/data/index_0286/raw/neroelectronics by/sale_buyers.csv
> - Total rows: 324

### Schema
```
root
 |-- Покупатель: string (nullable = true)
 |-- E-mail: string (nullable = true)
 |-- Телефон: string (nullable = true)
 |-- Дата регистрации: string (nullable = true)
 |-- Сайт: string (nullable = true)
 |-- Кол-во полностью оплаченных заказов: integer (nullable = true)
 |-- Кол-во частично оплаченных заказов: integer (nullable = true)
 |-- Сумма полученных оплат: string (nullable = true)

```

### Data sample
```
| Покупатель                | E-mail                         | Телефон            | Дата регистрации    | Сайт                                               |   Кол-во полностью оплаченных заказов |   Кол-во частично оплаченных заказов | Сумма полученных оплат   |
|:--------------------------|:-------------------------------|:-------------------|:--------------------|:---------------------------------------------------|--------------------------------------:|-------------------------------------:|:-------------------------|
| Reading                   | reading@mail.ru                |                    | 21.01.2020 13:28:15 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Татьяна Ведехина          | t.vedehina@neroelectronics.by  |                    | 27.12.2019 14:19:25 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Сергей                    | 1280455@gmail.com              | 80333010455        | 08.11.2024 12:40:13 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Вера Юркевич              | v.yurkevich@neroelectronics.by |                    | 04.05.2021 14:08:00 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Антон                     | anton_palmov@mail.ru           | +7 (909) 929-78-10 | 04.12.2023 02:05:44 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Олег Олейник              | belomor87@mail.ru              | 375298670180       | 18.07.2022 22:36:07 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Артем                     | tommy.vrb@gmail.com            | 375295513722       | 20.04.2022 12:05:51 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Сергей Афанасьев          | serg_pana@ngs.ru               | +7 923 125-80-75   | 11.01.2022 10:57:38 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Виктория                  | 9235267828@mail.ru             | 79235267828        | 14.01.2022 09:46:05 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Сергей                    | ktv023@yandex.ru               | 79374116206        | 11.01.2022 14:27:56 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Bjørn Knutsson            | bknutsson@hotmail.com          | +47 92247751       | 30.10.2021 10:06:40 | Nero Electronics — Intelligent IoT devices for hi- |                                     0 |                                    0 | €0.00                    |
| Giedrius Zujus            | zujus.giedrius@gmail.com       | 37068638004        | 04.10.2021 20:36:08 | Nero Electronics — Intelligent IoT devices for hi- |                                     0 |                                    0 | €0.00                    |
| Blaž Bizjak               | bizi25@gmail.com               | 38641859069        | 31.08.2021 21:01:44 | Nero Electronics — Intelligent IoT devices for hi- |                                     0 |                                    0 | €0.00                    |
| Сергей                    | sergikoffmeister@gmail.com     | 79269017223        | 20.07.2021 09:04:55 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Валерий Васильевич Багнюк | arka.nikolaev@gmail.com        | 380632782067       | 05.10.2020 17:29:07 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Михаил Архипов            | info@nerosk.ru                 |                    | 18.06.2019 13:55:15 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Илья Шалимов              | vamilash@yandex.com            | 79619299573        | 16.07.2020 13:12:16 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Ратибор Булатов           | admin@neroelectronics.by       | 375291111111       | 05.04.2018 17:25:55 | Nero Electronics — Умный учет | Автоматика         |                                     6 |                                    6 | €4,935.70                |
| Дмитрий                   | sda69@mail.ru                  | +7(903) 274-11-78  | 23.03.2020 11:28:23 | Nero Electronics — Умный учет | Автоматика         |                                     0 |                                    0 | €0.00                    |
| Jakob Buzan               | jakoxyking@hotmail.com         | +386 30 350 370    | 06.03.2020 12:45:51 | Nero Electronics — Intelligent IoT devices for hi- |                                     0 |                                    0 | €0.00                    |
```


## About final data
> - Total rows: 307

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- actuality: string (nullable = true)

```

### Columns completeness
```
{
    "names": 100.0,
    "emails": 100.0,
    "phones": 33.88,
    "actuality": 100.0
}
```

### Data sample
```
| names                         | emails                         | phones           | actuality   |
|:------------------------------|:-------------------------------|:-----------------|:------------|
| ['Сергей']                    | ['safemode@mail.ru']           |                  | 10.12.2021  |
| ['Алексей']                   | ['listogib34@mail.ru']         |                  | 26.02.2020  |
| ['Столбов Алексей Игоревич']  | ['stolbov@parnas.biz']         |                  | 30.09.2019  |
| ['Ирина']                     | ['i_4@mail.ru']                |                  | 12.09.2024  |
| ['Коко']                      | ['arheepoff@mail.ru']          |                  | 22.07.2019  |
| ['Андрей']                    | ['9398935@gmail.com']          |                  | 20.09.2020  |
| ['Дмитрий']                   | ['d.tsybulko@gmail.com']       | ['375296853263'] | 17.08.2022  |
| ['Евгений']                   | ['kasplast@mail.ru']           |                  | 19.06.2021  |
| ['Титит']                     | ['4534553@xn--s1af.tr']        |                  | 01.07.2019  |
| ['Валерий Васильевич Багнюк'] | ['arka.nikolaev@gmail.com']    |                  | 05.10.2020  |
| ['Михаил']                    | ['info@nerosk.ru']             |                  | 12.07.2019  |
| ['Алексей']                   | ['vinnift@gmail.com']          | ['375255057708'] | 17.06.2021  |
| ['Лошаков Сергей Васильевич'] | ['loshakovsergey62@gmail.com'] |                  | 19.12.2019  |
| ['Павел Джуро-Ковалевский']   | ['mybox-pasha@mail.ru']        |                  | 05.08.2021  |
| ['Сергей']                    | ['7063540@gmail.com']          | ['375297063540'] | 29.03.2024  |
| ['Михаил Архипов']            | ['info@nerosk.ru']             |                  | 18.06.2019  |
| ['Михаил']                    | ['arheepoff@mail.ru']          |                  | 18.07.2019  |
| ['Ирина']                     | ['ass@bk-cargo.ru']            |                  | 15.01.2025  |
| ['Сергей']                    | ['docen74@gmail.com']          | ['375296882110'] | 30.11.2023  |
| ['Елена']                     | ['hello@dishistudio.com']      |                  | 20.10.2020  |
```