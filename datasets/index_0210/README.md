# Parsetron results

## About row data

> - Code name: index_0210
> - File path: /media/user/Samsung T7/bd/index_0210/raw/onlinetrade.ru.txt
> - Total rows: 3618534

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Номер телефона: string (nullable = true)

```

### Data sample
```
| ФИО                     | Дата рождения   | Почта                          | Номер телефона   |
|:------------------------|:----------------|:-------------------------------|:-----------------|
| Kamran                  | 08.02.1991      | huseynov.kamran@hotmail.com    |                  |
| Николай                 |                 | nik123123@yandex.ru            |                  |
| Расул                   |                 | kanibadam2020@gmail.com        |                  |
| Екатерина               |                 | katanya-85@mail.ru             |                  |
| Дмитрий                 |                 | 9074356@mail.ru                |                  |
| ТАРАН ЛЮБОВЬ АЛЕКСЕЕВНА |                 | lubaivan@yandex.ru             |                  |
| Сергей                  |                 | gol-75@bk.ru                   |                  |
| Сергей                  |                 | belovserg90@yandex.ru          |                  |
| Брайченко Юрий          |                 | 1754828@mail.ru                |                  |
| Владимир                |                 | modeos210@gmail.com            |                  |
| Руслан                  | 20.07.1974      | rmustaev30@gmail.com           |                  |
| Wladimir49              |                 | Wolodir49@mail.ru              |                  |
| Леонид                  |                 | whiteteyka@rambler.ru          |                  |
| Алексей                 |                 | mr.akinthearmy@mail.ru         |                  |
| Михаил                  | 06.04.2002      | mihail.kol22@gmail.com         |                  |
| Svetlana                |                 | kvestor-1@mail.ru              |                  |
| Кристина                |                 | andreeujok1111@gmail.com       |                  |
| Олег                    |                 | 1osef0leg@gmail.com8           |                  |
| Максим                  |                 | nesterov471@inbox.ru           |                  |
| Наталия                 |                 | anatoliy.vinogradov.00@mail.ru |                  |
```


## About final data
> - Total rows: 3601417

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)

```

### Data sample
```
| names                              | emails                        | phones          | birth_date   |
|:-----------------------------------|:------------------------------|:----------------|:-------------|
| ['Олег']                           | ['kuzma07101974@gmail.com']   | ['79130770831'] | 07.10.1974   |
| ['Валерия']                        | ['lero4ka1236@mail.ru']       | ['79045782068'] | 16.10.1993   |
| ['Андрей']                         | ['andzolotov@gmail.com']      | ['79119277870'] | 19.04.1987   |
| ['Александр']                      | ['moi-komp@mail.ru']          | ['79125918732'] | 20.09.1991   |
| ['Николай']                        | ['ngomzov@yandex.ru']         | ['79308924477'] | 02.10.1979   |
| ['Lenormand']                      | ['lenormf@gmail.com']         | ['79313437773'] | 01.01.1980   |
| ['Екатерина']                      | ['larina.karinka@ya.ru']      | ['79689404546'] | 02.05.1979   |
| ['Максим Молодцов']                | ['molodcovmv@mail.ru']        | ['73519020586'] | 10.11.1972   |
| ['Укибаева Инна']                  | ['inna-buh2@mail.ru']         | ['79000782504'] | 01.01.1979   |
| ['Ильинов Денис']                  | ['illinov@mail.ru']           | ['79001249296'] | 18.01.1992   |
| ['Макс']                           | ['russian_max@mail.ru']       | ['79001280844'] | 19.05.1988   |
| ['Алексей Александрович Калюжный'] | ['akaluznyi1961@gmail.com']   | ['79001371489'] | 19.06.1961   |
| ['Светлана']                       | ['svetalade@mail.ru']         | ['79002593986'] | 23.12.1988   |
| ['Ярослав Бондарь']                | ['tashita88@mail.ru']         | ['79002939714'] | 30.07.1988   |
| ['Владимир']                       | ['gff33@mail.ru']             | ['79003699555'] | 19.04.1980   |
| ['Олег']                           | ['tslv.oleg@gmail.com']       | ['79005269295'] | 21.05.1995   |
| ['Александр']                      | ['bullet35rus@yandex.ru']     | ['79005369945'] | 25.09.1993   |
| ['Сергей']                         | ['toritsyn.sergei@yandex.ru'] | ['79005372610'] | 19.12.2019   |
| ['Сергей']                         | ['setextend@gmail.com']       | ['79005443497'] | 27.07.1988   |
| ['Алексей']                        | ['snake35rus@mail.ru']        | ['79005451015'] | 18.07.1986   |
```