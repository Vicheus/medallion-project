# Parsetron results

## About row data

> - File path: detskiy_mir.csv
> - Total rows: 1048574

### Schema
```
root
 |-- bonus_card: string (nullable = true)
 |-- name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- user_agent: string (nullable = true)
 |-- date: timestamp (nullable = true)

```

### Data sample
```
|       bonus_card | name                  | email                               |       phone | user_agent   | date                |
|-----------------:|:----------------------|:------------------------------------|------------:|:-------------|:--------------------|
| 2221321156467176 | Дияна Расулова        | diana193333@icloud.com              | 79670259324 | IOSApp       | 2024-08-21 13:47:01 |
| 2221178779717951 | екатерина             | eklezzz@yandex.ru                   | 79061630330 | AndroidApp   | 2024-08-21 13:47:00 |
| 2221261296458968 | Давид Чалигава        | x96jbwr6t5@privaterelay.appleid.com | 79518397257 | IOSApp       | 2024-08-21 13:47:01 |
| 2221199394186950 | Екатерина Терещенко   | adidas04ka@mail.ru                  | 79089381129 | IOSApp       | 2024-08-21 13:47:00 |
| 2221146511789646 | Анастасия Перевышкова | n.perevishkova@yandex.ru            | 79261044888 | IOSApp       | 2024-08-21 13:47:00 |
| 2221281098374866 | Екатерина Иваненко    | kovalevaket1986@mail.ru             | 79186620075 | AndroidApp   | 2024-08-21 13:47:00 |
| 2221238067089677 | Виктор Шимченко       | shimchenkov@inbox.ru                | 79964691919 | IOSApp       | 2024-08-21 13:46:59 |
| 2221268876453996 | Анастасия Никонова    | sillynasti@vk.com                   | 79964022758 | IOSApp       | 2024-08-21 13:46:59 |
| 2221158906593038 | Антонина Кухарская    | a.kuharskaya@ru.mail                | 79064445045 | IOSApp       | 2024-08-21 13:46:58 |
| 2221190206240200 | Замира Богатырева     | zema081@mail.ru                     | 79218750706 | IOSApp       | 2024-08-21 13:46:59 |
| 2221159362802657 | Кристина Гвенетадзе   | qiso-piso1993@mail.ru               | 79622442288 | IOSApp       | 2024-08-21 13:46:57 |
| 2221138630489406 | Светлана Проценко     | protsenko-se@yandex.ru              | 79994319563 | AndroidApp   | 2024-08-21 13:46:57 |
| 2221162072014662 | Елена Марусина        | mit_ea@mail.ru                      | 79191391450 | website      | 2024-08-21 13:46:55 |
| 2221188825006879 | Марина Родина         | 686798@mail.ru                      | 79834200525 | IOSApp       | 2024-08-21 13:46:57 |
| 2221143570386109 | Лейла Алиева          | lalieva325@gmail.com                | 79180029634 | IOSApp       | 2024-08-21 13:46:56 |
| 2221203930219547 | Анастасия Косарева    | kosarevaaa925@gmail.com             | 79158232370 | IOSApp       | 2024-08-21 13:46:55 |
| 2221176872525594 | Ольга Шанскова        | olgashanskova@mail.ru               | 79876144375 | AndroidApp   | 2024-08-21 13:46:55 |
| 2221172167029418 | Нина                  | laim2116@yandex.ru                  | 79897107991 | IOSApp       | 2024-08-21 13:46:56 |
| 2221253614304305 | Aidanek Bakytbekova   | nurlan_1194@icloud.com              | 79969699044 | AndroidApp   | 2024-08-21 13:46:56 |
| 2221120343334640 | Валерия Донских       | valeriya_donskih@mail.ru            | 79261735898 | IOSApp       | 2024-08-21 13:46:55 |
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
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- client_card_number: string (nullable = true)
 |-- actuality: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.95% |
| Phones | 99.97% |
| Accounts | 100.00% |
| Actuality | 100.00% |
| Raw_metadata | 100.00% |



### Data sample
```
| names                     | emails                                  | phones          | accounts                                                                           | actuality   | raw_metadata                     |
|:--------------------------|:----------------------------------------|:----------------|:-----------------------------------------------------------------------------------|:------------|:---------------------------------|
| ['Дияна Расулова']        | ['diana193333@icloud.com']              | ['79670259324'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221321156467176')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Екатерина']             | ['eklezzz@yandex.ru']                   | ['79061630330'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221178779717951')] | 21.08.2024  | ['{"user_agent": "AndroidApp"}'] |
| ['Давид Чалигава']        | ['x96jbwr6t5@privaterelay.appleid.com'] | ['79518397257'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221261296458968')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Екатерина Терещенко']   | ['adidas04ka@mail.ru']                  | ['79089381129'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221199394186950')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Анастасия Перевышкова'] | ['n.perevishkova@yandex.ru']            | ['79261044888'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221146511789646')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Екатерина Иваненко']    | ['kovalevaket1986@mail.ru']             | ['79186620075'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221281098374866')] | 21.08.2024  | ['{"user_agent": "AndroidApp"}'] |
| ['Виктор Шимченко']       | ['shimchenkov@inbox.ru']                | ['79964691919'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221238067089677')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Анастасия Никонова']    | ['sillynasti@vk.com']                   | ['79964022758'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221268876453996')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Антонина Кухарская']    | ['a.kuharskaya@ru.mail']                | ['79064445045'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221158906593038')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Замира Богатырева']     | ['zema081@mail.ru']                     | ['79218750706'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221190206240200')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Кристина Гвенетадзе']   | ['qiso-piso1993@mail.ru']               | ['79622442288'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221159362802657')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Светлана Проценко']     | ['protsenko-se@yandex.ru']              | ['79994319563'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221138630489406')] | 21.08.2024  | ['{"user_agent": "AndroidApp"}'] |
| ['Елена Марусина']        | ['mit_ea@mail.ru']                      | ['79191391450'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221162072014662')] | 21.08.2024  | ['{"user_agent": "website"}']    |
| ['Марина Родина']         | ['686798@mail.ru']                      | ['79834200525'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221188825006879')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Лейла Алиева']          | ['lalieva325@gmail.com']                | ['79180029634'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221143570386109')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Анастасия Косарева']    | ['kosarevaaa925@gmail.com']             | ['79158232370'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221203930219547')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Ольга Шанскова']        | ['olgashanskova@mail.ru']               | ['79876144375'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221176872525594')] | 21.08.2024  | ['{"user_agent": "AndroidApp"}'] |
| ['Нина']                  | ['laim2116@yandex.ru']                  | ['79897107991'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221172167029418')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
| ['Aidanek Bakytbekova']   | ['nurlan_1194@icloud.com']              | ['79969699044'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221253614304305')] | 21.08.2024  | ['{"user_agent": "AndroidApp"}'] |
| ['Валерия Донских']       | ['valeriya_donskih@mail.ru']            | ['79261735898'] | [Row(title='Карта лояльности Детский мир', client_card_number='2221120343334640')] | 21.08.2024  | ['{"user_agent": "IOSApp"}']     |
```