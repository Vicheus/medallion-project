from pyspark.sql.functions import (
    when,
    col,
    array,
    trim,
    regexp_replace,
    lit,
    struct,
    max,
    array_compact,
    concat_ws,
    first,
    array_distinct,
    flatten,
    collect_list,
    size,
    monotonically_increasing_id,
)
from pyspark.sql.types import StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import phone_udf, actuality_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "telegram_users"
    calc_completeness: bool = False

    def parser(self):
        source = "telegram_users"
        full_name_replace_regexp = "[^А-Яа-я\s]+"

        df_old = (
            self.read(
                path="/home/user/Documents/dev/git/datasets/data/out/telegram_users_16_09/opt/spark-data/out/telegram_users_16_09.json/telegram_users_16_09.json",
                header=False,
                sep="\n",
            )
            .withColumn("additional_info", col("metadata.additional_info"))
            .withColumn("created_date", col("metadata.created_date"))
            .withColumn("tg_id", col("metadata.tg_id"))
            .withColumn("tg_username", col("metadata.tg_username"))
            .select(
                "source",
                "full_name",
                "phone",
                "email",
                "additional_info",
                "created_date",
                "tg_id",
                "tg_username",
            )
        )

        df_1 = (
            self.read(
                path="/home/user/Documents/dev/git/datasets/data/tg/11_11/personfinder_backend_public_users.csv",
                header=True,
                sep=",",
            )
            .withColumn("source", lit(source))
            .withColumn(
                "full_name",
                trim(regexp_replace(col("name"), full_name_replace_regexp, "")),
            )
            .withColumn("phone", array_compact(array(phone_udf(col("phone")))))
            .withColumn("email", array())
            .withColumn("tg_id", col("tg_id").cast(StringType()))
            .withColumn("tg_username", trim(col("tg_username")))
            .withColumn("created_date", lit(None))
            .withColumn("additional_info", lit(None))
            .select(
                "source",
                "full_name",
                "phone",
                "email",
                "additional_info",
                "created_date",
                "tg_id",
                "tg_username",
            )
        )

        df_2 = (
            self.read(
                path="/home/user/Documents/dev/git/datasets/data/tg/11_11/tg_contact.csv",
                header=True,
                sep=",",
            )
            .withColumn("source", lit(source))
            .withColumn(
                "full_name",
                trim(
                    regexp_replace(
                        concat_ws(" ", col("last_name"), col("first_name")),
                        full_name_replace_regexp,
                        "",
                    )
                ),
            )
            .withColumn(
                "phone",
                array_compact(
                    array(phone_udf(col("phone1")), phone_udf(col("phone2")))
                ),
            )
            .withColumn("email", array())
            .withColumn("tg_id", col("tg_id").cast(StringType()))
            .withColumn("tg_username", trim(col("tg_username")))
            .withColumn(
                "created_date",
                actuality_date_udf(col("date2"), lit("%Y-%m-%dT%H:%M:%S.%f%z")),
            )
            .withColumn("additional_info", lit(None))
            .select(
                "source",
                "full_name",
                "phone",
                "email",
                "additional_info",
                "created_date",
                "tg_id",
                "tg_username",
            )
        )

        df_3 = (
            self.read(
                "/home/user/Documents/dev/git/datasets/data/tg/11_11/Trusted - Аркуш2.csv",
                header=True,
                sep=",",
            )
            .withColumn("source", lit(source))
            .withColumn("full_name", lit(None))
            .withColumn("phone", array_compact(array(phone_udf(col("Phone")))))
            .withColumn("email", array())
            .withColumn("tg_id", col("TG ID").cast(StringType()))
            .withColumn("tg_username", trim(col("TG username")))
            .withColumn("created_date", lit(None))
            .withColumn("additional_info", lit(None))
            .select(
                "source",
                "full_name",
                "phone",
                "email",
                "additional_info",
                "created_date",
                "tg_id",
                "tg_username",
            )
        )

        df_new = df_1.unionAll(df_2).unionAll(df_3)

        df = df_old.unionAll(df_new)

        df = (
            df.groupBy(["tg_id"])
            .agg(
                first("tg_username", ignorenulls=True).alias("tg_username"),
                first("full_name", ignorenulls=True).alias("full_name"),
                array_compact(array_distinct(collect_list("additional_info"))).alias(
                    "additional_info"
                ),
                max("created_date").alias("created_date"),
                array_compact(
                    array_distinct(flatten(collect_list(col("phone"))))
                ).alias("phone"),
                array_compact(
                    array_distinct(flatten(collect_list(col("email"))))
                ).alias("email"),
            )
            .select(
                "tg_id",
                "tg_username",
                "full_name",
                "phone",
                "email",
                "additional_info",
                "created_date",
            )
        )

        print(f"""After group size: {df.count()}""")

        df = (
            df.withColumn("source", lit(source))
            .withColumn("tg_id", col("tg_id"))
            .withColumn("tg_username", col("tg_username"))
            .withColumn(
                "phone",
                when(size(array_compact(col("phone"))) > 0, col("phone")).otherwise(
                    None
                ),
            )
            .withColumn(
                "email",
                when(size(array_compact(col("email"))) > 0, col("email")).otherwise(
                    None
                ),
            )
            .select(
                "source",
                "tg_id",
                "tg_username",
                "full_name",
                "phone",
                "email",
                "additional_info",
                "created_date",
            )
        )

        print(
            f"""TG_ID-PHONE: {df.filter(col('tg_id').isNotNull() & col('phone').isNotNull()).count()}"""
        )

        df.show()

        df = df.withColumn("id", monotonically_increasing_id()).select(
            "id",
            "source",
            "full_name",
            "phone",
            "email",
            struct("tg_id", "tg_username", "additional_info", "created_date").alias(
                "metadata"
            ),
        )

        print(
            "---------------------------------------------------------PROCESSING FINISHED---------------------------------------------------------"
        )
        print(f"""Final df size: {df.count()}""")

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
