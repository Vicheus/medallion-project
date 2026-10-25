# Parsetron results

## About row data

> - Code name: index_0170
> - File path: /media/user/SAMSUNG/Databases/index_0170/raw/parsed_data.csv
> - Total rows: 233175

### Schema
```
root
 |-- Expiration: integer (nullable = true)
 |-- Cardholder Name: string (nullable = true)
 |-- PAN: string (nullable = true)
 |-- IP: string (nullable = true)

```

### Data sample
```
|   Expiration | Cardholder Name   | PAN              | IP             |
|-------------:|:------------------|:-----------------|:---------------|
|       202209 | TIMUR CHAIKOVSKII | 427630XXXXXX1102 | 178.155.4.21   |
|       202209 | TIMUR CHAIKOVSKII | 427630XXXXXX1102 | 178.155.4.21   |
|       202209 | TIMUR CHAIKOVSKII | 427630XXXXXX1102 | 178.155.4.21   |
|       202112 | CARDHOLDER NAME   | 548430XXXXXX0552 | 128.70.244.185 |
|       202112 | CARDHOLDER NAME   | 548430XXXXXX0552 | 128.70.244.185 |
|       202112 | CARDHOLDER NAME   | 548430XXXXXX0552 | 128.70.244.185 |
|       202209 | TIMUR CHAIKOVSKII | 427630XXXXXX1102 | 178.155.4.21   |
|       202209 | TIMUR CHAIKOVSKII | 427630XXXXXX1102 | 178.155.4.21   |
|       202209 | TIMUR CHAIKOVSKII | 427630XXXXXX1102 | 178.155.4.21   |
|       202409 | DMITRIY CHUGUNOV  | 553691XXXXXX4497 | 178.155.6.61   |
|       202409 | DMITRIY CHUGUNOV  | 553691XXXXXX4497 | 178.155.6.61   |
|       202409 | DMITRIY CHUGUNOV  | 553691XXXXXX4497 | 178.155.6.61   |
|       202302 | DONOVA MARINA     | 427930XXXXXX9976 | 2.95.63.210    |
|       202302 | DONOVA MARINA     | 427930XXXXXX9976 | 2.95.63.210    |
|       202302 | DONOVA MARINA     | 427930XXXXXX9976 | 2.95.63.210    |
|       202302 | DONOVA MARINA     | 427930XXXXXX9976 | 2.95.63.210    |
|       202302 | DONOVA MARINA     | 427930XXXXXX9976 | 2.95.63.210    |
|       202302 | DONOVA MARINA     | 427930XXXXXX9976 | 2.95.63.210    |
|       202302 | DONOVA MARINA     | 427930XXXXXX9976 | 2.95.63.210    |
|       202302 | DONOVA MARINA     | 427930XXXXXX9976 | 2.95.63.210    |
```


## About final data
> - Total rows: 1973

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)
 |    |    |-- date: void (nullable = true)
 |-- financials: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- card_number: string (nullable = true)
 |    |    |-- date_issue: void (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- comment: void (nullable = true)

```

### Data sample
```
| names                     | ips                                    | financials                                                                                                       |
|:--------------------------|:---------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| ['Natalya Markova']       | [Row(ip='89.178.155.24', date=None)]   | [Row(title='СберБанк', card_number='552175XXXXXX0063', date_issue=None, date_expire='2023-06-01', comment=None)] |
| ['Gayvoronskiy Vlad']     | [Row(ip='85.174.192.190', date=None)]  | [Row(title='СберБанк', card_number='555949XXXXXX0685', date_issue=None, date_expire='2024-01-01', comment=None)] |
| ['Mikhail Dudarev']       | [Row(ip='37.146.62.199', date=None)]   | [Row(title='СберБанк', card_number='555949XXXXXX6249', date_issue=None, date_expire='2024-10-01', comment=None)] |
| ['Marin Pavel']           | [Row(ip='37.146.59.229', date=None)]   | [Row(title='СберБанк', card_number='479004XXXXXX9873', date_issue=None, date_expire='2024-08-01', comment=None)] |
| ['Aleksey Gromov']        | [Row(ip='45.157.215.5', date=None)]    | [Row(title='СберБанк', card_number='548674XXXXXX4283', date_issue=None, date_expire='2023-08-01', comment=None)] |
| ['Svetlana Stepanova']    | [Row(ip='31.181.136.15', date=None)]   | [Row(title='СберБанк', card_number='458443XXXXXX6083', date_issue=None, date_expire='2024-03-01', comment=None)] |
| ['Maksim Pechenkin']      | [Row(ip='178.176.218.189', date=None)] | [Row(title='СберБанк', card_number='552186XXXXXX4988', date_issue=None, date_expire='2024-04-01', comment=None)] |
| ['Anna']                  | [Row(ip='37.78.175.224', date=None)]   | [Row(title='СберБанк', card_number='479087XXXXXX6193', date_issue=None, date_expire='2022-10-01', comment=None)] |
| ['Dmitriy Sviridov']      | [Row(ip='213.87.137.252', date=None)]  | [Row(title='СберБанк', card_number='458443XXXXXX1123', date_issue=None, date_expire='2024-09-01', comment=None)] |
| ['Svetlana Temirova']     | [Row(ip='37.146.57.44', date=None)]    | [Row(title='СберБанк', card_number='555949XXXXXX9708', date_issue=None, date_expire='2023-11-01', comment=None)] |
| ['Robert Minasov']        | [Row(ip='95.153.129.238', date=None)]  | [Row(title='СберБанк', card_number='555949XXXXXX5743', date_issue=None, date_expire='2023-09-01', comment=None)] |
| ['Natalia Fursa']         | [Row(ip='37.146.57.60', date=None)]    | [Row(title='СберБанк', card_number='555949XXXXXX3510', date_issue=None, date_expire='2024-12-01', comment=None)] |
| ['Anton Zhuravlev']       | [Row(ip='176.59.67.226', date=None)]   | [Row(title='СберБанк', card_number='555949XXXXXX0761', date_issue=None, date_expire='2023-10-01', comment=None)] |
| ['Kristina Pavlova']      | [Row(ip='178.155.4.171', date=None)]   | [Row(title='СберБанк', card_number='479004XXXXXX2116', date_issue=None, date_expire='2022-12-01', comment=None)] |
| ['Aleksei Lagoda']        | [Row(ip='188.170.192.113', date=None)] | [Row(title='СберБанк', card_number='555949XXXXXX7373', date_issue=None, date_expire='2024-10-01', comment=None)] |
| ['Ruslan Rakhmanberdiev'] | [Row(ip='85.174.203.184', date=None)]  | [Row(title='СберБанк', card_number='458443XXXXXX6743', date_issue=None, date_expire='2025-02-01', comment=None)] |
| ['Dmitrii Borivosov']     | [Row(ip='188.162.167.103', date=None)] | [Row(title='СберБанк', card_number='555949XXXXXX0411', date_issue=None, date_expire='2022-05-01', comment=None)] |
| ['Mikhail Teleshev']      | [Row(ip='95.153.128.233', date=None)]  | [Row(title='СберБанк', card_number='479004XXXXXX5015', date_issue=None, date_expire='2025-08-01', comment=None)] |
| ['Sheremeteva Mariia']    | [Row(ip='85.174.198.232', date=None)]  | [Row(title='СберБанк', card_number='552175XXXXXX0050', date_issue=None, date_expire='2022-01-01', comment=None)] |
| ['Teslenko Alexander']    | [Row(ip='37.146.63.142', date=None)]   | [Row(title='СберБанк', card_number='555949XXXXXX3032', date_issue=None, date_expire='2024-07-01', comment=None)] |
```