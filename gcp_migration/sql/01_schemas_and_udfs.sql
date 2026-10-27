-- =============================================================================
-- 01_schemas_and_udfs.sql
-- GCP Medallion Architecture: Datasets, Descriptions, and Persistent UDFs
-- Project: medallion-project-512608 | Location: europe-west1
-- =============================================================================

-- 1. Persistent UDF: Clean & Normalize Full Name (Cyrillic Title Case)
CREATE OR REPLACE FUNCTION `silver.clean_name`(raw_name STRING)
RETURNS STRING
AS (
  CASE
    WHEN raw_name IS NULL OR TRIM(raw_name) = '' THEN NULL
    -- Filter out strings with numbers or excessive special characters
    WHEN REGEXP_CONTAINS(raw_name, r'[0-9<>{}\[\]\(\)\\/\$%\^]') THEN NULL
    -- Require minimum length and non-trivial character diversity
    WHEN LENGTH(TRIM(REGEXP_REPLACE(raw_name, r'[\s\.\-]+', ''))) < 3 THEN NULL
    -- Rejects placeholder test strings
    WHEN LOWER(TRIM(raw_name)) IN ('test', 'тест', 'нет', 'не определен', 'клиент', 'покупатель', 'покупатель пз юл') THEN NULL
    ELSE
      -- Collapse multi-spaces and apply Title Case
      INITCAP(TRIM(REGEXP_REPLACE(raw_name, r'\s+', ' ')))
  END
);

-- 2. Persistent UDF: Clean & Standardize Phone to E.164 (without leading '+')
CREATE OR REPLACE FUNCTION `silver.clean_phone_e164`(raw_phone STRING)
RETURNS STRING
AS (
  (
    WITH cleaned AS (
      SELECT REGEXP_REPLACE(raw_phone, r'[^0-9]', '') AS digits
    ),
    standardized AS (
      SELECT
        CASE
          -- 11 digits starting with 8 (common RU national prefix) -> replace with 7
          WHEN LENGTH(digits) = 11 AND STARTS_WITH(digits, '8') THEN CONCAT('7', SUBSTR(digits, 2))
          -- 10 digits starting with 9 -> prepend 7
          WHEN LENGTH(digits) = 10 AND STARTS_WITH(digits, '9') THEN CONCAT('7', digits)
          -- Valid E.164 11-15 digit string
          WHEN LENGTH(digits) BETWEEN 11 AND 15 THEN digits
          ELSE NULL
        END AS p
      FROM cleaned
    )
    SELECT
      CASE
        WHEN p IS NULL THEN NULL
        -- Require at least 4 distinct digits (filters identical digits like 77777777777 and repetitive dummies)
        WHEN (SELECT COUNT(DISTINCT ch) FROM UNNEST(SPLIT(p, '')) AS ch) < 4 THEN NULL
        -- Reject dummy sequential test patterns
        WHEN p IN ('71234567890', '79876543210', '70123456789') THEN NULL
        -- Reject all identical trailing digits (e.g. 70000000000, 79999999999)
        WHEN REGEXP_CONTAINS(p, r'^7(0{10}|1{10}|2{10}|3{10}|4{10}|5{10}|6{10}|7{10}|8{10}|9{10})$') THEN NULL
        ELSE p
      END
    FROM standardized
  )
);

-- 3. Persistent UDF: Clean & Validate Email Address
CREATE OR REPLACE FUNCTION `silver.clean_email`(raw_email STRING)
RETURNS STRING
AS (
  (
    WITH lower_em AS (
      SELECT LOWER(TRIM(raw_email)) AS em
    )
    SELECT
      CASE
        WHEN em IS NULL OR em = '' THEN NULL
        -- Verify standard email regex RFC-compliant format
        WHEN NOT REGEXP_CONTAINS(em, r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$') THEN NULL
        -- Filter out common placeholder & stop-list emails
        WHEN REGEXP_CONTAINS(em, r'^(none|null|test|admin|info|no|user|na|dummy)@') THEN NULL
        WHEN REGEXP_CONTAINS(em, r'@(?i)(no\.ru|test\.ru|example\.com|test\.com|placeholder\.org|mail\.invalid|localhost)$') THEN NULL
        ELSE em
      END
    FROM lower_em
  )
);

-- 4. Persistent UDF: Robust Multi-Format Date Parser with Sanity Bounds
CREATE OR REPLACE FUNCTION `silver.parse_date_safe`(raw_date STRING)
RETURNS DATE
AS (
  (
    WITH parsed AS (
      SELECT COALESCE(
        -- Try YYYY-MM-DD (standard ISO)
        SAFE.PARSE_DATE('%Y-%m-%d', SUBSTR(TRIM(raw_date), 1, 10)),
        -- Try DD.MM.YYYY (Russian standard)
        SAFE.PARSE_DATE('%d.%m.%Y', SUBSTR(TRIM(raw_date), 1, 10)),
        -- Try MM/DD/YYYY (US format / Excel exports)
        SAFE.PARSE_DATE('%m/%d/%Y', SUBSTR(TRIM(raw_date), 1, 10)),
        -- Try YYYY/MM/DD
        SAFE.PARSE_DATE('%Y/%m/%d', SUBSTR(TRIM(raw_date), 1, 10)),
        -- Try timestamp ISO substring
        SAFE.PARSE_DATE('%Y-%m-%d', SAFE_CAST(SAFE.PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%S', TRIM(raw_date)) AS STRING))
      ) AS d
    )
    SELECT
      CASE
        WHEN d IS NULL THEN NULL
        -- Filter placeholder dummy dates common in Russian registries/CRMs
        WHEN d = DATE '1900-01-01' OR d = DATE '0001-01-01' OR d = DATE '9999-12-31' THEN NULL
        -- Age check: reject dates older than 115 years or future dates > 1 year
        WHEN d < DATE_SUB(CURRENT_DATE(), INTERVAL 115 YEAR) THEN NULL
        WHEN d > DATE_ADD(CURRENT_DATE(), INTERVAL 365 DAY) THEN NULL
        ELSE d
      END
    FROM parsed
  )
);

-- 5. Persistent UDF: Standardize Biological Sex
CREATE OR REPLACE FUNCTION `silver.normalize_sex`(raw_sex STRING)
RETURNS STRUCT<code INT64, label STRING>
AS (
  CASE
    WHEN raw_sex IS NULL THEN STRUCT(CAST(NULL AS INT64), 'UNKNOWN')
    WHEN UPPER(TRIM(raw_sex)) IN ('M', '1', 'МУЖ', 'МУЖСКОЙ', 'MALE') THEN STRUCT(1, 'MALE')
    WHEN UPPER(TRIM(raw_sex)) IN ('F', '0', '2', 'Ж', 'ЖЕН', 'ЖЕНСКИЙ', 'FEMALE') THEN STRUCT(0, 'FEMALE')
    ELSE STRUCT(CAST(NULL AS INT64), 'UNKNOWN')
  END
);

-- 6. Persistent UDF: Clean & Validate Document (Passport, INN, SNILS)
CREATE OR REPLACE FUNCTION `silver.build_document_struct`(
  doc_type_raw STRING,
  doc_serial_raw STRING,
  doc_date_raw STRING,
  doc_authority_raw STRING
)
RETURNS STRUCT<
  type INT64,
  type_name STRING,
  serial STRING,
  date_issue DATE,
  authority STRING,
  authority_code STRING
>
AS (
  (
    WITH cleaned_serial AS (
      SELECT
        -- Strip whitespace and common punctuation from document serial
        REGEXP_REPLACE(TRIM(doc_serial_raw), r'[\s\-_]+', '') AS s,
        silver.parse_date_safe(doc_date_raw) AS d,
        TRIM(doc_authority_raw) AS auth
    ),
    classified AS (
      SELECT
        s,
        d,
        auth,
        CASE
          -- INN Person: 12 digits
          WHEN LENGTH(s) = 12 AND REGEXP_CONTAINS(s, r'^[0-9]{12}$') THEN 1
          -- SNILS: 11 digits
          WHEN LENGTH(s) = 11 AND REGEXP_CONTAINS(s, r'^[0-9]{11}$') THEN 2
          -- Russian Passport: 10 digits
          WHEN LENGTH(s) = 10 AND REGEXP_CONTAINS(s, r'^[0-9]{10}$') THEN 0
          -- INN Legal entity: 10 digits with INN hint in type
          WHEN LENGTH(s) = 10 AND LOWER(COALESCE(doc_type_raw, '')) LIKE '%инн%' THEN 1
          -- Birth Certificate or Foreign Passport
          WHEN REGEXP_CONTAINS(s, r'^[IVXLCDMivxlcdm]+-[А-Яа-яA-Za-z]+') THEN 5
          ELSE 4 -- Other / Foreign
        END AS t
      FROM cleaned_serial
    )
    SELECT
      CASE
        WHEN s IS NULL OR s = '' OR LENGTH(s) < 5 THEN NULL
        -- Reject if all identical characters (e.g. 0000000000)
        WHEN (SELECT COUNT(DISTINCT ch) FROM UNNEST(SPLIT(s, '')) AS ch) < 2 THEN NULL
        ELSE
          STRUCT(
            t AS type,
            CASE t
              WHEN 0 THEN 'RU_PASSPORT'
              WHEN 1 THEN 'INN'
              WHEN 2 THEN 'SNILS'
              WHEN 5 THEN 'BIRTH_CERTIFICATE'
              ELSE 'OTHER'
            END AS type_name,
            s AS serial,
            d AS date_issue,
            auth AS authority,
            REGEXP_EXTRACT(auth, r'([0-9]{3}-[0-9]{3})') AS authority_code
          )
      END
    FROM classified
  )
);

-- 7. Persistent UDF: Standardize & Validate Vehicle Attributes
CREATE OR REPLACE FUNCTION `silver.build_vehicle_struct`(
  model_raw STRING,
  year_raw INT64,
  color_raw STRING,
  plate_raw STRING,
  vin_raw STRING
)
RETURNS STRUCT<
  model STRING,
  manufacture_year INT64,
  color STRING,
  license_plate STRING,
  vin STRING
>
AS (
  (
    WITH cleaned AS (
      SELECT
        INITCAP(TRIM(model_raw)) AS m,
        CASE
          WHEN year_raw BETWEEN 1950 AND EXTRACT(YEAR FROM CURRENT_DATE()) + 1 THEN year_raw
          ELSE NULL
        END AS yr,
        INITCAP(TRIM(color_raw)) AS clr,
        -- Standardize plate: uppercase, remove spaces/dashes
        UPPER(REGEXP_REPLACE(TRIM(plate_raw), r'[\s\-_]+', '')) AS plt,
        -- VIN: uppercase, remove spaces, exactly 17 alphanumeric
        UPPER(REGEXP_REPLACE(TRIM(vin_raw), r'[^A-HJ-NPR-Z0-9a-hj-npr-z]', '')) AS v
    )
    SELECT
      CASE
        WHEN (plt IS NULL OR plt = '') AND (v IS NULL OR v = '') THEN NULL
        ELSE
          STRUCT(
            m AS model,
            yr AS manufacture_year,
            clr AS color,
            plt AS license_plate,
            CASE WHEN LENGTH(v) = 17 THEN v ELSE NULL END AS vin
          )
      END
    FROM cleaned
  )
);

-- 8. Persistent UDF: Clean & Validate IPv4 Address
CREATE OR REPLACE FUNCTION `silver.clean_ip_v4`(raw_ip STRING)
RETURNS STRING
AS (
  (
    WITH ip_trimmed AS (
      SELECT TRIM(raw_ip) AS ip
    )
    SELECT
      CASE
        WHEN ip IS NULL OR ip = '' THEN NULL
        -- Valid IPv4 syntax
        WHEN NOT REGEXP_CONTAINS(ip, r'^([0-9]{1,3}\.){3}[0-9]{1,3}$') THEN NULL
        -- Octet validity (<= 255)
        WHEN EXISTS(
          SELECT 1 FROM UNNEST(SPLIT(ip, '.')) AS octet
          WHERE CAST(octet AS INT64) > 255
        ) THEN NULL
        -- Filter private/loopback/dummy IPs if desired or keep valid external IPs
        WHEN ip IN ('0.0.0.0', '255.255.255.255', '127.0.0.1') THEN NULL
        ELSE ip
      END
    FROM ip_trimmed
  )
);

-- 9. Persistent UDF: Deterministic SHA-256 Hash ID
CREATE OR REPLACE FUNCTION `silver.hash_entity_id`(val STRING)
RETURNS STRING
AS (
  CASE
    WHEN val IS NULL OR TRIM(val) = '' THEN NULL
    ELSE TO_HEX(SHA256(TRIM(val)))
  END
);
