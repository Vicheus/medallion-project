# Parsetron results

## About row data

> - File path: customers.csv
> - Total rows: 82242

### Schema
```
root
 |-- №: string (nullable = true)
 |-- Имя клиента: string (nullable = true)
 |-- E-mail: string (nullable = true)
 |-- Телефон: string (nullable = true)
 |-- Обращений: string (nullable = true)
 |-- E-mail оператора: string (nullable = true)
 |-- Последнее обращение: timestamp (nullable = true)
 |-- Комментарий: string (nullable = true)
 |-- Канал связи: string (nullable = true)
 |-- Источник перехода: string (nullable = true)
 |-- Ответственный агент: string (nullable = true)
 |-- Категория: string (nullable = true)
 |-- Город: string (nullable = true)
 |-- Регион: string (nullable = true)
 |-- Страна: string (nullable = true)
 |-- Теги: string (nullable = true)

```

### Data sample
```
|      № | Имя клиента       | E-mail   | Телефон      |   Обращений | E-mail оператора   | Последнее обращение   | Комментарий   | Канал связи   | Источник перехода                                                        | Ответственный агент   | Категория   | Город                   | Регион                        | Страна   | Теги   |
|-------:|:------------------|:---------|:-------------|------------:|:-------------------|:----------------------|:--------------|:--------------|:-------------------------------------------------------------------------|:----------------------|:------------|:------------------------|:------------------------------|:---------|:-------|
| 107140 | Александр         | -        | 375336157863 |           1 |                    | 2026-01-13 11:07:42   |               | mrt.by        | campaign=(organic)|source=Google|medium=search                           | -                     | Новый       | Minsk                   | Minsk City, Minski rajon      | Belarus  |        |
|  96839 | Svetlana          | -        | -            |           3 | jivo@mrt.by        | 2026-01-13 11:03:40   |               | mrt.by        | -                                                                        | -                     | Завершен    | -                       | -                             | -        |        |
| 107138 | Minsk 107138      | -        | -            |           1 | jivo@mrt.by        | 2026-01-13 10:59:58   |               | mrt.by        | campaign=(organic)|source=Yandex|medium=search                           | -                     | Новый       | Minsk                   | Minsk City                    | Belarus  |        |
| 107135 | Minsk 107135      | -        | -            |           2 | jivo@mrt.by        | 2026-01-13 10:56:01   |               | mrt.by        | campaign=(organic)|source=Google|medium=search                           | -                     | Новый       | Minsk                   | Minsk City                    | Belarus  |        |
| 107139 | Татьяна Харламова | -        | -            |           1 | jivo@mrt.by        | 2026-01-13 10:54:58   |               | mrt.by        | -                                                                        | -                     | Новый       | -                       | -                             | -        |        |
|  78879 | Юлия              | -        | 80295787329  |           9 | jivo@mrt.by        | 2026-01-13 10:41:39   |               | mrt.by        | campaign=(organic)|source=Yandex|medium=search                           | -                     | Новый       | Minsk                   | Minsk City, Minsk             | Belarus  |        |
| 101516 | Minsk 101516      | -        | -            |           2 | jivo@mrt.by        | 2026-01-13 10:28:18   |               | mrt.by        | campaign=(direct)|source=(direct)                                        | -                     | Новый       | Minsk                   | Minsk City, Minsk District    | Belarus  |        |
| 107137 | Minsk 107137      | -        | -            |           1 | jivo@mrt.by        | 2026-01-13 10:18:36   |               | mrt.by        | campaign=(organic)|source=Google|medium=search                           | -                     | Новый       | Minsk (Centraĺny rajon) | Minsk City                    | Belarus  |        |
| 107133 | Sonechny 107133   | -        | -            |           1 | jivo@mrt.by        | 2026-01-13 10:16:40   |               | mrt.by        | campaign=(organic)|source=Google|medium=search                           | -                     | Новый       | Sonechny                | Minsk, Minsk District         | Belarus  |        |
| 107136 | Евгений           | -        | 375291654294 |           1 | jivo@mrt.by        | 2026-01-13 10:01:01   |               | mrt.by        | campaign=(organic)|source=Google|medium=search                           | -                     | Новый       | Minsk (Centraĺny rajon) | Minsk City                    | Belarus  |        |
| 107134 | Екатеина          | -        | 375333803850 |           1 | jivo@mrt.by        | 2026-01-13 09:35:06   |               | mrt.by        | campaign=(organic)|source=Google|medium=search                           | -                     | Новый       | Minsk                   | Minsk City                    | Belarus  |        |
|  98442 | Lara              | -        | -            |           3 | jivo@mrt.by        | 2026-01-13 09:34:28   |               | mrt.by        | -                                                                        | -                     | Новый       | -                       | -                             | -        |        |
| 102499 | Дарья Зборина     | -        | -            |           4 | jivo@mrt.by        | 2026-01-13 09:30:51   |               | mrt.by        | -                                                                        | -                     | Завершен    | -                       | -                             | -        |        |
| 107132 | Minsk 107132      | -        | -            |           1 |                    | 2026-01-13 09:29:20   |               | mrt.by        | campaign=(organic)|source=Google|medium=search                           | -                     | Новый       | Minsk                   | Minsk City                    | Belarus  |        |
| 107130 | Hrodna 107130     | -        | -            |           1 | jivo@mrt.by        | 2026-01-13 09:10:58   |               | mrt.by        | campaign=(organic)|source=Google|medium=search                           | -                     | Новый       | Hrodna                  | Grodnenskaya, Hrodna district | Belarus  |        |
| 107131 | Ольга             | -        | 375296249996 |           1 | jivo@mrt.by        | 2026-01-13 09:00:20   |               | mrt.by        | campaign=(organic)|source=Yandex|medium=search                           | -                     | Новый       | Minsk                   | Minsk City                    | Belarus  |        |
| 107059 | Дмитрий           | -        | 375333472857 |           2 | jivo@mrt.by        | 2026-01-13 08:33:24   |               | mrt.by        | campaign=(organic)|source=Google|medium=search                           | -                     | Завершен    | Baranovichi             | Brest                         | Belarus  |        |
| 107003 | ⁣                 | -        | -            |           2 | jivo@mrt.by        | 2026-01-13 08:14:08   |               | mrt.by        | -                                                                        | -                     | Новый       | -                       | -                             | -        |        |
| 107129 | Лидия             | -        | 375297709927 |           1 | info@mrt.by        | 2026-01-13 08:01:34   |               | mrt.by        | source=ig|medium=social|content=link_in_bio                              | -                     | Новый       | Minsk                   | Minsk City, Minski rajon      | Belarus  |        |
| 107128 | Света             | -        | 375292145251 |           1 | info@mrt.by        | 2026-01-13 08:01:34   |               | mrt.by        | campaign=(referral)|source=aibolit-obw.web.app|medium=referral|content=/ | -                     | Новый       | Minsk                   | Minsk City, Minsk             | Belarus  |        |
```


## About final data

### Schema
```
root
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Phones | 100.00% |
| Names | 100.00% |
| Emails | 33.55% |
| Actuality | 100.00% |



### Data sample
```
| phones           | names                      | emails   | actuality   |
|:-----------------|:---------------------------|:---------|:------------|
| ['375259341598'] | ['Вадим']                  |          | 17.12.2024  |
| ['375291382811'] | ['Ксения']                 |          | 04.03.2025  |
| ['375291438110'] | ['Александр']              |          | 15.08.2025  |
| ['375292428208'] | ['Елена']                  |          | 21.11.2025  |
| ['375292437754'] | ['Ольга']                  |          | 23.11.2025  |
| ['375293216673'] | ['Юрий']                   |          | 15.10.2024  |
| ['375293241679'] | ['Анастасия']              |          | 27.11.2025  |
| ['375293268291'] | ['Евгений']                |          | 07.01.2025  |
| ['375293762175'] | ['Галина']                 |          | 04.04.2025  |
| ['375295162508'] | ['Анастасия']              |          | 13.11.2025  |
| ['375295625306'] | ['Ольга']                  |          | 24.04.2023  |
| ['375295718805'] | ['Анастасия']              |          | 11.06.2025  |
| ['375295878786'] | ['Анастасия']              |          | 22.04.2025  |
| ['375296104482'] | ['Ирина']                  |          | 28.11.2025  |
| ['375296464281'] | ['Алеся', 'Алеся Игнатюк'] |          | 26.02.2025  |
| ['375296540241'] | ['Сергей']                 |          | 17.12.2024  |
| ['375296955521'] | ['Вера']                   |          | 24.05.2025  |
| ['375296997668'] | ['Кристина']               |          | 24.11.2025  |
| ['375297542954'] | ['Елена']                  |          | 13.01.2025  |
| ['375297738871'] | ['Екатерина']              |          | 26.05.2025  |
```