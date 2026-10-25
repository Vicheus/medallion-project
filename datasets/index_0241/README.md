# Parsetron results

## About row data

> - Code name: index_0241
> - File path: /media/user/SAMSUNG/Databases/index_0241/raw/auth.csv
> - Total rows: 13479

### Schema
```
root
 |-- vk_id: integer (nullable = true)
 |-- bdate: string (nullable = true)
 |-- email: string (nullable = true)
 |-- country: string (nullable = true)
 |-- city: string (nullable = true)
 |-- nickname: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)

```

### Data sample
```
|     vk_id | bdate      | email                        | country   | city             | nickname   | first_name   | last_name                       |
|----------:|:-----------|:-----------------------------|:----------|:-----------------|:-----------|:-------------|:--------------------------------|
|   3535791 | 13.9.1983  | Stalker_13@mail.ru           | Россия    | Москва           | Stalker_13 | Александр    | Урюпин                          |
| 611372770 | 10.8.1968  | PutyatinaEN@admlr.lipetsk.ru | NULL      | NULL             |            | Елена        | Путятина                        |
|   3636373 | 17.4.1981  | leysan-dsk@rambler.ru        | Россия    | Солнечногорск    |            | Лейсан       | Фатыхова                        |
|  38698656 | 17.1.1982  | Kristina.ugolnov@mail.ru     | Россия    | Лесосибирск      |            | Кристина     | Угольнова                       |
|  95580446 | 4.12.1993  | svko1293@gmail.com           | Россия    | Энгельс          |            | Светлана     | Янюшкина                        |
| 145262246 | 22.7.1988  | 79159901327@yandex.ru        | Россия    | Ярославль        |            | Светлана     | Веретенникова                   |
| 761131165 | 28.4.1952  | a.titarevka@mail.ru          | Россия    | Воронеж          |            | Геннадий     | Радченко                        |
| 372659355 | 23.11.1983 | rasputikov@rambler.ru        | Россия    | Магнитогорск     |            | Андрей       | Распутиков                      |
|  84193280 | 12.2.1978  | munse@mail.ru                | Россия    | NULL             |            | Руслан       | Павлов                          |
|  17599506 | 29.12.1985 | muska1985@mail.ru            | Россия    | Холмогоры        |            | Мария        | Хахилева                        |
|  38074235 | 18.7.1990  | bvolovatov@yandex.ru         | Россия    | Тула             |            | Борис        | Воловатов                       |
|  50986969 | 10.3.1965  | valentinasurovc@mail.ru      | Россия    | Бисерть          |            | Валентина    | Суровцева                       |
| 653201291 | 28.5.1986  | 1suntar@mail.ru              | NULL      | NULL             |            | Николай      | Александров                     |
| 526829565 | 22.6.1981  | MarkasovSA@gmail.com         | NULL      | NULL             |            | Сергей       | Маркасов                        |
|  33111021 | 19.3.1984  | natasha_200484@mail.ru       | Россия    | Калтасы          |            | Наталия      | Сапаева                         |
| 675258952 | 15.9.2007  | dondokov200270@gmail.com     | Россия    | Сосново-Озерское |            | Этигел       | Дондоков                        |
| 167399702 | 12.1.1973  | osnovatel73@mail.ru          | Россия    | Вологда          |            | Алексей      | Малахов                         |
| 784281478 | 1.2.2000   | ticshatrovo@mail.ru          | Россия    | Шатрово          |            | Тиц          | Шатровскогомуниципальногоокруга |
| 567643646 | 11.7.1989  | vikalevko@mail.ru            | NULL      | NULL             |            | Виктория     | Левко                           |
|  10750332 | 2.12.1993  | Cheb_kirill@mail.ru          | NULL      | NULL             |            | Кирилл       | Чебышев                         |
```

> - Code name: index_0241
> - File path: /media/user/SAMSUNG/Databases/index_0241/raw/users.csv
> - Total rows: 745819

### Schema
```
root
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- father_name: string (nullable = true)
 |-- password_hash: string (nullable = true)
 |-- birthday: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- phone_org: string (nullable = true)
 |-- phone_org_dop: string (nullable = true)
 |-- phone_mob: string (nullable = true)
 |-- inn: string (nullable = true)

```

### Data sample
```
| email                        | phone            | first_name    | last_name   | father_name      | password_hash                                                | birthday   | gender   | phone_org   | phone_org_dop   | phone_mob   | inn   |
|:-----------------------------|:-----------------|:--------------|:------------|:-----------------|:-------------------------------------------------------------|:-----------|:---------|:------------|:----------------|:------------|:------|
| 0000000000000000@mail.ru     | +7(831)212-12-12 | Иман          | Алихаджиева | Иссаевна         | $2y$13$GZXWpbuemXhwyQWVBtkzk.HHue2VfXv7CTTJDzr8MnMDJDcjrm0Lu | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 000000000003221wsq2@mail.ru  | +2(602)212-01-21 | Арби          | Асиев       | Баудиевич        | $2y$13$77UKxtXEZ9ohK1mYSxzaMOQ3QeotnpMwHKE3Z5pKMnAmb9nN6mHEO | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 00000000001sq2@mail.ru       | +7(651)242-34-23 | Исаков        | Исаков      | Магомедович      | $2y$13$8FS0/DQUVfPG1SzzoDO2yeFNkrL7DQtL6jQdXm5Mq6BFleNJRfdmq | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 000000000wsq2@mail.ru        | +7(564)198-45-34 | Индира        | Абдулаевна  | Ибрагимовна      | $2y$13$TAkwzH5T.fhP0ktAgH.lkOJHBUS.RGqLotT5UMwRJdgsNlBNXi/Fy | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 0000000jjjjjkkkkksq2@mail.ru | +7(981)212-12-12 | Луиза         | Вакаева     | Абдулаевна       | $2y$13$asYOpUwuXX52hqwhEj/YAO86MOvJf6krrKnhJgJTVCo7eXM9nz4oy | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 0000000q2@mail.ru            | +7(898)989-32-12 | Юнус          | Сулейманов  | Исаевич          | $2y$13$IsjeiP5w6iwyXqvc2bNbZuyDBsl6Mt8wXeL/72E/xzJcbqf2e69RS | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 000000116@inbox.ru           | +8(917)438-16-55 | Марина        | Ананина     | Александровна    | $2y$13$8lAP3X8..lwG1Oe6tsBhhu5is32ZbqJ8jX3wxlgtgNwOM1wYVK4AO | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 00000027@mail.ru             | +7(926)911-03-82 | Сергей        | Сенченко    | Васильевич       | $2y$13$7IjGOxvraQsmaV1l5KDAmepg4z8OT9L.QIn6bm.lpYcfoXRiq1uvK | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 000000q2@mail.ru             | +7(982)314-22-12 | Яха           | Алихаджиева | Усамовна         | $2y$13$M5mFriIFh5hopvHgsfLaV.KBl03FE2DLXQn8sBtZ4KgAaVf.ONMoy | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 0000175@bk.ru                | +7(955)000-01-75 | Александр     | Мутовкин    | Николаевич       | $2y$13$r41ynby9Rg6lowZfpNqtZeIe8wnfyqyraSU1MMZDOFxY4T6e6wu86 | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 00001@gts39.xyz              | +7(952)054-28-54 | Александр     | Вербицкий   | Анатольевич      | $2y$13$xiV3H9Iz3fW2F1d3Oi3dde0wbfMoTFW3kF3cF2KAt5/rEYJyebGz6 | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 0000556236@mail.ru           | +8(905)491-01-85 | Ольга         | Савина      | Владимировна     | $2y$13$lEhzahXhm3eYo1gKF.R1R..uVXTFtDgARbYxg9Yi1LLCmnQMoTvkK | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 0000770@rambler.ru           | +7(903)000-07-70 | Дмитрий       | Ибрагимов   | Равильевич       | $2y$13$MUFrXH8Yxu7E9EimawbEjO8AySxfTiEkUuhZCOZZCa1rSvxO2zB6K | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 0000@mail.ru                 | +7(916)000-00-00 | ббб           | ааа         | ввв              | $2y$13$txpmeVfPKK0uBOcJap8rXu9CTvD9JLv1q8V/y75Oo5g4twRyY..q6 | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 00@00.ru                     | +8(961)952-18-95 | жл            | лдолджл     | олдлолд          | $2y$13$/fULGSBceiobHMi.l3.LvuD6r2pY1qlLxSwsaifTS6v1a3Yb1/vFK | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 0000sdyuture@mail.ru         | +8(922)810-09-47 | Илья          | Архипов     | игоревич         | $2y$13$OQn1PZTzl9onw3KZDHo8RuSFwGgGPtFmPoY53I4dbJQ2w6HN0mPyq | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 000123456e@mail.ru           | +8(915)169-45-03 | Елена         | Рыжкова     | Николаевна       | $2y$13$nFzFkToLm8ws8GShMK35PO.5ACcKYC/9ILN46Uj1aYnoDsfz5/RDm | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 00017615i+10@gmail.com       | +7(922)058-88-67 | Хава          | Акиева      | Акиева Хава      | $2y$13$LnVWooYgtbBJcSp5dBs6lufYEqQjUXagpP79czaY/RjzL3/syVrcK | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 00017615i+11@gmail.com       | +7(937)592-00-20 | Амриева Элима | Эмпиема     | Амриева Элима    | $2y$13$2q3M7z50HgRtdnUHKGKYPuQavrArF/p0gAVvZ5hG6UCH8.B7gj4JW | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
| 00017615i+12@gmail.com       | +9(284)790-12-17 | Раяна         | Астамирова  | Раяна Астамирова | $2y$13$uqId6DoWYY/kDHtUlvu3FunfW.7O3uo9pnJnSiyWjvm6faF9vfUqO | NULL       | NULL     | NULL        | NULL            | NULL        | NULL  |
```


## About final data
> - Total rows: 552942

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- sex: integer (nullable = true)

```

### Data sample
```
| names                                 | emails                            | phones          | birth_date   | socials                                                          | address            | documents   |   sex |
|:--------------------------------------|:----------------------------------|:----------------|:-------------|:-----------------------------------------------------------------|:-------------------|:------------|------:|
| [' Ruslan']                           | ['rolex_x_08@mail.ru']            |                 | 27.02.1989   | [Row(title='ВКонтакте', id='67325651', link=None, comment=None)] | ['Россия Грозный'] |             |   nan |
| [' Ахматвалеева Фируза Сабирьяновна'] | ['akhmatvaleeva@mail.ru']         | ['79656482869'] |              |                                                                  |                    |             |   nan |
| [' Егорова Людмила Геннадьевна']      | ['legor47@yandex.ru']             | ['79113862648'] |              |                                                                  |                    |             |   nan |
| [' Шпуй Марина Александровна']        | ['mshpuy80@mail.ru']              |                 |              |                                                                  |                    |             |   nan |
| ['Abaszade Minaya Boyukaqa Kizi']     | ['minaya.abaszade83@gmail.com']   |                 |              |                                                                  |                    |             |   nan |
| ['Abdrakhmanov Rustam Искандарович']  | ['shiroyasha-98@mail.ru']         |                 |              |                                                                  |                    |             |   nan |
| ['Abdrzkva Ayyo Hhhzn']               | ['lola.mironova.921@mail.ru']     | ['79287390298'] |              |                                                                  |                    |             |   nan |
| ['Abdulaeva Heda Musluevna']          | ['abdulaeva998@bk.ru']            | ['79604401704'] |              |                                                                  |                    |             |   nan |
| ['Abdulazimov Israil Lechievich']     | ['israilabdulazimov85@gmail.com'] |                 |              |                                                                  |                    |             |   nan |
| ['Abdylhaidov Valid Umarovih']        | ['ymar1956@gmail.com']            | ['79288929921'] |              |                                                                  |                    |             |   nan |
| ['Abramovich Daniel Dosovicjh']       | ['ablgazaniar@yandex.ru']         |                 |              |                                                                  |                    |             |   nan |
| ['Abrarova Ilmira Rafilevna']         | ['ilmira_abrarova@mail.ru']       | ['79196020026'] |              |                                                                  |                    |             |   nan |
| ['Absb Svsva Sbsba']                  | ['cnsnana@mail.ru']               |                 |              |                                                                  |                    |             |   nan |
| ['Absbbs Sbsbab Sgags']               | ['avava@mail.ru']                 |                 |              |                                                                  |                    |             |   nan |
| ['Absbs Sbs S Sbbd']                  | ['wiei@mail.ru']                  | ['79193919293'] |              |                                                                  |                    |             |   nan |
| ['Absn Sbbsbc Dbns']                  | ['ahewikw@mail.ru']               | ['79193829034'] |              |                                                                  |                    |             |   nan |
| ['Abubakirova Amina Saithamzatovna']  | ['abbkrvs@gmail.com']             | ['79389090726'] |              |                                                                  |                    |             |   nan |
| ['Abuev Salah Zayndievich']           | ['gamemod9595@mail.ru']           | ['79635971440'] |              |                                                                  |                    |             |   nan |
| ['Abueva Makka Ruslanovna']           | ['makkaabueva@ickloud.com']       | ['79297920101'] |              |                                                                  |                    |             |   nan |
| ['Abz Anz Lom']                       | ['anzor1990a@gmail.com']          | ['79639844675'] |              |                                                                  |                    |             |   nan |
```