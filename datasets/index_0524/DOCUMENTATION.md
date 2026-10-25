# Parsetron results

## About row data

> - File path: medicenter_2024.csv
> - Total rows: 112100

### Schema
```
root
 |-- med_users_name: string (nullable = true)
 |-- med_users_email: string (nullable = true)
 |-- med_users_phone: string (nullable = true)

```

### Data sample
```
| med_users_name                 | med_users_email              | med_users_phone    |
|:-------------------------------|:-----------------------------|:-------------------|
| ЯЯковлева Ольга Леонидовна     | <blank>                      | +7 (919) 554-93-26 |
| Ящук Елена Анатольевна         | cab206@mail.ru               | +7 (921) 999-22-82 |
| Ящук Ева Кирилловна            | <blank>                      | +7 (963) 324-57-06 |
| ЯЩИНКО ДИАНА АЛЕКСЕЕВНА        | dianka.konushckina@yandex.ru | +7 (953) 632-59-18 |
| Ящинко Диана Алексеевна        | <blank>                      | +7 (911) 276-51-95 |
| Ященкова Марина Юрьевна        | kashino_20_01@mail.ru        | +7 (911) 918-11-40 |
| Ященкова Марина Юрьевна        | <blank>                      | +7 (981) 904-32-36 |
| Ященко Наталья Алексеевна      | nataceverynka2@gmail.com     | +7 (981) 741-31-55 |
| Ященко Виктория Александровна  | Vikazhukova7@gmail.com       | +7 (928) 376-32-26 |
| Ященко Анна Владимировна       | annmaks.invest@gmail.com     | +7 (905) 271-10-30 |
| Ященко Алина Васильевна        | <blank>                      | +7 (962) 704-27-24 |
| Ященко Александр Александрович | <blank>                      | +7 (911) 772-66-35 |
| Яшунский  А.В.                 | darthfduch@yandex.ru         | +7 (931) 256-67-97 |
| Яшновская Екатерина Андреевна  | pyatnica.e@bk.ru             | +7 (977) 510-11-73 |
| Яшкова                         | <blank>                      | +7 (911) 276-07-01 |
| Яшкина Юлия Юрьевна            | jyashkina@abz-1.ru           | +7 (921) 550-58-03 |
| Яшкина Виктория Юрьевна        | vikayashkina1990@gmail.com   | +7 (911) 179-32-13 |
| Яшкина Анна                    | <blank>                      | +7 (921) 402-21-41 |
| Яшина Александра Сергеевна     | <blank>                      | +7 (950) 041-85-46 |
| Яшин Павел Иванович            | pavelrus91@mail.ru           | +7 (981) 127-36-77 |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 45.82% |
| Phones | 98.55% |



### Data sample
```
| names                             | emails                          | phones          |
|:----------------------------------|:--------------------------------|:----------------|
| ['Янталева Евгения Витальевна']   | ['yantaleva89@mail.ru']         | ['79818621412'] |
| ['Янковская София Викторовна']    | ['sonivov1999@icloud.com']      | ['79516466916'] |
| ['Янина']                         | ['yaninaspb@mail.ru']           | ['79213150101'] |
| ['Яковлева Полина']               | ['polinajackson0510@gmail.com'] | ['79119069680'] |
| ['Яковенко Яна Юрьевна']          | ['yana_solnechnaya@mail.ru']    | ['79819529771'] |
| ['Юлия']                          | ['ulia.zzz@mail.ru']            | ['79215820165'] |
| ['Юдина Нина Петровна']           | ['ninochka-yudina@yandex.ru']   | ['79062747767'] |
| ['Эльзара']                       | ['elza.kahrimanova@yandeks.ru'] | ['79119091263'] |
| ['Элеонора']                      | ['holova@yandex.ru']            | ['79217523267'] |
| ['Элеонора']                      | ['renata8787@mail.ru']          | ['79214267637'] |
| ['Шишканов Артем Дмитриевич']     | ['shishkanova1@mail.ru']        | ['79134931385'] |
| ['Шарманджиева']                  | ['scharmanjiewa@yandex.ru']     | ['79413206885'] |
| ['Шальнова Любовь Александровна'] | ['dmitry135@mail.ru']           | ['79052587994'] |
| ['Чухнов Даниил Витальевич']      | ['limoncheg22@yandex.ru']       | ['79138451428'] |
| ['Чурганова Наталья']             | ['ladysandal@yandex.ru']        | ['79219691904'] |
| ['Чупров Виталий Владимирович']   | ['vanesdven@gmail.com']         | ['79312414511'] |
| ['Чикунова Анна Владимировна']    | ['anyachikunova@yandex.ru']     | ['79686638885'] |
| ['Червонная Ольга Владимировна']  | ['nicerin@yandex.ru']           | ['79117567309'] |
| ['Чакканбаева Элина Фяритовна']   | ['salivajke@gmail.com']         | ['79650534044'] |
| ['Цуркану Динара Викторовна']     | ['dinara.doneva@gmail.com']     | ['79677725961'] |
```