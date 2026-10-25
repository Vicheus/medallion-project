# Parsetron results

## About row data

> - File path: Гипермаркет_Леонардо_08_2024.csv
> - Total rows: 293779

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Номер телефона: double (nullable = true)
 |-- Адрес: string (nullable = true)

```

### Data sample
```
| ФИО                        | Почта   | Дата рождения   |   Номер телефона | Адрес   |
|:---------------------------|:--------|:----------------|-----------------:|:--------|
| Сарафанов Валерий          |         | 10.01.1986      |              nan |         |
| Кукольница Евгения         |         | 21.12.1980      |              nan |         |
| Павлова Галина             |         | 16.11.1981      |              nan |         |
| Шилина Татьяна             |         | 08.07.1988      |              nan |         |
| Конева Татьяна             |         | 16.01.1980      |              nan |         |
| Лапунова (Васильева) Елена |         | 94683600        |              nan |         |
| Шилова Юлия                |         | 02.08.2014      |              nan |         |
| Лапунов Вадим              |         | 17.12.1986      |              nan |         |
| Меджидова-Лычагина Елена   |         | 15.02.1977      |              nan |         |
| Гавриленко Тамара          |         | 29.02.1984      |              nan |         |
| Ибрагимова Венера          |         | 16.05.1987      |              nan |         |
| Струц Михаил               |         | 03.09.1992      |              nan |         |
| Викторова Таня             |         | 07.06.1988      |              nan |         |
| Скептик Андрей             |         | 08.04.1991      |              nan |         |
| Карпов Алекс               |         | 53298000        |              nan |         |
| Волгарева Юля              |         | 16.12.1982      |              nan |         |
| Моенко Инна                |         | 19.01.1991      |              nan |         |
| Ларионова Елена            |         | 13.05.1980      |              nan |         |
| Воробьева Александра       |         | 24.01.1985      |              nan |         |
| Волгарева(Спирина) Юлия    |         | 16.12.1982      |              nan |         |
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
 |-- birth_date: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.94% |
| Phones | 1.00% |
| Birth_date | 32.51% |
| Address | 42.77% |



### Data sample
```
| names                                                      | emails                        | phones          | birth_date   | address                                                                   |
|:-----------------------------------------------------------|:------------------------------|:----------------|:-------------|:--------------------------------------------------------------------------|
| ['Alarmигорь']                                             | ['garik.kovalenko@gmail.com'] |                 | 06.04.1986   |                                                                           |
| ['Aleksandrlobzinmail.Ruалександр']                        | ['aleksandr_lobzin@mail.ru']  |                 | 08.01.1985   | ['Таганрог']                                                              |
| ['Anastasiyaанастасия']                                    | ['aik539@mail.ru']            |                 |              | ['Екатеринбург']                                                          |
| ['Anmorisвасилий']                                         | ['dew_kras@mail.ru']          |                 | 29.07.1993   |                                                                           |
| ['Annaлыкова Анна']                                        | ['7843986@gmail.com']         |                 |              | ['Moscow Кисельный тупикdom 3str.1']                                      |
| ['Annaмаксина Анна']                                       | ['azulia25@gmail.com']        |                 | 22.08.1986   | ['129327 Москва енисейская ул.17 корп.1131']                              |
| ['Arshissaдяченко Мария']                                  | ['mi.diachenko@gmail.com']    |                 | 04.09.1994   | ['117042 Москва Плавский проезд']                                         |
| ['Elenaмитенко Елена']                                     | ['mitenkoelena@gmail.com']    |                 |              | ['Красногорск']                                                           |
| ['Elizabeth-Sanалександра']                                | ['sasha-ananas-2015@mail.ru'] |                 | 07.03.2001   |                                                                           |
| ['Elrinпатрушева Мария']                                   | ['elrinnuel@mail.ru']         |                 | 23.08.1994   | ['614088 Пермь Чердынская38-200']                                         |
| ['Fuenteкнязькова Анастасия']                              | ['knyazkova.nastya@mail.ru']  |                 | 06.10.1992   | ['652811 Осинники Победыд.38 кв.69']                                      |
| ['Funsheepеремеева Анастасия']                             | ['eremeeva.180492@gmail.com'] |                 | 17.04.1992   |                                                                           |
| ['Grinchхолодов Григорий']                                 | ['velzevyl88@mail.ru']        | ['79047538610'] | 31.10.1988   | ['400074 Волгоград ул.Социалистическая д.20а кв.3']                       |
| ['Gulsinaкучаева Гульсина']                                | ['ruslan5612@gmail.com']      |                 |              | ['460052 Оренбург Родимцева 16']                                          |
| ['Hashiriникулина Вероника']                               | ['nikhashiri@gmail.com']      |                 | 22.08.1991   | ['Хабаровск']                                                             |
| ['Irinaзязева Ирина']                                      | ['i.metel@bk.ru']             |                 |              | ['Москва самовывоз']                                                      |
| ['Ksydersбазылев Дмитрий']                                 | ['ksyders@mail.ru']           |                 | 13.09.1994   | ['Смоленск']                                                              |
| ['Lena.Eienapog']                                          | ['lena.elenapog@yandex.ru']   |                 |              |                                                                           |
| ['Lenafoфокина Елена']                                     | ['lenafo@narod.ru']           |                 |              | ['620073 Екатеринбург Академика Шварца']                                  |
| ['Luckyseaсолодухина Еленаелена Luckyseaсолодухина Елена'] | ['luckysea@yandex.ru']        |                 | 04.03.1981   | ['603000 Нижний Новгород603000 Нижний Новгород ул.Большая Покровская 56'] |
```