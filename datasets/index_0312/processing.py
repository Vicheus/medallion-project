from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    array_compact,
    size,
    collect_set,
    from_unixtime,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_date_udf, ip_address_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0312"

    def parser(self):
        df_devices = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0312/raw/preprocessed/users_devices_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("member_id", col("dmid"))
            .withColumn(
                "devices",
                when(
                    col("dua").isNotNull(),
                    struct(
                        lit("Login").alias("action"),
                        col("dua").alias("user_agent"),
                        lit(None).alias("date"),
                    ),
                ).otherwise(None),
            )
        )

        df_devices = df_devices.groupBy(["member_id"]).agg(
            collect_set("devices").alias("devices")
        )

        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0312/raw/preprocessed/members_preprocessed.csv",
                sep=";",
                header=True,
            )
            .join(df_devices, "member_id", "left")
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(name_udf(col("name")), name_udf(col("full_name")))
                    )
                ),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("address", address_udf(col("city")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("last_activity")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .withColumn("ip", ip_address_udf(col("ip_address")))
            .withColumn(
                "ip_address_date",
                ip_date_udf(
                    from_unixtime(col("last_activity")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("name").isNotNull() & col("members_pass_hash").isNotNull(),
                    array(
                        struct(
                            lit("Главный форум метрологов").alias("title"),
                            lit("https://metrologu.ru").alias("link"),
                            col("name").alias("login"),
                            col("members_pass_hash").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("profession").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    col("profession"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "ips",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("ip").isNotNull(),
                                struct(
                                    col("ip").alias("ip"),
                                    col("ip_address_date").alias("date"),
                                ),
                            )
                        )
                    )
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "address",
                "actuality",
                "emails",
                "accounts",
                "works",
                "devices",
                "ips",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "devices",
                when(size(col("devices")) > 0, col("devices")).otherwise(None),
            )
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
