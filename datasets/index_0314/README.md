# Parsetron results

## About row data

> - Code name: index_0314
> - File path: yandex_reviews.csv
> - Total rows: 4965925

### Schema
```
root
 |-- Телефон : long (nullable = true)
 |-- Email: string (nullable = true)
 |-- Имя: string (nullable = true)
 |-- ЯндексID: string (nullable = true)
 |-- ЯндексОтзывы: string (nullable = true)

```

### Data sample
```
|    Телефон  | Email                 | Имя             | ЯндексID                   | ЯндексОтзывы                                                           |
|------------:|:----------------------|:----------------|:---------------------------|:-----------------------------------------------------------------------|
| 79030281521 | 79030281521@yandex.ru | Юлия Г.         | 5jqpt75agxj793qepmf0q78kr4 | https://reviews.yandex.ru/user/5jqpt75agxj793qepmf0q78kr4?main_tab=org |
| 79030286592 | 79030286592@yandex.ru | Олеся Е.        | 671uenxr868p3ur53yv8t7zfcr | https://reviews.yandex.ru/user/671uenxr868p3ur53yv8t7zfcr?main_tab=org |
| 79030281666 | 79030281666@yandex.ru | Роман Сухатерин | tv6y5hm9r2xdacpbq9fbngm6zm | https://reviews.yandex.ru/user/tv6y5hm9r2xdacpbq9fbngm6zm?main_tab=org |
| 79030287900 | 79030287900@yandex.ru | Елена Б.        | 4xzga0r4x8mkpeyjkgpnyctgag | https://reviews.yandex.ru/user/4xzga0r4x8mkpeyjkgpnyctgag?main_tab=org |
| 79030289397 | 79030289397@yandex.ru | сергей а.       | q3xbn9cfavf6kkrnd52rbu4fkc | https://reviews.yandex.ru/user/q3xbn9cfavf6kkrnd52rbu4fkc?main_tab=org |
| 79030281199 | 79030281199@yandex.ru | С.А. М.         | 9dw6g7tbkt0er3k6mhfg4nwcdr | https://reviews.yandex.ru/user/9dw6g7tbkt0er3k6mhfg4nwcdr?main_tab=org |
| 79030283823 | 79030283823@yandex.ru | иван н.         | rpv6py63hamy2mgefhnbxf94n0 | https://reviews.yandex.ru/user/rpv6py63hamy2mgefhnbxf94n0?main_tab=org |
| 79030289612 | 79030289612@yandex.ru | александр к.    | 77g8vg5atzyfarw3d5dwzf8auw | https://reviews.yandex.ru/user/77g8vg5atzyfarw3d5dwzf8auw?main_tab=org |
| 79030280647 | 79030280647@yandex.ru | галина г.       | gck28vy5a5jwwztf9daf7u4bm0 | https://reviews.yandex.ru/user/gck28vy5a5jwwztf9daf7u4bm0?main_tab=org |
| 79030284561 | 79030284561@yandex.ru | Любовь Н.       | m79truy1w6z8q1ezgwttmazzzg | https://reviews.yandex.ru/user/m79truy1w6z8q1ezgwttmazzzg?main_tab=org |
| 79030286667 | 79030286667@yandex.ru | Алексей П.      | rufgke1wfrvfppf4tjrx9j8jqr | https://reviews.yandex.ru/user/rufgke1wfrvfppf4tjrx9j8jqr?main_tab=org |
| 79030282640 | 79030282640@yandex.ru | толик п.        | 0kpeg1mhbr0zyknh9wnuh4e6xc | https://reviews.yandex.ru/user/0kpeg1mhbr0zyknh9wnuh4e6xc?main_tab=org |
| 79030280321 | 79030280321@yandex.ru | Есаул           | ff5vavv23dbgg8j2xf4q0hgkyr | https://reviews.yandex.ru/user/ff5vavv23dbgg8j2xf4q0hgkyr?main_tab=org |
| 79030287745 | 79030287745@yandex.ru | Алексей П.      | k6e1321dkg643z4jny3x96b06g | https://reviews.yandex.ru/user/k6e1321dkg643z4jny3x96b06g?main_tab=org |
| 79030286161 | 79030286161@yandex.ru | андрей в.       | xhvphkxzh1d4wemkr52n34exjr | https://reviews.yandex.ru/user/xhvphkxzh1d4wemkr52n34exjr?main_tab=org |
| 79030289093 | 79030289093@yandex.ru | Михаил М.       | y4etfvh0kha6mmt6mdm74xaw50 | https://reviews.yandex.ru/user/y4etfvh0kha6mmt6mdm74xaw50?main_tab=org |
| 79030281179 | 79030281179@yandex.ru | Сергей ф.       | qkn5u2jgunjt185n3m1h58qnbw | https://reviews.yandex.ru/user/qkn5u2jgunjt185n3m1h58qnbw?main_tab=org |
| 79030281177 | 79030281177@yandex.ru | ИРИНА С.        | y65t8cnr7kff114vfx12zd1d6m | https://reviews.yandex.ru/user/y65t8cnr7kff114vfx12zd1d6m?main_tab=org |
| 79030287676 | 79030287676@yandex.ru | Кирилл Ш.       | mcgamyfeu51af3aj8uv2zh36ac | https://reviews.yandex.ru/user/mcgamyfeu51af3aj8uv2zh36ac?main_tab=org |
| 79030285852 | 79030285852@yandex.ru | максим с.       | hyqvvgvp8ac2rdur0506271c1g | https://reviews.yandex.ru/user/hyqvvgvp8ac2rdur0506271c1g?main_tab=org |
```


## About final data
> - Total rows: 3955139

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- id: string (nullable = true)

```

### Data sample
```
| names               | emails                    | phones          | accounts                                                                                        |
|:--------------------|:--------------------------|:----------------|:------------------------------------------------------------------------------------------------|
| ['Юлия Г.']         | ['79030281521@yandex.ru'] | ['79030281521'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='5jqpt75agxj793qepmf0q78kr4')] |
| ['Олеся Е.']        | ['79030286592@yandex.ru'] | ['79030286592'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='671uenxr868p3ur53yv8t7zfcr')] |
| ['Роман Сухатерин'] | ['79030281666@yandex.ru'] | ['79030281666'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='tv6y5hm9r2xdacpbq9fbngm6zm')] |
| ['Елена Б.']        | ['79030287900@yandex.ru'] | ['79030287900'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='4xzga0r4x8mkpeyjkgpnyctgag')] |
| ['Сергей А.']       | ['79030289397@yandex.ru'] | ['79030289397'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='q3xbn9cfavf6kkrnd52rbu4fkc')] |
| ['С.А. М.']         | ['79030281199@yandex.ru'] | ['79030281199'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='9dw6g7tbkt0er3k6mhfg4nwcdr')] |
| ['Иван Н.']         | ['79030283823@yandex.ru'] | ['79030283823'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='rpv6py63hamy2mgefhnbxf94n0')] |
| ['Александр К.']    | ['79030289612@yandex.ru'] | ['79030289612'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='77g8vg5atzyfarw3d5dwzf8auw')] |
| ['Галина Г.']       | ['79030280647@yandex.ru'] | ['79030280647'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='gck28vy5a5jwwztf9daf7u4bm0')] |
| ['Любовь Н.']       | ['79030284561@yandex.ru'] | ['79030284561'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='m79truy1w6z8q1ezgwttmazzzg')] |
| ['Алексей П.']      | ['79030286667@yandex.ru'] | ['79030286667'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='rufgke1wfrvfppf4tjrx9j8jqr')] |
| ['Толик П.']        | ['79030282640@yandex.ru'] | ['79030282640'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='0kpeg1mhbr0zyknh9wnuh4e6xc')] |
| ['Есаул']           | ['79030280321@yandex.ru'] | ['79030280321'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='ff5vavv23dbgg8j2xf4q0hgkyr')] |
| ['Алексей П.']      | ['79030287745@yandex.ru'] | ['79030287745'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='k6e1321dkg643z4jny3x96b06g')] |
| ['Андрей В.']       | ['79030286161@yandex.ru'] | ['79030286161'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='xhvphkxzh1d4wemkr52n34exjr')] |
| ['Михаил М.']       | ['79030289093@yandex.ru'] | ['79030289093'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='y4etfvh0kha6mmt6mdm74xaw50')] |
| ['Сергей Ф.']       | ['79030281179@yandex.ru'] | ['79030281179'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='qkn5u2jgunjt185n3m1h58qnbw')] |
| ['Ирина С.']        | ['79030281177@yandex.ru'] | ['79030281177'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='y65t8cnr7kff114vfx12zd1d6m')] |
| ['Кирилл Ш.']       | ['79030287676@yandex.ru'] | ['79030287676'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='mcgamyfeu51af3aj8uv2zh36ac')] |
| ['Максим С.']       | ['79030285852@yandex.ru'] | ['79030285852'] | [Row(title='Яндекс Отзывы', link='https://reviews.yandex.ru', id='hyqvvgvp8ac2rdur0506271c1g')] |
```