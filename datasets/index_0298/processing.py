from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array_compact,
    array_distinct,
    flatten,
    size,
    array,
    collect_set,
    concat,
    first,
)
from pyspark.sql.types import StructType, StringType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = True
    dataset_code_name: str = "index_0298"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = False

    def parser(self):
        df_persons_1 = (
            self.read(
                path="/media/user/T7 Shield/gosuslugi_2025/ГосУслуги/gos_uslugi_2023/Persons_with_livingplace.csv",
                sep=";",
                header=True,
            )
            .replace("null", None)
            .withColumn("names", array_compact(array(name_udf("FullName"))))
            .withColumn(
                "address", array_compact(array(address_udf(col("FullAddress"))))
            )
            .withColumn("emails", array_compact(array(email_udf(col("Email")))))
            .withColumn("phones", array_compact(array(phone_udf(col("Phone_Number")))))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("Serial").isNotNull() & col("Number").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    concat(col("Serial"), col("Number")),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("Snils").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("Snils"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("snils", col("Snils"))
            .filter(
                col("names").isNotNull()
                & (
                    col("phones").isNotNull()
                    | col("emails").isNotNull()
                    | col("documents").isNotNull()
                )
            )
            .select(
                "names",
                "birth_date",
                "address",
                "emails",
                "phones",
                "documents",
                "snils",
            )
        )

        df_persons_1.persist(StorageLevel.DISK_ONLY).count()

        df_address = (
            self.read(
                path="/media/user/T7 Shield/gosuslugi_2025/ГосУслуги/gos_uslugi_2023/Address.csv",
                sep=";",
                header=True,
            )
            .withColumn("address", address_udf(col("FullAddress")))
            .withColumn("OId", col("RId"))
            .groupBy("OId")
            .agg(collect_set(col("address")).alias("address"))
            .select("OId", "address")
        )

        df_documents = (
            self.read(
                path="/media/user/T7 Shield/gosuslugi_2025/ГосУслуги/gos_uslugi_2023/Document.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("Serial").isNotNull() & col("Number").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    concat(col("Serial"), col("Number")),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .withColumn("OId", col("RId"))
            .groupBy("OId")
            .agg(collect_set(col("documents")).alias("documents"))
            .select("OId", "documents")
        )

        df_mails = (
            self.read(
                path="/media/user/T7 Shield/gosuslugi_2025/ГосУслуги/gos_uslugi_2023/Mail.csv",
                sep=";",
                header=True,
            )
            .withColumn("emails", email_udf(col("Email")))
            .groupBy("OId")
            .agg(collect_set(col("emails")).alias("emails"))
            .select("OId", "emails")
        )

        df_phones = (
            self.read(
                path="/media/user/T7 Shield/gosuslugi_2025/ГосУслуги/gos_uslugi_2023/Phone.csv",
                sep=";",
                header=True,
            )
            .withColumn("phones", phone_udf(col("Number")))
            .groupBy("OId")
            .agg(collect_set(col("phones")).alias("phones"))
            .select("OId", "phones")
        )

        df_snils = (
            self.read(
                path="/media/user/T7 Shield/gosuslugi_2025/ГосУслуги/gos_uslugi_2023/Snils.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "snils_documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("Number").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("Number"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .withColumn("snils", col("Number"))
            .groupBy("OId")
            .agg(
                collect_set(col("snils_documents")).alias("snils_documents"),
                first("snils", ignorenulls=True).alias("snils"),
            )
            .select("OId", "snils_documents", "snils")
        )

        schema = (
            StructType()
            .add("Id", StringType(), True)
            .add("FId", StringType(), True)
            .add("Type", StringType(), True)
            .add("FullName", StringType(), True)
        )
        df_users_1 = (
            self.read(
                path="/media/user/T7 Shield/gosuslugi_2025/ГосУслуги/gos_uslugi_2023/User.csv",
                sep=";",
                schema=schema,
                header=False,
            )
            .withColumn("names", name_udf(col("FullName")))
            .withColumn("OId", col("Id"))
            .groupBy("OId")
            .agg(collect_set(col("names")).alias("names"))
            .select("OId", "names")
        )

        df_users_1 = (
            df_users_1.join(df_address, "OId", "left")
            .join(df_phones, "OId", "left")
            .join(df_mails, "OId", "left")
            .join(df_snils, "OId", "left")
            .join(df_documents, "OId", "left")
            .withColumn(
                "documents", flatten(concat(col("snils_documents"), col("documents")))
            )
            .withColumn("birth_date", lit(None))
            .select(
                "names",
                "birth_date",
                "address",
                "emails",
                "phones",
                "documents",
                "snils",
            )
        )

        df_users_2 = (
            self.read(
                path="/media/user/T7 Shield/gosuslugi_2025/ГосУслуги/gos_uslugi_2023/UserDetails.csv",
                sep=";",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("FirstName"), col("LastName"), col("MiddleName")),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("Birthday"), lit("%Y-%m-%d %H:%M:%S.%f")),
            )
            .withColumn("emails", email_udf(col("MailAddress")))
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
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
                            ).otherwise(None),
                            when(
                                col("Snils").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("Snils"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .groupBy("UId")
            .agg(
                collect_set(col("names")).alias("names"),
                collect_set(col("phones")).alias("phones"),
                collect_set(col("emails")).alias("emails"),
                flatten(collect_set(col("documents"))).alias("documents"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
                first("snils", ignorenulls=True).alias("snils"),
            )
            .withColumn("address", array())
            .select(
                "names",
                "birth_date",
                "address",
                "emails",
                "phones",
                "documents",
                "snils",
            )
        )

        df_users_1.persist(StorageLevel.DISK_ONLY).count()
        df_users_2.persist(StorageLevel.DISK_ONLY).count()

        df = df_persons_1.unionAll(df_users_1).unionAll(df_users_2)

        print(f"""Full: {df.count()}""")
        print(f"""With snils: {df.filter(col('snils').isNotNull()).count()}""")

        df_with_snils = (
            df.filter(col("snils").isNotNull())
            .groupBy("snils")
            .agg(
                array_compact(array_distinct(flatten(collect_set(col("names"))))).alias(
                    "names"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("phones"))))
                ).alias("phones"),
                array_compact(
                    array_distinct(flatten(collect_set(col("emails"))))
                ).alias("emails"),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
            )
            .select("names", "birth_date", "address", "emails", "phones", "documents")
        )

        df_without_snils_with_phones = (
            df.filter(col("snils").isNull() & (size(col("phones")) > 0))
            .groupBy(["names", "phones"])
            .agg(
                array_compact(
                    array_distinct(flatten(collect_set(col("emails"))))
                ).alias("emails"),
                array_compact(
                    array_distinct(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
            )
            .select("names", "birth_date", "address", "emails", "phones", "documents")
        )

        df_without_snils_and_phones = df.filter(
            col("snils").isNull() & (size(col("phones")) == 0)
        ).select("names", "birth_date", "address", "emails", "phones", "documents")

        df = df_with_snils.unionAll(df_without_snils_with_phones).unionAll(
            df_without_snils_and_phones
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
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
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
