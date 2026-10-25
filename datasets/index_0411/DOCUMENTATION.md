# Parsetron results

## About row data

> - File path: contacts_preprep_tetrika_school_7m_ru_new_full.csv
> - Total rows: 5772030

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Phone: string (nullable = true)
 |-- Email: string (nullable = true)
 |-- Contact URL: string (nullable = true)
 |-- Deal URL: string (nullable = true)

```

### Data sample
```
|            ID | Name                      | Phone            | Email                           | Contact URL                                        | Deal URL   |
|--------------:|:--------------------------|:-----------------|:--------------------------------|:---------------------------------------------------|:-----------|
| nan           |                           |                  |                                 |                                                    |            |
|   5.70869e+07 | Алексей                   | +7 964 277-08-80 | mary620-880@mail.ru             | https://preprep.amocrm.ru/contacts/detail/57086935 |            |
|   5.70869e+07 | Дарья                     | +7 963 269-42-65 | marbakhd@mail.ru                | https://preprep.amocrm.ru/contacts/detail/57086933 |            |
|   5.70869e+07 | Нина мама                 | +7 900 669-75-41 |                                 | https://preprep.amocrm.ru/contacts/detail/57086931 |            |
|   5.70869e+07 | Ирина                     | +7 904 644-75-00 | sakmaradm@mail.ru               | https://preprep.amocrm.ru/contacts/detail/57086929 |            |
|   5.70869e+07 | Матвей                    | +7 908 204-10-15 | zorin7826@gmail.com             | https://preprep.amocrm.ru/contacts/detail/57086927 |            |
|   5.70869e+07 | Давид                     | +7 988 673-74-77 | goar-petrosyan@inbox.ru         | https://preprep.amocrm.ru/contacts/detail/57086925 |            |
|   5.70869e+07 | Варвара                   | +7 928 160-83-77 | varya.guzovatya@inbox.ru        | https://preprep.amocrm.ru/contacts/detail/57086923 |            |
|   5.70869e+07 | Юлия                      | +7 950 207-47-30 | y-busova@mail.ru                | https://preprep.amocrm.ru/contacts/detail/57086921 |            |
|   5.70869e+07 | Ирина                     | +7 951 187-14-84 | titova.irina85@yandex.ru        | https://preprep.amocrm.ru/contacts/detail/57086919 |            |
|   5.70869e+07 | Александр                 | +7 906 307-74-96 | volkov81@mail.ru                | https://preprep.amocrm.ru/contacts/detail/57086917 |            |
|   5.70869e+07 | Нелли                     | +7 988 083-49-11 | 1751522066@65fakef.org          | https://preprep.amocrm.ru/contacts/detail/57086915 |            |
|   5.70869e+07 | Александр                 | +7 918 454-72-77 | 4547277@mail.ru                 | https://preprep.amocrm.ru/contacts/detail/57086913 |            |
|   5.70869e+07 | Ирина                     | +7 999 086-18-33 | apaskall969@bk.ru               | https://preprep.amocrm.ru/contacts/detail/57086911 |            |
|   5.70869e+07 | Таисия                    | +7 900 669-75-41 | 1751521808@62fakef.org          | https://preprep.amocrm.ru/contacts/detail/57086909 |            |
|   5.70869e+07 | Оганесян Лилит Гамлетовна | +7 953 282-34-86 | lilit_hovhannisyan_1988@mail.ru | https://preprep.amocrm.ru/contacts/detail/57086907 |            |
|   5.70869e+07 | Константин                | +7 8912 2599 82  | exp.pkv@icloud.com              | https://preprep.amocrm.ru/contacts/detail/57086905 |            |
|   5.70869e+07 | Галина                    | +7 951 545-78-74 | 1751521747@37fakef.org          | https://preprep.amocrm.ru/contacts/detail/57086903 |            |
|   5.70869e+07 | Ильсаф                    | +7 996 605-47-75 | ilsafk702@gmail.com             | https://preprep.amocrm.ru/contacts/detail/57086901 |            |
|   5.70869e+07 | Эмиль                     | +7 917 765-41-05 | zodiak2090ddnet@gmail.com       | https://preprep.amocrm.ru/contacts/detail/57086899 |            |
```


## About final data

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



### Data sample
```
| names                       | emails                                | phones          |
|:----------------------------|:--------------------------------------|:----------------|
| ['Дмитрий']                 | ['1751622168@37fakef.org']            | ['79960567330'] |
| ['Елизавета']               | ['eg.sakayeva@gmail.com']             | ['79110851564'] |
| ['Михаил']                  | ['1751612393@3fakef.org']             | ['79829216493'] |
| ['Ирина']                   | ['1751576997@69fakef.org']            | ['79827598926'] |
| ['Тохирджон']               | ['vohidovtohirdzon@gmail.com']        | ['79996119190'] |
| ['Наталия Михайловна']      | ['nataliya.larina1@yandex.ru']        | ['79163567720'] |
| ['Виктория']                | ['supervikad@gmail.com']              | ['79299380237'] |
| ['Оксана']                  | ['oksana-morozova-02021983@mail.ru']  | ['79144812805'] |
| ['Владимир']                | ['vova_prim@mail.ru']                 | ['79242551480'] |
| ['Ольга']                   | ['olgabrodagina9@gmail.com']          | ['79519802015'] |
| ['Ольга']                   | ['o-leek@yandex.ru']                  | ['79214587825'] |
| ['Светлана']                | ['660929@mail.ru']                    | ['79833316115'] |
| ['Екатерина']               | ['i_t_a_k1@mail.ru']                  | ['79279932718'] |
| ['Рукина Елена Викторовна'] | ['rimaball310@gmail.com']             | ['79081432192'] |
| ['Мария']                   | ['toritzyna2013@yandex.ru']           | ['79508911598'] |
| ['Александр']               | ['shura.shevelev.1989@mail.ru']       | ['79063092346'] |
| ['Милана']                  | ['1751469339@7fakef.org']             | ['79269926150'] |
| ['Николай']                 | ['nikolaylatartsev@outlook.com']      | ['79883438603'] |
| ['Ольга']                   | ['biryukova.olg2016@yandex.ru']       | ['79825106736'] |
| ['Кристина']                | ['kristina.skorokhodova1997@mail.ru'] | ['79992285751'] |
```