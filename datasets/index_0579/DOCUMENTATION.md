# Parsetron results

## About row data

> - File path: aldente.csv
> - Total rows: 32233

### Schema
```
root
 |-- PhoneNumber: long (nullable = true)
 |-- Name: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- MagnetCards: string (nullable = true)
 |-- Comment: string (nullable = true)
 |-- WhenCreated: string (nullable = true)

```

### Data sample
```
|   PhoneNumber | Name      | Email   |   MagnetCards | Comment   | WhenCreated         |
|--------------:|:----------|:--------|--------------:|:----------|:--------------------|
|   79199224546 | 1         |         |               |           | 16.09.2025 17:44:41 |
|  755555555555 | 6666      |         |               |           | 16.09.2025 17:45:53 |
|   79990855066 | 613458    |         |               |           | 16.09.2025 17:44:31 |
|   79098267573 | Евгения   |         |       3004959 |           | 14.09.2025 16:15:44 |
|   79638285475 |           |         |               |           | 16.09.2025 17:46:28 |
|   79243029800 |           |         |               |           | 16.09.2025 17:47:08 |
|   79145460446 |           |         |               |           | 16.09.2025 17:44:21 |
|   79242103101 | Анна      |         |       3003210 |           | 14.09.2025 16:15:38 |
|   79098202070 | Ирина     |         |       3000442 |           | 14.09.2025 16:15:17 |
|   79997932886 | ---       |         |               |           | 16.09.2025 17:44:24 |
|   79242104867 |           |         |               |           | 24.10.2025 16:51:56 |
|   79141511963 |           |         |               |           | 16.09.2025 17:48:44 |
|  722222222222 |           |         |               |           | 16.09.2025 17:41:06 |
|   79144536150 | Александр |         |       3006374 |           | 14.09.2025 16:15:57 |
|   79249234344 | Алексей   |         |       3007342 |           | 14.09.2025 16:16:00 |
|   79144041779 | Ольга     |         |       3007046 |           | 14.09.2025 16:15:59 |
|   79990859844 | Светлана  |         |               |           | 16.09.2025 17:44:18 |
|   79141633492 |           |         |               |           | 16.09.2025 17:50:56 |
|   79147622194 | Вера      |         |       3007702 |           | 14.09.2025 16:16:08 |
|   79841580729 | ₽ДАРЬЯ    |         |               |           | 16.09.2025 17:48:20 |
```


## About final data

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
| Emails | 0.43% |
| Phones | 100.00% |
| Actuality | 100.00% |
| Raw_metadata | 29.05% |



### Data sample
```
| names                            | emails   | phones          | actuality   | raw_metadata                   |
|:---------------------------------|:---------|:----------------|:------------|:-------------------------------|
| ['Евгения']                      |          | ['79098267573'] | 14.09.2025  | ['{"MagnetCards": "3004959"}'] |
| ['Анна']                         |          | ['79242103101'] | 14.09.2025  | ['{"MagnetCards": "3003210"}'] |
| ['Ирина']                        |          | ['79098202070'] | 14.09.2025  | ['{"MagnetCards": "3000442"}'] |
| ['Александр']                    |          | ['79144536150'] | 14.09.2025  | ['{"MagnetCards": "3006374"}'] |
| ['Алексей']                      |          | ['79249234344'] | 14.09.2025  | ['{"MagnetCards": "3007342"}'] |
| ['Ольга']                        |          | ['79144041779'] | 14.09.2025  | ['{"MagnetCards": "3007046"}'] |
| ['Светлана']                     |          | ['79990859844'] | 16.09.2025  |                                |
| ['Вера']                         |          | ['79147622194'] | 14.09.2025  | ['{"MagnetCards": "3007702"}'] |
| ['Дарья']                        |          | ['79841580729'] | 16.09.2025  |                                |
| ['Abe Katsuya Abe']              |          | ['79243210408'] | 14.09.2025  | ['{"MagnetCards": "3003476"}'] |
| ['Alekseev Roman']               |          | ['79141553825'] | 14.09.2025  | ['{"MagnetCards": "3005261"}'] |
| ['Anastasia Lavrova Anastasia']  |          | ['79242181908'] | 14.09.2025  | ['{"MagnetCards": "3003865"}'] |
| ['Begalieva Galina Begalieva']   |          | ['79842866010'] | 14.09.2025  | ['{"MagnetCards": "3003349"}'] |
| ['Berezyuk Vitaly']              |          | ['79242187868'] | 14.09.2025  | ['{"MagnetCards": "3004462"}'] |
| ['Bolshaya Нина']                |          | ['79144184411'] | 14.09.2025  | ['{"MagnetCards": "3001764"}'] |
| ['Che Ruslan']                   |          | ['79249200719'] | 14.09.2025  | ['{"MagnetCards": "3006654"}'] |
| ['Chistyakova Юлия Chistyakova'] |          | ['79242054476'] | 14.09.2025  | ['{"MagnetCards": "3004374"}'] |
| ['Dautova Ekaterina Dautova']    |          | ['79242211720'] | 14.09.2025  | ['{"MagnetCards": "3003960"}'] |
| ['Elena Bychkova']               |          | ['79244029390'] | 16.09.2025  |                                |
| ['Elena Klimenko Elena']         |          | ['79241013535'] | 14.09.2025  | ['{"MagnetCards": "3004289"}'] |
```