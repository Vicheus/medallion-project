# Parsetron results

## About row data

> - Code name: index_0207
> - File path: kvartelia.ru.csv
> - Total rows: 10555241

### Schema
```
root
 |-- phone: string (nullable = true)
 |-- name: string (nullable = true)
 |-- city: string (nullable = true)
 |-- address: string (nullable = true)
 |-- profile_url: string (nullable = true)
 |-- photo_url: string (nullable = true)
 |-- ad_title: string (nullable = true)

```

### Data sample
```
|       phone | name       | city                              | address                                                  | profile_url                 | photo_url                                          | ad_title                     |
|------------:|:-----------|:----------------------------------|:---------------------------------------------------------|:----------------------------|:---------------------------------------------------|:-----------------------------|
| 79128408609 | юлия       | октябрьское, оренбургская область |                                                          | https://kvartelia.ru/user1  |                                                    |                              |
| 79803248662 | олег       | бирюч, белгородская область       |                                                          | https://kvartelia.ru/user2  |                                                    |                              |
| 79803248662 | олег       | бирюч, белгородская область       | бирюч; улица верхняя 5 (мкр. "северный")                 | https://kvartelia.ru/user2  | https://cdn.kvartelia.ru/small/002566/25662101.jpg | земля поселений(ижс) 15 сот. |
| 79528912151 | анатолий   | первомайское, томская область     |                                                          | https://kvartelia.ru/user3  |                                                    |                              |
| 79852589933 | илья       | вуктыл, коми                      |                                                          | https://kvartelia.ru/user4  |                                                    |                              |
| 79523847696 | ирина      | войсковицы, ленинградская область |                                                          | https://kvartelia.ru/user5  |                                                    |                              |
| 79264692066 | вера       | киевский, московская область      |                                                          | https://kvartelia.ru/user6  |                                                    |                              |
| 79106523752 | николаевна | сосновка, тамбовская область      |                                                          | https://kvartelia.ru/user7  |                                                    |                              |
| 79102072999 | хозяин     | покровское, орловская область     |                                                          | https://kvartelia.ru/user8  |                                                    |                              |
| 79045421578 | алексей    | троицкий, свердловская область    |                                                          | https://kvartelia.ru/user9  |                                                    |                              |
| 79613909084 | сергеевич  | глотовка, ульяновская область     |                                                          | https://kvartelia.ru/user10 |                                                    |                              |
| 79613909084 | сергеевич  | глотовка, ульяновская область     | жигулевск; ставропольский р-н; снт мичуринец             | https://kvartelia.ru/user10 | https://kvartelia.ru/images/no-photos.png          | дача 20 м² 7 сот.            |
| 79040780790 | юрий       | саргатское, омская область        |                                                          | https://kvartelia.ru/user11 |                                                    |                              |
| 79143657743 | ольга      | карымское, забайкальский край     |                                                          | https://kvartelia.ru/user12 |                                                    |                              |
| 79026075534 | рамиль     | пласт, челябинская область        |                                                          | https://kvartelia.ru/user13 |                                                    |                              |
| 79125958212 | стариков   | куеда, пермский край              |                                                          | https://kvartelia.ru/user14 |                                                    |                              |
| 79125958212 | стариков   | куеда, пермский край              | куеда; куединский р-н; пос. куеда; ул. м.с. ехлакова; 1в | https://kvartelia.ru/user14 | https://kvartelia.ru/images/no-photos.png          | земля поселений(ижс)         |
| 79522727331 | александр  | коробицыно, ленинградская область |                                                          | https://kvartelia.ru/user15 |                                                    |                              |
| 79522727331 | александр  | коробицыно, ленинградская область | санкт-петербург;                                         | https://kvartelia.ru/user15 | https://cdn.kvartelia.ru/small/002883/28838729.jpg | квартира в новостройке       |
| 79522727331 | александр  | коробицыно, ленинградская область | санкт-петербург;                                         | https://kvartelia.ru/user15 | https://cdn.kvartelia.ru/small/002630/26308981.jpg | квартира в новостройке       |
```


## About final data
> - Total rows: 4431427

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 99.99% |
| Address | 71.18% |
| Accounts | 100.00% |



### Data sample
```
| names            | phones          | address                                                                          | accounts                                                             |
|:-----------------|:----------------|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------|
| ['.Юрий']        | ['79803619188'] |                                                                                  | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user275276')]  |
| ['Abdul']        | ['79034812787'] | ['Избербаш Ул. Калинина 25']                                                     | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user3124803')] |
| ['Abdulkerimov'] | ['79520188433'] | ['Арсеньево Рабочий Посёлок Арсеньево']                                          | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user2827422')] |
| ['Abubakr']      | ['79288033308'] | ['Чонтаул Село Чонтаул']                                                         | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user2672040')] |
| ['Achi']         | ['79280761817'] |                                                                                  | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user1083876')] |
| ['Adlan']        | ['79238000404'] |                                                                                  | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user1070225')] |
| ['Aigyl']        | ['79872710653'] |                                                                                  | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user1772697')] |
| ['Aisenova']     | ['79109808864'] | ['Лежнево Лежневский Р-Н Пос. Городского Типа Лежнево 2-Я Ул. Луначарского 15']  | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user4430254')] |
| ['Akfdhj']       | ['79610558629'] | ['Солянка Село Солянка Вилюйская Улица']                                         | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user2674911')] |
| ['Akimova']      | ['79649425572'] | ['Сочи Микрорайон Центральный']                                                  | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user4482531')] |
| ['Aksenova']     | ['79606290919'] | ['Дубовое Белгородский Р-Н Пос. Дубовое Микрорайон Северный Пригородная Ул. 13'] | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user3133154')] |
| ['Albina']       | ['79644598832'] |                                                                                  | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user494788')]  |
| ['Aleei']        | ['79050007087'] |                                                                                  | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user1255831')] |
| ['Alek']         | ['79788033508'] | ['Ялта Ул Тимирязева']                                                           | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user3133420')] |
| ['Alekc']        | ['79537714679'] |                                                                                  | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user1167884')] |
| ['Aleks']        | ['79189960751'] | ['Мингрельская Станица Мингрельская']                                            | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user2835239')] |
| ['Aleks']        | ['79632844557'] | ['Черкесск Улица Доватора 78']                                                   | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user1764868')] |
| ['Aleks']        | ['79834003348'] | ['Ангарск Ангарское Городское Муниципальное Образование 17-Й Микрорайон']        | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user4187145')] |
| ['Aleks']        | ['79969358270'] | ['Улан-Удэ Снт Монолит Улица Четвёртая 7']                                       | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user1764696')] |
| ['Aleksandr']    | ['79171630479'] |                                                                                  | [Row(title='Kvartelia.ru', link='https://kvartelia.ru/user144202')]  |
```