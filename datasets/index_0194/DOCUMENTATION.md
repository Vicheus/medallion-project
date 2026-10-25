# Parsetron results

## About row data

> - Code name: index_0194
> - File path: /media/user/SAMSUNG/Databases/index_0194/raw/*.csv
> - Total rows: 633862

### Schema
```
root
 |-- LOGIN: string (nullable = true)
 |-- PASSWORD: string (nullable = true)
 |-- NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- SECOND_NAME: string (nullable = true)
 |-- PERSONAL_PHONE: string (nullable = true)
 |-- PERSONAL_MOBILE: double (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- PERSONAL_CITY: string (nullable = true)
 |-- PERSONAL_BIRTHDAY: date (nullable = true)

```

### Data sample
```
|         LOGIN | PASSWORD                                 | NAME          | LAST_NAME   | SECOND_NAME   |   PERSONAL_PHONE |   PERSONAL_MOBILE | EMAIL                  | PERSONAL_CITY   | PERSONAL_BIRTHDAY   |
|--------------:|:-----------------------------------------|:--------------|:------------|:--------------|-----------------:|------------------:|:-----------------------|:----------------|:--------------------|
| +375291297333 | V.0q5g~Wa2027fd649c5ccf781c776d7e03b2544 | karpovkos     |             |               |    +375291297333 |               nan | karpovkos@gmail.com    |                 |                     |
| +375297554775 | zpBFC9yG908e2c6bb142192882fe55db2e542a27 | chijik2004    |             |               |    +375297554775 |               nan | chijik2004@list.ru     | Минск           |                     |
| +375293640277 | GUCihQ92f4f8eb8ddc1dae8eb5389c87bdcf3c5c | hramtsova     |             |               |    +375293640277 |               nan | hramtsova@list.ru      | Минск           |                     |
| +375296708308 | d2F$3Ay:7ecaf6da0d086c9f87ef32e8b11c699a | sir.john.by   |             |               |    +375296708308 |               nan | sir.john.by@gmail.com  | Минск           |                     |
| +375291027942 | E3nwijb1b3329dd8762ed5fd05987479063fe975 | grotus72      |             |               |    +375291027942 |               nan | grotus72@mail.ru       | Осиповичи       |                     |
| +375291190157 | LmxlQuhy9f867cf53b3b5ac1949b3ea10dd6043f | prostova      |             |               |    +375291190157 |               nan | prostova@gmail.com     | Минск           |                     |
| +375293472296 | DW7nbWa56dbd0880bd014094830386ad270c3bc8 | lydia.masyuk  |             |               |    +375293472296 |               nan | lydia.masyuk@gmail.com | Минск           |                     |
| +375298639637 | k5-XK@6v31d35770a990f59531c51ef1dc80751c | ivashkavna    |             |               |    +375298639637 |               nan | ivashkavna@tyt.by      | Минск           |                     |
| +375296107682 | bD7*.cJ7b30717a6b038b05a90c10a2d4384fbe6 | pasha-guzikov |             |               |    +375296107682 |               nan | pasha-guzikov@mail.ru  | Минск           |                     |
| +375295326048 | VJoFfRvK4c9bc2564d284dbe3640a4253747e5be | shulepof92    |             |               |    +375295326048 |               nan | shulepof92@mail.ru     | Минск           |                     |
| +375291341866 | ETENsbhA55880fbb85ad66a7cfe35358734dcc4c | emaljarchuk   |             |               |    +375291341866 |               nan | emaljarchuk@mail.ru    | Минск           |                     |
| +375259039221 | Zj0#g]1R94fca9f9959802f22c2ca3edcfe640e9 | 12385vasya    |             |               |    +375259039221 |               nan | 12385vasya@gmail.com   | Минск           |                     |
| +375447171127 | uEWe4Qb82e86b3ed918fe9d2f9a9480b9d452a81 | by.goodwin    |             |               |    +375447171127 |               nan | by.goodwin@outlook.com | Минск           |                     |
| +375256271363 | ZQgNXJHi87d19351a24f10598369786e00c68532 | Ekkspress     |             |               |    +375256271363 |               nan | Ekkspress@gmail.com    | Минск           |                     |
| +375296999279 | 1Wv)fU3)25eac15bb6914da7f19441efb6c66d9d | zonec         |             |               |    +375296999279 |               nan | zonec@yandex.ru        | Минск           |                     |
| +375293146447 | cg4MdOTT652977085d41831b8b64cb9a96af33c2 | pinskcity     |             |               |    +375293146447 |               nan | pinskcity@gmail.com    | Минск           |                     |
| +375291324716 | 9sZO9xKv4e4b307562522502d391ea269cbbda01 | stratsevskygn |             |               |    +375291324716 |               nan | stratsevskygn@tut.by   | Минск           |                     |
| +375257896138 | UmASmxvU5058a0d16d7f8a78cb20cf233289d734 | prostokard    |             |               |    +375257896138 |               nan | prostokard@gmail.com   | Минск           |                     |
| +375293865030 | 1zEkiDt98ff6c32178e5217196ecc3792b941173 | andreygon1    |             |               |    +375293865030 |               nan | andreygon1@rambler.ru  | Минск           |                     |
| +375296709307 | mAQtiExy0ca5d687229eea2e46e06c63a300071f | vastu80       |             |               |    +375296709307 |               nan | vastu80@mail.ru        | Минск           |                     |
```


## About final data
> - Total rows: 319383

### Schema
```
root
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```

### Data sample
```
| emails   | phones           | names                     | address         | accounts                                                                                                                         |
|:---------|:-----------------|:--------------------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------|
|          | ['375257233977'] | ['Novikovaolesia']        | ['Борисов']     | [Row(title='Соседи', link='https://sosedi.by', login='+375257233977', password_hash='HLxmEyupfcfb43cb0196fe38217865cc30caa145')] |
|          | ['375259036605'] | ['Natalikapeckyrova']     |                 | [Row(title='Соседи', link='https://sosedi.by', login='+375259036605', password_hash='rY~1e1F-f6461a50f8172544fefd31b2aaccd4c5')] |
|          | ['375259594342'] | ['Ztarashkevich']         |                 | [Row(title='Соседи', link='https://sosedi.by', login='+375259594342', password_hash='6Ey5ifsu4d8447e34fa3ad6c8330443221dc1558')] |
|          | ['375291363559'] | ['Solar']                 |                 | [Row(title='Соседи', link='https://sosedi.by', login='+375291363559', password_hash='TEl3pDPw5fc8f1569419e23ed7a2aef31fa6b07a')] |
|          | ['375291434583'] | ['T.Rovd']                | ['Минск']       | [Row(title='Соседи', link='https://sosedi.by', login='+375291434583', password_hash='eyCZwfPaedf36ef4ff6a770237b4b6de8b5ddb10')] |
|          | ['375291545567'] | ['Broom']                 | ['Минск']       | [Row(title='Соседи', link='https://sosedi.by', login='+375291545567', password_hash='EIN6NaxN3caea31fa5a2f724a0504a0b46790809')] |
|          | ['375291612280'] | ['K.Irina']               |                 | [Row(title='Соседи', link='https://sosedi.by', login='+375291612280', password_hash='dYi28ZIc266411ba091523c0b498631e79fd9a60')] |
|          | ['375291953634'] | ['Ksana']                 | ['Минск']       | [Row(title='Соседи', link='https://sosedi.by', login='+375291953634', password_hash='ZVQyBEEQ07fd7507537fcb4a4195c307a94ce991')] |
|          | ['375292255913'] | ['Sunrise']               | ['Минск']       | [Row(title='Соседи', link='https://sosedi.by', login='+375292255913', password_hash='P2~q7n^J1cff9b202a4c7675976fde4de022692d')] |
|          | ['375292694197'] | ['Elektronic']            | ['Минск']       | [Row(title='Соседи', link='https://sosedi.by', login='+375292694197', password_hash=';0BhU2i@22f251ac0747b9771165a721f4ca16d7')] |
|          | ['375292808635'] | ['Anastasiyaaristarhova'] | ['Витебск']     | [Row(title='Соседи', link='https://sosedi.by', login='+375292808635', password_hash='WgpWTb3K6baf5164ba7fc63a69e89e9c729a7d37')] |
|          | ['375293353022'] | ['Mudruavskij']           |                 | [Row(title='Соседи', link='https://sosedi.by', login='+375293353022', password_hash='sM:3M+8t71dfa4ec57572100e1fcb8587414d44b')] |
|          | ['375293407990'] | ['Anna']                  | ['Минск']       | [Row(title='Соседи', link='https://sosedi.by', login='+375293407990', password_hash='MrwO4ngN593d91e665ad3b830db9273376ba400a')] |
|          | ['375293413014'] | ['Venna']                 |                 | [Row(title='Соседи', link='https://sosedi.by', login='+375293413014', password_hash='Kb01kkHxaf35e0fee71422a4eae51b6b86ed34c3')] |
|          | ['375293818270'] | ['Marina.Voluevich']      | ['Речица']      | [Row(title='Соседи', link='https://sosedi.by', login='+375293818270', password_hash='Mgn56SPC50c9305ea899763c12ee27bd818e33e4')] |
|          | ['375295027612'] | ['Arina']                 | ['Минск']       | [Row(title='Соседи', link='https://sosedi.by', login='+375295027612', password_hash='BmQ9aIAp34c2cc334f3206ec56e478b80525abef')] |
|          | ['375295277610'] | ['Wwwtima-Dima']          |                 | [Row(title='Соседи', link='https://sosedi.by', login='+375295277610', password_hash='AR7GhIX06d22a5ea17b3e7860bfcd39e3a66a5c6')] |
|          | ['375295506979'] | ['Lenka']                 | ['Минск']       | [Row(title='Соседи', link='https://sosedi.by', login='+375295506979', password_hash='HnPTazP596c2a27d360f42763cc4205363f58f5f')] |
|          | ['375295743746'] | ['-Margo-']               | ['Минск']       | [Row(title='Соседи', link='https://sosedi.by', login='+375295743746', password_hash='fcujlVxt72e45ff4a722c991e3e02d7388cbfb9f')] |
|          | ['375295869753'] | ['-Luna-']                | ['Радошковичи'] | [Row(title='Соседи', link='https://sosedi.by', login='+375295869753', password_hash='1iZHFvIJ00b9cbf3ca028d0ede0d493bbced27ea')] |
```