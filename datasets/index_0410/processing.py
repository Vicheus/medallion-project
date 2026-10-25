from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    regexp_extract,
    array_compact,
    array_distinct,
    concat,
    split,
    struct,
    coalesce,
    size,
)
from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    address_udf,
    phones_udf,
    birth_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0410"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0410/raw/orionnet.ru - @StormBaseAdapter(1).csv",
                sep=";",
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("address", address_udf(col("basic_address_text")))
            .withColumn("phones", phones_udf(split(col("contacts_text"), ",")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%m-%d")))
            .withColumn(
                "series", regexp_extract("basic_passport_text", r"серия\s*(\d{4})", 1)
            )
            .withColumn(
                "number", regexp_extract("basic_passport_text", r"номер\s*(\d+)", 1)
            )
            .withColumn(
                "issued_by",
                regexp_extract(
                    "basic_passport_text", r"выдан\s+(.+?)\s+дата выдачи", 1
                ),
            )
            .withColumn(
                "issued_at_raw",
                regexp_extract(
                    "basic_passport_text", r"дата выдачи\s*(\d{4}-\d{2}-\d{2})", 1
                ),
            )
            .withColumn(
                "issued_at",
                when(col("issued_at_raw") == "1970-01-01", None).otherwise(
                    col("issued_at_raw")
                ),
            )
            .withColumn(
                "accounts",
                when(
                    (col("login").isNotNull() | col("login2").isNotNull())
                    & (col("passwd").isNotNull() | col("passwd2").isNotNull()),
                    array(
                        struct(
                            lit("Орион телеком").alias("title"),
                            lit("http://www.orionnet.ru").alias("link"),
                            coalesce(col("login"), col("login2")).alias("login"),
                            coalesce(col("passwd"), col("passwd2")).alias("password"),
                        )
                    ),
                ),
            )
            .withColumn("ips_array", split(col("ipset_text"), ","))
            .withColumn(
                "ip1",
                when(
                    size(col("ips_array")) == 1,
                    ip_address_udf(split(col("ips_array")[0], "/")[0]),
                ).otherwise(None),
            )
            .withColumn(
                "ip2",
                when(
                    size(col("ips_array")) == 2,
                    ip_address_udf(split(col("ips_array")[1], "/")[0]),
                ).otherwise(None),
            )
            .withColumn(
                "ip3",
                when(
                    size(col("ips_array")) == 3,
                    ip_address_udf(split(col("ips_array")[2], "/")[0]),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip1").isNotNull(),
                                struct(
                                    ip_address_udf(col("ip1")).alias("ip"),
                                    lit(None).alias("date"),
                                ),
                            ),
                            when(
                                col("ip2").isNotNull(),
                                struct(
                                    ip_address_udf(col("ip2")).alias("ip"),
                                    lit(None).alias("date"),
                                ),
                            ),
                            when(
                                col("ip3").isNotNull(),
                                struct(
                                    ip_address_udf(col("ip3")).alias("ip"),
                                    lit(None).alias("date"),
                                ),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                (col("series").isNotNull() & (col("series") != ""))
                                & (col("number").isNotNull() & (col("number") != "")),
                                document_udf(
                                    lit(None),
                                    concat(col("series"), col("number")),
                                    col("issued_at"),
                                    lit(None),
                                    col("issued_by"),
                                    lit(None),
                                    lit("%Y-%M-%d"),
                                ),
                            ).otherwise(None)
                        )
                    )
                ),
            )
            .select(
                "names", "birth_date", "phones", "emails", "address", "documents", "ips"
            )
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
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
                "ips",
                when(
                    size(array_compact(col("ips"))) > 0, array_compact(col("ips"))
                ).otherwise(None),
            )
        )
        df = df.select(
            "names", "birth_date", "phones", "emails", "address", "documents", "ips"
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("address").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=50, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
