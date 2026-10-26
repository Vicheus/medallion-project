-- =============================================================================
-- 04_gold_tables_and_sp.sql
-- GCP Medallion Architecture: Gold Semantic Layer & Identity Resolution Routine
-- Project: medallion-project-512608 | Location: europe-west1
-- =============================================================================

-- 1. Gold Master Table: Unified 360-Degree Person Profiles
CREATE TABLE IF NOT EXISTS `gold.person_profiles_master` (
  person_id STRING NOT NULL OPTIONS(description="Deterministic master identity hash (SHA-256 of canonical name + birth_date or primary phone)"),
  primary_full_name STRING NOT NULL OPTIONS(description="Canonical Cyrillic full name in Title Case ('LastName FirstName MiddleName')"),
  sex_code INT64 OPTIONS(description="Biological sex: 1=Male, 0=Female, NULL=Unknown"),
  sex_label STRING OPTIONS(description="'MALE', 'FEMALE', or 'UNKNOWN'"),
  birth_date DATE OPTIONS(description="Validated date of birth (YYYY-MM-DD)"),
  birth_place STRING OPTIONS(description="Place of birth as stated in official records"),
  primary_phone STRING OPTIONS(description="Primary contact phone in E.164 digits-only format without leading '+'"),
  primary_email STRING OPTIONS(description="Primary validated contact email address"),
  primary_address STRING OPTIONS(description="Primary or latest known physical/registration address"),
  latest_actuality_date DATE OPTIONS(description="Latest timestamp or operation date associated with this individual"),
  -- Full History Arrays for Deep Investigation
  all_names ARRAY<STRING> OPTIONS(description="All distinct full name variations observed across sources"),
  phones ARRAY<STRING> OPTIONS(description="All distinct verified E.164 phone numbers"),
  emails ARRAY<STRING> OPTIONS(description="All distinct verified email addresses"),
  addresses ARRAY<STRING> OPTIONS(description="All distinct physical and registration addresses"),
  documents ARRAY<STRUCT<
    type INT64,
    type_name STRING,
    serial STRING,
    date_issue DATE,
    authority STRING,
    authority_code STRING
  >> OPTIONS(description="All verified identity documents (Passports, INNs, SNILS)"),
  works ARRAY<STRUCT<
    organization_name STRING,
    job_title STRING,
    company_inn STRING,
    company_ogrn STRING,
    salary NUMERIC,
    actuality_date DATE
  >> OPTIONS(description="Employment history and corporate relationships"),
  vehicles ARRAY<STRUCT<
    license_plate STRING,
    vin STRING,
    model STRING,
    manufacture_year INT64,
    color STRING
  >> OPTIONS(description="Registered vehicle ownerships"),
  digital_footprints ARRAY<STRUCT<
    channel_type STRING,
    channel_value STRING,
    ip_country STRING,
    registration_time TIMESTAMP
  >> OPTIONS(description="Digital activity, IP addresses, and social identifiers"),
  source_ids ARRAY<STRING> OPTIONS(description="List of all source indexes containing records for this identity"),
  source_entity_ids ARRAY<STRING> OPTIONS(description="List of all Bronze/Silver source_entity_id keys resolved into this identity"),
  ingest_date DATE NOT NULL OPTIONS(description="Pipeline run partition date"),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY primary_full_name, birth_date, primary_phone
OPTIONS(
  description="[PURPOSE]: Master 360-degree identity profile table resolving individuals across all 7 sources.\n[GRAIN]: One row per resolved unique person.\n[USE WHEN]: Looking up person contact info, demographics, document history, or cross-source profile.\n[DO NOT USE WHEN]: Querying transit ticket itineraries (use gold.person_movements_fact instead)."
);

-- 2. Gold Fact Table: Transportation and Passenger Movements
CREATE TABLE IF NOT EXISTS `gold.person_movements_fact` (
  movement_id STRING NOT NULL OPTIONS(description="Deterministic movement fact key (SHA-256 of ticket + departure)"),
  person_id STRING OPTIONS(description="Foreign key to gold.person_profiles_master (if resolved)"),
  passenger_full_name STRING NOT NULL OPTIONS(description="Passenger full name on ticket"),
  birth_date DATE OPTIONS(description="Passenger date of birth"),
  passenger_phone STRING OPTIONS(description="Contact phone associated with travel ticket"),
  passenger_document_serial STRING OPTIONS(description="Identity document presented during ticket purchase"),
  ticket_number STRING NOT NULL OPTIONS(description="Official travel ticket number"),
  transport_type STRING NOT NULL OPTIONS(description="'RAIL', 'FLIGHT', etc."),
  departure_date DATE NOT NULL OPTIONS(description="Scheduled departure date (partition key)"),
  port_from STRING NOT NULL OPTIONS(description="Origin station / port code or name"),
  port_to STRING NOT NULL OPTIONS(description="Destination station / port code or name"),
  train_number STRING OPTIONS(description="Train, flight, or vehicle transit number"),
  seat_class STRING OPTIONS(description="Coach class (e.g., '1', '2', 'COUPE', 'PLATZKART')"),
  seat STRING OPTIONS(description="Assigned seat or berth number"),
  source_id STRING NOT NULL OPTIONS(description="Origin source index (e.g. index_0020_movements)"),
  ingest_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY departure_date
CLUSTER BY port_from, port_to, passenger_full_name
OPTIONS(
  description="[PURPOSE]: Denormalized movement fact table linking passenger identities directly with transit tickets.\n[GRAIN]: One row per travel/ticket movement event.\n[USE WHEN]: User asks about travel routes, stations, train journeys, passenger itineraries, or co-travelers."
);

-- 3. Gold Fact Table: Employment & Corporate Affiliations
CREATE TABLE IF NOT EXISTS `gold.person_employment_fact` (
  employment_id STRING NOT NULL,
  person_id STRING OPTIONS(description="Foreign key to gold.person_profiles_master"),
  person_full_name STRING NOT NULL,
  birth_date DATE,
  person_phone STRING,
  company_name STRING NOT NULL,
  job_title STRING,
  company_inn STRING,
  company_ogrn STRING,
  salary NUMERIC,
  application_status STRING,
  source_id STRING NOT NULL,
  actuality_date DATE,
  ingest_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY company_name, company_inn, person_full_name
OPTIONS(
  description="[PURPOSE]: Denormalized employment and corporate directory.\n[GRAIN]: One row per person-company employment record.\n[USE WHEN]: User asks about who works at a specific company, employer INN lookups, or job titles."
);

-- 4. Gold Fact Table: Vehicle Ownership
CREATE TABLE IF NOT EXISTS `gold.person_vehicles_fact` (
  vehicle_fact_id STRING NOT NULL,
  person_id STRING OPTIONS(description="Foreign key to gold.person_profiles_master"),
  owner_full_name STRING NOT NULL,
  birth_date DATE,
  owner_phone STRING,
  license_plate STRING NOT NULL,
  vin STRING,
  model STRING,
  manufacture_year INT64,
  color STRING,
  source_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY license_plate, vin, owner_full_name
OPTIONS(
  description="[PURPOSE]: Denormalized vehicle ownership table.\n[GRAIN]: One row per registered vehicle ownership.\n[USE WHEN]: User asks about who owns a specific car, license plate lookups, or VIN searches."
);

-- 5. Gold Fact Table: Digital Footprints (IPs & Telegram)
CREATE TABLE IF NOT EXISTS `gold.person_digital_footprint_fact` (
  footprint_id STRING NOT NULL,
  person_id STRING OPTIONS(description="Foreign key to gold.person_profiles_master"),
  user_full_name STRING,
  contact_phone STRING,
  contact_email STRING,
  channel_type STRING NOT NULL OPTIONS(description="'IP' or 'TELEGRAM'"),
  channel_value STRING NOT NULL OPTIONS(description="IP address string or Telegram ID/handle"),
  ip_country STRING,
  registration_time TIMESTAMP,
  source_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY channel_type, channel_value, user_full_name
OPTIONS(
  description="[PURPOSE]: Denormalized digital footprint fact table linking online sessions, IPs, and Telegram handles.\n[GRAIN]: One row per digital identifier session.\n[USE WHEN]: User asks about online accounts, registration IPs, Telegram handles, or geolocated activity."
);

-- 6. Gold View: Flattened Document Search Lookup
CREATE OR REPLACE VIEW `gold.person_documents_lookup`
OPTIONS(
  description="[PURPOSE]: Flattened search view over all identity documents linked to master person profiles.\n[GRAIN]: One row per identity document.\n[USE WHEN]: Searching for individuals by passport serial, INN, or SNILS without requiring UNNEST()."
) AS
SELECT
  p.person_id,
  p.primary_full_name,
  p.birth_date,
  p.primary_phone,
  p.primary_email,
  d.type AS document_type_code,
  d.type_name AS document_type_name,
  d.serial AS document_serial,
  d.date_issue AS document_issue_date,
  d.authority AS issuing_authority,
  d.authority_code,
  p.ingest_date
FROM `gold.person_profiles_master` p,
UNNEST(p.documents) AS d;

-- 7. Gold Authorized View: Masked Profiles for Lower-Privilege Consumers
CREATE OR REPLACE VIEW `gold.v_person_profiles_masked`
OPTIONS(
  description="[SECURITY]: Authorized View providing masked PII profiles for Tier 1 / general analytics agents."
) AS
SELECT
  person_id,
  primary_full_name,
  sex_label,
  EXTRACT(YEAR FROM birth_date) AS birth_year,
  CASE
    WHEN primary_phone IS NOT NULL THEN CONCAT('+7 (***) ***-', SUBSTR(primary_phone, -4))
    ELSE NULL
  END AS primary_phone_masked,
  CASE
    WHEN primary_email IS NOT NULL THEN CONCAT('***@', SPLIT(primary_email, '@')[SAFE_OFFSET(1)])
    ELSE NULL
  END AS primary_email_masked,
  primary_address,
  latest_actuality_date,
  source_ids,
  ingest_date
FROM `gold.person_profiles_master`;

-- 8. Gold Metadata Table: Semantic Data Dictionary for AI Agents
CREATE TABLE IF NOT EXISTS `gold.semantic_data_dictionary` (
  table_name STRING NOT NULL,
  table_type STRING NOT NULL,
  domain STRING NOT NULL,
  purpose STRING NOT NULL,
  table_grain STRING NOT NULL,
  primary_key STRING NOT NULL,
  when_to_use STRING NOT NULL,
  when_not_to_use STRING NOT NULL,
  example_sql STRING NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- =============================================================================
-- Stored Procedure: sp_build_gold
-- =============================================================================
CREATE OR REPLACE PROCEDURE `gold.sp_build_gold`(p_ingest_date DATE)
BEGIN
  DECLARE v_date DATE DEFAULT COALESCE(p_ingest_date, CURRENT_DATE());

  -- Clean partition before rebuilding (idempotent daily re-runs)
  DELETE FROM `gold.person_profiles_master` WHERE ingest_date = v_date;
  DELETE FROM `gold.person_movements_fact` WHERE ingest_date = v_date;
  DELETE FROM `gold.person_employment_fact` WHERE ingest_date = v_date;
  DELETE FROM `gold.person_vehicles_fact` WHERE ingest_date = v_date;
  DELETE FROM `gold.person_digital_footprint_fact` WHERE ingest_date = v_date;

  -- ---------------------------------------------------------------------------
  -- 1. Identity Resolution & Entity Linking into gold.person_profiles_master
  -- ---------------------------------------------------------------------------
  -- Anchor persons: identify valid distinct persons with non-null clean names
  CREATE TEMP TABLE temp_person_anchors AS
  SELECT
    p.source_id,
    p.source_entity_id,
    p.full_name,
    p.sex_code,
    p.sex_label,
    p.birth_date,
    p.birth_place,
    p.actuality_date,
    -- Match key 1: Normalized full_name + birth_date
    -- Match key 2: First phone associated with this source_entity_id
    c.contact_value AS phone_anchor,
    d.doc_serial AS doc_anchor
  FROM `silver.persons` p
  LEFT JOIN (
    SELECT source_entity_id, contact_value,
      ROW_NUMBER() OVER(PARTITION BY source_entity_id ORDER BY created_at) AS rn
    FROM `silver.contacts` WHERE contact_type = 'PHONE' AND ingest_date = v_date
  ) c ON p.source_entity_id = c.source_entity_id AND c.rn = 1
  LEFT JOIN (
    SELECT source_entity_id, doc_serial,
      ROW_NUMBER() OVER(PARTITION BY source_entity_id ORDER BY created_at) AS rn
    FROM `silver.documents` WHERE ingest_date = v_date
  ) d ON p.source_entity_id = d.source_entity_id AND d.rn = 1
  WHERE p.ingest_date = v_date AND p.full_name IS NOT NULL;

  -- Compute deterministic cluster ID (person_id)
  CREATE TEMP TABLE temp_resolved_identities AS
  SELECT
    source_entity_id,
    source_id,
    full_name,
    sex_code,
    sex_label,
    birth_date,
    birth_place,
    actuality_date,
    -- Deterministic person_id based on (name + birth_date) OR (name + phone) OR doc OR fallback
    CASE
      WHEN full_name IS NOT NULL AND birth_date IS NOT NULL
        THEN silver.hash_entity_id(CONCAT('NAME_DOB:', full_name, '|', CAST(birth_date AS STRING)))
      WHEN full_name IS NOT NULL AND phone_anchor IS NOT NULL
        THEN silver.hash_entity_id(CONCAT('NAME_PHONE:', full_name, '|', phone_anchor))
      WHEN doc_anchor IS NOT NULL
        THEN silver.hash_entity_id(CONCAT('DOC:', doc_anchor))
      ELSE silver.hash_entity_id(CONCAT('SOURCE:', source_id, '|', source_entity_id))
    END AS person_id
  FROM temp_person_anchors;

  -- ---------------------------------------------------------------------------
  -- Pre-aggregate attribute arrays per resolved person_id
  -- ---------------------------------------------------------------------------
  CREATE TEMP TABLE temp_person_phones AS
  SELECT r.person_id, ARRAY_AGG(DISTINCT c.contact_value IGNORE NULLS) AS phones, ANY_VALUE(c.contact_value) AS primary_phone
  FROM temp_resolved_identities r
  JOIN `silver.contacts` c ON r.source_entity_id = c.source_entity_id AND c.contact_type = 'PHONE' AND c.ingest_date = v_date
  GROUP BY r.person_id;

  CREATE TEMP TABLE temp_person_emails AS
  SELECT r.person_id, ARRAY_AGG(DISTINCT c.contact_value IGNORE NULLS) AS emails, ANY_VALUE(c.contact_value) AS primary_email
  FROM temp_resolved_identities r
  JOIN `silver.contacts` c ON r.source_entity_id = c.source_entity_id AND c.contact_type = 'EMAIL' AND c.ingest_date = v_date
  GROUP BY r.person_id;

  CREATE TEMP TABLE temp_person_addresses AS
  SELECT r.person_id, ARRAY_AGG(DISTINCT a.address_raw IGNORE NULLS) AS addresses, ANY_VALUE(a.address_raw) AS primary_address
  FROM temp_resolved_identities r
  JOIN `silver.addresses` a ON r.source_entity_id = a.source_entity_id AND a.ingest_date = v_date
  WHERE a.address_raw IS NOT NULL AND TRIM(a.address_raw) != ''
  GROUP BY r.person_id;

  CREATE TEMP TABLE temp_person_docs AS
  SELECT r.person_id, ARRAY_AGG(STRUCT(d.doc_type AS type, d.doc_type_name AS type_name, d.doc_serial AS serial, d.date_issue, d.authority, d.authority_code) IGNORE NULLS) AS documents
  FROM temp_resolved_identities r
  JOIN `silver.documents` d ON r.source_entity_id = d.source_entity_id AND d.ingest_date = v_date
  GROUP BY r.person_id;

  CREATE TEMP TABLE temp_person_works AS
  SELECT r.person_id, ARRAY_AGG(STRUCT(w.organization_name, w.job_title, w.company_inn, w.company_ogrn, w.salary, w.actuality_date) IGNORE NULLS) AS works
  FROM temp_resolved_identities r
  JOIN `silver.works` w ON r.source_entity_id = w.source_entity_id AND w.ingest_date = v_date
  GROUP BY r.person_id;

  CREATE TEMP TABLE temp_person_vehicles AS
  SELECT r.person_id, ARRAY_AGG(STRUCT(v.license_plate, v.vin, v.model, v.manufacture_year, v.color) IGNORE NULLS) AS vehicles
  FROM temp_resolved_identities r
  JOIN `silver.vehicles` v ON r.source_entity_id = v.source_entity_id AND v.ingest_date = v_date
  GROUP BY r.person_id;

  CREATE TEMP TABLE temp_person_digital AS
  SELECT r.person_id, ARRAY_AGG(STRUCT(df.channel_type, df.channel_value, df.ip_country, df.registration_time) IGNORE NULLS) AS digital_footprints
  FROM temp_resolved_identities r
  JOIN `silver.digital_footprint` df ON r.source_entity_id = df.source_entity_id AND df.ingest_date = v_date
  GROUP BY r.person_id;

  -- Group by person_id and aggregate all attributes into Gold master
  INSERT INTO `gold.person_profiles_master` (
    person_id, primary_full_name, sex_code, sex_label, birth_date, birth_place,
    primary_phone, primary_email, primary_address, latest_actuality_date,
    all_names, phones, emails, addresses, documents, works, vehicles, digital_footprints,
    source_ids, source_entity_ids, ingest_date
  )
  SELECT
    r.person_id,
    -- Primary scalar attributes
    ANY_VALUE(r.full_name) AS primary_full_name,
    ANY_VALUE(r.sex_code) AS sex_code,
    COALESCE(ANY_VALUE(r.sex_label), 'UNKNOWN') AS sex_label,
    ANY_VALUE(r.birth_date) AS birth_date,
    ANY_VALUE(r.birth_place) AS birth_place,
    ANY_VALUE(ph.primary_phone) AS primary_phone,
    ANY_VALUE(em.primary_email) AS primary_email,
    ANY_VALUE(ad.primary_address) AS primary_address,
    MAX(r.actuality_date) AS latest_actuality_date,
    -- Arrays
    ARRAY_AGG(DISTINCT r.full_name IGNORE NULLS) AS all_names,
    COALESCE(ANY_VALUE(ph.phones), ARRAY<STRING>[]) AS phones,
    COALESCE(ANY_VALUE(em.emails), ARRAY<STRING>[]) AS emails,
    COALESCE(ANY_VALUE(ad.addresses), ARRAY<STRING>[]) AS addresses,
    COALESCE(ANY_VALUE(dc.documents), ARRAY<STRUCT<type INT64, type_name STRING, serial STRING, date_issue DATE, authority STRING, authority_code STRING>>[]) AS documents,
    COALESCE(ANY_VALUE(wk.works), ARRAY<STRUCT<organization_name STRING, job_title STRING, company_inn STRING, company_ogrn STRING, salary NUMERIC, actuality_date DATE>>[]) AS works,
    COALESCE(ANY_VALUE(vh.vehicles), ARRAY<STRUCT<license_plate STRING, vin STRING, model STRING, manufacture_year INT64, color STRING>>[]) AS vehicles,
    COALESCE(ANY_VALUE(dg.digital_footprints), ARRAY<STRUCT<channel_type STRING, channel_value STRING, ip_country STRING, registration_time TIMESTAMP>>[]) AS digital_footprints,
    ARRAY_AGG(DISTINCT r.source_id IGNORE NULLS) AS source_ids,
    ARRAY_AGG(DISTINCT r.source_entity_id IGNORE NULLS) AS source_entity_ids,
    v_date AS ingest_date
  FROM temp_resolved_identities r
  LEFT JOIN temp_person_phones ph ON r.person_id = ph.person_id
  LEFT JOIN temp_person_emails em ON r.person_id = em.person_id
  LEFT JOIN temp_person_addresses ad ON r.person_id = ad.person_id
  LEFT JOIN temp_person_docs dc ON r.person_id = dc.person_id
  LEFT JOIN temp_person_works wk ON r.person_id = wk.person_id
  LEFT JOIN temp_person_vehicles vh ON r.person_id = vh.person_id
  LEFT JOIN temp_person_digital dg ON r.person_id = dg.person_id
  GROUP BY r.person_id;

  -- ---------------------------------------------------------------------------
  -- 2. Build Fact Tables with Links to Person Profiles
  -- ---------------------------------------------------------------------------
  -- 2.1 Movements Fact
  INSERT INTO `gold.person_movements_fact` (
    movement_id, person_id, passenger_full_name, birth_date, passenger_phone,
    passenger_document_serial, ticket_number, transport_type, departure_date,
    port_from, port_to, train_number, seat_class, seat, source_id, ingest_date
  )
  SELECT
    silver.hash_entity_id(CONCAT(m.ticket_number, '|', CAST(m.departure_date AS STRING), '|', m.seat)) AS movement_id,
    p.person_id,
    COALESCE(p.primary_full_name, m.passenger_doc) AS passenger_full_name,
    p.birth_date,
    p.primary_phone AS passenger_phone,
    m.passenger_doc AS passenger_document_serial,
    m.ticket_number,
    m.transport_type,
    m.departure_date,
    m.port_from,
    m.port_to,
    m.train_number,
    m.seat_class,
    m.seat,
    m.source_id,
    v_date AS ingest_date
  FROM `silver.movements` m
  LEFT JOIN temp_resolved_identities r ON m.source_entity_id = r.source_entity_id
  LEFT JOIN `gold.person_profiles_master` p ON r.person_id = p.person_id AND p.ingest_date = v_date
  WHERE m.ingest_date = v_date;

  -- 2.2 Employment Fact
  INSERT INTO `gold.person_employment_fact` (
    employment_id, person_id, person_full_name, birth_date, person_phone,
    company_name, job_title, company_inn, company_ogrn, salary, application_status,
    source_id, actuality_date, ingest_date
  )
  SELECT
    silver.hash_entity_id(CONCAT(w.source_entity_id, '|', w.organization_name, '|', COALESCE(w.job_title, ''))) AS employment_id,
    p.person_id,
    COALESCE(p.primary_full_name, 'Unknown') AS person_full_name,
    p.birth_date,
    p.primary_phone AS person_phone,
    w.organization_name AS company_name,
    w.job_title,
    w.company_inn,
    w.company_ogrn,
    w.salary,
    w.application_status,
    w.source_id,
    w.actuality_date,
    v_date AS ingest_date
  FROM `silver.works` w
  LEFT JOIN temp_resolved_identities r ON w.source_entity_id = r.source_entity_id
  LEFT JOIN `gold.person_profiles_master` p ON r.person_id = p.person_id AND p.ingest_date = v_date
  WHERE w.ingest_date = v_date;

  -- 2.3 Vehicles Fact
  INSERT INTO `gold.person_vehicles_fact` (
    vehicle_fact_id, person_id, owner_full_name, birth_date, owner_phone,
    license_plate, vin, model, manufacture_year, color, source_id, ingest_date
  )
  SELECT
    silver.hash_entity_id(CONCAT(v.source_entity_id, '|', v.license_plate, '|', COALESCE(v.vin, ''))) AS vehicle_fact_id,
    p.person_id,
    COALESCE(p.primary_full_name, 'Unknown') AS owner_full_name,
    p.birth_date,
    p.primary_phone AS owner_phone,
    v.license_plate,
    v.vin,
    v.model,
    v.manufacture_year,
    v.color,
    v.source_id,
    v_date AS ingest_date
  FROM `silver.vehicles` v
  LEFT JOIN temp_resolved_identities r ON v.source_entity_id = r.source_entity_id
  LEFT JOIN `gold.person_profiles_master` p ON r.person_id = p.person_id AND p.ingest_date = v_date
  WHERE v.ingest_date = v_date;

  -- 2.4 Digital Footprints Fact
  INSERT INTO `gold.person_digital_footprint_fact` (
    footprint_id, person_id, user_full_name, contact_phone, contact_email,
    channel_type, channel_value, ip_country, registration_time, source_id, ingest_date
  )
  SELECT
    silver.hash_entity_id(CONCAT(df.source_entity_id, '|', df.channel_type, '|', df.channel_value)) AS footprint_id,
    p.person_id,
    COALESCE(p.primary_full_name, 'Unknown') AS user_full_name,
    p.primary_phone AS contact_phone,
    p.primary_email AS contact_email,
    df.channel_type,
    df.channel_value,
    df.ip_country,
    df.registration_time,
    df.source_id,
    v_date AS ingest_date
  FROM `silver.digital_footprint` df
  LEFT JOIN temp_resolved_identities r ON df.source_entity_id = r.source_entity_id
  LEFT JOIN `gold.person_profiles_master` p ON r.person_id = p.person_id AND p.ingest_date = v_date
  WHERE df.ingest_date = v_date;

  -- ---------------------------------------------------------------------------
  -- 3. Populate Semantic Data Dictionary for AI Agents
  -- ---------------------------------------------------------------------------
  DELETE FROM `gold.semantic_data_dictionary` WHERE TRUE;
  INSERT INTO `gold.semantic_data_dictionary` (
    table_name, table_type, domain, purpose, table_grain, primary_key, when_to_use, when_not_to_use, example_sql
  ) VALUES
  (
    'gold.person_profiles_master',
    'TABLE',
    'IDENTITY',
    'Unified 360-degree master profile table with scalar primary fields and full historical arrays.',
    '1 row per unique resolved individual',
    'person_id',
    'User asks for person profile, contact info (phone, email, address), demographics, or cross-source presence.',
    'User asks about specific rail ticket details, train routes, or company employment lists.',
    'SELECT primary_full_name, primary_phone, primary_email, birth_date FROM gold.person_profiles_master WHERE primary_full_name = "Петров Иван Иванович";'
  ),
  (
    'gold.person_movements_fact',
    'TABLE',
    'TRANSIT',
    'Denormalized passenger rail transit movement fact table.',
    '1 row per ticket movement event',
    'movement_id',
    'User asks about travel itineraries, train departures, station routes, or passenger travel dates.',
    'User asks about general person profiles without travel context.',
    'SELECT passenger_full_name, port_from, port_to, departure_date, train_number, seat FROM gold.person_movements_fact WHERE port_from = "МОСКВА" AND departure_date >= "2013-11-01";'
  ),
  (
    'gold.person_employment_fact',
    'TABLE',
    'EMPLOYMENT',
    'Denormalized corporate employment and loan applicant affiliations.',
    '1 row per person-company employment record',
    'employment_id',
    'User asks about who works at a specific company, employer INN queries, or job titles.',
    'User asks about travel movements or vehicle registrations.',
    'SELECT person_full_name, company_name, job_title, salary FROM gold.person_employment_fact WHERE UPPER(company_name) LIKE "%МАГНИТ%";'
  ),
  (
    'gold.person_vehicles_fact',
    'TABLE',
    'VEHICLES',
    'Denormalized vehicle ownership table linking individuals to registered vehicles.',
    '1 row per vehicle ownership record',
    'vehicle_fact_id',
    'User asks about car ownership, license plate lookups, or VIN searches.',
    'User asks about passenger tickets or employment.',
    'SELECT owner_full_name, license_plate, vin, model, color FROM gold.person_vehicles_fact WHERE license_plate = "А777АА78";'
  ),
  (
    'gold.person_digital_footprint_fact',
    'TABLE',
    'DIGITAL',
    'Denormalized digital footprint session table linking individuals to IPs and Telegram identifiers.',
    '1 row per digital identifier session',
    'footprint_id',
    'User asks about online account registration IPs, Telegram handles, or digital activity.',
    'User asks about physical travel movements or car ownership.',
    'SELECT user_full_name, channel_type, channel_value, ip_country FROM gold.person_digital_footprint_fact WHERE channel_type = "IP" AND channel_value = "185.220.101.5";'
  ),
  (
    'gold.person_documents_lookup',
    'VIEW',
    'DOCUMENTS',
    'Pre-unnested identity document lookup view linking persons to passports, INN, and SNILS.',
    '1 row per identity document',
    'document_serial',
    'User queries by passport number, INN, or SNILS.',
    'User queries by phone or email directly.',
    'SELECT primary_full_name, document_type_name, document_serial FROM gold.person_documents_lookup WHERE document_serial = "4012686811";'
  );

END;
