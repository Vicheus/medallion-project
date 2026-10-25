# Parsetron results

## About row data

> - File path: users_preprocessed.csv
> - Total rows: 31113

### Schema
```
root
 |-- fullname: string (nullable = true)
 |-- email: string (nullable = true)
 |-- telephone: string (nullable = true)
 |-- address_1: string (nullable = true)
 |-- address_2: string (nullable = true)
 |-- address_3: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- forwarded_ip: string (nullable = true)
 |-- user_agent: string (nullable = true)
 |-- date_added: timestamp (nullable = true)
 |-- fullname2: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- telephone2: string (nullable = true)
 |-- ip2: string (nullable = true)

```

### Data sample
```
| fullname                    | email                       | telephone        | address_1   | address_2   | address_3                                                               | ip              | forwarded_ip    | user_agent                                                                                                                                                         | date_added          | fullname2                   | email2                      | telephone2       | ip2             |
|:----------------------------|:----------------------------|:-----------------|:------------|:------------|:------------------------------------------------------------------------|:----------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|:----------------------------|:----------------------------|:-----------------|:----------------|
|                             | darya_rd@mail.ru            |                  |             |             | Ростов-на-Дону                                                          | 85.26.186.85    | 85.26.186.85    | Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.64                                    | 2018-04-16 13:29:09 |                             | darya_rd@mail.ru            |                  | 185.49.242.42   |
| Грамарчук Анна              | kapitosha.1981@mail.ru      | 89220777316      |             |             | Тюмень                                                                  | 188.186.23.131  | 188.186.23.131  | Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36                                                     | 2018-04-19 16:19:47 | Грамарчук Анна              | kapitosha.1981@mail.ru      | 89220777316      | 178.47.166.28   |
| Новичихина Наталья          | anrl4@rambler.ru            | 89509922851      |             |             | Лесосибирск 662543, Россия, Краснодарский край, Лесосибирск, д.5, кв.56 | 95.188.0.64     | 95.188.0.64     | Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36                                                             | 2018-04-23 07:29:14 | Новичихина Наталья          | anrl4@rambler.ru            | 89509922851      | 95.188.95.226   |
| Ольга                       | olg.baryschnickova@ya.ru    |                  |             |             | Москва                                                                  | 188.123.232.35  | 188.123.232.35  | Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5                                              | 2018-03-24 22:51:24 | Ольга                       | olg.baryschnickova@ya.ru    |                  | 194.85.9.14     |
| Петроченкова Ирина          | irkunya@yandex.ru           | +79166593799     |             |             | Москва                                                                  | 176.120.9.55    | 176.120.9.55    | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36                                                | 2018-03-26 09:36:16 | Петроченкова Ирина          | irkunay@yandex.ru           | +79166593799     | 176.120.9.40    |
| Морозкина Марина            | hrumpele_mm@mail.ru         | 89138394730      |             |             | Красноярск                                                              | 89.22.171.135   | 89.22.171.135   | Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.40                                | 2018-04-03 06:24:48 | Морозкина Марина            | hrumpele_mm@mail.ru         | 89138394730      | 109.171.55.221  |
| Сокольников Александр       | kotielnikova.60@mail.ru     | 9145749340       |             |             | Белогорск                                                               | 83.234.96.2     | 83.234.96.2     | Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36                                                      | 2018-04-04 18:25:11 | Сокольников Александр       | kotielnikova.60@mail.ru     | 9145749340       | 213.87.102.134  |
| Юлия                        | kozadaeva.68@mail.ru        |                  |             |             | Москва                                                                  | 5.228.94.110    | 5.228.94.110    | Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0                                                                                      | 2018-04-06 21:54:29 | Юлия                        | kozadaeva.68@mail.ru        |                  | 109.252.69.148  |
| Шимко Оксана                | oksana.shimko2012@yandex.ru | 89817429609      |             |             | Кронштадт                                                               | 5.18.204.231    | 5.18.204.231    | Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 YaBrowser/18.2.1.174 Yowser/2.5 Safari/537.36                     | 2018-04-08 01:37:44 | Шимко Оксана                | oksana.shimko2012@yandex.ru | 89817429609      | 176.59.11.9     |
| Сокольников Александр       | kotielnikova.60@mail.ru     | 9145749340       |             |             | Белогорск                                                               | 83.234.96.2     | 83.234.96.2     | Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36                                                      | 2018-04-09 15:49:01 | Сокольников Александр       | kotielnikova.60@mail.ru     | 9145749340       | 213.87.102.134  |
| Сокольников Александр       | kotielnikova.60@mail.ru     | 9145749340       |             |             | Белогорск                                                               | 83.234.96.2     | 83.234.96.2     | Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36                                                      | 2018-04-09 15:49:02 | Сокольников Александр       | kotielnikova.60@mail.ru     | 9145749340       | 213.87.102.134  |
| Анохина Зоя                 | anohina08@bk.ru             | 89151733091      |             |             | Наро-Фоминск                                                            | 95.108.133.218  | 109.95.75.82    | Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 YaBrowser/18.2.1.174 Yowser/2.5 Safari/537.36                      | 2018-04-10 05:47:14 | Анохина Зоя                 | anohina08@bk.ru             | 89151733091      | 176.59.40.22    |
| Агафонова Мария             | super.vip.MARIA@mail.ru     | +7(910)483-25-86 |             |             | Моцсква                                                                 | 213.87.130.152  | 213.87.130.152  | Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-A510F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87 Mobile Safari/537.36 | 2018-04-10 18:09:40 | Агафонова Мария             | super.vip.MARIA@mail.ru     | +7(910)483-25-86 | 213.87.150.45   |
| Ковшарь Владимир Адольфович | sonya84@mail.ru             | 89103488221      |             |             | Нижневартовск                                                           | 82.145.222.69   | 46.39.4.205     | Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.137                                     | 2018-04-12 07:38:36 | Ковшарь Владимир Адольфович | sonya84@mail.ru             | 89103488221      | 5.158.97.9      |
| Гриценко Лариса             | gritcenko.73@bk.ru          | 89147112510      |             |             | Уссурийск                                                               | 80.83.239.115   | 80.83.239.115   | Mozilla/5.0 (Linux; Android 7.0; SM-A720F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36                           | 2018-04-12 09:06:48 | Гриценко Лариса             | gritcenko.73@bk.ru          | 89147112510      | 80.83.239.115   |
| Борисова Ольга              | Olechka1609@mail.ru         | 9875060122       |             |             | г. Пенза                                                                | 37.113.41.154   | 37.113.41.154   | Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36                                                 | 2018-03-21 09:46:42 | Борисова Ольга              | Olechka1609@mail.ru         | 9875060122       | 66.102.9.140    |
| Очирова Екатерина           | tarasek.ru@mail.ru          |                  |             |             | Санкт-Петербург                                                         | 95.27.41.67     | 95.27.41.67     | Mozilla/5.0 (Windows NT 6.1; rv:58.0) Gecko/20100101 Firefox/58.0                                                                                                  | 2018-03-13 00:08:45 | Очирова Екатерина           | tarasek.ru@mail.ru          |                  | 95.27.40.90     |
|                             | sevas82@yandex.ru           | +79787609017     |             |             | Севастополь                                                             | 66.102.9.58     | 31.28.245.101   | Mozilla/5.0 (Linux; Android 5.0.2; SM-A300F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36                         | 2018-03-12 10:30:07 |                             | sevas82@yandex.ru           | +79787609017     | 5.149.212.147   |
| Виноградова Екатерина       | tasha1513@mail.ru           | 9213996720       |             |             | Санкт-Петербург                                                         | 188.170.73.37   | 188.170.73.37   | Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36                                                 | 2018-03-12 09:54:55 | Виноградова Екатерина       | tasha1513@mail.ru           | 9213996720       | 79.173.122.98   |
|                             | boudoir-boutique@mail.ru    | 79098249555      |             |             | Хабаровск                                                               | 188.162.228.205 | 188.162.228.205 | Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko                                                                                               | 2018-03-10 18:16:15 |                             | boudoir-boutique@mail.ru    | 79098249555      | 188.162.228.149 |
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
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- devices: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- user_agent: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 56.84% |
| Emails | 99.83% |
| Address | 97.64% |
| Ips | 100.00% |
| Devices | 5.62% |
| Actuality | 5.62% |



### Data sample
```
| names                         | phones          | emails                          | address                              | ips                                    | devices   | actuality   |
|:------------------------------|:----------------|:--------------------------------|:-------------------------------------|:---------------------------------------|:----------|:------------|
| ['- Ольга']                   |                 | ['oldeeva@yandex.ru']           | ['Москва']                           | [Row(ip='5.228.31.23', date=None)]     |           |             |
| ['. Ольга']                   | ['79777249399'] | ['lelya@ro.ru']                 | ['Москва ремизова']                  | [Row(ip='95.24.55.163', date=None)]    |           |             |
| ['Aaronkefjf Aaronkef']       |                 | ['mikhailkix305i@mail.ru']      | ['Toledo']                           | [Row(ip='216.131.114.18', date=None)]  |           |             |
| ['Abadnothea Abadnoth']       | ['79837356796'] | ['v.i.n.o.jo.hngood@gmail.com'] | ['Новошахтинск']                     | [Row(ip='93.81.214.115', date=None)]   |           |             |
| ['Abbott Cortney']            |                 | ['winwinly@hotmail.fr']         | ['North Mckayla 746 Witting Fields'] | [Row(ip='23.154.177.6', date=None)]    |           |             |
| ['Abernathy Sabina']          |                 | ['ddeancasey@aol.com']          | ['Wayneside 354 Kirlin Union']       | [Row(ip='107.189.31.181', date=None)]  |           |             |
| ['Adamrhicktq Adamrhick']     |                 | ['adam8873@rambler.ru']         | ['Россия Россия']                    | [Row(ip='176.123.9.77', date=None)]    |           |             |
| ['Adams Janice']              |                 | ['musicmanedw@gmail.com']       | ['Johnson City 445 Kunze Mountains'] | [Row(ip='185.220.102.243', date=None)] |           |             |
| ['Adrianwenvq Adrianwen']     |                 | ['lirikmakar@gmail.com']        | ['Gliwice']                          | [Row(ip='82.215.68.32', date=None)]    |           |             |
| ['Adrianwetsa Adrianwet']     |                 | ['potatoman@comcast.net']       | ['Le Mans']                          | [Row(ip='94.26.227.146', date=None)]   |           |             |
| ['Afliferu Afliferu']         |                 | ['sonypetrova1999@gmail.com']   | ['Shekhupura Shekhupura']            | [Row(ip='62.106.126.28', date=None)]   |           |             |
| ['Afrogedcv Afroged']         |                 | ['andrew.plotin@bk.ru']         | ['Москва']                           | [Row(ip='176.114.8.85', date=None)]    |           |             |
| ['Airon']                     |                 | ['airon-ra@yandex.ru']          | ['Москва']                           | [Row(ip='46.188.125.217', date=None)]  |           |             |
| ['Akimova Anna']              | ['79670926425'] | ['annanikolatarhani@mail.ru']   | ['Москва']                           | [Row(ip='37.145.83.237', date=None)]   |           |             |
| ['Albertdyemeeb Albertdyeme'] | ['79594742579'] | ['gm382836@gmail.com']          | ['Bereeda Bereeda']                  | [Row(ip='195.246.120.173', date=None)] |           |             |
| ['Albertomagya Albertomag']   | ['74213829881'] | ['anastasiiadhi58c5@mail.ru']   | ['San Miguel de Tucuman']            | [Row(ip='31.13.191.104', date=None)]   |           |             |
| ['Albertovna Regina']         | ['79248759666'] | ['regina.matakaeva@bk.ru']      | ['Черкесск']                         | [Row(ip='85.173.179.179', date=None)]  |           |             |
| ['Albertticli Alberttic']     |                 | ['np4910071@gmail.com']         | ['Banjul']                           | [Row(ip='188.126.79.19', date=None)]   |           |             |
| ['Albertveisthr Albertveist'] |                 | ['edivanoolga7@gmail.com']      | ['Al Manamah']                       | [Row(ip='195.246.120.157', date=None)] |           |             |
| ['Aldanadupys Aldanadup']     |                 | ['62@altinova.ru']              | ['Москва']                           | [Row(ip='188.19.28.197', date=None)]   |           |             |
```