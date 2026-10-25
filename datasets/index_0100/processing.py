from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    slice,
    array,
    first,
    size,
    collect_set,
    regexp_extract,
    array_compact,
    array_distinct,
    flatten,
    collect_list,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.incidences.udfs import incidence_udf, incidence_date_udf
from parsetron.sections.main.udfs import name_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0100"
    output_file_count: int = 200

    def prepare_incidences_df(self):
        df_legal_persons_incidences_details = self.read(
            path="/media/user/SAMSUNG/Databases/index_0100/raw/preprocessed/legal_incidences_details_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_natural_persons_incidences_details = self.read(
            path="/media/user/SAMSUNG/Databases/index_0100/raw/preprocessed/natural_incidences_details_preprocessed.csv",
            sep=";",
            header=True,
        )

        df_incidences = (
            df_legal_persons_incidences_details.unionAll(
                df_natural_persons_incidences_details
            )
            .groupBy(col("IdInsuredAccident"))
            .agg(
                first(col("DateOfAccident")).alias("DateOfAccident"),
                first(col("InsuranceCompany")).alias("InsuranceCompany"),
                collect_set("Participant").alias("Participants"),
            )
        )

        df_incidences.persist(StorageLevel.DISK_ONLY).count()

        return df_incidences

    def prepare_legal_persons_incidences(self):
        df_incidences = self.prepare_incidences_df()
        df_legal_incidences = self.read(
            path="/media/user/SAMSUNG/Databases/index_0100/raw/preprocessed/legal_incidences_preprocessed.csv",
            sep=";",
            header=True,
        )

        df = (
            df_legal_incidences.join(df_incidences, "IdInsuredAccident", "inner")
            .groupBy("IdLP")
            .agg(
                collect_set(
                    incidence_udf(
                        lit("ДТП"),
                        incidence_date_udf(
                            col("DateOfAccident"), lit("%Y-%m-%d %H:%M:%S.%f")
                        ),
                        col("InsuranceCompany"),
                        col("Participants"),
                        lit(""),
                    )
                ).alias("incidences")
            )
            .select("IdLP", "incidences")
        )

        return df

    def prepare_natural_persons_incidences(self):
        df_incidences = self.prepare_incidences_df()
        df_legal_incidences = self.read(
            path="/media/user/SAMSUNG/Databases/index_0100/raw/preprocessed/natural_incidences_preprocessed.csv",
            sep=";",
            header=True,
        )

        df = (
            df_legal_incidences.join(df_incidences, "IdInsuredAccident", "inner")
            .groupBy("IdNP")
            .agg(
                collect_set(
                    incidence_udf(
                        lit("ДТП"),
                        incidence_date_udf(
                            col("DateOfAccident"), lit("%Y-%m-%d %H:%M:%S.%f")
                        ),
                        col("InsuranceCompany"),
                        col("Participants"),
                        lit(""),
                    )
                ).alias("incidences")
            )
            .select("IdNP", "incidences")
        )

        return df

    def parser(self):
        df_legal_persons = self.read(
            path="/media/user/SAMSUNG/Databases/index_0100/raw/preprocessed/legal_persons_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_legal_persons = (
            df_legal_persons.withColumn("names", name_udf(col("OrganisationName")))
            .withColumn("birth_date", lit(None))
            .withColumn(
                "documents",
                when(
                    col("INN").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("INN").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("INN"),
                                    lit(None),
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
        )
        df_legal_persons_vehicles = self.read(
            path="/media/user/SAMSUNG/Databases/index_0100/raw/preprocessed/legal_persons_vehicles_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_legal_persons_vehicles = df_legal_persons_vehicles.withColumn(
            "vehicles",
            when(
                col("RegistrationNumber").isNotNull()
                | col("VIN").isNotNull()
                | col("Mark").isNotNull(),
                vehicle_udf(
                    lit(1),
                    col("Mark"),
                    col("YearOfCreation").cast("int"),
                    lit(None),
                    col("RegistrationNumber"),
                    col("VIN"),
                    lit(None),
                ),
            ),
        )
        df_legal_persons_vehicles = df_legal_persons_vehicles.groupby("IdLP").agg(
            when(size(collect_set("vehicles")) > 0, collect_set("vehicles"))
            .otherwise(None)
            .alias("vehicles")
        )
        df_legal_persons_vehicles.persist(StorageLevel.DISK_ONLY).count()

        df_legal_persons_incidences = self.prepare_legal_persons_incidences()

        df_legal = (
            df_legal_persons.join(df_legal_persons_vehicles, "IdLP", "inner")
            .join(df_legal_persons_incidences, "IdLP", "inner")
            .select("names", "birth_date", "vehicles", "documents", "incidences")
        )

        passport_doctype_regex = r"(Паспорт гражданина РФ)"
        passport_serial_regex = r"(\d{2} \d{2} №\d+)"
        passport_issue_date_regex = r"(\d{2}\.\d{2}\.\d{4})"
        passport_issuer_regex = r"выдан (.*)"

        driver_license_doctype_regex = r"(Водительское удостоверение РФ)"
        driver_license_serial_regex = r"(\d{4} №\d+)"

        df_natural_persons = self.read(
            path="/media/user/SAMSUNG/Databases/index_0100/raw/preprocessed/natural_persons_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_natural_persons = (
            df_natural_persons.withColumn("names", name_udf(col("FullName")))
            .withColumn(
                "passport_doctype",
                regexp_extract("CommentNP", passport_doctype_regex, 1),
            )
            .withColumn(
                "passport_serial", regexp_extract("CommentNP", passport_serial_regex, 1)
            )
            .withColumn(
                "passport_issue_date",
                regexp_extract("CommentNP", passport_issue_date_regex, 1),
            )
            .withColumn(
                "passport_issuer", regexp_extract("CommentNP", passport_issuer_regex, 1)
            )
            .withColumn(
                "driver_license_doctype",
                regexp_extract("CommentNP", driver_license_doctype_regex, 1),
            )
            .withColumn(
                "driver_license_serial",
                regexp_extract("CommentNP", driver_license_serial_regex, 1),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("DateOfBirth"), lit("%Y-%m-%d %H:%M:%S.%f")),
            )
            .withColumn(
                "documents",
                when(
                    col("passport_doctype").isNotNull()
                    | col("driver_license_doctype").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport_doctype").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport_serial"),
                                    col("passport_issue_date"),
                                    lit(None),
                                    col("passport_issuer"),
                                    lit(None),
                                    lit("%d.%m.%Y"),
                                ),
                            ).otherwise(None),
                            when(
                                col("driver_license_doctype").isNotNull(),
                                document_udf(
                                    lit("водительское удостоверение"),
                                    col("driver_license_serial"),
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
            .select("IdNP", "names", "birth_date", "documents")
        )

        df_natural_persons = df_natural_persons.groupby("IdNP").agg(
            first("names").alias("names"),
            first("birth_date").alias("birth_date"),
            array_distinct(flatten(collect_list("documents"))).alias("documents"),
        )

        df_natural_persons_vehicles = self.read(
            path="/media/user/SAMSUNG/Databases/index_0100/raw/preprocessed/natural_persons_vehicles_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_natural_persons_vehicles = df_natural_persons_vehicles.withColumn(
            "vehicles",
            when(
                col("RegistrationNumber").isNotNull()
                | col("VIN").isNotNull()
                | col("Mark").isNotNull(),
                vehicle_udf(
                    lit(1),
                    col("Mark"),
                    col("YearOfCreation").cast("int"),
                    lit(None),
                    col("RegistrationNumber"),
                    col("VIN"),
                    lit(None),
                ),
            ),
        )
        df_natural_persons_vehicles = df_natural_persons_vehicles.groupby("IdNP").agg(
            when(size(collect_set("vehicles")) > 0, collect_set("vehicles"))
            .otherwise(None)
            .alias("vehicles")
        )
        df_natural_persons_vehicles.persist(StorageLevel.DISK_ONLY).count()

        df_natural_persons_incidences = self.prepare_natural_persons_incidences()
        df_natural = (
            df_natural_persons.join(df_natural_persons_vehicles, "IdNP", "inner")
            .join(df_natural_persons_incidences, "IdNP", "inner")
            .select("names", "birth_date", "vehicles", "documents", "incidences")
        )

        df = df_legal.unionAll(df_natural)

        df = df.filter(
            col("names").isNotNull()
            & ((col("documents").isNotNull()) | (col("vehicles").isNotNull()))
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
            )
            .withColumn(
                "incidences",
                when(
                    size(col("incidences")) > 50, slice("incidences", 1, 50)
                ).otherwise(col("incidences")),
            )
            .withColumn(
                "vehicles",
                when(size(col("vehicles")) > 50, slice("vehicles", 1, 50)).otherwise(
                    col("vehicles")
                ),
            )
        )

        df = df.repartition(self.output_file_count)
        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
