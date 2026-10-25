# Parsetron results

## About row data

> - Code name: index_0149
> - File path: /media/user/SAMSUNG/Databases/index_0149/raw/annex/dump_accounts_preprocessed.csv
> - Total rows: 51847

### Schema
```
root
 |-- fullname: string (nullable = true)
 |-- email1: string (nullable = true)
 |-- email2: string (nullable = true)
 |-- phone_h: decimal(22,0) (nullable = true)
 |-- phone_m: string (nullable = true)
 |-- phone_w: long (nullable = true)
 |-- company: string (nullable = true)
 |-- company_address: string (nullable = true)
 |-- passport: string (nullable = true)
 |-- passport_given: string (nullable = true)
 |-- passport_date: string (nullable = true)

```

### Data sample
```
| fullname                        | email1                  | email2                     | phone_h   |      phone_m |   phone_w | company   | company_address   | passport   | passport_given   | passport_date   |
|:--------------------------------|:------------------------|:---------------------------|:----------|-------------:|----------:|:----------|:------------------|:-----------|:-----------------|:----------------|
| Чайка Виктор Викторович         |                         | Provik34@gmail.com         |           |  +9180529181 |       nan |           |                   |            |                  |                 |
| Иляева Галина Николаевна        |                         | vakcina_67@mail.ru         |           |  +9883425780 |       nan |           |                   |            |                  |                 |
| Носенко Ирина Михайловна        |                         | ugrozzza@ya.ru             |           |  +9298431690 |       nan |           |                   |            |                  |                 |
| Бак Виталий Владимирович        |                         | antonryzhichenko@gmail.com |           |  +9189320577 |       nan |           |                   |            |                  |                 |
| Царёв Максим Анатольевич        | maxtsaryov@mail.ru      | maxtsaryov@gmail.ru        |           | +79182917616 |       nan |           |                   |            |                  |                 |
| Калюжный Лев Николаевич         |                         | hozhouse23@mail.ru         |           |  +9186678667 |       nan |           |                   |            |                  |                 |
| Корбмахер Наталья Александровна |                         | evegin88@gmail.com         |           | +79883677022 |       nan |           |                   |            |                  |                 |
| Вецель Евгений Анатольевич      | eugene.leonar@gmail.com | eugene.leonar@gmail.com    |           | +79227444440 |       nan |           |                   |            |                  |                 |
| Зубенок Анатолий Александрович  |                         | babenkovruslan8@gmail.com  |           |  +9183571738 |       nan |           |                   |            |                  |                 |
| Колбасов Сергей Николаевич      |                         | Svutowwmu@rambler.ru       |           |  +9298351962 |       nan |           |                   |            |                  |                 |
| Удалов Сергей Владимирович      |                         | art-direktor1@mail.ru      |           | +79059927011 |       nan |           |                   |            |                  |                 |
| Беба Нелли Николаевна           |                         | Ammavaru@yandex.ru         |           | +79002938547 |       nan |           |                   |            |                  |                 |
| Колдаев Дмитрий Викторович      | Calday.ozersk@gmail.com | calday.ozersk@gmail.com    |           |  +9681100110 |       nan |           |                   |            |                  |                 |
| Шамшура Александр Александрович |                         | Sven4031@gmail.com         |           |  +9186671070 |       nan |           |                   |            |                  |                 |
| Чикуров Александр Алексеевич    |                         | cefiro922@gmail.com        |           |  +9528305355 |       nan |           |                   |            |                  |                 |
| Абазян Екатерина Константиновна |                         |                            |           |  +9881364240 |       nan |           |                   |            |                  |                 |
| Тримбач Артем Валерьевич        |                         | tvi1952-05@mail.ru         |           |  +9180620172 |       nan |           |                   |            |                  |                 |
| Яковенко Валерий Николаевич     | vkern2345@gmail.com     | vkern2345@gmail.com        |           |  +9186474067 |       nan |           |                   |            |                  |                 |
| Рудых Евгений Андреевич         | kazuma1412512@gmail.com | kazuma1412512@gmail.com    |           |  +9189957967 |       nan |           |                   |            |                  |                 |
| Ветошкин Сергей Васильевич      |                         | vip.budimir@list.ru        |           |   9280391715 |       nan |           |                   |            |                  |                 |
```


## About final data
> - Total rows: 47803

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)

```

### Data sample
```
| names                               | phones          | emails                                        | works   | documents   |
|:------------------------------------|:----------------|:----------------------------------------------|:--------|:------------|
| ['Чайка Виктор Викторович']         |                 | ['provik34@gmail.com']                        |         |             |
| ['Иляева Галина Николаевна']        |                 | ['vakcina_67@mail.ru']                        |         |             |
| ['Носенко Ирина Михайловна']        |                 | ['ugrozzza@ya.ru']                            |         |             |
| ['Бак Виталий Владимирович']        |                 | ['antonryzhichenko@gmail.com']                |         |             |
| ['Царёв Максим Анатольевич']        | ['79182917616'] | ['maxtsaryov@mail.ru', 'maxtsaryov@gmail.ru'] |         |             |
| ['Калюжный Лев Николаевич']         |                 | ['hozhouse23@mail.ru']                        |         |             |
| ['Корбмахер Наталья Александровна'] | ['79883677022'] | ['evegin88@gmail.com']                        |         |             |
| ['Вецель Евгений Анатольевич']      | ['79227444440'] | ['eugene.leonar@gmail.com']                   |         |             |
| ['Зубенок Анатолий Александрович']  |                 | ['babenkovruslan8@gmail.com']                 |         |             |
| ['Колбасов Сергей Николаевич']      |                 | ['svutowwmu@rambler.ru']                      |         |             |
| ['Удалов Сергей Владимирович']      | ['79059927011'] | ['art-direktor1@mail.ru']                     |         |             |
| ['Беба Нелли Николаевна']           | ['79002938547'] | ['ammavaru@yandex.ru']                        |         |             |
| ['Колдаев Дмитрий Викторович']      |                 | ['calday.ozersk@gmail.com']                   |         |             |
| ['Шамшура Александр Александрович'] |                 | ['sven4031@gmail.com']                        |         |             |
| ['Чикуров Александр Алексеевич']    |                 | ['cefiro922@gmail.com']                       |         |             |
| ['Тримбач Артем Валерьевич']        |                 | ['tvi1952-05@mail.ru']                        |         |             |
| ['Яковенко Валерий Николаевич']     |                 | ['vkern2345@gmail.com']                       |         |             |
| ['Рудых Евгений Андреевич']         |                 | ['kazuma1412512@gmail.com']                   |         |             |
| ['Ветошкин Сергей Васильевич']      | ['79280391715'] | ['vip.budimir@list.ru']                       |         |             |
| ['Елисеев Павел Валерьевич']        |                 | ['p.eliseyev@gmail.com']                      |         |             |
```