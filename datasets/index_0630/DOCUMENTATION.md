# Parsetron results

## About row data

> - File path: wp_users.csv
> - Total rows: 24339

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- user_login: string (nullable = true)
 |-- user_pass: string (nullable = true)
 |-- user_nicename: string (nullable = true)
 |-- user_email: string (nullable = true)
 |-- user_url: string (nullable = true)
 |-- user_activation_key: string (nullable = true)
 |-- user_status: integer (nullable = true)
 |-- display_name: string (nullable = true)

```

### Data sample
```
|   ID | user_login          | user_pass                          | user_nicename       | user_email                    | user_url   | user_activation_key   |   user_status | display_name   |
|-----:|:--------------------|:-----------------------------------|:--------------------|:------------------------------|:-----------|:----------------------|--------------:|:---------------|
|    4 | fazylov             | $P$BTeSPCiwI8N4ZcTnHxz8pUeunQiST80 | fazylov             | fazylov@psy-in.ru             |            |                       |             0 | Марат          |
|    5 | novosibirsk         | $P$Bw6.Bq0UlKpcbVZUFhJBFVwqkS4603/ | novosibirsk         | novosibirsk@psy-in.ru         |            |                       |             0 | Александр      |
|    6 | skirdinal           | $P$BWiq8RqMIR9nLI0xUb6brJ425/r0Qg/ | skirdinal           | skirdinal@mail.ru             |            |                       |             0 | Людмила        |
|    7 | kazan               | $P$B4P7aAjvY67sBN/3K6vtsbQqGE0K4w/ | kazan               | kazan@psy-in.ru               |            |                       |             0 | Диляра         |
|    8 | dav_88              | $P$BazvUem0X1FYsXyatHeJ5Y14aN4Acm1 | dav_88              | dav_88@mail.ru                |            |                       |             0 | Давыд          |
|   10 | pamilovanov         | $P$BRnXyrifaw7eUI7FnR1UI5xU/1haCW. | pamilovanov         | pamilovanov@mail.ru           |            |                       |             0 | Павел          |
|   11 | spb                 | $P$Bo.LxbHrgVDWfGsSNemMk7Lqq32z8w1 | spb                 | spb@psy-in.ru                 |            |                       |             0 | spb            |
|   12 | makaryev            | $P$BgFZL2Z7HjrRuR5drf3qdMjXjoYw5F. | makaryev            | makaryev@mail.ru              |            |                       |             0 | Алексей        |
|   13 | yedakina            | $P$BSs6HBZlmhbiV6Bb75ZQ5gLMDSMa3E1 | yedakina            | yedakina@psyip.ru             |            |                       |             0 | Татьяна        |
|   14 | astahovan           | $P$BSyoUYgTjFzkbEmxoe3IWizyHK5ZVl1 | astahovan           | astahovan@mail.ru             |            |                       |             0 | Наталья        |
|   15 | matveev             | $P$B0oflwH86PGqqt8iI3fVoGR.j/I5EN0 | matveev             | matveev@psyip.ru              |            |                       |             0 | Константин     |
|   16 | d.hobotov           | $P$BI5hIa0g5bNmC80TF9V9iH0qTEI4km/ | d-hobotov           | d.hobotov@bk.ru               |            |                       |             0 | Дмитрий        |
|   17 | vorobieva           | $P$BQg1vDVc7gu75D/p5DwX7cM1TYLluL. | vorobieva           | vorobieva@psyip.ru            |            |                       |             0 | vorobieva      |
|   18 | ruznyaev1968        | $P$B5kb7fAER8GLzPGL.gQQWHYbxjkv9j0 | ruznyaev1968        | ruznyaev1968@mail.ru          |            |                       |             0 | Владимир       |
|   19 | liya_f              | $P$BJrhnf0V5UiI0j23O1GK3X05hXouVt/ | liya_f              | liya_f@mail.ru                |            |                       |             0 | Лия            |
|   20 | girl10011           | $P$BZY5ssCITSpN1lU560DlOcPVTEDH5A1 | girl10011           | girl10011@gmail.com           |            |                       |             0 | Ольга          |
|   21 | a.v.rudakova        | $P$BixW.jy9AMkfP.UJZPtP4rlw5uBDHE/ | a-v-rudakova        | a.v.rudakova@gmail.com        |            |                       |             0 | Александра     |
|   22 | sgalyav             | $P$BUxYLuraC1M9.oydwCCronQ9E8Pf2m1 | sgalyav             | sgalyav@ya.ru                 |            |                       |             0 | sgalyav        |
|   23 | viktoria.savitskaja | $P$BBGyLZKn0.FdrjeN8Ejs/tK3obfOXf/ | viktoria-savitskaja | viktoria.savitskaja@gmail.com |            |                       |             0 | Виктория       |
|   24 | denis               | $P$BYSSAW5Ef9A0RPd18F1yBcWrndcF5z0 | denis               | denis@psy-in.ru               |            |                       |             0 | Денис          |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 100.00% |
| Accounts | 100.00% |



### Data sample
```
| names              | emails                            | accounts                                                                                                                                                               |
|:-------------------|:----------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ['Марат']          | ['fazylov@psy-in.ru']             | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='fazylov', password_hash='$P$BTeSPCiwI8N4ZcTnHxz8pUeunQiST80')]             |
| ['Александр']      | ['novosibirsk@psy-in.ru']         | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='novosibirsk', password_hash='$P$Bw6.Bq0UlKpcbVZUFhJBFVwqkS4603/')]         |
| ['Людмила']        | ['skirdinal@mail.ru']             | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='skirdinal', password_hash='$P$BWiq8RqMIR9nLI0xUb6brJ425/r0Qg/')]           |
| ['Диляра']         | ['kazan@psy-in.ru']               | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='kazan', password_hash='$P$B4P7aAjvY67sBN/3K6vtsbQqGE0K4w/')]               |
| ['Давыд']          | ['dav_88@mail.ru']                | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='dav_88', password_hash='$P$BazvUem0X1FYsXyatHeJ5Y14aN4Acm1')]              |
| ['Павел']          | ['pamilovanov@mail.ru']           | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='pamilovanov', password_hash='$P$BRnXyrifaw7eUI7FnR1UI5xU/1haCW.')]         |
| ['Алексей']        | ['makaryev@mail.ru']              | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='makaryev', password_hash='$P$BgFZL2Z7HjrRuR5drf3qdMjXjoYw5F.')]            |
| ['Татьяна']        | ['yedakina@psyip.ru']             | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='yedakina', password_hash='$P$BSs6HBZlmhbiV6Bb75ZQ5gLMDSMa3E1')]            |
| ['Наталья']        | ['astahovan@mail.ru']             | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='astahovan', password_hash='$P$BSyoUYgTjFzkbEmxoe3IWizyHK5ZVl1')]           |
| ['Константин']     | ['matveev@psyip.ru']              | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='matveev', password_hash='$P$B0oflwH86PGqqt8iI3fVoGR.j/I5EN0')]             |
| ['Дмитрий']        | ['d.hobotov@bk.ru']               | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='d.hobotov', password_hash='$P$BI5hIa0g5bNmC80TF9V9iH0qTEI4km/')]           |
| ['Vorobieva']      | ['vorobieva@psyip.ru']            | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='vorobieva', password_hash='$P$BQg1vDVc7gu75D/p5DwX7cM1TYLluL.')]           |
| ['Владимир']       | ['ruznyaev1968@mail.ru']          | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='ruznyaev1968', password_hash='$P$B5kb7fAER8GLzPGL.gQQWHYbxjkv9j0')]        |
| ['Ольга']          | ['girl10011@gmail.com']           | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='girl10011', password_hash='$P$BZY5ssCITSpN1lU560DlOcPVTEDH5A1')]           |
| ['Александра']     | ['a.v.rudakova@gmail.com']        | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='a.v.rudakova', password_hash='$P$BixW.jy9AMkfP.UJZPtP4rlw5uBDHE/')]        |
| ['Sgalyav']        | ['sgalyav@ya.ru']                 | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='sgalyav', password_hash='$P$BUxYLuraC1M9.oydwCCronQ9E8Pf2m1')]             |
| ['Виктория']       | ['viktoria.savitskaja@gmail.com'] | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='viktoria.savitskaja', password_hash='$P$BBGyLZKn0.FdrjeN8Ejs/tK3obfOXf/')] |
| ['Денис']          | ['denis@psy-in.ru']               | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='denis', password_hash='$P$BYSSAW5Ef9A0RPd18F1yBcWrndcF5z0')]               |
| ['Sofiasavchenko'] | ['sofiasavchenko@mail.ru']        | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='sofiasavchenko', password_hash='$P$Be0j2z1kG41V5EppCTG9PwKEcSUtY41')]      |
| ['Анна']           | ['avgalay@mail.ru']               | [Row(title='Институт Инновационных Психотехнологий (ИИП)', link='https://psy-in.ru', login='avgalay', password_hash='$P$BgbevYp24W8FxegqKKNZMTa8PNq3dY/')]             |
```