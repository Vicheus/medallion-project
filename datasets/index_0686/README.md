# Parsetron results

## About row data

> - Code name: index_0686
> - File path: azbyka_ru_preprocessed.csv
> - Total rows: 32456

### Schema
```
root
 |-- username: string (nullable = true)
 |-- email: string (nullable = true)
 |-- name: string (nullable = true)

```

### Data sample
```
| username                              | email                                  | name              |
|:--------------------------------------|:---------------------------------------|:------------------|
| nata-yashnovainternet-ru              | nata.yashnova@internet.ru              | Яшнова Наталия    |
| svyashenniyregentyandex-ru            | svyashenniyregent@yandex.ru            | Яхве ибн Мухаммад |
| ayakimovich23gmail-com                | ayakimovich23@gmail.com                | Яухим             |
| jasturmilagmail-com                   | jasturmila@gmail.com                   | Ясин              |
| yveta64mail-ru                        | yveta64@mail.ru                        | Ярушина           |
| kalabinaiaroslavnagmail-com           | kalabinaiaroslavna@gmail.com           | Ярославна         |
| yaroslava-baeva05yandex-ru            | yaroslava.baeva05@yandex.ru            | Ярослава          |
| yyaroslavamail-ru                     | yyaroslava@mail.ru                     | Ярослава          |
| sladehomeyandex-ru                    | sladehome@yandex.ru                    | Ярослава          |
| yari-christogmail-com                 | yari.christo@gmail.com                 | Ярослава          |
| slavka03121989gmail-com               | slavka03121989@gmail.com               | Ярослава          |
| iaroslavagoryushinamail-ru            | iaroslavagoryushina@mail.ru            | Ярослава          |
| yaroslava_smirnova_03mail-ru          | yaroslava_smirnova_03@mail.ru          | Ярослава          |
| evdokimovichyaroslavbomba984gmail-com | evdokimovichyaroslavbomba984@gmail.com | Ярослав           |
| shurakov-yaroslavinbox-ru             | shurakov.yaroslav@inbox.ru             | Ярослав Шураков   |
| jaroslawstasyukyandex-ru              | jaroslawstasyuk@yandex.ru              | Ярослав Стасюк    |
| yaroslav-premudriybk-ru               | yaroslav.premudriy@bk.ru               | Ярослав Премудрый |
| yaroslav-kamenskygmail-com            | yaroslav.kamensky@gmail.com            | Ярослав Каменский |
| lovlyrita30gmail-com                  | lovlyrita30@gmail.com                  | Ярослав           |
| odobetskiy24gmail-com                 | odobetskiy24@gmail.com                 | Ярослав           |
```


## About final data
> - Total rows: 31361

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                  | emails                           | source_entity_id                                         |
|:-----------------------|:---------------------------------|:---------------------------------------------------------|
| ['Анна']               | ['vatutina.anna@gmail.com']      | 00d115cebc4ddcb63393feea93d7f3fb48b0ef7f99279b86d88fe6f1 |
| ['Сергей']             | ['razdolbajgipotenuzu@mail.ru']  | 042df536721c7f94bd6f9137f7b4fce7de0cd5ba9ab0ba7da4d3fe2e |
| ['Кирилл']             | ['k3451970@ya.ru']               | 08efbc5cc5114c724d0b4e9b337178f565a4a95be9d924b81ac518ab |
| ['Елена']              | ['e-myag@yandex.ru']             | 0ac7738d9b358767265a6fbe1b681339fb4e19743aa062c749686794 |
| ['Игорь']              | ['axion63@yandex.ru']            | 0c0b8fe7854b623d7b487af6239f511e882301b557770c12e86f1a0d |
| ['Ильч']               | ['sizonovila839@gmail.com']      | 0caabd3f6f0e1a65909d91146574affbace3890467e4755aca79fb57 |
| ['Юлия']               | ['yulja.rozzza@gmail.com']       | 0cf2da68f9f707af62e2bd4ef857a582156eacbd80cbf8875c9cf8c3 |
| ['Любовь']             | ['karpach.lyuba@mail.ru']        | 0f364dba9c79c86351ef41c07c6d75bbe404b544a4eec59bd041f8ef |
| ['Михаил']             | ['transbumm@yandex.ru']          | 10011372965ba492cc3920f68aaf017b5a05dee40e8becf94e0af852 |
| ['Марина']             | ['mari-wa@mail.ru']              | 1118adc4cb4b6e5062e877759dcb81765ca93ed5b02d9cfc9f0c5c14 |
| ['Надежда']            | ['fantatrice@mail.ru']           | 11c08505f7428ebedec57c209f917c0c8a3dbaf2b819176cb75d1011 |
| ['Татьяна']            | ['tanya0785@mail.ru']            | 1268a33dc6f10a66ac8f29abd82d4a6af6ad1dbcad87e1b3ddcb68ae |
| ['Мария']              | ['swet843@mail.ru']              | 12aa0d61783e0dceb6a038109071bd6751a335e0a118cf3073c4d09b |
| ['Любовь Арсентьевна'] | ['lubov.bozhevalnaya@yandex.ru'] | 148c57d69cd5772b0c2397d47b9bf4a4493e6b7e3c1df8f2bfc50af3 |
| ['Владимирский']       | ['dios@eclipso.de']              | 15521b9a9f9929f0181a40175759cb93079a9724e190dda75d466409 |
| ['Татьяна']            | ['kotikova-tatyana@rambler.ru']  | 162111251eed0193976a11d2f25e26d160f3e8f7c92d7cf960adfeab |
| ['Дария']              | ['d.veli4ko@ya.ru']              | 16eac4e275832b6da190ca0893fa7edc299d2b61e1c9e290e8bc15e1 |
| ['Анастасия']          | ['nastya585o585@gmail.com']      | 17e70c7c91eff0ae122efa802a8d53582f3d97d9f28429ac4a5fe2a8 |
| ['Павел']              | ['pavelperepelkin02@gmail.com']  | 19438683ec49c55a95c2c7797a8128e06dab962ee69a8833b98a0989 |
| ['Александр Кириенко'] | ['aleksandrkiriencko@yandex.ru'] | 1b7c9b4260a2234f2f20f63d73c5e6e9a849451ae6725207f64e2664 |
```