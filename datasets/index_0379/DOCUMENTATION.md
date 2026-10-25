# Parsetron results

## About row data

> - File path: users_preprocessed.csv
> - Total rows: 32286

### Schema
```
root
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- address1: string (nullable = true)
 |-- address2: string (nullable = true)
 |-- address3: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- user_agent: string (nullable = true)
 |-- company: string (nullable = true)
 |-- created: timestamp (nullable = true)
 |-- modified: timestamp (nullable = true)

```

### Data sample
```
| name                    | email   | phone              | address1   | address2   | address3   | ip   | user_agent   | company   | created             | modified   |
|:------------------------|:--------|:-------------------|:-----------|:-----------|:-----------|:-----|:-------------|:----------|:--------------------|:-----------|
| Алексей Ременцов        |         | +7 (235) 235-23-52 |            |            |            |      |              |           | 2017-09-18 11:39:37 | NaT        |
| Андрей тест             |         | +7 (926) 438-23-47 |            |            |            |      |              |           | 2017-09-18 14:41:58 | NaT        |
| Александр               |         | +7 (978) 267-92-06 |            |            |            |      |              |           | 2017-09-19 10:20:11 | NaT        |
| Алексей                 |         | +7 (926) 974-12-43 |            |            |            |      |              |           | 2017-09-19 12:17:23 | NaT        |
| олег                    |         | +7 (977) 258-25-18 |            |            |            |      |              |           | 2017-09-20 06:34:32 | NaT        |
| олег леонидович робутев |         | +7 (977) 258-25-18 |            |            |            |      |              |           | 2017-09-21 02:36:06 | NaT        |
| Ирина                   |         | +7 (926) 546-73-52 |            |            |            |      |              |           | 2017-09-21 02:39:49 | NaT        |
| Ольга                   |         | +7 (916) 863-42-11 |            |            |            |      |              |           | 2017-09-21 04:40:10 | NaT        |
| Виктор                  |         | +7 (495) 958-12-75 |            |            |            |      |              |           | 2017-09-21 05:15:09 | NaT        |
| Евгений он              |         | +7 (909) 941-29-89 |            |            |            |      |              |           | 2017-09-22 01:48:58 | NaT        |
| Андрей тест             |         | +7 (926) 438-23-47 |            |            |            |      |              |           | 2017-09-22 07:15:00 | NaT        |
| Александр               |         | +7 (977) 604-10-94 |            |            |            |      |              |           | 2017-09-22 07:15:44 | NaT        |
| Виктор                  |         | +7 (916) 162-29-76 |            |            |            |      |              |           | 2017-09-23 03:13:01 | NaT        |
| Александр               |         | +7 (929) 554-90-57 |            |            |            |      |              |           | 2017-09-25 02:04:11 | NaT        |
| Александр               |         | +7 (929) 554-90-57 |            |            |            |      |              |           | 2017-09-25 02:04:12 | NaT        |
| Светлана                |         | +7 (916) 297-07-64 |            |            |            |      |              |           | 2017-09-25 03:37:00 | NaT        |
| Husya                   |         | +7 (968) 799-20-46 |            |            |            |      |              |           | 2017-09-25 06:03:54 | NaT        |
| ольга                   |         | +7 (891) 694-23-28 |            |            |            |      |              |           | 2017-09-25 14:17:49 | NaT        |
| Тюрин Сергей            |         | +7 (961) 660-85-40 |            |            |            |      |              |           | 2017-09-26 07:32:35 | NaT        |
| Светлана                |         | +7 (926) 526-27-40 |            |            |            |      |              |           | 2017-09-27 03:48:53 | NaT        |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- devices: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- action: string (nullable = false)
 |    |    |-- user_agent: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 100.00% |
| Emails | 67.23% |
| Address | 91.49% |
| Works | 0.18% |
| Devices | 88.83% |
| Ips | 88.83% |
| Actuality | 97.22% |



### Data sample
```
| names                         | phones          | emails                         | address                                                                                                                                 | works   | devices                                                                                                                                                                                                                                                                        | ips                                            | actuality   |
|:------------------------------|:----------------|:-------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------|:------------|
| ['Галина']                    | ['74955541511'] | ['olegoleg@uandex.ru']         | ['Российская Федерация Люберцы ул. Южная дом 21 кв. 127']                                                                               |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.2.777 Yowser/2.5 Safari/537.36', date='10.12.2021')]                                                               | [Row(ip='141.101.77.184', date='10.12.2021')]  | 10.12.2021  |
| ['Щурий Ольга Николаевна']    | ['79013899409'] |                                | ['Российская Федерация москва']                                                                                                         |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Linux; arm_64; Android 7.0; M6T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 YaApp_Android/20.125.1 YaSearchBrowser/20.125.1 BroPP/1.0 SA/3 Mobile Safari/537.36', date='05.03.2021')]               | [Row(ip='162.158.203.16', date='05.03.2021')]  | 05.03.2021  |
| ['Алексей Владимирович']      | ['79025754854'] | ['a89841841608@yandex.ru']     | ['Российская Федерация Южно-Сахалинск ул.Емельянова 33 кв 82']                                                                          |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36', date='04.03.2021')]                                                                                          | [Row(ip='172.68.10.35', date='04.03.2021')]    | 04.03.2021  |
| ['Лора Сифурова']             | ['79031970040'] | ['lora.sifurova@gmail.com']    | ['Российская Федерация Москва ул. 9-я Парковая д. 49 корп. 1']                                                                          |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', date='29.09.2017')]                                                                                         | [Row(ip='185.19.22.161', date='29.09.2017')]   | 29.09.2017  |
| ['Андрей']                    | ['79034050593'] |                                |                                                                                                                                         |         |                                                                                                                                                                                                                                                                                |                                                | 27.10.2020  |
| ['Ирина']                     | ['79035359696'] | ['iren.maximova@gmail.com']    | ['Российская Федерация Москва Ул. Фестивальная д. 65 кВ. 118']                                                                          |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4', date='19.06.2018')]                                                                                | [Row(ip='5.228.22.91', date='19.06.2018')]     | 19.06.2018  |
| ['Зинаида']                   | ['79035538475'] |                                | ['Российская Федерация Богородицк']                                                                                                     |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi Note 9 Pro Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.7.4-gn', date='13.01.2021')] | [Row(ip='83.220.238.156', date='13.01.2021')]  | 13.01.2021  |
| ['Татьяна']                   | ['79035739578'] | ['krav75@inbox.ru']            | ['Российская Федерация ул.Наташи Ковшовой д 29 кв 234 под 6 эт 6. домофон 234в']                                                        |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko', date='30.03.2021')]                                                                                                                                               | [Row(ip='172.68.246.205', date='30.03.2021')]  | 30.03.2021  |
| ['Денис']                     | ['79037835776'] |                                | ['Российская Федерация Москва м.Сходненская ул.Свободы д.59 кв. 10']                                                                    |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5', date='04.11.2017')]                                                                                       | [Row(ip='83.220.56.241', date='04.11.2017')]   | 04.11.2017  |
| ['Александр']                 | ['79039681865'] | ['88@8av.ru']                  | ['Российская Федерация Народная 9 кв. 53']                                                                                              |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15', date='11.04.2021')]                                                                                     | [Row(ip='172.68.50.93', date='11.04.2021')]    | 11.04.2021  |
| ['Дарья']                     | ['79056567979'] | ['dashamenzhulina@mail.ru']    | ['Российская Федерация Белгород']                                                                                                       |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 YaBrowser/21.11.6.402.10 SA/3 Mobile/15E148 Safari/604.1', date='19.12.2021')]                                       | [Row(ip='172.68.245.32', date='19.12.2021')]   | 19.12.2021  |
| ['Лариса']                    | ['79062676312'] |                                |                                                                                                                                         |         |                                                                                                                                                                                                                                                                                |                                                | 27.11.2020  |
| ['Наталья']                   | ['79068022757'] | ['acro.natalya@yandex.ru']     | ['Российская Федерация Москва Машиностроителей 10-72']                                                                                  |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', date='05.12.2020')]                                                                                         | [Row(ip='188.16.10.187', date='05.12.2020')]   | 05.12.2020  |
| ['Андрей']                    | ['79096256599'] | ['79096256599@yandex.ru']      | ['Российская Федерация Москва', 'Москва']                                                                                               |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.8.0.10', date='19.11.2019')]                                | [Row(ip='213.87.132.237', date='19.11.2019')]  | 19.11.2019  |
| ['Елена']                     | ['79096696586'] | ['emorozova.1970@mail.ru']     | ['Российская Федерация']                                                                                                                |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Linux; arm_64; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaApp_Android/21.23.1 YaSearchBrowser/21.23.1 BroPP/1.0 SA/3 Mobile Safari/537.36', date='11.04.2021')]             | [Row(ip='172.68.245.150', date='11.04.2021')]  | 11.04.2021  |
| ['Борис Георгиевич Мануйлов'] | ['79096758924'] | ['manuylov76@mail.ru']         | ['Российская Федерация Москва Москва ул. Исаковского8-3-483 метро Строгино СЗАО автобусы 652 654 до остановки quot3-й микрорайонquot.'] |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 YaBrowser/20.7.3.101 Yowser/2.5 Yptp/1.23 Safari/537.36', date='18.08.2020')]                                                    | [Row(ip='109.252.113.165', date='18.08.2020')] | 18.08.2020  |
| ['Галина']                    | ['79104226150'] | ['galka-b@yandex.ru']          | ['Российская Федерация Москва Миклухо-Маклая 181 кв.340 6 под. 8 эт. код 340']                                                          |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36', date='22.06.2019')]                                                                                          | [Row(ip='46.242.12.172', date='22.06.2019')]   | 22.06.2019  |
| ['Елена']                     | ['79104286898'] | ['elena79104414363@yandex.ru'] | ['Российская Федерация Москва']                                                                                                         |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 YaBrowser/18.9.1.464 (beta) Yowser/2.5 Safari/537.36', date='10.09.2018')]                                                        | [Row(ip='128.69.185.97', date='10.09.2018')]   | 10.09.2018  |
| ['Михаил']                    | ['79104349238'] |                                | ['Российская Федерация Москва Маломосковская 22 БЦ АНТАРИС13-']                                                                         |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1', date='28.05.2019')]                                                                     | [Row(ip='188.191.161.30', date='28.05.2019')]  | 28.05.2019  |
| ['Юлия']                      | ['79117687100'] | ['juliaton@mail.ru']           | ['Российская Федерация Москва Ленинградская обл Всеволожский р-н г.Мурино б-р Менделеева 4150']                                         |         | [Row(action='Оформление заказа', user_agent='Mozilla/5.0 (iPad; CPU OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 YaBrowser/19.6.2.445.11 Mobile/15E148 Safari/605.1', date='28.06.2019')]                                                      | [Row(ip='188.227.9.223', date='28.06.2019')]   | 28.06.2019  |
```