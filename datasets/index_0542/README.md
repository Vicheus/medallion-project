# Parsetron results

## About row data

> - Code name: index_0542
> - File path: data.csv
> - Total rows: 60905

### Schema
```
root
 |-- Наименование: string (nullable = true)
 |-- Дата создания: string (nullable = true)
 |-- Instagram_WZ (контакт): string (nullable = true)
 |-- Телефон: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- BotHelp_CUser_ID (контакт): string (nullable = true)
 |-- Должность (контакт): string (nullable = true)
 |-- Компания: string (nullable = true)
 |-- Сделки: string (nullable = true)
 |-- _c9: string (nullable = true)
 |-- _c10: string (nullable = true)
 |-- _c11: string (nullable = true)
 |-- _c12: string (nullable = true)
 |-- _c13: string (nullable = true)

```

### Data sample
```
| Наименование               | Дата создания   | Instagram_WZ (контакт)   | Телефон           | Email   | BotHelp_CUser_ID (контакт)   | Должность (контакт)   | Компания   | Сделки            | _c9   | _c10   | _c11   | _c12   | _c13   |
|:---------------------------|:----------------|:-------------------------|:------------------|:--------|:-----------------------------|:----------------------|:-----------|:------------------|:------|:-------|:-------|:-------|:-------|
| Vlad Poletaev              | Сегодня 13:15   | @thevladpoletaev         |                   |         |                              |                       |            | Заявка от (Vlad…  |       |        |        |        |        |
| Ольга Гомолко              | Сегодня 12:59   | @olga_gomolko_           |                   |         |                              |                       |            | Заявка от (Ольга… |       |        |        |        |        |
| Olga_model_travel          | Сегодня 12:44   | @malekylaolga8           | +375 25 740-96-38 |         |                              |                       |            | Заявка от (Olga_… |       |        |        |        |        |
| Екатерина                  | Сегодня 12:36   | @senkevich21             |                   |         |                              |                       |            | Заявка от (Екате… |       |        |        |        |        |
| Марина                     | Сегодня 12:32   |                          | +375 29 397 3326  |         |                              |                       |            | Козловский Серге… |       |        |        |        |        |
| ...                        | Сегодня 12:05   | @alina.milashevskaya_    |                   |         |                              |                       |            | Заявка от (       |       |        |        |        |        |
| Автоконтакт +375296668252  | Сегодня 11:58   |                          | +375 29 666-82-52 |         |                              |                       |            | Звонок от +37529… |       |        |        |        |        |
| Воля                       | Сегодня 11:43   | @ponamorova              |                   |         |                              |                       |            | Заявка от (Воля)  |       |        |        |        |        |
| Женя                       | Сегодня 11:42   | @_irllurt                |                   |         |                              |                       |            | Заявка от (Женя)  |       |        |        |        |        |
| Анастасия                  | Сегодня 11:40   |                          | +375 44 567-08-46 |         |                              |                       |            | Анастасия         |       |        |        |        |        |
| Автоконтакт +375296100209  | Сегодня 11:23   |                          | +375 29 610-02-09 |         |                              |                       |            | Сергей            |       |        |        |        |        |
| Автоконтакт +375296210494  | Сегодня 10:52   |                          | +375 29 621-04-94 |         |                              |                       |            | Валентина         |       |        |        |        |        |
| Ольга Монич                | Сегодня 10:50   | @olya_plaskonnaya        |                   |         |                              |                       |            | Заявка от (Ольга… |       |        |        |        |        |
| Миша Рябушко               | Сегодня 10:49   | @mishka_shishka7         |                   |         |                              |                       |            | Заявка от (Миша…  |       |        |        |        |        |
| Кристина Белько            | Сегодня 09:41   | @kristi_belko            |                   |         |                              |                       |            | Заявка от (Крист… |       |        |        |        |        |
| ...                        | Вчера 22:44     | @danilevich_10           |                   |         |                              |                       |            | Заявка от (       |       |        |        |        |        |
| Наталья Иванец             | Вчера 22:44     | @ivanets_nata87          |                   |         |                              |                       |            | Заявка от (Натал… |       |        |        |        |        |
| Вероника Цубикова | Певица | Вчера 19:35     | @veronikatsubikova       |                   |         |                              |                       |            | Заявка от (Верон… |       |        |        |        |        |
| Автоконтакт +375296175566  | Вчера 18:20     |                          | +375 29 617-55-66 |         |                              |                       |            | Звонок от +37529… |       |        |        |        |        |
| Анна Тиунчик               | Вчера 16:27     | @anya_tiunchik           |                   |         |                              |                       |            | Заявка от (Тиунч… |       |        |        |        |        |
```


## About final data
> - Total rows: 34946

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- socials: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- id: string (nullable = true)
 |    |    |-- link: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 43.15% |
| Emails | 1.51% |
| Socials | 74.22% |
| Actuality | 98.37% |



### Data sample
```
| names                             | phones           | emails   | socials                                                                         | actuality   |
|:----------------------------------|:-----------------|:---------|:--------------------------------------------------------------------------------|:------------|
| ['Vlad Poletaev']                 |                  |          | [Row(title='Instagram', id=None, link='@thevladpoletaev', comment=None)]        |             |
| ['Ольга Гомолко']                 |                  |          | [Row(title='Instagram', id=None, link='@olga_gomolko_', comment=None)]          |             |
| ['Olgamodeltravel']               | ['375257409638'] |          | [Row(title='Instagram', id=None, link='@malekylaolga8', comment=None)]          |             |
| ['Екатерина']                     |                  |          | [Row(title='Instagram', id=None, link='@senkevich21', comment=None)]            |             |
| ['Марина']                        | ['375293973326'] |          |                                                                                 |             |
| ['Воля']                          |                  |          | [Row(title='Instagram', id=None, link='@ponamorova', comment=None)]             |             |
| ['Женя']                          |                  |          | [Row(title='Instagram', id=None, link='@_irllurt', comment=None)]               |             |
| ['Анастасия']                     | ['375445670846'] |          |                                                                                 |             |
| ['Ольга Монич']                   |                  |          | [Row(title='Instagram', id=None, link='@olya_plaskonnaya', comment=None)]       |             |
| ['Миша Рябушко']                  |                  |          | [Row(title='Instagram', id=None, link='@mishka_shishka7', comment=None)]        |             |
| ['Кристина Белько']               |                  |          | [Row(title='Instagram', id=None, link='@kristi_belko', comment=None)]           |             |
| ['Наталья Иванец']                |                  |          | [Row(title='Instagram', id=None, link='@ivanets_nata87', comment=None)]         |             |
| ['Вероника Цубикова Певица']      |                  |          | [Row(title='Instagram', id=None, link='@veronikatsubikova', comment=None)]      |             |
| ['Анна Тиунчик']                  |                  |          | [Row(title='Instagram', id=None, link='@anya_tiunchik', comment=None)]          |             |
| ['M A R I Y A V O R O N A']       |                  |          | [Row(title='Instagram', id=None, link='@__mashen_ka_', comment=None)]           |             |
| ['Екатерина Зубарь']              |                  |          | [Row(title='Instagram', id=None, link='@ekaterina.zubar', comment=None)]        |             |
| ['Tatsiana Kaftayan']             |                  |          | [Row(title='Instagram', id=None, link='@kaftayan', comment=None)]               |             |
| ['Tatiana Ikanovich']             |                  |          | [Row(title='Instagram', id=None, link='@tatiikanovich', comment=None)]          |             |
| ['Эндокринолог Алла Шепелькевич'] |                  |          | [Row(title='Instagram', id=None, link='@prof_alla_shepelkevich', comment=None)] |             |
| ['Olga']                          |                  |          | [Row(title='Instagram', id=None, link='@daniilborsenkou', comment=None)]        |             |
```