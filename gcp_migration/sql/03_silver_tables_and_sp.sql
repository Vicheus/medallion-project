-- =============================================================================
-- 03_silver_tables_and_sp.sql
-- GCP Medallion Architecture: Silver Normalized Entity Tables & Transformation Routine
-- Project: medallion-project-512608 | Location: europe-west1
-- =============================================================================

-- 1. Silver Table: Normalized Persons
CREATE TABLE IF NOT EXISTS `silver.persons` (
  source_id STRING NOT NULL,
  source_entity_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  full_name STRING,
  first_name STRING,
  last_name STRING,
  middle_name STRING,
  sex_code INT64,
  sex_label STRING,
  birth_date DATE,
  birth_place STRING,
  actuality_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY source_id, source_entity_id, full_name
OPTIONS(
  description="Silver cleansed and normalized individual persons extracted from all Bronze sources."
);

-- 2. Silver Table: Contacts (Phones and Emails)
CREATE TABLE IF NOT EXISTS `silver.contacts` (
  source_id STRING NOT NULL,
  source_entity_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  contact_type STRING NOT NULL OPTIONS(description="'PHONE' or 'EMAIL'"),
  contact_value STRING NOT NULL OPTIONS(description="Normalized E.164 phone or cleaned email"),
  is_valid BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY contact_type, contact_value, source_entity_id
OPTIONS(
  description="Silver normalized contact endpoints (E.164 phone numbers and validated emails)."
);

-- 3. Silver Table: Physical Addresses
CREATE TABLE IF NOT EXISTS `silver.addresses` (
  source_id STRING NOT NULL,
  source_entity_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  address_raw STRING,
  postal_code STRING,
  city STRING,
  street STRING,
  house STRING,
  room STRING,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY source_id, source_entity_id
OPTIONS(
  description="Silver cleansed physical and registration addresses."
);

-- 4. Silver Table: Identity Documents
CREATE TABLE IF NOT EXISTS `silver.documents` (
  source_id STRING NOT NULL,
  source_entity_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  doc_type INT64 OPTIONS(description="0=Passport, 1=INN, 2=SNILS, 5=Birth Cert, 4=Other"),
  doc_type_name STRING,
  doc_serial STRING NOT NULL,
  date_issue DATE,
  date_expire DATE,
  authority STRING,
  authority_code STRING,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY doc_type_name, doc_serial, source_entity_id
OPTIONS(
  description="Silver cleansed and classified identity documents (Passports, INNs, SNILS)."
);

-- 5. Silver Table: Employment and Corporate Relationships
CREATE TABLE IF NOT EXISTS `silver.works` (
  source_id STRING NOT NULL,
  source_entity_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  organization_name STRING,
  job_title STRING,
  company_inn STRING,
  company_ogrn STRING,
  salary NUMERIC,
  application_status STRING,
  actuality_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY company_inn, organization_name, source_entity_id
OPTIONS(
  description="Silver employment positions, employer organizations, and corporate affiliation records."
);

-- 6. Silver Table: Travel and Transportation Movements
CREATE TABLE IF NOT EXISTS `silver.movements` (
  source_id STRING NOT NULL,
  source_entity_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  ticket_number STRING,
  transport_type STRING DEFAULT 'RAIL',
  departure_date DATE NOT NULL,
  port_from STRING,
  port_to STRING,
  train_number STRING,
  seat_class STRING,
  seat STRING,
  passenger_doc STRING,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY departure_date
CLUSTER BY port_from, port_to, source_entity_id
OPTIONS(
  description="Silver travel tickets, routes, and passenger transport movements."
);

-- 7. Silver Table: Registered Vehicles
CREATE TABLE IF NOT EXISTS `silver.vehicles` (
  source_id STRING NOT NULL,
  source_entity_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  license_plate STRING,
  vin STRING,
  model STRING,
  manufacture_year INT64,
  color STRING,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY license_plate, vin, source_entity_id
OPTIONS(
  description="Silver vehicle registrations, license plates, VINs, and car models."
);

-- 8. Silver Table: Digital Footprint (IPs and Socials)
CREATE TABLE IF NOT EXISTS `silver.digital_footprint` (
  source_id STRING NOT NULL,
  source_entity_id STRING NOT NULL,
  ingest_date DATE NOT NULL,
  channel_type STRING NOT NULL OPTIONS(description="'IP' or 'TELEGRAM'"),
  channel_value STRING NOT NULL,
  ip_country STRING,
  registration_time TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY ingest_date
CLUSTER BY channel_type, channel_value, source_entity_id
OPTIONS(
  description="Silver digital footprint identifiers (IP addresses and Telegram handles)."
);

