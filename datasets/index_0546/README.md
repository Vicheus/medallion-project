# Parsetron results

## About row data

> - Code name: index_0546
> - File path: tеnchаt.ru-@StormBaseAdapter.csv
> - Total rows: 1230369

### Schema
```
root
 |-- source_id: string (nullable = true)
 |-- fio: string (nullable = true)
 |-- bdate: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- email: string (nullable = true)
 |-- inn: string (nullable = true)
 |-- address: string (nullable = true)
 |-- job_title: string (nullable = true)
 |-- company: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- instagram_username: string (nullable = true)
 |-- tenchat_username: string (nullable = true)
 |-- tenchat_id: string (nullable = true)
 |-- subscribers_count: string (nullable = true)
 |-- description: string (nullable = true)
 |-- work_status: string (nullable = true)
 |-- education: string (nullable = true)
 |-- photo: string (nullable = true)

```

### Data sample
```
|   source_id | fio             | bdate      |       phone | email   | inn   | address   | job_title            | company   | gender   | instagram_username   |   tenchat_username |   tenchat_id |   subscribers_count | description   | work_status   | education   | photo                                                                                               |
|------------:|:----------------|:-----------|------------:|:--------|:------|:----------|:---------------------|:----------|:---------|:---------------------|-------------------:|-------------:|--------------------:|:--------------|:--------------|:------------|:----------------------------------------------------------------------------------------------------|
|        8649 | Шейкин Артём    |            |             |         |       |           |                      |           |          |                      |            0148880 |         8649 |                   0 |               |               |             |                                                                                                     |
|        8650 | Алексей         |            |             |         |       |           |                      |           |          |                      |            0148881 |         8650 |                   0 |               |               |             |                                                                                                     |
|        8651 | Димон           |            | 79042885068 |         |       |           |                      |           |          |                      |            0148882 |         8651 |                   0 |               |               |             |                                                                                                     |
|        8652 | Заурбек         |            |             |         |       |           |                      |           |          |                      |            0148883 |         8652 |                   3 |               |               |             |                                                                                                     |
|        8653 | Е               |            |             |         |       |           |                      |           |          |                      |            0148884 |         8653 |                   0 |               |               |             |                                                                                                     |
|        8654 |                 |            |             |         |       |           |                      |           |          |                      |            0148885 |         8654 |                   0 |               |               |             |                                                                                                     |
|        8655 | Демидова Полина | 1991-04-08 |             |         |       | Москва    | Тендерный специалист |           |          |                      |            0148886 |         8655 |                  77 |               |               |             | https://cdn1.tenchat.ru/static/vbc-gostinder/user-picture/42473600-2794-46a5-85a2-38ca6af7c549.jpeg |
|        8656 |                 |            |             |         |       |           |                      |           |          |                      |            0148887 |         8656 |                   0 |               |               |             |                                                                                                     |
|        8657 | Николай         |            |             |         |       |           |                      |           |          |                      |            0148888 |         8657 |                   0 |               |               |             |                                                                                                     |
|        8658 | Дмитрий         |            |             |         |       |           |                      |           |          |                      |            0148889 |         8658 |                   0 |               |               |             |                                                                                                     |
|        8659 | Александр       |            | 79197207259 |         |       |           |                      |           |          |                      |            0148890 |         8659 |                   0 |               |               |             |                                                                                                     |
|        8660 | Дмитрий         |            |             |         |       |           |                      |           |          |                      |            0148891 |         8660 |                   0 |               |               |             |                                                                                                     |
|        8661 | Евгений         |            |             |         |       |           |                      |           |          |                      |            0148892 |         8661 |                   0 |               |               |             |                                                                                                     |
|        8662 | Андрей          |            |             |         |       |           |                      |           |          |                      |            0148893 |         8662 |                   0 |               |               |             |                                                                                                     |
|        8663 | Заур            |            |             |         |       |           |                      |           |          |                      |            0148894 |         8663 |                   0 |               |               |             |                                                                                                     |
|        8664 | Иван            |            |             |         |       |           |                      |           |          |                      |            0148895 |         8664 |                   0 |               |               |             |                                                                                                     |
|        8665 | Юлиан           |            |             |         |       |           |                      |           |          |                      |            0148896 |         8665 |                   0 |               |               |             |                                                                                                     |
|        8666 | Игорь           |            |             |         |       |           |                      |           |          |                      |            0148897 |         8666 |                   1 |               |               |             |                                                                                                     |
|        8667 |                 |            |             |         |       |           |                      |           |          |                      |            0148898 |         8667 |                   0 |               |               |             |                                                                                                     |
|        8668 | Антон           |            |             |         |       |           |                      |           |          |                      |            0148899 |         8668 |                   0 |               |               |             |                                                                                                     |
```


## About final data
> - Total rows: 92848

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 12.62% |
| Sex | 2.42% |
| Address | 27.98% |
| Phones | 99.95% |
| Emails | 0.05% |
| Documents | 5.14% |
| Socials | 1.78% |
| Works | 10.38% |
| Raw_metadata | 21.15% |



### Data sample
```
| names                           | birth_date   |   sex | address       | phones          | emails   | documents                                                                                                                   | socials   | works                                                                                                                | raw_metadata                                                                                                                                                                                                                                                                                                                                                               |
|:--------------------------------|:-------------|------:|:--------------|:----------------|:---------|:----------------------------------------------------------------------------------------------------------------------------|:----------|:---------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Димон']                       |              |   nan |               | ['79042885068'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Александр']                   |              |   nan |               | ['79197207259'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Андреев Андрей']              |              |   nan |               | ['79182618528'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Александр']                   |              |   nan |               | ['79622082684'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Дмитрий']                     |              |   nan |               | ['79145437518'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Сергей']                      |              |   nan |               | ['79009096830'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Жигалин Денис']               | 21.11.1989   |     1 | ['Москва']    | ['79104783068'] |          | [Row(type=1, serial='231306744571', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |           | [Row(post='Account Manager', date_start=None, date_end=None, company=None, address=None, comment=None)]              | ['{"description": "Привет 10 лет работаю в рекламной индустрии. Последнее время всё больше нахожу себя в проектах связанных с мерчем а именно одеждой и трендовыми атрибутами. Люблю музыку и прогулки - это главные источники вдохновения для работы. Ищу новых друзей и неспешно знакомлюсь с площадкой", "education": "Московский государственный институт культуры"}'] |
| ['Эдик']                        |              |   nan |               | ['79324247675'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['S Роман']                     |              |   nan |               | ['79283441737'] |          |                                                                                                                             |           | [Row(post='SMM-менеджер', date_start=None, date_end=None, company=None, address=None, comment=None)]                 | ['{"work_status": "NOTLOOKINGFORJOB"}']                                                                                                                                                                                                                                                                                                                                    |
| ['Илья']                        |              |   nan |               | ['79052220691'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Йонас']                       |              |   nan |               | ['79112145591'] |          | [Row(type=1, serial='360101003406', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Ткаченко Николай']            |              |   nan |               | ['79787188876'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Евгений']                     |              |   nan |               | ['79037432477'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Рожков Роман Викторович']     |              |   nan |               | ['79818222401'] |          | [Row(type=1, serial='781431314412', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Завьялов Олег Александрович'] |              |   nan |               | ['79108514110'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Владислав']                   |              |   nan |               | ['79393054776'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Алексей']                     |              |   nan |               | ['79257728100'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Виталий']                     |              |   nan |               | ['79506722555'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Andrey']                      |              |   nan |               | ['79048350254'] |          |                                                                                                                             |           |                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                            |
| ['Тураев Ильяс']                |              |   nan | ['Краснодар'] | ['79181596371'] |          | [Row(type=1, serial='644107245316', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |           | [Row(post='Главный управляющий директор', date_start=None, date_end=None, company=None, address=None, comment=None)] | ['{"subscribers_count": "349", "description": "Я занимаюсь ремонтом квартир домов офисов магазинов государству и частникам .В данный момент ремонтирую квартиры переселенцам из Херсонадетскому дому и переселенцам с ветхого жилья."}']                                                                                                                                   |
```