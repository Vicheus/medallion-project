# Parsetron results

## About row data

> - File path: data.csv
> - Total rows: 491

### Schema
```
root
 |-- _id: string (nullable = true)
 |-- _index: string (nullable = true)
 |-- _score: string (nullable = true)
 |-- address: string (nullable = true)
 |-- address.keyword: string (nullable = true)
 |-- db_name_pretty: string (nullable = true)
 |-- db_name_pretty.keyword: string (nullable = true)
 |-- full_name: string (nullable = true)
 |-- full_name.keyword: string (nullable = true)
 |-- id: string (nullable = true)
 |-- metadata.birth_date: string (nullable = true)
 |-- metadata.myrotvorets_url: string (nullable = true)
 |-- metadata.myrotvorets_url.keyword: string (nullable = true)
 |-- source: string (nullable = true)
 |-- source.keyword: string (nullable = true)

```

### Data sample
```
| _id                    | _index           |   _score | address   | address.keyword   | db_name_pretty   | db_name_pretty.keyword   | full_name                            | full_name.keyword                    | id          | metadata.birth_date         | metadata.myrotvorets_url                                                 | metadata.myrotvorets_url.keyword                                         | source   | source.keyword   |
|:-----------------------|:-----------------|---------:|:----------|:------------------|:-----------------|:-------------------------|:-------------------------------------|:-------------------------------------|:------------|:----------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------|:---------|:-----------------|
| external__v1_204516390 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Василевский Вадим Климентьевич       | Василевский Вадим Климентьевич       | 204,516,390 | Mar 20, 1974 @ 02:00:00.000 | Беларусь"                                                                | Беларусь"                                                                | vagner   | vagner           |
| external__v1_204516389 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Подковальников Сергей Владимирович   | Подковальников Сергей Владимирович   | 204,516,389 | Sep 27, 1969 @ 02:00:00.000 | https://myrotvorets.center/criminal/podkovalnikov-sergej-vladimirovich/  | https://myrotvorets.center/criminal/podkovalnikov-sergej-vladimirovich/  | vagner   | vagner           |
| external__v1_204516356 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Рябихин Сергей Валентинович          | Рябихин Сергей Валентинович          | 204,516,356 | Mar 5, 1969 @ 02:00:00.000  | https://myrotvorets.center/criminal/ryabikhin-sergej-valentinovich/      | https://myrotvorets.center/criminal/ryabikhin-sergej-valentinovich/      | vagner   | vagner           |
| external__v1_204516344 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Каразий Анатолий Александрович       | Каразий Анатолий Александрович       | 204,516,344 | Feb 21, 1969 @ 02:00:00.000 | https://myrotvorets.center/criminal/karazij-anatolij-aleksandrovich/     | https://myrotvorets.center/criminal/karazij-anatolij-aleksandrovich/     | vagner   | vagner           |
| external__v1_204516332 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Масленсков Анатолий Александрович    | Масленсков Анатолий Александрович    | 204,516,332 | Jul 29, 1968 @ 02:00:00.000 | https://myrotvorets.center/criminal/maslenskov-anatolij-aleksandrovich/  | https://myrotvorets.center/criminal/maslenskov-anatolij-aleksandrovich/  | vagner   | vagner           |
| external__v1_204516331 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Аникин Андрей Владимирович           | Аникин Андрей Владимирович           | 204,516,331 | Jan 12, 1968 @ 02:00:00.000 | https://myrotvorets.center/criminal/anikin-andrej-vladimirovich/         | https://myrotvorets.center/criminal/anikin-andrej-vladimirovich/         | vagner   | vagner           |
| external__v1_204516320 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Гусев Геннадий Иванович              | Гусев Геннадий Иванович              | 204,516,320 | Jan 9, 1968 @ 02:00:00.000  | https://myrotvorets.center/criminal/gusev-gennadij-ivanovich/            | https://myrotvorets.center/criminal/gusev-gennadij-ivanovich/            | vagner   | vagner           |
| external__v1_204516319 | osintflow-vagner |        1 | Украина   | Украина           | Военнослужащие   | Военнослужащие           | Бабка Сергей Евгеньевич              | Бабка Сергей Евгеньевич              | 204,516,319 | Dec 7, 1967 @ 02:00:00.000  | https://myrotvorets.center/criminal/babka-sergej-evgenevich/             | https://myrotvorets.center/criminal/babka-sergej-evgenevich/             | vagner   | vagner           |
| external__v1_204516307 | osintflow-vagner |        1 | Беларусь  | Беларусь          | Военнослужащие   | Военнослужащие           | Василевский Вадим Александрович      | Василевский Вадим Александрович      | 204,516,307 | Aug 26, 1980 @ 03:00:00.000 | https://myrotvorets.center/criminal/vasilevskij-vadim-aleksandrovich/    | https://myrotvorets.center/criminal/vasilevskij-vadim-aleksandrovich/    | vagner   | vagner           |
| external__v1_204516306 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Бурлаков Владимир Владимирович       | Бурлаков Владимир Владимирович       | 204,516,306 | Sep 4, 1984 @ 03:00:00.000  | https://myrotvorets.center/criminal/burlakov-vladimir-vladimirovich/     | https://myrotvorets.center/criminal/burlakov-vladimir-vladimirovich/     | vagner   | vagner           |
| external__v1_204516295 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Мартынов Сергей Геннадьевич          | Мартынов Сергей Геннадьевич          | 204,516,295 | Dec 11, 1966 @ 02:00:00.000 | https://myrotvorets.center/criminal/martynov-sergej-gennadevich/         | https://myrotvorets.center/criminal/martynov-sergej-gennadevich/         | vagner   | vagner           |
| external__v1_204516283 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Зорин Анатолий Александрович         | Зорин Анатолий Александрович         | 204,516,283 | Nov 25, 1966 @ 02:00:00.000 | https://myrotvorets.center/criminal/zorin-anatolij-aleksandrovich/       | https://myrotvorets.center/criminal/zorin-anatolij-aleksandrovich/       | vagner   | vagner           |
| external__v1_204516271 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Балмагамбетов Сансызбай Каиргалеевич | Балмагамбетов Сансызбай Каиргалеевич | 204,516,271 | Feb 6, 1973 @ 02:00:00.000  | https://myrotvorets.center/criminal/balmagambetov-sansyzbaj-kairgaleevi/ | https://myrotvorets.center/criminal/balmagambetov-sansyzbaj-kairgaleevi/ | vagner   | vagner           |
| external__v1_204516248 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Казгунов Евгений Викторович          | Казгунов Евгений Викторович          | 204,516,248 | Feb 4, 1966 @ 02:00:00.000  | https://myrotvorets.center/criminal/kazgunov-evgenij-viktorovich/        | https://myrotvorets.center/criminal/kazgunov-evgenij-viktorovich/        | vagner   | vagner           |
| external__v1_204516236 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Чупов Сергей Владимирович            | Чупов Сергей Владимирович            | 204,516,236 | Jan 6, 1965 @ 02:00:00.000  | https://myrotvorets.center/criminal/chupov-sergej-vladimirovich/         | https://myrotvorets.center/criminal/chupov-sergej-vladimirovich/         | vagner   | vagner           |
| external__v1_204516235 | osintflow-vagner |        1 | Украина   | Украина           | Военнослужащие   | Военнослужащие           | Мосиенко Юрий Викторович             | Мосиенко Юрий Викторович             | 204,516,235 | Oct 14, 1964 @ 02:00:00.000 | https://myrotvorets.center/criminal/mosienko-yurij-viktorovich/          | https://myrotvorets.center/criminal/mosienko-yurij-viktorovich/          | vagner   | vagner           |
| external__v1_204516224 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Макаров Сергей Андреевич             | Макаров Сергей Андреевич             | 204,516,224 | Mar 12, 1964 @ 02:00:00.000 | https://myrotvorets.center/criminal/makarov-sergej-andreevich-2/         | https://myrotvorets.center/criminal/makarov-sergej-andreevich-2/         | vagner   | vagner           |
| external__v1_204516213 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Иваськов Сергей Иванович             | Иваськов Сергей Иванович             | 204,516,213 | Sep 29, 1963 @ 02:00:00.000 | https://myrotvorets.center/criminal/ivaskov-sergej-ivanovich/            | https://myrotvorets.center/criminal/ivaskov-sergej-ivanovich/            | vagner   | vagner           |
| external__v1_204516190 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Шахов Виктор Михайлович              | Шахов Виктор Михайлович              | 204,516,190 | Nov 23, 1962 @ 02:00:00.000 | https://myrotvorets.center/criminal/shakhov-viktor-mikhajlovich/         | https://myrotvorets.center/criminal/shakhov-viktor-mikhajlovich/         | vagner   | vagner           |
| external__v1_204516189 | osintflow-vagner |        1 | Россия    | Россия            | Военнослужащие   | Военнослужащие           | Ащеулов Алексей Анатольевич          | Ащеулов Алексей Анатольевич          | 204,516,189 | Jun 27, 1972 @ 02:00:00.000 | https://myrotvorets.center/criminal/ashheulov-aleksej-anatolevich/       | https://myrotvorets.center/criminal/ashheulov-aleksej-anatolevich/       | vagner   | vagner           |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- links: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- source_entity_id: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 100.00% |
| Address | 100.00% |
| Links | 100.00% |
| Source_entity_id | 100.00% |



### Data sample
```
| names                               | birth_date   | address     | links                                                                                                                   | source_entity_id                                         |
|:------------------------------------|:-------------|:------------|:------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| ['Терещенко Олег Сергеевич']        | 01.10.1982   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/tereshhenko-oleg-sergeevich/', comment=None)]       | bc72a71ceae7ec3af62b343c9b0a7cdc9ec067b177e60fb6b148784e |
| ['Гертер Федор Михайлович']         | 31.03.1977   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/gerter-fedor-mikhajlovich/', comment=None)]         | 2028fd9c91343c3c24fd0d24535ed764af2ba1baae61dfd499b26720 |
| ['Шарыпов Олег Анатольевич']        | 13.04.1980   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/sharypov-oleg-anatolevich/', comment=None)]         | 8e12fc040f5e1f5919d6e89404655d74687dc44c5d7d3cc90d190ee5 |
| ['Клешнев Александр Юрьевич']       | 15.04.1967   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/kleshnev-aleksandr-yurevich/', comment=None)]       | 7502f2dd277a17ddfbe428ad0dc30383615b8af891536d4664a236a3 |
| ['Сазонов Валентин Дмитриевич']     | 04.03.1985   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/sazonov-valentin-dmitrievich/', comment=None)]      | b8a8529e9c1c8b1f9e3aa0e3c62e94d17d54f6fc98b39a794a8a0b64 |
| ['Валиев Ильсен Хамзаевич']         | 06.09.1990   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/valiev-ilsen-khamzaevich/', comment=None)]          | c0cc7e87006117e88f8b7806504310e011bbd0731119649e7ef4ab1f |
| ['Швецов Игорь Геннадьевич']        | 22.07.1978   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/shvecov-igor-gennadevich/', comment=None)]          | 0039963f7cfca20d310d95bb03f0755f74b5f48e08c65e6af7f693d3 |
| ['Лабинский Антон Михайлович']      | 04.04.1982   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/labinskij-anton-mikhajlovich/', comment=None)]      | 1c098dbd9549fbc590992ae858eaa289ced71eb7fa7ce6e62eab1ac9 |
| ['Кубанкин Алексей Михайлович']     | 05.08.1969   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/kubankin-aleksej-mikhajlovich/', comment=None)]     | 37e71096bf499b13813ac8b5cce7ae74cec91abc6605087bfc175eb5 |
| ['Саржан Виктор Александрович']     | 28.11.1969   | ['Украина'] | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/sarzhan-viktor-aleksandrovich/', comment=None)]     | 0fdaa78cf818b5f7343ff556077a2ab6032d4c90bb77cf836c62c132 |
| ['Сидоров Сергей Александрович']    | 01.01.1972   | ['Украина'] | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/sidorov-sergej-aleksandrovich/', comment=None)]     | 833c8212d73ebbdf2f31e0c924029290067f3acf358a6c02dc109f17 |
| ['Желяско Владимир Валерьевич']     | 12.05.1974   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/zhelyasko-vladimir-valerevich/', comment=None)]     | 044427d30865c21b584beaa9b52793b4ebca10e30a7cfa1a2468bc0b |
| ['Руденко Александр Святославович'] | 26.12.1984   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/rudenko-aleksandr-svyatoslavovich/', comment=None)] | 5f10868040f1b2b4e82d2cb1fb3024accbe9d9356a002f7374eee003 |
| ['Бекалдиев Заурбек Анатольевич']   | 21.09.1975   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/bekaldiev-zaurbek-anatolevich/', comment=None)]     | 7b962e08e03e97f7bf3cfb32e06f4563dabe09f2db0f219b1d387dab |
| ['Павич Зоран Радованович']         | 19.04.1991   | ['Сербия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/pavich-zoran-radovanovich/', comment=None)]         | 5aa24b218db4ccfe9c2239fa9f23b46b669634d778a3e463628707c1 |
| ['Хаметов Дамир Наильевич']         | 20.03.1975   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/khametov-damir-nailevich/', comment=None)]          | 5b2989e2bdcda8baa502596016827f15d32ad8ad25f8617b995bd226 |
| ['Забудский Дмитрий Иванович']      | 21.01.1985   | ['Украина'] | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/zabudskij-dmitrij-ivanovich/', comment=None)]       | 07c2444b03adde812e141bf318d55ef47d2bae0fbccae4815d5f9908 |
| ['Мухамедьянов Фанил Магжанович']   | 25.04.1967   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/mukhamedyanov-fanil-magzhanovich/', comment=None)]  | 6a7cc29ba4634716cbc80f6f2f766ab04532254d0c003902ec28ca45 |
| ['Китаев Владимир Михайлович']      | 01.07.1984   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/kitaev-vladimir-mikhajlovich/', comment=None)]      | 8fbded20c8d070b3a2c82cce64f6a557e6826246341a5f0c64c2e64e |
| ['Гусев Геннадий Иванович']         | 09.01.1968   | ['Россия']  | [Row(title='Myrotvorets', link='https://myrotvorets.center/criminal/gusev-gennadij-ivanovich/', comment=None)]          | c1fb29f8a8104e295675ea654e6e32ade406fbb66b39f520d6a10cff |
```