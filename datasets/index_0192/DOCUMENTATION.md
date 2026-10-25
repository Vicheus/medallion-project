# Parsetron results

## About row data

> - Code name: index_0192
> - File path: /media/user/SAMSUNG/Databases/index_0192/raw/users_preprocessed.csv
> - Total rows: 15133

### Schema
```
root
 |-- LOGIN: string (nullable = true)
 |-- PASSWORD: string (nullable = true)
 |-- NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- SECOND_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- PERSONAL_PHONE: string (nullable = true)

```

### Data sample
```
| LOGIN               | PASSWORD                                 | NAME                   | LAST_NAME     | SECOND_NAME   | EMAIL                           |   PERSONAL_PHONE |
|:--------------------|:-----------------------------------------|:-----------------------|:--------------|:--------------|:--------------------------------|-----------------:|
| admin               | 6o@O8pV~b2951cf33c90a891369052e1379023fb | Site                   | Admin         |               | shop@pplus.by                   |           324324 |
| content             | Pt8:1pG;6473884d234647c225e7f33f33f0388c | Контент-редактор       |               |               | shop@pplus.by                   |                  |
| SEOadmin            | r\Y4i6P~02a51e0354c607f3c6c61fb02a18d9d9 | SEOadmin               | SEOadmin      | SEOadmin      | denis@db.by                     |                  |
| internet-shop       | hELFYYeQ53c9aeb47aceca356c99df1da5f29c4b | Администратор          | Администратор | Администратор | shop@pplus.by                   |                  |
| internet-shop2      | h*7A,oT690b8dfa84b4bd0e2b7f778f30f279e7d | Администратор          | Администратор | Администратор | shop@pplus.by                   |                  |
| asoqo               | zsDOsCMu5e15865f6fad109ca00e0988cb004ee7 | Григорий               | Романов       |               | asoqo@mail.ru                   |                  |
| anonymous_2gXOSYCF3 | NJ60Taf4fc70e31099c3765379338d27a84a2da8 | Анонимный пользователь |               |               | anonymous_2gXOSYCF3@example.com |                  |
| artem.kovrigo       | O]p7,W9r440722f2f4cb3577d765db684c882b33 | artem                  | kovrigo       |               | artem.kovrigo@pplus.by          |                  |
| сара                | 6UVIan6Xde9cf678a41234fad935113d1b197da4 | александра             | поплавская    |               | poplavskaya.sanya@mail.ru       |                  |
| petrovich           | 7A6xitiec8deeeed83f7c735c4b1d6950c355f46 | Артур                  | Петрович      |               | petrovichab@gmail.com           |                  |
| donvaleron7         | FhUbNY126386d3b94ace1bdbb7b38f261819a883 | Валерий                | Латочко       |               | valeron7@tut.by                 |                  |
| natallia120289      | sIRELwmvd5a81d847925c7d71a834faa01955107 | Наталья                |               |               | natallia1202@yandex.ru          |                  |
| m3gap1har           | J68cxCv62dce1f0350fbc3309201876fc4b45932 | Елена                  | Пучкова       |               | m.c.fly@tut.by                  |                  |
| dashapashik         | 0BNJMdL8befae46f56d56ed61d4ad69a1825c5bf | Даша                   | Пашик         |               | dasha_pashulya_92@mail.ru       |                  |
| liliya.kohovec      | 8SAv0HyX4265fef1188397cca4a61f2cbf5d245a | liliya                 | kohovec       |               | liliya.kohovec@pplus.by         |                  |
| andrey.dobrovolskiy | 4L6gq5I4d98ab51d531a9b3c89f3779a8747784f | andrey                 | dobrovolskiy  |               | andrey.dobrovolskiy@pplus.by    |                  |
| egabist             | 5eHUVinD94f7b352c3a779d6555d0759bda9a5c9 | Егор                   | Шарец         |               | sharets@list.ru                 |                  |
| dasha_cherne        | 3M7nyS9Ifa51693ada4d9b7543590d762f0f95c1 | Даша                   | Черненко      |               | daryachernenko4@gmail.com       |                  |
| ummu                | KVnP75zu25a4ff39b356264adac117c3fa7befde | Абдуллах               | Стадник       |               | ummuasiya9@gmail.com            |                  |
| witka8686           | Ev0Y8bjI40e308a115c68c10132da6e2edd2ae25 | Виталий                | Порфененко    |               | witka86@yandex.by               |                  |
```


## About final data
> - Total rows: 11618

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```

### Data sample
```
| names                          | phones   | emails                           | accounts                                                                                                                               |
|:-------------------------------|:---------|:---------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| ['Admin Site']                 |          | ['shop@pplus.by']                | [Row(title='Алло', link='https://alloplus.by', login='admin', password_hash='6o@O8pV~b2951cf33c90a891369052e1379023fb')]               |
| ['Контент-Редактор']           |          | ['shop@pplus.by']                | [Row(title='Алло', link='https://alloplus.by', login='content', password_hash='Pt8:1pG;6473884d234647c225e7f33f33f0388c')]             |
| ['Seoadmin Seoadmin Seoadmin'] |          | ['denis@db.by']                  | [Row(title='Алло', link='https://alloplus.by', login='SEOadmin', password_hash='r\\Y4i6P~02a51e0354c607f3c6c61fb02a18d9d9')]           |
| ['Романов Григорий']           |          | ['asoqo@mail.ru']                | [Row(title='Алло', link='https://alloplus.by', login='asoqo', password_hash='zsDOsCMu5e15865f6fad109ca00e0988cb004ee7')]               |
| ['Kovrigo Artem']              |          | ['artem.kovrigo@pplus.by']       | [Row(title='Алло', link='https://alloplus.by', login='artem.kovrigo', password_hash='O]p7,W9r440722f2f4cb3577d765db684c882b33')]       |
| ['Поплавская Александра']      |          | ['poplavskaya.sanya@mail.ru']    | [Row(title='Алло', link='https://alloplus.by', login='сара', password_hash='6UVIan6Xde9cf678a41234fad935113d1b197da4')]                |
| ['Петрович Артур']             |          | ['petrovichab@gmail.com']        | [Row(title='Алло', link='https://alloplus.by', login='petrovich', password_hash='7A6xitiec8deeeed83f7c735c4b1d6950c355f46')]           |
| ['Латочко Валерий']            |          | ['valeron7@tut.by']              | [Row(title='Алло', link='https://alloplus.by', login='donvaleron7', password_hash='FhUbNY126386d3b94ace1bdbb7b38f261819a883')]         |
| ['Наталья']                    |          | ['natallia1202@yandex.ru']       | [Row(title='Алло', link='https://alloplus.by', login='natallia120289', password_hash='sIRELwmvd5a81d847925c7d71a834faa01955107')]      |
| ['Пучкова Елена']              |          | ['m.c.fly@tut.by']               | [Row(title='Алло', link='https://alloplus.by', login='m3gap1har', password_hash='J68cxCv62dce1f0350fbc3309201876fc4b45932')]           |
| ['Пашик Даша']                 |          | ['dasha_pashulya_92@mail.ru']    | [Row(title='Алло', link='https://alloplus.by', login='dashapashik', password_hash='0BNJMdL8befae46f56d56ed61d4ad69a1825c5bf')]         |
| ['Kohovec Liliya']             |          | ['liliya.kohovec@pplus.by']      | [Row(title='Алло', link='https://alloplus.by', login='liliya.kohovec', password_hash='8SAv0HyX4265fef1188397cca4a61f2cbf5d245a')]      |
| ['Dobrovolskiy Andrey']        |          | ['andrey.dobrovolskiy@pplus.by'] | [Row(title='Алло', link='https://alloplus.by', login='andrey.dobrovolskiy', password_hash='4L6gq5I4d98ab51d531a9b3c89f3779a8747784f')] |
| ['Шарец Егор']                 |          | ['sharets@list.ru']              | [Row(title='Алло', link='https://alloplus.by', login='egabist', password_hash='5eHUVinD94f7b352c3a779d6555d0759bda9a5c9')]             |
| ['Черненко Даша']              |          | ['daryachernenko4@gmail.com']    | [Row(title='Алло', link='https://alloplus.by', login='dasha_cherne', password_hash='3M7nyS9Ifa51693ada4d9b7543590d762f0f95c1')]        |
| ['Стадник Абдуллах']           |          | ['ummuasiya9@gmail.com']         | [Row(title='Алло', link='https://alloplus.by', login='ummu', password_hash='KVnP75zu25a4ff39b356264adac117c3fa7befde')]                |
| ['Порфененко Виталий']         |          | ['witka86@yandex.by']            | [Row(title='Алло', link='https://alloplus.by', login='witka8686', password_hash='Ev0Y8bjI40e308a115c68c10132da6e2edd2ae25')]           |
| ['Яровой Павел']               |          | ['pasha.yarick@yandex.ru']       | [Row(title='Алло', link='https://alloplus.by', login='Yarick', password_hash='Sj0ldmRn46722ccc2006773713cb2af2770ab1fe')]              |
| ['Желткович Ирина']            |          | ['zheltkovich.82@mail.ru']       | [Row(title='Алло', link='https://alloplus.by', login='1312', password_hash='Ne5AKSYQ79d7039fb003774705e50c69861e07d4')]                |
| ['Царьков Ярослав']            |          | ['yariktsarik@gmail.com']        | [Row(title='Алло', link='https://alloplus.by', login='YYT', password_hash='DXPMYYRDe880a3344d1fd720dd141413b1e56ebe')]                 |
```