# Parsetron results

## About row data

> - Code name: index_0409
> - File path: contacts_cmexpert_ru_40k_2025.csv
> - Total rows: 38263

### Schema
```
root
 |-- ID: string (nullable = true)
 |-- Name: string (nullable = true)
 |-- Phone: string (nullable = true)
 |-- Page: string (nullable = true)
 |-- contact URL: string (nullable = true)
 |-- URL: string (nullable = true)

```

### Data sample
```
|       ID | Name                                | Phone              | Page                                                 | contact URL   | URL   |
|---------:|:------------------------------------|:-------------------|:-----------------------------------------------------|:--------------|:------|
| 47243658 | АБАКАНСКАЯ ТОРГОВАЯ ПЛОЩАДКА        | 79831913322        | https://cmexpert.amocrm.ru/companies/detail/47243658 |               |       |
| 49904260 | Аббасов Камил Видади оглы           | +7 (906) 000-05-17 | https://cmexpert.amocrm.ru/contacts/detail/49904260  |               |       |
| 49745186 | Абдиба Давид Важевич                | +7 (925) 297-77-41 | https://cmexpert.amocrm.ru/contacts/detail/49745186  |               |       |
| 49608512 | Абдирашид уулу Ырысбек              | +7 (906) 066-10-93 | https://cmexpert.amocrm.ru/contacts/detail/49608512  |               |       |
| 49475462 | Абдрахманов Алмаз Хайдарович        | +7 (937) 777-40-94 | https://cmexpert.amocrm.ru/contacts/detail/49475462  |               |       |
| 49730358 | АБДУКОДИРОВ ТИМУР БОХОДИРЖОНОВИЧ    | +7 (923) 182-90-00 | https://cmexpert.amocrm.ru/contacts/detail/49730358  |               |       |
| 49323774 | Абдулаева                           | +7 (999) 208-42-90 | https://cmexpert.amocrm.ru/contacts/detail/49323774  |               |       |
| 46146532 | АБДУЛБАСИРОВ ИСЛАМ АБДУЛХАМИДОВИЧ   |                    | https://cmexpert.amocrm.ru/contacts/detail/46146532  |               |       |
| 49365742 | Абдулин Руслан Илгизович            | +7 (902) 264-64-56 | https://cmexpert.amocrm.ru/contacts/detail/49365742  |               |       |
| 50281346 | Абдулкадиров                        | +7 (936) 666-63-66 | https://cmexpert.amocrm.ru/contacts/detail/50281346  |               |       |
| 49279828 | Абдуллаев Сабухи Ровшанович         | +7 (987) 081-11-18 | https://cmexpert.amocrm.ru/contacts/detail/49279828  |               |       |
| 49326872 | Абдуллин Магомед Фоатович           | +7 (960) 033-90-55 | https://cmexpert.amocrm.ru/contacts/detail/49326872  |               |       |
| 49374062 | Абдурагимов Наби Исмаилович         | +7 (988) 228-20-75 | https://cmexpert.amocrm.ru/contacts/detail/49374062  |               |       |
| 50101268 | Абдуразаков Виталий Юрьевич         | +7 (911) 782-89-79 | https://cmexpert.amocrm.ru/contacts/detail/50101268  |               |       |
| 50362964 | Абдуразаков Юрий Геннадьевич        | +7 (918) 014-85-93 | https://cmexpert.amocrm.ru/contacts/detail/50362964  |               |       |
| 49263026 | Абдурахманов Абдуллох Абубахрамович | +7 (913) 475-52-74 | https://cmexpert.amocrm.ru/contacts/detail/49263026  |               |       |
| 50632948 | Абдурзаков Билал Ибрагимович        | +7 (989) 928-82-04 | https://cmexpert.amocrm.ru/contacts/detail/50632948  |               |       |
| 50679315 | Абдусалямов Шавкат Хасмджонович     | +7 (968) 372-42-72 | https://cmexpert.amocrm.ru/contacts/detail/50679315  |               |       |
| 49440300 | Абеев Ильфат Ринатович              |                    | https://cmexpert.amocrm.ru/contacts/detail/49440300  |               |       |
| 49319308 | Абеев Ильфат Ринатович              |                    | https://cmexpert.amocrm.ru/contacts/detail/49319308  |               |       |
```


## About final data
> - Total rows: 16914

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 100.00% |



### Data sample
```
| names                           | phones          |
|:--------------------------------|:----------------|
| ['Авангард']                    | ['79020407676'] |
| ['Автосалон Oscar Орел']        | ['79102020990'] |
| ['Автосалон Леон Авто']         | ['78612501002'] |
| ['Автотрейд Екат']              | ['79002099995'] |
| ['Агамалов Алы Аббасович']      | ['79917100989'] |
| ['Александр']                   | ['79611005454'] |
| ['Александр']                   | ['79807253885'] |
| ['Александр']                   | ['79819717455'] |
| ['Александр Еремеев - Уволен']  | ['79867360149'] |
| ['Альянс Уфа']                  | ['79374788243'] |
| ['Андрей']                      | ['79267814868'] |
| ['Анна Сабурова']               | ['78633067777'] |
| ['Антон']                       | ['79626991047'] |
| ['Артём']                       | ['79093000066'] |
| ['Баркалов Владислав Павлович'] | ['79250170171'] |
| ['Вадим']                       | ['79211029378'] |
| ['Вадим']                       | ['79174889237'] |
| ['Василий Кармаев']             | ['79166443177'] |
| ['Виктор']                      | ['79148762538'] |
| ['Виктор']                      | ['79233555597'] |
```