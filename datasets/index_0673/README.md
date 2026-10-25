# Parsetron results

## About row data

> - Code name: index_0673
> - File path: kаssу_ru.csv
> - Total rows: 93228

### Schema
```
root
 |-- user_id: string (nullable = true)
 |-- passport_id: string (nullable = true)
 |-- sberbank_id: string (nullable = true)
 |-- telegram_id: string (nullable = true)
 |-- telegram_username: string (nullable = true)
 |-- agent_id: string (nullable = true)
 |-- geo_city_id: string (nullable = true)
 |-- login: string (nullable = true)
 |-- email: string (nullable = true)
 |-- email_confirm: string (nullable = true)
 |-- password: string (nullable = true)
 |-- password_old: string (nullable = true)
 |-- family: string (nullable = true)
 |-- name: string (nullable = true)
 |-- patronymic: string (nullable = true)
 |-- sex: string (nullable = true)
 |-- birthday: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- about: string (nullable = true)
 |-- locale: string (nullable = true)
 |-- delivery: string (nullable = true)
 |-- delivery_sms: string (nullable = true)
 |-- online: string (nullable = true)
 |-- fault_count: string (nullable = true)
 |-- forgot_count: string (nullable = true)
 |-- dt_forgot: string (nullable = true)
 |-- dt_create: string (nullable = true)
 |-- dt_update: string (nullable = true)

```

### Data sample
```
|   user_id |   passport_id | sberbank_id   | telegram_id   | telegram_username   | agent_id   | geo_city_id   | login   | email                           |   email_confirm | password                         | password_old                     | family         | name      | patronymic   | sex     | birthday   |       phone | about   | locale   |   delivery |   delivery_sms |   online |   fault_count |   forgot_count | dt_forgot   |   dt_create |   dt_update |
|----------:|--------------:|:--------------|:--------------|:--------------------|:-----------|:--------------|:--------|:--------------------------------|----------------:|:---------------------------------|:---------------------------------|:---------------|:----------|:-------------|:--------|:-----------|------------:|:--------|:---------|-----------:|---------------:|---------:|--------------:|---------------:|:------------|------------:|------------:|
|    786121 |       3314008 | NULL          | NULL          | NULL                | NULL       | NULL          | NULL    | olga-yashhuk@yandex.ru          |               1 | 5c86bc171130932d2a91aa8cd281ccee | NULL                             | Ольга          | Ящук      | NULL         | f       | NULL       | 79659011986 | NULL    | NULL     |          0 |              0 |        0 |             0 |              0 | NULL        |  1754852525 |  1754852878 |
|    784386 |       3298258 | NULL          | NULL          | NULL                | NULL       | NULL          | NULL    | chernova-o@mail.ru              |               1 | eb7ebd317902bc85b6d78dc5478421cd | NULL                             | Ольга          | Ященко    | NULL         | f       | NULL       | 79630509540 | NULL    | NULL     |          1 |              1 |        0 |             0 |              1 | 1751282912  |  1751271300 |  1751283007 |
|    500661 |       1816245 | NULL          | NULL          | NULL                | NULL       | NULL          | NULL    | yashkinakss@gmail.com           |               1 | NULL                             | 6707d497a85fc0a94a3a13b1266c67e6 | Ксения         | Яшкина    |              | unknown | NULL       | 79779478430 | NULL    | NULL     |          1 |              0 |        0 |             0 |              0 | NULL        |  1581692381 |  1581692540 |
|    704084 |       2651454 | NULL          | NULL          | NULL                | NULL       | 1928          | NULL    | yashina-1999@internet.ru        |               1 | 811b7d23ec29bec7c4d34db0f0aaec91 | NULL                             | Дарья          | Яшина     | Андреевна    | f       | 946580400  | 79630404458 | NULL    | NULL     |          1 |              1 |        0 |             0 |              0 | NULL        |  1701672165 |  1701677083 |
|    230432 |       1138322 | NULL          | NULL          | NULL                | NULL       | NULL          | NULL    | edumnova91@gmail.com            |               1 | NULL                             | 60e0435d9c604562dae35a052f63ed2c | Екатерина      | Яцкевич   |              | unknown | NULL       | 79221471707 | NULL    | NULL     |          0 |              0 |        0 |             0 |              1 | NULL        |  1520442916 |  1577209306 |
|    773491 |       3085316 | NULL          | NULL          | NULL                | NULL       | NULL          | NULL    | olchikyatkina@yandex.ru         |               1 | 98bfe5cc35c1c9881e134dbfd16fd62d | NULL                             | Ольга          | Яткина    | NULL         | unknown | NULL       | 79833130478 | NULL    | NULL     |          1 |              1 |        0 |             0 |              0 | NULL        |  1735065009 |  1735065158 |
|    759903 |       2946250 | NULL          | NULL          | NULL                | NULL       | 1928          | NULL    | sofik98@mail.ru                 |               1 | e7e79f14779e1292ed259117430258a4 | NULL                             | Софья          | Ярутина   |              | f       | 887310000  | 79086384319 | NULL    | NULL     |          1 |              1 |        0 |             0 |              0 | NULL        |  1728879321 |  1728879476 |
|     83648 |        238404 | NULL          | NULL          | NULL                | NULL       | 1928          | NULL    | vlad-ekk@tt66.ru                |               1 | NULL                             | cf7e6b0569aefe78f8c69925b5bf1732 | Шастина        | Ярославна | Владимировна | f       | 851713200  | 79049828560 | NULL    | NULL     |          1 |              1 |        0 |             0 |              0 | NULL        |  1383290755 |  1508161685 |
|    388619 |       1477659 | NULL          | NULL          | NULL                | NULL       | 1908          | NULL    | jaroslava-chepkasova@rambler.ru |               0 | NULL                             | f993a338f08bcaddb8d302f701b86c20 | Цепелева       | Ярославна | Игоревна     | f       | 680727600  | 79505538939 | NULL    | NULL     |          1 |              1 |        0 |             0 |              1 | NULL        |  1551942156 |  1551942591 |
|     21319 |         57140 | NULL          | NULL          | NULL                | NULL       | NULL          | NULL    | lexismine@yandex.ru             |               1 | NULL                             | 2f922b7fde6f98b8e88eeeb87d98f837 | Усольцева      | Ярославна | Игоревна     | f       | NULL       | 79025003376 | NULL    | NULL     |          0 |              0 |        0 |             0 |              0 | NULL        |  1310392131 |  1508161685 |
|    138458 |        511730 | NULL          | NULL          | NULL                | NULL       | 1928          | NULL    | yaroslavnaekb@gmail.com         |               1 | NULL                             | 94c21979737aeda81e68d44326469813 | Кудина         | Ярославна | Агабековна   | f       | 752871600  | 79049876713 | NULL    | NULL     |          1 |              1 |        0 |             0 |              0 | NULL        |  1446100604 |  1508161685 |
|    766087 |       2980264 | NULL          | NULL          | NULL                | NULL       | 1928          | NULL    | krya5585@mail.ru                |               1 | f633678198ab43eaac3e06db05dcf199 | NULL                             | Красносельских | Ярославна | Артёмовна    | f       | NULL       | 79827143000 | NULL    | NULL     |          0 |              0 |        0 |             0 |              0 | NULL        |  1730289789 |  1730289954 |
|     10342 |         46261 | NULL          | NULL          | NULL                | NULL       | 1928          | NULL    | rbcrf_90@mail.ru                |               1 | NULL                             | 05a35668c9811b0c75b1d80d44d5d0bc | Захарова       | Ярославна | Олеговна     | f       | 647719200  | 79068118667 | NULL    | NULL     |          1 |              1 |        0 |             0 |              0 | NULL        |  1286458066 |  1508161685 |
|      6863 |         42836 | NULL          | NULL          | NULL                | NULL       | NULL          | NULL    | tiel@bk.ru                      |               1 | NULL                             | 58f1d3194e28f171e89b053c2c6df6d9 | Яровая         | Ярослава  | Владимировна | f       | NULL       | 79227060075 | NULL    | NULL     |          1 |              1 |        0 |             0 |              0 | NULL        |  1271434883 |  1508161685 |
|    771469 |       3042324 | NULL          | NULL          | NULL                | NULL       | NULL          | NULL    | yaroslava_kholo@mail.ru         |               1 | 1b417ea95920e88bfa2bb3442803771f | NULL                             | Холобудовская  | Ярослава  | NULL         | f       | 519760800  | 79049841616 | NULL    | NULL     |          1 |              1 |        0 |             0 |              0 | NULL        |  1732881564 |  1732881776 |
|     27788 |         63534 | NULL          | NULL          | NULL                | NULL       | 1928          | NULL    | slavka80@bk.ru                  |               1 | NULL                             | 9a874587f7ed761e5be2408f2ac2315e | Сафронова      | Ярослава  | Сергеевна    | f       | 327956400  | 79226060007 | NULL    | NULL     |          0 |              0 |        0 |             0 |              0 | NULL        |  1321029793 |  1508161685 |
|     92051 |         18759 | NULL          | NULL          | NULL                | NULL       | 2429          | NULL    | postnikov@chelcom.ru            |               1 | NULL                             | 8711369f55d3ad9cbbb4df7bce2acdd2 | Постникова     | Ярослава  | Геннадьевна  | f       | 711828000  | 79624853789 | NULL    | NULL     |          1 |              1 |        0 |             0 |              0 | NULL        |  1345062836 |  1508161685 |
|    166044 |        385714 | NULL          | NULL          | NULL                | NULL       | 1590          | NULL    | popova_yaroslava@inbox.ru       |               1 | NULL                             | b161962fe4ca85bf4f3842e03e936095 | Попова         | Ярослава  | Сергеевна    | f       | 774122400  | 79194584149 | NULL    | NULL     |          1 |              1 |        0 |             0 |              1 | NULL        |  1417932096 |  1508161685 |
|    152827 |        593729 | NULL          | NULL          | NULL                | NULL       | 1928          | NULL    | youreternity@mail.ru            |               1 | NULL                             | cbf5aec6ef5c20f43c422b1ef57157c8 | Платонова      | Ярослава  | Ивановна     | f       | 595364400  | 79090039327 | NULL    | NULL     |          0 |              0 |        0 |             0 |              0 | NULL        |  1456920406 |  1508161685 |
|    123336 |        429886 | NULL          | NULL          | NULL                | NULL       | 1928          | NULL    | yasica@mail.ru                  |               1 | NULL                             | 32df32e1db0234c60aaec3fa4468938d | Маслакова      | Ярослава  | Ивановна     | f       | 553284000  | 79326145148 | NULL    | NULL     |          1 |              1 |        0 |             0 |              0 | NULL        |  1424854889 |  1508161685 |
```


## About final data
> - Total rows: 93126

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- actuality: date (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Sex | 99.63% |
| Birth_date | 81.17% |
| Phones | 99.50% |
| Emails | 99.96% |
| Actuality | 100.00% |
| Raw_metadata | 99.99% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                               |   sex | birth_date   | phones          | emails                         | actuality   | raw_metadata                                             | source_entity_id                                         |
|:------------------------------------|------:|:-------------|:----------------|:-------------------------------|:------------|:---------------------------------------------------------|:---------------------------------------------------------|
| ['Абатурова Ольга Владимировна']    |     0 | 10.09.1983   | ['79222178908'] | ['abaturova_ov@e1.ru']         | 16.10.2017  | ['{"password_old": "896c2eee46eb842c153195f8ec40118d"}'] | 151c400933ae88f45718af633ba2201783e954e67aa5cc3cf2917f4c |
| ['Агапов Константин Михайлович']    |     1 |              | ['79222008890'] | ['agapovk@gmail.com']          | 16.10.2017  | ['{"password_old": "f9cc81aadff0bd7cbb17a8bbb4a38ebd"}'] | d3b21024a5c21020edefd8d9cf7db3aaaa3d6528de75979570783106 |
| ['Агафуров Александр Вадимович']    |     1 | 13.06.1995   | ['79959260614'] | ['present59rus@gmail.com']     | 21.10.2024  | ['{"password": "247d13bdd14babf1ce0ea57cf1213c8c"}']     | 9c519ec71fe37e279962417f835a00cbc2ca235526aa7da4333bb79d |
| ['Адмаев Виталий Владимирович']     |     1 |              | ['79037106699'] | ['vitalyva2012@yandex.ru']     | 16.10.2017  | ['{"password_old": "3dfcbadf15fd533c2f44a966a24920fc"}'] | 1a06c4a9dc3ab304ffc3344b539c86181755a65dfdb2c8947eb44d92 |
| ['Азнаева Ирина Павловна']          |     0 | 07.09.1983   | ['79089117074'] | ['aznaeva83@mail.ru']          | 16.10.2017  | ['{"password_old": "bc22c369e1758583304b41bdcb73402f"}'] | f62bb93dae695a8d077809068a8c672c740d9ac2b0f2f526c43eb377 |
| ['Айдамирова Диана Гюльага Кызы']   |     0 | 26.06.1991   | ['79221466820'] | ['kaktysixovna@gmail.com']     | 16.10.2017  | ['{"password_old": "dc02e028c79f46906272ea6f7b9b7c5c"}'] | 4091a96dc7ce75c4af596e4a79e0d3bdaf8a89022aea356833f79566 |
| ['Айсаринов Жанат Барлыкович']      |     1 | 26.09.1985   | ['79193167707'] | ['zhan.aisarinov@mail.ru']     | 09.11.2024  | ['{"password": "c374a391204376baa8759cd826241c31"}']     | 54adba08fcea98fbbadd16199ace3fdf38cfdc9076c0dab934fa1b82 |
| ['Аксенов Александр Александрович'] |     1 | 22.03.1987   | ['79506508733'] | ['alexbol174@mail.ru']         | 16.10.2017  | ['{"password_old": "67db9cec6b414f22cc8867630451c773"}'] | 205c9feb6d295a6550880a17e14e9ce3c044085a3528198f20c69de7 |
| ['Акулова Александра Алексеевна']   |     0 | 11.05.1990   | ['79025856860'] | ['oxyeen@mail.ru']             | 16.10.2017  | ['{"password_old": "b07ebe3470cfd679e461e39aa82a00bc"}'] | b133c9eb929539a816dcf19c321b3ae90d922ab0d219f7b2ce9ae782 |
| ['Александр Сергеевич']             |     1 | 22.04.1987   | ['79124704561'] | ['zlo.74@yandex.ru']           | 16.10.2017  | ['{"password_old": "4ae953c2e7f7fdfb5881260e90bdf9d6"}'] | 7ac5174672191e94faf1a51af63ca4ea26f50c06c00beb6d2be8675d |
| ['Александр Сергеевич']             |     1 | 25.04.1981   | ['79963270368'] | ['goshinli@mail.ru']           | 16.10.2017  | ['{"password_old": "7309c9e8be8335d5860fb09fe940bd65"}'] | b4b6a392a510a3b425bbd364f507ba2a3cce3552c3a612aa5d88cbd3 |
| ['Александра Алексеевна']           |     0 | 27.03.1992   | ['79120449195'] | ['alexandra.evst@gmail.com']   | 16.10.2017  | ['{"password_old": "bb54980f69795d9c82a2983124bbfe2b"}'] | 09637896f346760ea49bf1c26bafacdfd1c1b137412cef360f747415 |
| ['Алексей Вячеславович']            |     1 | 01.03.1993   | ['79630503540'] | ['a_omelkov@mail.ru']          | 16.10.2017  | ['{"password_old": "2a9920dab2b222b3574dca350bb12a4d"}'] | d76885ede2a9f8b7084f271d84414d752164ac1c0bc06e2e6722a212 |
| ['Алышев Сергей Петрович']          |     1 |              | ['79655340515'] | ['alyschev-s@inbox.ru']        | 16.10.2017  | ['{"password_old": "25df839241afd2ce33532646ca9f789c"}'] | 8e5cfc18fdbf3b6ae0b27528cc0268fd0ab41cce90f19981dc346498 |
| ['Андрей Дмитриевич']               |     1 | 24.12.1983   | ['79222566399'] | ['yakusya1225@mail.ru']        | 16.10.2017  | ['{"password_old": "0c5646091491f084d8876f9b208ff5d1"}'] | bccaedc9b1083b1a1e9204ad0e2a52b6d9d263ceaf23ed294b9c206d |
| ['Андрей Плаксин Сергеевич']        |     1 | 25.07.1984   | ['79530084759'] | ['pas1984andrei@yandex.ru']    | 21.05.2020  | ['{"password_old": "9807855d28ec3c338be87553d1b52ac3"}'] | 47c9a8c6e8992aff19892e5d330b09a6933abd5acdf717593b295ac0 |
| ['Андрюшкин Аркадий Алексеевич']    |     1 |              | ['79876543210'] | ['kanaroooo@gmail.com']        | 27.08.2018  | ['{"password_old": "06c55e5f901f6b8c622f680433c3cff6"}'] | 87583572cb27ac4f946d71c9af887a7fc68b393fe1717d16b9a70247 |
| ['Аникина Ирина Фидратовна']        |     0 | 19.09.1974   | ['79221885730'] | ['anikina33@mail.ru']          | 16.10.2017  | ['{"password_old": "f66b0c7bc9b32a568fd79debd630bf3a"}'] | fdca6ec0bb5743d6e43f90d02cef5a1b0d18d1105dee25170ed50f0d |
| ['Анисимкова Альбина Харисовна']    |     0 | 26.12.2016   | ['79090042442'] | ['albinaanisimkva@rambler.ru'] | 16.10.2017  | ['{"password_old": "0ab840a9800b987cc2767eff8b108b09"}'] | 6e740d1df2eb8a288644b917aa4735ada8107005bdea6c7510a7102c |
| ['Анисимова Инна Викторовна']       |     0 | 25.01.1986   | ['79223110655'] | ['kiziv@mail.ru']              | 16.10.2017  | ['{"password_old": "c817661b7e04ff8104bf1e59f663b42e"}'] | df9ab815ab8195d38f3024a7747a86333ba6c359ba746a163006e046 |
```