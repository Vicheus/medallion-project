# Parsetron results

## About row data

> - Code name: index_0641
> - File path: users_kz_members.csv
> - Total rows: 699

### Schema
```
root
 |-- regid: integer (nullable = true)
 |-- email: string (nullable = true)
 |-- password: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- mobile: string (nullable = true)
 |-- country: string (nullable = true)
 |-- ipadd: string (nullable = true)

```

### Data sample
```
|   regid | email                        | password                         | first_name   | last_name       | mobile          | country    | ipadd           |
|--------:|:-----------------------------|:---------------------------------|:-------------|:----------------|:----------------|:-----------|:----------------|
|  101028 | abdu6191@gmail.com           | 3b6c44615935fb93fdb251d68a10398a | Abdumalik    | Kurbankhazhiyev | +77056874960    | kazakhstan | 172.68.10.60    |
|  102161 | bitov895@gmail.comgm         | ca6926d5906fdc59d19002e57eebb7f1 | Oleg         | Ivankov         | <blank>         | kazakhstan | 172.68.239.49   |
|  102808 | radzhan34@gmail.com          | a3ba69e2ec610876c33076ed6f2c12d7 | Rajan        | Akanov          | <blank>         | kazakhstan | 172.68.246.148  |
|  103088 | slavalcd@gmail.com           | dd4a7f5b3557b61861e8054c2aabbb1f | Vyacheslav   | Kim             | <blank>         | kazakhstan | 172.68.10.120   |
|  103213 | lenatyugaynps@gmail.com      | dd4a7f5b3557b61861e8054c2aabbb1f | Lena         | Tyugay          | <blank>         | kazakhstan | 172.68.244.50   |
|  103531 | sseitov03@gmail.com          | 3d558122fcac9ea5fdc9ee8eccf8f433 | Saken        | Seitov          | <blank>         | kazakhstan | 172.68.182.192  |
|  103708 | jezkent777@gmail.com         | 7332c5667187ea0584b07d85524cf59a | Dmitriy      | Varnakin        | <blank>         | kazakhstan | 172.68.11.91    |
|  103875 | elzalee.1960@gmail.com       | 25cadc9049da2e83cf8ce3d3f2529702 | elza         | li              | <blank>         | kazakhstan | 162.158.182.246 |
|  103991 | gvs1946@bk.ru                | b6b8e20176eddf5006b2eeca093a7e65 | Valentina    | Gordeyeva       | +7 777 186 6934 | kazakhstan | 162.158.179.240 |
|  104884 | boychenko.vip7@gmail.com     | a4550ecc477971a58a91c760c96145db | NIKOLAY      | BOICHENKO       | <blank>         | kazakhstan | 172.68.245.219  |
|  105155 | tvisnevskaa42@gmail.com      | a0044a7b77c85b03f7447701b6ddb3bb | Tatyana      | Vishnevskaia    | <blank>         | kazakhstan | 172.68.10.84    |
|  106393 | viktor2015nik@gmail.com      | e13bb698a43679d8c5bd5ccdf4cda7b6 | Viktor       | Gerasimov       | <blank>         | kazakhstan | 172.68.244.74   |
|  106654 | kirshin_andreyka@mail.ru     | 5b103bbd81bb4f312930c378e7242672 | Andrey       | Kirshin         | <blank>         | kazakhstan | 172.68.10.150   |
|  107326 | mega.bekseit@gmail.com       | 4194bfdbe7e26b7e15b6ed7d35eaf10b | Bekseit      | Danyarov        | <blank>         | kazakhstan | 172.68.182.18   |
|  107535 | cryptonbas@yahoo.com         | bbee998db50d357429c853ef7b963719 | Nurlan       | Panzabekov      | <blank>         | kazakhstan | 172.68.245.63   |
|  107649 | valerii.alert@gmail.com      | fde070c9a07a6246cd21d20d7ee32946 | Valeriy      | Yerokhin        | <blank>         | kazakhstan | 172.68.11.181   |
|  107901 | zauresh.lider.4444@gmail.com | f37f02686590560cc869b54ecbd2ff51 | Зауреш       | Шаяхметова      | <blank>         | kazakhstan | 172.68.245.195  |
|  108105 | Airdropman480@gmail.com      | 7d380eaf11e928c687144ea1282d113b | Vadim        | Gorbul          | <blank>         | kazakhstan | 172.68.238.78   |
|  108253 | 2012elissa2012@gmail.com     | 33e5ef18820985408c0c9f2ba2a0c3fc | Elissa       | Aidamirova      | <blank>         | kazakhstan | 172.68.182.54   |
|  108693 | taliakor888@gmail.com        | 5b567b874d1af9c36d6484d7b26c404a | Nataliya     | Korosteleva     | <blank>         | kazakhstan | 172.68.10.30    |
```


## About final data
> - Total rows: 673

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = false)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Phones | 2.82% |
| Emails | 100.00% |
| Ips | 100.00% |
| Accounts | 100.00% |



### Data sample
```
| names                    | phones          | emails                                          | ips                        | accounts                                                                                                                                                   |
|:-------------------------|:----------------|:------------------------------------------------|:---------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Bakhytzhan Akezhan']   |                 | ['sady.m@yandex.com']                           | [Row(ip='92.47.30.74')]    | [Row(title='123RF', link='https://www.123rf.com/', login='sady.m@yandex.com', password_hash='a59ba6e9b63acb3c6856c7bd220e55c6')]                           |
| ['Dauletbaeff Berdakh']  |                 | ['dauletbaeffberdakh@gmail.com']                | [Row(ip='90.143.169.237')] | [Row(title='123RF', link='https://www.123rf.com/', login='dauletbaeffberdakh@gmail.com', password_hash='e43f3a1c205dc30719862ee25b5a43bb')]                |
| ['Kleyev Dmitriy']       |                 | ['dimankleev1988@gmail.com']                    | [Row(ip='172.68.244.248')] | [Row(title='123RF', link='https://www.123rf.com/', login='dimankleev1988@gmail.com', password_hash='5ffaa311f6b1c439ef716b06b6bf2895')]                    |
| ['Kruger Nancy']         |                 | ['ashleyartand1976@zontero.win']                | [Row(ip='205.185.222.72')] | [Row(title='123RF', link='https://www.123rf.com/', login='ashleyartand1976@zontero.win', password_hash='6f01bf38875055913c6ef3774eb2fb3d')]                |
| ['Pinson Qihong']        |                 | ['thomaswasuacts1951@intomail.pw']              | [Row(ip='46.237.8.41')]    | [Row(title='123RF', link='https://www.123rf.com/', login='thomaswasuacts1951@intomail.pw', password_hash='7444c2b206045a4abb64e1e5a83128e8')]              |
| ['Shmakov Viktor']       |                 | ['sos7070@yahoo.com']                           | [Row(ip='172.68.245.141')] | [Row(title='123RF', link='https://www.123rf.com/', login='sos7070@yahoo.com', password_hash='92c4358d35be072b15ea406da3e1dce9')]                           |
| ['Balabanov Sergey']     |                 | ['sbalabanov1962@gmail.com']                    | [Row(ip='162.158.182.30')] | [Row(title='123RF', link='https://www.123rf.com/', login='sbalabanov1962@gmail.com', password_hash='2e2b75f0ab0487f91b794d10e056a7da')]                    |
| ['Beckner Bill']         |                 | ['lashaunlco4j@mail.ru']                        | [Row(ip='119.26.144.80')]  | [Row(title='123RF', link='https://www.123rf.com/', login='lashaunlco4j@mail.ru', password_hash='6408376b3b8cd06eda63387cb3ea5fcc')]                        |
| ['Asertf Sdf']           |                 | ['wr6iteskomt@gmail.com']                       | [Row(ip='178.72.70.213')]  | [Row(title='123RF', link='https://www.123rf.com/', login='wr6iteskomt@gmail.com', password_hash='4a734b4d1c252e8c4ca7726da8ff8aa6')]                       |
| ['Brem Valentina']       |                 | ['zelinskay6@gmail.com']                        | [Row(ip='172.68.246.142')] | [Row(title='123RF', link='https://www.123rf.com/', login='zelinskay6@gmail.com', password_hash='58ea7aa8aabecb043a28266d35389ead')]                        |
| ['Chongbang Jeff']       |                 | ['leroybrail1990@megahost.info']                | [Row(ip='72.178.18.206')]  | [Row(title='123RF', link='https://www.123rf.com/', login='leroybrail1990@megahost.info', password_hash='1e31dc459e7b8e16401bf7b05f6c9f63')]                |
| ['Jabagina Makhbal']     |                 | ['makhbal.jabagina@gmail.com']                  | [Row(ip='172.68.11.145')]  | [Row(title='123RF', link='https://www.123rf.com/', login='makhbal.jabagina@gmail.com', password_hash='c8603fa0cda9ef0d1a23c1b79e2695e3')]                  |
| ['Ospanov Ilyas']        |                 | ['oilyasb1984@gmail.com']                       | [Row(ip='37.150.0.159')]   | [Row(title='123RF', link='https://www.123rf.com/', login='oilyasb1984@gmail.com', password_hash='d96cf9978a90ca0891fe707ed003837c')]                       |
| ['Smelyanskiy Yevgeniy'] | ['77772315418'] | ['tehnoplusyou.tobe@gmail.com']                 | [Row(ip='172.68.245.147')] | [Row(title='123RF', link='https://www.123rf.com/', login='tehnoplusyou.tobe@gmail.com', password_hash='f7369b81dd27ee565b8f48dfceeca796')]                 |
| ['Varavkin Danila']      |                 | ['danila.varavkin@gmail.com']                   | [Row(ip='159.89.123.102')] | [Row(title='123RF', link='https://www.123rf.com/', login='danila.varavkin@gmail.com', password_hash='81191374ccc17b4c492d580ba4a5bc1a')]                   |
| ['Bgsg Jgge']            |                 | ['lin.h.duonglanngocba0012.34567890@gmail.com'] | [Row(ip='27.67.19.253')]   | [Row(title='123RF', link='https://www.123rf.com/', login='lin.h.duonglanngocba0012.34567890@gmail.com', password_hash='de929b872e736cc0666b6ed6897a982b')] |
| ['Chen Rakesh']          |                 | ['susiefk0@bk.ru']                              | [Row(ip='209.107.196.56')] | [Row(title='123RF', link='https://www.123rf.com/', login='susiefk0@bk.ru', password_hash='003380f6fde0622318a8959e478997e3')]                              |
| ['Kadyrov Islam']        |                 | ['element@spaces.ru']                           | [Row(ip='172.68.10.72')]   | [Row(title='123RF', link='https://www.123rf.com/', login='element@spaces.ru', password_hash='71cae1d4e4ac7bda62e842c2765ce487')]                           |
| ['Temirkhanova Alima']   |                 | ['alima67a@gmail.com']                          | [Row(ip='172.68.245.141')] | [Row(title='123RF', link='https://www.123rf.com/', login='alima67a@gmail.com', password_hash='4efe5cacafe300fd7644293efcdba718')]                          |
| ['Tyugay Lena']          |                 | ['lenatyugaynps@gmail.com']                     | [Row(ip='172.68.244.50')]  | [Row(title='123RF', link='https://www.123rf.com/', login='lenatyugaynps@gmail.com', password_hash='dd4a7f5b3557b61861e8054c2aabbb1f')]                     |
```