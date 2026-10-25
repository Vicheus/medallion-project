# Parsetron results

## About row data

> - Code name: index_0518
> - File path: ru_business_persons.csv
> - Total rows: 2489342

### Schema
```
root
 |-- name: string (nullable = true)
 |-- title: string (nullable = true)
 |-- company: string (nullable = true)
 |-- b_phone: string (nullable = true)
 |-- b_email: string (nullable = true)

```

### Data sample
```
| name                                | title                                                            | company                                                                                                                                                  | b_phone       | b_email            |
|:------------------------------------|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|:-------------------|
| Mr Evgengii Aleksandrovich Shikanov | Chairman of the Liquidation Commission                           | Llc Csc -Metrologia                                                                                                                                      | +7 9857628245 | eshikanov@mail.ru  |
| Mr Mikhail Petrovich Nikolaev       | Technical Director                                               | Ecodor Co. Ltd.                                                                                                                                          | +7 4991877818 | info@ecodor.ru     |
| Mr Vitalii Gennadyevich Meshchanov  | Director of |nternational Business                               | Otkrytoe Aktsionernoe Obshchestvo Vserossiiskii Nauchno-Issledovatelskii, Proektno-Konstruktorskii I Tekhnologicheskii Institut Kabelnoi Promyshlennosti | +7 4953622513 | vniikp@vniikp.ru   |
| Ms Elena Nikolaevna Klimova         | First Deputy General Director                                    | Joint Stock Foreign Trade Company Exima                                                                                                                  | +7 4956902480 | info@exima.ru      |
| Ms Elena Vladimirovna Larchenko     | Other Official                                                   | Promavtokontrakt                                                                                                                                         | +7 4959610072 | moscow@promavto.ru |
| Mr Mikhail Semenovich Lashchenov    | Chairman of the Board of Directors                               | Jsc Stroyenergogroup                                                                                                                                     | +7 4999723841 | mechal2006@mail.ru |
| Mr Evgenii Vadimovich Savostyanov   | Member of board of directors; Chairman of the Board of Directors | Sistema Mass-Media Joint Stock Company                                                                                                                   | +7 4952296363 | office@smm.ru      |
| Mr Grigorii Yuryevich Sukhov        | Vice President for Finance and Investment                        | Sistema Mass-Media Joint Stock Company                                                                                                                   | +7 4952296363 | office@smm.ru      |
| Mr Denis Klimentyevich Pak          | Supervisory Board Member                                         | Otkrytoe Aktsionernoe Obshchestvo Innovatsionnyi Nauchno-Proizvodstvennyi Tsentr Tekstilnoi I Legkoi Promyshlennosti                                     | +7 9166089367 | info@inpctlp.ru    |
| Ms Nadezhda Aleksandrovna Kim       | Supervisory Board Member                                         | Otkrytoe Aktsionernoe Obshchestvo Innovatsionnyi Nauchno-Proizvodstvennyi Tsentr Tekstilnoi I Legkoi Promyshlennosti                                     | +7 9166089367 | info@inpctlp.ru    |
| Mr Grigorii Isakovich Dubinovskii   | Supervisory Board Member                                         | Aktsionernoe Obshchestvo Butovskii Kombinat                                                                                                              | +7 4957127188 | bkbutovo@mail.ru   |
| Mr Igor Aleksandrovich Kamenskoy    | Chairman (Investment Committee)                                  | Federal Grid Company of Unified Energy System , Joint-Stock Company ( Fgc Ues , Jsc)                                                                     | +7 4957105208 | lpmes@lpmes.ru     |
| Mr Oleg Yuryevich Isaev             | Member (Strategy Committee)                                      | Federal Grid Company of Unified Energy System , Joint-Stock Company ( Fgc Ues , Jsc)                                                                     | +7 4957105208 | lpmes@lpmes.ru     |
| Mr Egor Vyacheslavovich Prokhorov   | Director (Board of Directors)                                    | Federal Grid Company of Unified Energy System , Joint-Stock Company ( Fgc Ues , Jsc)                                                                     | +7 4957105208 | lpmes@lpmes.ru     |
| Ms Svetlana Aleksandrovna Balaeva   | Member (Investment Committee)                                    | Federal Grid Company of Unified Energy System , Joint-Stock Company ( Fgc Ues , Jsc)                                                                     | +7 4957105208 | lpmes@lpmes.ru     |
| Viktor Korneyevich Yavorsky         | Member (Strategy Committee)                                      | Federal Grid Company of Unified Energy System , Joint-Stock Company ( Fgc Ues , Jsc)                                                                     | +7 4957105208 | lpmes@lpmes.ru     |
| Mr Roman Yevgenyevich Filimonov     | First Deputy Chairman, Management Board                          | Federal Grid Company of Unified Energy System , Joint-Stock Company ( Fgc Ues , Jsc)                                                                     | +7 4957105208 | lpmes@lpmes.ru     |
| Mr Pavel Anatolyevich Livinskii     | Chairman (Strategy Committee)                                    | Federal Grid Company of Unified Energy System , Joint-Stock Company ( Fgc Ues , Jsc)                                                                     | +7 4957105208 | lpmes@lpmes.ru     |
| Mr Sergey Terebulin                 | Deputy Chairman (Management Board)                               | Federal Grid Company of Unified Energy System , Joint-Stock Company ( Fgc Ues , Jsc)                                                                     | +7 4957105208 | lpmes@lpmes.ru     |
| Ms Oksana Vladimirovna Shatokhina   | Member (Strategy Committee)                                      | Federal Grid Company of Unified Energy System , Joint-Stock Company ( Fgc Ues , Jsc)                                                                     | +7 4957105208 | lpmes@lpmes.ru     |
```


## About final data
> - Total rows: 2488114

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)

```



### Data sample
```
| names                                | phones          | emails                 | works                                                                                                                                                                                                                                                                          |
|:-------------------------------------|:----------------|:-----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Evgengii Aleksandrovich Shikanov'] | ['79857628245'] | ['eshikanov@mail.ru']  | [Row(post='Chairman of the Liquidation Commission', date_start=None, date_end=None, company='Llc Csc -Metrologia', address=None, comment=None)]                                                                                                                                |
| ['Mikhail Petrovich Nikolaev']       | ['74991877818'] | ['info@ecodor.ru']     | [Row(post='Technical Director', date_start=None, date_end=None, company='Ecodor Co. Ltd.', address=None, comment=None)]                                                                                                                                                        |
| ['Vitalii Gennadyevich Meshchanov']  | ['74953622513'] | ['vniikp@vniikp.ru']   | [Row(post='Director of nternational Business', date_start=None, date_end=None, company='Otkrytoe Aktsionernoe Obshchestvo Vserossiiskii Nauchno-Issledovatelskii Proektno-Konstruktorskii I Tekhnologicheskii Institut Kabelnoi Promyshlennosti', address=None, comment=None)] |
| ['Elena Nikolaevna Klimova']         | ['74956902480'] | ['info@exima.ru']      | [Row(post='First Deputy General Director', date_start=None, date_end=None, company='Joint Stock Foreign Trade Company Exima', address=None, comment=None)]                                                                                                                     |
| ['Elena Vladimirovna Larchenko']     | ['74959610072'] | ['moscow@promavto.ru'] | [Row(post='Other Official', date_start=None, date_end=None, company='Promavtokontrakt', address=None, comment=None)]                                                                                                                                                           |
| ['Mikhail Semenovich Lashchenov']    | ['74999723841'] | ['mechal2006@mail.ru'] | [Row(post='Chairman of the Board of Directors', date_start=None, date_end=None, company='Jsc Stroyenergogroup', address=None, comment=None)]                                                                                                                                   |
| ['Evgenii Vadimovich Savostyanov']   | ['74952296363'] | ['office@smm.ru']      | [Row(post='Member of board of directors Chairman of the Board of Directors', date_start=None, date_end=None, company='Sistema Mass-Media Joint Stock Company', address=None, comment=None)]                                                                                    |
| ['Grigorii Yuryevich Sukhov']        | ['74952296363'] | ['office@smm.ru']      | [Row(post='Vice President for Finance and Investment', date_start=None, date_end=None, company='Sistema Mass-Media Joint Stock Company', address=None, comment=None)]                                                                                                          |
| ['Denis Klimentyevich Pak']          | ['79166089367'] | ['info@inpctlp.ru']    | [Row(post='Supervisory Board Member', date_start=None, date_end=None, company='Otkrytoe Aktsionernoe Obshchestvo Innovatsionnyi Nauchno-Proizvodstvennyi Tsentr Tekstilnoi I Legkoi Promyshlennosti', address=None, comment=None)]                                             |
| ['Nadezhda Aleksandrovna Kim']       | ['79166089367'] | ['info@inpctlp.ru']    | [Row(post='Supervisory Board Member', date_start=None, date_end=None, company='Otkrytoe Aktsionernoe Obshchestvo Innovatsionnyi Nauchno-Proizvodstvennyi Tsentr Tekstilnoi I Legkoi Promyshlennosti', address=None, comment=None)]                                             |
| ['Grigorii Isakovich Dubinovskii']   | ['74957127188'] | ['bkbutovo@mail.ru']   | [Row(post='Supervisory Board Member', date_start=None, date_end=None, company='Aktsionernoe Obshchestvo Butovskii Kombinat', address=None, comment=None)]                                                                                                                      |
| ['Igor Aleksandrovich Kamenskoy']    | ['74957105208'] | ['lpmes@lpmes.ru']     | [Row(post='Chairman Investment Committee', date_start=None, date_end=None, company='Federal Grid Company of Unified Energy System Joint-Stock Company Fgc Ues Jsc', address=None, comment=None)]                                                                               |
| ['Oleg Yuryevich Isaev']             | ['74957105208'] | ['lpmes@lpmes.ru']     | [Row(post='Member Strategy Committee', date_start=None, date_end=None, company='Federal Grid Company of Unified Energy System Joint-Stock Company Fgc Ues Jsc', address=None, comment=None)]                                                                                   |
| ['Egor Vyacheslavovich Prokhorov']   | ['74957105208'] | ['lpmes@lpmes.ru']     | [Row(post='Director Board of Directors', date_start=None, date_end=None, company='Federal Grid Company of Unified Energy System Joint-Stock Company Fgc Ues Jsc', address=None, comment=None)]                                                                                 |
| ['Svetlana Aleksandrovna Balaeva']   | ['74957105208'] | ['lpmes@lpmes.ru']     | [Row(post='Member Investment Committee', date_start=None, date_end=None, company='Federal Grid Company of Unified Energy System Joint-Stock Company Fgc Ues Jsc', address=None, comment=None)]                                                                                 |
| ['Viktor Korneyevich Yavorsky']      | ['74957105208'] | ['lpmes@lpmes.ru']     | [Row(post='Member Strategy Committee', date_start=None, date_end=None, company='Federal Grid Company of Unified Energy System Joint-Stock Company Fgc Ues Jsc', address=None, comment=None)]                                                                                   |
| ['Roman Yevgenyevich Filimonov']     | ['74957105208'] | ['lpmes@lpmes.ru']     | [Row(post='First Deputy Chairman Management Board', date_start=None, date_end=None, company='Federal Grid Company of Unified Energy System Joint-Stock Company Fgc Ues Jsc', address=None, comment=None)]                                                                      |
| ['Pavel Anatolyevich Livinskii']     | ['74957105208'] | ['lpmes@lpmes.ru']     | [Row(post='Chairman Strategy Committee', date_start=None, date_end=None, company='Federal Grid Company of Unified Energy System Joint-Stock Company Fgc Ues Jsc', address=None, comment=None)]                                                                                 |
| ['Sergey Terebulin']                 | ['74957105208'] | ['lpmes@lpmes.ru']     | [Row(post='Deputy Chairman Management Board', date_start=None, date_end=None, company='Federal Grid Company of Unified Energy System Joint-Stock Company Fgc Ues Jsc', address=None, comment=None)]                                                                            |
| ['Oksana Vladimirovna Shatokhina']   | ['74957105208'] | ['lpmes@lpmes.ru']     | [Row(post='Member Strategy Committee', date_start=None, date_end=None, company='Federal Grid Company of Unified Energy System Joint-Stock Company Fgc Ues Jsc', address=None, comment=None)]                                                                                   |
```