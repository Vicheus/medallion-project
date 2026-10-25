# Parsetron results

## About row data

> - File path: vird_ru.csv
> - Total rows: 97186

### Schema
```
root
 |-- ФИО: string (nullable = true)
 |-- Номер телефона1: string (nullable = true)
 |-- Номер телефона2: string (nullable = true)
 |-- Ссылка на карточку: string (nullable = true)
 |-- _c4: string (nullable = true)
 |-- _c5: string (nullable = true)

```

### Data sample
```
| ФИО                          |   Номер телефона1 |   Номер телефона2 | Ссылка на карточку                                            | _c4   | _c5   |
|:-----------------------------|------------------:|------------------:|:--------------------------------------------------------------|:------|:------|
| Бондаренко Катерина Петровна |       79999999000 |       78442368256 | http://vird.ru/content/office/contact_details.php?cid=39561#  |       |       |
| Апанович Александр           |       79999989983 |       74952972527 | http://vird.ru/content/office/contact_details.php?cid=103543# |       |       |
| Дарья                        |       79999972144 |                   | http://vird.ru/content/office/contact_details.php?cid=103060# |       |       |
| Лаптев Павел                 |       79999894602 |                   | http://vird.ru/content/office/contact_details.php?cid=109425# |       |       |
| Выскарка Игорь Анатольевич   |       79999891442 |                   | http://vird.ru/content/office/contact_details.php?cid=106660# |       |       |
| Иванов Александр             |       79999848610 |       74951518606 | http://vird.ru/content/office/contact_details.php?cid=91963#  |       |       |
| Косогоров Иван Александрович |       79999791541 |                   | http://vird.ru/content/office/contact_details.php?cid=101165# |       |       |
| Суюров Владислав             |       79999770817 |                   | http://vird.ru/content/office/contact_details.php?cid=112269# |       |       |
| Григорьев Игорь Михайлович   |       79999750027 |                   | http://vird.ru/content/office/contact_details.php?cid=106609# |       |       |
| Леденева Галина              |       79999739541 |                   | http://vird.ru/content/office/contact_details.php?cid=104849# |       |       |
| Ичетовкина Анна Рафисовна    |       79999696123 |                   | http://vird.ru/content/office/contact_details.php?cid=116114# |       |       |
| Барсуков Павел Борисович     |       79999239659 |                   | http://vird.ru/content/office/contact_details.php?cid=108770# |       |       |
| Леухина Евгения Вадимовна    |       79999171183 |       74951438300 | http://vird.ru/content/office/contact_details.php?cid=117169# |       |       |
| Дюсмос Елена                 |       79999097754 |                   | http://vird.ru/content/office/contact_details.php?cid=114891# |       |       |
| Бреусова Елена               |       79999038277 |                   | http://vird.ru/content/office/contact_details.php?cid=111566# |       |       |
| Никонов Дмитрий Игоревич     |       79999029732 |                   | http://vird.ru/content/office/contact_details.php?cid=112537# |       |       |
| Карасенко Антон Владимирович |       79998802360 |                   | http://vird.ru/content/office/contact_details.php?cid=108584# |       |       |
| Уткин Юрий                   |       79998791292 |                   | http://vird.ru/content/office/contact_details.php?cid=111795# |       |       |
| Подзоров Никита Дмитриевич   |       79998425800 |                   | http://vird.ru/content/office/contact_details.php?cid=105674# |       |       |
| Сурков Артём Олегович        |       79998354510 |                   | http://vird.ru/content/office/contact_details.php?cid=98570#  |       |       |
```


## About final data

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
| names                               | phones          |
|:------------------------------------|:----------------|
| ['Черкасов Владимир']               | ['79997825103'] |
| ['Сапожников Антон']                | ['79899560330'] |
| ['Фил Алекс Петрович']              | ['79898172098'] |
| ['Рррр Кавпыв Ваыап']               | ['79889485449'] |
| ['Артем']                           | ['79009151415'] |
| ['Корсунов Сергей Генадьевич']      | ['79885197955'] |
| ['Кичигин Алексей Сергеевич']       | ['79882533554'] |
| ['Ямалетдинов Ринат Рустамович']    | ['79882338064'] |
| ['Комаров Сергей']                  | ['79879550000'] |
| ['Канеева Ильнура Ибрагимовна']     | ['79876179276'] |
| ['Петлин Андрей']                   | ['79874045682'] |
| ['Саломаткин Александр Сергеевич']  | ['79873834812'] |
| ['Емельяненко Сергей Вячеславович'] | ['79872988841'] |
| ['Синицын Денис Юрьевич']           | ['79871081453'] |
| ['Багдасаровна Анна Акоповна']      | ['79853836959'] |
| ['Машков Феддор Анатольевич']       | ['79853805018'] |
| ['Лаптев Александр']                | ['79853610454'] |
| ['Копылов Евгений Вячеславович']    | ['79853379254'] |
| ['Горелов Анатолий Александрович']  | ['79852277036'] |
| ['Андросов Никита']                 | ['79851990226'] |
```