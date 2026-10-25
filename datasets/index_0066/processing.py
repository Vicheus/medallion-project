from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    collect_set,
    size,
    array_compact,
    array_distinct,
    flatten,
    first,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    birth_date_udf,
    address_udf,
)
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0066"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True
    output_file_count: int = 50

    def parser(self):
        df_client = self.read(
            path="/media/user/SAMSUNG/Databases/index_0066/raw/clients.txt",
            sep="|",
            header=True,
        ).coalesce(50)

        passport_counts = df_client.groupBy("Паспорт (цифры)").count()

        passports_to_null = passport_counts.filter(col("count") > 3).select(
            "Паспорт (цифры)"
        )

        df_client = (
            df_client.join(
                passports_to_null.withColumn("to_null", lit(True)),
                on="Паспорт (цифры)",
                how="left",
            )
            .withColumn(
                "Паспорт (цифры)",
                when(col("to_null"), None).otherwise(col("Паспорт (цифры)")),
            )
            .drop("to_null")
        )

        df_client = (
            df_client.withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата Рождения (Д)"), lit("%d.%m.%Y"))
            )
            .withColumn("birth_place", address_udf(col("Место рождения")))
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                (
                                    col("Паспорт (цифры)").isNotNull()
                                    & (col("Паспорт (цифры)") != "")
                                ),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("Паспорт (цифры)").alias("serial"),
                                    lit(None).alias("date_issue"),
                                    lit(None).alias("date_expire"),
                                    lit(None).alias("authority"),
                                    lit(None).alias("authority_code"),
                                    lit("yyyy-MM-dd"),
                                ),
                            ),
                        )
                    )
                ),
            )
            .select(
                "Системный номер", "names", "birth_date", "birth_place", "documents"
            )
        )
        df_client.cache()

        df_phones = self.read(
            path="/media/user/SAMSUNG/Databases/index_0066/raw/phones_utf8.txt",
            sep="|",
            header=True,
        ).coalesce(50)
        df_phones.cache()

        df_existing_clients = (
            df_phones.filter(col("id").isNotNull())
            .withColumn("emails", email_udf(col("@E-mail")))
            .withColumn("phones", phone_udf(col("*Телефон")))
            .select("Системный номер", "emails", "phones")
        )

        df_with_fio = (
            df_phones.filter(col("id").isNull() & col("ФИО-группа").isNotNull())
            .withColumn("emails", lit(None))
            .withColumn("phones", lit(None))
            .withColumn("names", name_udf(col("ФИО-группа")))
            .withColumn("birth_date", birth_date_udf(col("ДР"), lit("%d.%m.%Y")))
            .withColumn("birth_place", lit(None))
            .withColumn("documents", array())
            .select(
                "names", "birth_date", "birth_place", "emails", "phones", "documents"
            )
        )

        df_client = df_client.join(
            df_existing_clients,
            df_client["Системный номер"] == df_existing_clients["Системный номер"],
            how="left",
        ).select("names", "birth_date", "birth_place", "emails", "phones", "documents")

        df = df_client.unionAll(df_with_fio)

        df_without_doc = (
            df.filter(col("documents")[0]["serial"].isNull())
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        ).select("names", "birth_date", "birth_place", "emails", "phones", "documents")

        df_with_doc = (
            df.filter(col("documents")[0]["serial"].isNotNull())
            .groupby(col("documents")[0]["serial"])
            .agg(
                collect_set("names").alias("names"),
                first("birth_date", ignorenulls=True).alias("birth_date"),
                first("birth_place", ignorenulls=True).alias("birth_place"),
                flatten(collect_set("documents")).alias("documents"),
                collect_set("emails").alias("emails"),
                collect_set("phones").alias("phones"),
            )
            .select(
                "names", "birth_date", "birth_place", "emails", "phones", "documents"
            )
        )

        df = df_with_doc.unionAll(df_without_doc)

        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
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

        df.show(n=100, truncate=False)

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
