from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    max,
    size,
    array_distinct,
    flatten,
    collect_list,
    collect_set,
    first,
    from_unixtime,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    birth_date_udf,
    email_udf,
    sex_udf,
    actuality_date_udf,
)
from parsetron.sections.device.udfs import device_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: 10
    dataset_code_name: str = "index_0019"

    def parser(self):
        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0019/raw/users_kassy.ru/users_kassy.ru_3M.csv",
            sep=",",
            header=True,
        )
        df_orders = self.read(
            path="/media/user/SAMSUNG/Databases/index_0019/raw/users_kassy.ru/orders_kassy.ru_13.8M/*.csv",
            sep=",",
            header=True,
        )

        df_users = (
            df_users.withColumn(
                "names", name_parts_udf(col("name"), col("family"), col("patronymic"))
            )
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "birth_date", birth_date_udf(col("birthday"), lit("yyyy-MM-dd"))
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "accounts",
                when(
                    col("password").isNotNull() & col("login").isNotNull(),
                    array(
                        struct(
                            lit("kassy.ru").alias("title"),
                            lit("https://kassy.ru/").alias("link"),
                            col("login").alias("login"),
                            col("password").alias("password_hash"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(
                        coalesce(col("dt_update"), col("dt_create"), col("dt_check")),
                        "yyyy-MM-dd HH:mm:ss",
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
        )
        df_users = df_users.select(
            "user_id",
            "names",
            "sex",
            "birth_date",
            "phones",
            "emails",
            "accounts",
            "actuality",
        )
        df_users = df_users.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("accounts").isNotNull()
            )
        )

        df_orders = df_orders.withColumn("ip", ip_address_udf(col("ip")))

        df_orders = df_orders.select("user_id", "ip", "dt_create", "agent").filter(
            col("user_id").isNotNull()
        )
        df_orders = df_orders.groupBy("user_id", "ip", "agent").agg(
            max("dt_create").alias("dt_create")
        )

        df_orders.show(n=20, truncate=False)

        df_orders = df_orders.withColumn(
            "ips",
            when(
                col("ip").isNotNull(),
                array(
                    struct(
                        col("ip").alias("ip"),
                        ip_date_udf(
                            from_unixtime(col("dt_create"), "yyyy-MM-dd HH:mm:ss")
                        ).alias("date"),
                    )
                ),
            ),
        ).withColumn(
            "devices",
            when(
                col("agent").isNotNull(),
                array(
                    struct(
                        lit("kassy.ru").alias("title"),
                        col("agent").alias("user_agent"),
                        device_date_udf(
                            from_unixtime(col("dt_create"), "yyyy-MM-dd HH:mm:ss")
                        ).alias("date"),
                    )
                ),
            ),
        )

        df = df_users.join(df_orders, on="user_id", how="left")

        df = df.groupby("user_id").agg(
            when(size(collect_set("names")) > 0, collect_set("names"))
            .otherwise(None)
            .alias("names"),
            first("sex").alias("sex"),
            first("birth_date").alias("birth_date"),
            max("actuality").alias("actuality"),
            when(size(collect_set("phones")) > 0, collect_set("phones"))
            .otherwise(None)
            .alias("phones"),
            when(size(collect_set("emails")) > 0, collect_set("emails"))
            .otherwise(None)
            .alias("emails"),
            when(
                size(array_distinct(flatten(collect_list("accounts")))) > 0,
                array_distinct(flatten(collect_list("accounts"))),
            )
            .otherwise(None)
            .alias("accounts"),
            when(
                size(array_distinct(flatten(collect_list("devices")))) > 0,
                array_distinct(flatten(collect_list("devices"))),
            )
            .otherwise(None)
            .alias("devices"),
            when(
                size(array_distinct(flatten(collect_list("ips")))) > 0,
                array_distinct(flatten(collect_list("ips"))),
            )
            .otherwise(None)
            .alias("ips"),
        )

        df = df.select(
            "names",
            "sex",
            "birth_date",
            "phones",
            "emails",
            "accounts",
            "ips",
            "devices",
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=100, truncate=False)

        df.printSchema()

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
