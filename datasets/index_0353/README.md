# Parsetron results

## About row data

> - Code name: index_0353
> - File path: клиенты_usurt_ru.csv
> - Total rows: 47192

### Schema
```
root
 |-- Электронная почта: string (nullable = true)
 |-- Имя: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Телефон: string (nullable = true)

```

### Data sample
```
| Электронная почта                       | Имя          | Фамилия     | Телефон         |
|:----------------------------------------|:-------------|:------------|:----------------|
| artamonova.ekaterina.16032003@yandex.ru | Екатерина    | Артамонова  | 79049593778     |
| lic-2-11a-nasibullina-adelina@yandex.ru | Аделина      | Насибуллина | +79046677067    |
| viktoriya.yazeva131285228234@gmail.com  | Виктория     | Язева       | 79776776519     |
| fedya_fedya_ivanov_2003_ivanov@mail.ru  | Фёедор       | Иванов      | 79874460470     |
| andrei.andrei-vinogradov1701@yandex.ru  | Андрей       | Виноградов  | +79152753038    |
| missis.melnikova-kseniya2002@yandex.ru  | Ксения       | Мельникова  | +79807423784    |
| mitrofanov.business.studying@gmail.com  | Дмитрий      | Митрофанов  | +79532493236    |
| iekatierina.miedviedieva.1999@mail.ru   | Екатерина    | Медведева   | 79998626945     |
| anastasiya.kovaleva.98.nastya@mail.ru   | Анастасия    | Ковалева    | 79276983820     |
| malich.kristino4ka.saveleva@gmail.com   | Кристина     | Самусеаа    | 8-952-999-92-94 |
| dasha.dmamontova2000.koroleva@mail.ru   | Дарья        | Мамонтова   | +79851158808    |
| anastasiia.alexandrovna.931@gmail.com   | Анастасия    | Казакова    | 79777093105     |
| mironova.masha-mironova2011@yandex.ru   | Мария        | Миронова    | 79020089818     |
| nastya.magic.dumbledore2018@gmail.com   | Анастасия    | Чарикова    | 79170365988     |
| maria.alekseevna.mikhailova@gmail.com   | Мария        | Михайлова   | +79870271508    |
| savelev_andrey_vladimirovich@mail.ru    | Андрей       | Савельев    | 79647354852     |
| matyushevskaya.ekaterina2@yandex.com    | Екатерина    | Матюшевская | +79156494849    |
| abdusaminovmuhammadaziz315@gmail.com    | Мухаммадазиз | Абдусаминов | +79265942051    |
| elkin.daniil.yaroslavovich@yandex.ru    | Даниил       | Елкин       | +79096438050    |
| 929000650dilshod.toshmatov@gmail.com    | Дилшоджон    | Тошматов    | 79097212118     |
```


## About final data
> - Total rows: 47152

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
| Emails | 98.03% |
| Phones | 98.05% |



### Data sample
```
| names                     | emails                               | phones          |
|:--------------------------|:-------------------------------------|:----------------|
| ['Капитанова Анастасия']  | ['anastasiyakapitanova02@gmail.com'] | ['79069178839'] |
| ['Комарова Татьяна']      | ['tanyaaaaa.komarova2002@gmail.com'] | ['79065060593'] |
| ['Акшанов Александр']     | ['sasha-aksh3.x.plane10@yandex.ru']  | ['79651438539'] |
| ['Микульшина Анастасия']  | ['anastasia.mikulshina@yandex.ru']   | ['79855838648'] |
| ['Ясинская Елизавета']    | ['yasinskaya.liza2003@yandex.ru']    | ['79851219425'] |
| ['Горбунова Диана']       | ['diana.gorbunowa2012@yandex.ru']    | ['79502592280'] |
| ['Прокопенко Светлана']   | ['sveta.prokopenko14@icloud.com']    | ['79058789750'] |
| ['Маркова Анастасия']     | ['anastasiamarkova725@gmail.com']    | ['79777746384'] |
| ['Иванов Иван']           | ['dagldiangrigorij070@yandex.ru']    | ['79081795291'] |
| ['Лебедев Дмитрий']       | ['dimonlebedev200325@gmail.com']     | ['79186755895'] |
| ['Рамазанова Валерия']    | ['lera.ramazanova.vr@gmail.com']     | ['79826651248'] |
| ['Саржевский Иван']       | ['sarzhevskiy.ivan.d@gmail.com']     | ['79283740917'] |
| ['Васильева Екатерина']   | ['vasileva.kate0708@yandex.ru']      | ['79157421303'] |
| ['Абдюханов Марат']       | ['abdyukhanov.marat@gmail.com']      | ['79851902307'] |
| ['Шувалова Анастасия']    | ['nastya.shuvalova.03@mail.ru']      | ['79262762740'] |
| ['Белянкина Ангелина']    | ['angelina.beliankina@mail.ru']      | ['79168084331'] |
| ['Ахмадиева Гулия']       | ['guliaahmadieva488@gmail.com']      | ['79870983905'] |
| ['Захарова Софья']        | ['sofia.zakharova1504@mail.ru']      | ['79101895328'] |
| ['Рождественский Никита'] | ['rozhdestvensky.n7@gmail.com']      | ['79851883688'] |
| ['Молдован Анастасия']    | ['nastya.moldovan03@gmail.com']      | ['79153194540'] |
```