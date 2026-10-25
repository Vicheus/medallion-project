# Parsetron results

## About row data

> - Code name: index_0668
> - File path: mobchasti_ru_22_7k_09_02_2024.csv
> - Total rows: 22711

### Schema
```
root
 |-- email: string (nullable = true)
 |-- phone_number: string (nullable = true)
 |-- address: string (nullable = true)
 |-- name: string (nullable = true)
 |-- surname: string (nullable = true)
 |-- patronymic: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- ip: string (nullable = true)

```

### Data sample
```
| email                          |   phone_number | address                                                                                                 | name          | surname      | patronymic    | birth_date   | ip              |
|:-------------------------------|---------------:|:--------------------------------------------------------------------------------------------------------|:--------------|:-------------|:--------------|:-------------|:----------------|
| r_rud970@mail.ru               |    79145690716 | 676290, г. Тында, Красная Пресня, 27                                                                    | Рудольф       |              |               | 16.01.1970   | 172.68.10.230   |
| kovach7411@gmail.com           |    79155301934 |                                                                                                         | Михаил        | Ковач        | Андреевич     |              | 162.158.239.36  |
| nsabardak73@mail.ru            |    79963834694 | г. Москва, м. Царицыно, выход №1, ул. Каспийская 36 стр 2, Царицынский рынок, 2 этаж, павильон Мобчасти | Николай       |              |               | 16.04.1973   | 162.158.202.175 |
| zaxar4422@ya.ru                |    79210728953 |                                                                                                         | Александровна | Валентина    | Локашева      |              | 162.158.239.36  |
| maksvlasov555@gmail.com        |    79278307441 | 433750, Барыш, Кирова, 135, 10                                                                          | Максим        |              |               | 04.01.1986   | 162.158.158.118 |
| maltsev.aa@gmail.com           |    79824813443 |                                                                                                         | Александр     | Мальцев      | Александрович |              | 172.70.247.176  |
| coop01@mail.ru                 |    79144776788 | 674500 Забайкальский край, пгт.Оловянная, ул.Перова 19/3                                                | Викторович    | Андрей       |               |              | 162.158.202.73  |
| danmlmuhametzanov@gmail.com    |    79093490934 |                                                                                                         | Вильдан       | Мухаметзянов | Ирикович      |              | 172.68.11.110   |
| iljinov.serezha@yandex.ru      |    79148845623 |                                                                                                         | Сергей        | Ильинов      | Георгиевич    |              | 141.101.77.229  |
| konstantin150697feet@gmail.com |    79182965228 |                                                                                                         | Константин    |              |               | 15.06.1997   | 172.70.246.226  |
| vma66@rambler.ru               |    79372223905 |                                                                                                         | Виктор        | Митюков      | Александрович |              | 108.162.229.99  |
| sanja1221@gmail.com            |    79836027984 |                                                                                                         | Александр     | Будкин       | Михайлович    |              | 172.71.102.28   |
| remkomp72@gmail.com            |    79323212886 |                                                                                                         | Давыдов       | Владимир     |               |              | 162.158.111.6   |
| knayzev010@mail.ru             |    79912482494 |                                                                                                         | Буданцев      | Рамиль       | Идрисович     |              | 162.158.182.32  |
| petrov-maxim1993@yandex.ru     |    79998491617 |                                                                                                         | Максим        |              |               |              | 172.71.98.126   |
| andrey12041992@yandex.ru       |    79513409173 | ______________________________________________________________                                          | Андрей        |              |               | 12.04.1992   | 108.162.229.141 |
| bobbarbanell@rambler.ru        |    79093490934 |                                                                                                         | Вильдан       |              |               |              | 172.68.11.150   |
| refa69@mail.ru                 |    79261215569 | 142440 Московская область Ногинский район посёлок Обухово ул Советская дом 29                           | Р             | Хикматов     | М             |              | 162.158.183.238 |
| bogorodsky.leha@yandex.ru      |    79511331860 |                                                                                                         | Алексей       |              |               |              | 172.68.244.33   |
| slabov.si@yandex.ru            |    79104278714 |                                                                                                         | Иванович      | Сергей       |               |              | 162.158.94.58   |
```


## About final data
> - Total rows: 3798

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 17.14% |
| Phones | 100.00% |
| Address | 4.11% |
| Ips | 96.84% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                               | birth_date   | phones          | address                                | ips                                                                                                   | source_entity_id                                         |
|:------------------------------------|:-------------|:----------------|:---------------------------------------|:------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| ['Дидич Дмитрий Александрович']     |              | ['79028250700'] |                                        | [Row(ip='172.71.246.90', date=None, comment=None)]                                                    | ebbed355a206325dfdd525532b82679cf50b6c28e8a75ded6dbfff75 |
| ['Никифоров Ярослав Александрович'] | 01.01.1970   | ['79637804120'] |                                        | [Row(ip='172.70.243.167', date=None, comment=None)]                                                   | d34ce90e1607ce545531840816fd22a24192888099e04e420083509d |
| ['Таджика Хуршед Хасанович']        |              | ['79522223675'] |                                        | [Row(ip='162.158.111.78', date=None, comment=None)]                                                   | 1c771753459b5ad2063e6cdd7be70a292464395847827dd8e03e96f8 |
| ['Максим']                          | 04.01.1986   | ['79278307441'] | ['433750 Барыш Кирова 135 10']         | [Row(ip='162.158.158.118', date=None, comment=None)]                                                  | ad98f63a81e6d734efcf57c805c16f62e1b888c0689b69df6e2af701 |
| ['Артур']                           | 06.09.1987   | ['79872580505'] |                                        | [Row(ip='172.68.10.115', date=None, comment=None)]                                                    | 06bcd9b8e9482e5ef5c405c249fc4f3b74f32bee07c9358ae15b2e74 |
| ['Беляев Владимир Николаевич']      |              | ['79050534010'] |                                        | [Row(ip='172.71.98.126', date=None, comment=None)]                                                    | f824bb1d68425005e8367ea51077fe6fe9c8a6ff0e763ca4affc4008 |
| ['Савенко Евгений Сергеевич']       |              | ['79601885552'] |                                        | [Row(ip='141.101.77.65', date=None, comment=None)]                                                    | 25d7c0775d48e746e74bef4a2ef5e055c84281a34af8d19f4bc274b2 |
| ['Спаринопта Андрей Сергеевич']     |              | ['79264703948'] |                                        | [Row(ip='162.158.134.10', date=None, comment=None)]                                                   | 68962bf57c8d904c4116f080ac3e14874b7616363c24976d0658db62 |
| ['Дмитрий']                         | 11.02.1988   | ['79788880380'] | ['г.Феодосия ул. Старшинова 21 кв.98'] | [Row(ip='141.101.77.65', date=None, comment=None)]                                                    | d31518fe4bedd91aee7b88be5da0ed3ecb9b3efac5efe723c1ccfd31 |
| ['Игорь']                           | 14.08.1992   | ['79028811401'] |                                        | [Row(ip='141.101.77.5', date=None, comment=None)]                                                     | 319281907d41c402b1951b560e0fae9da68e8a9d2f5258d996bd107d |
| ['Кривенцев Артем Вячеславович']    |              | ['79936140803'] |                                        | [Row(ip='162.158.239.50', date=None, comment=None)]                                                   | 48a194e1b37bfaaf0d9f516a826032162277679227950b585ac7c21d |
| ['Рашит']                           |              | ['79603869914'] |                                        |                                                                                                       | df67f304504d7d1cfb07bccf5a149fad2b9462f47e41112a083852ce |
| ['Седова Елена Сергеевна']          |              | ['79044441766'] |                                        | [Row(ip='162.158.86.217', date=None, comment=None)]                                                   | 308d3b914122575828b1a816a2fdbeace27a4a72edb1d1f1706da47a |
| ['Сергей Германович Самсонов']      |              | ['79374359750'] |                                        | [Row(ip='172.71.246.67', date=None, comment=None)]                                                    | cb811bd03c1ac13a448588f19cda8874289e1324bf362d7371b93a1e |
| ['Барсук Светлана Борисовна']       |              | ['79147848664'] |                                        | [Row(ip='172.71.98.94', date=None, comment=None)]                                                     | 0fa41ba53cab3d1079b4e4053bddaa2e85804dc7d8d63b6de9918318 |
| ['Гулящев Дмитрий Геннадьевич']     |              | ['79084757868'] |                                        | [Row(ip='172.70.111.85', date=None, comment=None)]                                                    | 5b666d320b305500f85908c72f8d5b00c465ba415267b30f6e9567a9 |
| ['Одинцов Игорь Сергеевич']         |              | ['79042096300'] |                                        | [Row(ip='172.70.250.148', date=None, comment=None)]                                                   | 74ce67270e57d9c5eab94b48230819b36b58de91698c6c96df881140 |
| ['Попов Леонид Константинович']     |              | ['79043815224'] |                                        | [Row(ip='162.158.183.156', date=None, comment=None), Row(ip='172.71.98.58', date=None, comment=None)] | f12d6e842f65d179d113a2db9fb7c616fab708db3305fb078b6a1a55 |
| ['Абдумелов Ю А']                   |              | ['79915001687'] |                                        | [Row(ip='162.158.110.100', date=None, comment=None)]                                                  | 5ff34a8f6f2e802db484e056bbb62ed164b1d4055443e8b0b4a27f63 |
| ['Антон']                           | 21.08.1989   | ['79154181617'] |                                        | [Row(ip='172.70.251.143', date=None, comment=None)]                                                   | da929121e8f219faaff179a65474b25349059fcad40b50901ed025d5 |
```