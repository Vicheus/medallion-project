# Parsetron results

## About row data

> - Code name: index_0115
> - File path: pipe_separated_rows.csv
> - Total rows: 379539

### Schema
```
root
 |-- unknown_field_1: string (nullable = true)
 |-- unknown_field_2: string (nullable = true)
 |-- unknown_field_3: string (nullable = true)
 |-- unknown_field_4: string (nullable = true)
 |-- unknown_field_5: string (nullable = true)
 |-- unknown_field_6: string (nullable = true)
 |-- unknown_field_7: string (nullable = true)
 |-- unknown_field_8: string (nullable = true)
 |-- raw_data: string (nullable = true)
 |-- system_number: string (nullable = true)
 |-- unknown_field_9: string (nullable = true)

```

### Data sample
```
| unknown_field_1   | unknown_field_2   | unknown_field_3   | unknown_field_4   |   unknown_field_5 | unknown_field_6   | unknown_field_7   |   unknown_field_8 | raw_data                                          |   system_number | unknown_field_9   |
|:------------------|:------------------|:------------------|:------------------|------------------:|:------------------|:------------------|------------------:|:--------------------------------------------------|----------------:|:------------------|
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | бабинова марина викторовна 24.01.1977 05499889645 |        26553852 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | бабина надежда николаевна 13.04.1980 04831895079  |        26553850 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | бабенко руслан васильевич 24.01.1974 07048958692  |        26553848 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | бабенко ольга ивановна 22.12.1968 06784542000     |        26553846 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 |                                                   |        26553845 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | бабаринова ирина юрьевна 23.01.1990 0998591       |        26553844 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 |                                                   |        26553843 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | бабак оксана александровна 23.06.1984 136763      |        26553842 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 |                                                   |        26553841 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 |                                                   |        26553839 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | ащеулова алена николаевна 05.04.1979 12769963821  |        26553837 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | ашуров рустам ракибович 30.07.1985 10694355667    |        26553835 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | ахтаров ренат рафикович 07.05.1986 13667499106    |        26553833 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 |                                                   |        26553832 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | ахрамович ирина ивановна 30.05.1985               |        26553831 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 |                                                   |        26553830 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | ахметова вера динусовна 02.05.1991 1446028        |        26553829 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | ахметов андрей камильевич 30.11.1988 13568137070  |        26553827 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 |                                                   |        26553826 | ,                 |
|                   |                   |                   |                   |                 0 |                   |                   |                 0 | ахмедьянов рустам могсимович 02.10.1976 04873247  |        26553825 | ,                 |
```

> - Code name: index_0115
> - File path: comma_separated_rows_with_names.csv
> - Total rows: 28148932

### Schema
```
root
 |-- phone: string (nullable = true)
 |-- surname: string (nullable = true)
 |-- name: string (nullable = true)
 |-- patronymic: string (nullable = true)
 |-- dateofbirth: string (nullable = true)
 |-- place_of_birth: string (nullable = true)
 |-- passport: string (nullable = true)
 |-- snils: string (nullable = true)
 |-- inn: string (nullable = true)
 |-- address: string (nullable = true)
 |-- comment: string (nullable = true)
 |-- system_number: string (nullable = true)

```

### Data sample
```
| phone          | surname     | name      | patronymic    | dateofbirth   | place_of_birth   | passport               | snils       | inn          | address                                                                                        | comment     | system_number   |
|:---------------|:------------|:----------|:--------------|:--------------|:-----------------|:-----------------------|:------------|:-------------|:-----------------------------------------------------------------------------------------------|:------------|:----------------|
| телефон        |             | фио       |               | Дата рождения | место рождения   | паспорт                | снилс       | инн          | адрес                                                                                          | комментарий | системный номер |
| 89526126126312 | лачинов     | максим    | игоревич      | 28-01-1981    |                  | 2507 868310 11.10.2007 | 14122676430 |              | 664009, иркутская обл, , иркутск г, , советская ул, д.176, корп.200, кв.8                      |             | 2292100         |
| 84959268622185 | бербекова   | раиса     | алиевна       | 23-11-1976    |                  | 8305 755497 01.03.2006 | 7171707556  | 070708385680 | г. москва осенняя 10 488                                                                       |             | 505956          |
| 8924646521859  | контомирова | татьяна   | юрьевна       | 14-01-1987    |                  | 2509 239021 10.07.2009 | 13635563869 |              | 665415, иркутская обл, , черемхово г, , орджоникидзе ул, д.18, корп.а, кв.28                   |             | 2279512         |
| 952743612992   | вершинина   | наталья   | валерьевна    | 09-05-1973    |                  |                        | 2072637923  |              | каменск-уральский привокзальная 42 12                                                          |             | 15175267        |
| 899149015562   | пономарев   | андрей    | владимирович  | 19-11-1963    |                  | 2509 147322 01.03.2009 | 4870708174  |              | 665451, иркутская обл, , усолье-сибирское г, , интернациональная ул, д.87, корп., кв.94        |             | 2276236         |
| 899148836435   | скляров     | олег      | александрович | 18-12-1960    |                  | 7507 098677 28.11.2007 | 11693587287 |              | 665459, иркутская обл, , усолье-сибирское г, , сеченова ул, д.7, корп., кв.38                  |             | 2277523         |
| 898344183737   | tи+¦l-      | l=lttltl- | ¦ltt+t=l      | 20-09-1982    |                  | 2504 301539 26.11.2004 | 11397216756 |              | 666925, иркутская обл, бодайбинский р-н, , артемовский рп, 60 лет октября ул, д.4, корп., кв.2 |             | 2291760         |
| 898276900067   | чайковская  | вероника  | владимировна  | 15-05-2015    |                  |                        | 18922617098 |              | г екатеринбург якутская 17 2                                                                   |             | 15405495        |
| 896555228877   | соловьев    | савелий   | сергеевич     | 14-03-2002    |                  |                        | 16295755708 |              | ревда островского 6                                                                            |             | 15330100        |
| 896501182177   | григорьева  | ольга     | сергеевна     | 08-01-1988    |                  | 2507 951772 28.02.2008 | 13308841948 |              | 666671, иркутская обл, , усть-илимск г, , трудовая ул, д.4, корп., кв.6                        |             | 2292427         |
| 896496572032   | романенко   | алексей   | владимирович  | 07-07-1968    |                  | 2503 945999 28.06.2003 | 3648660778  |              | 664040, иркутская обл, , иркутск г, , тельмана ул, д.146, корп., кв.                           |             | 2291187         |
| 896496572030   | романенко   | алексей   | владимирович  | 07-07-1968    |                  |                        | 3648660778  |              | 664040, иркутская обл, , иркутск г, , тельмана ул, д.146, корп., кв.                           |             | 2332801         |
| 896454400270   | ветров      | евгений   | сергеевич     | 08-10-1987    |                  |                        | 11953207955 |              | 664013, иркутская обл, , иркутск г, , восточный пер, д.3, корп., кв.21                         |             | 2332142         |
| 896454400267   | ветров      | евгений   | сергеевич     | 08-10-1987    |                  | 2511 674758 11.04.2012 | 11953207955 |              | 664013, иркутская обл, , иркутск г, , восточный пер, д.3, корп., кв.21                         |             | 2283514         |
| 896454332003   | скачкова    | ольга     | николаевна    | 26-04-1987    |                  | 2507 865972 01.08.2007 | 9946716333  |              | 665462, иркутская обл, , усолье-сибирское г, , ватутина ул, д.2, корп., кв.15                  |             | 2276662         |
| 896454002650   | лучининов   | борис     | юрьевич       | 04-12-1979    |                  |                        | 7462209863  |              | 665835, иркутская обл, , ангарск г, , гагарина ул, д.17, корп., кв.76                          |             | 2335077         |
| 896448109012   | кипрушина   | ольга     | андреевна     | 28-06-1991    |                  | 2510 493813 30.06.2011 | 14019665144 |              | 665360, иркутская обл, зиминский р-н, , центральный хазан п, мира ул, д.69, корп., кв.2        |             | 2280072         |
| 896448028950   | глебов      | денис     | владимирович  | 15-12-1980    |                  |                        | 11874116558 |              | 664019, иркутская обл, , иркутск г, , баррикад ул, д.187, корп., кв.69                         |             | 2332323         |
| 896448028945   | глебов      | денис     | владимирович  | 15-12-1980    |                  | 2506 769414 16.03.2007 | 11874116558 |              | 664019, иркутская обл, , иркутск г, , баррикад ул, д.187, корп., кв.69                         |             | 2293172         |
```


## About final data
> - Total rows: 16273656

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- birth_date: string (nullable = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = false)

```



### Data sample
```
| names                                  | birth_date   | phones   | documents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | address                                                                   |
|:---------------------------------------|:-------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| ['Абаев Сергей Геннадьевич']           | 18.06.1989   |          | [Row(type=2, serial='16863112478', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                                                                                                                                              | ['Россия Московская Область Ленинский Район Пос.Новодрожжино Д.11 Кв.52'] |
| ['Абаева Алтынай Кунакбаевна']         | 24.12.1969   |          | [Row(type=0, serial='5300455721', country='RUS', date_issue='07.01.2001', date_expire=None, authority=None, authority_code=None), Row(type=2, serial='149276409950', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                            | ['Россияоренбургская Облг. Орскул Майскаяд.34']                           |
| ['Абаева Елена Георгиевна']            |              |          | [Row(type=2, serial='06604878179', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                                                                                                                                              |                                                                           |
| ['Абаева Зоя Аврамовна']               | 26.03.1953   |          | [Row(type=0, serial='9002244490', country='RUS', date_issue='26.01.2002', date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                                                                                                                                       | ['С. Мичурино Пер. Колхозный 4 0']                                        |
| ['Абазова Людмила Ивановна']           | 16.01.1968   |          | [Row(type=0, serial='8202806791', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='06997207222', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['Р-Н Кизлярский Большой Бредихин']                                       |
| ['Абаимова Татьяна Михайловна']        | 09.07.1962   |          | [Row(type=2, serial='06787224101', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                                                                                                                                              | ['Г.Ульяновск Пр-Т Ленинского Комсомола 5 221']                           |
| ['Абаимова Татьяна Павловна']          |              |          | [Row(type=2, serial='01157349829', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                                                                                                                                              |                                                                           |
| ['Абакаргаджиева Альбина Хизбулаевна'] | 09.04.1990   |          | [Row(type=0, serial='8209837082', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='14649033470', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['Р-Н Левашинский Джангамахи']                                            |
| ['Абакаров Абакар Магомедович']        | 27.02.1955   |          | [Row(type=0, serial='8203584168', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='06704800452', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['Г Махачкала Махачкала Ул Богатырева 11 14']                             |
| ['Абакаров Абдулалим Абакарович']      | 05.11.1975   |          | [Row(type=0, serial='8205499391', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='13456374364', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['Г Избербаш Избербаш Ул Комарова']                                       |
| ['Абакаров Абубакар Магомедович']      | 11.04.1985   |          | [Row(type=0, serial='8206077680', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='14071140104', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['Р-Н Бабаюртовский Уцми-Юрт']                                            |
| ['Абакаров Абубакар Магомедович']      | 12.03.1988   |          | [Row(type=0, serial='8203262545', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='12945486997', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['368352Р-Н Гунибский С Мегеб']                                           |
| ['Абакаров Бислан Абдулаевич']         | 25.05.1989   |          | [Row(type=0, serial='8203752052', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='13135567034', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=0, serial='8203752052', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='131355670340', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] | ['Р-Н Новолакский Тухчар']                                                |
| ['Абакаров Гасан Абдулманапович']      | 16.01.1982   |          | [Row(type=0, serial='8203548217', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='12959149803', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['368596Р-Н Кайтагский С Рука']                                           |
| ['Абакаров Гусейн Абакарович']         | 18.06.1936   |          | [Row(type=0, serial='8203220151', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='11020201342', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['Р-Н Кулинский Вихли']                                                   |
| ['Абакаров Идрис Салихович']           | 16.08.1986   |          | [Row(type=0, serial='8206130198', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='13805781269', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['368585Р-Н Дахадаевский С Трисанчи']                                     |
| ['Абакаров Ильяс Абакарович']          | 27.09.1966   |          | [Row(type=0, serial='8201427216', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='13813636761', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['Г Махачкала Махачкала Ул Лаптиева 55 31']                               |
| ['Абакаров Магомед Ибрагимович']       | 17.11.1968   |          | [Row(type=0, serial='8201388910', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='05742657075', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['Г Махачкала Махачкала Пр-Кт Амет-Хан Султана 6 49']                     |
| ['Абакаров Магомед Омарович']          | 06.10.1956   |          | [Row(type=0, serial='8203766015', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='07196320367', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['368250Р-Н Гергебильский С Гергебиль']                                   |
| ['Абакаров Наби Алиевич']              | 20.01.1941   |          | [Row(type=0, serial='8203101064', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None), Row(type=2, serial='07203097631', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]                                                                                                                                                                                                                                                     | ['Г Махачкала Махачкала Ул Пархоменко']                                   |
```