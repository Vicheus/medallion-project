# Parsetron results

## About row data

> - Code name: index_0335
> - File path: urok.1c.ru_01_2023.txt
> - Total rows: 185555

### Schema
```
root
 |-- Имя: string (nullable = true)
 |-- Фамилия: string (nullable = true)
 |-- Почта: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- Отчество: string (nullable = true)

```

### Data sample
```
| Имя       | Фамилия   | Почта                             |   Номер телефона | Отчество      |
|:----------|:----------|:----------------------------------|-----------------:|:--------------|
| Александр |           | aledem@rarus.ru                   |                  |               |
| Дарья     |           | dd@rarus.ru                       |                  |               |
| Наталья   | Лебедева  | lebn@1c.ru                        |                  |               |
| Виталий   | Мельник   | vitali@rarus.ru                   |                  |               |
| Евгений   | Брагин    | bragev@rarus.ru                   |      74444444444 | Александрович |
|           |           | 78432121357@repetitor.1c.ru       |      78432121357 |               |
|           |           | 71251251255@urok.1c.ru            |      71251251255 |               |
|           |           | 76125151221@urok.1c.ru            |      76125151221 |               |
|           |           | 71361612413@urok.1c.ru            |      71361612413 |               |
|           |           | 72415125125@urok.1c.ru            |      72415125125 |               |
|           |           | 75121512424@urok.1c.ru            |      75121512424 |               |
|           |           | 71251251251@urok.1c.ru            |      71251251251 |               |
|           |           | 76231261236@dmitrd.urok.rrsdev.ru |      76231261236 |               |
|           |           | 79629699271@dmitrd.urok.rrsdev.ru |      79629699271 |               |
|           |           | 74845168545@dmitrd.urok.rrsdev.ru |      74845168545 |               |
|           |           | 72421412412@dmitrd.urok.rrsdev.ru |      72421412412 |               |
|           |           | fdfsf@esfsd.sdf                   |                  | Test 3        |
|           |           | fewf@dsf.sdfs                     |                  | Test 3        |
|           |           | sdf@sdf.sf                        |                  | Test 3        |
|           |           | dfdzf@asdasd.ad                   |                  | Test 3        |
```


## About final data
> - Total rows: 180617

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
| Emails | 100.00% |
| Phones | 3.65% |


### Data sample
```
| names                                | emails                           | phones          |
|:-------------------------------------|:---------------------------------|:----------------|
| ['Кошкин Андрей Фёдорович']          | ['akoshkin19@mail.ru']           | ['79212210150'] |
| ['Фокина Ирина Александровна']       | ['79156787986@urok.1c.ru']       | ['79156787986'] |
| ['Крамаренко Матвей Алексеевич']     | ['kozhuhova88@mail.ru']          | ['79806352125'] |
| ['Абдурахманова Зифа Мансуровна']    | ['79527810656@mail.ru']          | ['79200529112'] |
| ['Волобуева Амелия Михайловна']      | ['reloading@inbox.ru']           | ['79140335270'] |
| ['Павлюков Артем Сергеевич']         | ['artm.pavlyukov@mail.ru']       | ['79108566895'] |
| ['Золотавина Злата Александровна']   | ['zlatazolotavina@gmail.com']    | ['79220081815'] |
| ['Шленчак Виктория Валентиновна']    | ['evlahin@list.ru']              | ['79216929040'] |
| ['Сандова Виктория Владиславовна']   | ['vikasan-2@mail.ru']            | ['79088882573'] |
| ['Маханенков Арсений Сергеевич']     | ['amahanenkov053@gmail.com']     | ['79107351128'] |
| ['Гришина Валентина Владимировна']   | ['grishina.val3ntyna@yandex.ru'] | ['79834664445'] |
| ['Шамсетдинов Ильдар Агзамович']     | ['shams64@mail.ru']              | ['79273043904'] |
| ['Пелигарова Татьяна Анатольевна']   | ['pelitatana2@gmail.com']        | ['79514274028'] |
| ['Гришина Виктория Александровна']   | ['ludmilagrishina318@gmail.com'] | ['79806727978'] |
| ['Дуйдов Егор Сергеевич']            | ['viktoria.dujjdova@yandex.ru']  | ['79197524419'] |
| ['Вилкова Елена Юрьевна']            | ['vilkovaelena.bal@mail.ru']     | ['79271523619'] |
| ['Чащин Егор Владимирович']          | ['chaschin.eg@yandex.ru']        | ['79024255905'] |
| ['Савельев Александр Александрович'] | ['saha.saveljew@yandex.ru']      | ['79271242035'] |
| ['Сергеева Полина Руслановна']       | ['polina_sergeeva_2008@list.ru'] | ['79081292044'] |
| ['Кулакова Екатерина Олеговна']      | ['katakulakova@gmail.com']       | ['79126098938'] |
```