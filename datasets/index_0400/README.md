# Parsetron results

## About row data

> - Code name: index_0400
> - File path: iw-shop.ru.txt
> - Total rows: 18399

### Schema
```
root
 |-- IP: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Адрес: string (nullable = true)
 |-- Имя: string (nullable = true)
 |-- Фамилия: string (nullable = true)

```

### Data sample
```
| IP              | Почта                     | Адрес                               | Имя       | Фамилия     |
|:----------------|:--------------------------|:------------------------------------|:----------|:------------|
| 107.178.47.3    |                           |                                     | Владислав | Волохов     |
| 108.171.128.175 | labrador_87@mail.ru       | Симферопольский бульвар д.10 к 1    | Сергей    | Орищин      |
| 108.171.129.167 |                           | Москва, 3-я Прядильная, 13к1, кв.65 | Алексей   | Кочетов     |
| 108.171.129.167 |                           | Плетешковский пер 2                 | Антон     | Аржановский |
| 108.171.129.167 | opekunov.victor@gmail.com | 115114,                             | Михаил    | Моршин      |
| 108.171.133.174 |                           | 462278                              | Олег      | Гуридов     |
| 109.110.66.5    |                           | Москва,                             | Алексей   | Баталов     |
| 109.111.150.199 |                           | Новаторов 36-1-130                  | Ольга     | Паламарчук  |
| 109.124.212.82  |                           |                                     | Качанов   | Александр   |
| 109.124.91.102  | Meridasin@yandex.ru       |                                     | Антон     | Аржановский |
| 109.126.222.148 |                           | цурюпы д.28                         |           | СЕВА        |
| 109.126.225.152 | alga-travel@hotmail.com   | 1-я владимирская д56 кв78           |           | Александр   |
| 109.126.226.199 |                           |                                     | Алексей   | Левченко    |
| 109.126.229.246 |                           | ул. Искры, д.13/1                   | Елена     | Боклашова   |
| 109.126.234.68  | grishin.artem@gmail.com   | Москва, ул. Нагатинская 16          | Антон     | Болтенков   |
| 109.126.243.44  | vasikov@bk.ru             |                                     |           | Сергей      |
| 109.127.163.242 | porsus@rambler.ru         | 2 Южнопортовый проезд 13 кв 1       | Ольга     | Иванова     |
| 109.161.33.186  | skirdokvas@yandex.ru      |                                     | Ирина     | Озупис      |
| 109.165.59.74   |                           |                                     | Ирина     | Суслина     |
| 109.168.156.217 |                           | Ставропольский                      | Светлана  | Зенько      |
```


## About final data
> - Total rows: 6430

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: void (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |
| Address | 79.75% |
| Ips | 100.00% |



### Data sample
```
| names                     | emails                        | address                             | ips                                    |
|:--------------------------|:------------------------------|:------------------------------------|:---------------------------------------|
| ['Станислав']             | ['a.chernomordova@gmail.com'] | ['ул.Щукинская д.5 стр.2 офис 312'] | [Row(ip='79.164.30.87', date=None)]    |
| ['Алексей Музолев']       | ['alek83@mail.ru']            |                                     | [Row(ip='62.213.119.53', date=None)]   |
| ['Яшкин Леонид']          | ['alekc_k2002@mail.ru']       | ['Варшавское ш.rnдом 47 корп. 4']   | [Row(ip='77.105.189.120', date=None)]  |
| ['Кирилл']                | ['amura1988@mail.ru']         | ['Пресненская']                     | [Row(ip='109.188.124.142', date=None)] |
| ['Дудина-Садовская Анна'] | ['antipova.ieva@mail.ru']     | ['Бережковская наб. 4 кв 107']      | [Row(ip='195.98.177.86', date=None)]   |
| ['Мальцев Андрей']        | ['avvish@mail.ru']            | ['2-й Неопалимовский переулок 10']  | [Row(ip='78.36.5.192', date=None)]     |
| ['Иноземцев Андрей']      | ['crysis90.93@mail.ru']       | ['Москва']                          | [Row(ip='83.167.105.181', date=None)]  |
| ['Анна П']                | ['dasharahmanova@mail.ru']    | ['Москва']                          | [Row(ip='212.42.48.99', date=None)]    |
| ['Михеев Андрей']         | ['dmitriy_kryl@mail.ru']      | ['м.Проспект']                      | [Row(ip='188.94.229.206', date=None)]  |
| ['Горябин Максим']        | ['esco_100@rambler.ru']       | ['Москва']                          | [Row(ip='195.230.70.225', date=None)]  |
| ['Виталий']               | ['ggubanov.68@mail.ru']       | ['Москва']                          | [Row(ip='83.149.8.90', date=None)]     |
| ['Вохмин Андрей']         | ['gvst1st@yandex.ru']         |                                     | [Row(ip='91.77.159.80', date=None)]    |
| ['Баранова Марья']        | ['horor-73@mail.ru']          | ['Воркута Ул.Нагорная Д.21 Кв.73']  | [Row(ip='83.149.8.155', date=None)]    |
| ['Илья Большов']          | ['ilya-bol@yandex.ru']        | ['м. Коньковоrnв рабочее время']    | [Row(ip='85.21.152.243', date=None)]   |
| ['Тучинский Петр']        | ['keet86@mail.ru']            | ['Москва']                          | [Row(ip='81.26.152.27', date=None)]    |
| ['Рыкова Юлия']           | ['lapisinka@bk.ru']           | ['г.Москва']                        | [Row(ip='185.95.107.194', date=None)]  |
| ['Виталий']               | ['lema.tatrieva@mail.ru']     | ['Ставропольский']                  | [Row(ip='94.29.123.202', date=None)]   |
| ['Кузьмин А.А.']          | ['lexus88391@rambler.ru']     | ['Мичуринский']                     | [Row(ip='178.176.86.71', date=None)]   |
| ['Вики Александр']        | ['lukalister@yandex.ru']      | ['Пр-т Академика Сахарова 12']      | [Row(ip='91.77.231.130', date=None)]   |
| ['Самаруха Илья']         | ['madamzolly@yandex.ru']      | ['Байкальская 17 кор.1 кв.15']      | [Row(ip='95.25.204.193', date=None)]   |
```