from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, greatest

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0129"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0129/raw/pilkinail @durov_database.json/users-crm-796452.json",
            sep="\n",
            header=False,
        )

        df = (
            df.replace("NULL", None)
            .withColumn("birth_date", col("_source.birth_date"))
            .withColumn("email", col("_source.email"))
            .withColumn("first_name", col("_source.first_name"))
            .withColumn("last_name", col("_source.last_name"))
            .withColumn("middle_name", col("_source.middle_name"))
            .withColumn("phone", col("_source.phone"))
            .withColumn("sex", col("_source.sex"))
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "birth_date",
                birth_date_udf(col("birth_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("_source.app_login_at"),
                        col("_source.created_at"),
                        col("_source.last_active_at"),
                        col("_source.last_visit"),
                        col("_source.updated_at"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("order_count"),
                    col("_source.order_count"),
                    lit("payment_count"),
                    col("_source.payment_count"),
                    lit("payment_sum"),
                    col("_source.payment_sum"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "birth_date",
                "sex",
                "actuality",
                "raw_metadata",
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df = df.dropDuplicates()

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select("names", "emails", "phones", "birth_date", "sex", "actuality")

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
