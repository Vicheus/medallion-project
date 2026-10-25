from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    collect_list,
    struct,
    trim,
    lower,
    concat,
    flatten,
    max,
    first,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
    birth_date_udf,
)
from parsetron.sections.socials.udfs import social_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0564"
    validate_invalid_groupping: bool = True

    def parser(self):
        EMAILS_TO_IGNORE = ["info@monochromeyou.ru"]
        df_orders = (
            (
                self.read(
                    path="/home/user/Documents/data/index_0564/raw/MONOCHROME/order*.csv",
                    sep=",",
                    header=True,
                )
            )
            .replace("NULL", None)
            .filter(
                (
                    lower(trim(col("country"))).isin(["россия", "ru", "russia", "рф"])
                    | col("country").isNull()
                )
                & ~(col("email").isin(EMAILS_TO_IGNORE))
            )
        )

        df_preorders = (
            (
                self.read(
                    path="/home/user/Documents/data/index_0564/raw/MONOCHROME/preorder.csv",
                    sep=",",
                    header=True,
                )
            )
            .replace("NULL", None)
            .filter((col("phone").startswith("7") | col("phone").startswith("+7")))
        )

        df_cards = self.read(
            path="/home/user/Documents/data/index_0564/raw/MONOCHROME/cards.csv",
            sep=",",
            header=True,
        )
        df_users = (
            self.read(
                path="/home/user/Documents/data/index_0564/raw/MONOCHROME/users*.csv",
                sep=",",
                header=True,
            )
            .filter(
                (~col("username").contains("@yahoo.com"))
                & (col("phone").startswith("7") | col("phone").startswith("+7"))
            )
            .withColumn("user_id", col("admin_id"))
            .withColumn(
                "names",
                array_compact(
                    array(name_parts_udf(col("name"), col("surname"), lit(None)))
                ),
            )
            .withColumn("birth_date", birth_date_udf(col("dob"), lit("%Y-%m-%d")))
            .withColumn("emails", array_compact(array(email_udf(col("username")))))
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .withColumn("address", array_compact(array(address_udf(col("city")))))
        )

        df_users = (
            df_users.join(df_cards, "user_id", "left")
            .withColumn(
                "socials",
                when(
                    col("instagram").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("instagram").isNotNull(),
                                social_udf(
                                    lit("Instagram"),
                                    col("instagram"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None)
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                array(
                    struct(
                        lit("MONOCHROME").alias("title"),
                        lit("https://monochrome.ru").alias("link"),
                        col("username").alias("login"),
                        col("password").alias("password_hash"),
                        col("number").alias("client_card_number"),
                    )
                ),
            )
            .withColumn("raw_metadata", array())
            .withColumn("actuality", lit(None))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "socials",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df_orders = (
            df_orders.withColumn(
                "names", name_parts_udf(col("name"), col("surname"), lit(None))
            )
            .withColumn("birth_date", lit(None))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address_str",
                when(
                    col("city").isNotNull(),
                    concat_ws(
                        ", ",
                        when(
                            col("postcode") != "",
                            col("postcode"),
                        ).otherwise(None),
                        when(
                            col("country") != "",
                            col("country"),
                        ).otherwise(None),
                        col("city"),
                        when(
                            col("street") != "",
                            concat(lit("ул. "), col("street")),
                        ).otherwise(None),
                        when(
                            col("house") != "",
                            concat(lit("д. "), col("house")),
                        ).otherwise(None),
                        when(
                            col("building") != "", concat(lit("стр. "), col("building"))
                        ).otherwise(None),
                        when(
                            col("building") != "",
                            concat(lit("кв. "), col("building")),
                        ).otherwise(None),
                    ),
                ),
            )
            .withColumn("address", address_udf(col("address_str")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("comment_a"),
                    col("comment_a"),
                    lit("comment"),
                    col("comment"),
                ),
            )
            .withColumn("socials", array())
            .withColumn("accounts", array())
            .select(
                "user_id",
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "socials",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df_orders = (
            df_orders.withColumn("names", array_compact(array(col("names"))))
            .withColumn("emails", array_compact(array(col("emails"))))
            .withColumn("phones", array_compact(array(col("phones"))))
            .withColumn("address", array_compact(array(col("address"))))
            .withColumn("raw_metadata", array_compact(array(col("raw_metadata"))))
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "socials",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df_preorders = (
            df_preorders.withColumn(
                "names", array_compact(array(name_udf(col("name"))))
            )
            .withColumn("emails", array_compact(array(email_udf(col("email")))))
            .withColumn("phones", array_compact(array(name_udf(col("phone")))))
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("birth_date", lit(None))
            .withColumn("address", array())
            .withColumn("socials", array())
            .withColumn("accounts", array())
            .withColumn("raw_metadata", array())
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "socials",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_orders.unionAll(df_users).unionAll(df_preorders)

        df = df.filter(
            col("names").isNotNull()
            & (
                (col("phones").isNotNull() & (size(col("phones")) > 0))
                | (col("emails").isNotNull() & (size(col("emails")) > 0))
            )
        )

        df = (
            df.groupBy(["emails", "phones"])
            .agg(
                array_compact(
                    array_distinct(flatten(collect_list(col("names"))))
                ).alias("names"),
                array_compact(
                    array_distinct(flatten(collect_list(col("address"))))
                ).alias("address"),
                array_compact(
                    array_distinct(flatten(collect_list(col("socials"))))
                ).alias("socials"),
                array_compact(
                    array_distinct(flatten(collect_list(col("accounts"))))
                ).alias("accounts"),
                array_compact(
                    array_distinct(flatten(collect_list(col("raw_metadata"))))
                ).alias("raw_metadata"),
                max(col("actuality")).alias("actuality"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
            )
            .select(
                "names",
                "birth_date",
                "emails",
                "phones",
                "address",
                "socials",
                "accounts",
                "raw_metadata",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
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
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
        )

        df = df.filter(
            (col("names").isNotNull() & (size(col("names")) > 0))
            & (
                (col("phones").isNotNull() & (size(col("phones")) > 0))
                | (col("emails").isNotNull() & (size(col("emails")) > 0))
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
