# Parsetron results

## About row data

> - Code name: index_0118
> - File path: /media/user/TRANSCEND/Databases/index_0118/raw/spasskie_vorota_preprocessed.csv
> - Total rows: 152553

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- email: string (nullable = true)
 |-- name: string (nullable = true)
 |-- password_hash: string (nullable = true)
 |-- phone1: long (nullable = true)
 |-- phone2: long (nullable = true)

```

### Data sample
```
|   id | email              | name                        | password_hash                    |        phone1 |   phone2 |
|-----:|:-------------------|:----------------------------|:---------------------------------|--------------:|---------:|
|    5 | riv2@ads-soft.ru   | Русаков Игорь               | c8021797a2a6113e4b5434cd13f28fd6 | nan           |      nan |
|    6 | dp_master@i.ua     | wewe ewwe                   | 9b9e1476fa5a06d80721e6e5b5e84301 | nan           |      nan |
|    7 | gda1@ads-soft.ru   | Адс Дмитрий Александрович   | 25d55ad283aa400af464c76d713c07ad | nan           |      nan |
|    9 | riv@ads-soft.ru    | Русаков Riv@ads-soft.ru     | 25d55ad283aa400af464c76d713c07ad | nan           |      nan |
|   10 | goo@adssoft.ru     | Иванов Петр Викторович      | 7c75229488e284a74aed1eeadcb67f72 | nan           |      nan |
|   11 | asd@asd.com        | Иванников Иван Васильевич   | e82b6d117619364bd5a544df7b718cc1 | nan           |      nan |
|   12 | avtlon@mail.ru     | Талдин Алексей Владимирович | 206badcd9de4781bcbb387b952c23550 |   7.9163e+10  |      nan |
|   13 | mishin@mrggroup.ru | Иванов Иван Иванович        | ff78b1ac3dfa79e5a0c39d15073c520b |   7.91652e+10 |      nan |
|   14 | kaskometr          | Каскометр                   | e71ce1a1c00427ab95afa20c53090170 | nan           |      nan |
|   15 | gda@ads-soft.ru    | Адс Дмитрий                 | 25d55ad283aa400af464c76d713c07ad | nan           |      nan |
```


## About final data
> - Total rows: 92417

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
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```

### Data sample
```
| names                           | emails                 | phones          | accounts                                                                                                                                                            |
|:--------------------------------|:-----------------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Русаков Игорь']               | ['riv2@ads-soft.ru']   |                 | [Row(title='Страховая компания "Спасские ворота"', link='https://spasskievorota.ru', login='riv2@ads-soft.ru', password_hash='c8021797a2a6113e4b5434cd13f28fd6')]   |
| ['Wewe Ewwe']                   | ['dp_master@i.ua']     |                 | [Row(title='Страховая компания "Спасские ворота"', link='https://spasskievorota.ru', login='dp_master@i.ua', password_hash='9b9e1476fa5a06d80721e6e5b5e84301')]     |
| ['Адс Дмитрий Александрович']   | ['gda1@ads-soft.ru']   |                 | [Row(title='Страховая компания "Спасские ворота"', link='https://spasskievorota.ru', login='gda1@ads-soft.ru', password_hash='25d55ad283aa400af464c76d713c07ad')]   |
| ['Русаков Rivads-Soft.Ru']      | ['riv@ads-soft.ru']    |                 | [Row(title='Страховая компания "Спасские ворота"', link='https://spasskievorota.ru', login='riv@ads-soft.ru', password_hash='25d55ad283aa400af464c76d713c07ad')]    |
| ['Иванов Петр Викторович']      | ['goo@adssoft.ru']     |                 | [Row(title='Страховая компания "Спасские ворота"', link='https://spasskievorota.ru', login='goo@adssoft.ru', password_hash='7c75229488e284a74aed1eeadcb67f72')]     |
| ['Иванников Иван Васильевич']   | ['asd@asd.com']        |                 | [Row(title='Страховая компания "Спасские ворота"', link='https://spasskievorota.ru', login='asd@asd.com', password_hash='e82b6d117619364bd5a544df7b718cc1')]        |
| ['Талдин Алексей Владимирович'] | ['avtlon@mail.ru']     | ['79163034457'] | [Row(title='Страховая компания "Спасские ворота"', link='https://spasskievorota.ru', login='avtlon@mail.ru', password_hash='206badcd9de4781bcbb387b952c23550')]     |
| ['Иванов Иван Иванович']        | ['mishin@mrggroup.ru'] | ['79165200134'] | [Row(title='Страховая компания "Спасские ворота"', link='https://spasskievorota.ru', login='mishin@mrggroup.ru', password_hash='ff78b1ac3dfa79e5a0c39d15073c520b')] |
| ['Адс Дмитрий']                 | ['gda@ads-soft.ru']    |                 | [Row(title='Страховая компания "Спасские ворота"', link='https://spasskievorota.ru', login='gda@ads-soft.ru', password_hash='25d55ad283aa400af464c76d713c07ad')]    |
| ['Иванов Иван Иванович']        | ['gda2@ads-soft.ru']   |                 | [Row(title='Страховая компания "Спасские ворота"', link='https://spasskievorota.ru', login='gda2@ads-soft.ru', password_hash='346f71e3111c2dea79591669a45be281')]   |
```