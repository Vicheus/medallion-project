# Parsetron results

## About row data

> - Code name: index_0332
> - File path: philharmonia.spb.ru_2023.txt
> - Total rows: 219702

### Schema
```
root
 |-- Имя: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Почта: string (nullable = true)

```

### Data sample
```
| Имя       | Фамилия      | Почта                                           |
|:----------|:-------------|:------------------------------------------------|
| Оксана    | Стебакова    | Oksanastebakova@yandex.ru                       |
| Александр | Сычев        | 62177_vkontakte@philsystemmailaddr.ru           |
| Алина     | Ортон        | alinavanorton@mail.ru                           |
| Василий   | Крылосов     | vkrylosov@gmail.com                             |
|           |              | 556876428019925_facebook@philsystemmailaddr.ru  |
| Ирина     | Овсянникова  | yaroslav.latyshev@gmail.com                     |
| Артем     | Громов       | gromov-artem-88@mail.ru                         |
|           |              | sunanny@hotmail.com                             |
| Thomas    | Saurin       | thomassaurin@gmail.com                          |
|           |              | 2029638987052413_facebook@philsystemmailaddr.ru |
| Ольга     | Иванова      | olivbuh@gmail.com                               |
| Мазурек   | Виктор       | victor.a.mazurek@gmail.com                      |
| Ksenia    | Samusenko    | secretariat@pomor.org                           |
| Мария     | Кочуланова   | holamarymar@gmail.com                           |
| фонРозен  | Александр    | alex@von.rosen.red                              |
| Светлана  | Комиссарова  | lanamirovabg@yandex.ru                          |
|           |              | 1726571290715600_facebook@philsystemmailaddr.ru |
| Наталья   | Федорова     | Nvafedorova@mail.ru                             |
| Алина     | Тимиргазиева | laragazzagann@mail.ru                           |
| Артем     | Ляхов        | vasquezj@mail.ru                                |
```


## About final data
> - Total rows: 205195

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)

```

### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |


### Data sample
```
| names                  | emails                            |
|:-----------------------|:----------------------------------|
| ['Андрей Атясов']      | ['atyasovav@yandex.ru']           |
| ['Юрий Шония']         | ['shoniya1982@icloud.com']        |
| ['Марина Николаева']   | ['alexxandra7@mail.ru']           |
| ['Name Surname']       | ['filebox1500@mail.ru']           |
| ['Александра Жукова']  | ['kosc.info@mail.ru']             |
| ['Людмила Васильева']  | ['l2703508@yandex.ru']            |
| ['Юлия Абаева']        | ['julianna90@mail.ru']            |
| ['Марина Маслова']     | ['marmas2009@rambler.ru']         |
| ['Анна Милехина']      | ['annmilekhina@mail.ru']          |
| ['Валентина Татарчук'] | ['valentina-tatarchuk@yandex.ru'] |
| ['Анна Зорина']        | ['m-kuku.anna@yandex.ru']         |
| ['Ольга Сошникова']    | ['ops63po@list.ru']               |
| ['Элеонора Арнет']     | ['norik59@mail.ru']               |
| ['Иван Пономарев']     | ['iponlyme@rambler.ru']           |
| ['Алена Г']            | ['9500486130@mail.ru']            |
| ['Марина Лохматова']   | ['lokhmatova@rambler.ru']         |
| ['Марина Стеревцева']  | ['msterkh@gmail.com']             |
| ['Татьяна Табачок']    | ['nickoevans@mail.ru']            |
| ['Кристина Яничкина']  | ['doggy_morsh@mail.ru']           |
| ['Татьяна Харитонова'] | ['tanhar74@mail.ru']              |
```