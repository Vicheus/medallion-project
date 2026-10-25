# Parsetron results

## About row data

> - Code name: index_0262
> - File path: /media/user/SAMSUNG/Databases/index_0262/raw/users_preprocessed.csv
> - Total rows: 445081

### Schema
```
root
 |-- author_ip: string (nullable = true)
 |-- author_name: string (nullable = true)
 |-- author_email: string (nullable = true)

```

### Data sample
```
| author_ip       | author_name   | author_email                  |
|:----------------|:--------------|:------------------------------|
| 62.183.127.44   | stroiteli     | angel-i-demon@inbox.ru        |
| 82.145.220.255  | arssochi77777 | arssochi77777@yandex.ru       |
| 94.232.17.172   | ЯнеЯ          | alla06-06@bk.ru               |
| 217.212.230.173 | yoliya16      | yoliya16@mail.ru              |
| 46.159.196.231  | ARMAVIR228FBI | nomail@okru.ru                |
| 5.138.151.113   | Бокова        | verba.ol@yandex.ru            |
| 176.32.147.68   | muha83        | muha83@mail.ru                |
| 95.153.169.136  | Витькина      | nomail@okru.ru                |
| 95.153.191.232  | мирона        | nomail@okru.ru                |
| 5.139.170.65    | квинта        | vale.rowenskaia2014@yandex.ru |
| 95.153.189.88   | Олеся2013     | Olesehka2012@mail.ru          |
| 80.239.243.154  | АннаОЛЕГ      | nomail@okru.ru                |
| 31.181.139.116  | LEXUS_JS      | VIRABUAN2014@MAIL.RU          |
| 94.77.7.168     | Цербер        | nomail@okru.ru                |
| 46.158.134.200  | Игорь87       | nomail@okru.ru                |
| 95.153.200.210  | Кира5         | irina_povoiko@mail.ru         |
| 85.175.218.107  | prok          | work-prok@mail.ru             |
| 176.32.154.217  | dashuny       | shihckerimova.alla@yandex.ru  |
| 31.181.64.181   | AstEugene     | a_eugene@mail.ru              |
| 85.26.186.218   | Svetlana1980  | himicheva.svetlana@yandex.ru  |
```


## About final data
> - Total rows: 247883

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- ip: string (nullable = true)

```

### Data sample
```
| names          | emails                            | ips                        |
|:---------------|:----------------------------------|:---------------------------|
| ['Stroiteli']  | ['angel-i-demon@inbox.ru']        | [Row(ip='62.183.127.44')]  |
| ['Янея']       | ['alla06-06@bk.ru']               | [Row(ip='94.232.17.172')]  |
| ['Бокова']     | ['verba.ol@yandex.ru']            | [Row(ip='5.138.151.113')]  |
| ['Витькина']   | ['nomail@okru.ru']                | [Row(ip='95.153.169.136')] |
| ['Мирона']     | ['nomail@okru.ru']                | [Row(ip='95.153.191.232')] |
| ['Квинта']     | ['vale.rowenskaia2014@yandex.ru'] | [Row(ip='5.139.170.65')]   |
| ['Аннаолег']   | ['nomail@okru.ru']                | [Row(ip='80.239.243.154')] |
| ['Lexusjs']    | ['virabuan2014@mail.ru']          | [Row(ip='31.181.139.116')] |
| ['Цербер']     | ['nomail@okru.ru']                | [Row(ip='94.77.7.168')]    |
| ['Prok']       | ['work-prok@mail.ru']             | [Row(ip='85.175.218.107')] |
| ['Dashuny']    | ['shihckerimova.alla@yandex.ru']  | [Row(ip='176.32.154.217')] |
| ['Asteugene']  | ['a_eugene@mail.ru']              | [Row(ip='31.181.64.181')]  |
| ['Кыса']       | ['nomail@okru.ru']                | [Row(ip='94.232.22.7')]    |
| ['San-Sanich'] | ['alex07.1971@mail.ru']           | [Row(ip='185.3.33.51')]    |
| ['Tanayaza']   | ['tanayazamalzeva@mail.ru']       | [Row(ip='94.232.16.236')]  |
| ['Niss']       | ['i_linnik@nbox.ru']              | [Row(ip='217.118.81.203')] |
| ['Людмилаб']   | ['barannik.maria3@mail.ru']       | [Row(ip='176.32.154.232')] |
| ['Vitalion']   | ['vitalix-vitalion@rambler.ru']   | [Row(ip='94.232.19.201')]  |
| ['Gps']        | ['vadim_0632@mail.ru']            | [Row(ip='46.173.191.109')] |
| ['Bidyin']     | ['bidyin@mail.ru']                | [Row(ip='94.232.16.141')]  |
```