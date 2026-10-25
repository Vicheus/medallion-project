# Parsetron results

## About row data

> - Code name: index_0626
> - File path: users_kz.csv
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
> - Total rows: 676

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- ips: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ip: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |
| Phones | 2.81% |
| Ips | 100.00% |
| Accounts | 100.00% |



### Data sample
```
| names                         | emails                           | phones          | ips                         | accounts                                                                                                                   |
|:------------------------------|:---------------------------------|:----------------|:----------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| ['Kurbankhazhiyev Abdumalik'] | ['abdu6191@gmail.com']           | ['77056874960'] | [Row(ip='172.68.10.60')]    | [Row(title='Trident Crypto Fund', login='abdu6191@gmail.com', password_hash='3b6c44615935fb93fdb251d68a10398a')]           |
| ['Ivankov Oleg']              | ['bitov895@gmail.comgm']         |                 | [Row(ip='172.68.239.49')]   | [Row(title='Trident Crypto Fund', login='bitov895@gmail.comgm', password_hash='ca6926d5906fdc59d19002e57eebb7f1')]         |
| ['Akanov Rajan']              | ['radzhan34@gmail.com']          |                 | [Row(ip='172.68.246.148')]  | [Row(title='Trident Crypto Fund', login='radzhan34@gmail.com', password_hash='a3ba69e2ec610876c33076ed6f2c12d7')]          |
| ['Kim Vyacheslav']            | ['slavalcd@gmail.com']           |                 | [Row(ip='172.68.10.120')]   | [Row(title='Trident Crypto Fund', login='slavalcd@gmail.com', password_hash='dd4a7f5b3557b61861e8054c2aabbb1f')]           |
| ['Tyugay Lena']               | ['lenatyugaynps@gmail.com']      |                 | [Row(ip='172.68.244.50')]   | [Row(title='Trident Crypto Fund', login='lenatyugaynps@gmail.com', password_hash='dd4a7f5b3557b61861e8054c2aabbb1f')]      |
| ['Seitov Saken']              | ['sseitov03@gmail.com']          |                 | [Row(ip='172.68.182.192')]  | [Row(title='Trident Crypto Fund', login='sseitov03@gmail.com', password_hash='3d558122fcac9ea5fdc9ee8eccf8f433')]          |
| ['Varnakin Dmitriy']          | ['jezkent777@gmail.com']         |                 | [Row(ip='172.68.11.91')]    | [Row(title='Trident Crypto Fund', login='jezkent777@gmail.com', password_hash='7332c5667187ea0584b07d85524cf59a')]         |
| ['Li Elza']                   | ['elzalee.1960@gmail.com']       |                 | [Row(ip='162.158.182.246')] | [Row(title='Trident Crypto Fund', login='elzalee.1960@gmail.com', password_hash='25cadc9049da2e83cf8ce3d3f2529702')]       |
| ['Gordeyeva Valentina']       | ['gvs1946@bk.ru']                | ['77771866934'] | [Row(ip='162.158.179.240')] | [Row(title='Trident Crypto Fund', login='gvs1946@bk.ru', password_hash='b6b8e20176eddf5006b2eeca093a7e65')]                |
| ['Boichenko Nikolay']         | ['boychenko.vip7@gmail.com']     |                 | [Row(ip='172.68.245.219')]  | [Row(title='Trident Crypto Fund', login='boychenko.vip7@gmail.com', password_hash='a4550ecc477971a58a91c760c96145db')]     |
| ['Vishnevskaia Tatyana']      | ['tvisnevskaa42@gmail.com']      |                 | [Row(ip='172.68.10.84')]    | [Row(title='Trident Crypto Fund', login='tvisnevskaa42@gmail.com', password_hash='a0044a7b77c85b03f7447701b6ddb3bb')]      |
| ['Gerasimov Viktor']          | ['viktor2015nik@gmail.com']      |                 | [Row(ip='172.68.244.74')]   | [Row(title='Trident Crypto Fund', login='viktor2015nik@gmail.com', password_hash='e13bb698a43679d8c5bd5ccdf4cda7b6')]      |
| ['Kirshin Andrey']            | ['kirshin_andreyka@mail.ru']     |                 | [Row(ip='172.68.10.150')]   | [Row(title='Trident Crypto Fund', login='kirshin_andreyka@mail.ru', password_hash='5b103bbd81bb4f312930c378e7242672')]     |
| ['Danyarov Bekseit']          | ['mega.bekseit@gmail.com']       |                 | [Row(ip='172.68.182.18')]   | [Row(title='Trident Crypto Fund', login='mega.bekseit@gmail.com', password_hash='4194bfdbe7e26b7e15b6ed7d35eaf10b')]       |
| ['Panzabekov Nurlan']         | ['cryptonbas@yahoo.com']         |                 | [Row(ip='172.68.245.63')]   | [Row(title='Trident Crypto Fund', login='cryptonbas@yahoo.com', password_hash='bbee998db50d357429c853ef7b963719')]         |
| ['Yerokhin Valeriy']          | ['valerii.alert@gmail.com']      |                 | [Row(ip='172.68.11.181')]   | [Row(title='Trident Crypto Fund', login='valerii.alert@gmail.com', password_hash='fde070c9a07a6246cd21d20d7ee32946')]      |
| ['Шаяхметова Зауреш']         | ['zauresh.lider.4444@gmail.com'] |                 | [Row(ip='172.68.245.195')]  | [Row(title='Trident Crypto Fund', login='zauresh.lider.4444@gmail.com', password_hash='f37f02686590560cc869b54ecbd2ff51')] |
| ['Gorbul Vadim']              | ['airdropman480@gmail.com']      |                 | [Row(ip='172.68.238.78')]   | [Row(title='Trident Crypto Fund', login='airdropman480@gmail.com', password_hash='7d380eaf11e928c687144ea1282d113b')]      |
| ['Aidamirova Elissa']         | ['2012elissa2012@gmail.com']     |                 | [Row(ip='172.68.182.54')]   | [Row(title='Trident Crypto Fund', login='2012elissa2012@gmail.com', password_hash='33e5ef18820985408c0c9f2ba2a0c3fc')]     |
| ['Korosteleva Nataliya']      | ['taliakor888@gmail.com']        |                 | [Row(ip='172.68.10.30')]    | [Row(title='Trident Crypto Fund', login='taliakor888@gmail.com', password_hash='5b567b874d1af9c36d6484d7b26c404a')]        |
```