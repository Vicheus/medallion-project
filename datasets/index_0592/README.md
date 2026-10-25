# Parsetron results

## About row data

> - Code name: index_0592
> - File path: repa.csv
> - Total rows: 53244

### Schema
```
root
 |-- PhoneNumber: long (nullable = true)
 |-- Name: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- MagnetCards: long (nullable = true)
 |-- Comment: string (nullable = true)
 |-- WhenCreated: string (nullable = true)

```

### Data sample
```
|   PhoneNumber | Name                 | Email   |      MagnetCards | Comment   | WhenCreated         |
|--------------:|:---------------------|:--------|-----------------:|:----------|:--------------------|
|   79649403210 | Adam                 |         | 9649403210954660 |           | 07.02.2025 16:34:52 |
|   79818190451 | AG                   |         | 9818190451954670 |           | 07.02.2025 16:44:22 |
|   79812521488 | Ahmed                |         | 9812521488861570 |           | 07.02.2025 16:38:14 |
|   79506223278 | Ain                  |         | 9506223278954670 |           | 07.02.2025 16:42:19 |
|   79953168654 | Akim                 |         | 9953168654954680 |           | 07.02.2025 16:46:52 |
|   14734062354 | aksan                |         | 4734062354861558 |           | 07.02.2025 16:45:55 |
|   79108964008 | Akseniya             |         | 9108964008954670 |           | 07.02.2025 16:41:22 |
|   79829506580 | Al                   |         | 9829506580874680 |           | 07.02.2025 16:45:47 |
|   79394073856 | Al                   |         | 9394073856861570 |           | 07.02.2025 16:36:15 |
|   79326968576 | Al                   |         | 9326968576861580 |           | 07.02.2025 16:39:38 |
|   79326965504 | Al                   |         | 9326965504861570 |           | 07.02.2025 16:48:24 |
|   79252469583 | Albert               |         | 9252469583861570 |           | 07.02.2025 16:50:22 |
|   79998219395 | Albert Mhitaryants   |         | 9998219395954690 |           | 07.02.2025 16:42:55 |
|   79154608295 | Aleks                |         | 9154608295861570 |           | 07.02.2025 16:42:16 |
|   79771350002 | Aleksander Sosnowski |         | 9771350002954660 |           | 07.02.2025 16:34:52 |
|   79991404036 | Aleksandr            |         | 9991404036861560 |           | 07.02.2025 16:45:53 |
|   79991389552 | Aleksandr            |         | 9991389552861580 |           | 07.02.2025 16:48:51 |
|   79867446605 | Aleksandr            |         | 9867446605954680 |           | 07.02.2025 16:47:23 |
|   79867376408 | Aleksandr            |         | 9867376408954680 |           | 07.02.2025 16:37:49 |
|   79506150106 | Aleksandr            |         | 9506150106954660 |           | 07.02.2025 16:44:35 |
```


## About final data
> - Total rows: 46269

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
| Emails | 0.02% |
| Phones | 100.00% |
| Actuality | 100.00% |
| Raw_metadata | 99.99% |



### Data sample
```
| names                    | emails   | phones          | actuality   | raw_metadata                            |
|:-------------------------|:---------|:----------------|:------------|:----------------------------------------|
| ['Ahmed']                |          | ['79812521488'] | 07.02.2025  | ['{"MagnetCards": "9812521488861570"}'] |
| ['Akim']                 |          | ['79953168654'] | 07.02.2025  | ['{"MagnetCards": "9953168654954680"}'] |
| ['Akseniya']             |          | ['79108964008'] | 07.02.2025  | ['{"MagnetCards": "9108964008954670"}'] |
| ['Albert']               |          | ['79252469583'] | 07.02.2025  | ['{"MagnetCards": "9252469583861570"}'] |
| ['Albert Mhitaryants']   |          | ['79998219395'] | 07.02.2025  | ['{"MagnetCards": "9998219395954690"}'] |
| ['Aleks']                |          | ['79154608295'] | 07.02.2025  | ['{"MagnetCards": "9154608295861570"}'] |
| ['Aleksander Sosnowski'] |          | ['79771350002'] | 07.02.2025  | ['{"MagnetCards": "9771350002954660"}'] |
| ['Aleksandr']            |          | ['79991404036'] | 07.02.2025  | ['{"MagnetCards": "9991404036861560"}'] |
| ['Aleksandr']            |          | ['79991389552'] | 07.02.2025  | ['{"MagnetCards": "9991389552861580"}'] |
| ['Aleksandr']            |          | ['79867446605'] | 07.02.2025  | ['{"MagnetCards": "9867446605954680"}'] |
| ['Aleksandr']            |          | ['79867376408'] | 07.02.2025  | ['{"MagnetCards": "9867376408954680"}'] |
| ['Aleksandr']            |          | ['79506150106'] | 07.02.2025  | ['{"MagnetCards": "9506150106954660"}'] |
| ['Aleksandr']            |          | ['79506054049'] | 07.02.2025  | ['{"MagnetCards": "9506054049861560"}'] |
| ['Aleksandr']            |          | ['79264014111'] | 07.02.2025  | ['{"MagnetCards": "9264014111861550"}'] |
| ['Aleksandr']            |          | ['79203222913'] | 07.02.2025  | ['{"MagnetCards": "9203222913861550"}'] |
| ['Aleksandr']            |          | ['79201119380'] | 07.02.2025  | ['{"MagnetCards": "9201119380874660"}'] |
| ['Aleksandr']            |          | ['79184441954'] | 07.02.2025  | ['{"MagnetCards": "9184441954861570"}'] |
| ['Aleksandr']            |          | ['79108863059'] | 07.02.2025  | ['{"MagnetCards": "9108863059954670"}'] |
| ['Aleksandr']            |          | ['79101253438'] | 07.02.2025  | ['{"MagnetCards": "9101253438954660"}'] |
| ['Aleksandr']            |          | ['79037311241'] | 07.02.2025  | ['{"MagnetCards": "9037311241874660"}'] |
```