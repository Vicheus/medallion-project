from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_compact,
    size,
    coalesce,
    concat,
    collect_set,
    max,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)
from parsetron.sections.device.udfs import device_udf
from parsetron.sections.ips.udfs import ip_address_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0617"
    validate_invalid_groupping: bool = True
    calc_completeness: bool = True

    def parser(self):
        df1 = (
            self.read(
                path="/media/user/T7/datasets/index_0617/raw/preprocessed/users.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                name_parts_udf(col("name"), col("last_name"), col("middle_name")),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(
                        col("created_at"), col("updated_at"), lit("%Y-%m-%d %H:%M:%S")
                    )
                ),
            )
            .withColumn("ips", lit(None))
            .withColumn("devices", lit(None))
            .select("names", "phones", "emails", "ips", "devices", "actuality")
        )

        df2 = (
            self.read(
                path="/media/user/T7/datasets/index_0617/raw/preprocessed/user2.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("created_at"), col("updated_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn("ip", ip_address_udf(col("ip")))
            .withColumn("user_agent", concat(col("user_agent_1"), col("user_agent_2")))
            .withColumn(
                "devices",
                when(
                    col("user_agent").isNotNull(),
                    device_udf(
                        lit("Оформление заказа").alias("action"),
                        col("user_agent").alias("user_agent"),
                    ),
                ),
            )
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    struct(
                        ip_address_udf(col("ip")).alias("ip"),
                    ),
                ),
            )
            .select("names", "phones", "emails", "ips", "devices", "actuality")
        )

        df = df1.unionAll(df2)

        df = (
            df.groupBy(["names", "phones"])
            .agg(
                array_compact(collect_set(col("emails"))).alias("emails"),
                array_compact(collect_set(col("ips"))).alias("ips"),
                array_compact(collect_set(col("devices"))).alias("devices"),
                max("actuality").alias("actuality"),
            )
            .select("names", "phones", "emails", "ips", "devices", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "devices",
                when(size(col("devices")) > 0, col("devices")).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
