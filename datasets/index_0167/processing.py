from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    flatten,
    array_compact,
    collect_list,
    first,
    collect_set,
    explode,
    concat,
    size,
    concat_ws,
    coalesce,
    expr,
    split,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.main.udfs import (
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    name_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0167"

    def parser(self):
        df_1 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0167/raw/eosago_1_output.csv",
            sep=";",
            header=True,
        )
        df_2 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0167/raw/eosago_2_output_ids_decoded.csv/*.csv",
            sep=";",
            header=True,
        )
        df = df_1.join(df_2, "id", "left")

        def prepare_drivers_df_for_joins(df):
            df_drivers = df.withColumn("drivers", explode("parsed_drivers_json"))

            df_drivers = df_drivers.select(
                concat_ws(
                    " ",
                    col("drivers.last_name"),
                    col("drivers.first_name"),
                    col("drivers.middle_name"),
                ).alias("driver_full_name"),
                col("drivers.birthday").alias("driver_birthday"),
                col("drivers.address").alias("driver_address"),
                col("drivers.license_number").alias("driver_license_number"),
                col("drivers.license_date").alias("driver_license_date"),
                col("drivers.license_series").alias("driver_license_series"),
                col("drivers.sex").alias("driver_sex"),
                col("car").alias("car"),
                col("license_plate").alias("license_plate"),
                col("vin").alias("vin"),
                col("vehicle_year_issue").alias("vehicle_year_issue"),
                col("id").alias("record_id"),
            )

            return df_drivers

        def prepare_owners_insurers_df(df, df_drivers):
            df_owners_insurers = (
                df.filter(
                    (col("owner_fullname") == col("insurer_fullname"))
                    & (col("owner_pasNumber") == col("insurer_pasNumber"))
                    & (col("owner_pasSerial") == col("insurer_pasSerial"))
                )
                .join(
                    df_drivers,
                    (df_drivers["driver_full_name"] == df["owner_fullname"])
                    & (df_drivers["driver_birthday"] == df["owner_birthday"]),
                    "left",
                )
                .withColumn("names", name_udf(col("owner_fullname")))
                .withColumn("sex", sex_udf(col("owner_sex")))
                .withColumn(
                    "birth_date", birth_date_udf(col("owner_birthday"), lit("%d.%m.%Y"))
                )
                .withColumn("phones", phone_udf(col("insurer_phone")))
                .withColumn("emails", email_udf(col("insurer_email")))
                .withColumn(
                    "address",
                    array_compact(
                        array_distinct(
                            array(
                                address_udf(col("owner_address")),
                                address_udf(col("driver_address")),
                            )
                        )
                    ),
                )
                .withColumn(
                    "documents",
                    when(
                        (
                            col("owner_pasSerial").isNotNull()
                            & col("owner_pasNumber").isNotNull()
                        )
                        | (
                            col("driver_license_series").isNotNull()
                            & col("driver_license_number").isNotNull()
                        ),
                        array_compact(
                            array(
                                when(
                                    (
                                        col("owner_pasSerial").isNotNull()
                                        | col("owner_pasNumber").isNotNull()
                                    ),
                                    document_udf(
                                        lit(None),
                                        concat(
                                            col("owner_pasSerial"),
                                            col("owner_pasNumber"),
                                        ),
                                        col("owner_pasDate"),
                                        lit(None),
                                        col("owner_pasIssued"),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ).otherwise(None),
                                when(
                                    (
                                        col("driver_license_series").isNotNull()
                                        | col("driver_license_number").isNotNull()
                                    ),
                                    document_udf(
                                        lit("водительское удостоверение"),
                                        concat(
                                            col("driver_license_series"),
                                            col("driver_license_number"),
                                        ),
                                        col("driver_license_date"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ).otherwise(None),
                            )
                        ),
                    ).otherwise(None),
                )
                .withColumn(
                    "vehicles",
                    when(
                        df["license_plate"].isNotNull()
                        | df["vin"].isNotNull()
                        | df["car"].isNotNull(),
                        array_compact(
                            array_distinct(
                                array(
                                    vehicle_udf(
                                        lit(1),
                                        df["car"],
                                        df["vehicle_year_issue"].cast("int"),
                                        lit(None),
                                        df["license_plate"],
                                        df["vin"],
                                        lit(None),
                                    )
                                )
                            )
                        ),
                    ),
                )
                .select(
                    "id",
                    "names",
                    "sex",
                    "birth_date",
                    "phones",
                    "emails",
                    "address",
                    "documents",
                    "vehicles",
                    "owner_fullname",
                    "owner_birthday",
                )
                .drop_duplicates()
            )

            df_drivers_for_owners_insurers_relations = (
                df_drivers.join(
                    df_owners_insurers,
                    (df_drivers["record_id"] == df_owners_insurers["id"])
                    & (
                        df_drivers["driver_full_name"]
                        != df_owners_insurers["owner_fullname"]
                    )
                    & (
                        df_drivers["driver_birthday"]
                        != df_owners_insurers["owner_birthday"]
                    ),
                    how="inner",
                )
                .groupBy("record_id")
                .agg(
                    collect_list(
                        concat_ws(
                            " ",
                            name_udf("driver_full_name"),
                            birth_date_udf("driver_birthday", lit("%d.%m.%Y")),
                            lit("Водительское удостоверение:"),
                            concat("driver_license_series", "driver_license_number"),
                            "driver_license_date",
                            lit("водитель того же автомобиля"),
                        )
                    ).alias("other_drivers")
                )
                .select("record_id", "other_drivers")
            )

            df_owners_insurers = (
                df_owners_insurers.join(
                    df_drivers_for_owners_insurers_relations,
                    df_owners_insurers["id"]
                    == df_drivers_for_owners_insurers_relations["record_id"],
                    "left",
                )
                .withColumn("relations", col("other_drivers"))
                .select(
                    "names",
                    "sex",
                    "birth_date",
                    "phones",
                    "emails",
                    "address",
                    "documents",
                    "vehicles",
                    "relations",
                )
            )
            return df_owners_insurers

        def prepare_owners_not_insurers_df(df, df_drivers):
            df_owners_not_insurers = (
                df.filter(
                    (col("owner_fullname") != col("insurer_fullname"))
                    & (col("owner_pasNumber") != col("insurer_pasNumber"))
                    & (col("owner_pasSerial") != col("insurer_pasSerial"))
                )
                .join(
                    df_drivers,
                    (df_drivers["driver_full_name"] == df["owner_fullname"])
                    & (df_drivers["driver_birthday"] == df["owner_birthday"]),
                    "left",
                )
                .withColumn("names", name_udf(col("owner_fullname")))
                .withColumn("sex", sex_udf(col("owner_sex")))
                .withColumn(
                    "birth_date", birth_date_udf(col("owner_birthday"), lit("%d.%m.%Y"))
                )
                .withColumn("phones", lit(None))
                .withColumn("emails", lit(None))
                .withColumn(
                    "address",
                    array_compact(
                        array_distinct(
                            array(
                                address_udf(col("owner_address")),
                                address_udf(col("driver_address")),
                            )
                        )
                    ),
                )
                .withColumn(
                    "documents",
                    when(
                        (
                            col("owner_pasSerial").isNotNull()
                            & col("owner_pasNumber").isNotNull()
                        )
                        | (
                            col("driver_license_series").isNotNull()
                            & col("driver_license_number").isNotNull()
                        ),
                        array_compact(
                            array(
                                when(
                                    (
                                        col("owner_pasSerial").isNotNull()
                                        | col("owner_pasNumber").isNotNull()
                                    ),
                                    document_udf(
                                        lit(None),
                                        concat(
                                            col("owner_pasSerial"),
                                            col("owner_pasNumber"),
                                        ),
                                        col("owner_pasDate"),
                                        lit(None),
                                        col("owner_pasIssued"),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ).otherwise(None),
                                when(
                                    (
                                        col("driver_license_series").isNotNull()
                                        | col("driver_license_number").isNotNull()
                                    ),
                                    document_udf(
                                        lit("водительское удостоверение"),
                                        concat(
                                            col("driver_license_series"),
                                            col("driver_license_number"),
                                        ),
                                        col("driver_license_date"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ).otherwise(None),
                            )
                        ),
                    ).otherwise(None),
                )
                .withColumn(
                    "vehicles",
                    when(
                        df["license_plate"].isNotNull()
                        | df["vin"].isNotNull()
                        | df["car"].isNotNull(),
                        array_compact(
                            array_distinct(
                                array(
                                    vehicle_udf(
                                        lit(1),
                                        df["car"],
                                        df["vehicle_year_issue"].cast("int"),
                                        lit(None),
                                        df["license_plate"],
                                        df["vin"],
                                        lit(None),
                                    )
                                )
                            )
                        ),
                    ),
                )
                .withColumn(
                    "relations",
                    array_compact(
                        array_distinct(
                            array(
                                concat_ws(
                                    " ",
                                    name_udf(col("insurer_fullname")),
                                    birth_date_udf(
                                        col("insurer_birthday"), lit("%d.%m.%Y")
                                    ),
                                    lit("Паспорт:"),
                                    concat(
                                        col("insurer_pasSerial"),
                                        col("insurer_pasNumber"),
                                    ),
                                    phone_udf(col("insurer_phone")),
                                    email_udf(col("insurer_email")),
                                    lit("Страхователь"),
                                )
                            )
                        )
                    ),
                )
                .select(
                    "id",
                    "names",
                    "sex",
                    "birth_date",
                    "phones",
                    "emails",
                    "address",
                    "documents",
                    "vehicles",
                    "relations",
                    "owner_fullname",
                    "owner_birthday",
                )
                .drop_duplicates()
            )

            df_drivers_for_owners_not_insurers_relations = (
                df_drivers.join(
                    df_owners_not_insurers,
                    (df_drivers["record_id"] == df_owners_not_insurers["id"])
                    & (
                        df_drivers["driver_full_name"]
                        != df_owners_not_insurers["owner_fullname"]
                    )
                    & (
                        df_drivers["driver_birthday"]
                        != df_owners_not_insurers["owner_birthday"]
                    ),
                    how="inner",
                )
                .groupBy("record_id")
                .agg(
                    collect_list(
                        concat_ws(
                            " ",
                            name_udf("driver_full_name"),
                            birth_date_udf("driver_birthday", lit("%d.%m.%Y")),
                            lit("Водительское удостоверение:"),
                            concat("driver_license_series", "driver_license_number"),
                            "driver_license_date",
                            lit("водитель того же автомобиля"),
                        )
                    ).alias("other_drivers")
                )
                .select("record_id", "other_drivers")
            )

            df_owners_not_insurers = (
                df_owners_not_insurers.join(
                    df_drivers_for_owners_not_insurers_relations,
                    df_owners_not_insurers["id"]
                    == df_drivers_for_owners_not_insurers_relations["record_id"],
                    "left",
                )
                .withColumn("relations", concat(col("relations"), col("other_drivers")))
                .select(
                    "names",
                    "sex",
                    "birth_date",
                    "phones",
                    "emails",
                    "address",
                    "documents",
                    "vehicles",
                    "relations",
                )
            )
            return df_owners_not_insurers

        def prepare_insurers_not_owners_df(df, df_drivers):
            df_insurers_not_owners = (
                df.filter(
                    (col("owner_fullname") != col("insurer_fullname"))
                    & (col("owner_pasNumber") != col("insurer_pasNumber"))
                    & (col("owner_pasSerial") != col("insurer_pasSerial"))
                )
                .join(
                    df_drivers,
                    (df_drivers["driver_full_name"] == df["insurer_fullname"])
                    & (df_drivers["driver_birthday"] == df["insurer_birthday"]),
                    "left",
                )
                .withColumn("names", name_udf(col("insurer_fullname")))
                .withColumn("sex", sex_udf(col("insurer_sex")))
                .withColumn(
                    "birth_date",
                    birth_date_udf(col("insurer_birthday"), lit("%d.%m.%Y")),
                )
                .withColumn("phones", phone_udf(col("insurer_phone")))
                .withColumn("emails", email_udf(col("insurer_email")))
                .withColumn(
                    "address",
                    array_compact(
                        array_distinct(
                            array(
                                address_udf(col("insurer_address")),
                                address_udf(col("driver_address")),
                            )
                        )
                    ),
                )
                .withColumn(
                    "documents",
                    when(
                        (
                            col("insurer_pasSerial").isNotNull()
                            & col("insurer_pasNumber").isNotNull()
                        )
                        | (
                            col("driver_license_series").isNotNull()
                            & col("driver_license_number").isNotNull()
                        ),
                        array_compact(
                            array(
                                when(
                                    (
                                        col("insurer_pasSerial").isNotNull()
                                        | col("insurer_pasNumber").isNotNull()
                                    ),
                                    document_udf(
                                        lit(None),
                                        concat(
                                            col("insurer_pasSerial"),
                                            col("insurer_pasNumber"),
                                        ),
                                        col("insurer_pasDate"),
                                        lit(None),
                                        col("insurer_pasIssued"),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ).otherwise(None),
                                when(
                                    (
                                        col("driver_license_series").isNotNull()
                                        | col("driver_license_number").isNotNull()
                                    ),
                                    document_udf(
                                        lit("водительское удостоверение"),
                                        concat(
                                            col("driver_license_series"),
                                            col("driver_license_number"),
                                        ),
                                        col("driver_license_date"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ).otherwise(None),
                            )
                        ),
                    ).otherwise(None),
                )
                .withColumn(
                    "vehicles",
                    when(
                        df["license_plate"].isNotNull()
                        | df["vin"].isNotNull()
                        | df["car"].isNotNull(),
                        array_compact(
                            array_distinct(
                                array(
                                    vehicle_udf(
                                        lit(1),
                                        df["car"],
                                        df["vehicle_year_issue"].cast("int"),
                                        lit(None),
                                        df["license_plate"],
                                        df["vin"],
                                        lit(None),
                                    )
                                )
                            )
                        ),
                    ),
                )
                .withColumn(
                    "relations",
                    array_compact(
                        array_distinct(
                            array(
                                concat_ws(
                                    " ",
                                    name_udf(col("owner_fullname")),
                                    birth_date_udf(
                                        col("owner_birthday"), lit("%d.%m.%Y")
                                    ),
                                    lit("Паспорт:"),
                                    concat(
                                        col("owner_pasSerial"), col("owner_pasNumber")
                                    ),
                                    lit("Владелец"),
                                )
                            )
                        )
                    ),
                )
                .select(
                    "id",
                    "names",
                    "sex",
                    "birth_date",
                    "phones",
                    "emails",
                    "address",
                    "documents",
                    "vehicles",
                    "relations",
                    "insurer_fullname",
                    "insurer_birthday",
                )
                .drop_duplicates()
            )

            df_drivers_for_insurers_not_owners_relations = (
                df_drivers.join(
                    df_insurers_not_owners,
                    (df_drivers["record_id"] == df_insurers_not_owners["id"])
                    & (
                        df_drivers["driver_full_name"]
                        != df_insurers_not_owners["insurer_fullname"]
                    )
                    & (
                        df_drivers["driver_birthday"]
                        != df_insurers_not_owners["insurer_birthday"]
                    ),
                    how="inner",
                )
                .groupBy("record_id")
                .agg(
                    collect_list(
                        concat_ws(
                            " ",
                            name_udf("driver_full_name"),
                            birth_date_udf("driver_birthday", lit("%d.%m.%Y")),
                            lit("Водительское удостоверение:"),
                            concat("driver_license_series", "driver_license_number"),
                            "driver_license_date",
                            lit("водитель того же автомобиля"),
                        )
                    ).alias("other_drivers")
                )
                .select("record_id", "other_drivers")
            )

            df_insurers_not_owners = (
                df_insurers_not_owners.join(
                    df_drivers_for_insurers_not_owners_relations,
                    df_insurers_not_owners["id"]
                    == df_drivers_for_insurers_not_owners_relations["record_id"],
                    "left",
                )
                .withColumn("relations", concat(col("relations"), col("other_drivers")))
                .select(
                    "names",
                    "sex",
                    "birth_date",
                    "phones",
                    "emails",
                    "address",
                    "documents",
                    "vehicles",
                    "relations",
                )
            )
            return df_insurers_not_owners

        def prepare_drivers_not_insurers_not_owners_df(df):
            df_drivers_not_insurers_not_owners = df.withColumn(
                "drivers", explode("parsed_drivers_json")
            )

            df_drivers_not_insurers_not_owners = (
                df_drivers_not_insurers_not_owners.select(
                    concat_ws(
                        " ",
                        col("drivers.last_name"),
                        col("drivers.first_name"),
                        col("drivers.middle_name"),
                    ).alias("driver_full_name"),
                    col("drivers.birthday").alias("driver_birthday"),
                    col("drivers.address").alias("driver_address"),
                    col("drivers.license_number").alias("driver_license_number"),
                    col("drivers.license_date").alias("driver_license_date"),
                    col("drivers.license_series").alias("driver_license_series"),
                    col("drivers.sex").alias("driver_sex"),
                    col("car").alias("car"),
                    col("license_plate").alias("license_plate"),
                    col("vin").alias("vin"),
                    col("vehicle_year_issue").alias("vehicle_year_issue"),
                    col("owner_fullname").alias("owner_full_name"),
                    col("owner_birthday").alias("owner_birthday"),
                    col("owner_pasSerial").alias("owner_pasSerial"),
                    col("owner_pasNumber").alias("owner_pasNumber"),
                    col("insurer_fullname").alias("insurer_full_name"),
                    col("insurer_birthday").alias("insurer_birthday"),
                    col("insurer_pasSerial").alias("insurer_pasSerial"),
                    col("insurer_pasNumber").alias("insurer_pasNumber"),
                    col("insurer_phone").alias("insurer_phone"),
                    col("insurer_email").alias("insurer_email"),
                )
            )

            df_drivers_not_insurers_not_owners = (
                df_drivers_not_insurers_not_owners.filter(
                    (col("driver_full_name") != col("owner_full_name"))
                    & (col("driver_full_name") != col("insurer_full_name"))
                )
                .withColumn("names", name_udf(col("driver_full_name")))
                .withColumn("sex", sex_udf(col("driver_sex")))
                .withColumn(
                    "birth_date",
                    birth_date_udf(col("driver_birthday"), lit("%d.%m.%Y")),
                )
                .withColumn("phones", lit(None))
                .withColumn("emails", lit(None))
                .withColumn(
                    "address",
                    array_compact(
                        array_distinct(array(address_udf(col("driver_address"))))
                    ),
                )
                .withColumn(
                    "documents",
                    when(
                        (
                            col("driver_license_series").isNotNull()
                            & col("driver_license_number").isNotNull()
                        ),
                        array_compact(
                            array(
                                when(
                                    (
                                        col("driver_license_series").isNotNull()
                                        | col("driver_license_number").isNotNull()
                                    ),
                                    document_udf(
                                        lit("водительское удостоверение"),
                                        concat(
                                            col("driver_license_series"),
                                            col("driver_license_number"),
                                        ),
                                        col("driver_license_date"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ).otherwise(None)
                            )
                        ),
                    ).otherwise(None),
                )
                .withColumn(
                    "vehicles",
                    when(
                        col("license_plate").isNotNull()
                        | col("vin").isNotNull()
                        | col("car").isNotNull(),
                        array_compact(
                            array_distinct(
                                array(
                                    vehicle_udf(
                                        lit(1),
                                        col("car"),
                                        col("vehicle_year_issue").cast("int"),
                                        lit(None),
                                        col("license_plate"),
                                        col("vin"),
                                        lit(None),
                                    )
                                )
                            )
                        ),
                    ),
                )
                .withColumn(
                    "relations",
                    array_compact(
                        array_distinct(
                            array(
                                concat_ws(
                                    " ",
                                    name_udf(col("owner_full_name")),
                                    birth_date_udf(
                                        col("owner_birthday"), lit("%d.%m.%Y")
                                    ),
                                    lit("Паспорт:"),
                                    concat(
                                        col("owner_pasSerial"), col("owner_pasNumber")
                                    ),
                                    lit("Владелец"),
                                ),
                                concat_ws(
                                    " ",
                                    name_udf(col("insurer_full_name")),
                                    birth_date_udf(
                                        col("insurer_birthday"), lit("%d.%m.%Y")
                                    ),
                                    lit("Паспорт:"),
                                    concat(
                                        col("insurer_pasSerial"),
                                        col("insurer_pasNumber"),
                                    ),
                                    phone_udf(col("insurer_phone")),
                                    email_udf(col("insurer_email")),
                                    lit("Страхователь"),
                                ),
                            )
                        )
                    ),
                )
                .select(
                    "names",
                    "sex",
                    "birth_date",
                    "phones",
                    "emails",
                    "address",
                    "documents",
                    "vehicles",
                    "relations",
                )
                .drop_duplicates()
            )

            return df_drivers_not_insurers_not_owners

        df = (
            df.withColumn(
                "cleaned_drivers_json", regexp_replace(col("drivers"), r"\\", "")
            )
            .withColumn(
                "cleaned_drivers_json",
                regexp_replace(col("cleaned_drivers_json"), r"\"\"", '"'),
            )
            .withColumn("split_drivers_json", split(col("cleaned_drivers_json"), "~"))
            .withColumn(
                "parsed_drivers_json",
                expr(
                    "transform(split_drivers_json, x -> from_json(x, 'struct<first_name:string, last_name:string, middle_name:string, birthday:string, address:string, license_number:string, issue_date:string, license_date:string, license_series:string, sex:string>'))"
                ),
            )
            .withColumn(
                "owner_fullname",
                concat_ws(
                    " ",
                    col("owner_lastName"),
                    col("owner_firstName"),
                    col("owner_middleName"),
                ),
            )
            .withColumn(
                "insurer_fullname",
                concat_ws(
                    " ",
                    col("insurer_lastName"),
                    col("insurer_firstName"),
                    col("insurer_middleName"),
                ),
            )
            .withColumn("vin", coalesce(col("vin"), col("vehicle_vin")))
        )

        df_drivers = prepare_drivers_df_for_joins(df)

        df_owners_insurers = prepare_owners_insurers_df(df, df_drivers)
        df_owners_not_insurers = prepare_owners_not_insurers_df(df, df_drivers)
        df_insurers_not_owners = prepare_insurers_not_owners_df(df, df_drivers)
        df_drivers_not_insurers_not_owners = prepare_drivers_not_insurers_not_owners_df(
            df
        )

        df = (
            df_drivers_not_insurers_not_owners.unionAll(df_insurers_not_owners)
            .unionAll(df_owners_insurers)
            .unionAll(df_owners_not_insurers)
            .drop_duplicates()
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.groupby(["names", "birth_date"])
            .agg(
                array_compact(collect_set(col("phones"))).alias("phones"),
                array_compact(collect_set(col("emails"))).alias("emails"),
                flatten(array_compact(collect_set(col("address")))).alias("address"),
                flatten(array_compact(collect_set(col("documents")))).alias(
                    "documents"
                ),
                flatten(array_compact(collect_set(col("vehicles")))).alias("vehicles"),
                flatten(array_compact(collect_set(col("relations")))).alias(
                    "relations"
                ),
                first(col("sex")).alias("sex"),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "phones",
                "emails",
                "address",
                "documents",
                "vehicles",
                "relations",
            )
        )
        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(
                    size(array_compact(col("vehicles"))) > 0,
                    array_compact(col("vehicles")),
                ).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    size(array_compact(col("relations"))) > 0,
                    array_compact(col("relations")),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("documents").isNotNull()
                | col("emails").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
