# Parsetron results

## About row data

> - Code name: index_0349
> - File path: заказы_respect_shoes_19_04_2022.csv
> - Total rows: 103161

### Schema
```
root
 |-- Электронная почта: string (nullable = true)
 |-- ФИО: string (nullable = true)
 |-- Телефон: string (nullable = true)

```

### Data sample
```
| Электронная почта                      | ФИО                         |     Телефон |
|:---------------------------------------|:----------------------------|------------:|
| pavel-pasha-ivanov-1991-ivanov@mail.ru | Павел                       | 79101427404 |
| chistova.elv@yaroslavl.gazprom-neft.ru | Елена                       |             |
| anastasia.savitskaya@bakermckenzie.com | Анастасия                   |             |
| kolesnikova.tatiana/yurievna@gmail.com | Колесникова Татьяна Юрьевна |             |
| kokorina_alena_kokorina_alena@mail.ru  | Маралина Ю.в.               |             |
| Elena.Sviderskaya@novokuznetsk.sns.ru  | Елена                       |             |
| Natalya.Panchenco@hals-development.ru  | Наталья                     | 79166332308 |
| Tatiana.Deminashvili@interprombank.ru  | Татьяна                     | 79031529731 |
| anastasiya.pahomova@aksioma-group.com  | Пахомова А.е.               |             |
| dinara.sadekova@ru.manpowergroup.com   | Алексей                     |             |
| ekaterina.prockopchuck1991@yandex.ru   | Екатерина                   |             |
| TATYANA.M.KHOROSHAVINA@Raiffeisen.ru   | Хорошавина Т.м.             |             |
| ekaterina.zavorina@lafargeholcim.com   | Екатерина                   |             |
| katya-ekaterina-ivanova-1988@mail.ru   | Екатерина Иванова           | 79647026620 |
| alexander_osobenny_voronezh@maul.ru    | Александр                   | 79304173417 |
| andreevaanastasiaolegovna@gmail.com    | Anastasia                   |             |
| evgeniya.poletikina@crediteurope.ru    | Полетыкина Евгения Игоревна |             |
| viktoriyaalbrant1998.2015@gmail.com    | Виктория                    | 79139189164 |
| karpenko.talochka@yandex.ru15120410    | Наталия Аркадьевна          | 79258845781 |
| Twins-tatyana.sharanihina@yandex.ru    | Татьяна                     |             |
```


## About final data
> - Total rows: 101661

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
| Emails | 99.98% |
| Phones | 19.74% |



### Data sample
```
| names                           | emails                                     | phones          |
|:--------------------------------|:-------------------------------------------|:----------------|
| ['Павел']                       | ['pavel-pasha-ivanov-1991-ivanov@mail.ru'] | ['79101427404'] |
| ['Елена']                       | ['chistova.elv@yaroslavl.gazprom-neft.ru'] |                 |
| ['Анастасия']                   | ['anastasia.savitskaya@bakermckenzie.com'] |                 |
| ['Маралина Ю.В.']               | ['kokorina_alena_kokorina_alena@mail.ru']  |                 |
| ['Елена']                       | ['elena.sviderskaya@novokuznetsk.sns.ru']  |                 |
| ['Наталья']                     | ['natalya.panchenco@hals-development.ru']  | ['79166332308'] |
| ['Татьяна']                     | ['tatiana.deminashvili@interprombank.ru']  | ['79031529731'] |
| ['Пахомова А.Е.']               | ['anastasiya.pahomova@aksioma-group.com']  |                 |
| ['Алексей']                     | ['dinara.sadekova@ru.manpowergroup.com']   |                 |
| ['Екатерина']                   | ['ekaterina.prockopchuck1991@yandex.ru']   |                 |
| ['Хорошавина Т.М.']             | ['tatyana.m.khoroshavina@raiffeisen.ru']   |                 |
| ['Екатерина']                   | ['ekaterina.zavorina@lafargeholcim.com']   |                 |
| ['Екатерина Иванова']           | ['katya-ekaterina-ivanova-1988@mail.ru']   | ['79647026620'] |
| ['Александр']                   | ['alexander_osobenny_voronezh@maul.ru']    | ['79304173417'] |
| ['Anastasia']                   | ['andreevaanastasiaolegovna@gmail.com']    |                 |
| ['Полетыкина Евгения Игоревна'] | ['evgeniya.poletikina@crediteurope.ru']    |                 |
| ['Виктория']                    | ['viktoriyaalbrant1998.2015@gmail.com']    | ['79139189164'] |
| ['Наталия Аркадьевна']          | ['karpenko.talochka@yandex.ru15120410']    | ['79258845781'] |
| ['Татьяна']                     | ['twins-tatyana.sharanihina@yandex.ru']    |                 |
| ['Александра']                  | ['aleksandra.alekseevna.1990@list.ru']     | ['79067139760'] |
```