# Parsetron results

## About row data

> - Code name: index_0584
> - File path: friendsorchestra.ru.csv
> - Total rows: 31906

### Schema
```
root
 |-- PhoneNumber: long (nullable = true)
 |-- Name: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- MagnetCards: string (nullable = true)
 |-- Comment: string (nullable = true)
 |-- WhenCreated: string (nullable = true)
 |-- _c6: string (nullable = true)

```

### Data sample
```
|   PhoneNumber | Name                        | Email                | MagnetCards   | Comment                   | WhenCreated         | _c6   |
|--------------:|:----------------------------|:---------------------|:--------------|:--------------------------|:--------------------|:------|
|   79137462761 | 1                           |                      |               |                           | 04.11.2023 20:47:02 |       |
|   79996564583 | Виктория Константиновна     |                      |               |                           | 26.10.2024 0:16:28  |       |
|   79232238888 | АЛЕНА                       |                      |               |                           | 07.07.2023 15:49:11 |       |
|   79930043673 | Валерия                     |                      |               |                           | 29.11.2024 21:33:29 |       |
|   79138983286 | Дарья                       |                      |               |                           | 03.08.2022 8:00:57  |       |
|   79999909106 | ИЛЬЯ                        | trigandead@gmail.com |               |                           | 03.08.2022 8:00:39  |       |
|   79835143915 | КРИСТИНА                    |                      |               |                           | 03.08.2022 8:00:13  |       |
|   79137707666 | Марина                      | mura90210@yandex.ru  |               |                           | 03.08.2022 8:00:36  |       |
|   79231882534 | Станислав Владимирович      |                      |               |                           | 09.03.2023 13:15:02 |       |
|   79137003208 | Мария                       | Marianoch@yandex.ru  |               |                           | 03.08.2022 8:00:59  |       |
|   79224633999 | Юлия                        |                      |               |                           | 30.06.2022 11:32:41 |       |
|   79137691845 | Регина                      |                      |               |                           | 30.05.2025 19:45:41 |       |
|   79132086517 | Анна                        |                      |               |                           | 30.06.2022 11:32:50 |       |
|   79921167591 | A. Borya                    |                      |               |                           | 03.03.2023 11:48:47 |       |
|   79831313616 | Aborneva Anna               |                      |               |                           | 22.01.2019 0:08:39  |       |
|   79963815991 | Abuzarova Regina            |                      |               |                           | 27.05.2024 16:34:30 |       |
|   79139858145 | Adamovskaya Инна Викторовна |                      |               |                           | 03.04.2022 10:14:44 |       |
|   79137293178 | Afonasina Anna              | anaehe@yandex.ru     |               | п/о 4200 безнал от 27.02. | 16.08.2019 9:58:40  |       |
|   79139403495 | Akhanteva Anna              |                      |               |                           | 16.08.2019 9:58:41  |       |
|   79963829552 | Akhmerova Mariya            |                      |               |                           | 03.08.2022 8:00:19  |       |
```


## About final data
> - Total rows: 31297

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- actuality: date (nullable = true)
 |-- raw_metadata: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 11.20% |
| Phones | 99.96% |
| Actuality | 100.00% |
| Raw_metadata | 4.23% |



### Data sample
```
| names                           | emails                    | phones          | actuality   | raw_metadata   |
|:--------------------------------|:--------------------------|:----------------|:------------|:---------------|
| ['Виктория Константиновна']     |                           | ['79996564583'] | 26.10.2024  |                |
| ['Алена']                       |                           | ['79232238888'] | 07.07.2023  |                |
| ['Валерия']                     |                           | ['79930043673'] | 29.11.2024  |                |
| ['Дарья']                       |                           | ['79138983286'] | 03.08.2022  |                |
| ['Илья']                        | ['trigandead@gmail.com']  | ['79999909106'] | 03.08.2022  |                |
| ['Кристина']                    |                           | ['79835143915'] | 03.08.2022  |                |
| ['Марина']                      | ['mura90210@yandex.ru']   | ['79137707666'] | 03.08.2022  |                |
| ['Станислав Владимирович']      |                           | ['79231882534'] | 09.03.2023  |                |
| ['Мария']                       | ['marianoch@yandex.ru']   | ['79137003208'] | 03.08.2022  |                |
| ['Юлия']                        |                           | ['79224633999'] | 30.06.2022  |                |
| ['Регина']                      |                           | ['79137691845'] | 30.05.2025  |                |
| ['Анна']                        |                           | ['79132086517'] | 30.06.2022  |                |
| ['A. Borya']                    |                           | ['79921167591'] | 03.03.2023  |                |
| ['Aborneva Anna']               |                           | ['79831313616'] | 22.01.2019  |                |
| ['Abuzarova Regina']            |                           | ['79963815991'] | 27.05.2024  |                |
| ['Adamovskaya Инна Викторовна'] |                           | ['79139858145'] | 03.04.2022  |                |
| ['Afonasina Anna']              | ['anaehe@yandex.ru']      | ['79137293178'] | 16.08.2019  |                |
| ['Akhanteva Anna']              |                           | ['79139403495'] | 16.08.2019  |                |
| ['Akhmerova Mariya']            |                           | ['79963829552'] | 03.08.2022  |                |
| ['Akil Samir']                  | ['eng.samir95@gmail.com'] | ['79137224599'] | 03.08.2022  |                |
```