# Parsetron results

## About row data

> - Code name: index_0129
> - File path: users-crm-796452.json
> - Total rows: 796452

### Schema
```
root
 |-- _id: string (nullable = true)
 |-- _ignored: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- _index: string (nullable = true)
 |-- _score: string (nullable = true)
 |-- _source: struct (nullable = true)
 |    |-- __soft_deleted: long (nullable = true)
 |    |-- app_first_login_at: string (nullable = true)
 |    |-- app_login_at: string (nullable = true)
 |    |-- birth_date: string (nullable = true)
 |    |-- city_id: long (nullable = true)
 |    |-- comment: string (nullable = true)
 |    |-- confirm_email: boolean (nullable = true)
 |    |-- confirm_sms: boolean (nullable = true)
 |    |-- country_id: long (nullable = true)
 |    |-- created_at: string (nullable = true)
 |    |-- default_tips: long (nullable = true)
 |    |-- deleted_at: string (nullable = true)
 |    |-- deleting_at: string (nullable = true)
 |    |-- email: string (nullable = true)
 |    |-- employer_id: string (nullable = true)
 |    |-- first_name: string (nullable = true)
 |    |-- id: long (nullable = true)
 |    |-- is_blocked: boolean (nullable = true)
 |    |-- last_active_at: string (nullable = true)
 |    |-- last_name: string (nullable = true)
 |    |-- last_unit_visited: long (nullable = true)
 |    |-- last_visit: string (nullable = true)
 |    |-- last_visited_assigned_employer: string (nullable = true)
 |    |-- middle_name: string (nullable = true)
 |    |-- order_count: long (nullable = true)
 |    |-- payment_count: long (nullable = true)
 |    |-- payment_sum: string (nullable = true)
 |    |-- phone: string (nullable = true)
 |    |-- phone_code: long (nullable = true)
 |    |-- sex: long (nullable = true)
 |    |-- source_company_id: long (nullable = true)
 |    |-- status: string (nullable = true)
 |    |-- updated_at: string (nullable = true)
 |    |-- user_source_id: long (nullable = true)
 |-- _type: string (nullable = true)
 |-- sort: array (nullable = true)
 |    |-- element: long (containsNull = true)

```

### Data sample
```
|   _id | _ignored   | _index    | _score   | _source                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | _type   | sort   |
|------:|:-----------|:----------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|:-------|
|  9001 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:18', default_tips=None, deleted_at=None, deleting_at=None, email='а000112424@example.com', employer_id=None, first_name='Татьяна', id=9001, is_blocked=False, last_active_at=None, last_name='', last_unit_visited=40, last_visit='2019-11-22 18:00:00', last_visited_assigned_employer=None, middle_name='', order_count=2, payment_count=2, payment_sum='3400.00', phone='+79623848120', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:28:24', user_source_id=None)                                                        | _doc    | [0]    |
|  9002 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:18', default_tips=None, deleted_at=None, deleting_at=None, email='nastya.kuzichkina@mail.ru', employer_id=None, first_name='Анастасия', id=9002, is_blocked=False, last_active_at=None, last_name='Хрупова', last_unit_visited=0, last_visit='0000-00-00 00:00:00', last_visited_assigned_employer=None, middle_name='', order_count=3, payment_count=0, payment_sum='0.00', phone='+79119450705', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:28:24', user_source_id=None)                                                | _doc    | [1]    |
|  9003 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:18', default_tips=None, deleted_at=None, deleting_at=None, email='а000010496@example.com', employer_id=None, first_name='Алла', id=9003, is_blocked=False, last_active_at=None, last_name='Салазар', last_unit_visited=18, last_visit='2022-10-14 19:00:00', last_visited_assigned_employer=None, middle_name='', order_count=10, payment_count=9, payment_sum='8200.00', phone='+79045127522', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2022-10-14 19:58:50', user_source_id=None)                                                   | _doc    | [2]    |
|  9004 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:18', default_tips=None, deleted_at=None, deleting_at=None, email='а000157545@example.com', employer_id=None, first_name='Юлия', id=9004, is_blocked=False, last_active_at=None, last_name='Потенко', last_unit_visited=0, last_visit='0000-00-00 00:00:00', last_visited_assigned_employer=None, middle_name='', order_count=0, payment_count=0, payment_sum='0.00', phone='+79523646790', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:42:33', user_source_id=None)                                                        | _doc    | [3]    |
|  9005 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:18', default_tips=None, deleted_at=None, deleting_at=None, email='liberman688@mail.ru', employer_id=None, first_name='Анжела', id=9005, is_blocked=False, last_active_at=None, last_name='Бейлина', last_unit_visited=0, last_visit='0000-00-00 00:00:00', last_visited_assigned_employer=None, middle_name='', order_count=0, payment_count=0, payment_sum='0.00', phone='+79219970999', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:42:33', user_source_id=None)                                                         | _doc    | [4]    |
|  9006 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:19', default_tips=None, deleted_at=None, deleting_at=None, email='nat027@mail.ru', employer_id=None, first_name='Наталья', id=9006, is_blocked=False, last_active_at=None, last_name='Шамкова', last_unit_visited=43, last_visit='2019-09-12 14:15:00', last_visited_assigned_employer=None, middle_name='', order_count=5, payment_count=3, payment_sum='4600.00', phone='+79217408121', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:28:24', user_source_id=None)                                                         | _doc    | [5]    |
|  9007 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date='1974-07-22 00:00:00', city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:19', default_tips=None, deleted_at=None, deleting_at=None, email='irina_grine4ka@mail.ru', employer_id=None, first_name='Ирина', id=9007, is_blocked=False, last_active_at=None, last_name='Гринько', last_unit_visited=33, last_visit='2021-11-13 12:00:00', last_visited_assigned_employer=None, middle_name='', order_count=4, payment_count=4, payment_sum='8400.00', phone='+79213942084', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2021-11-13 13:23:55', user_source_id=None)                                  | _doc    | [6]    |
|  9008 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:19', default_tips=None, deleted_at=None, deleting_at=None, email='а000142689@example.com', employer_id=None, first_name='Ксения', id=9008, is_blocked=False, last_active_at=None, last_name='Салева', last_unit_visited=0, last_visit='0000-00-00 00:00:00', last_visited_assigned_employer=None, middle_name='', order_count=0, payment_count=0, payment_sum='0.00', phone='+79650615536', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:42:33', user_source_id=None)                                                       | _doc    | [7]    |
|  9009 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at='2020-07-20 10:09:36', app_login_at='2020-11-17 12:45:28', birth_date=None, city_id=1, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:19', default_tips=None, deleted_at=None, deleting_at=None, email='lukina.ku@gmail.com', employer_id=None, first_name='Ксения', id=9009, is_blocked=False, last_active_at='2022-09-16 13:05:45', last_name='Федорина', last_unit_visited=37, last_visit='2022-09-16 13:45:00', last_visited_assigned_employer=None, middle_name='', order_count=38, payment_count=36, payment_sum='67150.00', phone='+79062511240', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2022-09-16 14:36:03', user_source_id=None) | _doc    | [8]    |
|  9010 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:19', default_tips=None, deleted_at=None, deleting_at=None, email='le_ruska@mail.ru', employer_id=None, first_name='Валерия', id=9010, is_blocked=False, last_active_at=None, last_name='Панова', last_unit_visited=0, last_visit='0000-00-00 00:00:00', last_visited_assigned_employer=None, middle_name='', order_count=0, payment_count=0, payment_sum='0.00', phone='+79218633731', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:42:33', user_source_id=None)                                                            | _doc    | [9]    |
|  9011 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:20', default_tips=None, deleted_at=None, deleting_at=None, email='а000268722@example.com', employer_id=None, first_name='Елена', id=9011, is_blocked=False, last_active_at=None, last_name='', last_unit_visited=0, last_visit='2019-02-05 09:00:00', last_visited_assigned_employer=None, middle_name='', order_count=1, payment_count=1, payment_sum='100.00', phone='+79213471060', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:28:24', user_source_id=None)                                                            | _doc    | [10]   |
|  9012 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:20', default_tips=None, deleted_at=None, deleting_at=None, email='Cosha200014@gmail.com', employer_id=None, first_name='Софья', id=9012, is_blocked=False, last_active_at=None, last_name='Афанасьева', last_unit_visited=0, last_visit='0000-00-00 00:00:00', last_visited_assigned_employer=None, middle_name='', order_count=0, payment_count=0, payment_sum='0.00', phone='+79062663427', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:42:33', user_source_id=None)                                                     | _doc    | [11]   |
|  9013 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:20', default_tips=None, deleted_at=None, deleting_at=None, email='jshspb90@gmail.com', employer_id=None, first_name='Юлия+Шабалина', id=9013, is_blocked=False, last_active_at=None, last_name='Шабалина', last_unit_visited=0, last_visit='0000-00-00 00:00:00', last_visited_assigned_employer=None, middle_name='', order_count=0, payment_count=0, payment_sum='0.00', phone='+79219560009', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:42:33', user_source_id=None)                                                  | _doc    | [12]   |
|  9014 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:21', default_tips=None, deleted_at=None, deleting_at=None, email='mlopanogova@yandex.ru', employer_id=None, first_name='Марина', id=9014, is_blocked=False, last_active_at=None, last_name='Лопаногова', last_unit_visited=22, last_visit='2022-10-09 09:00:00', last_visited_assigned_employer=None, middle_name='', order_count=26, payment_count=26, payment_sum='46000.00', phone='+79119511182', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2022-10-09 10:16:47', user_source_id=None)                                             | _doc    | [13]   |
|  9015 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:21', default_tips=None, deleted_at=None, deleting_at=None, email='а000146928@example.com', employer_id=None, first_name='Наталья', id=9015, is_blocked=False, last_active_at=None, last_name='Моспалюк', last_unit_visited=0, last_visit='0000-00-00 00:00:00', last_visited_assigned_employer=None, middle_name='', order_count=0, payment_count=0, payment_sum='0.00', phone='+79213297398', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:42:33', user_source_id=None)                                                    | _doc    | [14]   |
|  9016 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:21', default_tips=None, deleted_at=None, deleting_at=None, email='а000127458@example.com', employer_id=None, first_name='Галина', id=9016, is_blocked=False, last_active_at=None, last_name='Прощай', last_unit_visited=0, last_visit='0000-00-00 00:00:00', last_visited_assigned_employer=None, middle_name='', order_count=0, payment_count=0, payment_sum='0.00', phone='+79818869703', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:42:33', user_source_id=None)                                                       | _doc    | [15]   |
|  9017 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:21', default_tips=None, deleted_at=None, deleting_at=None, email='ch.maria.sp@gmail.com', employer_id=None, first_name='Мария', id=9017, is_blocked=False, last_active_at=None, last_name='Чижикова', last_unit_visited=124, last_visit='2022-09-09 10:15:00', last_visited_assigned_employer=None, middle_name='', order_count=4, payment_count=4, payment_sum='5300.00', phone='+79110197082', phone_code=None, sex=0, source_company_id=53, status=None, updated_at='2022-09-09 11:37:46', user_source_id=None)                                                 | _doc    | [16]   |
|  9018 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:21', default_tips=None, deleted_at=None, deleting_at=None, email='а000140551@example.com', employer_id=None, first_name='Татьяна', id=9018, is_blocked=False, last_active_at=None, last_name='Булыгина', last_unit_visited=21, last_visit='2019-12-18 14:00:00', last_visited_assigned_employer=None, middle_name='', order_count=1, payment_count=1, payment_sum='1300.00', phone='+79218632599', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:28:24', user_source_id=None)                                                | _doc    | [17]   |
|  9019 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=1, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:21', default_tips=None, deleted_at=None, deleting_at=None, email='helenkuli@mail.ru', employer_id=None, first_name='Елена', id=9019, is_blocked=False, last_active_at='2022-09-14 06:31:15', last_name='Куликова', last_unit_visited=23, last_visit='2022-09-14 19:45:00', last_visited_assigned_employer=None, middle_name='', order_count=8, payment_count=7, payment_sum='13200.00', phone='+79213240556', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2022-09-14 20:44:29', user_source_id=None)                                        | _doc    | [18]   |
|  9020 |            | crm_users |          | Row(__soft_deleted=0, app_first_login_at=None, app_login_at=None, birth_date=None, city_id=None, comment='', confirm_email=True, confirm_sms=True, country_id=1, created_at='2019-02-01 00:37:21', default_tips=None, deleted_at=None, deleting_at=None, email='kseniazaitseva@yandex.ru', employer_id=None, first_name='Ксения', id=9020, is_blocked=False, last_active_at=None, last_name='Ануфриева', last_unit_visited=0, last_visit='0000-00-00 00:00:00', last_visited_assigned_employer=None, middle_name='', order_count=0, payment_count=0, payment_sum='0.00', phone='+79111018045', phone_code=None, sex=0, source_company_id=1, status=None, updated_at='2020-08-19 14:42:33', user_source_id=None)                                                  | _doc    | [19]   |
```


## About final data
> - Total rows: 762844

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 47.19% |
| Phones | 99.95% |
| Birth_date | 20.03% |
| Sex | 100.00% |
| Actuality | 100.00% |



### Data sample
```
| names                      | emails                         | phones          | birth_date   |   sex | actuality   |
|:---------------------------|:-------------------------------|:----------------|:-------------|------:|:------------|
| ['Виноградова Наталья']    |                                | ['79522833306'] |              |     0 | 19.08.2020  |
| ['Васильева Наталья']      | ['nata149161@gmail.com']       | ['79217769174'] |              |     0 | 19.08.2020  |
| ['Жамбалова Галина']       | ['galdagma@yandex.ru']         | ['79818891525'] |              |     0 | 19.08.2020  |
| ['Берсенева Олеся']        | ['bersenevaolesia@icloud.com'] | ['79500401053'] |              |     0 | 19.08.2020  |
| ['Романова Вероника']      |                                | ['79312329939'] |              |     0 | 07.10.2022  |
| ['Сидорова Екатерина']     | ['mckate88@inbox.ru']          | ['79516794302'] |              |     0 | 25.10.2020  |
| ['Тружикова Ольга']        |                                | ['79118174402'] |              |     0 | 19.08.2020  |
| ['Муравская Светлана']     |                                | ['79215937889'] |              |     0 | 19.08.2020  |
| ['Писарева Женя']          | ['pisareva-z@mail.ru']         | ['79816867491'] |              |     0 | 26.08.2020  |
| ['Секерина Дарья']         | ['dasekerina@mail.ru']         | ['79102730335'] |              |     0 | 19.08.2020  |
| ['Захарова Зинаида']       | ['zinaida_om@mail.ru']         | ['79210981211'] |              |     0 | 10.12.2021  |
| ['Ложкина Марина']         | ['baby_freak@mail.ru']         | ['79216508585'] |              |     0 | 19.08.2020  |
| ['Коптева Анастасия']      | ['anothernastylia@mail.ru']    | ['79992068512'] |              |     0 | 24.04.2021  |
| ['Лобанова Дарья']         |                                | ['79500415506'] |              |     0 | 19.08.2020  |
| ['Петров Сергей']          | ['syuft@mail.ru']              | ['79117421832'] |              |     0 | 19.08.2020  |
| ['Алевтина']               |                                | ['79213440913'] |              |     0 | 06.09.2022  |
| ['Чашина Анна Валерьевна'] |                                | ['79533500361'] |              |     0 | 22.08.2022  |
| ['Бармина Оксана']         | ['oobarmina@gmail.com']        | ['79112552538'] | 12.09.1989   |     0 | 30.09.2021  |
| ['Захарова Ольга']         | ['olezha19@yandex.ru']         | ['79315829766'] |              |     0 | 19.08.2020  |
| ['Соколова Светлана']      | ['blond1981@yandex.ru']        | ['79111338603'] |              |     0 | 19.08.2020  |
```