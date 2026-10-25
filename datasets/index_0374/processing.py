from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    array_compact,
    array_distinct,
    struct,
    size,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0374"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0374/raw/kvadroom_ru.csv",
                sep="\t",
                header=True,
            )
            .replace("<blank>", None)
            .filter(~col("E-Mail").contains(".ua"))
            .withColumn(
                "names", name_parts_udf(col("Name"), col("Full Name"), col("Otchest"))
            )
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn("emails", email_udf(col("E-Mail")))
            .withColumn(
                "actuality", actuality_date_udf(col("Reg Date"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "works",
                when(
                    col("Company").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    col("Company"),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("emails").isNotNull() & col("Pass").isNotNull(),
                    array(
                        struct(
                            lit("Квадрум").alias("title"),
                            lit("https://kvadroom.ru").alias("link"),
                            col("emails").alias("login"),
                            col("Pass").alias("password"),
                        )
                    ),
                ),
            )
            .select("names", "emails", "phones", "actuality", "works", "accounts")
        )

        df = df.drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY).count()
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
