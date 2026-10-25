# Parsetron results

## About row data

> - Code name: index_0299
> - File path: /media/user/SAMSUNG/Databases/index_0299/raw/glavkniga.ru.txt
> - Total rows: 23201

### Schema
```
root
 |-- Почта: string (nullable = true)
 |-- Номер телефона: string (nullable = true)
 |-- Имя: string (nullable = true)

```

### Data sample
```
| Почта                     |   Номер телефона | Имя       |
|:--------------------------|-----------------:|:----------|
| moiseira@yandex.ru        |      79383436588 | Ирина     |
| liliy.kl@mail.ru          |      79067547956 | Лилия     |
| olg-maje1@yandex.ru       |      79085031984 | Ольга     |
| apis54@mail.ru            |      79060818790 | Владимир  |
| VB02121975@yandex.ru      |      79610005946 | Юлия      |
| irina-vish@mail.ru        |      79038491843 | Ирина     |
| vinikada@yandex.ru        |      79141591565 | виктор    |
| office@boulder-loaders.ru |      79940129645 | Татьяна   |
| melnikov300684@mail.ru    |      79627986123 | Екатерина |
| elena-dmitrieva@bk.ru     |      79149032946 | Елена     |
| irkamih@rambler.ru        |      79029436256 | ирина     |
| nata-mez@mail.ru          |      79151457692 | Наталья   |
| sheu@nasha-tema.tv        |      79529012919 | Алена     |
| apple-room.glbux@mail.ru  |      79650384686 | Марина    |
| Resinna@list.ru           |      79504880876 | Инна      |
| ekaterina-s7@rambler.ru   |      79183401827 | Екатерина |
| jkmuf0907@rambler.ru      |      79051910009 | Ольга     |
| mar1368@mail.ru           |      79277799944 | Марина    |
| korbero@ya.ru             |      79023617225 | Екатерина |
| juliapt@mail.ru           |      78129972247 | PP        |
```


## About final data
> - Total rows: 22941

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
```
{
    "names": 100.0,
    "emails": 99.98,
    "phones": 99.45
}
```

### Data sample
```
| names                   | emails                              | phones          |
|:------------------------|:------------------------------------|:----------------|
| ['Татьяна']             | ['tg197401@mail.ru']                | ['79091786451'] |
| ['Урал Рамазанович']    | ['pred.soveta-krop@yandex.ru']      | ['79124032103'] |
| ['Вячеслав']            | ['dyatlovv@gmail.com']              | ['79163189184'] |
| ['Алекс']               | ['177trof@mail.ru']                 | ['79851431977'] |
| ['Анна']                | ['petr198812@gmail.com']            | ['79198054252'] |
| ['Инна']                | ['tagir1712@mail.ru']               | ['79095672945'] |
| ['Ольга']               | ['olga_shappo@mail.ru']             | ['79035300617'] |
| ['Наталья']             | ['kozyrev-n@yandex.ru']             | ['79267276777'] |
| ['Наталья']             | ['z_modem@mail.ru']                 | ['79254433385'] |
| ['Наталья']             | ['n.gubina0130@mail.ru']            | ['79621003796'] |
| ['Сергеева Елена']      | ['sergeevae2008@yandex.ru']         | ['79267821782'] |
| ['Наталья']             | ['pigasik67@gmail.om']              | ['79529966515'] |
| ['Татьяна']             | ['lvovatv@mail.ru']                 | ['79247043557'] |
| ['Елена']               | ['elena.kadirlieva@energostroy.ru'] | ['79119516021'] |
| ['Дарья']               | ['d.ids@mail.ru']                   | ['79112737522'] |
| ['Евгения']             | ['pen999@mail.ru']                  | ['79122230820'] |
| ['O.Sayapinain-Tex.Ru'] | ['o.sayapina@in-tex.ru']            | ['79161345046'] |
| ['Алиса']               | ['kirilinaalisa@yandex.ru']         | ['79065445777'] |
| ['Марина Матвеева']     | ['mar.avramenko2010@yandex.ru']     | ['79685286750'] |
| ['Татьяна']             | ['tpafonina@yandex.ru']             | ['79219122281'] |
```