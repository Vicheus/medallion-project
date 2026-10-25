# Parsetron results

## About row data

> - Code name: index_0442
> - File path: weltrade.ru.csv
> - Total rows: 12733

### Schema
```
root
 |-- Name: string (nullable = true)
 |-- City: string (nullable = true)
 |-- Phone: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- Comment: string (nullable = true)
 |-- Balance: string (nullable = true)

```

### Data sample
```
| Name                             | City              | Phone         | Email                  | Comment       |   Balance |
|:---------------------------------|:------------------|:--------------|:-----------------------|:--------------|----------:|
| Чапаев Василий Иванович          | Москва            | -- no --      | kombat@inbox.ru        | СТАНДАРТ счет |      0    |
| Рыжов Константин Евгеньевич      | Обнинск           | +7 4843951280 | murman@obninsk.com     | СТАНДАРТ счет |      1.89 |
| Капариха Александр Александрович | Минск             | -- no --      | kapa51@rambler.ru      | СТАНДАРТ счет |      0    |
| Рудой Дмитрий Валерьевич         | Санкт - Петербург | -- no --      | volcoff@list.ru        | СТАНДАРТ счет |      1.1  |
| Сидоренко Елена Валерьевна       | Киев              | +380675003235 | elenasydorenko@mail.ru | СТАНДАРТ счет |      9.8  |
| Константин Рыжов                 | Обнинск           | -- 51280 --   | murman@obninsk.com     | СТАНДАРТ счет |      2.66 |
| Рыжов Константин Евгеньевич      | Обнинск           | +7 4843951280 | murman@obninsk.com     | СТАНДАРТ счет |      4.49 |
| Рыжов Сергей Евгеньевич          | Обнинск           | 48321         | murman@obninsk.com     | СТАНДАРТ счет |    107.99 |
| Кашпаренко Валерий Иванович      | Шымкент           | -- no --      | walera@ukonet.com      | СТАНДАРТ счет |      0.07 |
| Хузиахметов Марат Рафикович      | Норильск          | -- no --      | retro@nrd.ru           | СТАНДАРТ счет |      3.47 |
| rvchvt 4tyjt                     | tujjjtujrtj       | -- no --      | info@sms.biz.ua        | СТАНДАРТ счет |      8.26 |
| Турек Александр Александровиич   | Москва            | +79265716267  | alexturek@mail.ru      | СТАНДАРТ счет |      0.02 |
| Суханов Алексей                  | Челябинск         | +79097435609  | alsu1900@list.ru       | СТАНДАРТ счет |      0    |
| Евсеев Роман Петрович            | Новокузнецк       | -- no --      | erp1@yandex.ru         | СТАНДАРТ счет |      1.84 |
| Андрей Окороков                  | Черняховск        | +79316042595  | andru-69@mail.ru       | СТАНДАРТ счет |      0.04 |
| Тризно Наталья Александровна     | Минск             | -- no --      | henon@mail.ru          | СТАНДАРТ счет |      0    |
| Власов Валерий Васильевич        | Амурск            | -- no --      | vlasov@mail.amursk.ru  | СТАНДАРТ счет |      0    |
| Давыдов Андрей Алимович          | Чебоксары         | +79023288184  | andreydavidov@mail.ru  | СТАНДАРТ счет |      0    |
| Кондякова Елена Леонидовна       | Петербург         | -- no --      | andreans3006@yahoo.com | СТАНДАРТ счет |      0.08 |
| Dolin Vyacheslav                 | Vorkuta           | -- no --      | slavadlin@rambler.ru   | СТАНДАРТ счет |      0    |
```


## About final data
> - Total rows: 6752

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.94% |
| Phones | 47.47% |
| Address | 99.82% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                              | emails                     | phones          | address            | raw_metadata                                                                                                                                                                                                                                                                                    |
|:-----------------------------------|:---------------------------|:----------------|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Evgeniy Tkachenko']              | ['e.jeka.mail@gmail.com']  |                 | ['Vitebsk']        | ['{"Comment": "C поиска на Google МИНИ счет", "Balance": "62.75"}']                                                                                                                                                                                                                             |
| ['Jie Wang']                       | ['wangjie0503@yeah.net']   |                 | ['Sichuan']        | ['{"Comment": "123.116.108.12", "Balance": "10.49"}', '{"Comment": "123.116.108.12", "Balance": "0.00"}']                                                                                                                                                                                       |
| ['Wai Gao']                        | ['sky1688@126.com']        |                 | ['Shen Yang']      | ['{"Comment": "FREE account", "Balance": "0.00"}']                                                                                                                                                                                                                                              |
| ['Yu Zhao']                        | ['zyzyzzz2e@tom.com']      |                 | ['Beijing']        | ['{"Comment": "FREE account", "Balance": "0.00"}']                                                                                                                                                                                                                                              |
| ['Андрей Бадин']                   | ['czart91@yandex.ru']      | ['79084457610'] | ['Хабаровск']      | ['{"Comment": "МИКРО счет", "Balance": "51.20"}']                                                                                                                                                                                                                                               |
| ['Андрей Галузо']                  | ['andrey_galuzo@tyt.by']   |                 | ['Гомель']         | ['{"Comment": "МИКРО счет", "Balance": "3 103.44"}']                                                                                                                                                                                                                                            |
| ['Антипин Илья Вячеславович']      | ['alexander890@yandex.ru'] | ['74852474527'] | ['Ярославль']      | ['{"Comment": "МИКРО счет", "Balance": "0.00"}']                                                                                                                                                                                                                                                |
| ['Владимир Химко']                 | ['khimko@bigmir.net']      |                 | ['Киев']           | ['{"Comment": "МИНИ счет", "Balance": "0.00"}']                                                                                                                                                                                                                                                 |
| ['Владимр Добровольский']          | ['dobrovol_sky@mail.ru']   |                 | ['Киев']           | ['{"Comment": "МИКРО счет", "Balance": "0.00"}']                                                                                                                                                                                                                                                |
| ['Голованов Роман Сергеевич']      | ['htc276@mail.ru']         |                 | ['Краснознаменск'] | ['{"Comment": "МИНИ счет", "Balance": "35.20"}']                                                                                                                                                                                                                                                |
| ['Гренчак Владимир Николаевич']    | ['grenchak@mail.ru']       |                 | ['Синельниково']   | ['{"Comment": "МИКРО счет", "Balance": "62.30"}']                                                                                                                                                                                                                                               |
| ['Докучаев Андрей Владимирович']   | ['mysterikon@yahoo.com']   |                 | ['Печоры']         | ['{"Comment": "МИКРО счет", "Balance": "0.67"}']                                                                                                                                                                                                                                                |
| ['Зотов Игорь Алексеевич']         | ['zia6@mail.ru']           |                 | ['Красноярск']     | ['{"Comment": "МИКРО счет", "Balance": "0.64"}']                                                                                                                                                                                                                                                |
| ['Калинин Александр Геннадьевич']  | ['sharik200082@mail.ru']   | ['79279482826'] | ['Уфа']            | ['{"Comment": "МИКРО счет", "Balance": "0.00"}']                                                                                                                                                                                                                                                |
| ['Касьян Александр Викторович']    | ['cb153@yandex.ru']        |                 | ['Ейск']           | ['{"Comment": "МИКРО счет", "Balance": "65.19"}']                                                                                                                                                                                                                                               |
| ['Козляев Валерий Михайлович']     | ['waleriy3@yandex.ru']     |                 | ['Новосибирск']    | ['{"Comment": "МИНИ счет", "Balance": "88.94"}']                                                                                                                                                                                                                                                |
| ['Комисаров Сергей Александрович'] | ['siriys85@yahoo.com']     |                 | ['Москва']         | ['{"Comment": "МИКРО счет", "Balance": "18.51"}']                                                                                                                                                                                                                                               |
| ['Коптев Р.В.']                    | ['vasilish@samtel.ru']     |                 | ['Самара']         | ['{"Comment": "МИКРО счет", "Balance": "6.56"}']                                                                                                                                                                                                                                                |
| ['Лабутин Денис']                  | ['nitubal@list.ru']        |                 | ['Альметьевск']    | ['{"Comment": "МИКРО счет", "Balance": "17.36"}']                                                                                                                                                                                                                                               |
| ['Лилия Лучко']                    | ['inforexgroup@mail.ru']   | ['79258880636'] | ['пос Редкино']    | ['{"Comment": "МИНИ счет", "Balance": "46.20"}', '{"Comment": "МИНИ счет", "Balance": "0.00"}', '{"Comment": "МИНИ счет", "Balance": "7.17"}', '{"Comment": "МИНИ счет", "Balance": "0.25"}', '{"Comment": "СТАНДАРТ счет", "Balance": "0.00"}', '{"Comment": "МИНИ счет", "Balance": "0.05"}'] |
```