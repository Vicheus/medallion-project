# Parsetron results

## About row data

> - Code name: index_0359
> - File path: users_preprocessed.csv
> - Total rows: 742159

### Schema
```
root
 |-- firstName: string (nullable = true)
 |-- secondName: string (nullable = true)
 |-- lastName: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- yearOfBirth: integer (nullable = true)

```

### Data sample
```
| firstName   | secondName   | lastName    | email                    | phone          |   yearOfBirth |
|:------------|:-------------|:------------|:-------------------------|:---------------|--------------:|
| Алла        | Потаповна    | Мельникова  | super@opnscl.ru          | (68) 0590-9661 |           nan |
| Симонов     | Саныч        | Сергей      | syhauzab@yomail.info     |                |           nan |
| Александра  |              | Иванова     |                          |                |           nan |
| Василий     |              | Иванов      |                          |                |           nan |
| Влад        | Сергеевич    | Римошевский | taobdemb@10mail.org      |                |           nan |
| Михаил      | Петросович   | Овсепян     | twjwczofefee@dropmail.me |                |           nan |
| Олег        | Олегович     | Олего       | twjwczofefee@dropmail.me | +79629695802   |          1999 |
| серго       | сергеевич    | сергей      |                          |                |           nan |
| Алевтина    | Маргеловна   | Иванова     | jsdujktab@emlhub.com     |                |           nan |
| Хе          | Су           | Хан         | twiaiwoisdey@dropmail.me |                |           nan |
| Олег        | Комплексович | Эдипов      | sjfpfotn@yomail.info     |                |           nan |
| Ахмат       | Рамзанович   | Ходоренко   | ofywiptab@emlhub.com     |                |           nan |
| Учитель     | Олегович     | Второй      | jfygpwbbb@emlpro.com     |                |           nan |
| Имя         | Отчество     | Фамилия     | ya@ya.ru                 |                |           nan |
| Хе          | Су           | Хан         | ya1@ya.ru                |                |           nan |
| Дмитрий     | Игоревич     | Смирнов     | kbkfvnpbb@emlpro.com     |                |           nan |
| Адам        | Мусхутович   | Гончаренко  | lubbgfhbb@emlhub.com     | 123456789      |          1999 |
| Мария       | Георгиевна   | Фомина      | super@me.ru              |                |           nan |
| Закван      | Вячеславович | Гайнуллин   | head@me.ru               |                |           nan |
| Учитель     | Андреевич    | Скинтеев    | dis.tortriver@gmail.com  |                |           nan |
```


## About final data
> - Total rows: 226490

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 94.41% |
| Phones | 38.51% |



### Data sample
```
| names                                | emails                      | phones          |
|:-------------------------------------|:----------------------------|:----------------|
| ['Мельникова Алла Потаповна']        | ['super@opnscl.ru']         |                 |
| ['Сергей Симонов Саныч']             | ['syhauzab@yomail.info']    |                 |
| ['Римошевский Влад Сергеевич']       | ['taobdemb@10mail.org']     |                 |
| ['Олего Олег Олегович']              |                             | ['79629695802'] |
| ['Иванова Алевтина Маргеловна']      | ['jsdujktab@emlhub.com']    |                 |
| ['Эдипов Олег Комплексович']         | ['sjfpfotn@yomail.info']    |                 |
| ['Ходоренко Ахмат Рамзанович']       | ['ofywiptab@emlhub.com']    |                 |
| ['Второй Учитель Олегович']          | ['jfygpwbbb@emlpro.com']    |                 |
| ['Хан Хе Су']                        | ['ya1@ya.ru']               |                 |
| ['Смирнов Дмитрий Игоревич']         | ['kbkfvnpbb@emlpro.com']    |                 |
| ['Гончаренко Адам Мусхутович']       | ['lubbgfhbb@emlhub.com']    |                 |
| ['Фомина Мария Георгиевна']          | ['super@me.ru']             |                 |
| ['Гайнуллин Закван Вячеславович']    | ['head@me.ru']              |                 |
| ['Скинтеев Учитель Андреевич']       | ['dis.tortriver@gmail.com'] |                 |
| ['Скинтеев Ответственный Андреевич'] | ['distort.river@gmail.com'] |                 |
| ['Торопов Иван']                     | ['toropov@jetstyle.ru']     |                 |
| ['Сидоров Петр Сергеевич']           | ['sidorov@gmail.com']       |                 |
| ['Дынькова Людмила Викторовна']      | ['logos25@yandex.ru']       |                 |
| ['Филоненко Владимир Игоревич']      | ['79825679297@yandex.ru']   |                 |
| ['Плешкова Оксана Николаевна']       | ['oks200803@mail.ru']       |                 |
```