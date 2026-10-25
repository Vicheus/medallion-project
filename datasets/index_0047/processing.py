from pyspark.sql.functions import (
    size,
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    coalesce,
)
from pyspark.sql.types import StructType, StringType

from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0047"
    calc_completeness: bool = False

    def parser(self):

        schema = (
            StructType()
            .add("id", StringType(), True)
            .add("username", StringType(), True)
            .add("username_canonical", StringType(), True)
            .add("email", StringType(), True)
            .add("email_canonical", StringType(), True)
            .add("enabled", StringType(), True)
            .add("salt", StringType(), True)
            .add("password", StringType(), True)
            .add("last_login", StringType(), True)
            .add("confirmation_token", StringType(), True)
            .add("password_requested_at", StringType(), True)
            .add("roles", StringType(), True)
            .add("created_at", StringType(), True)
            .add("updated_at", StringType(), True)
            .add("date_of_birth", StringType(), True)
            .add("firstname", StringType(), True)
            .add("lastname", StringType(), True)
            .add("website", StringType(), True)
            .add("biography", StringType(), True)
            .add("gender", StringType(), True)
            .add("locale", StringType(), True)
            .add("timezone", StringType(), True)
            .add("phone", StringType(), True)
            .add("facebook_uid", StringType(), True)
            .add("facebook_name", StringType(), True)
            .add("facebook_data", StringType(), True)
            .add("twitter_uid", StringType(), True)
            .add("twitter_name", StringType(), True)
            .add("twitter_data", StringType(), True)
            .add("gplus_uid", StringType(), True)
            .add("gplus_name", StringType(), True)
            .add("gplus_data", StringType(), True)
            .add("token", StringType(), True)
            .add("two_step_code", StringType(), True)
            .add("patronymic", StringType(), True)
            .add("position", StringType(), True)
            .add("publisher_id", StringType(), True)
            .add("schoolclass_id", StringType(), True)
            .add("school_title", StringType(), True)
            .add("skype", StringType(), True)
            .add("address", StringType(), True)
            .add("region_id", StringType(), True)
            .add("country_id", StringType(), True)
            .add("type", StringType(), True)
            .add("vkontakte_uid", StringType(), True)
            .add("odnoklassniki_uid", StringType(), True)
            .add("avatar", StringType(), True)
            .add("show_stat", StringType(), True)
            .add("show_activity", StringType(), True)
            .add("qid", StringType(), True)
            .add("school_number", StringType(), True)
            .add("city", StringType(), True)
            .add("main_language_id", StringType(), True)
            .add("additional_language_id", StringType(), True)
            .add("is_participate_in_verification", StringType(), True)
            .add("teacher_code", StringType(), True)
            .add("school_id", StringType(), True)
            .add("school_locality_id", StringType(), True)
            .add("deleted_at", StringType(), True)
            .add("deleted", StringType(), True)
            .add("esia_id", StringType(), True)
        )

        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0047/raw/resh.csv",
            sep=",",
            schema=schema,
            header=False,
        )

        df = (
            df.replace("null", None)
            .withColumn(
                "names",
                name_parts_udf(col("firstname"), col("lastname"), col("patronymic")),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "birth_date",
                birth_date_udf(col("date_of_birth"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "socials",
                when(
                    col("facebook_uid").isNotNull()
                    | col("facebook_name").isNotNull()
                    | col("twitter_uid").isNotNull()
                    | col("twitter_name").isNotNull()
                    | col("gplus_uid").isNotNull()
                    | col("gplus_name").isNotNull()
                    | col("skype").isNotNull()
                    | col("vkontakte_uid").isNotNull()
                    | col("odnoklassniki_uid").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("facebook_uid").isNotNull()
                                | col("facebook_name").isNotNull(),
                                social_udf(
                                    lit("Facebook"),
                                    col("facebook_uid"),
                                    col("facebook_name"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("twitter_uid").isNotNull()
                                | col("twitter_name").isNotNull(),
                                social_udf(
                                    lit("Twitter"),
                                    col("twitter_uid"),
                                    col("twitter_name"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("gplus_uid").isNotNull()
                                | col("gplus_name").isNotNull(),
                                social_udf(
                                    lit("Google Plus"),
                                    col("gplus_uid"),
                                    col("gplus_name"),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("vkontakte_uid").isNotNull()
                                & ~col("vkontakte_uid").isin(
                                    ["Ученик", "Учитель", "Родитель"]
                                ),
                                social_udf(
                                    lit("ВКонтакте"),
                                    col("vkontakte_uid"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("odnoklassniki_uid").isNotNull(),
                                social_udf(
                                    lit("Одноклассники"),
                                    col("odnoklassniki_uid"),
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
                    col("id").isNotNull() & col("username").isNotNull(),
                    array_compact(
                        array(
                            struct(
                                lit("Российская электронная школа").alias("title"),
                                lit("http://resh.edu.ru").alias("link"),
                                col("username").alias("login"),
                                col("id").alias("id"),
                                col("password").alias("password"),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("last_login"), col("updated_at"), col("created_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("school_title"),
                    col("school_title"),
                    lit("esia_id"),
                    col("esia_id"),
                    lit("biography"),
                    col("biography"),
                    lit("position"),
                    col("position"),
                ),
            )
        )

        df = df.select(
            "names",
            "phones",
            "emails",
            "birth_date",
            "sex",
            "socials",
            "accounts",
            "actuality",
            "raw_metadata",
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
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
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
