# Parsetron results

## About row data

> - File path: fierashop_ru_03_06_2026.csv
> - Total rows: 46728

### Schema
```
root
 |-- name: string (nullable = true)
 |-- surname: string (nullable = true)
 |-- patronymic: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone_number: string (nullable = true)
 |-- city: string (nullable = true)

```

### Data sample
```
| name                            | surname    | patronymic   | email                    |   phone_number | city   |
|:--------------------------------|:-----------|:-------------|:-------------------------|---------------:|:-------|
| Ящинская Елена Николаевна       |            |              | yasleno4ka@yandex.ru     |    79374030637 |        |
| ященко Галина Яковлевна         |            |              | g.yashchenko@mail.ru     |    79044844572 |        |
| Яштаков                         | Руслан     | Фёдорович    | yashtakov.ruslan@mail.ru |    79179179064 | Казань |
| Яшнар                           | Бекязов    |              | hk.spr@ya.ru             |    79636559989 | Москва |
| Яшкин Сергей                    |            |              | srvlion@yandex.ru        |    79122084996 |        |
| Яшина Нина Владимировна         |            |              | melon81@mail.ru          |    79163919512 |        |
| Яшин Сергей Владимирович        |            |              | Brillianta-sveta@mail.ru |    79851735537 |        |
| Яшин Валерий Васильевич         |            |              | ivasenkoelena@mail.ru    |    79221040709 |        |
| Яшин Артём                      |            |              | angener@rambler.ru       |    79520434494 |        |
| Яшагин                          | Константин |              | yashagin@gmail.com       |    79221679004 |        |
| Яцын Анатолий                   |            |              | ttwtflal@gmail.com       |    79313213200 |        |
| Яценко Алина                    |            |              | sa@arabella.ru           |    79150634088 |        |
| Яхшибекова Алина Феликсовна     |            |              | alina230878alina@mail.ru |    79963269966 |        |
| Яханов И.В.                     |            |              | airportufa@mail.ru       |    79174212995 |        |
| Яушев Дмитрий                   |            |              | dima591@yandex.ru        |    79264165299 |        |
| Ятманова Наталья Александровна  |            |              | Ntasha1977@mail.ru       |    79877268814 |        |
| Ятманова Елена                  |            |              | Super-gaz@yandex.ru      |    79055038212 |        |
| яськова                         | Алла       |              | Allavinograd1@gmail.com  |    79152656685 |        |
| ЯСЫРЕВ МАКСИМ АЛЕКСАНДРОВИЧ     |            |              | Yamax1974@mail.ru        |    79028017489 |        |
| Ястремская Екатерина Евгеньевна |            |              | Yakat78@mail.ru          |    79104291193 |        |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 93.08% |
| Emails | 99.96% |
| Address | 68.05% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                                    | phones          | emails                    | address            | source_entity_id                                         |
|:-----------------------------------------|:----------------|:--------------------------|:-------------------|:---------------------------------------------------------|
| ['Лазарев Юра Вадимович']                | ['79259128285'] | ['lazarev-opt@mail.ru']   | ['Наро-Фоминск']   | 008cf57e7ee6185f5c947700b999142347747baa16866fed6b6975f6 |
| ['Оксана Николаевна Загороднова']        | ['79276580548'] | ['zagora.63@mail.ru']     |                    | 013cb42fe1cadb1b950ab315d2cb879ad47afff68c4520c935fa7f1e |
| ['Батов Александр Юрьевич']              | ['79166142554'] | ['aleksandr_13@mail.ru']  | ['Москва']         | 01ee997f4cbf53f55b364ec334cc8ee6469b7fe0071cb92bc0a04e05 |
| ['Кормакова Юлия Борисовна']             | ['79853816908'] | ['selpo.kuhni@bk.ru']     | ['Щёлково МО']     | 020a87e273e06f6e54b7694d10f7f1fc2881b638a4138f59b5d8297a |
| ['Шестаков Артём Сергеевич']             | ['79226642332'] | ['g-shot2808@mail.ru']    |                    | 0244b69fb3e0aca5ed60e5df113415bcacd924cd169b60a2c58f5c71 |
| ['Гриненко Александр']                   | ['79536251121'] | ['a_grinenko@list.ru']    | ['Москва']         | 04b42a4700c4610f432c058d107a36ec85dd214ec902988178ed1098 |
| ['Патрин Евгений']                       | ['79243700962'] | ['1evgeniy.p972@mail.ru'] | ['Москва']         | 058df416be4d7517eb21f8f46940edbcc405a24a4ecde8b46963a2e2 |
| ['Черникова Светлана Юрьевна']           | ['79160698363'] | ['hoff987@yandex.ru']     |                    | 05c25fedd9eeb823a8c7d67a94151fce2aa19dffc01203c53d3b46d0 |
| ['Крашенникова Маргарита Александровна'] | ['79035617770'] | ['margosha_k@mail.ru']    |                    | 060afafb21e77eaaffc92725461270a5b53aa5de6175aa04bd75b0c4 |
| ['Отрощенкова Юлия']                     |                 | ['julija-otr84@mail.ru']  |                    | 0620690880fba27986bd0ae26d3525531aa25d2f5b7477c5a95f61d5 |
| ['Кадыров Влад']                         | ['79272361902'] | ['s500600@yandex.ru']     | ['Уфа']            | 079ab39ec450b6311b5b88f03646d32e4d51fb57aed62dc608a037c5 |
| ['Роман']                                | ['79581982830'] | ['7712550@gmail.com']     | ['Москва']         | 099e63414950f0c51d0ef350c7e1dd7076ea6d5f9b89ae942898dbc7 |
| ['Сенаторова Ирина']                     | ['79273613253'] | ['skrinia@yandex.ru']     | ['Пенза']          | 0b0cfc8e555cc7532162829e8b5b7acc406691f688fd6f608948f04d |
| ['Лучникова Елена']                      | ['79120612613'] | ['lev.dsg@gmail.com']     | ['Пермь']          | 0bcc029c6c05c30f69a8b516e82cba6d302fc73355fabc25aa74922a |
| ['Шкуропатова Анна']                     | ['79889484144'] | ['kshkuropatov@mail.ru']  | ['Ростов-на-Дону'] | 0c5ec77c58f032e2b5667b46fb1171d16aa432516170ebc5676d0f79 |
| ['Марсунов Сергей Владимирович']         | ['79149697173'] | ['mars@mail.ru']          |                    | 0de78f04afef5ba6a27fce632d3ed089b540943b8286a77145967f89 |
| ['Пикалов Дмитрий Сергеевич']            | ['79279083518'] | ['pikalov-1987@mail.ru']  |                    | 0f362daee0d98b4cc789058b598252b0ce3d3028b983e2301695fafc |
| ['Кузьминых Степан']                     | ['79821321632'] | ['steffan0720@gmail.com'] | ['Тюмень']         | 0fc5a2903c34d11824e94795fde2efb34c59f85be68324e1fe9c3429 |
| ['Разливин Денис Андреевичь']            | ['79292122249'] | ['a037he66rus@yandex.ru'] | ['Асбест']         | 1029e53c22f73225d484c9a1140d60a5a7946a6bd3647700b20db273 |
| ['Ермаков Геннадий']                     | ['79093344916'] | ['gena0111@mail.ru']      | ['Саратов']        | 1121050aa5f4447e28286f717779a368ebd030c727e03ea9a85a8591 |
```