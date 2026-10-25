# Parsetron results

## About row data

> - File path: ru_cdek_client_phone_38m_2022.csv
> - Total rows: 38917973

### Schema
```
root
 |-- name: string (nullable = true)
 |-- emails: string (nullable = true)
 |-- phones: string (nullable = true)

```

### Data sample
```
| name                               | emails                       | phones       |
|:-----------------------------------|:-----------------------------|:-------------|
| H&M 632                            |                              | Телефон1     |
| Abazov Zaur Adalbievich            |                              | ||9996450109 |
| Афоньшина Наталья                  | natasha81_44@mail.ru         | ||9969409855 |
| Надежда Лисина                     | lisina.nadejda2011@yandex.ru | ||9961951736 |
| KARLOVYCH IVAN                     |                              | ||9897289812 |
| Кайдарова Юлия                     | ecotrio.7570@woodfun.ru      | ||9852592232 |
| Sergey Chekanov                    | 2331888@gmail.com            | ||9852331888 |
| зиновьева людмила                  | ludmila692@yandex.ru         | ||9852136619 |
| Французов Лев                      |                              | ||9829034041 |
| Бейлис Людмила Борисовна           | mila.bejlis.37@mail.ru       | ||9780739070 |
| Юлия Секретарева                   | multcafe.korolev@gmail.com   | ||9779905976 |
| Сало Ирина Александровна           | chigik81@mail.ru             | ||9778068381 |
| ИП Огульник Виктория               | pokupkisp@gmail.com          | ||9772922085 |
| Получатель Дрожжачих Александр     |                              | ||9772710042 |
| Krasilshikov Kirill Urevich        |                              | ||9771777180 |
| Игнатенко Евгения                  | e-ewgeniya@mail.ru           | ||9687977915 |
| Православная классическая гимназия | ecotrio.7618@woodfun.ru      | ||9674859436 |
| Сегал Светлана                     | segal_sv_73@mail.ru          | ||9636498927 |
| Nadezhda Skrypnik                  |                              | ||9624444844 |
| Иван Тарасенко                     | ivantarasen@yandex.ru        | ||9617927827 |
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

```



### Data sample
```
| names                              | emails                            | phones          |
|:-----------------------------------|:----------------------------------|:----------------|
| ['Козлов Вячеслав Александрович.'] | ['barabansheg@gmail.com']         | ['79867649711'] |
| ['Павел Зубарев']                  | ['18true@mail.ru']                | ['79999083887'] |
| ['Буцукина Галина Семеновна']      | ['galina-ayat@yandex.ru']         | ['79998807908'] |
| ['Сизова Евгения']                 | ['evgeniyasizovaalex@yandex.ru']  | ['79998489880'] |
| ['Псилеас Юлия Владимировна']      | ['irini.klevi@yandex.ru']         | ['79998435609'] |
| ['Мишакин Роман']                  | ['ozonorder@jd.com']              | ['79998122642'] |
| ['Arseniy Murukin']                | ['3287321@gmail.com']             | ['79997957015'] |
| ['Тимошин Александр Валерьевич']   | ['vashey.pochty.adres@gmail.com'] | ['79997235744'] |
| ['Таушканов Евгений']              | ['9996430484_7614342003@iqos.ru'] | ['79996430484'] |
| ['Сербиновский Владимир']          | ['vovaed@mail.ru']                | ['79996393000'] |
| ['Шеметов Евгений']                | ['ozonorder@jd.com']              | ['79996076112'] |
| ['Драганов Евгений']               | ['jonwowtoy@gmail.com']           | ['79996066078'] |
| ['Морунова Анна']                  | ['an_morunova@mail.ru']           | ['79996007485'] |
| ['Талипова Наталья']               | ['natali.talipova99@mail.ru']     | ['79995486024'] |
| ['Maksim Shumkov']                 | ['maksimshumkov@mail.ru']         | ['79994996215'] |
| ['Петровнин Дима']                 | ['tytyty111sss@icloud.com']       | ['79994473305'] |
| ['Шиловский Денис Алексеевич']     | ['shilovskijd@mail.ru']           | ['79992600904'] |
| ['Ксения Крюкова']                 | ['ksenya_kryukova@inbox.ru']      | ['79992335497'] |
| ['Сапожников Дмитрий']             | ['gz70-24@bk.ru']                 | ['79992189819'] |
| ['Клеймёнов Антон']                | ['cheshirskii_kat@mail.ru']       | ['79992144392'] |
```