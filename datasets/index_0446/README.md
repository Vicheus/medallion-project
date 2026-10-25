# Parsetron results

## About row data

> - Code name: index_0446
> - File path: pleer_ru.csv
> - Total rows: 3685323

### Schema
```
root
 |-- last_name: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- middle_name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- city: string (nullable = true)
 |-- email: string (nullable = true)

```

### Data sample
```
| last_name   | first_name   | middle_name    |       phone | city                                     | email                        |
|:------------|:-------------|:---------------|------------:|:-----------------------------------------|:-----------------------------|
| Полякова    | Мария        | Александровна  | 79153323959 | Москва                                   | poliachka.08@gmail.com       |
| Навасардян  | Лилит        | Артуровна      | 79370750807 | Самара                                   | miglil93@mail.ru             |
| Алмаметова  | Дина         | Рафаэльвна     | 79811256999 | Санкт-Петербург                          | di.almametova@yandex.ru      |
| Сорокин     | Антон        | Андреевич      | 79263480283 | Москва                                   | Tonioni@yandex.ru            |
| Сальдюн     | Яна          | Евгеньевна     | 79137545278 | город Новосибирск                        | yana.saldyun@mail.ru         |
| Бондаренко  | Антонина     | Олеговна       | 79322485495 | Нефтеюганск                              | ant.olegowna@yandex.ru       |
| Кузнецова   | Анастасия    | Викторовна     | 79322485208 | Сургут                                   | nasten-ka1988@mail.ru        |
| Кулишкина   | Любовь       | Владимировна   | 79609061921 | Россия, Кемеровская область, Прокопьевск | kulishkina.lyubov@mail.ru    |
| Карпенко    | Алексей      | Андреевич      | 79261422116 | г.Хабаровск                              | kiseliov92@mail.ru           |
| Букшина     | Елена        | Михайловна     | 79161182714 | Москва                                   | 2509koska@mail.ru            |
| Ляхов       | Вадим        | Валерьевич     | 79134867818 | Новосибирск                              | vadim.lyakhov@mail.ru        |
| Бондаренко  | Ольга        | Николаевна     | 79286646856 | Краснодар                                | ms.helga.92@mail.ru          |
| Жаворонкова | Зиля         | Юлаевна        | 79135308538 | Норильск                                 | Zhavoronkov84@mail.ru        |
| Рыбакова    | Анастасия    | Вадимовна      | 79626841170 | Санкт-Петербург                          | severpalmira98@gmail.com     |
| Полянская   | Ирина        | Васильевна     | 79232827381 | Красноярск                               | polyanskaya-i@mail.ru        |
| Поповкина   | Наталья      | Владимировна   | 79197619152 | г. Серпухов                              | popovkina78@mail.ru          |
| Тамасян     | Диана        | Георгиевна     | 79041593335 | Иркутск                                  | didiana1994@mail.ru          |
| Джалалян    | Дарья        | Николаевна     | 79372411601 | Саратов                                  | svetochka.xaritonova95@bk.ru |
| Крапивина   | Лариса       | Александровна  | 79222185525 | Лесной                                   | 2ora@mail.ru                 |
| Зинченко    | Алина        | Константиновна | 79143400779 | Москвп                                   | a_96@inbox.ru                |
```


## About final data
> - Total rows: 2956236

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 80.17% |
| Emails | 92.60% |
| Address | 99.69% |



### Data sample
```
| names                                       | phones          | emails                              | address                                |
|:--------------------------------------------|:----------------|:------------------------------------|:---------------------------------------|
| ['Abdukarimova Sarvinoz Otkir Qizi']        |                 | ['safubi07@gmail.com']              | ['Чирчик']                             |
| ['Abdul Rahym Oguzhan Ogly']                |                 | ['bosshanov111@gmail.com']          | ['Бишкек']                             |
| ['Abdullaeva Aziza Murat Qizi']             |                 | ['malika.mp@mail.ru']               | ['Tashkent']                           |
| ['Abdullaeva Gulnoz Atanazarova']           |                 | ['sezan333777@gmail.com']           | ['Ташкент']                            |
| ['Abdumutalibov Shahzodbek Oybekovich']     |                 | ['shaxmusic2@gmail.com']            | ['Ташкент']                            |
| ['Abdusamadova Ziyoda Shuxratovna']         |                 | ['ziyodaabdusamatova441@gmail.com'] | ['Ташкент']                            |
| ['Abrorov Azimjon Azamjon Ogli']            |                 | ['azimabrorov0111@gmail.com']       | ['Ташкент']                            |
| ['Agazhanova Zhanna Altynbekovna']          |                 | ['zhanna_183@mail.ru']              | ['Алматы']                             |
| ['Ahmadjonov Jahongir Shokirjon']           |                 | ['blackice7150206@gmail.com']       | ['Ташкент']                            |
| ['Aitmukhanov Sultan Kairatbekivich']       |                 | ['sula007@mail.ru']                 | ['Алматы']                             |
| ['Akbarova Khidoyat Gapirjanovna']          |                 | ['sjeeiskeo@gmail.com']             | ['Ташкент']                            |
| ['Akelan Nina Pavlovna']                    | ['79990806534'] | ['ninok_260695@mail.ru']            | ['Комсомольск-на-Амуре Комсомольский'] |
| ['Aleksei Hucggth Urrtyvtuv']               | ['79379643751'] | ['alek.birukov@yandex.ru']          | ['Саратов']                            |
| ['Alevskaya Ekaterina Ekaterina Alevskaya'] | ['79537960350'] | ['windcet@gmail.com']               | ['Новосибирска']                       |
| ['Almorawi Khaled Moohmad']                 | ['79298846998'] | ['khms77@hotmail.com']              | ['Махачкала']                          |
| ['Amashukeli Tamta T']                      | ['73476340254'] | ['tutukebi@yahoo.com']              | ['New York']                           |
| ['Anda Muzikante Ata']                      |                 | ['amuzikante@inbox.lv']             | ['Latvija']                            |
| ['Ani Bukhaidze Ani']                       |                 | ['anouki97@mail.ru']                | ['Tbilisi']                            |
| ['Ankry Oksana Vladimirovna']               |                 | ['hebotareva1@mail.ru']             | ['Haifa']                              |
| ['Ardazishvili Eva Aleko']                  |                 | ['ardazishvili.ani@mail.ru']        | ['Tbilisi']                            |
```