# Parsetron results

## About row data

> - Code name: index_0230
> - File path: /media/user/SAMSUNG/Databases/index_0230/raw/РЖД Персонал (2022).txt
> - Total rows: 691443

### Schema
```
root
 |-- Место: string (nullable = true)
 |-- Имя: string (nullable = true)
 |-- Отчество: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Роль: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Номер телефона1: string (nullable = true)
 |-- Номер телефона2: string (nullable = true)
 |-- Номер телефона3: long (nullable = true)

```

### Data sample
```
| Место   | Имя          | Отчество      | Фамилия     | Роль                                                                                    | Почта   |   Номер телефона1 |   Номер телефона2 |   Номер телефона3 |
|:--------|:-------------|:--------------|:------------|:----------------------------------------------------------------------------------------|:--------|------------------:|------------------:|------------------:|
|         | Абибе        | Ябиновна      | Аджаева     | Уборщик производственных помещений                                                      |         |                   |                   |     nan           |
|         | Абук-Магомед | Митихерович   | Магомедов   | Слесарь аварийно-восстановительных работ                                                |         |                   |                   |     nan           |
|         | Азамат       | Каиржанович   | Ержанов     | Заместитель начальника дистанции (по контактной сети)                                   |         |       79724167159 |       79724165426 |     nan           |
|         | Айнур        | Галиевич      | Фазлетдинов | Монтер пути                                                                             |         |                   |                   |     nan           |
|         | Акмал        |               | Исаков      | Монтер пути                                                                             |         |                   |                   |     nan           |
|         | Акылбек      | Касимбекович  | Култеков    | Монтер пути                                                                             |         |                   |                   |     nan           |
|         | Алавди       | Насрудиевич   | Борзиев     | Слесарь аварийно-восстановительных работ                                                |         |                   |                   |     nan           |
|         | Александр    | Александрович | Волынец     | Помощник машиниста электропоезда                                                        |         |                   |                   |     nan           |
|         | Александр    | Александрович | Голованов   | Заместитель начальника центра                                                           |         |       79985773325 |       79985773304 |     nan           |
|         | Александр    | Александрович | Иванов      | Первый заместитель начальника центра                                                    |         |       79603828823 |       79603835669 |     nan           |
|         | Александр    | Александрович | Кравченко   | Механизатор (докер-механизатор) комплексной бригады на погрузочно- разгрузочных работах |         |                   |                   |     nan           |
|         | Александр    | Александрович | Кулин       | Монтер пути                                                                             |         |                   |                   |     nan           |
|         | Александр    | Александрович | Лапынин     | Мастер дорожный                                                                         |         |                   |                   |     nan           |
|         | Александр    | Александрович | Манин       | Ревизор по безопасности движения поездов                                                |         |       79143298793 |                   |     nan           |
|         | Александр    | Александрович | Митраков    | Помощник машиниста дизельпоезда                                                         |         |                   |                   |     nan           |
|         | Александр    | Александрович | Ободов      | Начальник центра                                                                        |         |       79985964509 |       79985964431 |       7.99859e+10 |
|         | Александр    | Александрович | Семыкин     | Машинист рельсового автобуса                                                            |         |                   |                   |     nan           |
|         | Александр    | Александрович | Скавронский | Монтер пути                                                                             |         |                   |                   |     nan           |
|         | Александр    | Александрович | Сторож      | Оператор котельной                                                                      |         |                   |                   |     nan           |
|         | Александр    | Александрович | Ткачев      | Машинист электровоза (грузовое движение)                                                |         |                   |                   |     nan           |
```


## About final data
> - Total rows: 232031

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)

```

### Data sample
```
| names                                | works                                                                                                                                                                                                      | phones                                        | emails                            |
|:-------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------|:----------------------------------|
| ['Абдрахманов Руслан Каюмович']      | [Row(post='Машинист электровоза грузовое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                                   |                                               | ['ruslanvoron@mail.ru']           |
| ['Абросимов Алексей Викторович']     | [Row(post='Помощник машиниста электровоза грузовое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                         |                                               | ['alex.14abrosim@yandex.ru']      |
| ['Авилова Елена Витальевна']         | [Row(post='Ведущий специалист по управлению персоналом', date_start=None, date_end=None, company='ОАО РЖД Отдел управления персоналом', address=None, comment=None)]                                       | ['79502551290', '79502551240']                | ['dcs6-evavilova@skzd.rzd']       |
| ['Авходыев Ринат Дамирович']         | [Row(post='Стропальщик', date_start=None, date_end=None, company='ОАО РЖД Восстановительный поезд на станции Ноябрьск I', address=None, comment=None)]                                                     |                                               | ['avrida92@yandex.ru']            |
| ['Агапова Надежда Юрьевна']          | [Row(post='Агент коммерческий', date_start=None, date_end=None, company='ОАО РЖД Погрузпункт станции Находка', address=None, comment=None)]                                                                | ['79985666018']                               |                                   |
| ['Агапонов Сергей Владимирович']     | [Row(post='Помощник машиниста тепловоза грузовое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                           |                                               | ['agaponov911@bk.ru']             |
| ['Агафонов Владимир Николаевич']     | [Row(post='Машинист электровоза грузового движения', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                                  |                                               | ['vovaagafonov710@gmail.com']     |
| ['Агронов Андрей Викторович']        | [Row(post='Машинист тепловоза маневровое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                                   |                                               | ['andrey.agronov@mail.ru']        |
| ['Азанов Сергей Викторович']         | [Row(post='Старший электромеханик', date_start=None, date_end=None, company='ОАО РЖД Куст тяговых подстанций станции Бисер станции Койва III группа', address=None, comment=None)]                         | ['79702145920']                               |                                   |
| ['Айвазян Степан Оганесович']        | [Row(post='Машинист электровоза грузовое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады Кавказская', address=None, comment=None)]                                        |                                               | ['stepan.a89@gmail.com']          |
| ['Акимов Андрей Александрович']      | [Row(post='Помощник машиниста электровоза грузовое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                         |                                               | ['akimov1984.akimov@yandex.ru']   |
| ['Александров Александр Павлович']   | [Row(post='Помощник машиниста электровоза грузовое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                         |                                               | ['san.aleksandrov2010@yandex.ru'] |
| ['Александрова Алла Вячеславовна']   | [Row(post='Кладовщик', date_start=None, date_end=None, company='ОАО РЖД Группа материально-технического обеспечения', address=None, comment=None)]                                                         | ['79111437216']                               |                                   |
| ['Александрович Василий Викторович'] | [Row(post='Помощник машиниста электровоза грузовое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                         |                                               | ['baldwolf@yandex.ru']            |
| ['Алексеев Алексей Геннадьевич']     | [Row(post='Машинист тепловоза маневровое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                                   |                                               | ['alexeeva.1977@bk.ru']           |
| ['Алексеев Евгений Юрьевич']         | [Row(post='Помощник машиниста электровоза грузового движения', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                        |                                               | ['alexev.evgeny@yandex.ru']       |
| ['Алексеенко Петр Степанович']       | [Row(post='Машинист электровоза грузовое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                                   |                                               | ['ptr.alekseenko@mail.ru']        |
| ['Алиев Роман Джаванширович']        | [Row(post='Машинист электровоза вспомогательная работа при депо', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                     |                                               | ['romanaliev102@gmail.com']       |
| ['Алимов Артем Альбертович']         | [Row(post='Старший электромеханик участок I группы', date_start=None, date_end=None, company='ОАО РЖД Участок связи и радиосвязи Кизнер искл.-Казань вкл.- Н.Аракчино искл.', address=None, comment=None)] | ['79163742699', '79163742383', '79163575869'] |                                   |
| ['Амелин Валерий Викторович']        | [Row(post='Машинист электровоза грузовое движение', date_start=None, date_end=None, company='ОАО РЖД Локомотивные бригады', address=None, comment=None)]                                                   |                                               | ['amelin_87@list.ru']             |
```