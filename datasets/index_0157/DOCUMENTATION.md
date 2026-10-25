# Parsetron results

## About row data

> - File path: b_sale_order.csv
> - Total rows: 55806

### Schema
```
root
 |-- ID: string (nullable = true)
 |-- LID: string (nullable = true)
 |-- PERSON_TYPE_ID: string (nullable = true)
 |-- PAYED: string (nullable = true)
 |-- DATE_PAYED: string (nullable = true)
 |-- EMP_PAYED_ID: string (nullable = true)
 |-- CANCELED: string (nullable = true)
 |-- DATE_CANCELED: string (nullable = true)
 |-- EMP_CANCELED_ID: string (nullable = true)
 |-- REASON_CANCELED: string (nullable = true)
 |-- STATUS_ID: string (nullable = true)
 |-- DATE_STATUS: string (nullable = true)
 |-- EMP_STATUS_ID: string (nullable = true)
 |-- PRICE_DELIVERY: string (nullable = true)
 |-- PRICE_PAYMENT: string (nullable = true)
 |-- ALLOW_DELIVERY: string (nullable = true)
 |-- DATE_ALLOW_DELIVERY: string (nullable = true)
 |-- EMP_ALLOW_DELIVERY_ID: string (nullable = true)
 |-- DEDUCTED: string (nullable = true)
 |-- DATE_DEDUCTED: string (nullable = true)
 |-- EMP_DEDUCTED_ID: string (nullable = true)
 |-- REASON_UNDO_DEDUCTED: string (nullable = true)
 |-- MARKED: string (nullable = true)
 |-- DATE_MARKED: string (nullable = true)
 |-- EMP_MARKED_ID: string (nullable = true)
 |-- REASON_MARKED: string (nullable = true)
 |-- RESERVED: string (nullable = true)
 |-- PRICE: string (nullable = true)
 |-- CURRENCY: string (nullable = true)
 |-- DISCOUNT_VALUE: string (nullable = true)
 |-- USER_ID: string (nullable = true)
 |-- PAY_SYSTEM_ID: string (nullable = true)
 |-- DELIVERY_ID: string (nullable = true)
 |-- DATE_INSERT: string (nullable = true)
 |-- DATE_UPDATE: string (nullable = true)
 |-- USER_DESCRIPTION: string (nullable = true)
 |-- ADDITIONAL_INFO: string (nullable = true)
 |-- PS_STATUS: string (nullable = true)
 |-- PS_STATUS_CODE: string (nullable = true)
 |-- PS_STATUS_DESCRIPTION: string (nullable = true)
 |-- PS_STATUS_MESSAGE: string (nullable = true)
 |-- PS_SUM: string (nullable = true)
 |-- PS_CURRENCY: string (nullable = true)
 |-- PS_RESPONSE_DATE: string (nullable = true)
 |-- COMMENTS: string (nullable = true)
 |-- TAX_VALUE: string (nullable = true)
 |-- STAT_GID: string (nullable = true)
 |-- SUM_PAID: string (nullable = true)
 |-- RECURRING_ID: string (nullable = true)
 |-- PAY_VOUCHER_NUM: string (nullable = true)
 |-- PAY_VOUCHER_DATE: string (nullable = true)
 |-- LOCKED_BY: string (nullable = true)
 |-- DATE_LOCK: string (nullable = true)
 |-- RECOUNT_FLAG: string (nullable = true)
 |-- AFFILIATE_ID: string (nullable = true)
 |-- DELIVERY_DOC_NUM: string (nullable = true)
 |-- DELIVERY_DOC_DATE: string (nullable = true)
 |-- UPDATED_1C: string (nullable = true)
 |-- STORE_ID: string (nullable = true)
 |-- ORDER_TOPIC: string (nullable = true)
 |-- CREATED_BY: string (nullable = true)
 |-- RESPONSIBLE_ID: string (nullable = true)
 |-- DATE_PAY_BEFORE: string (nullable = true)
 |-- DATE_BILL: string (nullable = true)
 |-- ACCOUNT_NUMBER: string (nullable = true)
 |-- TRACKING_NUMBER: string (nullable = true)
 |-- XML_ID: string (nullable = true)
 |-- ID_1C: string (nullable = true)
 |-- VERSION_1C: string (nullable = true)
 |-- VERSION: integer (nullable = true)
 |-- EXTERNAL_ORDER: string (nullable = true)
 |-- BX_USER_ID: string (nullable = true)
 |-- COMPANY_ID: string (nullable = true)
 |-- IS_RECURRING: string (nullable = true)
 |-- RUNNING: string (nullable = true)
 |-- SEARCH_CONTENT: string (nullable = true)
 |-- IS_SYNC_B24: string (nullable = true)

```

### Data sample
```
|   ID | LID   |   PERSON_TYPE_ID | PAYED   | DATE_PAYED          | EMP_PAYED_ID   | CANCELED   | DATE_CANCELED       | EMP_CANCELED_ID   | REASON_CANCELED   | STATUS_ID   | DATE_STATUS         |   EMP_STATUS_ID |   PRICE_DELIVERY |   PRICE_PAYMENT | ALLOW_DELIVERY   | DATE_ALLOW_DELIVERY   | EMP_ALLOW_DELIVERY_ID   | DEDUCTED   | DATE_DEDUCTED   | EMP_DEDUCTED_ID   | REASON_UNDO_DEDUCTED   | MARKED   | DATE_MARKED   |   EMP_MARKED_ID | REASON_MARKED   | RESERVED   |    PRICE | CURRENCY   |   DISCOUNT_VALUE |   USER_ID |   PAY_SYSTEM_ID |   DELIVERY_ID | DATE_INSERT         | DATE_UPDATE         | USER_DESCRIPTION   | ADDITIONAL_INFO   | PS_STATUS   | PS_STATUS_CODE   | PS_STATUS_DESCRIPTION   | PS_STATUS_MESSAGE   | PS_SUM   | PS_CURRENCY   | PS_RESPONSE_DATE   | COMMENTS   |   TAX_VALUE | STAT_GID   |   SUM_PAID | RECURRING_ID   | PAY_VOUCHER_NUM   | PAY_VOUCHER_DATE   | LOCKED_BY   | DATE_LOCK           | RECOUNT_FLAG   | AFFILIATE_ID   | DELIVERY_DOC_NUM   | DELIVERY_DOC_DATE   | UPDATED_1C   | STORE_ID   | ORDER_TOPIC   |   CREATED_BY | RESPONSIBLE_ID   | DATE_PAY_BEFORE   | DATE_BILL   |   ACCOUNT_NUMBER | TRACKING_NUMBER   | XML_ID                              | ID_1C   | VERSION_1C   |   VERSION | EXTERNAL_ORDER   | BX_USER_ID   | COMPANY_ID   | IS_RECURRING   | RUNNING   | SEARCH_CONTENT   | IS_SYNC_B24   |
|-----:|:------|-----------------:|:--------|:--------------------|:---------------|:-----------|:--------------------|:------------------|:------------------|:------------|:--------------------|----------------:|-----------------:|----------------:|:-----------------|:----------------------|:------------------------|:-----------|:----------------|:------------------|:-----------------------|:---------|:--------------|----------------:|:----------------|:-----------|---------:|:-----------|-----------------:|----------:|----------------:|--------------:|:--------------------|:--------------------|:-------------------|:------------------|:------------|:-----------------|:------------------------|:--------------------|:---------|:--------------|:-------------------|:-----------|------------:|:-----------|-----------:|:---------------|:------------------|:-------------------|:------------|:--------------------|:---------------|:---------------|:-------------------|:--------------------|:-------------|:-----------|:--------------|-------------:|:-----------------|:------------------|:------------|-----------------:|:------------------|:------------------------------------|:--------|:-------------|----------:|:-----------------|:-------------|:-------------|:---------------|:----------|:-----------------|:--------------|
|    1 | s1    |                1 | Y       | 2016-10-10 14:52:13 | 1              | N          | NULL                | NULL              | NULL              | F           | 2016-10-10 14:52:14 |               1 |                0 |               0 | Y                | 2016-10-10 14:52:13   | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   6097   | RUB        |                0 |         1 |               1 |             1 | 2016-10-10 14:52:12 | 2017-12-28 22:47:13 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |     6097   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |                1 | NULL              | bx_300b185a88790c2f11bd929ccf79fa63 | NULL    | NULL         |        12 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|    2 | s1    |                1 | Y       | 2016-10-10 14:52:15 | 1              | N          | NULL                | NULL              | NULL              | F           | 2016-10-10 14:52:15 |               1 |                0 |               0 | Y                | 2016-10-10 14:52:15   | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   4550.4 | RUB        |                0 |         1 |               1 |             1 | 2016-10-10 14:52:14 | 2017-12-28 22:47:13 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |     4550.4 | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |                2 | NULL              | bx_108be96b9e388b1fb84533976e66721e | NULL    | NULL         |        12 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|    3 | s1    |                1 | Y       | 2016-10-10 14:52:16 | 1              | N          | NULL                | NULL              | NULL              | P           | 2016-10-10 14:52:16 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   4312.1 | RUB        |                0 |         1 |               1 |             1 | 2016-10-10 14:52:15 | 2017-12-28 22:47:14 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |     4312.1 | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |                3 | NULL              | bx_72dc0c76bcbd2624c17dbb84d2c6d7fe | NULL    | NULL         |        10 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|    4 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2016-10-10 14:52:16 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   2199   | RUB        |                0 |         1 |               1 |             1 | 2016-10-10 14:52:16 | 2017-12-28 22:47:14 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |                4 | NULL              | bx_388e286e70f597a7413bf2a4151aa3f1 | NULL    | NULL         |         5 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|    5 | s1    |                1 | N       | NULL                | NULL           | N          | 2016-10-10 14:52:18 | 1                 | NULL              | N           | 2016-10-10 14:52:17 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   5087.1 | RUB        |                0 |         1 |               1 |             1 | 2016-10-10 14:52:17 | 2017-12-28 22:47:14 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |                5 | NULL              | bx_ebc777848d436e72f851d9b66d659be4 | NULL    | NULL         |         8 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|    6 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-13 09:21:32 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          | 141318   | RUB        |                0 |         1 |              14 |            16 | 2017-02-13 09:21:31 | 2017-12-28 22:47:14 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | 1           | 2017-02-13 09:21:47 | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |                6 | NULL              | bx_65dab790648bda8c828913f0d6e7640d | NULL    | NULL         |         9 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|    7 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-17 16:00:33 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |  23419.2 | RUB        |                0 |         1 |               1 |             1 | 2017-02-17 16:00:32 | 2017-12-28 22:47:14 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | 1           | 2017-02-17 16:08:30 | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |                7 | NULL              | bx_7725e1c03abc992f73a5c73748b23a98 | NULL    | NULL         |         5 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|    8 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-17 16:27:07 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |  23419.2 | RUB        |                0 |         1 |               1 |             1 | 2017-02-17 16:27:07 | 2017-12-28 22:47:15 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |                8 | NULL              | bx_8204efa6c060edf62bef13b5239ea6f3 | NULL    | NULL         |         4 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|    9 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-17 17:21:41 |               1 |              490 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   8526   | RUB        |                0 |         1 |               1 |            19 | 2017-02-17 17:21:41 | 2017-12-28 22:47:15 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |                9 | NULL              | bx_7373dbe8bc1da44fc38152cf779b9f75 | NULL    | NULL         |         5 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   10 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-17 17:25:46 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |  23419.2 | RUB        |                0 |         1 |               1 |            16 | 2017-02-17 17:25:46 | 2017-12-28 22:47:15 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |               10 | NULL              | bx_f41b2678c8a28f547ecd94f665ca199e | NULL    | NULL         |         4 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   11 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-17 17:34:47 |               1 |             1000 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   7400   | RUB        |                0 |         1 |               1 |            20 | 2017-02-17 17:34:47 | 2017-12-28 22:47:15 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |               11 | NULL              | bx_3207a8de18ac92744b9aec40a08335c3 | NULL    | NULL         |         5 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   12 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-17 21:40:31 |               1 |              490 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   9490   | RUB        |                0 |         1 |               7 |            19 | 2017-02-17 21:40:30 | 2017-12-28 22:47:15 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |               12 | NULL              | bx_4c9f40522239d130f922001944b563ca | NULL    | NULL         |         7 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   13 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-17 21:45:26 |               1 |              490 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   9490   | RUB        |                0 |         1 |               7 |            19 | 2017-02-17 21:45:26 | 2017-12-28 22:47:15 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |               13 | NULL              | bx_45b4924740ef9794b5c774899c8b8783 | NULL    | NULL         |         5 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   14 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-17 21:48:31 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   9000   | RUB        |                0 |         1 |               1 |            16 | 2017-02-17 21:48:31 | 2017-12-28 22:47:16 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |               14 | NULL              | bx_5bff22d080afbc2e0091eeee526e3916 | NULL    | NULL         |         4 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   15 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-17 21:49:32 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |  23419.2 | RUB        |                0 |         1 |               7 |            25 | 2017-02-17 21:49:32 | 2017-12-28 22:47:16 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |               15 | NULL              | bx_86760fb1460f3736acc8e216aac5c6a2 | NULL    | NULL         |         4 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   16 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-02-21 10:07:45 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |   9340   | RUB        |                0 |         1 |               1 |            16 | 2017-02-21 10:07:45 | 2017-12-28 22:47:16 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |               16 | NULL              | bx_a42e7145289487600239b47b077a720a | NULL    | NULL         |         4 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   17 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-03-01 15:31:37 |               3 |              490 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |  16562   | RUB        |                0 |         3 |              15 |            19 | 2017-03-01 15:31:37 | 2017-12-28 22:47:16 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | 1           | 2017-03-14 09:23:09 | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            3 | NULL             | NULL              | NULL        |               17 | NULL              | bx_892bef47ac74a5d7eafff357abb12f6a | NULL    | NULL         |         5 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   18 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-03-14 09:25:11 |               1 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |  31730   | RUB        |                0 |         1 |               1 |            24 | 2017-03-14 09:25:10 | 2017-12-28 22:47:16 | test               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | 1           | 2017-03-14 09:59:42 | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            1 | NULL             | NULL              | NULL        |               18 | NULL              | bx_d236c2ed51c64f0685eab277e6581abb | NULL    | NULL         |         8 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   19 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-03-16 17:29:35 |               5 |                0 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |  36020   | RUB        |                0 |         5 |               7 |            16 | 2017-03-16 17:29:35 | 2017-12-28 22:47:16 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            5 | NULL             | NULL              | NULL        |               19 | NULL              | bx_bf4bf4593824b1ff7c25125e568d7d4b | NULL    | NULL         |         6 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
|   20 | s1    |                1 | N       | NULL                | NULL           | N          | NULL                | NULL              | NULL              | N           | 2017-04-07 13:55:52 |               6 |             1000 |               0 | N                | NULL                  | NULL                    | N          | NULL            | NULL              | NULL                   | N        | NULL          |               0 |                 | N          |  82200   | RUB        |                0 |         6 |               1 |            20 | 2017-04-07 13:55:51 | 2017-12-28 22:47:17 | NULL               | NULL              | NULL        | NULL             | NULL                    | NULL                | NULL     | NULL          | NULL               | NULL       |           0 | NULL       |        0   | NULL           | NULL              | NULL               | NULL        | NULL                | Y              | NULL           | NULL               | NULL                | N            | NULL       | NULL          |            6 | NULL             | NULL              | NULL        |               20 | NULL              | bx_b5cb564af2b9388f809923d9937547bb | NULL    | NULL         |         6 | N                | NULL         | NULL         | N              | N         | NULL             | N             |
```

> - File path: b_sale_order_props_value.csv
> - Total rows: 186964

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- ORDER_ID: integer (nullable = true)
 |-- ORDER_PROPS_ID: integer (nullable = true)
 |-- NAME: string (nullable = true)
 |-- VALUE: string (nullable = true)
 |-- CODE: string (nullable = true)
 |-- XML_ID: string (nullable = true)
 |-- ENTITY_ID: integer (nullable = true)
 |-- ENTITY_TYPE: string (nullable = true)

```

### Data sample
```
|   ID |   ORDER_ID |   ORDER_PROPS_ID | NAME           | VALUE               | CODE     | XML_ID                              |   ENTITY_ID | ENTITY_TYPE   |
|-----:|-----------:|-----------------:|:---------------|:--------------------|:---------|:------------------------------------|------------:|:--------------|
|    1 |          1 |                1 | Ф.И.О.         | Иванов Петр         | FIO      | bx_f137cbf9f73c6af64ace7ac96e62be47 |           1 | ORDER         |
|    2 |          1 |                2 | E-Mail         | example@example.com | EMAIL    | bx_0c3a965ecf2cbe163ff6fdbbdec3dff3 |           1 | ORDER         |
|    3 |          1 |                3 | Телефон        | 8 495 2312121       | PHONE    | bx_d7d0497f9087ac76f82d70a7698cda6f |           1 | ORDER         |
|    4 |          1 |                4 | Индекс         | 101000              | ZIP      | bx_648d69eea6077c08491bb428b43658af |           1 | ORDER         |
|    5 |          1 |                5 | Город          | Москва              | CITY     | bx_01b4e16afb118b83412af7903dcfc9f2 |           1 | ORDER         |
|    6 |          1 |                6 | Местоположение | 0000073738          | LOCATION | bx_385f67e5e6a691a583f52aa457197a4e |           1 | ORDER         |
|    7 |          1 |                7 | Адрес доставки | ул. Первомайская 93 | ADDRESS  | bx_1b734c03f83fd4205ee049aff4aedba3 |           1 | ORDER         |
|    8 |          2 |                1 | Ф.И.О.         | Иванов Петр         | FIO      | bx_38c9447a8d41a61d3f7b3b05d744b2a8 |           2 | ORDER         |
|    9 |          2 |                2 | E-Mail         | example@example.com | EMAIL    | bx_b6d434f1670d48b806145c405a5f5577 |           2 | ORDER         |
|   10 |          2 |                3 | Телефон        | 8 495 2312121       | PHONE    | bx_9274c90c7a44b78f035dee10115f5a09 |           2 | ORDER         |
|   11 |          2 |                4 | Индекс         | 101000              | ZIP      | bx_27eee190fadd7159335dcc7fd53af236 |           2 | ORDER         |
|   12 |          2 |                5 | Город          | Москва              | CITY     | bx_196df2eb4cae09ea4be52b1b5dec72a0 |           2 | ORDER         |
|   13 |          2 |                6 | Местоположение | 0000073738          | LOCATION | bx_1c1e5e101118b83385b413c827559e31 |           2 | ORDER         |
|   14 |          2 |                7 | Адрес доставки | ул. Первомайская 93 | ADDRESS  | bx_e80d3c1d53e7c6aec08500c7fb2345e7 |           2 | ORDER         |
|   15 |          3 |                1 | Ф.И.О.         | Иванов Петр         | FIO      | bx_97523a314edce0486b16347798f5b45b |           3 | ORDER         |
|   16 |          3 |                2 | E-Mail         | example@example.com | EMAIL    | bx_29c22fc4a4cd6e115f8bcf612924f427 |           3 | ORDER         |
|   17 |          3 |                3 | Телефон        | 8 495 2312121       | PHONE    | bx_66cf7e4c621564287ef6a0d04ab75a84 |           3 | ORDER         |
|   18 |          3 |                4 | Индекс         | 101000              | ZIP      | bx_07325d37ce734fd66b84c3d9d01a2e6e |           3 | ORDER         |
|   19 |          3 |                5 | Город          | Москва              | CITY     | bx_02775254591cc725368377df90bd355c |           3 | ORDER         |
|   20 |          3 |                6 | Местоположение | 0000073738          | LOCATION | bx_bafb4d1936145a394b5984aed8e58514 |           3 | ORDER         |
```

> - File path: b_user.csv
> - Total rows: 3112735

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- TIMESTAMP_X: string (nullable = true)
 |-- LOGIN: string (nullable = true)
 |-- PASSWORD: string (nullable = true)
 |-- CHECKWORD: string (nullable = true)
 |-- ACTIVE: string (nullable = true)
 |-- NAME: string (nullable = true)
 |-- LAST_NAME: string (nullable = true)
 |-- EMAIL: string (nullable = true)
 |-- LAST_LOGIN: string (nullable = true)
 |-- DATE_REGISTER: timestamp (nullable = true)
 |-- LID: string (nullable = true)
 |-- PERSONAL_PROFESSION: string (nullable = true)
 |-- PERSONAL_WWW: string (nullable = true)
 |-- PERSONAL_ICQ: string (nullable = true)
 |-- PERSONAL_GENDER: string (nullable = true)
 |-- PERSONAL_BIRTHDATE: string (nullable = true)
 |-- PERSONAL_PHOTO: string (nullable = true)
 |-- PERSONAL_PHONE: string (nullable = true)
 |-- PERSONAL_FAX: string (nullable = true)
 |-- PERSONAL_MOBILE: string (nullable = true)
 |-- PERSONAL_PAGER: string (nullable = true)
 |-- PERSONAL_STREET: string (nullable = true)
 |-- PERSONAL_MAILBOX: string (nullable = true)
 |-- PERSONAL_CITY: string (nullable = true)
 |-- PERSONAL_STATE: string (nullable = true)
 |-- PERSONAL_ZIP: string (nullable = true)
 |-- PERSONAL_COUNTRY: string (nullable = true)
 |-- PERSONAL_NOTES: string (nullable = true)
 |-- WORK_COMPANY: string (nullable = true)
 |-- WORK_DEPARTMENT: string (nullable = true)
 |-- WORK_POSITION: string (nullable = true)
 |-- WORK_WWW: string (nullable = true)
 |-- WORK_PHONE: string (nullable = true)
 |-- WORK_FAX: string (nullable = true)
 |-- WORK_PAGER: string (nullable = true)
 |-- WORK_STREET: string (nullable = true)
 |-- WORK_MAILBOX: string (nullable = true)
 |-- WORK_CITY: string (nullable = true)
 |-- WORK_STATE: string (nullable = true)
 |-- WORK_ZIP: string (nullable = true)
 |-- WORK_COUNTRY: string (nullable = true)
 |-- WORK_PROFILE: string (nullable = true)
 |-- WORK_LOGO: string (nullable = true)
 |-- WORK_NOTES: string (nullable = true)
 |-- ADMIN_NOTES: string (nullable = true)
 |-- STORED_HASH: string (nullable = true)
 |-- XML_ID: string (nullable = true)
 |-- PERSONAL_BIRTHDAY: string (nullable = true)
 |-- EXTERNAL_AUTH_ID: string (nullable = true)
 |-- CHECKWORD_TIME: timestamp (nullable = true)
 |-- SECOND_NAME: string (nullable = true)
 |-- CONFIRM_CODE: string (nullable = true)
 |-- LOGIN_ATTEMPTS: string (nullable = true)
 |-- LAST_ACTIVITY_DATE: string (nullable = true)
 |-- AUTO_TIME_ZONE: string (nullable = true)
 |-- TIME_ZONE: string (nullable = true)
 |-- TIME_ZONE_OFFSET: string (nullable = true)
 |-- TITLE: string (nullable = true)
 |-- BX_USER_ID: string (nullable = true)
 |-- LANGUAGE_ID: string (nullable = true)
 |-- BLOCKED: string (nullable = true)
 |-- PASSWORD_EXPIRED: string (nullable = true)

```

### Data sample
```
|   ID | TIMESTAMP_X         | LOGIN               | PASSWORD                                                                                                   | CHECKWORD                                | ACTIVE   | NAME                   | LAST_NAME   | EMAIL                           | LAST_LOGIN          | DATE_REGISTER       | LID   | PERSONAL_PROFESSION   | PERSONAL_WWW   | PERSONAL_ICQ   | PERSONAL_GENDER   | PERSONAL_BIRTHDATE   | PERSONAL_PHOTO   | PERSONAL_PHONE     | PERSONAL_FAX   | PERSONAL_MOBILE   | PERSONAL_PAGER   | PERSONAL_STREET   | PERSONAL_MAILBOX   | PERSONAL_CITY   | PERSONAL_STATE   | PERSONAL_ZIP   | PERSONAL_COUNTRY   | PERSONAL_NOTES   | WORK_COMPANY   | WORK_DEPARTMENT   | WORK_POSITION   | WORK_WWW   | WORK_PHONE   | WORK_FAX   | WORK_PAGER   | WORK_STREET   | WORK_MAILBOX   | WORK_CITY   | WORK_STATE   | WORK_ZIP   | WORK_COUNTRY   | WORK_PROFILE   | WORK_LOGO   | WORK_NOTES   | ADMIN_NOTES   | STORED_HASH   | XML_ID   | PERSONAL_BIRTHDAY   | EXTERNAL_AUTH_ID   | CHECKWORD_TIME      | SECOND_NAME   | CONFIRM_CODE   | LOGIN_ATTEMPTS   | LAST_ACTIVITY_DATE   | AUTO_TIME_ZONE   | TIME_ZONE   | TIME_ZONE_OFFSET   | TITLE   | BX_USER_ID                       | LANGUAGE_ID   | BLOCKED   | PASSWORD_EXPIRED   |
|-----:|:--------------------|:--------------------|:-----------------------------------------------------------------------------------------------------------|:-----------------------------------------|:---------|:-----------------------|:------------|:--------------------------------|:--------------------|:--------------------|:------|:----------------------|:---------------|:---------------|:------------------|:---------------------|:-----------------|:-------------------|:---------------|:------------------|:-----------------|:------------------|:-------------------|:----------------|:-----------------|:---------------|:-------------------|:-----------------|:---------------|:------------------|:----------------|:-----------|:-------------|:-----------|:-------------|:--------------|:---------------|:------------|:-------------|:-----------|:---------------|:---------------|:------------|:-------------|:--------------|:--------------|:---------|:--------------------|:-------------------|:--------------------|:--------------|:---------------|:-----------------|:---------------------|:-----------------|:------------|:-------------------|:--------|:---------------------------------|:--------------|:----------|:-------------------|
|    1 | 2021-04-14 22:30:01 | admin               | p~0J8G>uf5ce1017ae35b4fd79c51e4567a8b53f                                                                   | g1MK3o8n5512b54a4b444ad72d06e38d3e3297ad | Y        |                        |             | tset@test.ru                    | 2023-04-12 09:17:46 | 2016-10-10 14:47:23 | s1    |                       |                |                |                   | NULL                 | NULL             | +7 (234) 235-43-45 |                | 8 495 2312121     |                  |                   |                    |                 |                  |                | 0                  |                  |                |                   |                 |            |              |            |              |               |                |             |              |            | 0              |                | NULL        |              |               | NULL          |          | NULL                | NULL               | 2019-08-26 11:56:29 |               | NULL           | 17398            | NULL                 |                  | NULL        | NULL               |         | 12a0eccac208309161721698ff13fa35 | ru            | N         | N                  |
|    2 | 2021-04-04 06:25:02 | anonymous_n8x7tuczO | Ryg4CKnP740f4ec550cab525aaaad35198fb818e                                                                   | 7Gaqtf1n2be1b97ca36bbbe82125caa5fdf06ee1 | N        | Анонимный пользователь | NULL        | anonymous_n8x7tuczO@example.com | NULL                | 2017-01-31 17:08:11 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7(987)760-76-16   | NULL           | +7(904)981-70-64  | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | saleanonymous      | 2017-01-31 17:08:11 | NULL          | NULL           | NULL             | NULL                 | NULL             | NULL        | NULL               | NULL    | NULL                             | NULL          | N         | N                  |
|    3 | 2017-12-29 01:11:47 | redwhite87          | 9VKRYBox1a4ef382dd12a367c3f7f3f2243645f3                                                                   | G6kWpAvt06c3d242f408201d6aefb545ae21787f | Y        | NULL                   | Вася        | redwhite87@gmail.com            | 2017-03-01 15:31:37 | 2017-03-01 15:31:37 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | 89163665638        | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | d6d8f183a312ac280168dff434634c16 | NULL          | N         | N                  |
|    4 | 2021-04-12 17:40:02 | admin_client        | $6$zNxGz5Ra5YPCTUCJ$.7HaN83bylQ9nNF3YWQk.f57jd4NyoPGryx/ISp4EzcGHaK06K86m7oOCDGRLlIEXRjgfEdLoIHXFNeggzD2/1 | uCxKvlDTf25d2e7e357033275af02097a81e7c95 | Y        |                        |             | redwhite87@gmail.com            | 2024-07-04 14:04:46 | 2017-03-06 13:05:14 | s1    |                       |                |                |                   | NULL                 | NULL             | +7 (111) 111-11-11 |                | 89163665638       |                  |                   |                    | Москва          |                  |                | 0                  |                  |                |                   |                 |            |              |            |              |               |                |             |              |            | 0              |                | NULL        |              |               | NULL          |          | NULL                | NULL               | 2019-07-15 15:55:26 |               | NULL           | 0                | NULL                 |                  | NULL        | NULL               |         | 8f3f169d9e904bf1b71056b47b1deb54 | ru            | N         | N                  |
|    5 | 2017-12-29 01:11:47 | test                | W2AngFFp784050ed5a4469d3c236a9a041850f30                                                                   | ykpwC2sO9689417c404fdc9ff218cba8b8f49874 | Y        | NULL                   | Тест        | test@mail.ru                    | 2017-03-16 17:29:35 | 2017-03-16 17:29:35 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | 81818181           | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 206              | NULL                 | NULL             | NULL        | NULL               | NULL    | f931f234b19a46e648fc05769832f0e2 | NULL          | N         | N                  |
|    6 | 2017-12-29 01:11:47 | iris-flower         | KMoEyTgr199ff992df1d1afd64ae1549965f272d                                                                   | LUl1aFaF9f9c97eeb25641ccb68173b3fd0d044e | Y        | NULL                   | ирина       | iris-flower@list.ru             | 2017-04-07 13:55:51 | 2017-04-07 13:55:51 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (926) 363-65-40 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | d6d8f183a312ac280168dff434634c16 | NULL          | N         | N                  |
|    7 | 2017-12-29 01:11:47 | redwhite871         | HEEL1faW53c6e2c47dc76ef9538bb8ddcb58a7cd                                                                   | w2uDl8pSa90d6c20ce0729c123604003419b4e89 | Y        | NULL                   | Игорь       | redwhite87@gmail.com            | 2017-04-20 19:32:34 | 2017-04-20 19:32:34 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | 89163665638        | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | d6d8f183a312ac280168dff434634c16 | NULL          | N         | N                  |
|    8 | 2017-12-29 01:11:46 | redwhite872         | e64Hs6jA075ddab6a766838f5dcc8e39ef8bd818                                                                   | KD9ppfXqee05118c89e5d7e4f7bf73916919110c | Y        | NULL                   | Игорь       | redwhite87@gmail.com            | 2017-05-05 11:04:11 | 2017-05-05 11:04:11 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (916) 366-56-38 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | d6d8f183a312ac280168dff434634c16 | NULL          | N         | N                  |
|    9 | 2017-12-29 01:11:46 | redwhite873         | UFyvYmola42ae5e974eee713da82cbf2a86e750b                                                                   | SDAoHvrJ967427fe8333ed2e08a150d20818b58c | Y        | NULL                   | Игорь       | redwhite87@gmail.com            | 2017-05-17 15:39:46 | 2017-05-17 15:39:46 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (916) 366-56-38 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | d6d8f183a312ac280168dff434634c16 | NULL          | N         | N                  |
|   10 | 2017-12-29 01:11:46 | azaretskaya78       | xuQ0lXTA284f9c05df758b334a022bafe58d0684                                                                   | BoEizWKI912ad874db014eb37f483a93e48b5776 | Y        | NULL                   | Анна        | azaretskaya78@gmail.com         | 2017-05-17 22:01:51 | 2017-05-17 22:01:51 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (985) 997-86-66 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | 8564ebcf69a298faa8c389e9ebfa00d5 | NULL          | N         | N                  |
|   11 | 2017-12-29 01:11:46 | arbidol88           | VbcUvB7E463eac5fbcee92fc52c21126abd72804                                                                   | QyVskbBT1276ae9ba34beb195847232ff38e968c | Y        | NULL                   | Тест        | arbidol88@gmail.com             | 2017-05-17 23:56:02 | 2017-05-17 23:56:02 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (926) 987-37-37 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | 122aca6c586115f38ebb91d9709dc07c | NULL          | N         | N                  |
|   12 | 2018-10-15 01:31:20 | romanmiami007       | sOrs1ZPH0cbba5526ebd1e6dfd4ff144f7c851f3                                                                   | hNIgc07Pc1fd2b138d1f99ea6a2a2c7bef6d9d02 | Y        | Беленин                | Андрей      | romanmiami007@yahoo.com         | 2017-05-19 06:14:38 | 2017-05-19 06:14:38 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (965) 339-96-53 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | NULL                             | NULL          | N         | N                  |
|   13 | 2017-12-29 01:11:47 | 11111               | FpJ41TVTae7ffd7784cc1351fbe34f5e8c343d6c                                                                   | GnGxOSjvf38357f80684738bfdd97acdc655ff63 | Y        | NULL                   | 1111        | 11111@1111.ru                   | 2017-05-19 17:00:44 | 2017-05-19 17:00:42 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (111) 111-11-11 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | a2f5dc4e9c51f21dde954399f4ad0dde | NULL          | N         | N                  |
|   14 | 2020-11-23 13:56:34 | cmanager            | ezkPL2X606d098955005296dfe4b7c861581999f                                                                   | aXMfvYem611087b505abce383db5b62e5081510c | N        | Алена                  |             | mail@mail.ru                    | 2020-02-18 09:04:25 | 2017-05-21 11:01:37 | s1    |                       |                |                |                   | NULL                 | NULL             |                    |                |                   |                  |                   |                    |                 |                  |                | 0                  |                  |                |                   |                 |            |              |            |              |               |                |             |              |            | 0              |                | NULL        |              |               | NULL          |          | NULL                | NULL               | 2020-11-23 13:56:34 |               | NULL           | 0                | NULL                 |                  | NULL        | NULL               |         | dc187829829569b72a715dcb1d84d09f |               | N         | N                  |
|   18 | 2017-05-22 16:16:16 | only_see_user       | DhAhy0US61e66f4345c28e44e39a3b84c5df511b                                                                   | gufx66Gf8818ab011d4439cc98569519f4c87858 | Y        | ЕВ                     |             | mail10@mail.ru                  | 2019-01-29 10:31:30 | 2017-05-21 11:07:13 | s1    |                       |                |                |                   | NULL                 | NULL             |                    |                |                   |                  |                   |                    |                 |                  |                | 0                  |                  |                |                   |                 |            |              |            |              |               |                |             |              |            | 0              |                | NULL        |              |               | NULL          |          | NULL                | NULL               | 2017-05-22 16:16:16 |               | NULL           | 0                | NULL                 |                  | NULL        | NULL               |         | 76bab0582f21580757bb2c6f5994c8db |               | N         | N                  |
|   19 | 2017-05-23 11:56:22 | only_see_user1      | Cq6APusm57d144530f0d04b70e16c222459fd8a9                                                                   | E3CCvBnzb2dba54e78b8dc3928442cdce25c53ee | Y        | ЛИ                     |             | mail11@mail.ru                  | 2018-01-15 17:56:04 | 2017-05-21 11:08:30 | s1    |                       |                |                |                   | NULL                 | NULL             |                    |                |                   |                  |                   |                    |                 |                  |                | 0                  |                  |                |                   |                 |            |              |            |              |               |                |             |              |            | 0              |                | NULL        |              |               | NULL          |          | NULL                | NULL               | 2017-05-23 11:56:22 |               | NULL           | 0                | NULL                 |                  | NULL        | NULL               |         | 623cd4693702f5d0de5f1772a3dadc40 |               | N         | N                  |
|   20 | 2017-12-29 01:11:47 | s__                 | bjGRat7r1e1f472340854bacc46783fea0be337c                                                                   | QmjdBqOue3141fffd2bb0e3984e1f7a5be9fcdf1 | Y        | NULL                   | Сергей      | s@mail.ru                       | 2017-05-22 11:16:15 | 2017-05-22 11:16:12 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (811) 988-18-52 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | 0d71f0c710b45a399e32e4ae71d1cb93 | NULL          | N         | N                  |
|   21 | 2017-12-29 01:11:47 | fgdfgf              | qxuJYXuvcabe518627197aa3014789d9c86cc676                                                                   | Z2EvEuUZ10700941e8b5b3ab2b015814b2d59c00 | Y        | NULL                   | dfgdfgg     | fgdfgf@dff.ru                   | 2017-05-22 11:48:02 | 2017-05-22 11:48:02 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (234) 554-35-34 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | 91221f46e8fbdbc7b1fbeb82f0da118e | NULL          | N         | N                  |
|   22 | 2017-12-29 01:11:47 | s__1                | 8lvlFvLl364c698fe75a98b131af97278c8ee5de                                                                   | S6qWWYtb3a35dffd495670817c387adf9d99cb7b | Y        | NULL                   | Ник         | s@mail.ru                       | 2017-05-23 11:10:53 | 2017-05-23 11:10:51 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (818) 900-35-65 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | 0d71f0c710b45a399e32e4ae71d1cb93 | NULL          | N         | N                  |
|   23 | 2017-12-29 01:11:46 | nyakhontoff         | vHxd1mZ75676c8bd5d50b3f1494efe5e065593cf                                                                   | Fk1QUno5083e6c3f0844f4a6fdf234f86d4cf881 | Y        | NULL                   | Николай     | nyakhontoff@gmail.com           | 2017-05-23 14:13:22 | 2017-05-23 14:13:22 | s1    | NULL                  | NULL           | NULL           |                   | NULL                 | NULL             | +7 (985) 229-89-99 | NULL           | NULL              | NULL             | NULL              | NULL               | NULL            | NULL             | NULL           | NULL               | NULL             | NULL           | NULL              | NULL            | NULL       | NULL         | NULL       | NULL         | NULL          | NULL           | NULL        | NULL         | NULL       | NULL           | NULL           | NULL        | NULL         | NULL          | NULL          | NULL     | NULL                | NULL               | 2017-12-28 21:57:11 | NULL          | NULL           | 0                | NULL                 | NULL             | NULL        | NULL               | NULL    | 68e8090e5a30ba4109443d93a523218f | NULL          | N         | N                  |
```

> - File path: b_sale_user_props.csv
> - Total rows: 5210

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- NAME: string (nullable = true)
 |-- USER_ID: integer (nullable = true)
 |-- PERSON_TYPE_ID: integer (nullable = true)
 |-- DATE_UPDATE: string (nullable = true)
 |-- XML_ID: string (nullable = true)
 |-- VERSION_1C: string (nullable = true)

```

### Data sample
```
|   ID | NAME   |   USER_ID |   PERSON_TYPE_ID | DATE_UPDATE         | XML_ID   | VERSION_1C   |
|-----:|:-------|----------:|-----------------:|:--------------------|:---------|:-------------|
|    1 | test   |         1 |                1 | 2017-02-13 09:21:32 | NULL     | NULL         |
|    2 | test   |         1 |                1 | 2017-02-17 16:00:33 | NULL     | NULL         |
|    3 | test   |         1 |                1 | 2017-02-17 16:27:07 | NULL     | NULL         |
|    4 | test   |         1 |                1 | 2017-02-17 17:21:41 | NULL     | NULL         |
|    5 | test   |         1 |                1 | 2017-02-17 17:25:46 | NULL     | NULL         |
|    6 | test   |         1 |                1 | 2017-02-17 17:34:47 | NULL     | NULL         |
|    7 | test   |         1 |                1 | 2017-02-17 21:40:31 | NULL     | NULL         |
|    8 | test   |         1 |                1 | 2017-02-17 21:45:27 | NULL     | NULL         |
|    9 | test   |         1 |                1 | 2017-02-17 21:48:31 | NULL     | NULL         |
|   10 | test   |         1 |                1 | 2017-02-17 21:49:32 | NULL     | NULL         |
|   11 | test   |         1 |                1 | 2017-02-21 10:07:45 | NULL     | NULL         |
|   12 | Вася   |         3 |                1 | 2017-03-01 15:31:37 | NULL     | NULL         |
|   13 | test   |         1 |                1 | 2017-03-14 09:25:11 | NULL     | NULL         |
|   14 | Тест   |         5 |                1 | 2017-03-16 17:29:36 | NULL     | NULL         |
|   15 | ирина  |         6 |                1 | 2017-04-07 13:55:52 | NULL     | NULL         |
|   16 | Игорь  |         4 |                1 | 2017-04-07 14:53:57 | NULL     | NULL         |
|   17 | Игорь  |         7 |                1 | 2017-04-20 19:32:35 | NULL     | NULL         |
|   18 | Игорь  |         8 |                1 | 2017-05-05 11:04:11 | NULL     | NULL         |
|   19 | Игорь  |         9 |                1 | 2017-05-17 15:39:47 | NULL     | NULL         |
|   20 | Анна   |        10 |                1 | 2017-05-17 22:01:51 | NULL     | NULL         |
```

> - File path: b_sale_user_props_value.csv
> - Total rows: 15630

### Schema
```
root
 |-- ID: integer (nullable = true)
 |-- USER_PROPS_ID: integer (nullable = true)
 |-- ORDER_PROPS_ID: integer (nullable = true)
 |-- NAME: string (nullable = true)
 |-- VALUE: string (nullable = true)

```

### Data sample
```
|   ID |   USER_PROPS_ID |   ORDER_PROPS_ID | NAME     | VALUE               |
|-----:|----------------:|-----------------:|:---------|:--------------------|
|    1 |               1 |                1 | Ваше имя | test                |
|    2 |               1 |                2 | e-mai    | suppor@avkey-web.ru |
|    3 |               1 |                3 | Телефон  | 2342354345          |
|    4 |               2 |                1 | Ваше имя | test                |
|    5 |               2 |                2 | e-mai    | suppor@avkey-web.ru |
|    6 |               2 |                3 | Телефон  | 2342354345          |
|    7 |               3 |                1 | Ваше имя | test                |
|    8 |               3 |                2 | e-mai    | suppor@avkey-web.ru |
|    9 |               3 |                3 | Телефон  | 2342354345          |
|   10 |               4 |                1 | Ваше имя | test                |
|   11 |               4 |                2 | e-mai    | suppor@avkey-web.ru |
|   12 |               4 |                3 | Телефон  | 2342354345          |
|   13 |               5 |                1 | Ваше имя | test                |
|   14 |               5 |                2 | e-mai    | suppor@avkey-web.ru |
|   15 |               5 |                3 | Телефон  | 2342354345          |
|   16 |               6 |                1 | Ваше имя | test                |
|   17 |               6 |                2 | e-mai    | suppor@avkey-web.ru |
|   18 |               6 |                3 | Телефон  | 2342354345          |
|   19 |               7 |                1 | Ваше имя | test                |
|   20 |               7 |                2 | e-mai    | suppor@avkey-web.ru |
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
 |-- address: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- sex: integer (nullable = true)
 |-- birth_date: string (nullable = true)
 |-- accounts: array (nullable = true)
 |    |-- element: struct (containsNull = false)
 |    |    |-- title: string (nullable = false)
 |    |    |-- link: string (nullable = false)
 |    |    |-- login: string (nullable = true)
 |    |    |-- password_hash: string (nullable = true)
 |    |    |-- id: string (nullable = true)
 |-- works: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- post: string (nullable = true)
 |    |    |-- date_start: string (nullable = true)
 |    |    |-- date_end: string (nullable = true)
 |    |    |-- company: string (nullable = true)
 |    |    |-- address: string (nullable = true)
 |    |    |-- comment: string (nullable = true)
 |-- documents: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- type: integer (nullable = true)
 |    |    |-- serial: string (nullable = false)
 |    |    |-- country: string (nullable = true)
 |    |    |-- date_issue: string (nullable = true)
 |    |    |-- date_expire: string (nullable = true)
 |    |    |-- authority: string (nullable = true)
 |    |    |-- authority_code: string (nullable = true)
 |-- actuality: string (nullable = true)

```


### Columns completeness

| Column   | Completeness |
|----------|--------------|
| Names | 100.00% |
| Emails | 99.74% |
| Phones | 94.09% |
| Address | 44.00% |
| Sex | 0.05% |
| Birth_date | 0.00% |
| Accounts | 100.00% |
| Works | 99.86% |
| Documents | 9.01% |
| Actuality | 0.00% |



### Data sample
```
| names                                | emails                      | phones          | address                                               |   sex | birth_date   | accounts                                                                                                                                                        | works   | documents                                                                                                                 | actuality   |
|:-------------------------------------|:----------------------------|:----------------|:------------------------------------------------------|------:|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------|:--------------------------------------------------------------------------------------------------------------------------|:------------|
| ['Наталья']                          | ['undeadnike@yandex.ru']    | ['79265017108'] |                                                       |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='UndeadNike', password_hash='X3arWZ0Uc77f6f76db0b34ef42790997c0ef6e7d', id='296')]                     | [None]  |                                                                                                                           |             |
| ['Кристина']                         | ['toxic_11@mail.ru']        | ['79161093690'] |                                                       |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='toxic_11', password_hash='rphxq1HM63851b8cee6726af74d5f0cfb13cca9d', id='125')]                       | [None]  |                                                                                                                           |             |
| ['Игорь']                            | ['redwhite87@gmail.com']    | ['79163665638'] | ['Арбат']                                             |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='redwhite871', password_hash='HEEL1faW53c6e2c47dc76ef9538bb8ddcb58a7cd', id='7')]                      | [None]  |                                                                                                                           |             |
| ['Ирина']                            | ['kmara63@gmail.com']       | ['79653447972'] | ['ул.Центральная д.4 кв.35']                          |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='kmara63', password_hash='mGvePg2C59cd0a9210215699ce42850a9bb92e35', id='51')]                         | [None]  |                                                                                                                           |             |
| ['Екатерина']                        | ['kruk1986@mail.ru']        | ['79153684206'] | ['Бондарева 5']                                       |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='kruk1986', password_hash='zHeTpIVs0871a2370594dfafd56fb8c13e2a245f', id='124')]                       | [None]  |                                                                                                                           |             |
| ['Светлана']                         | ['fox.budusov@yandex.ru']   | ['79082717596'] | ['Пономарева 12-24']                                  |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='fox.budusov', password_hash='1dkiFsDc90472ef8caf6d71f0db09b5d8cc3c827', id='307')]                    | [None]  | [Row(type=0, serial='5708268969', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Юрий']                             | ['9252232278@mail.ru']      | ['79268734832'] | ['Зеленый проспект 682 кв 80']                        |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='9252232278', password_hash='JI13Tofx22eefdf743162df96aa28788be929a22', id='169')]                     | [None]  |                                                                                                                           |             |
| ['Марина']                           | ['podokonnik@mail.ru']      |                 |                                                       |     0 |              | [Row(title='FineWall', link='https://finewall.ru', login='openid.mail.ru/mail/podokonnik', password_hash='O5Bkxa8tb52da8c476c9d10e7d9ed74fab0b5a63', id='334')] | [None]  |                                                                                                                           |             |
| ['Юрий', 'Балагуров Юрий']           | ['yurgend85@yandex.ru']     | ['79622114975'] | ['Овинная 30']                                        |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='yurgend85', password_hash='jXV7HqW3b659700027bdcaf48098f3520a7e8b34', id='272')]                      | [None]  | [Row(type=0, serial='7804440728', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Дарья', 'Феногенова Дарья']        | ['orlana@inbox.ru']         | ['79165052413'] | ['ул. Мытная д. 23 корп. 1 кв. 75А 2 подъезд 5 этаж'] |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='orlana', password_hash='2c5jTwMm31489447dc2ca53317a88a3abcacdfbd', id='282')]                         | [None]  |                                                                                                                           |             |
| ['Юлия', 'Голубева Юлия Борисовна']  | ['golubeva6672@rambler.ru'] | ['79106659401'] | ['Тутаевское Шоссе Д.66 Корп. 2 Кв. 72']              |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='golubeva6672', password_hash='VUif1Moj23c3311066aebdf5d75c2ff13cf55e78', id='383')]                   | [None]  | [Row(type=0, serial='7805453287', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Антон', 'Ардашев Антон']           | ['nurosapon@gmail.com']     | ['79124540419'] | ['Пушкинская 224 - 45']                               |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='nurosapon', password_hash='SB5XPuYI856118a5021b150c70c89714cd7d3917', id='155')]                      | [None]  | [Row(type=0, serial='9405647623', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Оксана']                           | ['sharikovahome@yandex.ru'] | ['79611499061'] | ['Ул. Макаренко 18']                                  |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='sharikovahome', password_hash='bLhEf9Owfbc425bdd1a00515326315f1ec293064', id='154')]                  | [None]  | [Row(type=0, serial='7015641046', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Юлия']                             | ['sizova@uhsep.com']        | ['79269190329'] |                                                       |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='sizova', password_hash='SnFrlUVwa21bb8c5374b5e53ebf4533cb46eaae7', id='317')]                         | [None]  |                                                                                                                           |             |
| ['Евгений']                          |                             | ['79200000000'] |                                                       |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='test5', password_hash='itwT9QUk5d2ac50ff8fef828e58bdb6704e451f7', id='388')]                          | [None]  |                                                                                                                           |             |
| ['Елена', 'Логинова Елена Петровна'] | ['arhrobinson@gmail.com']   | ['79212432303'] | ['наб.Северной Двины 71 корп.1 оф.609']               |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='arhrobinson', password_hash='Jpc2ghXK289887023030e216c3505e3ea485f649', id='428')]                    | [None]  | [Row(type=0, serial='1103863376', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Алексей']                          | ['ransalex@gmail.com']      | ['79178595669'] | ['Казань']                                            |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='ransalex', password_hash='6iW0XJ9Y541689ae34cb1e08b3a1a2cd508defbe', id='101')]                       | [None]  | [Row(type=0, serial='9207062792', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Павел']                            | ['mazepa@lgk.su']           | ['79035762251'] | ['Москва ул.Липецкая д. 40 подъезд 4 кв. 221']        |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='Mazepa', password_hash='eyHZWt432cd10b4f47527f4b3b7ef5953da3f1b5', id='415')]                         | [None]  |                                                                                                                           |             |
| ['Сергей']                           | ['xak-s1@mail.ru']          | ['79376461149'] | ['443086 г. Самара ул. Лукачева 4 кв.108']            |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='xak-s1', password_hash='gG7urHoVe348c8c089b26460209dbcb25e7ab8c0', id='422')]                         | [None]  | [Row(type=0, serial='0311935523', country='RUS', date_issue=None, date_expire=None, authority=None, authority_code=None)] |             |
| ['Ярослав']                          | ['dolgalev87@yandex.ru']    | ['79621719666'] |                                                       |   nan |              | [Row(title='FineWall', link='https://finewall.ru', login='Dolgalev87', password_hash='J6Zm7ymL0459942e0927c806f1e776deb54ba828', id='433')]                     | [None]  |                                                                                                                           |             |
```