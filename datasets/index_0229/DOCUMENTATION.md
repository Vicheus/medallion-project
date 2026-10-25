# Parsetron results

## About row data

> - File path: labquest_*.csv
> - Total rows: 466113

### Schema
```
root
 |-- ФИО Пациента: string (nullable = true)
 |-- Пол: string (nullable = true)
 |-- Дата рождения: string (nullable = true)
 |-- Заказчик: string (nullable = true)
 |-- Телефон: string (nullable = true)
 |-- Адрес эл_почты: string (nullable = true)
 |-- Паспорт_кем выдан: string (nullable = true)
 |-- Паспорт_номер: string (nullable = true)
 |-- Паспорт_серия: string (nullable = true)

```

### Data sample
```
| ФИО Пациента                              | Пол   | Дата рождения   | Заказчик                       |     Телефон | Адрес эл_почты                | Паспорт_кем выдан           | Паспорт_номер   | Паспорт_серия   |
|:------------------------------------------|:------|:----------------|:-------------------------------|------------:|:------------------------------|:----------------------------|:----------------|:----------------|
| ABBAS DAKKA                               | М     | 18.01.1998      | АО «МОБИМЕД» Домодедово DMEMED | 79779076521 | abbas.5@live.com              | ЛЕБАНОН                     | 4142626         | RL              |
| ABBASOV PARVIZ                            | М     | 23.06.1975      | ООО «ПроЛаб»                   | 79651156589 | nomail@labquest.ru            | АЙЗЕРБАЙДЖАН                | С03834347       |                 |
| ABDELMAWGOUD MARIAM YASSER SABRY MOURTADA | Ж     | 16.06.2001      | АО «МОБИМЕД» Домодедово        | 79307098344 | mariamyasset189@gmail.com     | EGY                         | A24555713       |                 |
| ABDELRAHMAN SABER ABDELHAMD MOHAMED       | М     | 17.05.2003      | АО «МОБИМЕД» Домодедово        | 79261360342 | abdelrahmansaber315@gmail.com | ЕГИПЕТ                      | 32658290        | A               |
| ABDUL RAZZAK ISMAEEL ABDUL AZIZ           | М     | 15.09.1975      | Верба Экспресс                 | 79951150303 |                               | MINISTRY OF FOREIGN AFFAIRS | L001313         | 154-22          |
| ABDULAEV SHEROZJON                        | М     | 19.02.1998      | АО «МОБИМЕД» Домодедово DMEMED | 79060527441 | sheroz0777@mail.ru            |                             | 1007754         | 40              |
| ABDULLAJONOV JASURMIRZO YORKINBOY UGLI    | М     | 06.11.2008      | ООО «Сколмед»                  | 79621166050 |                               |                             | 8068610         | FA              |
| ABDULLAYEV CAVID AYDIN OGLU JAVID         | М     | 23.09.1990      | ООО «Сколмед»                  | 79065074747 | cavid0482@gmail.com           |                             | C0              | 1038036         |
| ABDURAZOKOV MIRKOMIL MURODIL UGLI         | М     | 26.01.2004      | АО «МОБИМЕД» Мичуринский       | 79037552214 | kahor@mail.ru                 | MIA 30000                   | 0969178         | FA              |
| ABDUZUKHROV JAMSHIDJON TOLIBOVICH         | М     | 17.06.1983      | АО «МОБИМЕД» Домодедово        | 79670798658 | abrorov@yahoo.com             | 18.07.2022                  | 5956590         | FA              |
| ABDYEVA SAPARGUL                          | Ж     | 23.03.1975      | АО «МОБИМЕД» Домодедово        | 79654121217 | demoandroio@gmail.com         | МВД 0401                    | 3349287         | 66              |
| ABIDO MARIA DE LOURDES                    | Ж     | 19.10.1946      | АО «МОБИМЕД» Домодедово        | 79153707369 | alfeola@mail.ru               | BRA                         | FS414209        |                 |
| ABRAMOVA NIKA                             | Ж     | 25.02.1993      | АО «МОБИМЕД» Домодедово        | 79164050987 | nikafs_93@mail.ru             | МВД 77306                   | 9511445         | 75              |
| ACHILOVA MAMLAKAT ERGASHEVNA              | Ж     | 24.06.1985      | ООО «Сколмед»                  | 79257752633 |                               |                             | 4199694         | fa              |
| ADNAN IBRAHIM QARAH                       | М     | 01.02.1969      | Верба Экспресс                 | 79951150303 |                               | MINISTRY OF FOREIGN AFFAIRS | L001878         | 154-19          |
| AFONSO JUELMA CALABRIA CANI               | Ж     | 19.09.1999      | АО «МОБИМЕД» Домодедово        | 79777160800 | dennilsonmiranda49@gmail.com  | AGO                         | N2475184        |                 |
| AGAPOV FILIPP                             | М     | 05.04.1987      | АО «МОБИМЕД» Домодедово        | 79213678850 | f.agapov@mail.ru              | МВД 78039                   | 9973886         | 75              |
| AGBAYAHOUN HENRI JOEL                     | М     | 04.03.1998      | АО «МОБИМЕД» Домодедово        | 79804361071 |                               | BENIN                       | B0776998        |                 |
| AGRAWAL SANJEEV KUMAR                     | М     | 15.02.1972      | АО «МОБИМЕД»                   | 79031321886 | henamohan@gmail.com           | CHANDIGARH                  | D1140537        |                 |
| AGUIE YVES GAEL AUDRAN                    | М     | 08.09.1989      | АО «МОБИМЕД» Домодедово        | 79990033709 | audrangael0@gmail.com         | CIV                         | 18AT45055       |                 |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Sex | 99.98% |
| Birth_date | 99.93% |
| Phones | 99.76% |
| Emails | 45.82% |
| Documents | 18.52% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                                         |   sex | birth_date   | phones          | emails                            | documents                                                                                                                       | raw_metadata                                       |
|:----------------------------------------------|------:|:-------------|:----------------|:----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------|
| ['Abbas Dakka']                               |     1 | 18.01.1998   | ['79779076521'] | ['abbas.5@live.com']              |                                                                                                                                 | ['{"Заказчик": "АО «МОБИМЕД» Домодедово DMEMED"}'] |
| ['Abbasov Parviz']                            |     1 | 23.06.1975   | ['79651156589'] | ['nomail@labquest.ru']            |                                                                                                                                 | ['{"Заказчик": "ООО «ПроЛаб»"}']                   |
| ['Abdelmawgoud Mariam Yasser Sabry Mourtada'] |     0 | 16.06.2001   | ['79307098344'] | ['mariamyasset189@gmail.com']     |                                                                                                                                 | ['{"Заказчик": "АО «МОБИМЕД» Домодедово"}']        |
| ['Abdelrahman Saber Abdelhamd Mohamed']       |     1 | 17.05.2003   | ['79261360342'] | ['abdelrahmansaber315@gmail.com'] |                                                                                                                                 | ['{"Заказчик": "АО «МОБИМЕД» Домодедово"}']        |
| ['Abdul Razzak Ismaeel Abdul Aziz']           |     1 | 15.09.1975   | ['79951150303'] |                                   |                                                                                                                                 | ['{"Заказчик": "Верба Экспресс"}']                 |
| ['Abdulaev Sherozjon']                        |     1 | 19.02.1998   | ['79060527441'] | ['sheroz0777@mail.ru']            | [Row(type=4, serial='401007754', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]        | ['{"Заказчик": "АО «МОБИМЕД» Домодедово DMEMED"}'] |
| ['Abdullajonov Jasurmirzo Yorkinboy Ugli']    |     1 | 06.11.2008   | ['79621166050'] |                                   |                                                                                                                                 | ['{"Заказчик": "ООО «Сколмед»"}']                  |
| ['Abdullayev Cavid Aydin Oglu Javid']         |     1 | 23.09.1990   | ['79065074747'] | ['cavid0482@gmail.com']           |                                                                                                                                 | ['{"Заказчик": "ООО «Сколмед»"}']                  |
| ['Abdurazokov Mirkomil Murodil Ugli']         |     1 | 26.01.2004   | ['79037552214'] | ['kahor@mail.ru']                 |                                                                                                                                 | ['{"Заказчик": "АО «МОБИМЕД» Мичуринский"}']       |
| ['Abduzukhrov Jamshidjon Tolibovich']         |     1 | 17.06.1983   | ['79670798658'] | ['abrorov@yahoo.com']             |                                                                                                                                 | ['{"Заказчик": "АО «МОБИМЕД» Домодедово"}']        |
| ['Abdyeva Sapargul']                          |     0 | 23.03.1975   | ['79654121217'] | ['demoandroio@gmail.com']         | [Row(type=4, serial='663349287', country='RUS', date_issue=None, date_expire=None, authority='МВД 0401', authority_code=None)]  | ['{"Заказчик": "АО «МОБИМЕД» Домодедово"}']        |
| ['Abido Maria De Lourdes']                    |     0 | 19.10.1946   | ['79153707369'] | ['alfeola@mail.ru']               |                                                                                                                                 | ['{"Заказчик": "АО «МОБИМЕД» Домодедово"}']        |
| ['Abramova Nika']                             |     0 | 25.02.1993   | ['79164050987'] | ['nikafs_93@mail.ru']             | [Row(type=4, serial='759511445', country='RUS', date_issue=None, date_expire=None, authority='МВД 77306', authority_code=None)] | ['{"Заказчик": "АО «МОБИМЕД» Домодедово"}']        |
| ['Achilova Mamlakat Ergashevna']              |     0 | 24.06.1985   | ['79257752633'] |                                   |                                                                                                                                 | ['{"Заказчик": "ООО «Сколмед»"}']                  |
| ['Adnan Ibrahim Qarah']                       |     1 | 01.02.1969   | ['79951150303'] |                                   |                                                                                                                                 | ['{"Заказчик": "Верба Экспресс"}']                 |
| ['Afonso Juelma Calabria Cani']               |     0 | 19.09.1999   | ['79777160800'] | ['dennilsonmiranda49@gmail.com']  |                                                                                                                                 | ['{"Заказчик": "АО «МОБИМЕД» Домодедово"}']        |
| ['Agapov Filipp']                             |     1 | 05.04.1987   | ['79213678850'] | ['f.agapov@mail.ru']              | [Row(type=4, serial='759973886', country='RUS', date_issue=None, date_expire=None, authority='МВД 78039', authority_code=None)] | ['{"Заказчик": "АО «МОБИМЕД» Домодедово"}']        |
| ['Agbayahoun Henri Joel']                     |     1 | 04.03.1998   | ['79804361071'] |                                   |                                                                                                                                 | ['{"Заказчик": "АО «МОБИМЕД» Домодедово"}']        |
| ['Agrawal Sanjeev Kumar']                     |     1 | 15.02.1972   | ['79031321886'] | ['henamohan@gmail.com']           |                                                                                                                                 | ['{"Заказчик": "АО «МОБИМЕД»"}']                   |
| ['Aguie Yves Gael Audran']                    |     1 | 08.09.1989   | ['79990033709'] | ['audrangael0@gmail.com']         |                                                                                                                                 | ['{"Заказчик": "АО «МОБИМЕД» Домодедово"}']        |
```