# Parsetron results

## About row data

> - File path: zacks_com.txt
> - Total rows: 8449

### Schema
```
root
 |-- Email: string (nullable = true)
 |-- Name: string (nullable = true)
 |-- City: string (nullable = true)
 |-- Phone: string (nullable = true)

```

### Data sample
```
| Email                    | Name               | City                                          |        Phone |
|:-------------------------|:-------------------|:----------------------------------------------|-------------:|
| zzzelllo@gmail.com       | Bulgakov Aleksandr | MOSCOW MARSHALA KATUKOVA STR. 21-1-72         |  79251852050 |
| zzzdik@yandex.ru         | Zzzdik Zzzdik      | KRASNOYARSK SITY KRASNOYARSK. LENIN STREET 91 |  79029253260 |
| zzzalkor1988@gmail.com   | Belyashin Ivan     | 5 15                                          |  89299118790 |
| zzz@sanet.ru             | Zaozerski Serguei  | ARKHANGELSK P.O.BOX 31                        |              |
| zzoopark@yandex.ru       | Ryzhkov Sergey     |                                               |  79277556195 |
| zyryanovwasily@yandex.ru | Zyryanov Vasily    | MOSCOW                                        |   9203689315 |
| zyf113@mail.ru           |                    | 225                                           |  79896229582 |
| zxz9zxz@gmail.com        | Fred Zed           | MOSCOW PODSOSENSKY 20 BLD 1                   |  74959894128 |
| zxz8zxz@gmail.com        | Zed Fred           | MOSCOW PODSOSENSKY LANE 20 BLD 1              |  74959894128 |
| zxx@inbox.com            | Z Alex             |                                               |              |
| zxwr111@gmail.com        | Bogatikov Artem    | YELETS KIRPICHNAYA 19                         |  79601404281 |
| zxman@softhome.net       | Yakimov Igor       | SAINT-PETERSBURG AVIAKONSTRUKTOROV ST. 1-45   |              |
| zxd70@mail.ru            | Kh Dim             | EKATERINA RUSSIAN                             |  79222055533 |
| zxcqwe2014@mail.ru       | Kaufman Sergey     | MOSCOW                                        |  89629318166 |
| zwerewa281@gmail.com     | Zvereva Natalya    | PERM MIRA126-9                                |  89082788019 |
| zvezda7770@yandex.ru     | Popov Petr         | KAZAN RUSSIA                                  |  89674677910 |
| zveruga2@ya.ru           | Yyyy Yyy           | MOSCOW                                        |              |
| zverevlespkab@yandex.ru  |                    |                                               |  79530537298 |
| zver001@mail.ru          | Borisoff Egor      | MOSCOW RUSSIA                                 |  79032246384 |
| zuzin7377@gmail.com      |                    | DZERZHINSK                                    | 789527638060 |
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
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.84% |
| Phones | 74.78% |
| Address | 92.20% |



### Data sample
```
| names                      | emails                       | phones          | address                                           |
|:---------------------------|:-----------------------------|:----------------|:--------------------------------------------------|
| ['Bulgakov Aleksandr']     | ['zzzelllo@gmail.com']       | ['79251852050'] | ['Moscow Marshala Katukova Str. 21-1-72']         |
| ['Zzzdik Zzzdik']          | ['zzzdik@yandex.ru']         | ['79029253260'] | ['Krasnoyarsk Sity Krasnoyarsk. Lenin Street 91'] |
| ['Belyashin Ivan']         | ['zzzalkor1988@gmail.com']   | ['79299118790'] | ['5 15']                                          |
| ['Zaozerski Serguei']      | ['zzz@sanet.ru']             |                 | ['Arkhangelsk P.O.Box 31']                        |
| ['Ryzhkov Sergey']         | ['zzoopark@yandex.ru']       | ['79277556195'] |                                                   |
| ['Zyryanov Vasily']        | ['zyryanovwasily@yandex.ru'] | ['79203689315'] | ['Moscow']                                        |
| ['Fred Zed']               | ['zxz9zxz@gmail.com']        | ['74959894128'] | ['Moscow Podsosensky 20 Bld 1']                   |
| ['Zed Fred']               | ['zxz8zxz@gmail.com']        | ['74959894128'] | ['Moscow Podsosensky Lane 20 Bld 1']              |
| ['Z Alex']                 | ['zxx@inbox.com']            |                 |                                                   |
| ['Bogatikov Artem']        | ['zxwr111@gmail.com']        | ['79601404281'] | ['Yelets Kirpichnaya 19']                         |
| ['Yakimov Igor']           | ['zxman@softhome.net']       |                 | ['Saint-Petersburg Aviakonstruktorov St. 1-45']   |
| ['Kh Dim']                 | ['zxd70@mail.ru']            | ['79222055533'] | ['Ekaterina Russian']                             |
| ['Kaufman Sergey']         | ['zxcqwe2014@mail.ru']       | ['79629318166'] | ['Moscow']                                        |
| ['Zvereva Natalya']        | ['zwerewa281@gmail.com']     | ['79082788019'] | ['Perm Mira126-9']                                |
| ['Popov Petr']             | ['zvezda7770@yandex.ru']     | ['79674677910'] | ['Kazan Russia']                                  |
| ['Borisoff Egor']          | ['zver001@mail.ru']          | ['79032246384'] | ['Moscow Russia']                                 |
| ['Pro Katerina']           | ['zuyasha90@mail.ru']        | ['78632223537'] |                                                   |
| ['Shiriyazdanova Zulfira'] | ['zulfira.sh2014@yandex.ru'] |                 | ['Volgogradskaya 9']                              |
| ['Balto Zubris']           | ['zubris@krjuk.ru']          |                 | ['Morkti Dorkti 099']                             |
| ['Allway Ou Zubiriyuy']    | ['zubiriyuy@g-mailix.com']   | ['78125235266'] | ['Saint-Peterburg']                               |
```