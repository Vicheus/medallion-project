from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    array_size,
    struct,
    coalesce,
    regexp_replace,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    raw_metadata_udf,
    actuality_date_udf,
    relations_udf,
)
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.document.udfs import document_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0513"
    calc_completeness: bool = False
    validate_invalid_groupping: bool = True
    output_file_count: int = 5
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        df = self.read(
            path="/home/user/Downloads/bases_new/daryn_online.csv",
            sep=",",
        )

        df_schools = self.read(
            path="/home/user/Downloads/bases_new/daryn_school.csv",
            sep=",",
        )

        child = df.alias("child")
        parent = df.alias("parent")
        df_schools = df_schools.alias("schools")

        df = (
            child.join(
                parent, col("child.parent_user_id") == col("parent.user_id"), "left"
            )
            .join(
                df_schools, col("child.school_id") == col("schools.school_id"), "left"
            )
            .withColumn("names", name_udf(col("child.name")))
            .withColumn(
                "phones",
                phone_udf(col("child.phone"), lit(self.dataset_country_code.value)),
            )
            .withColumn("emails", email_udf(col("child.email")))
            .withColumn(
                "birth_date", birth_date_udf(col("child.birthdate"), lit("%Y-%m-%d"))
            )
            .withColumn("ip", ip_address_udf(col("child.last_known_ip")))
            .withColumn(
                "accounts",
                array(
                    struct(
                        lit("Daryn.kz – РГПО «ДАРЫН»").alias("title"),
                        lit("https://daryn.kz/").alias("link"),
                        col("child.email").alias("login"),
                        col("child.password").alias("password_hash"),
                    )
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("child.iin").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("child.iin").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("child.iin"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                    lit(self.dataset_country_code.value),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("child.updated_at"), col("child.created_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            col("ip").alias("ip"),
                            ip_date_udf(
                                col("child.last_available"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("child.user_desc"),
                    regexp_replace(col("child.user_desc"), "<[^>]+>", ""),
                ),
            )
            .withColumn(
                "relations",
                when(
                    col("parent.name").isNotNull(),
                    relations_udf(
                        concat_ws(" ", name_udf(col("parent.name")), lit("Родитель"))
                    ),
                ).otherwise(None),
            )
            .select(
                "names",
                "birth_date",
                "phones",
                "emails",
                "relations",
                "ips",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(), array_compact(array(col("emails")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(), array_compact(array(col("phones")))
                ).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    col("relations").isNotNull(), array_compact(array(col("relations")))
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(array_size(col("ips")) > 0, col("ips")).otherwise(None),
            )
            .withColumn(
                "documents",
                when(array_size(col("documents")) > 0, col("documents")).otherwise(
                    None
                ),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(),
                    array_compact(array(col("raw_metadata"))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
