from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    collect_set,
    array,
    max,
    size,
    concat_ws,
    concat,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0214"

    def parser(self):
        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0214/raw/preprocessed/users_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("lastname"), col("firstname"), col("fathersname")),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        when(col("zip").isNotNull(), col("zip")).otherwise(None),
                        when(col("city").isNotNull(), col("city")).otherwise(None),
                        when(col("street").isNotNull(), col("street")).otherwise(None),
                        when(
                            col("building").isNotNull(),
                            concat(lit("д. "), col("building")),
                        ).otherwise(None),
                        when(
                            col("flat").isNotNull(), concat(lit("кв. "), col("flat"))
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("datetime"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("amount"),
                    col("amount"),
                    lit("withdraw_amount"),
                    col("withdraw_amount"),
                    lit("notification_type"),
                    col("notification_type"),
                ),
            )
            .select("names", "emails", "phones", "address", "actuality", "raw_metadata")
        )

        df_payments = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0214/raw/preprocessed/payments_preprocessed.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("lastname"), col("firstname"), col("fathersname")),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        when(col("zip").isNotNull(), col("zip")).otherwise(None),
                        when(col("city").isNotNull(), col("city")).otherwise(None),
                        when(col("street").isNotNull(), col("street")).otherwise(None),
                        when(
                            col("building").isNotNull(),
                            concat(lit("д. "), col("building")),
                        ).otherwise(None),
                        when(
                            col("flat").isNotNull(), concat(lit("кв. "), col("flat"))
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn("actuality", lit(None))
            .withColumn("raw_metadata", lit(None))
            .withColumn("raw_metadata", lit(None))
            .select("names", "emails", "phones", "address", "actuality", "raw_metadata")
        )

        df = (
            df_users.unionAll(df_payments)
            .groupBy(["names", "phones"])
            .agg(
                collect_set(col("emails")).alias("emails"),
                collect_set(col("address")).alias("address"),
                max("actuality").alias("actuality"),
                collect_set("raw_metadata").alias("raw_metadata"),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
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
