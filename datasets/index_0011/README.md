# Parsetron results

## About row data

> - Code name: index_0011
> - File path: Kari_club_raw.csv
> - Total rows: 1360085

### Schema
```
root
 |-- card_number: long (nullable = true)
 |-- barcode: long (nullable = true)
 |-- timestamp: timestamp (nullable = true)
 |-- phone_number: string (nullable = true)
 |-- email: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- patronymic_name: string (nullable = true)
 |-- birth_date: date (nullable = true)
 |-- gender: string (nullable = true)
 |-- region: string (nullable = true)
 |-- city: string (nullable = true)
 |-- is_new_card: boolean (nullable = true)

```

### Data sample
```
|      card_number |       barcode | timestamp           |   phone_number | email                      | last_name   | first_name   | patronymic_name   | birth_date   | gender   | region                | city            | is_new_card   |
|-----------------:|--------------:|:--------------------|---------------:|:---------------------------|:------------|:-------------|:------------------|:-------------|:---------|:----------------------|:----------------|:--------------|
| 7782306288408206 | 2306288408209 | 2022-04-16 08:02:25 |    79854925349 | summer-92@mail.ru          | Лушникова   | Марина       | Александровна     | 1992-02-29   | Женский  | Москва                | Москва          | False         |
| 7782305311414934 | 2305311414934 | 2022-04-25 08:49:39 |    79139346486 | i364042720@gmail.com       | Лопатина    | Наталья      | Сергеевна         | 1985-05-29   | Женский  | Москва                | Москва          | False         |
| 7782300049604591 | 2300049604596 | 2022-04-13 02:51:28 |    79202563110 | smirnoff050780@mail.ru     | Смирнова    | Дарья        | Александровна     | 1983-06-24   | Женский  | Гессен                | Франкфурт       | False         |
| 7782300030970217 | 2300030970211 | 2022-04-27 05:53:03 |    79025628415 | sopkhodoeva@mail.ru        | Сопходоева  | Елена        | Николаевна        | 1978-10-15   | Женский  | Новосибирская область | Новосибирск     | False         |
| 7782300071768652 | 2300071768655 | 2022-04-24 13:03:47 |    79802477394 | buneaeva@mail.ru           | Буняева     | Мария        | Андреевна         | 1984-08-01   | Женский  | Воронежская область   | Воронеж         | False         |
| 7782300048909959 | 2300048909951 | 2022-04-27 14:01:09 |    79115337957 | alexandrarocheva@gmail.com | Рочева      | Александра   | Алексеевна        | 1988-01-11   | Женский  | Москва                | Москва          | False         |
| 7782305890229257 | 2305890229257 | 2022-04-05 20:42:54 |    79031546931 | dfa72@mail.ru              | Соловьева   | Ирина        | Эдуардовна        | 1972-08-28   | Женский  | Москва                | Москва          | False         |
| 7782305290877507 | 2305290877508 | 2022-04-11 13:56:07 |    79250828888 | ak@4cio.ru                 | Кравченко   | Алексей      | Юрьевич           | 1964-03-18   | Мужской  | Москва                | Москва          | False         |
|    2307677471927 | 2307677471927 | 2022-04-22 10:01:08 |    79268387006 | lili_luckygirl@mail.ru     | Фоминых     | Лилия        | Тагировна         | 1987-03-25   | Женский  | Москва                | Москва          | True          |
|    2307851513016 | 2307851513016 | 2022-04-09 16:13:11 |    79043568967 | 010310-r@mail.ru           | Кудрявцева  | Юлия         | Юрьевна           | 1970-05-07   | Женский  | Москва                | Москва          | True          |
| 7782305948502465 | 2305948502462 | 2022-04-10 16:18:47 |    79214314519 | igorekli70@yandex.ru       | Ли          | Игорь        | Борисович         | 1970-06-08   | Мужской  | Санкт-Петербург       | Санкт-Петербург | False         |
|    2307700016798 | 2307700016798 | 2022-04-13 11:04:28 |    79107066140 | alex-under@rambler.ru      | Манацков    | Александр    | Владимирович      | 1970-01-26   | Мужской  | Москва                | Москва          | True          |
| 7782300069789686 | 2300069789686 | 2022-04-20 18:14:48 |    79035716018 | olyaion@rambler.ru         | Иванова     | Ольга        | Николаевна        | 1983-05-21   | Женский  | Москва                | Москва          | False         |
| 7782300086653253 | 2300086653250 | 2022-04-02 06:19:13 |    79284512715 | soloma-ru@yandex.ru        | Румянцев    | Павел        | Александрович     | 1981-05-19   | Мужской  | Москва                | Москва          | False         |
| 7782306990731291 | 2306990731299 | 2022-04-19 18:57:41 |    79217502444 | antonzhaa@mail.ru          | Желамский   | Антон        | Александрович     | 1980-11-14   | Мужской  | Санкт-Петербург       | Санкт-Петербург | False         |
| 7782305345526588 | 2305345526580 | 2022-04-16 15:51:26 |    79852480547 | sveta.bazenkova@mail.ru    | Базенкова   | Светлана     | Васильевна        | 1975-01-18   | Женский  | Москва                | Москва          | False         |
| 7782307208569077 | 2307208569079 | 2022-04-13 16:26:49 |    79200334040 | oduvanchik666@inbox.ru     | Демяносова  | Ольга        | Николаевна        | 1986-10-25   | Женский  | Нижегородская область | Нижний Новгород | False         |
| 7782300021356756 | 2300021356758 | 2022-04-28 19:56:58 |    79201660703 | andrey.bukin@mail.ru       | Букин       | Андрей       | Юрьевич           | 1984-07-12   | Мужской  | Санкт-Петербург       | Санкт-Петербург | False         |
| 7782300060993535 | 2300060993532 | 2022-04-06 17:34:50 |    79189127838 | fotini002@list.ru          | Торосян     | Светлана     | Арменовна         | 1985-06-21   | Женский  | Москва                | Москва          | False         |
| 7782304528901213 | 2304528901213 | 2022-04-05 14:16:02 |    79277552494 | olga.bessonova@lenta.ru    | Бессонова   | Ольга        | Валентиновна      | 1965-12-14   | Женский  | Самарская область     | Самара          | False         |
```


## About final data
> - Total rows: 1337520

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- client_card_number: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Address | 92.98% |
| Emails | 99.93% |
| Phones | 99.99% |
| Birth_date | 99.96% |
| Sex | 99.99% |
| Accounts | 100.00% |
| Actuality | 100.00% |



### Data sample
```
| names                                 | address                               | emails                             | phones          | birth_date   |   sex | accounts                                                                                  | actuality   |
|:--------------------------------------|:--------------------------------------|:-----------------------------------|:----------------|:-------------|------:|:------------------------------------------------------------------------------------------|:------------|
| ['Melnikov Dmitriy Вячеславович']     | ['Новосибирская область Новосибирск'] | ['dmitriymelnikov1976@gmail.com']  | ['79233246773'] | 12.12.1976   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='2307687725959')]    | 31.01.2022  |
| ['Navoyan Gag Rafael']                | ['Москва']                            | ['gag.ogannisian@yandex.ru']       | ['79163399887'] | 18.01.1994   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='2307266394583')]    | 29.03.2022  |
| ['Nodirov Qodie Jobirovich']          | ['Новосибирская область Новосибирск'] | ['saymahmud1998@icloud.com']       | ['79233763330'] | 21.04.1998   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782305529757165')] | 20.04.2022  |
| ['Shabanova Svetlana Vyacheslavovna'] | ['Москва']                            | ['svetlya4ok@bk.ru']               | ['79168856991'] | 01.02.1990   |     0 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782305753711284')] | 11.12.2021  |
| ['Маматкулова Ркиной Камолитдиновна'] | ['Санкт-Петербург']                   | ['mamatkulovaerkinoj1@gmail.com']  | ['79523999357'] | 02.01.1990   |     0 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='2307610304862')]    | 03.01.2022  |
| ['Баха Абд Тын']                      | ['Москва']                            | ['abdalievbakyt@gmail.com']        | ['79779881020'] | 27.05.1990   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782305855060838')] | 23.01.2022  |
| ['Бугай Александр Владимирович']      | ['Забайкальский Край Чита']           | ['albug2005@mail.ru']              | ['79149335030'] | 13.02.1978   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782305480405481')] | 17.12.2021  |
| ['Мамедов Али Тейюбоглы']             | ['Санкт-Петербург']                   | ['ali2021231987@gmail.com']        | ['79506620929'] | 23.12.1987   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782305218178830')] | 30.01.2022  |
| ['Константинова Анна Владимировна']   | ['Москва']                            | ['avk7603@mail.ru']                | ['79065070739'] | 28.03.1976   |     0 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782304039867002')] | 17.02.2022  |
| ['Петроченко Анна Владимировна']      | ['Новосибирская область Новосибирск'] | ['anabramova1978@gmail.com']       | ['79514042202'] | 16.02.1978   |     0 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782300088252005')] | 06.12.2021  |
| ['Иванов Артм Русланавич']            | ['Ростовская область Ростов-на-Дону'] | ['kirillplesakov00@gmail.com']     | ['79952291788'] | 10.06.2015   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='2307976823120')]    | 26.02.2022  |
| ['Адиятуллина Асия Миняжетдиновна']   | ['Москва']                            | ['adiatullinaasia4@gmail.com']     | ['79255343379'] | 03.03.1965   |     0 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782305169061647')] | 20.02.2022  |
| ['Тайлоков Абдисалом Очилович']       | ['Москва']                            | ['timevremya12@gmail.com']         | ['79612417742'] | 26.04.1982   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782305663035048')] | 09.02.2022  |
| ['Исмоилов Абдулатиф Абдусатторович'] | ['Нью-Йорк']                          | ['iabdulatif65@gmail.com']         | ['79776447498'] | 10.08.2001   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782305783016670')] | 13.04.2022  |
| ['Мирзоходжаев Абдулла Халимович']    | ['Башкортостан Уфа']                  | ['fghsijfid@gmail.com']            | ['79126152828'] | 05.03.1979   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='7782305248303218')] | 08.02.2022  |
| ['Умаров Абдулла Тураевич']           |                                       | ['abdulla90moskva2021@gmail.com']  | ['79917034009'] | 23.12.1990   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='2307995776698')]    | 30.01.2022  |
| ['Абозаед Абдуллах Мохаммед']         | ['Татарстан Казань']                  | ['abdallamohamed5996@gmail.com']   | ['79966058629'] | 26.09.2002   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='2307324267569')]    | 22.03.2022  |
| ['Мирзозода Абдулло Мирзо']           | ['Курганская область Курган']         | ['danil3385656@gmail.com']         | ['79120426737'] | 27.08.1990   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='2307373734548')]    | 01.12.2021  |
| ['Нарзуллоев Абдулло Бахруллоевич']   | ['Москва']                            | ['narzulloevabdullo368@gmail.com'] | ['79840002009'] | 27.01.2002   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='2307255872160')]    | 19.02.2022  |
| ['Дустназаров Абдулхай Абдукаюмович'] | ['Москва']                            | ['abdulhaj4@gmail.com']            | ['79256817573'] | 29.03.1999   |     1 | [Row(title='Kari Club', link='https://kari.com/', client_card_number='2307524248924')]    | 14.02.2022  |
```