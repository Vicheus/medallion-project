from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    coalesce,
    max,
    array,
    size,
    struct,
    array_compact,
    array_distinct,
    collect_set,
    collect_list,
    flatten,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0033"

    def parser(self):
        df_accounts_profile = self.read(
            path="/media/user/SAMSUNG/Databases/index_0033/raw/yappy/accounts_profile.csv",
            sep="\t",
            header=True,
        )
        df_accounts_user = self.read(
            path="/media/user/SAMSUNG/Databases/index_0033/raw/yappy/accounts_user.csv",
            sep="\t",
            header=True,
        )
        df_accounts_userdevice = self.read(
            path="/media/user/SAMSUNG/Databases/index_0033/raw/yappy/accounts_userdevice.csv",
            sep="\t",
            header=True,
        )
        df_social_auth_socialids = self.read(
            path="/media/user/SAMSUNG/Databases/index_0033/raw/yappy/social_auth_socialids.csv",
            sep="\t",
            header=True,
        )

        df_accounts_profile = (
            df_accounts_profile.replace("NULL", None)
            .withColumn(
                "names",
                regexp_replace(
                    name_parts_udf(col("first_name"), col("last_name"), lit("")),
                    r"^[\W_]+|[\W_]+$",
                    "",
                ),
            )
            .filter(
                col("names").rlike(".*[a-zA-Zа-яА-Я].*[a-zA-Zа-яА-Я].*[a-zA-Zа-яА-Я].*")
            )
            .select(
                "names",
                "nickname",
                "phone",
                "user_id",
                "approved_date",
                "last_user_updated_at",
            )
            .alias("accounts_profile")
        )

        df_accounts_user = (
            df_accounts_user.replace("NULL", None)
            .select("username", "password", "email", "id")
            .alias("accounts_user")
        )

        df_accounts_userdevice = (
            df_accounts_userdevice.replace("NULL", None)
            .select("creator_id", "device", "os", "last_visit")
            .alias("accounts_userdevice")
        )

        df_social_auth_socialids = (
            df_social_auth_socialids.replace("NULL", None)
            .select("profile_id", "external_id")
            .alias("social_auth_socialids")
        )

        df = (
            df_accounts_profile.join(
                df_accounts_user,
                df_accounts_profile.user_id == df_accounts_user.id,
                "left",
            )
            .join(
                df_accounts_userdevice,
                df_accounts_profile.user_id == df_accounts_userdevice.creator_id,
                "left",
            )
            .join(
                df_social_auth_socialids,
                df_accounts_profile.user_id == df_social_auth_socialids.profile_id,
                "left",
            )
        )
        df = (
            df.withColumn(
                "phones",
                array_distinct(
                    array_compact(
                        array(
                            phone_udf(col("accounts_profile.phone")),
                            phone_udf(col("social_auth_socialids.external_id")),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("accounts_user.email")))
            .withColumn(
                "devices",
                when(
                    col("device").isNotNull(),
                    array(
                        struct(
                            lit("Вход").alias("action"),
                            concat_ws(
                                " ",
                                col("accounts_userdevice.device"),
                                col("accounts_userdevice.os"),
                            ).alias("title"),
                            device_date_udf(
                                col("accounts_userdevice.last_visit")
                            ).alias("date"),
                        )
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("accounts_user.id").isNotNull(),
                    array(
                        struct(
                            lit("Yappi").alias("title"),
                            col("accounts_user.password").alias("password_hash"),
                            col("accounts_user.id").alias("id"),
                            col("accounts_user.username").alias("login"),
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("last_user_updated_at"), col("approved_date")),
                    lit("%Y-%m-%d %H:%M:%S.%f"),
                ),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
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
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )

        df = df.select("names", "emails", "phones", "accounts", "devices", "actuality")

        df = df.groupby(col("names"), col("phones")).agg(
            when(size(collect_set("emails")) > 0, collect_set("emails"))
            .otherwise(None)
            .alias("emails"),
            when(
                size(array_compact(array_distinct(flatten(collect_list("accounts")))))
                > 0,
                array_compact(array_distinct(flatten(collect_list("accounts")))),
            )
            .otherwise(None)
            .alias("accounts"),
            when(
                size(array_compact(array_distinct(flatten(collect_list("devices")))))
                > 0,
                array_compact(array_distinct(flatten(collect_list("devices")))),
            )
            .otherwise(None)
            .alias("devices"),
            max("actuality").alias("actuality"),
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
