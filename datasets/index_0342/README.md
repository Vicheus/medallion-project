# Parsetron results

## About row data

> - Code name: index_0342
> - File path: клиенты_enjoyspa_ru.csv
> - Total rows: 170202

### Schema
```
root
 |-- Имя: string (nullable = true)
 |-- Телефон: string (nullable = true)
 |-- Почта: string (nullable = true)

```

### Data sample
```
| Имя                            |     Телефон | Почта                           |
|:-------------------------------|------------:|:--------------------------------|
| Попрыгушина Наталья Викторовна | 79263395379 | tysia@yandex.ru                 |
| ГРИНЧИШИНА РОКСОЛАНА СЕРГЕЕВНА | 79651089898 | roksfrut@mail.ru                |
| Марина Александровна Сеничева  | 79154542423 | musy.89@mail.ru                 |
| Гурщенкова Татьяна Валерьевна  | 79151267394 | tania77772@mail.ru              |
| Ерохина Алена Александровна    | 79031934548 | alena_m_87@bk.ru                |
| Бояркина Татьяна Николаевна    | 79225384778 | tatiana_karetnikova@mail.ru     |
| Юлианна Скальнова Юлианна      | 79159899201 | yulianna.spatar2017@gmail.com   |
| Anastasiya Snyatovskaya        | 79646408558 | nasteriya@gmail.com             |
| Никитина Юлия Олеговна         | 79036255554 | samsnta_kiss@mail.ru            |
| Коваль Ирина Сергеевна         | 79661545120 |                                 |
| Мария Олеговна Степина         | 79308971922 | kroxinadetka@gmail.com          |
| Петровская Александра          | 79854243577 | 89166328453s@gmail.com          |
| Татьяна Сухоребрикова          | 79873504715 | tanya.sukhorebrikova.00@mail.ru |
| Кристина Перекальская          | 79962043550 | k_perekalskaya@mail.ru          |
| Маргарита Жаворонкова          | 79688883131 | zhavoronkova_official@mail.ru   |
| Анастасия Овсянникова          | 79151252626 | kulevskajaanastasija@gmail.com  |
| Анастасия Ладейщикова          | 79258616316 | ladia2001@icloud.com            |
| Крапеницкая Екатерина          | 79854725862 | casyxe@mail.ru                  |
| Анастасия Елифанкина           | 79250861147 | funky2213@gmail.com             |
| Boanerg?s Emmanuella           | 79683715895 | viossie@bk.fr                   |
```


## About final data
> - Total rows: 170007

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
| Phones | 98.27% |
| Emails | 93.33% |



### Data sample
```
| names                              | phones          | emails                              |
|:-----------------------------------|:----------------|:------------------------------------|
| ['Попрыгушина Наталья Викторовна'] | ['79263395379'] | ['tysia@yandex.ru']                 |
| ['Гринчишина Роксолана Сергеевна'] | ['79651089898'] | ['roksfrut@mail.ru']                |
| ['Марина Александровна Сеничева']  | ['79154542423'] | ['musy.89@mail.ru']                 |
| ['Гурщенкова Татьяна Валерьевна']  | ['79151267394'] | ['tania77772@mail.ru']              |
| ['Ерохина Алена Александровна']    | ['79031934548'] | ['alena_m_87@bk.ru']                |
| ['Бояркина Татьяна Николаевна']    | ['79225384778'] | ['tatiana_karetnikova@mail.ru']     |
| ['Юлианна Скальнова Юлианна']      | ['79159899201'] | ['yulianna.spatar2017@gmail.com']   |
| ['Anastasiya Snyatovskaya']        | ['79646408558'] | ['nasteriya@gmail.com']             |
| ['Никитина Юлия Олеговна']         | ['79036255554'] | ['samsnta_kiss@mail.ru']            |
| ['Коваль Ирина Сергеевна']         | ['79661545120'] |                                     |
| ['Мария Олеговна Степина']         | ['79308971922'] | ['kroxinadetka@gmail.com']          |
| ['Петровская Александра']          | ['79854243577'] | ['89166328453s@gmail.com']          |
| ['Татьяна Сухоребрикова']          | ['79873504715'] | ['tanya.sukhorebrikova.00@mail.ru'] |
| ['Кристина Перекальская']          | ['79962043550'] | ['k_perekalskaya@mail.ru']          |
| ['Маргарита Жаворонкова']          | ['79688883131'] | ['zhavoronkova_official@mail.ru']   |
| ['Анастасия Овсянникова']          | ['79151252626'] | ['kulevskajaanastasija@gmail.com']  |
| ['Анастасия Ладейщикова']          | ['79258616316'] | ['ladia2001@icloud.com']            |
| ['Крапеницкая Екатерина']          | ['79854725862'] | ['casyxe@mail.ru']                  |
| ['Анастасия Елифанкина']           | ['79250861147'] | ['funky2213@gmail.com']             |
| ['Boanergs Emmanuella']            | ['79683715895'] | ['viossie@bk.fr']                   |
```