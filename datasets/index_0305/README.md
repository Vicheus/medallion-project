# Parsetron results

## About row data

> - Code name: index_0305
> - File path: /media/user/SAMSUNG/Databases/index_0305/raw/address_preprocessed.csv
> - Total rows: 72129

### Schema
```
root
 |-- user_id: integer (nullable = true)
 |-- country: string (nullable = true)
 |-- index: integer (nullable = true)
 |-- region: string (nullable = true)
 |-- city: string (nullable = true)
 |-- street: string (nullable = true)
 |-- building: string (nullable = true)
 |-- room: string (nullable = true)

```

### Data sample
```
|   user_id | country   |   index | region               | city             | street    |   building |   room |
|----------:|:----------|--------:|:---------------------|:-----------------|:----------|-----------:|-------:|
|         2 |           |     nan |                      |                  |           |            |        |
|         1 |           |     nan |                      |                  |           |            |        |
|         6 |           |  610002 | Кировская Область    | Киров            |           |            |        |
|         7 |           |  249441 | Калужская Область    | Киров            |           |            |        |
|         2 |           |     nan |                      | Москва           | Тест      |          1 |     12 |
|         7 |           |  173008 | Новгородская Область | Великий Новгород |           |            |        |
|         7 |           |  173008 |                      | Великий Новгород |           |            |        |
|        14 |           |  601640 |                      | Карабаново       |           |            |        |
|         4 |           |  600014 |                      | Владимир         |           |            |        |
|        14 |           |  601640 |                      | Карабаново       |           |            |        |
|         4 |           |  600014 |                      | Владимир         | мира      |          1 |      2 |
|        15 |           |  101000 |                      | Москва           | test      |         44 |     44 |
|        16 |           |  141707 | Московская Область   | Долгопрудный     |           |            |        |
|        16 |           |  243140 | Брянская Область     | Клинцы           |           |            |        |
|        16 |           |     nan | Москва               | Москва           |           |            |        |
|        16 |           |  600014 | Владимирская Область | Владимир         |           |            |        |
|        16 |           |  123182 |                      | Москва           | Руставели |          3 |      2 |
|        17 |           |  101000 |                      | Москва           | Тестовая  |          1 |      1 |
|        17 |           |  101000 | Москва               | Москва           | Тестовая  |          1 |      1 |
|        17 |           |  101000 | Москва               | Москва           | Тестовая  |          1 |      1 |
```

> - Code name: index_0305
> - File path: /media/user/SAMSUNG/Databases/index_0305/raw/users_preprocessed.csv
> - Total rows: 53383

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- fullname: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- mobilephone: string (nullable = true)
 |-- lastlogin: long (nullable = true)
 |-- username: string (nullable = true)
 |-- password: string (nullable = true)

```

### Data sample
```
|   id | fullname                      | email                         | phone   |   mobilephone |   lastlogin | username                | password                                                     |
|-----:|:------------------------------|:------------------------------|:--------|--------------:|------------:|:------------------------|:-------------------------------------------------------------|
|    1 | Илья                          | ilia61@yandex.ru              |         |  +79127083169 |  1737035648 | admin                   | $2y$10$nsScAZBN8riKSXFlNWmaSuqTPFHO5Iy4csK3RvQgguOc4bRNa6KrS |
|    2 | Test                          | test@test.ru                  |         |  +71111111111 |           0 | test@test.ru            | $2y$10$.apJDGPWvtDrFwQSmhRUxuzpaUEfloNUNeR6cXcs5x85gQUUE4sx. |
|    3 |                               | next.level.seogroup@gmail.com |         |               |  1643282263 | seo                     | $2y$10$MnR5JL5OWb0MiUybgVVOwOL1MO.Uo5lL3yZpps5s6U4EfN2FQkquG |
|    4 | Николай Джоникидзе            | nik0lazzz@mail.ru             |         |  +79254323082 |           0 | nik0lazzz@mail.ru       | $2y$10$NdECFUBr/OIVqVRQOWLhIOlmwZANGob/j952UcVDfZFbB1R8ScPyC |
|    5 | Вапва                         | satalit844@mail.ru            |         |               |           0 | satalit844@mail.ru      | $2y$10$yFEZSODyJhZ9JZsHh6SIf.hIWdXNCQ3BTlOFzfttNqhq9Dwn54ZqG |
|    6 | Хохлунов                      | cgfc@sdfg.ru                  |         |  +79090990909 |           0 | cgfc@sdfg.ru            | $2y$10$vfj5OMZSwIPM89IejU9KluyRWngX9Kguiaf2ykhYvY6QfQfJVT60i |
|    7 | Тест                          | 8243844@gmail.com             |         |  +79688243844 |  1637399978 | 8243844@gmail.com       | $2y$10$gRv4mbx4hmRn54NF.Zig0.JYzzqvYkMgeaULXyNXWPsDKzEwNQxwq |
|   14 | 79254323082                   |                               |         |  +79254323082 |  1589785279 | 79254323082             | $2y$10$NiIz4Lfao4sYeOj.RzhK4eW.5xguj8Ii4LrzzZXYVYCBi.59AttxC |
|   15 | Test                          | ttt@ya.ru                     |         |               |           0 | ttt@ya.ru               | $2y$10$NGW0gRAjJxGGb1RIdemoO.3.YL1h3iMvxLsHzfOIWMPqFoNL4fA/C |
|   16 | Андрей                        | kudryavtsev87@yandex.ru       |         |               |           0 | kudryavtsev87@yandex.ru | $2y$10$Ipu7HXIw1NhgrmKvuTCIdekwkugYohqpplpNhETsWihaY4oiX9LOe |
|   17 | pavel                         | pavel.usachev@mation.ru       |         |               |  1590766979 | usachev                 | $2y$10$iQFsN2QBSKw1wjjC4dgOnuHLC./Z6BOq0KTB0TclRjFHjJdxnRtZe |
|   18 | Alex                          | 106@optnb.ru                  |         |               |  1620394452 | 106@optnb.ru            | $2y$10$fiaIdOq2.0FbVObieHsw3u3rKj7JDrIthyHslFZviKLs48S0xSQyW |
|   19 | Денис                         | 1@1.ru                        |         |               |           0 | 1@1.ru                  | $2y$10$aJYsJWpcWFORVkCFYAllQ.5Ji3Eiark5WxgMXex/V8wBZ7jzZius6 |
|   20 | Стреха Денис Александрович    | dstrekha@gmail.com            |         |  +79162736573 |           0 | dstrekha@gmail.com      | $2y$10$VvoPItsv5rf6V0S6QjqlCOmZ0IHT.5tokwMEQYfPJ2v3X35U41AZe |
|   21 | Павлова Татьяна               | berindat@mail.ru              |         |  +79031176961 |           0 | berindat@mail.ru        | $2y$10$.Y1hpiSym.OWOjKlTB1dvusX1YLWKukGIWgq2pRNw5zcY0e8R9dWC |
|   22 | Качина Мария Витальевна       | uoslpmhdik@yandex.ru          |         |  +79687248777 |           0 | uoslpmhdik@yandex.ru    | $2y$10$MHyVxDM7h2NydfliGPv3meNtdHZJgk6WB8nrPIkOojBQALSSuyW3C |
|   23 | Кузичев Вячеслав Вячеславович | 6912735@mail.ru               |         |  +79096912735 |           0 | 6912735@mail.ru         | $2y$10$gM1Y3tNAdrTM42I/VoHHFeAV9Y6JcDZI8w/jpYDdur6V6Hvz6uow. |
|   24 | Чебанов Сергей Юрьевич        | chebanov07@yandex.ru          |         |  +79032200602 |           0 | chebanov07@yandex.ru    | $2y$10$fuaGyItSfJMFYBf48y3JvuJ2OkTFTjVS4Wwt0AyG7waXP1y8yHXuS |
|   25 | Янкин Дмитрий Геннадиевич     | barrosha@bk.ru                |         |  +79035742012 |           0 | barrosha@bk.ru          | $2y$10$gkWn6JdwP7M.mns4jdcMqeVApdcsqjXZP9qwwOEqJHr.rbA3evpMS |
|   26 | Иван                          | net@net.ru                    |         |  +79160013940 |           0 | net@net.ru              | $2y$10$Pfy0ruAWgiFY1EC6fbDQa.Yjh3yNjCJplGdHf468fdMsKuh2Jm2aC |
```


## About final data
> - Total rows: 51550

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
 |    |-- element: string (containsNull = false)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- actuality: string (nullable = true)

```

### Columns completeness
```
{
    "names": 100.0,
    "emails": 99.89,
    "phones": 99.22,
    "address": 98.11,
    "accounts": 99.91,
    "actuality": 100.0
}
```

### Data sample
```
| names                           | emails                                                    | phones          | address                                                                                    | accounts                                                                                                                                                           | actuality   |
|:--------------------------------|:----------------------------------------------------------|:----------------|:-------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| ['A Александр']                 | ['urbis@bk.ru', 'ipp-natalia@yandex.ru']                  | ['74953536659'] | ['603000 Нижний Новгород Нижний Новгород']                                                 | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='ipp-natalia@yandex.ru', password_hash='$2y$10$brAgefC1WNxrYA4zCsEfWOKWFb99xNkaUXtLnTg2UxkHCA0kH/C8a')]     | 01.01.1970  |
| ['Aleksandr Golovin']           | ['q.golovin@gmail.com', '89276661516igor@gmail.com']      | ['79636668200'] | ['420000 Татарстан Казань']                                                                | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='89276661516igor@gmail.com', password_hash='$2y$10$gJycSc.ODFQ35nJuympR6.0emQI9Xjfmqg7gS8o1e9x/a898rN75m')] | 01.01.1970  |
| ['Alex']                        | ['106@optnb.ru']                                          |                 | ['101000 Москва Москва', '190000 Санкт-Петербург Санкт-Петербург пр-кт Юрия Гагарина 1 5'] | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='106@optnb.ru', password_hash='$2y$10$fiaIdOq2.0FbVObieHsw3u3rKj7JDrIthyHslFZviKLs48S0xSQyW')]              | 07.05.2021  |
| ['Alexander']                   | ['alex012008@gmail.com', 'serg.soloviev70@yandex.ru']     | ['79165150874'] | ['111674 Москва Москва']                                                                   | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='serg.soloviev70@yandex.ru', password_hash='$2y$10$LLiWni1J1XSAxkquZYeYveA5gv1vp25B9KEP64Y17VeqhzYXMZHR.')] | 01.01.1970  |
| ['Alexander Алекандр']          | ['916591@gmail.com', 'karlen532@gmail.com']               | ['79165913681'] | ['115162 Москва Москва Татищева 3А 102']                                                   | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='karlen532@gmail.com', password_hash='$2y$10$w0pUJfAPeOwzBk0zzDupseQk98RGCfYnVvs8RVKmh4QWIt0jB5TUC')]       | 01.01.1970  |
| ['Alyaev Bata']                 | ['ba7941@gmail.com', 'demkovn@mail.ru']                   | ['79672779939'] | ['141980 Московская Дубна']                                                                | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='demkovn@mail.ru', password_hash='$2y$10$v2hRF3gpNP.eKyW8pC/SFemVm1UnvyMdgb9eL52KaSINmnDj28see')]           | 01.01.1970  |
| ['Ambre Naturel']               | ['ambrenaturel@yandex.ru', 'ltreuk@bk.ru']                | ['79263361168'] | ['660000 Красноярск Красноярск ул Мечникова 11 47']                                        | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='ltreuk@bk.ru', password_hash='$2y$10$7KICmQjDFyL57QyFN5IBGubrgZRideYofvOtkOQK5ddr8jsG6h4iK')]              | 01.01.1970  |
| ['Aybyatova Regina']            | ['regina.aibyatova@gmail.com', 'aleksandr_37@list.ru']    | ['79625553737'] | ['153000 Иваново Иваново']                                                                 | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='Aleksandr_37@list.ru', password_hash='$2y$10$kMG5Cnq8/HfNA2vVTKqH.uCpfR/2ZPhxzS7t1CoYralJcnUvAAOcC')]      | 01.01.1970  |
| ['Ayoub Mohamed Samir Mohamed'] | ['msamirvip@yandex.ru', 'garaldo@mail.ru']                | ['79009574067'] | ['683024 Камчатский Петропавловск-Камчатский 50 лет Октября 171']                          | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='garaldo@mail.ru', password_hash='$2y$10$cYiGnzQxZYK3x4Vwl3yEPu3zSzifvU6emuajgtwJO/BRyIhGcBrQO')]           | 01.01.1970  |
| ['Azat']                        | ['azat.g@mail.ru', 'askerko1962@mail.ru']                 | ['79220997733'] | ['190000 Санкт-Петербург Санкт-Петербург']                                                 | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='askerko1962@mail.ru', password_hash='$2y$10$nOStignRjeAxevL3g6DA/.KNDYqLrAx4ArPMO6F1swQPCYjbQHphi')]       | 11.12.2020  |
| ['Aрсенкова Мария']             | ['1709rt@gmail.com', 'livepoddojdem18@gmail.com']         | ['79626189409'] | ['299011 Севастополь Севастополь пр-кт Победы 6 6']                                        | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='livepoddojdem18@gmail.com', password_hash='$2y$10$pOtC4DPMWM/L977BQ4q8p.36cermJSGOphwaxPbhn69CSBZLD34ya')] | 01.01.1970  |
| ['Bandit Aboba']                | ['aboba_bandit@mail.ru', 'tva3@inbox.ru']                 | ['78005553535'] | ['101000 Москва Москва']                                                                   | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='tva3@inbox.ru', password_hash='$2y$10$Ua6BRrE2fdtj.uWfp2tH.uxRsR5mfeg4.3oOJ8Q.6QnA.HPY2nzJG')]             | 01.01.1970  |
| ['Barbinyagra Alexander']       | ['a.barbinyagra@gmail.com', 'veskel66@yandex.ru']         | ['79266208022'] | ['111674 Москва Москва']                                                                   | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='veskel66@yandex.ru', password_hash='$2y$10$tb9qQPVMdYnL7p9VhbTR/epLw26pcFpnzhQxuffNYDlKk3wOHuID2')]        | 01.01.1970  |
| ['Bochkarev Semyon']            | ['imleerooy@gmail.com', 'evdolganov@gmail.com']           | ['79639030431'] | ['Москва Москва Софийская 261']                                                            | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='evdolganov@gmail.com', password_hash='$2y$10$RRD58JS4By7k4AXyuj8QgOCDQZXH5YOqFtoEVsKQig9aqMoI/q.7G')]      | 01.01.1970  |
| ['Bogoutdinov Vitaly']          | ['designb@mail.ru', 'p.shvedoff@gmail.com']               | ['79670588161'] | ['111673 Москва Москва ул Суздальская д 18 к 2 644']                                       | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='p.shvedoff@gmail.com', password_hash='$2y$10$GX8iB5dYfGZ92J9H9Soil.ZKDqyPGUUEcolcKTjJVW62ASdpOQ5my')]      | 01.01.1970  |
| ['Breg Dmitry']                 | ['dd_spam@hotmail.com', 'rustamshamiev@gmail.com']        | ['79055947782'] | ['101000 г Москва Москва']                                                                 | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='rustamshamiev@gmail.com', password_hash='$2y$10$1sM6vchZ.l1DOqXUXo0OeOsqx/vdLvIfxrsc1sS267xfJu5aR.1CS')]   | 01.01.1970  |
| ['C Ole']                       | ['oleg4110@mail.ru', 'n89376233410@gmail.com']            | ['79013678503'] | ['420000 Татарстан Казань']                                                                | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='n89376233410@gmail.com', password_hash='$2y$10$LysDLL3ivRp1KHHkhoZX9.fsSoCh.MsI74wdQWR7am6QRf.MoPnhK')]    | 01.01.1970  |
| ['Dima Arkatov']                | ['arkatov.dima@gmail.com', 'maksim_finogenov@mail.ru']    | ['79778779821'] | ['101000 Москва Москва']                                                                   | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='maksim_finogenov@mail.ru', password_hash='$2y$10$pLCvNUXmJv5Xqlc3PoCtqeJ85M2zQPDjAM5RL6nM9B.Lxgw8nNGIq')]  | 01.01.1970  |
| ['Dmitriy']                     | ['mariy35bondarenko@mail.ru', 'kaktotakandrei@yandex.ru'] | ['79518507855'] | ['398058 Липецк Липецк ул Леонтия Кривенкова д 15 69']                                     | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='kaktotakandrei@yandex.ru', password_hash='$2y$10$1eVQqrQwh6TOmn3zkWcWGOmrTkOQG1c3bPqf5SKTvckOkrCuxZdUi')]  | 05.10.2020  |
| ['Dmitry Dmitry']               | ['lev.tkachinsky@yandex.ru', 'oniev13@yandex.ru']         | ['79264376264'] | ['101000 Москва Москва']                                                                   | [Row(title='nbdoc.ru', link='https://nbdoc.ru/', login='oniev13@yandex.ru', password_hash='$2y$10$p5wcIyn0UjEJ5BJ5Rm7fhe..MxNHY8FZPKDmggfiwQt0bledvl5dW')]         | 01.01.1970  |
```