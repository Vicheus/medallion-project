from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    struct,
    array_compact,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0217"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0217/raw/ykt_users/users.csv",
                sep="\t",
                header=True,
            )
            .replace("NULL", None)
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("ip_address", ip_address_udf(col("register_ip")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%Y-%m-%d")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                col("create_date"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "devices",
                when(
                    col("register_agent").isNotNull(),
                    array(
                        struct(
                            lit("Оформление заказа").alias("action"),
                            col("register_agent").alias("user_agent"),
                            device_date_udf(
                                col("create_date"), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "socials",
                when(
                    col("vk_id").isNotNull()
                    | col("fb_id").isNotNull()
                    | col("ok_id").isNotNull()
                    | col("insta_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("vk_id").isNotNull(),
                                social_udf(
                                    lit("Vk"), col("vk_id"), lit(None), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("fb_id").isNotNull(),
                                social_udf(
                                    lit("Facebook"), col("fb_id"), lit(None), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("ok_id").isNotNull(),
                                social_udf(
                                    lit("Ok"), col("ok_id"), lit(None), lit(None)
                                ),
                            ).otherwise(None),
                            when(
                                col("insta_id").isNotNull(),
                                social_udf(
                                    lit("Instagram"),
                                    col("insta_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("login").isNotNull() & col("password").isNotNull(),
                    array_compact(
                        array(
                            struct(
                                lit("Ykt.Ru").alias("title"),
                                lit("https://ykt.ru/").alias("link"),
                                col("login").alias("login"),
                                col("password").alias("password_hash"),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        col("create_date"),
                        col("email_verify_date"),
                        col("phone_confirmed_date"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "sex",
                "birth_date",
                "ips",
                "devices",
                "accounts",
                "socials",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "devices",
                when(size(col("devices")) > 0, col("devices")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
