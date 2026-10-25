# Parsetron results

## About row data

> - File path: kvadroom_ru.csv
> - Total rows: 225234

### Schema
```
root
 |-- E-Mail: string (nullable = true)
 |-- Phone: string (nullable = true)
 |-- Full Name: string (nullable = true)
 |-- Name: string (nullable = true)
 |-- Otchest: string (nullable = true)
 |-- Reg Date: string (nullable = true)
 |-- Bal: double (nullable = true)
 |-- Company: string (nullable = true)
 |-- Pass: string (nullable = true)

```

### Data sample
```
| E-Mail                    |     Phone | Full Name    | Name      | Otchest       | Reg Date   |   Bal | Company               | Pass       |
|:--------------------------|----------:|:-------------|:----------|:--------------|:-----------|------:|:----------------------|:-----------|
| Ledeneva-t@mail.ru        | 487950582 | Леденева     | Татьяна   | Валерьевна    | 2010-08-11 |     0 | "АН ""Держава"        | 68563      |
| ukrconsalt-n@narod.ru     | 487997481 | Андреева     | Екатерина | Леонидовна    | 2010-05-18 |     0 | "ООО""Укрконсалт-Н""" | 48542      |
| maxssud@bigmir.net        | 500419071 | Сидоров      | Максим    | Сергеевич     | 2009-11-26 |   137 | <blank>               | 434351     |
| sergeyrabota10@rambler.ru | 501304000 | Иванов       | Сергей    | Станиславович | 2011-09-28 |     0 | <blank>               | 28121      |
| jul_bo@mail.ru            | 502032907 | <blank>      | Ирина     | Евгеньевна    | 2009-06-05 |   227 | <blank>               | 58629      |
| Linysachief@gmail.com     | 502382052 | Шевякова     | Инна      | Игоревна      | 2009-06-17 |   227 | <blank>               | 41052      |
| dommechti2010@mail.ru     | 503118340 | Новак        | Алёна     | Витальевна    | 2010-09-06 |     0 | felixnovak            | 28147      |
| smokeonawater@bigmir.net  | 503913864 | Василькова   | Светлана  | Зиновьевна    | 2009-04-16 |   227 | <blank>               | 50106      |
| kvartiru@list.ru          | 503925698 | Шпора        | Сергей    | Николаевич    | 2011-04-05 |     0 | Премьер               | 43326      |
| lgr@rbcmail.ru            | 505373820 | Григорьева   | Любовь    | Васильевна    | 2009-03-16 |   227 | <blank>               | 75009      |
| paxanec@yandex.ru         | 505985471 | Боков        | Вячеслав  | Валентинович  | 2009-03-05 |   227 | <blank>               | 23953      |
| tatyana-pelipas@mail.ru   | 506044750 | Пелипас      | Татьяна   | Анатольевна   | 2010-04-14 |     0 | "АН ""Киев-риэлти"""  | 47718      |
| borispolbalro@mail.ru     | 506085315 | Лобкова      | Анна      | Ивановна      | 2010-07-16 |   137 | <blank>               | 60488      |
| yukka2904@mail.ru         | 506454187 | Булгакова    | Юлия      | Анатольевна   | 2009-06-02 |   187 | <blank>               | 62975      |
| evpastyle@mail.ru         | 506505678 | Грубар       | Андрей    | Богданович    | 2012-01-02 |     3 | <blank>               | 9770465    |
| evpastyle@list.ru         | 506505678 | Попов        | Андрей    | Богданович    | 2009-03-13 |   187 | <blank>               | 336764     |
| city2002@inbox.ru         | 506971377 | Толстолуцкий | Вячеслав  | Викторович    | 2009-03-19 |   227 | <blank>               | 3691465    |
| Lr_irina@mail.ru          | 507218072 | Антонова     | Ирина     | Анатольевна   | 2012-02-28 |     0 | <blank>               | zvbkkbjyth |
| tata82107@mail.ru         | 507744558 | Шатная       | Наталья   | Григорьевна   | 2011-04-16 |   170 | <blank>               | 6271698    |
| lybovgashek@mail.ru       | 507776734 | Гашек        | Любовь    | Яновна        | 2012-02-22 |     0 | <blank>               | lg100472   |
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
 |-- actuality: string (nullable = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.83% |
| Phones | 99.59% |
| Actuality | 99.99% |
| Works | 9.09% |
| Accounts | 99.83% |



### Data sample
```
| names                              | emails                      | phones          | actuality   | works                                                                                                     | accounts                                                                                               |
|:-----------------------------------|:----------------------------|:----------------|:------------|:----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| ['Черкасова Наталья Васильевна']   | ['nataly_chefa@mail.ru']    |                 | 23.11.2010  | [Row(post=None, date_start=None, date_end=None, company='а.с.Столица', address=None, comment=None)]       | [Row(title='Квадрум', link='https://kvadroom.ru', login='nataly_chefa@mail.ru', password='65450')]     |
| ['Михеев Алексей Владимирович']    | ['ria.kn1@mail.ru']         | ['73912144025'] | 10.09.2011  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='ria.kn1@mail.ru', password='40910')]          |
| ['Кузнецова Ирина Николаевна']     | ['5006237@mail.ru']         | ['74955006237'] | 05.08.2010  | [Row(post=None, date_start=None, date_end=None, company='Бест-недвижимость', address=None, comment=None)] | [Row(title='Квадрум', link='https://kvadroom.ru', login='5006237@mail.ru', password='9092653')]        |
| ['Баска Олег Юрьевич']             | ['baskakov_o@incom.ru']     | ['74955007150'] | 18.04.2012  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='baskakov_o@incom.ru', password='1234567890')] |
| ['Пушилина Наталья Викторовна']    | ['info@ant-est.ru']         | ['74955100565'] | 06.09.2010  | [Row(post=None, date_start=None, date_end=None, company='Антей-Эстейт', address=None, comment=None)]      | [Row(title='Квадрум', link='https://kvadroom.ru', login='info@ant-est.ru', password='46421')]          |
| ['Ирина Павловна']                 | ['strobmen@mail.ru']        | ['74956410901'] | 11.12.2009  | [Row(post=None, date_start=None, date_end=None, company='Строй-Профиль', address=None, comment=None)]     | [Row(title='Квадрум', link='https://kvadroom.ru', login='strobmen@mail.ru', password='62401')]         |
| ['Cтепанов Алексей Осипович']      | ['franc21@mail.ru']         | ['74957225434'] | 09.05.2011  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='franc21@mail.ru', password='22367')]          |
| ['Матвиюк Наталья Николаевна']     | ['9951258@mail.ru']         | ['74957416883'] | 20.02.2011  | [Row(post=None, date_start=None, date_end=None, company='АН Риэлт Академия', address=None, comment=None)] | [Row(title='Квадрум', link='https://kvadroom.ru', login='9951258@mail.ru', password='846751')]         |
| ['Малеева Елена Валерьевна']       | ['elmaleeva@mail.ru']       | ['74957559393'] | 29.02.2012  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='elmaleeva@mail.ru', password='admin123')]     |
| ['Вольская Татьяна Александровна'] | ['oskina.t@gmail.com']      | ['74959251192'] | 29.05.2012  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='oskina.t@gmail.com', password='169199')]      |
| ['Шибаев Владислав Юльевич']       | ['uzaoarenda@mail.ru']      | ['74959603337'] | 12.03.2009  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='uzaoarenda@mail.ru', password='749852')]      |
| ['Иванов Игорь Михайлович']        | ['doronina1111@rambler.ru'] | ['74959682464'] | 27.06.2009  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='doronina1111@rambler.ru', password='81493')]  |
| ['Шагов Сергей Артурович']         | ['sergey_lukyanov@bk.ru']   | ['74964440174'] | 18.08.2010  | [Row(post=None, date_start=None, date_end=None, company='Организация', address=None, comment=None)]       | [Row(title='Квадрум', link='https://kvadroom.ru', login='sergey_lukyanov@bk.ru', password='90870')]    |
| ['Вахтина Наталья Анатольевна']    | ['sesan@mail.ru']           | ['78442234580'] | 17.04.2012  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='sesan@mail.ru', password='984114')]           |
| ['Бувин Игорь Николаевич']         | ['buvin66@bk.ru']           | ['79015325347'] | 18.05.2010  | [Row(post=None, date_start=None, date_end=None, company='Инком', address=None, comment=None)]             | [Row(title='Квадрум', link='https://kvadroom.ru', login='buvin66@bk.ru', password='58282')]            |
| ['Орлова Любовь Сергеевна']        | ['2591954nb@mail.ru']       | ['79015726778'] | 16.03.2009  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='2591954nb@mail.ru', password='505128')]       |
| ['Александр Юрьевич']              | ['foxy.05@mail.ru']         | ['79015985388'] | 01.05.2011  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='foxy.05@mail.ru', password='77871')]          |
| ['Дзядук Елена Евгеньевна']        | ['d_chana@bk.ru']           | ['79031525265'] | 18.01.2010  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='d_chana@bk.ru', password='55587')]            |
| ['Кондратьева Анна Евгеньевна']    | ['kondraanna@mail.ru']      | ['79031591593'] | 16.06.2009  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='kondraanna@mail.ru', password='22477')]       |
| ['Чундраков Максим Александрович'] | ['mchundrakov@yandex.ru']   | ['79032357057'] | 12.03.2009  |                                                                                                           | [Row(title='Квадрум', link='https://kvadroom.ru', login='mchundrakov@yandex.ru', password='79879')]    |
```