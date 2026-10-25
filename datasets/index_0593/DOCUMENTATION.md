# Parsetron results

## About row data

> - File path: 150к.csv
> - Total rows: 153314

### Schema
```
root
 |-- id: integer (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- patronymic_name: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- sex: boolean (nullable = true)
 |-- birth_date: date (nullable = true)
 |-- nationality: string (nullable = true)
 |-- email: string (nullable = true)
 |-- address: string (nullable = true)
 |-- document_type: integer (nullable = true)
 |-- document_number: string (nullable = true)
 |-- document_issue_date: date (nullable = true)
 |-- document_issuerer: string (nullable = true)
 |-- owner: integer (nullable = true)
 |-- accountable: string (nullable = true)
 |-- hash_sum: string (nullable = true)
 |-- created_at: timestamp (nullable = true)
 |-- updated_at: timestamp (nullable = true)
 |-- deleted_at: timestamp (nullable = true)
 |-- password: string (nullable = true)
 |-- is_email_verified: boolean (nullable = true)
 |-- is_phone_verified: boolean (nullable = true)
 |-- all_notifications_disabled: boolean (nullable = true)
 |-- on_board_promo_notification_enabled: boolean (nullable = true)
 |-- off_board_promo_notification_enabled: boolean (nullable = true)
 |-- service_message_notification_enabled: boolean (nullable = true)
 |-- language: string (nullable = true)
 |-- photo_id: integer (nullable = true)
 |-- is_subscribed_to_mailing: boolean (nullable = true)
 |-- deposit_balance: double (nullable = true)
 |-- sync_id: string (nullable = true)
 |-- remote_id: string (nullable = true)
 |-- creator_node_id: string (nullable = true)
 |-- is_dummy: boolean (nullable = true)
 |-- is_first_enter: boolean (nullable = true)
 |-- vodohod_id: integer (nullable = true)
 |-- booking_id: string (nullable = true)
 |-- libra_id: string (nullable = true)
 |-- folio_id: string (nullable = true)
 |-- keycard_id: string (nullable = true)
 |-- libra_generic: string (nullable = true)
 |-- libra_guid: string (nullable = true)
 |-- libra_guest_generic: string (nullable = true)
 |-- audiopoint_notification_enabled: boolean (nullable = true)
 |-- libra_reservation_id: string (nullable = true)
 |-- current_cruise_id: integer (nullable = true)
 |-- arrival_at: string (nullable = true)
 |-- departure_at: string (nullable = true)
 |-- mindbox_id: integer (nullable = true)
 |-- westcall_id: integer (nullable = true)
 |-- westcall_login: string (nullable = true)
 |-- westcall_password: string (nullable = true)
 |-- blocked_at: timestamp (nullable = true)
 |-- westcall_expiration_date: timestamp (nullable = true)
 |-- deposit_for_payment: integer (nullable = true)
 |-- external_id: string (nullable = true)

```

### Data sample
```
|        id | first_name   | last_name   | patronymic_name   |       phone | sex   | birth_date   | nationality   | email                   | address   |   document_type | document_number   | document_issue_date   | document_issuerer   |   owner | accountable   | hash_sum   | created_at          | updated_at          | deleted_at   | password   | is_email_verified   | is_phone_verified   | all_notifications_disabled   | on_board_promo_notification_enabled   | off_board_promo_notification_enabled   | service_message_notification_enabled   | language   |   photo_id | is_subscribed_to_mailing   |   deposit_balance | sync_id                              | remote_id   | creator_node_id                      | is_dummy   | is_first_enter   |   vodohod_id | booking_id   |   libra_id | folio_id   | keycard_id   |   libra_generic | libra_guid                           | libra_guest_generic                  | audiopoint_notification_enabled   | libra_reservation_id                 |   current_cruise_id | arrival_at   | departure_at   |   mindbox_id |   westcall_id | westcall_login     | westcall_password    | blocked_at   | westcall_expiration_date   |   deposit_for_payment | external_id   |
|----------:|:-------------|:------------|:------------------|------------:|:------|:-------------|:--------------|:------------------------|:----------|----------------:|:------------------|:----------------------|:--------------------|--------:|:--------------|:-----------|:--------------------|:--------------------|:-------------|:-----------|:--------------------|:--------------------|:-----------------------------|:--------------------------------------|:---------------------------------------|:---------------------------------------|:-----------|-----------:|:---------------------------|------------------:|:-------------------------------------|:------------|:-------------------------------------|:-----------|:-----------------|-------------:|:-------------|-----------:|:-----------|:-------------|----------------:|:-------------------------------------|:-------------------------------------|:----------------------------------|:-------------------------------------|--------------------:|:-------------|:---------------|-------------:|--------------:|:-------------------|:---------------------|:-------------|:---------------------------|----------------------:|:--------------|
| 123594627 | Евгений      | Глушаков    | Витальевич        | 79529513634 | True  | 1963-12-10   | RU            | rav41997@yandex.ru      |           |               1 | 2009062467        |                       |                     |     nan |               |            | 2021-10-20 16:04:49 | 2021-11-13 09:49:04 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 2ecd6ffb-aff9-4329-8b1b-9fadde953a50 |             | 5c4b130a-9aec-4640-8069-48e1810d4122 | False      | False            |          nan |              |     180561 |            |              |         1118833 | 55065add-adf3-4574-81e0-46f67c8de276 | ffdd1605-0d70-4e4c-99eb-ad712a502960 | True                              | b06f2f76-bd4a-4aa3-b754-742e326913e0 |               12444 |              |                |          nan |        188022 | r.222.u.188022.uWj | hfNVmwZGh2LDkskb6gzh | NaT          | NaT                        |                   nan |               |
| 123574535 | Галина       | Позолотина  | Геннадьевна       | 79516419228 | False | 1957-02-25   | RU            |                         |           |               1 | 4109229670        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 11:48:28 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 37f2871b-8c5d-4f31-a240-e2c6da8e614c |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     243300 |            |              |         1143820 | 0382a488-4627-4454-9d40-aa0ca9a23132 | 70274f41-2f1f-45c3-87ee-131833098121 | True                              | 9ea6b24d-e4b3-464e-94a1-ee62b1d310bc |               12346 |              |                |          nan |        168354 | r.110.u.168354.6VS | IszcJ0nKnLE1LDKEDedW | NaT          | NaT                        |                   nan |               |
| 123574521 | Наталья      | Безбородова | Петровна          | 79117653479 | False | 1964-07-27   | RU            |                         |           |               1 | 4009817733        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 09:35:19 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 41198cdf-c296-4770-b78b-fe453cc3a24d |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     255878 |            |              |         1151808 | 62606074-f09c-4559-bac6-007583ec5158 | 77ab82c7-068e-4d9f-8ddc-2b468edd1cfc | True                              | fe8df247-40e2-4b77-ad6d-a29255f9a7ec |               12346 |              |                |          nan |        168370 | r.111.u.168370.oCi | kOliNNnRB60bxVwcXgxM | NaT          | NaT                        |                   nan |               |
| 123574540 | Елена        | Кузнецова   | Александровна     | 79111546047 | False | 1955-09-04   | RU            |                         |           |               1 | 501349648         |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 11:22:26 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 094f4d87-310e-436f-a25f-066e821cd20f |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     236291 |            |              |         1139166 | 212b4501-d80a-4e74-a76c-1a833959f40b | 0c58f995-a90b-4e7f-96c6-de74145d0234 | True                              | 89a41841-5b83-4c39-9552-ce56ace58082 |               12346 |              |                |          nan |        168344 | r.228.u.168344.IXb | bkpNIfUM0GzhrTGe0Zy2 | NaT          | NaT                        |                   nan |               |
| 123574534 | Людмила      | Шарайзина   | Абрамовна         | 79633254414 | False | 1967-10-24   | RU            | frosia67@mail.ru        |           |               1 | 4012686250        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 14:31:24 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 14a6c8c5-0200-4020-bc6f-c91ccb4055ec |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     251341 |            |              |         1148922 | 610db18a-c1fe-4ba3-a6b9-0967b2655620 | 2f952718-fab8-425f-989a-1a29778485ea | True                              | f5e7b3d9-348a-4350-a882-b09d4a5b7d4d |               12346 |              |                |          nan |        168366 | r.215.u.168366.uTQ | KN33m0vRdt7F0yKDjR17 | NaT          | NaT                        |                   nan |               |
| 123574516 | Наталья      | Смирнова    | Михайловна        |             | True  | 1954-09-08   | RU            |                         |           |               1 | 4003730502        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 10:10:14 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 27b38664-11c1-45f4-a5f3-84d09f06e42f |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     239459 |            |              |         1141318 | d57bac7c-747f-4769-b7a9-3e9686af1476 | aa34e4aa-7473-416a-8dcd-168f06153993 | True                              | 5c7e6a46-f9d2-45ae-bf61-363bca39672b |               12346 |              |                |          nan |        168348 | r.442.u.168348.cfV | VLjiJsVFDijyEfwRr8K6 | NaT          | NaT                        |                   nan |               |
| 123574522 | Анна         | Осипова     | Петровна          | 79117190800 | False | 1973-01-30   | RU            |                         |           |               1 | 4017995535        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 11:53:36 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 4d50b9fa-db44-4a75-98d9-3996eafb06c7 |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     255880 |            |              |         1151807 | 093819e9-426f-4e37-b050-e9f94e47eb88 | e2bdac3f-b2b4-48b1-8b07-00724d689c73 | True                              | a83d2143-5d0b-46b3-8166-1d691d899112 |               12346 |              |                |          nan |        168369 | r.111.u.168369.XYM | cVzewHmh7X8Ck5gQtonw | NaT          | NaT                        |                   nan |               |
| 123574525 | Антония      | Кайро       | Сергеевна         | 79213030884 | False | 1984-11-06   | RU            | konstantinovanv@mc21.ru |           |               1 | 4005429363        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 14:36:39 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 3fc1bd79-bf2a-4349-a56c-8126fd48eea8 |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     250345 |            |              |         1148200 | 51169c58-7522-4a16-8712-43e2a4caf3d4 | 9bcbc242-cc78-43ad-8224-5d288336e65b | True                              | 49ebe2a8-5a64-40a1-bc7b-0b2865a99271 |               12346 |              |                |          nan |        168364 | r.428.u.168364.gZ5 | PpTwGaxq3G870cunqWFi | NaT          | NaT                        |                   nan |               |
| 123574526 | Олег         | Кузнеченков | Андроникович      | 79213030884 | True  | 1950-08-15   | RU            | konstantinovanv@mc21.ru |           |               1 | 4002609454        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 11:23:38 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 08eecd49-ca73-4e58-ba3c-7fdbf62ec271 |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     250342 |            |              |         1148199 | d303e30d-2e99-4c32-b363-5dd5360bc302 | f8a9eafb-b03f-45f4-bc7c-288c38ecfef4 | True                              | cf328654-3c48-4ea4-a805-5b76a0aaabe6 |               12346 |              |                |          nan |        168363 | r.424.u.168363.ueP | sjQz8r5JvrsKdoTsTu4f | NaT          | NaT                        |                   nan |               |
| 123574530 | Валентина    | Жукова      | Ивановна          | 79101821926 | False | 1945-06-21   | RU            | russia@vus-tour.ru      |           |               1 | 1702495241        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 11:33:34 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | a00d7cdd-2e69-4d58-a77c-8f9ce0d508bd |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     243446 |            |              |         1143903 | 5380f089-c14d-4b97-bf8b-f04a733a2e6f | b99bfa7e-350b-4b55-9f29-1996e20f8319 | True                              | ec81c808-7918-4cb5-b044-7e14b9d15603 |               12346 |              |                |          nan |        168359 | r.342.u.168359.LiO | 3JeqDMaO705An1LyGVc9 | NaT          | NaT                        |                   nan |               |
| 123574531 | Александр    | Жуков       | Георгиевич        | 79101821926 | True  | 1944-09-29   | RU            | russia@vus-tour.ru      |           |               1 | 1702495757        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 11:12:33 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 0fa692a0-d8bf-4b45-ba83-64e6d23daff8 |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     243447 |            |              |         1143902 | 461b0708-c3ce-4a31-9b6c-b3b4e12aa299 | 510a0e64-1cb2-4a1b-b21c-fb60ee128d89 | True                              | 27b31919-e7f6-4181-a514-259994b612f0 |               12346 |              |                |          nan |        168358 | r.342.u.168358.8Up | qvR8TvvhX87e7TAAwqD0 | NaT          | NaT                        |                   nan |               |
| 123515710 | Антон        | Егоров      | Алексеевич        | 79119314516 | True  | 1983-06-07   | RU            |                         |           |               1 | 4107998038        |                       |                     |     nan |               |            | 2021-07-06 13:02:27 | 2021-10-20 11:12:37 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 06b8085d-155b-4f17-bded-31591a851ba0 |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     214212 |            |              |         1123624 | 7fc4193f-e77f-4e95-8218-d8b9011f140f | a834c68c-3b90-4344-861d-2f78d8e0cb8b | True                              | fc5e45f8-fda0-44a1-8c68-f4ba5a909d15 |                 nan |              |                |          nan |        117792 | r.231.u.117792.hwL | D9y33WNwG4BMtpsYaX1z | NaT          | NaT                        |                   nan |               |
| 123574527 | Анна         | Соколова    | Анатольевна       | 79213030884 | False | 1971-02-06   | RU            | konstantinovanv@mc21.ru |           |               1 | 4015451700        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 11:44:41 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 43485d69-c145-4f71-bb39-2fa5462f4017 |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     250343 |            |              |         1148198 | df7df793-2f64-40f0-ba0b-c409bfe3fa4e | 6320a26e-0b82-42d6-beab-6726f2f90c8b | True                              | 85de4cca-8b65-4675-93bd-a4e148a76efa |               12346 |              |                |          nan |        168362 | r.424.u.168362.9um | YrIIVOavIU2AezBsQxzR | NaT          | NaT                        |                   nan |               |
| 123574539 | Александр    | Зинченко    | Владимирович      | 79054500594 | True  | 1982-11-03   | RU            | dinok82@mail.ru         |           |               1 | 6003517548        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 12:15:10 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 8877f532-bdf2-4b84-9ea1-0374bcfacf10 |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     237195 |            |              |         1139745 | b4a87a07-275b-4708-a878-c6a7445a0cc4 | e9f1dd8a-512c-4394-839d-77de0b8dfa90 | True                              | 38c5dda1-7e4c-4d7c-8bb3-cf27088ad6a0 |               12346 |              |                |          nan |        168346 | r.419.u.168346.8lq | OVqaxRtQVO2TNOywxe3N | NaT          | NaT                        |                   nan |               |
| 123574538 | Константин   | Смирнов     | Сергеевич         |             | True  | 1978-03-13   | RU            |                         |           |               1 | 4003550399        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 12:15:29 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | bc92f4d6-8a9b-4a94-b1f9-29e8c5d279b5 |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     239458 |            |              |         1141317 | 03a76662-5900-4428-b480-e9cb6e167609 | 826a1118-c836-45e9-a633-df78d19ce108 | True                              | 9c702bc3-8e9b-4f34-a9d8-b00a246f7b21 |               12346 |              |                |          nan |        168347 | r.440.u.168347.ZS5 | 4GmZ52VVel8I2DnrjiKv | NaT          | NaT                        |                   nan |               |
| 123574524 | Александр    | Кайро       | Викторович        | 79213030884 | True  | 1982-09-02   | RU            |                         |           |               1 | 0                 |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 13:03:06 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | ee218d9e-0df5-4764-aae8-a27a04370eea |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     250344 |            |              |         1148201 | db8d06a6-e945-47f5-9d70-516072ee526b | 750c8b53-edb3-4bfb-bdb6-99042a29d1cd | True                              | 6b63907e-0a4b-4bb7-8322-c086b00eca13 |               12346 |              |                |          nan |        168365 | r.428.u.168365.w2Y | 5YXcuDDtOm5BqfLRPQyR | NaT          | NaT                        |                   nan |               |
| 123574528 | Николай      | Власов      | Петрович          | 79117007300 | True  | 1954-10-27   | RU            |                         |           |               1 | 3702349726        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 09:07:50 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | b70a6afc-4aa0-4f95-8fea-af8f5806f528 |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     249235 |            |              |         1147525 | e4bf22c8-1836-4daa-8731-ba86f7b09aa5 | 8ef325a0-7c52-4863-a63d-f0a06bf5b245 | True                              | bc72383d-2f86-4da8-9428-ce2c7c1399b9 |               12346 |              |                |          nan |        168361 | r.227.u.168361.5Io | gFO4wKDsJHapremLrovk | NaT          | NaT                        |                   nan |               |
| 123574517 | Надежда      | Алексеева   | Ивановна          |             | True  | 1947-01-05   | RU            |                         |           |               1 | 4004283863        |                       |                     |     nan |               |            | 2021-09-10 20:08:43 | 2021-10-20 11:20:46 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 6c1e3769-06d0-4f28-9b86-5e405f687343 |             | d5b7b1b0-1e95-443b-8d49-c1b47eda023c | False      | False            |          nan |              |     239460 |            |              |         1141319 | 2c585c29-efdd-4559-ae09-b302680c7775 | ba20ecc0-e994-4d74-aaa2-fc3ab1a1ef34 | True                              | 54508500-7561-4e6f-8cfa-659fe74deab2 |               12346 |              |                |          nan |        168349 | r.444.u.168349.ltx | os7gK4sCrPDEQgmLUOfN | NaT          | NaT                        |                   nan |               |
| 123594642 | Ирина        | Лебедева    | Николаевна        | 89688946860 | False | 1960-04-02   | RU            | dvask@mail.ru           |           |               1 | 4508140185        |                       |                     |     nan |               |            | 2021-10-20 16:04:49 | 2021-11-13 07:56:24 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   |            |        nan | False                      |                 0 | 796817ad-37e9-46c5-b219-7cc72bb30541 |             | 5c4b130a-9aec-4640-8069-48e1810d4122 | False      | False            |          nan |              |     180579 |            |              |         1118851 | 396ffd01-5c98-4e98-95b9-2d96c77a17da | 83507f8c-c8c4-435c-b553-fbf7dd49109c | True                              | 5dc83696-1394-4fd2-8aa6-e26374e0ed65 |               12444 |              |                |          nan |        188037 | r.204.u.188037.xIT | GDOGnNpzgJmXHH2CrRRp | NaT          | NaT                        |                   nan |               |
| 123594639 | Сергей       | Волос       | Михайлович        |             | True  | 1952-01-28   | RU            |                         |           |               1 | 45 05 500009      |                       |                     |     nan |               |            | 2021-10-20 16:04:49 | 2021-11-13 06:57:45 | NaT          |            | False               | False               | False                        | True                                  | True                                   | True                                   | RUS        |        nan | False                      |                 0 | 4b3f9758-7a54-41d0-a7df-b0343f2586a7 |             | 5c4b130a-9aec-4640-8069-48e1810d4122 | False      | False            |          nan |              |     180578 |            |              |         1118848 | ee0fa1ea-757f-4f77-86b4-5cdec99f916d | db5bffb0-b58e-4be2-9540-09db9c05b1eb | True                              | bce6c8e3-df20-4d64-9377-6866d01ccd8e |               12444 |              |                |          nan |        188034 | r.406.u.188034.PeG | NzQlEWIBF5hPu3CRY5K4 | NaT          | NaT                        |                   nan |               |
```

> - File path: 150к (2).csv
> - Total rows: 109538

### Schema
```
root
 |-- fio: string (nullable = true)
 |-- tel: double (nullable = true)
 |-- comment: string (nullable = true)
 |-- dob: string (nullable = true)
 |-- nationality: string (nullable = true)
 |-- email: string (nullable = true)
 |-- address: string (nullable = true)
 |-- passport_child: string (nullable = true)
 |-- passport: string (nullable = true)
 |-- passport_issuerer: string (nullable = true)
 |-- data: string (nullable = true)

```

### Data sample
```
| fio                                |           tel | comment   | dob        | nationality   | email                                    | address                                                                              | passport_child   | passport      | passport_issuerer                                                                 | data       |
|:-----------------------------------|--------------:|:----------|:-----------|:--------------|:-----------------------------------------|:-------------------------------------------------------------------------------------|:-----------------|:--------------|:----------------------------------------------------------------------------------|:-----------|
| романов артема александрович       |   7.92679e+10 |           |            |               | romanova-ganievami@sch2120.yaconnect.com |                                                                                      |                  | VII-МЮ 693725 |                                                                                   | 2021-07-10 |
| романова ксения александровна      |   7.92679e+10 |           |            |               | romanova-ganievami@sch2120.yaconnect.com |                                                                                      |                  | V-ИК 701605   |                                                                                   | 2021-07-10 |
| романова-ганиева мария ибрагимовна |   7.92679e+10 |           | 18.12.1984 |               | romanova-ganievami@sch2120.yaconnect.com | Москва, Филимонковское поселение, поселок Марьино, Березовая ул, дом 9 кор. 1. кв. 1 |                  | 4610957285    | ТП 2 в гор. Одинцово ОУФМС России по Московской обл. в Одинцовском рне 2010-03-27 | 2021-07-11 |
| романова-ганиева мария ибрагимовна |   7.92679e+10 |           | 18.12.1984 | RU            | romanova-ganievami@sch2120.yaconnect.com |                                                                                      |                  | 4610957285    |                                                                                   | 2021-07-10 |
| ганиева зарина ибрагимовна         |   7.92679e+10 |           | 13.01.1978 | RU            | romanova-ganievami@sch2120.yaconnect.com |                                                                                      |                  | 4603663883    |                                                                                   | 2021-07-10 |
| кубракова нина александровна       | nan           |           | 23.05.1945 | RU            | kinematics.nina.aleksandrovna@gmail.com  |                                                                                      |                  | 1801541317    |                                                                                   | 2021-05-26 |
| красильников сергей сергеевич      |   7.98174e+10 |           | 13.07.1986 | RU            | krasilnikov.sergey.sergeevich@gmail.com  |                                                                                      |                  | 1106470684    |                                                                                   | 2021-05-26 |
| лукьянова наталья викторовна       |   7.9117e+10  |           | 12.02.1971 | RU            | natalia.lukiyanova.kallstrom@gmail.com   |                                                                                      |                  | 4015454626    |                                                                                   | 2021-08-10 |
| глушкова алена романовна           |   7.91051e+10 |           |            |               | pankratovaolgastanislavovna@gmail.com    |                                                                                      |                  | I-ОБ 894000   |                                                                                   | 2021-08-12 |
| зубкова валентина яковлевна        |   7.91051e+10 |           | 16.04.1951 | RU            | pankratovaolgastanislavovna@gmail.com    |                                                                                      |                  | 6111738509    |                                                                                   | 2021-08-10 |
| панкратова ольга станиславовна     |   7.91051e+10 |           | 29.03.1961 | RU            | pankratovaolgastanislavovna@gmail.com    |                                                                                      |                  | 6106329238    |                                                                                   | 2021-08-10 |
| калинина валентина андреевна       |   7.91156e+10 |           |            |               | valentina.kalininadyadkina@gmail.com     | Архангельск Московский 43 /3-280                                                     |                  |               |                                                                                   | 2021-07-26 |
| галашева лидия николаевна          |   7.90955e+10 |           | 04.09.1947 | RU            | valentina.kalininadyadkina@gmail.com     |                                                                                      |                  | 1101345099    |                                                                                   | 2021-09-29 |
| квашонкин валерий геннадьевич      |   7.92172e+10 |           | 17.06.1952 | RU            | valentina.kalininadyadkina@gmail.com     |                                                                                      |                  | 1900198994    |                                                                                   | 2021-09-29 |
| калинина валентина андреевна       |   7.90955e+10 |           | 21.07.1954 | RU            | valentina.kalininadyadkina@gmail.com     |                                                                                      |                  | 1101338080    |                                                                                   | 2021-09-29 |
| иванова людмила андреевна          |   7.9119e+10  |           | 19.05.1950 | RU            | valentina.kalininadyadkina@gmail.com     |                                                                                      |                  | 4108090062    |                                                                                   | 2021-09-29 |
| михайленко олег валентинович       |   7.91855e+10 |           | 19.05.1972 |               | viktoria.mikhaylenko@lawpartners.ru      | г.Ростов-на-Дону, ул.Красноармейская 240 кв.89                                       |                  | 6017135623    | Отделением №2 отдела УФМС России по РО в г.Ростове-на-Дону 2017-06-05             | 2021-07-25 |
| мамаева александра анатольевна     |   7.91122e+10 |           | 27.10.2007 |               | mamaeva.maria.anatolyevna@gmail.com      |                                                                                      |                  | II-АК 599291  |                                                                                   | 2021-08-07 |
| михайленко виктория валерьевна     | nan           |           | 20.02.1987 | RU            | viktoria.mikhaylenko@lawpartners.ru      |                                                                                      |                  | 6006699130    |                                                                                   | 2021-07-24 |
| михайленко олег валентинович       | nan           |           | 19.05.1972 | RU            | viktoria.mikhaylenko@lawpartners.ru      |                                                                                      |                  | 6017135623    |                                                                                   | 2021-07-24 |
```

> - File path: База пациентов_из_xls.csv
> - Total rows: 980254

### Schema
```
root
 |-- fio: string (nullable = true)
 |-- dob: string (nullable = true)
 |-- tel: long (nullable = true)
 |-- email: string (nullable = true)
 |-- comment: string (nullable = true)

```

### Data sample
```
| fio                              | dob        |          tel | email                    | comment                                                                                                                |
|:---------------------------------|:-----------|-------------:|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| махкамов бахром алимжанович      | 04.07.1986 | 998974146559 | makhkamovba@trcont.ru    | Дата первого визита: 15.04.2022 Сумма оплаченных счетов пациента: 1600                                                 |
| асхатова дарья                   | 20.07.2007 | 996999999967 |                          | Дата первого визита: 09.05.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 35601 |
| асхатова дарья                   | 20.07.2001 | 996999999967 |                          | Дата первого визита: 28.08.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 5900  |
| найзабекова альбина              | 04.09.1990 | 996999999962 |                          | Дата первого визита: 09.01.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 23765 |
| сыдыков бакытбек                 | 18.07.1970 | 996999999555 |                          | Дата первого визита: 12.08.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 34200 |
| колосова анна                    | 06.08.1995 | 996999996556 | marshmallowuka@gmail.com | Дата первого визита: 03.09.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 22545 |
| ибрагимова анна васильевна       | 06.08.1995 | 996999996556 |                          | Дата первого визита: 08.10.2024 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 11255 |
| уланбек кызы бегайым             | 19.06.1991 | 996999887010 |                          | Дата первого визита: 26.08.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 40355 |
| женишев ахмад                    | 27.04.2004 | 996999866661 | azhenishev@gmail.com     | Дата первого визита: 16.08.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 8050  |
| хихиза фатима                    | 21.09.1967 | 996999797993 |                          | Дата первого визита: 29.04.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 27045 |
| марс жылдыз                      | 29.07.2002 | 996999666147 |                          | Сумма оплаченных счетов пациента: 5680                                                                                 |
| исакова алиса                    | 05.02.1997 | 996999516201 |                          | Дата первого визита: 23.06.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 16655 |
| таалайбеков илай                 | 25.07.2022 | 996999500148 |                          | Дата первого визита: 15.08.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 9000  |
| алмазбеков аманбай кутманбекович | 10.04.2018 | 996999453045 |                          | Дата первого визита: 14.10.2024 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 4220  |
| калилова айгерим талайбекова     | 24.08.1996 | 996999445688 |                          | Дата первого визита: 23.01.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 14000 |
| амангулов ормон                  | 03.08.1987 | 996999421111 |                          | Дата первого визита: 02.04.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 25680 |
| махмудов алишер                  | 26.02.1985 | 996999400900 | kaset.kawe@gmail.com     | Дата первого визита: 16.01.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 26844 |
| алымкулова алтынай               | 22.02.1987 | 996999301300 |                          | Дата первого визита: 16.06.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 18015 |
| неговора наталия                 | 06.10.1979 | 996999300600 |                          | Дата первого визита: 10.06.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 9780  |
| брычеев тимур                    | 23.06.2015 | 996999300600 |                          | Дата первого визита: 29.05.2025 Офис первого визита: ФМО Бишкек Байтик-Баатыра Сумма оплаченных счетов пациента: 15780 |
```


## About final data

### Schema
```
root
 |-- names: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- birth_date: string (nullable = true)
 |-- sex: integer (nullable = true)
 |-- emails: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- phones: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- actuality: date (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Birth_date | 98.16% |
| Sex | 12.01% |
| Emails | 79.89% |
| Phones | 84.81% |
| Address | 0.63% |
| Documents | 20.00% |
| Actuality | 8.50% |



### Data sample
```
| names                               | birth_date   |   sex | emails                      | phones          | address   | documents                                                                                                                 | actuality   |
|:------------------------------------|:-------------|------:|:----------------------------|:----------------|:----------|:--------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Глушаков Евгений Витальевич']     | 10.12.1963   |     1 | ['rav41997@yandex.ru']      | ['79529513634'] |           | [Row(type=0, serial='2009062467', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Позолотина Галина Геннадьевна']   | 25.02.1957   |     0 |                             | ['79516419228'] |           | [Row(type=0, serial='4109229670', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Безбородова Наталья Петровна']    | 27.07.1964   |     0 |                             | ['79117653479'] |           | [Row(type=0, serial='4009817733', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Кузнецова Елена Александровна']   | 04.09.1955   |     0 |                             | ['79111546047'] |           | [Row(type=4, serial='501349648', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)]  |             |
| ['Шарайзина Людмила Абрамовна']     | 24.10.1967   |     0 | ['frosia67@mail.ru']        | ['79633254414'] |           | [Row(type=0, serial='4012686250', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Смирнова Наталья Михайловна']     | 08.09.1954   |     1 |                             |                 |           | [Row(type=0, serial='4003730502', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Осипова Анна Петровна']           | 30.01.1973   |     0 |                             | ['79117190800'] |           | [Row(type=0, serial='4017995535', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Кайро Антония Сергеевна']         | 06.11.1984   |     0 | ['konstantinovanv@mc21.ru'] | ['79213030884'] |           | [Row(type=0, serial='4005429363', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Кузнеченков Олег Андроникович']   | 15.08.1950   |     1 | ['konstantinovanv@mc21.ru'] | ['79213030884'] |           | [Row(type=0, serial='4002609454', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Жукова Валентина Ивановна']       | 21.06.1945   |     0 | ['russia@vus-tour.ru']      | ['79101821926'] |           | [Row(type=0, serial='1702495241', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Жуков Александр Георгиевич']      | 29.09.1944   |     1 | ['russia@vus-tour.ru']      | ['79101821926'] |           | [Row(type=0, serial='1702495757', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Егоров Антон Алексеевич']         | 07.06.1983   |     1 |                             | ['79119314516'] |           | [Row(type=0, serial='4107998038', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Соколова Анна Анатольевна']       | 06.02.1971   |     0 | ['konstantinovanv@mc21.ru'] | ['79213030884'] |           | [Row(type=0, serial='4015451700', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Зинченко Александр Владимирович'] | 03.11.1982   |     1 | ['dinok82@mail.ru']         | ['79054500594'] |           | [Row(type=0, serial='6003517548', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Смирнов Константин Сергеевич']    | 13.03.1978   |     1 |                             |                 |           | [Row(type=0, serial='4003550399', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Кайро Александр Викторович']      | 02.09.1982   |     1 |                             | ['79213030884'] |           |                                                                                                                           |             |
| ['Власов Николай Петрович']         | 27.10.1954   |     1 |                             | ['79117007300'] |           | [Row(type=0, serial='3702349726', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Алексеева Надежда Ивановна']      | 05.01.1947   |     1 |                             |                 |           | [Row(type=0, serial='4004283863', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Лебедева Ирина Николаевна']       | 02.04.1960   |     0 | ['dvask@mail.ru']           | ['79688946860'] |           | [Row(type=0, serial='4508140185', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Волос Сергей Михайлович']         | 28.01.1952   |     1 |                             |                 |           | [Row(type=0, serial='4505500009', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
```