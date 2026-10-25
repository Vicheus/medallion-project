# Parsetron results

## About row data

> - File path: finterra.ru_2024.csv
> - Total rows: 150366

### Schema
```
root
 |-- Имя: string (nullable = true)
 |-- Телефон: long (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Сумма: double (nullable = true)

```

### Data sample
```
| Имя                  |     Телефон | Почта                         |    Сумма |
|:---------------------|------------:|:------------------------------|---------:|
| Сарапкина Елена      | 79274083238 | elena.sarapkina.76@mail.ru    |  5484.97 |
| Кораблева Любовь     | 79297291735 | lyubov.korableva.1975@mail.ru |   721.99 |
| Дырыгина Наталья     | 79274125778 | ndyrygina@mail.ru             |     0    |
| Мельникова Екатерина | 79274098400 | melnicovakaty@gmail.com       | 36178.8  |
| Филимонов Александр  | 79274109093 | alexsandr616@gmail.com        |     0    |
| Баранова Светлана    | 79600461818 | sbarnova@bk.ru                |     0    |
| Гуськова Наталья     | 79270313237 | natalya.guskova.2012@mail.ru  |  7589.18 |
| Бурдова Татьяна      | 79063264470 | burdova.tatyana@mail.ru       |     0    |
| Емельянов Артур      | 79600484906 | emelyanart@gmail.com          |    53.36 |
| Шлыков Геннадий      | 79274232047 | usfkazan@gmail.com            |  6109.65 |
| Гимаев Артур         | 79179337153 | aprivalov86@gmail.com         |     0    |
| Титова Марина        | 79178596332 | mmmarinat62@gmail.com         |  2457.21 |
| Пикмуллина Татьяна   | 79274403814 | tany.pik@gmail.com            |     0    |
| Еналиев Альберт      | 79178945120 | enaliev672@gmail.com          |     0    |
| Капустин Андрей      | 79152174672 | ckopo.ympy@gmail.com          |  8778.24 |
| Селиванов Вячеслав   | 79519271606 | bigslava123@gmail.com         |     0    |
| Еналиева Нурия       | 79173995449 | nuriya700enalieva@gmail.com   | 14904.7  |
| Мингалиева Алсу      | 79600449845 | alsoumin@gmail.com            |     0    |
| Волков Артур         | 79061415915 | arturwoolf.1989@gmail.com     |     0    |
| Шарифуллин Алмаз     | 79173976441 | almazaifara@gmail.com         |     0    |
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
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.98% |
| Phones | 99.97% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                    | emails                         | phones          | raw_metadata              |
|:-------------------------|:-------------------------------|:----------------|:--------------------------|
| ['Алексеев Андрей']      | ['andrey.dekorperm@gmail.com'] | ['79194903459'] | ['{"Сумма": "4381.66"}']  |
| ['Фирсов Василий']       | ['firsov.vasil@gmail.com']     | ['79055269061'] | ['{"Сумма": "0.0"}']      |
| ['Терещенко Эдуард']     | ['idilegko@gmail.com']         | ['79248140010'] | ['{"Сумма": "1850.11"}']  |
| ['Харитонов Антон']      | ['a.haritonov1986@gmail.com']  | ['79270764402'] | ['{"Сумма": "6366.68"}']  |
| ['Серебряков Дмитрий']   | ['duserebro@gmail.com']        | ['79227720421'] | ['{"Сумма": "0.0"}']      |
| ['Дудкина Елена']        | ['elenadudkinammm@gmail.com']  | ['79629223226'] | ['{"Сумма": "240.47"}']   |
| ['Хорунжина Эльвира']    | ['valena.555@mail.ru']         | ['79262249454'] | ['{"Сумма": "1598.27"}']  |
| ['Испирь Игорь']         | ['jobland@yandex.ru']          | ['79603463655'] | ['{"Сумма": "778.99"}']   |
| ['Березин Андрей']       | ['andreiberezinmmm@gmail.ru']  | ['79881726212'] | ['{"Сумма": "10728.96"}'] |
| ['Бублей Валентина']     | ['bubley34@gmail.com']         | ['79047774376'] | ['{"Сумма": "309.36"}']   |
| ['Борисенко Светлана']   | ['borisenkocapital@gmail.com'] | ['79093795209'] | ['{"Сумма": "41101.18"}'] |
| ['Котко Иван Сергеевич'] | ['ivankotko@gmail.com']        | ['79053316282'] | ['{"Сумма": "90.42"}']    |
| ['Бабинцев Александр']   | ['ya.bben@yandex.ru']          | ['79243640797'] | ['{"Сумма": "170.6"}']    |
| ['Кривых Татьяна']       | ['krivyh1955@mail.ru']         | ['79024453817'] | ['{"Сумма": "3160.01"}']  |
| ['Фролова Светлана']     | ['lanafrolova@inbox.ru']       | ['79138908313'] | ['{"Сумма": "5054.19"}']  |
| ['Котышков Сергей']      | ['sergeipavlovic78@gmail.com'] | ['79093899515'] | ['{"Сумма": "33933.33"}'] |
| ['Коротина Вера']        | ['verakorotina@gmail.com']     | ['79275062327'] | ['{"Сумма": "91.99"}']    |
| ['Берсенев Олег']        | ['olegbersenevmmm@gmail.com']  | ['79270545832'] | ['{"Сумма": "2392.99"}']  |
| ['Перухина Кристина']    | ['kristina02081992@gmail.com'] | ['79271372624'] | ['{"Сумма": "0.0"}']      |
| ['Данилова Татьяна']     | ['dantat80@gmail.com']         | ['79630779056'] | ['{"Сумма": "10062.79"}'] |
```