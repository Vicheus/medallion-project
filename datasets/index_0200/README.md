# Parsetron results

## About row data

> - Code name: index_0200
> - File path: premiya_preprocessed.csv
> - Total rows: 738201

### Schema
```
root
 |-- id: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- father_name: string (nullable = true)
 |-- password_hash: string (nullable = true)
 |-- auth_key: string (nullable = true)
 |-- password_reset_token: string (nullable = true)
 |-- role: string (nullable = true)
 |-- created_at: string (nullable = true)
 |-- rate_allowance_updated_at: string (nullable = true)
 |-- rate_allowance: integer (nullable = true)
 |-- photo: string (nullable = true)
 |-- birthday: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- phone_org: integer (nullable = true)
 |-- phone_org_dop: string (nullable = true)
 |-- phone_mob: string (nullable = true)
 |-- region_id: integer (nullable = true)

```

### Data sample
```
|    id | email                        | phone            | first_name   | last_name     | father_name      | password_hash                                                | auth_key         | password_reset_token                        |   role | created_at          | rate_allowance_updated_at   |   rate_allowance | photo   | birthday   | gender   |   phone_org | phone_org_dop   | phone_mob   |   region_id |
|------:|:-----------------------------|:-----------------|:-------------|:--------------|:-----------------|:-------------------------------------------------------------|:-----------------|:--------------------------------------------|-------:|:--------------------|:----------------------------|-----------------:|:--------|:-----------|:---------|------------:|:----------------|:------------|------------:|
|  4623 | sovet.gvardiya.2011@mail.ru  | +7(978)849-59-27 | Лариса       | Шкурина       | Николаевна       | $2y$13$Pbsz7Cp01JdOKfFt7VWmv.wnHfPpXT9ne9.34IeSp/IIZoVqqC3Dy | zinVy_ILrClP06nL | \N                                          |      1 | 2023-12-04 06:17:56 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|     7 | mailto.lex+2@gmail.com       | +7(905)750-52-72 | Александр    | Урюпин        | Александрович    | $2y$13$bSTL/IAKlHF2r/FA9Odfl.H73gd5SAiEBhlm0ZlB4ENNUzXxHwjvS | u2FzPvD1UK3gk24N | \N                                          |      1 | 2023-11-12 11:06:08 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|     6 | Stalker_13@mail.ru           | 13123123         | Александр    | Урюпин        | фывафыва         | $2y$13$ZXiL6afoQM7BJWcSdKi.Heew0/3DM9KNTP4QBDbSTJo5yvYuJja.m | fB69FaMfMZIc-HNd | \N                                          |      1 | 2023-11-12 08:58:33 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|     9 | jiltunadru@gufum.com         | +9(999)999-99-99 | Тейлор       | Фрост         | Джеймс           | $2y$13$RI/lcdt29LvkOCVU37sXx.bU5MPWRZKO6Ftw9plIIC5ds433kg7o. | 3hiIhF5GkpaRP8wk | \N                                          |      1 | 2023-11-13 06:40:32 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
| 37086 | imam.musaev.2018@mail.ru     | +7(989)944-65-70 | Имам         | Мусаев        | Магомед-Эминович | $2y$13$finuJJfLa5MbAvz2mZzjA.0Z//aiCGLZO4KjubaWVg2L673L.rU3C | ZRWqAWYFfTgzjAzY | \N                                          |      5 | 2023-12-28 18:10:56 | 2023-12-28 18:10:56.096729  |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    10 | lomakina.anna.97@mail.ru     | +8(919)170-22-11 | Анна         | Ломакина      | Владимировна     | $2y$13$cwN0irW6pPt/wua.uxDIBuaAPDzChN1.EEOPDP6n6WmBnc7Q6g8pe | lhy_W57NbtVsArp5 | \N                                          |      1 | 2023-11-13 06:54:59 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    11 | Rsovet@bk.ru                 | +7(978)729-02-17 | Роман        | Шантаев       | Сергеевич        | $2y$13$VrMA/92NtqXE52.0nRfCl.KrafVzUeH2SCojVBgegXAwTLeNoX26W | WFwv5PZaxgZnF5v6 | \N                                          |      1 | 2023-11-13 07:15:49 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    12 | Matsenkool@yandex.ru         | +7(920)006-23-23 | Олеся        | Маценко       | Игоревна         | $2y$13$sxdKB/vfgEkS3iHvnFBLZ.ozM.cEshMr5BbJNktlKYIW7spJUnyPW | hpy8kW010djICOHA | \N                                          |      1 | 2023-11-13 07:45:04 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    13 | PutyatinaEN@admlr.lipetsk.ru | +8(904)296-10-69 | Елена        | Путятина      | Николаевна       | $2y$13$6.oTbDf11pAPgj0yNpvTg.vUMqZnRl.fC7d45NBEIl7OZUsUyefBC | qXhHRodb3QqPcsNg | MG1h_HusnA1qeZiO7h5QV5XPU3PG7d7Q_1699862314 |      1 | 2023-11-13 07:58:34 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    14 | leysan-dsk@rambler.ru        | +7(915)420-49-72 | Лейсан       | Фатыхова      | Равилевна        | $2y$13$FEBzg4MqiLQ3YJ95sIfJC.RGKCWvs9OFy0uYErHHxqM4LvLY5hzXC | mOaLpQaQGw6MC0Ft | bzzvQIVAHP2zRZd_8KoZ2cPDKOQRvFYh_1699862543 |      1 | 2023-11-13 08:02:23 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    15 | Kristina.ugolnov@mail.ru     | \N               | Кристина     | Угольнова     | \N               | $2y$13$EGsbXiJy7o6eTmyHrX1B7.BQwqwr2sL0OxG9J86f13ZB/V65F9i9K | wyIesbsG4nYlrvuu | h60iQAHFkgL-ye8ZGNzxjoyCqzq5ofqq_1699862970 |      1 | 2023-11-13 08:09:31 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    17 | 79159901327@yandex.ru        | +7(915)990-13-27 | Светлана     | Веретенникова | Юрьевна          | $2y$13$UPB32nu.i13LPvDOD06zjOuSFrK4fIU/ljl5LvYZ8z9ebWN.4EE0q | fm3tCanBOJ31y58K | 5roJ1kGWkJlYKuIMP6UPoBt2wIdRpcqR_1699864107 |      1 | 2023-11-13 08:28:27 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    18 | ekstarikova@mail.ru          | +7(921)744-53-78 | Екатерина    | Иванькина     | Валерьевна       | $2y$13$JRp01oeHc37JPOvHIeSLcexKMjsgB7wRztH9iqNxMq2qJPJ8xkgPa | IiZYsXwl058UciCU | \N                                          |      1 | 2023-11-13 08:30:43 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    20 | vesnin_ivan@bk.ru            | +7(961)772-71-58 | Иван         | Веснин        | Сергеевич        | $2y$13$Upx8s7j6ZNAgxtKFEp84nePVitxEjxLhHuSHCZ1tZJogDNNZA.UXO | uBJ0XnXtjooLDj9R | \N                                          |      1 | 2023-11-13 08:57:40 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    21 | buinova2709@mail.ru          | +7(904)125-08-31 | Виктория     | Буйнова       | Юрьевна          | $2y$13$AFlCVdJ7pygCyocjG67ZvuyJnHZ/ndHQRKi6//0KkzzIKpGM7WUJS | Hcxn5seCbwwOzZyZ | \N                                          |      1 | 2023-11-13 09:13:06 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    22 | okhu@mail.ru                 | +8(953)903-03-41 | Ольга        | Ханькова      | Ивановна         | $2y$13$roe9EL5gM3yebPdmJ6KZMOd3JwimNytwe3lc0L4J106UpEV682DWq | Q-0Ug638jL71-pc2 | \N                                          |      1 | 2023-11-13 09:23:13 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    23 | tekeze@hexi.pics             | +7(999)999-99-99 | тест         | Тест          | тест             | $2y$13$8NJ8ylvbsZHx9A4WN//a1OMjB3ocRfK5pjL6QkY79CtMbaQgC7wyi | m_4AUzuW5w_jGUz0 | \N                                          |      1 | 2023-11-13 10:28:21 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    24 | l.koryanova87@mail.ru        | +7(914)176-75-79 | Любовь       | Корянова      | Александровна    | $2y$13$4XSjaRdsPwgtxa2yFyf0BeQ7nNdUFWZHk2BoJfq7.Il9fm9imFVPm | 8rxZi-f6IEgrnri5 | \N                                          |      1 | 2023-11-13 10:49:53 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    25 | smartcity@mo-novorossiysk.ru | +7(918)040-05-96 | Евгений      | Зурабян       | Леонович         | $2y$13$YpNZk.13oNKAhncHvoIHGePACwa.l6.jOYGjJ7UJQnDczwUHakosy | _JrXN2QkMH-InlX_ | \N                                          |      1 | 2023-11-13 11:02:08 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
|    26 | abbant-45@yandex.ru          | +7(987)318-86-86 | Владимир     | Милаев        | Николаевич       | $2y$13$8GO7VoBwvLn.heyppU0F5.PklfFV3Ju24rENEctzCDVkyY0M3RY6W | RYbNNUHNudkkVl0x | \N                                          |      1 | 2023-11-13 11:04:14 | 2023-12-13 00:00:00         |               60 | \N      | \N         | \N       |         nan | \N              | \N          |         nan |
```


## About final data
> - Total rows: 566166

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 70.58% |
| Emails | 96.76% |
| Sex | 5.16% |
| Birth_date | 5.22% |
| Actuality | 25.71% |



### Data sample
```
| names                                | phones                         | emails                                   |   sex | birth_date   | actuality   |
|:-------------------------------------|:-------------------------------|:-----------------------------------------|------:|:-------------|:------------|
| ['Маршуба Денис Александрович']      | ['79209551875']                | ['denmars@mail.ru']                      |   nan |              | 13.12.2023  |
| ['Проплеткина Екатерина Андреевна']  | ['79509046055']                | ['ekaterina.rodyushkova@tularegion.org'] |   nan |              | 13.12.2023  |
| ['Логинова Мария Александровна']     | ['79600117794']                | ['logimar@rambler.ru']                   |   nan |              | 13.12.2023  |
| ['Подъява Татьяна Васильевна']       | ['79930253958']                | ['79231746163@yandex.ru']                |     0 | 12.05.1987   | 13.12.2023  |
| ['Острикова Вера Тихоновна']         | ['79809389273']                | ['amo.kamenka@tularegion.ru']            |   nan |              | 13.12.2023  |
| ['Гришина Елена Владимировна']       | ['79273607075']                | ['grishina_adm@mail.ru']                 |   nan |              | 13.12.2023  |
| ['Михеев Кирилл Валерьевич']         | ['79051446043']                | ['kiri-mikheev@yandex.ru']               |     1 | 24.10.1989   | 13.12.2023  |
| ['Митрохина Ольга Евгеньевна']       | ['79379154230']                | ['vadmoper@mail.ru']                     |   nan |              | 13.12.2023  |
| ['Кытина Анастасия Андреевна']       | ['79055470881']                | ['kytina84@inbox.ru']                    |   nan |              | 13.12.2023  |
| ['Кудинов Игорь Серафимович']        | ['79112973841']                | ['mo20fo@yandex.ru']                     |   nan |              | 13.12.2023  |
| ['Строганова Наталья Александровна'] |                                | ['stroganovan@mail.ru']                  |   nan | 01.01.1970   | 13.12.2023  |
| ['Колышкина Светлана Борисовна']     | ['73834921429', '79137093007'] | ['sbk@bolotnoe.ru']                      |     0 | 01.05.1992   | 13.12.2023  |
| ['Ильина Татьяна Федоровна']         |                                | ['chicago2005@bk.ru']                    |   nan |              | 13.12.2023  |
| ['Шакирова Алсу Минехадыевна']       | ['79375882771']                | ['stozer.nur@tatar.ru']                  |   nan |              | 13.12.2023  |
| ['Денисова Полина Григорьевна']      |                                | ['polina.denisowa.0000@mail.ru']         |   nan |              | 13.12.2023  |
| ['Мацаров Руслан Сайханович']        | ['79635848084']                | ['ruslanmacarov30@gmail.com']            |   nan |              | 28.12.2023  |
| ['Новикова Вера Александровна']      | ['79065067238']                | ['ahlebininoadm@mail.ru']                |     0 | 01.12.1961   | 13.12.2023  |
| ['Фёдорова Анастасия Сергеевна']     |                                | ['fedorovaas@gov86.org']                 |   nan |              | 13.12.2023  |
| ['Маслова Маргарита Анатольевна']    |                                | ['mkoy2sosh@yandex.ru']                  |   nan |              | 13.12.2023  |
| ['Мякотина Татьяна Владимировна']    | ['79116139805']                | ['myakotina.t@mail.ru']                  |   nan |              | 13.12.2023  |
```