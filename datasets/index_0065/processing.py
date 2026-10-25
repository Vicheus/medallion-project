from pyspark import StorageLevel
from pyspark.sql.functions import (
    explode,
    when,
    col,
    lit,
    size,
    array,
    concat_ws,
    first,
    collect_list,
    flatten,
    coalesce,
    from_json,
    regexp_replace,
    transform,
    array_distinct,
    array_compact,
)
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DoubleType,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phones_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0065"
    telephone_schema = ArrayType(
        StructType(
            [
                StructField("TelephoneType", StringType(), True),
                StructField("TelephonePresentation", StringType(), True),
                StructField("Number", StringType(), True),
            ]
        )
    )

    def process_kasko_df(self, file_name):
        df = self.read(path=file_name, sep=";", header=True)
        df = (
            df.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_udf(col("full_name")),
                            name_udf(col("juridical_name")),
                            name_udf(col("juridical_full_name")),
                        )
                    )
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("birth_day"), lit("%d.%m.%Y")))
            .withColumn("sex", lit(None))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("fact_address")),
                            address_udf(col("juridical_address")),
                        )
                    )
                ),
            )
            .withColumn(
                "telephones",
                from_json(
                    regexp_replace(col("telephones"), '""', '"'), self.telephone_schema
                ),
            )
            .withColumn(
                "telephones",
                transform(col("telephones"), lambda x: x["TelephonePresentation"]),
            )
            .withColumn("phones", phones_udf(col("telephones")))
            .withColumn("emails", array())
            .withColumn(
                "documents",
                when(
                    col("passport_number").isNotNull()
                    | col("inn").isNotNull()
                    | col("juridical_inn").isNotNull()
                    | col("driver_license_number").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport_number").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("passport_number"),
                                    col("passport_date_of_issue"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                            when(
                                col("inn").isNotNull()
                                | col("juridical_inn").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    coalesce(col("inn"), col("juridical_inn")),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                            when(
                                col("driver_license_number").isNotNull(),
                                document_udf(
                                    lit("водительское удостоверение"),
                                    col("driver_license_number"),
                                    col("driver_license_date_of_issue"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(
                    (col("car_reg_number").isNotNull() & (col("car_reg_number") != ""))
                    | (col("car_vin").isNotNull() & (col("car_vin") != ""))
                    | col("car_model").isNotNull() & (col("car_model") != ""),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("car_model"),
                            col("car_year").cast("int"),
                            col("car_color"),
                            col("car_reg_number"),
                            col("car_vin"),
                            lit(None),
                        )
                    ),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "documents",
                "vehicles",
            )
        )

        return df

    def process_eosago_df(self, file_name):
        df = self.read(path=file_name, sep=";", header=True)
        df = (
            df.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_udf(col("full_name")),
                            name_udf(col("juridical_name")),
                            name_udf(col("juridical_full_name")),
                        )
                    )
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("birth_day"), lit("%d.%m.%Y")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("fact_address")),
                            address_udf(col("juridical_address")),
                        )
                    )
                ),
            )
            .withColumn(
                "telephones",
                from_json(
                    regexp_replace(col("telephones"), '""', '"'), self.telephone_schema
                ),
            )
            .withColumn(
                "telephones",
                transform(col("telephones"), lambda x: x["TelephonePresentation"]),
            )
            .withColumn("phones", phones_udf(col("telephones")))
            .withColumn("emails", array())
            .withColumn(
                "documents",
                when(
                    col("passport_number").isNotNull()
                    | col("juridical_inn").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport_number").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("passport_number"),
                                    col("passport_date_of_issue"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                            when(
                                col("juridical_inn").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("juridical_inn"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(
                    (col("car_reg_number").isNotNull() & (col("car_reg_number") != ""))
                    | (col("car_vin").isNotNull() & (col("car_vin") != ""))
                    | col("car_model").isNotNull() & (col("car_model") != ""),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("car_model"),
                            col("car_year").cast("int"),
                            col("car_color"),
                            col("car_reg_number"),
                            col("car_vin"),
                            lit(None),
                        )
                    ),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "documents",
                "vehicles",
            )
        )

        return df

    def process_drivers_df(self, file_name):
        driver_schema = ArrayType(
            StructType(
                [
                    StructField("Email", StringType(), True),
                    StructField("AgeDriver", StringType(), True),
                    StructField(
                        "Documents",
                        ArrayType(
                            StructType(
                                [
                                    StructField("Name", StringType(), True),
                                    StructField("Number", StringType(), True),
                                    StructField("Series", StringType(), True),
                                    StructField("Surname", StringType(), True),
                                    StructField("NumberOld", StringType(), True),
                                    StructField("SeriesOld", StringType(), True),
                                    StructField("MiddleName", StringType(), True),
                                    StructField("DateOfIssue", StringType(), True),
                                    StructField("DateBeginDrive", StringType(), True),
                                    StructField("DateOfIssueOld", StringType(), True),
                                    StructField("TypeOfDocument", StringType(), True),
                                    StructField("Issued", StringType(), True),
                                ]
                            )
                        ),
                        True,
                    ),
                    StructField(
                        "RequestKBM",
                        StructType(
                            [
                                StructField("ID", StringType(), True),
                                StructField("KBM_Value", DoubleType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField(
                        "Telephones",
                        ArrayType(
                            StructType(
                                [
                                    StructField("Number", StringType(), True),
                                    StructField("TelephoneType", StringType(), True),
                                    StructField(
                                        "TelephonePresentation", StringType(), True
                                    ),
                                ]
                            )
                        ),
                        True,
                    ),
                    StructField("ContractorType", StringType(), True),
                    StructField(
                        "PhisicalSection",
                        StructType(
                            [
                                StructField("INN", StringType(), True),
                                StructField("Sex", StringType(), True),
                                StructField("Name", StringType(), True),
                                StructField("Post", StringType(), True),
                                StructField("NameLat", StringType(), True),
                                StructField("Surname", StringType(), True),
                                StructField("Birthday", StringType(), True),
                                StructField(
                                    "Passport",
                                    StructType(
                                        [
                                            StructField("Number", StringType(), True),
                                            StructField("Series", StringType(), True),
                                            StructField("GivedOut", StringType(), True),
                                            StructField(
                                                "DateOfIssue", StringType(), True
                                            ),
                                            StructField(
                                                "DocumentType", StringType(), True
                                            ),
                                            StructField(
                                                "Asko_DivisionCode", StringType(), True
                                            ),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("WorkPlace", StringType(), True),
                                StructField("BirthPlace", StringType(), True),
                                StructField("MiddleName", StringType(), True),
                                StructField("SurnameLat", StringType(), True),
                                StructField("Nationality", StringType(), True),
                                StructField("Entrepreneur", BooleanType(), True),
                                StructField("Asko_Official", BooleanType(), True),
                                StructField(
                                    "DriverLicense",
                                    StructType(
                                        [
                                            StructField("Number", StringType(), True),
                                            StructField("Series", StringType(), True),
                                            StructField(
                                                "DateOfIssue", StringType(), True
                                            ),
                                            StructField(
                                                "DateBeginDrive", StringType(), True
                                            ),
                                            StructField(
                                                "TypeOfDocument", StringType(), True
                                            ),
                                        ]
                                    ),
                                    True,
                                ),
                                StructField("MiddleNameLat", StringType(), True),
                                StructField("Asko_INNFromFNS", StringType(), True),
                                StructField("Asko_NationalityCode", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("ExperienceDriver", StringType(), True),
                    StructField(
                        "JuridicalAddress",
                        StructType(
                            [
                                StructField("Area", StringType(), True),
                                StructField("City", StringType(), True),
                                StructField("OKATO", StringType(), True),
                                StructField("Region", StringType(), True),
                                StructField("Street", StringType(), True),
                                StructField("Country", StringType(), True),
                                StructField("ZipCode", StringType(), True),
                                StructField("CaseNumber", StringType(), True),
                                StructField("HomeNumber", StringType(), True),
                                StructField("Settlement", StringType(), True),
                                StructField("ApartmentNumber", StringType(), True),
                                StructField("AddressPresentation", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                ]
            )
        )

        df = self.read(path=file_name, sep=";", header=True)
        df = (
            df.withColumn(
                "car_drivers",
                from_json(regexp_replace(col("car_drivers"), '""', '"'), driver_schema),
            )
            .withColumn("driver", explode(transform(col("car_drivers"), lambda x: x)))
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_udf(
                                concat_ws(
                                    " ",
                                    col("driver.PhisicalSection.Surname"),
                                    col("driver.PhisicalSection.Name"),
                                    col("driver.PhisicalSection.MiddleName"),
                                )
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("driver.PhisicalSection.Birthday"), lit("%d.%m.%Y")),
            )
            .withColumn("sex", sex_udf(col("driver.PhisicalSection.Sex")))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                col("driver.JuridicalAddress.AddressPresentation")
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "telephones",
                transform(
                    col("driver.Telephones"), lambda x: x["TelephonePresentation"]
                ),
            )
            .withColumn("phones", phones_udf(col("telephones")))
            .withColumn("emails", array(email_udf(col("driver.Email"))))
            .withColumn(
                "documents",
                when(
                    col("driver.PhisicalSection.Passport.Number").isNotNull()
                    | col("driver.PhisicalSection.INN").isNotNull()
                    | col("driver.PhisicalSection.DriverLicense.Number").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col(
                                    "driver.PhisicalSection.Passport.Number"
                                ).isNotNull(),
                                document_udf(
                                    lit(None),
                                    concat_ws(
                                        " ",
                                        col("driver.PhisicalSection.Passport.Number"),
                                        col("driver.PhisicalSection.Passport.Number"),
                                    ),
                                    col("driver.PhisicalSection.Passport.DateOfIssue"),
                                    lit(None),
                                    col("driver.PhisicalSection.Passport.GivedOut"),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                            when(
                                col("driver.PhisicalSection.INN").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("driver.PhisicalSection.INN"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                            when(
                                col(
                                    "driver.PhisicalSection.Passport.Number"
                                ).isNotNull(),
                                document_udf(
                                    lit("водительское удостоверение"),
                                    concat_ws(
                                        " ",
                                        col("driver.PhisicalSection.Passport.Series"),
                                        col("driver.PhisicalSection.Passport.Number"),
                                    ),
                                    col("driver.PhisicalSection.Passport.DateOfIssue"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(
                    (col("car_reg_number").isNotNull() & (col("car_reg_number") != ""))
                    | (col("car_vin").isNotNull() & (col("car_vin") != ""))
                    | col("car_model").isNotNull() & (col("car_model") != ""),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("car_model"),
                            col("car_year").cast("int"),
                            col("car_color"),
                            col("car_reg_number"),
                            col("car_vin"),
                            lit(None),
                        )
                    ),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "documents",
                "vehicles",
            )
        )

        return df

    def process_avtocod_df(self, file_name):
        df = self.read(path=file_name, sep=";", header=True)
        df = (
            df.withColumn(
                "names", array_compact(array_distinct(array(name_udf(col("name")))))
            )
            .withColumn("birth_date", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("address", array())
            .withColumn("phones", array())
            .withColumn("emails", array())
            .withColumn("documents", array())
            .withColumn(
                "vehicles",
                when(
                    (
                        col("vehicle_reg_number").isNotNull()
                        & (col("vehicle_reg_number") != "")
                    )
                    | (col("vehicle_vin").isNotNull() & (col("vehicle_vin") != ""))
                    | col("vehicle_brand").isNotNull() & (col("vehicle_brand") != ""),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("vehicle_brand"),
                            col("vehicle_year").cast("int"),
                            col("vehicle_color"),
                            col("vehicle_reg_number"),
                            col("vehicle_vin"),
                            lit(None),
                        )
                    ),
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "phones",
                "emails",
                "documents",
                "vehicles",
            )
        )

        return df

    def parser(self):
        df_eosago_insurers = self.process_eosago_df(
            "acko/acko_eosago_insurers_preprocessed.csv"
        )
        df_eosago_owners = self.process_eosago_df(
            "acko/acko_eosago_owners_preprocessed.csv"
        )
        df_eosago = df_eosago_insurers.unionAll(df_eosago_owners)

        df_kasko_insurers = self.process_kasko_df(
            "acko/acko_kasko_insurers_preprocessed.csv"
        )
        df_kasko_owners = self.process_kasko_df(
            "acko/acko_kasko_owners_preprocessed.csv"
        )
        df_kasko = df_kasko_insurers.unionAll(df_kasko_owners)

        df_kasko_drivers = self.process_drivers_df(
            "acko/acko_kasko_drivers_preprocessed.csv"
        )
        df_eosago_drivers = self.process_drivers_df(
            "acko/acko_osago_drivers_preprocessed.csv"
        )
        df_drivers = df_kasko_drivers.unionAll(df_eosago_drivers)

        df_avtocod = self.process_avtocod_df("acko/acko_avtocod_preprocessed.csv")

        df = df_eosago.unionAll(df_kasko).unionAll(df_drivers).unionAll(df_avtocod)

        print(f"df size: {df.count()}")
        print(f"df with unique name: {df.select(col("names")).distinct().count()}")

        df = (
            df.filter(col("names").isNotNull())
            .groupby(col("names"))
            .agg(
                array_compact(array_distinct(flatten(collect_list("phones")))).alias(
                    "phones"
                ),
                array_compact(array_distinct(flatten(collect_list("emails")))).alias(
                    "emails"
                ),
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_list("vehicles")))).alias(
                    "vehicles"
                ),
                array_compact(array_distinct(flatten(collect_list("documents")))).alias(
                    "documents"
                ),
                first(coalesce("sex")).alias("sex"),
                first(coalesce("birth_date")).alias("birth_date"),
            )
        )

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )

        df = df.select(
            "names",
            "birth_date",
            "sex",
            "address",
            "phones",
            "emails",
            "documents",
            "vehicles",
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
                | col("vehicles").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
