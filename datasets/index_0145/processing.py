from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, struct, size, greatest
from pyspark.sql.types import StringType, StructField, StructType

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    actuality_date_udf,
)
from parsetron.sections.device.udfs import device_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0145"

    def parser(self):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("type", StringType(), True),
                StructField("source", StringType(), True),
                StructField("name", StringType(), True),
                StructField("last_name", StringType(), True),
                StructField("middle_name", StringType(), True),
                StructField("birthday", StringType(), True),
                StructField("email", StringType(), True),
                StructField("phone", StringType(), True),
                StructField("phone_is_preferred", StringType(), True),
                StructField("email_is_preferred", StringType(), True),
                StructField("sms_is_preferred", StringType(), True),
                StructField("comment", StringType(), True),
                StructField("dealership_id", StringType(), True),
                StructField("model_code", StringType(), True),
                StructField("call_request_id", StringType(), True),
                StructField("feedback_request_id", StringType(), True),
                StructField("corporate_client_request_id", StringType(), True),
                StructField("credit_request_id", StringType(), True),
                StructField("purchase_car_request_id", StringType(), True),
                StructField("test_drive_request_id", StringType(), True),
                StructField("ip", StringType(), True),
                StructField("user_agent", StringType(), True),
                StructField("created_at", StringType(), True),
                StructField("used_cars_request_id", StringType(), True),
                StructField("subscribe_request_id", StringType(), True),
                StructField("rent_request_id", StringType(), True),
                StructField("service_request_id", StringType(), True),
                StructField("is_dealer_platform", StringType(), True),
                StructField("spare_request_id", StringType(), True),
                StructField("accessory_request_id", StringType(), True),
                StructField("preapproval_request_id", StringType(), True),
                StructField("order_request_id", StringType(), True),
                StructField("crm_lead_type", StringType(), True),
                StructField("comment_crm", StringType(), True),
                StructField("channel_detail", StringType(), True),
                StructField("auction_request_id", StringType(), True),
                StructField("extended_insurance_request_id", StringType(), True),
            ]
        )
        df_leads = (
            self.read(
                path="/home/user/Documents/data/index_0145/raw/kia.ru/preprocessed/leads.csv",
                sep="\t",
                schema=schema,
                header=False,
            )
            .replace("NULL", None)
            .replace("\tNULL", None)
            .replace("\\N", None)
            .withColumn(
                "names",
                name_parts_udf(
                    col("name"),
                    col("last_name"),
                    when(col("middle_name") == "N", lit(None)).otherwise(
                        col("middle_name")
                    ),
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%M-%d")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "ips",
                when(
                    col("ip").isNotNull(),
                    array(
                        struct(
                            col("ip").alias("ip"),
                            ip_date_udf(
                                col("created_at"), lit("yyyy-MM-dd HH:mm:ss")
                            ).alias("date"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "devices",
                when(
                    col("user_agent").isNotNull(),
                    array(
                        struct(
                            lit("kia.ru").alias("title"),
                            col("user_agent").alias("user_agent"),
                            device_date_udf(
                                col("created_at"), lit("yyyy-MM-dd HH:mm:ss")
                            ).alias("date"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("accounts", array())
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .select(
                "names",
                "phones",
                "emails",
                "birth_date",
                "ips",
                "devices",
                "accounts",
                "actuality",
            )
        )

        df_users = (
            self.read(
                path="/home/user/Documents/data/index_0145/raw/kia.ru/preprocessed/users.csv",
                sep=",",
                header=True,
            )
            .replace("NULL", None)
            .replace("\tNULL", None)
            .replace("\\N", None)
            .withColumn(
                "names",
                name_parts_udf(
                    col("name"),
                    col("surname"),
                    when(col("second_name") == "N", lit(None)).otherwise(
                        col("second_name")
                    ),
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%M-%d")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("ips", array())
            .withColumn(
                "devices",
                when(
                    col("mobile_user_agent").isNotNull(),
                    array(
                        struct(
                            lit("kia.ru").alias("title"),
                            col("mobile_user_agent").alias("user_agent"),
                            device_date_udf(
                                col("last_login_mobile"), lit("yyyy-MM-dd HH:mm:ss")
                            ).alias("date"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("email").isNotNull() & col("password").isNotNull(),
                    array(
                        struct(
                            lit("Kia.ru").alias("title"),
                            lit("https://www.kia.ru").alias("link"),
                            col("password").alias("password_hash"),
                            col("email").alias("login"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(col("last_login_web"), col("last_login_mobile")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "birth_date",
                "ips",
                "devices",
                "accounts",
                "actuality",
            )
        )

        df = df_leads.unionAll(df_users).drop_duplicates()

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("accounts").isNotNull()
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
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
            .withColumn(
                "devices",
                when(size(col("devices")) > 0, col("devices")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
