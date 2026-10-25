# Parsetron results

## About row data

> - Code name: index_0396
> - File path: users_preprocessed.csv
> - Total rows: 66490

### Schema
```
root
 |-- name1: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- email1: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- phone1: long (nullable = true)
 |-- phone2: string (nullable = true)
 |-- phone3: string (nullable = true)
 |-- address: string (nullable = true)
 |-- name2: string (nullable = true)
 |-- post: string (nullable = true)
 |-- login: string (nullable = true)
 |-- password: string (nullable = true)
 |-- ip: string (nullable = true)
 |-- date_insert: timestamp (nullable = true)

```

### Data sample
```
| name1                        | birth_date   | email1                   | email2                 |      phone1 |       phone2 |       phone3 | address                                                                                                         | name2             | post     | login                    | password                         | ip             | date_insert         |
|:-----------------------------|:-------------|:-------------------------|:-----------------------|------------:|-------------:|-------------:|:----------------------------------------------------------------------------------------------------------------|:------------------|:---------|:-------------------------|:---------------------------------|:---------------|:--------------------|
| Сергей                       | 0000-00-00   | aleshin77@mail.ru        | aleshin77@mail.ru      | 79166942092 |              |  79166942092 | Долгопрудный Московская область, 141707, Долгопрудный г, Пацаева пр-кт, д.15а (Пункт выдачи)                    | Сергей            |          | aleshin77@mail.ru        | 8fd2328e5cc2da47d8a8cf476ba3dd2f | 85.140.1.116   | 2018-01-09 15:44:57 |
| Яськов Виктор Яськов         | 1970-01-01   | v5820405@yandex.ru       | v5820405@yandex.ru     | 79175820405 |              |  79175820405 | Лобня Московская область, 141730, Лобня г, Маяковского ул, д.4А, оф. 215 (Пункт выдачи)                         | Виктор            |          | v5820405@yandex.ru       | 9780dec077226fe8b0114da37b867c5e | 213.87.159.15  | 2018-01-12 18:38:22 |
| Кузнецов Дмитрий             | 1970-01-01   | manager1@antennmaster.ru | info@antennmarket.ru   | 79202530661 |              | +79202530661 | Нижний Новгород Нижегородская область,  (Пункт выдачи)                                                          | Дмитрий Кузнецов  |          | manager1@antennmaster.ru | fbcf069ae92bb34724c6717dbc310e11 | 94.25.167.29   | 2018-01-18 15:46:43 |
| Терехин Максим Сергеевич     | 0000-00-00   | sb.vladimir_33@mail.ru   | sb.vladimir_33@mail.ru | 79101751600 |              |  79101751600 | Владимир Владимирская область, 600003, Владимир г, Добросельская ул, д.201 (Пункт выдачи)                       | Максим            |          | sb.vladimir_33@mail.ru   | 44d1e3d891329b851515e099fb9b2df6 | 37.19.76.2     | 2018-01-22 22:38:49 |
| Терехин Максим Сергеевич     | 0000-00-00   | sb.vladimir_33@mail.ru   | sb.vladimir_33@mail.ru | 79101751600 |              |  79101751600 | Владимир Владимирская область, 600003, Владимир г, Добросельская ул, д.201 (Пункт выдачи)                       | Максим            |          | sb.vladimir_33@mail.ru   | 44d1e3d891329b851515e099fb9b2df6 | 37.19.76.49    | 2018-01-22 22:38:49 |
| Терехин Максим Сергеевич     | 0000-00-00   | sb.vladimir_33@mail.ru   | sb.vladimir_33@mail.ru | 79101751600 |              |  79101751600 | Уточните адрес.                                                                                                 | Максим            |          | sb.vladimir_33@mail.ru   | 44d1e3d891329b851515e099fb9b2df6 | 37.19.76.84    | 2018-01-22 22:38:49 |
| Романкин Евгений             | 1981-03-21   | romankin27@yandex.ru     | romankin27@yandex.ru   | 79184619503 |              |  79184619503 | Краснодар Краснодарский край, 350065, Краснодар г, Гидростроителей ул, д.62, корпус 2 (Пункт выдачи - boxberry) | Евгений           |          | romankin27@yandex.ru     | 1d1e18f5aff052783ff76a234ed6c3c5 | 95.153.181.71  | 2018-01-24 12:12:44 |
|                              | 0000-00-00   | mpilyaev@netfort.ru      | mpilyaev@netfort.ru    |  9262313864 |              | +79262313864 | Самовывоз с московского склада                                                                                  | Пиляев Максим     |          | mpilyaev@netfort.ru      | 7381cb4fcf07f7e0bdb4140b7e04b9c5 | 93.184.164.9   | 2018-01-26 11:26:07 |
| Власов Александр Леонидович  | 0000-00-00   | alex-lift@yandex.ru      | alex-lift@yandex.ru    | 79255060622 |              |  79255060622 | Москва Москва,                                                                                                  | Александр         |          | alex-lift@yandex.ru      | af90675d596c03e9d99048dc1249c615 | 79.139.145.35  | 2018-02-13 16:20:27 |
| Червяков Дмитрий             | 0000-00-00   | 79261750666@securon.ru   | 79261750666@securon.ru | 79261750666 |              |  79261750666 | Самовывоз с московского склада                                                                                  | Дмитрий           |          | 79261750666@securon.ru   | 40b25e36399d21f5920c61b8f8e738d6 | 109.252.80.27  | 2018-02-14 15:40:46 |
| Червяков Дмитрий             | 0000-00-00   | 79261750666@securon.ru   | 79261750666@securon.ru | 79261750666 |              |  79261750666 | Самовывоз с московского склада                                                                                  | Дмитрий           |          | 79261750666@securon.ru   | 40b25e36399d21f5920c61b8f8e738d6 | 31.173.80.82   | 2018-02-14 15:40:46 |
| ... Дмитрий                  | 1970-01-01   | domofon.yu@gmail.com     | domofon.yu@gmail.com   | 79257754434 |              |  79165463330 | "Москва 2-я Рощинская ул. д.4 ""Ю-Сервис"""                                                                     | Кирилл            |          | domofon.yu@gmail.com     | 86ad4f800be74c7eca1e9e6b28adb613 | 185.8.7.2      | 2018-02-15 13:49:46 |
| ... Дмитрий                  | 1970-01-01   | domofon.yu@gmail.com     | domofon.yu@gmail.com   | 79257754434 |              |  79165463330 | "Москва 2-я Рощинская ул. д.4 ""Ю-Сервис"""                                                                     | Кирилл            |          | domofon.yu@gmail.com     | 86ad4f800be74c7eca1e9e6b28adb613 | 84.23.53.79    | 2018-02-15 13:49:46 |
| ... Дмитрий                  | 1970-01-01   | domofon.yu@gmail.com     | domofon.yu@gmail.com   | 79257754434 |              |  79165463330 | Москва 2-я Рощинская ул. д.4                                                                                    | Кирилл            |          | domofon.yu@gmail.com     | 86ad4f800be74c7eca1e9e6b28adb613 | 185.8.7.2      | 2018-02-15 13:49:46 |
| Какауридзе Гия Омариевич     | 1970-01-01   | spv-30@yandex.ru         | spv-30@yandex.ru       | 79618147939 |              |  79618147939 | Самовывоз с московского склада                                                                                  | Гия               |          | spv-30@yandex.ru         | 2c2667acad9365984f381893d121196e | 185.26.170.85  | 2018-02-27 12:44:51 |
| Убейкин Станислав Витальевич | 1974-11-19   | info@vm116.ru            | info@vm116.ru          | 79625566216 | +79033055774 |  79625566216 | Москва                                                                                                          | ООО «ВИДЕОМАСТЕР» | Менеджер | info@vm116.ru            | 683310d4eb100b597afa70e4c63ffc4b | 78.138.131.237 | 2018-03-05 13:08:41 |
| Евгений                      | 0000-00-00   | kazus2005@yandex.ru      | kazus2005@yandex.ru    | 79209336677 |              |  79209336677 | Ковров Владимирская область, 601909, Ковров г, Социалистическая ул, д.20/1, оф. 105 (Пункт выдачи)              | Евгений           |          | kazus2005@yandex.ru      | 7fbc80933ea5ada13316c7bb0a8b0d39 | 185.235.66.112 | 2018-03-12 18:50:41 |
| Евгений                      | 0000-00-00   | kazus2005@yandex.ru      | kazus2005@yandex.ru    | 79209336677 |              |  79209336677 | Ковров Владимирская область, 601909, Ковров г, Социалистическая ул, д.20/1, оф. 105 (Пункт выдачи)              | Евгений           |          | kazus2005@yandex.ru      | 7fbc80933ea5ada13316c7bb0a8b0d39 | 185.235.66.85  | 2018-03-12 18:50:41 |
| Евгений                      | 0000-00-00   | kazus2005@yandex.ru      | kazus2005@yandex.ru    | 79209336677 |              |  79209336677 | Ковров Владимирская область, 601909, Ковров г, Социалистическая ул, д.20/1, оф. 105 (Пункт выдачи)              | Евгений           |          | kazus2005@yandex.ru      | 7fbc80933ea5ada13316c7bb0a8b0d39 | 95.66.175.196  | 2018-03-12 18:50:41 |
| Евгений                      | 0000-00-00   | kazus2005@yandex.ru      | kazus2005@yandex.ru    | 79209336677 |              |  79209336677 | Ковров Владимирская область,  (Пункт выдачи)                                                                    | Евгений           |          | kazus2005@yandex.ru      | 7fbc80933ea5ada13316c7bb0a8b0d39 | 95.66.175.196  | 2018-03-12 18:50:41 |
```


## About final data
> - Total rows: 38894

### Schema
```
root
 |-- names: array (nullable = false)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 100.00% |
| Emails | 99.77% |
| Address | 67.24% |
| Ips | 81.04% |
| Accounts | 4.16% |
| Works | 4.86% |
| Actuality | 22.19% |



### Data sample
```
| names                                   | phones                         | emails                      | address                                                               | ips                                    | accounts                                                                                                                                     | works                                                                                                            | actuality   |
|:----------------------------------------|:-------------------------------|:----------------------------|:----------------------------------------------------------------------|:---------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|:------------|
| ['Иванов Дмитрий']                      | ['74955181639']                | ['id@lightwerk.ru']         | ['Москва ул. Ибрагимова д.12 оф.3']                                   | [Row(ip='109.188.124.17', date=None)]  |                                                                                                                                              |                                                                                                                  |             |
| ['Пай Руслан']                          | ['74957481611', '79269007055'] | ['prv@dean.ru']             |                                                                       |                                        |                                                                                                                                              | [Row(post='менеджер по развитию', date_start=None, date_end=None, company=None, address=None, comment=None)]     | 16.09.2020  |
| ['Петров Владислав Александрович']      | ['74959958053']                | ['petrov@atlantics.ru']     | ['Москва Самовывоз']                                                  | [Row(ip='80.252.153.192', date=None)]  |                                                                                                                                              |                                                                                                                  |             |
| ['Колеров Владимир']                    | ['74991104440']                | ['kolerov@natel.company']   |                                                                       |                                        |                                                                                                                                              |                                                                                                                  | 10.06.2024  |
| ['Ильин Владимир']                      | ['74997052924']                | ['partner@stolicatele.com'] |                                                                       |                                        |                                                                                                                                              |                                                                                                                  | 27.07.2021  |
| ['Богачев Сергей']                      | ['78124545454']                | ['jdzkag5br9ye@mail.ru']    |                                                                       |                                        |                                                                                                                                              |                                                                                                                  | 21.02.2023  |
| ['Гринькин Андрей']                     | ['78469277383', '79376467601'] | ['a.grinkin@ekcpert.ru']    |                                                                       |                                        |                                                                                                                                              | [Row(post='Руководитель направления', date_start=None, date_end=None, company=None, address=None, comment=None)] | 17.02.2020  |
| ['Мицевич Сергей Александрович']        | ['78652913591']                | ['info@isnr.ru']            |                                                                       |                                        |                                                                                                                                              |                                                                                                                  | 03.05.2022  |
| ['Снегирев Виталий Юрьевич', 'Виталий'] | ['79002799166']                | ['design@oxlift.ru']        | ['Москва Москва востряковский проезд 10б строение 8']                 | [Row(ip='213.79.119.29', date=None)]   |                                                                                                                                              |                                                                                                                  | 04.03.2020  |
| ['Ильдар']                              | ['79017940270']                | ['sultan-92@inbox.ru']      | ['Самовывоз с московского склада']                                    | [Row(ip='176.59.49.197', date=None)]   |                                                                                                                                              |                                                                                                                  |             |
| ['Алексей']                             | ['79024746306']                | ['ludens74@mail.ru']        | ['Пермь Пермский область 614070 Пермь г Дружбы ул д.23 Пункт выдачи'] | [Row(ip='5.140.165.218', date=None)]   |                                                                                                                                              |                                                                                                                  |             |
| ['Ляховец Сергей Михайлович', 'Сергей'] | ['79028165777']                | ['ip65777@yandex.ru']       | ['Уточните адрес.']                                                   | [Row(ip='176.59.45.7', date=None)]     | [Row(title='Сатро-Паладин', link='https://satro-paladin.com', login='ip65777@yandex.ru', password_hash='fbd18996c02cc69fa3917a3a5064283c')]  |                                                                                                                  | 26.02.2019  |
| ['Андрей']                              | ['79030131670']                | ['anders81@mail.ru']        | ['Москва большая грузинская д 69']                                    | [Row(ip='194.67.55.238', date=None)]   |                                                                                                                                              |                                                                                                                  |             |
| ['Михайлова Вероника Евгеньевна']       | ['79030341037']                | ['veron.eva.m@mail.ru']     | ['Тверь УЛ.КОРОБКОВА ДОМ 2 КВ 85']                                    | [Row(ip='176.114.192.11', date=None)]  |                                                                                                                                              |                                                                                                                  |             |
| ['Юрий']                                | ['79031739339', '79654091095'] | ['yuri1507@yandex.ru']      | ['123290 Москва Шелепихинское ш.25 кв.37']                            | [Row(ip='83.79.101.38', date=None)]    | [Row(title='Сатро-Паладин', link='https://satro-paladin.com', login='yuri1507@yandex.ru', password_hash='0232688cd639bc008bc8075f360764ff')] |                                                                                                                  | 07.06.2018  |
| ['Ковбасюк Алексей Евгеньевич']         | ['79032107559']                | ['krpresnja@gmail.com']     | ['Москва Б.Грузинская ул. д16. кв 91']                                | [Row(ip='46.242.3.10', date=None)]     |                                                                                                                                              |                                                                                                                  |             |
| ['Булавин Антон']                       | ['79032535314']                | ['bulavin_as@dsinv.ru']     | ['Москва Мосфильмовская 70']                                          | [Row(ip='178.251.136.163', date=None)] |                                                                                                                                              |                                                                                                                  |             |
| ['Шипенко Игорь Александрович']         | ['79032667638']                | ['igorship@mail15.com']     | ['Москва Б. Дорогомиловская 11 383']                                  | [Row(ip='79.141.229.56', date=None)]   |                                                                                                                                              |                                                                                                                  |             |
| ['Максим']                              | ['79032715252']                | ['2lmk@mail.ru']            | ['Москва г. Москва Марксистская улица дом 3 стр. 1 офис 508 5 этаж']  | [Row(ip='80.76.225.70', date=None)]    |                                                                                                                                              |                                                                                                                  |             |
| ['Шараева Мария']                       | ['79035242511']                | ['9824215@mail.ru']         | ['Москва Г. Москва ул. Большая Дмитровка д. 17А']                     | [Row(ip='10.2.0.10', date=None)]       |                                                                                                                                              |                                                                                                                  |             |
```