# Parsetron results

## About row data

> - Code name: index_0193
> - File path: /media/user/SAMSUNG/Databases/index_0193/raw/users_preprocessed.csv
> - Total rows: 12455

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
 |-- PERSONAL_GENDER: string (nullable = true)
 |-- PERSONAL_MOBILE: string (nullable = true)
 |-- PERSONAL_WWW: string (nullable = true)
 |-- PERSONAL_CITY: string (nullable = true)
 |-- WORK_DEPARTMENT: string (nullable = true)
 |-- WORK_POSITION: string (nullable = true)
 |-- PERSONAL_BIRTHDAY: date (nullable = true)
 |-- WORK_PHONE: string (nullable = true)

```

### Data sample
```
| LOGIN                | PASSWORD                                                                                                   | NAME                   | LAST_NAME   | SECOND_NAME   | EMAIL                           | PERSONAL_PHONE      | PERSONAL_GENDER   | PERSONAL_MOBILE                        | PERSONAL_WWW   | PERSONAL_CITY   | WORK_DEPARTMENT                           | WORK_POSITION                                                                                             | PERSONAL_BIRTHDAY   | WORK_PHONE      |
|:---------------------|:-----------------------------------------------------------------------------------------------------------|:-----------------------|:------------|:--------------|:--------------------------------|:--------------------|:------------------|:---------------------------------------|:---------------|:----------------|:------------------------------------------|:----------------------------------------------------------------------------------------------------------|:--------------------|:----------------|
| admin                | 6o&S]D2t009e9b9b36fd25402c34722357a3b76a                                                                   | Денис                  | Толстиков   |               | admin@yurkas.by1                |                     |                   |                                        |                |                 |                                           |                                                                                                           |                     |                 |
| anonymous_IvfVhrgDR  | fCltZhIJ4a44782408ae0c5ef977cd9c7f4a60c1                                                                   | Анонимный пользователь |             |               | anonymous_ivfvhrgdr@example.com |                     |                   |                                        |                |                 |                                           |                                                                                                           |                     |                 |
| bondarchik@yurkas.by | A{c88e/W73232596ba4032df007a5aa792bb1b75                                                                   | Владимир               | Бондарчик   | Анатольевич   | bondarchik@yurkas.by            |                     | M                 |                                        |                |                 | ИТ                                        | зам. директора по ИТ                                                                                      | 1976-03-25          | +375296695694   |
| akulich@yurkas.by    | $6$Ydgu2j6WFpXGhsvq$cr8TVL2dbh3BjGYFc0GPyJP8SljMrdNCAv5MlBvi2P0jD5D8hOruwq5mCVN3B50T9EhHbRyU3UhdYYVKnqdCl. | Николай                | Акулич      | Иванович      | akulich@yurkas.by               |                     | M                 | +375296390528                          |                | Минск           | Отдел разработки программного обеспечения | Начальник отдела разработки программного обеспечения                                                      | 1987-11-27          |                 |
| korovina@yurkas.by   | Dj6},gM7d4def8b6ccb2576cde7559b717b32f58                                                                   | Ольга                  | Коровина    | Сергеевна     | korovina@yurkas.by              |                     | F                 | +375296010752                          |                |                 | ИТ                                        | Специалист по сопровождению 1С                                                                            |                     |                 |
| grinko@yurkas.by     | F*3go4#Fd9992c5d7869c8bdb1c4a937d5a98d0a                                                                   | Виктор                 | Гринько     | Юрьевич       | grinko@yurkas.by                |                     | M                 | 375292641664                           |                | Минск           | Отдел информационных технологий           | Администратор системный                                                                                   | 1986-07-23          |                 |
| inbox123@geekhare.me | 6Gf\B}q6f7e88ede5e72210a5505854909352eb3                                                                   | Андрей                 | Заяц        | Юрьевич       | inbox123@geekhare.me            |                     | M                 | +375298440242                          |                | Минск           |                                           |                                                                                                           | 1991-01-22          |                 |
| director@yurkas.by   | $6$T2ECcny60L17IvsW$zyiDL6GE6ecGWvW0KPdXyV5UojwcnnEwaLMZHFIzeS0Bz9cEdstrpYnwqzZwFXCqFLj/juFqy4afVYtyEDDWV. | Дмитрий                | Юркевич     | Валерьевич    | director@yurkas.by              |                     | M                 |                                        |                | Минск           |                                           | "Учредитель Частного предприятия ""Юркас"""                                                               |                     |                 |
| zoya@yurkas.by       | $6$MHCvukSYH5QSYCO1$DF9bhLqzSItnx4fh3DIxSZ.urpi79ZYxOjWvLi8pNLww7zMRrGzgiHY2GEPrfn6zCqdSgugavuKyLwzsdMDAD/ | Зоя                    | Юркевич     | Владимировна  | zoya@yurkas.by                  |                     | F                 |                                        |                | Минск           |                                           | "Учредитель Частного предприятия ""Дверной Лидер""/ Руководитель проектов Частного предприятия ""Юркас""" |                     |                 |
| info@yurkas.by       | $6$Xegbm1WnSxr8YBY9$v8iQaJ/u1.BJUURbjzJr958aBD988XzKzPI3FhkXg0B1RncnmmP88MyJvGMmNytJEkfiNo.rmIpniquaKYH3J0 | Екатерина              | Жигало      | Игоревна      | info@yurkas.by                  |                     | F                 | +375296889951                          |                | Минск           | Администрация                             | Помощник руководителя                                                                                     | 1987-09-14          |                 |
| reception@yurkas.by  | H1~z:o4F1aac19aa3a6610642a4e5ce28713b2ec                                                                   | Ольга                  | Анкуда      |               | o.ankuda@yurkas.by              | +375175119950       | F                 |                                        |                |                 | Администрация                             | Офис-менеджер                                                                                             |                     | +375175119961   |
| svetogor@yurkas.by   | >y5RQ,5c26ab6fe04cde58192a094410ccce16f7                                                                   | Елена                  | Светогор    | Геннадиевна   | svetogor@yurkas.by              | +375 29 6706645     | F                 | Личный +375 29 6842693                 |                |                 | Бухгалтерия                               | Главный бухгалтер                                                                                         | 1972-06-16          | 8 017 511 99 55 |
| melnik@yurkas.by     | mL{5<w7X190c80b96a91414daae2b4767bf76611                                                                   | Екатерина              | Мельник     | Викторовна    | melnik@yurkas.by                |                     | F                 |                                        |                |                 | Бухгалтерия                               | Зам. гл. бухгалтера                                                                                       |                     | 375296706645    |
| zayceva.a@yurkas.by  | $6$0NMoURDq4J4iJPgQ$f6YLcbzUy8Fs0w1lN3h.IKjZNuaGZ1kFX1CIjrTyiFKm4sVd6NKRtnAWGeCqu9GNfXEJDWma75tVhDrn/FtOF1 | Анастасия              | Брокар      |               | zaitseva@yurkas.by              |                     | F                 |                                        |                |                 | Бухгалтерия                               | Бухгалтер по заработной плате                                                                             | 1985-11-02          |                 |
| yarovskaya@yurkas.by | $6$1fsP7A8wfUMwx1Do$XajEjz9qEuzwliCrEjPogyuoCuyIUSk1c50SdnbJNdrzyJP34cFG1kFKDZRtR4Lh48s.bIs8TQBlYGEMZjlLx1 | Марина                 | Яровская    | Вячеславовна  | yarovskaya@yurkas.by            |                     | F                 | 375292189976( личный)                  |                |                 | Финансово-экономический отдел             | Бухгалтер по финансам и кредиту                                                                           | 1983-08-03          | 375296706645    |
| ep@yurkas.by         | $6$O5NRj7G3t5ybSt46$D4iGruIdC0HUF9jUA7LuDGeUmCPLFGKG1hkdQSVOQezbtnTwm5TIQGzJfU75d0chRfnFJoW9GmsNxt6drXIYm0 | Елена                  | Павлушкина  | Павловна      | Pavlushkina@yurkas.by           | личный 375296219717 | F                 |                                        |                |                 | Бухгалтерия                               | Бухгалтер                                                                                                 | 2020-08-20          | 80175119955     |
| nat_ign@yurkas.by    | $6$GTYNhoUKlK0iHLUr$JQknoXxSJayzBOU9uGzcBzIyS29pIL1ViZVMR8NrCf1m0xgSSUBl8kk04ALlJqdWBRkHK3QkkfCN2E1Gy09Bd/ | Наталья                | Игнашевич   |               | nat_ign@yurkas.by               |                     | F                 | +375291974100 (личный)                 |                |                 | Бухгалтерия                               | Бухгалтер по ВЭД                                                                                          | 1974-06-20          | +37517511-99-50 |
| danilevich@yurkas.by | lQ,23m_If5919897346f753574d8f252d280b749                                                                   | Татьяна                | Данилевич   | Михайловна    | danilevich@yurkas.by            |                     |                   |                                        |                |                 | Отдел по поставкам и логистике            | Вед. специалист по поставкам и логистике                                                                  |                     | 375296109942    |
| puhova@yurkas.by     | $6$fM3TP3v6pl73G96A$sl0iVEV7prDqlR7CaJehhYQcXXuWX1T7FQb2ePsFTfgrh.C09uFWYtsKeHYLakw5ckHaiDH5k9Qe8WXzmMWS90 | Ольга                  | Пухова      | Юрьевна       | puhova@yurkas.by                |                     | F                 | +375296559441, +375295559441 (личные)  |                |                 | Отдел по поставкам и логистике            | Начальник отдела поставок                                                                                 | 1986-09-10          |                 |
| logist@yurkas.by     | $6$JLb2eHorWUr2X9E2$EisHRI15928lfL4m/Mg3fIu1bai3MXifNCdbG.z3p5/Hb4FrsWuTmk/ODa49dFOdNDbrr7pv19DvHzu.VJGqa0 | Екатерина              | Гуринович   | Валерьевна    | logist@yurkas.by                |                     | F                 | +375291249867 личный - НЕ РАЗДАВАТЬ!!! |                |                 | Отдел транспортной логистики              | Начальник транспортной логистики                                                                          | 1989-11-05          | +375296796545   |
```


## About final data
> - Total rows: 2649

### Schema
```
root
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
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
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```

### Data sample
```
| emails   | phones           | names                    | works   | accounts                                                                                                                                    | socials   |
|:---------|:-----------------|:-------------------------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------|:----------|
|          | ['375255012100'] | ['Сергей']               |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_9784q1aee', password_hash='uOEs7QB4aa3154369e4aae452d6312794100327e')] |           |
|          | ['375255022858'] | ['Наталья']              |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_8277Nczeu', password_hash='ZPQ5gbYi8538af24fbfa197c9b27065a2b696715')] |           |
|          | ['375255079966'] | ['Сергей']               |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_6491ONMZQ', password_hash='0TqzDSI19971516bc7251629fbd2c77cc3beac77')] |           |
|          | ['375255247790'] | ['Александр']            |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_7153ghj0K', password_hash='gff6xMkRf387836f020f8ce1d0c5814699f344e1')] |           |
|          | ['375255251012'] | ['Андрей']               |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_9302EKDIN', password_hash='V86ckkmUdcccc8120e5e11ad4b3c997cb9023195')] |           |
|          | ['375255317891'] | ['Мария']                |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_7423YAEFE', password_hash='1Rb0dd4be095050c9829cd7e8d93f73a9427a6f9')] |           |
|          | ['375256522295'] | ['Сергей']               |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_3334d4CyH', password_hash='MQyDtsc4952e550a0c340d9431baa4d16e31fb01')] |           |
|          | ['375257034942'] | ['Игорь']                |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_2687YrED4', password_hash='ymKbnPh182e460e884fce495dadb5834ccdeccb8')] |           |
|          | ['375257227093'] | ['Наталья']              |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_3008EsQwN', password_hash='6JlVDQowb94ebd257d6077a3ae60e2fa673a38ab')] |           |
|          | ['375257608101'] | ['Полина']               |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_1067jslZE', password_hash='EScIU8MS52e16462ca5db46b4c504b4a30739bfd')]     |           |
|          | ['375257761263'] | ['Сидор А.В. Г.Лида Ип'] |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_2216GfMIp', password_hash='NL00BMS4e392412ab9d3527a42094e5b140597b0')] |           |
|          | ['375259231130'] | ['Андрей']               |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_7365PUQZh', password_hash='2dqG89BB00c9702e8c74fc22011ee306271d7b61')] |           |
|          | ['375259256378'] | ['Татьяна']              |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_4568W3jTS', password_hash='qr9kKNTy459cceacdc89e48bf90ac50c11960654')] |           |
|          | ['375259445215'] | ['Юлия']                 |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_2851Zv0rF', password_hash='E1fG4Eqxcf91211d05fcb21826f825c451e61a56')] |           |
|          | ['375259560006'] | ['Татьяна']              |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_5061BkjKG', password_hash='hTOpyfdacd2feae72794aef3cae655431bb27a9f')] |           |
|          | ['375259666455'] | ['Марина']               |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_4299UzXeA', password_hash='2TWc7PSM895c8a541b63014cf5035f32327761f9')] |           |
|          | ['375291013557'] | ['Евгения']              |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_6213Hp7i6', password_hash='2dCE5Mvpb0ac13df57dcd1a73128eb62573adbb3')] |           |
|          | ['375291028351'] | ['Андрей']               |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_7375LMSd0', password_hash='X8LhjhJw51f1ade4ccb7c2491f4299a9c82a2521')] |           |
|          | ['375291046564'] | ['Татьяна']              |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_1308WbwWB', password_hash='Ox0eZfmA65f7228ff5d59bf4bbfadcfd4f3b982b')]     |           |
|          | ['375291070101'] | ['Алескандр']            |         | [Row(title='Юркас', link='https://yurkas.by', login='imopenlines_wgt_4417ZTyRO', password_hash='oGaxq1b48e2480aef1a854f2ae7792e6f51b6450')] |           |
```