# Parsetron results

## About row data

> - Code name: index_0159
> - File path: /media/user/SAMSUNG/Databases/index_0159/raw/sravni.ru_db/sravni.ru_db.txt
> - Total rows: 1000000

### Schema
```
root
 |-- phone: string (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- middle_name: string (nullable = true)

```

### Data sample
```
|       phone | birth_date   | last_name   | first_name   | middle_name    |
|------------:|:-------------|:------------|:-------------|:---------------|
| 79151896110 | 24.07.1967   | podshivalov | vitalii      | vladimirovich  |
| 79069238805 | 14.03.1961   | larisa      |              |                |
| 79226537493 | 26.01.1976   | denisova    | oksana       | dmitrievna     |
| 79619199990 | 18.01.1989   | ekimova     | alesya       | romanovna      |
| 79523878767 | 29.01.1987   | makhova     | ekaterina    | gennadevna     |
| 73952645794 | 06.05.1986   | timofeeva   | elena        | valerevna      |
| 79877225708 | 22.01.1986   | ibragimov   | ruslan       | zinnurovich    |
| 79174068735 | 31.01.1994   | aleksei     |              |                |
| 79148998879 | 30.01.1948   | gerasimov   | aleksandr    | semenovich     |
| 79522585958 | 26.12.1999   | alimova     | taisiya      | vitalevna      |
| 79513147101 | 28.03.1997   | karpenkova  | viktoriya    | viktorovna     |
| 79053491397 | 12.08.1983   | mikhail     |              |                |
| 79156311573 | 05.10.1981   | elena       |              |                |
| 79871356710 | 19.06.1996   | aleksei     |              |                |
| 79267385327 | 05.07.1953   | vyacheslav  |              |                |
| 89126756094 | 25.12.1951   | mamaeva     | galiya       | ilmyatdinovna  |
| 73452432214 | 22.12.1967   | monarev     | oleg         | igorevich      |
| 79137462638 | 28.01.1997   | shemanskii  | maksim       | aleksandrovich |
| 79063834111 | 07.01.2005   | stepanov    | artem        | anatolevich    |
| 79069687775 | 25.08.1981   | natalya     |              |                |
```


## About final data
> - Total rows: 984658

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)

```

### Data sample
```
| names                                                                    | phones          | birth_date   |
|:-------------------------------------------------------------------------|:----------------|:-------------|
| ['Podshivalov Vitalii Vladimirovich', 'Подшивалов Виталии Владимирович'] | ['79151896110'] | 24.07.1967   |
| ['Larisa', 'Лариса']                                                     | ['79069238805'] | 14.03.1961   |
| ['Denisova Oksana Dmitrievna', 'Денисова Оксана Дмитриевна']             | ['79226537493'] | 26.01.1976   |
| ['Ekimova Alesya Romanovna', 'Екимова Алесыа Романовна']                 | ['79619199990'] | 18.01.1989   |
| ['Makhova Ekaterina Gennadevna', 'Макхова Екатерина Геннадевна']         | ['79523878767'] | 29.01.1987   |
| ['Timofeeva Elena Valerevna', 'Тимофеева Елена Валеревна']               | ['73952645794'] | 06.05.1986   |
| ['Ibragimov Ruslan Zinnurovich', 'Ибрагимов Руслан Зиннурович']          | ['79877225708'] | 22.01.1986   |
| ['Aleksei', 'Алексеи']                                                   | ['79174068735'] | 31.01.1994   |
| ['Gerasimov Aleksandr Semenovich', 'Герасимов Александр Семенович']      | ['79148998879'] | 30.01.1948   |
| ['Alimova Taisiya Vitalevna', 'Алимова Таисиыа Виталевна']               | ['79522585958'] | 26.12.1999   |
| ['Karpenkova Viktoriya Viktorovna', 'Карпенкова Викториыа Викторовна']   | ['79513147101'] | 28.03.1997   |
| ['Mikhail', 'Микхаил']                                                   | ['79053491397'] | 12.08.1983   |
| ['Elena', 'Елена']                                                       | ['79156311573'] | 05.10.1981   |
| ['Aleksei', 'Алексеи']                                                   | ['79871356710'] | 19.06.1996   |
| ['Vyacheslav', 'Выачеслав']                                              | ['79267385327'] | 05.07.1953   |
| ['Mamaeva Galiya Ilmyatdinovna', 'Мамаева Галиыа Илмыатдиновна']         | ['79126756094'] | 25.12.1951   |
| ['Monarev Oleg Igorevich', 'Монарев Олег Игоревич']                      | ['73452432214'] | 22.12.1967   |
| ['Shemanskii Maksim Aleksandrovich', 'Шеманскии Максим Александрович']   | ['79137462638'] | 28.01.1997   |
| ['Stepanov Artem Anatolevich', 'Степанов Артем Анатолевич']              | ['79063834111'] | 07.01.2005   |
| ['Natalya', 'Наталыа']                                                   | ['79069687775'] | 25.08.1981   |
```