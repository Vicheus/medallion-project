-- =============================================================================
-- 06_dynamic_silver_engine.sql
-- Autonomous Dynamic Silver Extraction Engine
-- Project: medallion-project-512608 | Location: europe-west1
--
-- Replaces brittle monolithic hardcoded UNION ALL procedures with dynamic,
-- catalog-driven ingestion that never throws "Table not found" compile errors!
-- =============================================================================

-- =============================================================================
-- Procedure: silver.sp_transform_metadata_source
-- Dynamically transforms a SINGLE source from Bronze to Silver using mapping rules
-- =============================================================================
CREATE OR REPLACE PROCEDURE `silver.sp_transform_metadata_source`(p_source_id STRING, p_ingest_date DATE)
BEGIN
  DECLARE v_date DATE DEFAULT COALESCE(p_ingest_date, CURRENT_DATE());
  DECLARE v_table_name STRING DEFAULT CONCAT('raw_', p_source_id);
  DECLARE v_table_exists INT64 DEFAULT 0;
  DECLARE v_spec JSON;
  DECLARE v_sql STRING;

  -- 1. Check if Bronze table exists in INFORMATION_SCHEMA
  SET v_table_exists = (
    SELECT COUNT(*)
    FROM `medallion-project-512608.bronze.INFORMATION_SCHEMA.TABLES`
    WHERE table_name = v_table_name
  );

  IF v_table_exists = 0 THEN
    -- Graceful skip: NO compile-time or run-time crash if table has not arrived yet!
    SELECT FORMAT('[SKIP] Source bronze.%s does not exist in BigQuery yet. Skipping extraction.', v_table_name) AS status;
    RETURN;
  END IF;

  -- 2. Fetch mapping spec from central catalog
  SET v_spec = (
    SELECT mapping_spec
    FROM `ops_monitoring.source_catalog`
    WHERE source_id = p_source_id AND is_active = TRUE
    LIMIT 1
  );

  IF v_spec IS NULL THEN
    SELECT FORMAT('[SKIP] Source %s has no active mapping spec in ops_monitoring.source_catalog.', p_source_id) AS status;
    RETURN;
  END IF;

  -- 3. Idempotently clear target partitions for this source_id on v_date
  DELETE FROM `silver.persons` WHERE source_id = p_source_id AND ingest_date = v_date;
  DELETE FROM `silver.contacts` WHERE source_id = p_source_id AND ingest_date = v_date;
  DELETE FROM `silver.addresses` WHERE source_id = p_source_id AND ingest_date = v_date;
  DELETE FROM `silver.documents` WHERE source_id = p_source_id AND ingest_date = v_date;
  DELETE FROM `silver.works` WHERE source_id = p_source_id AND ingest_date = v_date;
  DELETE FROM `silver.digital_footprint` WHERE source_id = p_source_id AND ingest_date = v_date;

  -- ---------------------------------------------------------------------------
  -- 4. Entity: PERSONS
  -- ---------------------------------------------------------------------------
  IF JSON_VALUE(v_spec.target_entities.persons.enabled) = 'true' THEN
    SET v_sql = FORMAT("""
      INSERT INTO `silver.persons` (
        source_id, source_entity_id, ingest_date,
        full_name, first_name, last_name, middle_name,
        sex_code, sex_label, birth_date, birth_place, actuality_date
      )
      SELECT
        source_id,
        source_entity_id,
        @v_date,
        silver.clean_name(%s),
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
      FROM `bronze.%s`
      WHERE ingest_date = @v_date
    """,
      -- full_name
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.persons.full_name_col) IS NOT NULL THEN
          FORMAT("CAST(%s AS STRING)", JSON_VALUE(v_spec.target_entities.persons.full_name_col))
        WHEN JSON_VALUE(v_spec.target_entities.persons.first_name_col) IS NOT NULL THEN
          FORMAT("CONCAT(COALESCE(CAST(%s AS STRING),''), ' ', COALESCE(CAST(%s AS STRING),''), ' ', COALESCE(CAST(%s AS STRING),''))",
            JSON_VALUE(v_spec.target_entities.persons.last_name_col),
            JSON_VALUE(v_spec.target_entities.persons.first_name_col),
            JSON_VALUE(v_spec.target_entities.persons.middle_name_col)
          )
        ELSE "CAST(NULL AS STRING)"
      END,
      -- first_name
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.persons.first_name_col) IS NOT NULL THEN
          FORMAT("silver.clean_name(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.persons.first_name_col))
        ELSE "CAST(NULL AS STRING)"
      END,
      -- last_name
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.persons.last_name_col) IS NOT NULL THEN
          FORMAT("silver.clean_name(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.persons.last_name_col))
        ELSE "CAST(NULL AS STRING)"
      END,
      -- middle_name
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.persons.middle_name_col) IS NOT NULL THEN
          FORMAT("silver.clean_name(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.persons.middle_name_col))
        ELSE "CAST(NULL AS STRING)"
      END,
      -- sex_code
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.persons.sex_col) IS NOT NULL THEN
          FORMAT("(silver.normalize_sex(CAST(%s AS STRING))).code", JSON_VALUE(v_spec.target_entities.persons.sex_col))
        ELSE "CAST(NULL AS INT64)"
      END,
      -- sex_label
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.persons.sex_col) IS NOT NULL THEN
          FORMAT("(silver.normalize_sex(CAST(%s AS STRING))).label", JSON_VALUE(v_spec.target_entities.persons.sex_col))
        ELSE "'UNKNOWN'"
      END,
      -- birth_date
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.persons.birth_date_col) IS NOT NULL THEN
          FORMAT("silver.parse_date_safe(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.persons.birth_date_col))
        ELSE "CAST(NULL AS DATE)"
      END,
      -- birth_place
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.persons.birth_place_col) IS NOT NULL THEN
          FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.persons.birth_place_col))
        ELSE "CAST(NULL AS STRING)"
      END,
      -- actuality_date
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.persons.actuality_date_col) IS NOT NULL THEN
          FORMAT("COALESCE(silver.parse_date_safe(CAST(%s AS STRING)), @v_date)", JSON_VALUE(v_spec.target_entities.persons.actuality_date_col))
        ELSE "@v_date"
      END,
      -- from table
      v_table_name
    );
    EXECUTE IMMEDIATE v_sql USING v_date AS v_date;
  END IF;

  -- ---------------------------------------------------------------------------
  -- 5. Entity: CONTACTS
  -- ---------------------------------------------------------------------------
  IF v_spec.target_entities.contacts IS NOT NULL THEN
    FOR item IN (
      SELECT
        JSON_VALUE(c.contact_type) AS c_type,
        JSON_VALUE(c.value_col) AS val_col
      FROM UNNEST(JSON_EXTRACT_ARRAY(v_spec.target_entities.contacts)) c
    ) DO
      IF item.val_col IS NOT NULL THEN
        SET v_sql = FORMAT("""
          INSERT INTO `silver.contacts` (
            source_id, source_entity_id, ingest_date,
            contact_type, contact_value, is_valid
          )
          SELECT
            source_id,
            source_entity_id,
            @v_date,
            '%s',
            %s,
            TRUE
          FROM `bronze.%s`
          WHERE ingest_date = @v_date
            AND %s IS NOT NULL
            AND %s != ''
        """,
          item.c_type,
          CASE
            WHEN item.c_type = 'PHONE' THEN FORMAT("silver.clean_phone_e164(CAST(%s AS STRING))", item.val_col)
            WHEN item.c_type = 'EMAIL' THEN FORMAT("silver.clean_email(CAST(%s AS STRING))", item.val_col)
            ELSE FORMAT("TRIM(CAST(%s AS STRING))", item.val_col)
          END,
          v_table_name,
          FORMAT("CAST(%s AS STRING)", item.val_col),
          CASE
            WHEN item.c_type = 'PHONE' THEN FORMAT("silver.clean_phone_e164(CAST(%s AS STRING))", item.val_col)
            WHEN item.c_type = 'EMAIL' THEN FORMAT("silver.clean_email(CAST(%s AS STRING))", item.val_col)
            ELSE FORMAT("TRIM(CAST(%s AS STRING))", item.val_col)
          END
        );
        EXECUTE IMMEDIATE v_sql USING v_date AS v_date;
      END IF;
    END FOR;
  END IF;

  -- ---------------------------------------------------------------------------
  -- 6. Entity: ADDRESSES
  -- ---------------------------------------------------------------------------
  IF JSON_VALUE(v_spec.target_entities.addresses.enabled) = 'true' THEN
    SET v_sql = FORMAT("""
      INSERT INTO `silver.addresses` (
        source_id, source_entity_id, ingest_date,
        address_raw, postal_code, city, street, house, room
      )
      SELECT
        source_id,
        source_entity_id,
        @v_date,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
      FROM `bronze.%s`
      WHERE ingest_date = @v_date
        AND (%s IS NOT NULL OR %s IS NOT NULL OR %s IS NOT NULL)
    """,
      -- address_raw
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.addresses.address_raw_col) IS NOT NULL THEN
          FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.addresses.address_raw_col))
        ELSE
          FORMAT("TRIM(CONCAT(COALESCE(CAST(%s AS STRING),''), ' ', COALESCE(CAST(%s AS STRING),''), ' ', COALESCE(CAST(%s AS STRING),'')))",
            COALESCE(JSON_VALUE(v_spec.target_entities.addresses.city_col), "''"),
            COALESCE(JSON_VALUE(v_spec.target_entities.addresses.street_col), "''"),
            COALESCE(JSON_VALUE(v_spec.target_entities.addresses.house_col), "''")
          )
      END,
      -- postal_code
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.addresses.postal_code_col) IS NOT NULL THEN
          FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.addresses.postal_code_col))
        ELSE "CAST(NULL AS STRING)"
      END,
      -- city
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.addresses.city_col) IS NOT NULL THEN
          FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.addresses.city_col))
        ELSE "CAST(NULL AS STRING)"
      END,
      -- street
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.addresses.street_col) IS NOT NULL THEN
          FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.addresses.street_col))
        ELSE "CAST(NULL AS STRING)"
      END,
      -- house
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.addresses.house_col) IS NOT NULL THEN
          FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.addresses.house_col))
        ELSE "CAST(NULL AS STRING)"
      END,
      -- room
      CASE
        WHEN JSON_VALUE(v_spec.target_entities.addresses.room_col) IS NOT NULL THEN
          FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.addresses.room_col))
        ELSE "CAST(NULL AS STRING)"
      END,
      v_table_name,
      COALESCE(FORMAT("CAST(%s AS STRING)", JSON_VALUE(v_spec.target_entities.addresses.address_raw_col)), "NULL"),
      COALESCE(FORMAT("CAST(%s AS STRING)", JSON_VALUE(v_spec.target_entities.addresses.city_col)), "NULL"),
      COALESCE(FORMAT("CAST(%s AS STRING)", JSON_VALUE(v_spec.target_entities.addresses.street_col)), "NULL")
    );
    EXECUTE IMMEDIATE v_sql USING v_date AS v_date;
  END IF;

  -- ---------------------------------------------------------------------------
  -- 7. Entity: DOCUMENTS
  -- ---------------------------------------------------------------------------
  IF v_spec.target_entities.documents IS NOT NULL THEN
    FOR doc IN (
      SELECT
        CAST(JSON_VALUE(d.doc_type) AS INT64) AS d_type,
        JSON_VALUE(d.doc_type_name) AS d_type_name,
        JSON_VALUE(d.doc_serial_col) AS serial_col,
        JSON_VALUE(d.doc_number_col) AS num_col,
        JSON_VALUE(d.authority_col) AS auth_col,
        JSON_VALUE(d.authority_code_col) AS auth_code_col,
        JSON_VALUE(d.date_issue_col) AS issue_col,
        JSON_VALUE(d.date_expire_col) AS expire_col
      FROM UNNEST(JSON_EXTRACT_ARRAY(v_spec.target_entities.documents)) d
    ) DO
      IF doc.serial_col IS NOT NULL THEN
        SET v_sql = FORMAT("""
          INSERT INTO `silver.documents` (
            source_id, source_entity_id, ingest_date,
            doc_type, doc_type_name, doc_serial, date_issue, date_expire, authority, authority_code
          )
          SELECT
            source_id,
            source_entity_id,
            @v_date,
            %d,
            '%s',
            %s,
            %s,
            %s,
            %s,
            %s
          FROM `bronze.%s`
          WHERE ingest_date = @v_date
            AND %s IS NOT NULL
            AND TRIM(CAST(%s AS STRING)) != ''
        """,
          COALESCE(doc.d_type, 0),
          COALESCE(doc.d_type_name, 'PASSPORT'),
          -- doc_serial
          CASE
            WHEN doc.num_col IS NOT NULL THEN
              FORMAT("TRIM(CONCAT(COALESCE(CAST(%s AS STRING),''), ' ', COALESCE(CAST(%s AS STRING),'')))", doc.serial_col, doc.num_col)
            ELSE
              FORMAT("TRIM(CAST(%s AS STRING))", doc.serial_col)
          END,
          -- date_issue
          CASE WHEN doc.issue_col IS NOT NULL THEN FORMAT("silver.parse_date_safe(CAST(%s AS STRING))", doc.issue_col) ELSE "CAST(NULL AS DATE)" END,
          -- date_expire
          CASE WHEN doc.expire_col IS NOT NULL THEN FORMAT("silver.parse_date_safe(CAST(%s AS STRING))", doc.expire_col) ELSE "CAST(NULL AS DATE)" END,
          -- authority
          CASE WHEN doc.auth_col IS NOT NULL THEN FORMAT("TRIM(CAST(%s AS STRING))", doc.auth_col) ELSE "CAST(NULL AS STRING)" END,
          -- authority_code
          CASE WHEN doc.auth_code_col IS NOT NULL THEN FORMAT("TRIM(CAST(%s AS STRING))", doc.auth_code_col) ELSE "CAST(NULL AS STRING)" END,
          v_table_name,
          FORMAT("CAST(%s AS STRING)", doc.serial_col),
          doc.serial_col
        );
        EXECUTE IMMEDIATE v_sql USING v_date AS v_date;
      END IF;
    END FOR;
  END IF;

  -- ---------------------------------------------------------------------------
  -- 8. Entity: WORKS (Employment & Corporate)
  -- ---------------------------------------------------------------------------
  IF JSON_VALUE(v_spec.target_entities.works.enabled) = 'true' THEN
    SET v_sql = FORMAT("""
      INSERT INTO `silver.works` (
        source_id, source_entity_id, ingest_date,
        organization_name, job_title, company_inn, company_ogrn, salary, application_status, actuality_date
      )
      SELECT
        source_id,
        source_entity_id,
        @v_date,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
      FROM `bronze.%s`
      WHERE ingest_date = @v_date
        AND (%s IS NOT NULL OR %s IS NOT NULL)
    """,
      -- organization_name
      CASE WHEN JSON_VALUE(v_spec.target_entities.works.organization_name_col) IS NOT NULL THEN FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.works.organization_name_col)) ELSE "CAST(NULL AS STRING)" END,
      -- job_title
      CASE WHEN JSON_VALUE(v_spec.target_entities.works.job_title_col) IS NOT NULL THEN FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.works.job_title_col)) ELSE "CAST(NULL AS STRING)" END,
      -- company_inn
      CASE WHEN JSON_VALUE(v_spec.target_entities.works.company_inn_col) IS NOT NULL THEN FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.works.company_inn_col)) ELSE "CAST(NULL AS STRING)" END,
      -- company_ogrn
      CASE WHEN JSON_VALUE(v_spec.target_entities.works.company_ogrn_col) IS NOT NULL THEN FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.works.company_ogrn_col)) ELSE "CAST(NULL AS STRING)" END,
      -- salary
      CASE WHEN JSON_VALUE(v_spec.target_entities.works.salary_col) IS NOT NULL THEN FORMAT("SAFE_CAST(%s AS NUMERIC)", JSON_VALUE(v_spec.target_entities.works.salary_col)) ELSE "CAST(NULL AS NUMERIC)" END,
      -- application_status
      CASE WHEN JSON_VALUE(v_spec.target_entities.works.application_status_col) IS NOT NULL THEN FORMAT("TRIM(CAST(%s AS STRING))", JSON_VALUE(v_spec.target_entities.works.application_status_col)) ELSE "CAST(NULL AS STRING)" END,
      -- actuality_date
      CASE WHEN JSON_VALUE(v_spec.target_entities.works.actuality_date_col) IS NOT NULL THEN FORMAT("COALESCE(silver.parse_date_safe(CAST(%s AS STRING)), @v_date)", JSON_VALUE(v_spec.target_entities.works.actuality_date_col)) ELSE "@v_date" END,
      v_table_name,
      COALESCE(FORMAT("CAST(%s AS STRING)", JSON_VALUE(v_spec.target_entities.works.organization_name_col)), "NULL"),
      COALESCE(FORMAT("CAST(%s AS STRING)", JSON_VALUE(v_spec.target_entities.works.company_inn_col)), "NULL")
    );
    EXECUTE IMMEDIATE v_sql USING v_date AS v_date;
  END IF;

  -- ---------------------------------------------------------------------------
  -- 9. Entity: DIGITAL FOOTPRINT
  -- ---------------------------------------------------------------------------
  IF v_spec.target_entities.digital_footprint IS NOT NULL THEN
    FOR fp IN (
      SELECT
        JSON_VALUE(f.channel_type) AS ch_type,
        JSON_VALUE(f.value_col) AS val_col,
        JSON_VALUE(f.country_col) AS country_col,
        JSON_VALUE(f.timestamp_col) AS ts_col
      FROM UNNEST(JSON_EXTRACT_ARRAY(v_spec.target_entities.digital_footprint)) f
    ) DO
      IF fp.val_col IS NOT NULL THEN
        SET v_sql = FORMAT("""
          INSERT INTO `silver.digital_footprint` (
            source_id, source_entity_id, ingest_date,
            channel_type, channel_value, ip_country, registration_time
          )
          SELECT
            source_id,
            source_entity_id,
            @v_date,
            '%s',
            %s,
            %s,
            %s
          FROM `bronze.%s`
          WHERE ingest_date = @v_date
            AND %s IS NOT NULL
            AND %s != ''
        """,
          COALESCE(fp.ch_type, 'IP'),
          -- channel_value
          CASE
            WHEN fp.ch_type = 'IP' THEN FORMAT("silver.clean_ip_v4(CAST(%s AS STRING))", fp.val_col)
            ELSE FORMAT("TRIM(CAST(%s AS STRING))", fp.val_col)
          END,
          -- ip_country
          CASE WHEN fp.country_col IS NOT NULL THEN FORMAT("TRIM(CAST(%s AS STRING))", fp.country_col) ELSE "CAST(NULL AS STRING)" END,
          -- registration_time
          CASE WHEN fp.ts_col IS NOT NULL THEN FORMAT("SAFE_CAST(silver.parse_date_safe(CAST(%s AS STRING)) AS TIMESTAMP)", fp.ts_col) ELSE "CURRENT_TIMESTAMP()" END,
          v_table_name,
          FORMAT("CAST(%s AS STRING)", fp.val_col),
          CASE
            WHEN fp.ch_type = 'IP' THEN FORMAT("silver.clean_ip_v4(CAST(%s AS STRING))", fp.val_col)
            ELSE FORMAT("TRIM(CAST(%s AS STRING))", fp.val_col)
          END
        );
        EXECUTE IMMEDIATE v_sql USING v_date AS v_date;
      END IF;
    END FOR;
  END IF;

END;

-- =============================================================================
-- Procedure: silver.sp_transform_all_metadata_sources
-- Dynamically iterates across all active METADATA_DRIVEN sources that exist in Bronze!
-- =============================================================================
CREATE OR REPLACE PROCEDURE `silver.sp_transform_all_metadata_sources`(p_ingest_date DATE)
BEGIN
  DECLARE v_date DATE DEFAULT COALESCE(p_ingest_date, CURRENT_DATE());

  -- Iterate through active metadata sources
  FOR src IN (
    SELECT c.source_id
    FROM `ops_monitoring.source_catalog` c
    WHERE c.pipeline_type = 'METADATA_DRIVEN' AND c.is_active = TRUE
    ORDER BY c.source_id
  ) DO
    CALL `silver.sp_transform_metadata_source`(src.source_id, v_date);
  END FOR;

END;

-- =============================================================================
-- Procedure: silver.sp_transform_to_silver (Hybrid Dynamic Dispatcher)
-- Dispatches metadata sources dynamically, and executes Dataform-staged complex models safely.
-- OPTIONS(strict_mode=false) suppresses compile-time failures for staging views.
-- =============================================================================
CREATE OR REPLACE PROCEDURE `silver.sp_transform_to_silver`(p_ingest_date DATE)
OPTIONS(strict_mode=false)
BEGIN
  DECLARE v_date DATE DEFAULT COALESCE(p_ingest_date, CURRENT_DATE());
  DECLARE v_has_0020 INT64 DEFAULT 0;
  DECLARE v_has_0500 INT64 DEFAULT 0;

  -- 1. Execute all active metadata-driven standard sources dynamically
  CALL `silver.sp_transform_all_metadata_sources`(v_date);

  -- 2. Execute Dataform / Complex Staged Sources safely (checking table existence)
  SET v_has_0020 = (SELECT COUNT(*) FROM `medallion-project-512608.bronze.INFORMATION_SCHEMA.TABLES` WHERE table_name = "raw_index_0020");
  SET v_has_0500 = (SELECT COUNT(*) FROM `medallion-project-512608.bronze.INFORMATION_SCHEMA.TABLES` WHERE table_name = "raw_index_0500");

  -- 2.1 Sirena Rail Movements (index_0020)
  IF v_has_0020 > 0 THEN
    DELETE FROM `silver.movements` WHERE ingest_date = v_date AND source_id = "index_0020";
    DELETE FROM `silver.persons` WHERE ingest_date = v_date AND source_id = "index_0020";
    DELETE FROM `silver.contacts` WHERE ingest_date = v_date AND source_id = "index_0020";
    DELETE FROM `silver.documents` WHERE ingest_date = v_date AND source_id = "index_0020";

    -- Insert into movements from validated staging view
    INSERT INTO `silver.movements` (
      source_id, source_entity_id, ingest_date, ticket_number, transport_type, departure_date,
      port_from, port_to, train_number, seat_class, seat, passenger_doc
    )
    SELECT
      source_id, source_entity_id, ingest_date, ticket_number, transport_type, departure_date,
      port_from, port_to, train_number, coach_class, seat, passenger_doc
    FROM `silver.stg_index_0020_movements`
    WHERE ingest_date = v_date;

    -- Passenger profile
    INSERT INTO `silver.persons` (source_id, source_entity_id, ingest_date, full_name, birth_date, actuality_date)
    SELECT source_id, source_entity_id, ingest_date, passenger_name, birth_date, ticket_date
    FROM `silver.stg_index_0020_movements`
    WHERE ingest_date = v_date AND passenger_name IS NOT NULL;

    -- Passenger phone
    INSERT INTO `silver.contacts` (source_id, source_entity_id, ingest_date, contact_type, contact_value, is_valid)
    SELECT source_id, source_entity_id, ingest_date, "PHONE", phone, TRUE
    FROM `silver.stg_index_0020_movements`
    WHERE ingest_date = v_date AND phone IS NOT NULL;

    -- Passenger document
    INSERT INTO `silver.documents` (source_id, source_entity_id, ingest_date, doc_type, doc_type_name, doc_serial)
    SELECT source_id, source_entity_id, ingest_date, 0, "PASSPORT", passenger_doc
    FROM `silver.stg_index_0020_movements`
    WHERE ingest_date = v_date AND passenger_doc IS NOT NULL;
  END IF;

  -- 2.2 GIBDD SPb Vehicles (index_0500)
  IF v_has_0500 > 0 THEN
    DELETE FROM `silver.vehicles` WHERE ingest_date = v_date AND source_id = "index_0500";
    DELETE FROM `silver.persons` WHERE ingest_date = v_date AND source_id = "index_0500";
    DELETE FROM `silver.contacts` WHERE ingest_date = v_date AND source_id = "index_0500";
    DELETE FROM `silver.documents` WHERE ingest_date = v_date AND source_id = "index_0500";
    DELETE FROM `silver.works` WHERE ingest_date = v_date AND source_id = "index_0500";

    -- Insert into vehicles from validated staging view
    INSERT INTO `silver.vehicles` (
      source_id, source_entity_id, ingest_date, license_plate, vin, model, manufacture_year, color
    )
    SELECT
      source_id, source_entity_id, ingest_date, license_plate, vin, model, manufacture_year, color
    FROM `silver.stg_index_0500_vehicles`
    WHERE ingest_date = v_date;

    -- Owner profile
    INSERT INTO `silver.persons` (source_id, source_entity_id, ingest_date, full_name, birth_date, actuality_date)
    SELECT source_id, source_entity_id, ingest_date, owner_full_name, owner_birth_date, v_date
    FROM `silver.stg_index_0500_vehicles`
    WHERE ingest_date = v_date AND owner_full_name IS NOT NULL;

    -- Owner phone
    INSERT INTO `silver.contacts` (source_id, source_entity_id, ingest_date, contact_type, contact_value, is_valid)
    SELECT source_id, source_entity_id, ingest_date, "PHONE", owner_phone, TRUE
    FROM `silver.stg_index_0500_vehicles`
    WHERE ingest_date = v_date AND owner_phone IS NOT NULL;

    -- Owner passport
    INSERT INTO `silver.documents` (source_id, source_entity_id, ingest_date, doc_type, doc_type_name, doc_serial)
    SELECT source_id, source_entity_id, ingest_date, 0, "PASSPORT", owner_passport
    FROM `silver.stg_index_0500_vehicles`
    WHERE ingest_date = v_date AND owner_passport IS NOT NULL;

    -- Corporate entity relationship if vehicle owned by company
    INSERT INTO `silver.works` (source_id, source_entity_id, ingest_date, organization_name, company_inn, company_ogrn, actuality_date)
    SELECT source_id, source_entity_id, ingest_date, company_name, company_inn, company_ogrn, v_date
    FROM `silver.stg_index_0500_vehicles`
    WHERE ingest_date = v_date AND company_name IS NOT NULL;
  END IF;

END;
