# Parsetron results

## About row data

> - Code name: index_0568
> - File path: aravia_ru.csv
> - Total rows: 166051

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- NAME: string (nullable = true)
 |-- SECOND_NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- PERSONAL_PHONE: string (nullable = true)
 |-- XML_ID: string (nullable = true)
 |-- PERSONAL_BIRTHDAY: string (nullable = true)

```

### Data sample
```
|   ID | NAME               | SECOND_NAME   | LAST_NAME   | EMAIL                        |   PERSONAL_PHONE | XML_ID                                   | PERSONAL_BIRTHDAY   |
|-----:|:-------------------|:--------------|:------------|:-----------------------------|-----------------:|:-----------------------------------------|:--------------------|
|    3 | Марина             |               | Морозова    | morozova.m@aravia-prof.ru    |                  | 3#morozova.m@aravia-prof.ru#Морозова Мар |                     |
|    4 |                    |               |             | hmelevskaya.a@aravia-prof.ru |                  |                                          |                     |
|    6 |                    |               |             | 1c-user@aravia-prof.ru       |                  |                                          |                     |
|    7 | Ксения             |               | Истомина    | kseniya.i@aravia-prof.ru     |                  | 7#kseniya.i@aravia-prof.ru#              |                     |
|   21 |                    |               |             | konovalov@thelh.net          |      79123334313 | 21#konovalov@thelh.net#                  |                     |
|   29 | shichkin@thelh.net |               |             | shichkin@thelh.net           |                  | 29#shichkin@thelh.net#                   |                     |
|   33 | Ксения             |               | Истомина    | bk87@mail.ru                 |      79260566548 | 33#bk87@mail.ru# Ксения                  |                     |
|   34 |                    |               |             | e.roux@trackad.ai            |      77916999454 |                                          |                     |
|   39 | Марина             |               |             | vol4ica87@mail.ru            |      79104299631 | 39#vol4ica87@mail.ru# Марина             |                     |
|   40 |                    |               |             | v@gmail.com                  |      79101111111 |                                          |                     |
|   41 | sophio             |               |             | sophiochkadua@gmail.com      |     995593256336 |                                          |                     |
|   48 | anastasia.kr       |               |             | anastasia.kr@aravia-prof.ru  |                  |                                          |                     |
|   49 | Анастасия          | Алексеевна    | Сидорина    | sidorina.a@aravia-prof.ru    |      79153850914 |                                          |                     |
|   50 |                    |               |             | voloshina.k@aravia-prof.ru   |                  |                                          |                     |
|   54 | Яна                |               | Петрова     | iurii.sh@aravia-prof.ru      |      96895565635 |                                          |                     |
|   55 |                    |               |             | fedotova.v@aravia-prof.ru    |                  |                                          |                     |
|   56 | Руслан             | Викторович    | Жданов      | ruslan.z@aravia-prof.ru      |      79104453144 | 56#ruslan.z@aravia-prof.ru#Жданов Жданов |                     |
|   57 | Наталья            |               | Курбатова   | kisik2@rambler.ru            |       9055460979 |                                          |                     |
|   58 | Оксана             |               | Борцова     | oksaris@mail.ru              |      79168435040 |                                          |                     |
|   59 | Елена              | Замировна     | Сабирова    | meridum@list.ru              |      79852147061 |                                          |                     |
```


## About final data
> - Total rows: 163919

### Schema
```
root
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Emails | 99.94% |
| Phones | 91.52% |
| Names | 100.00% |
| Birth_date | 10.53% |



### Data sample
```
| emails                       | phones          | names                              | birth_date   |
|:-----------------------------|:----------------|:-----------------------------------|:-------------|
| ['0101ir@mail.ru']           | ['79637133313'] | ['Сокуренко Ирина Николаевна']     |              |
| ['0393737@mail.ru']          | ['79250393737'] | ['Каморкина Анна Юрьевна']         |              |
| ['13_375@list.ru']           | ['79260361320'] | ['Сидорова Екатерина Андреевна']   |              |
| ['1991yulchik@mail.ru']      | ['79102056214'] | ['Ломакина Юлия Сергеевна']        |              |
| ['1995duck@mail.ru']         |                 | ['Джумабекова Сания Сериковна']    |              |
| ['2131280@mail.ru']          | ['79139851280'] | ['Алексеева Дина Евгеньевна']      |              |
| ['27041998@inbox.ru']        | ['79152271365'] | ['Антипкина Анна Александровна']   |              |
| ['358791010077842@mail.ru']  | ['79999706522'] | ['Бабина Екатерина Олеговна']      |              |
| ['4eburashka_93@mail.ru']    | ['79160536716'] | ['Рахмонов Фирдавс Манонович']     |              |
| ['6fit@mail.ru']             |                 | ['Романова Кристина Игоревна']     | 28.06.1999   |
| ['75marina@mail.ru']         | ['79262452591'] | ['Бондарчук Марина Евгеньевна']    |              |
| ['7877613@mail.ru']          | ['79037784264'] | ['Кузьмина Елена Алексеевна']      |              |
| ['79505046302@yandex.ru']    | ['79199329940'] | ['Перевозкина Анна Алексеевна']    | 31.12.1991   |
| ['81marina1@mail.ru']        | ['79533934185'] | ['Белоусова Марина Сергеевна']     |              |
| ['89284472144ira@gmail.com'] | ['79299084321'] | ['Данилова Ирина Валентиновна']    |              |
| ['9057064307@mail.ru']       | ['79057064307'] | ['Алла Алла Сергеевна']            |              |
| ['9211935099@mail.ru']       | ['79211935099'] | ['Никитенко Наталья Владимировна'] |              |
| ['9295074088@mail.ru']       | ['79031301134'] | ['Борщева Кристина']               |              |
| ['9657650@mail.ru']          | ['79299657650'] | ['Голубева Елена Михайловна']      |              |
| ['9926081@mail.ru']          | ['79199926081'] | ['Щербакова Олеся Анатольевна']    |              |
```