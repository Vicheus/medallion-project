from pyspark import StorageLevel
from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    max,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
    flatten,
    collect_list,
    collect_set,
    first,
    coalesce,
)

from parsetron import Parsetron
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0086"

    def parser(self):
        df_email = self.read(
            path="/media/user/SAMSUNG/Databases/index_0086/raw/Westwing.ru_11.2019_3.3M/Email_Westwing.ru_11.2019_1,5M.txt",
            sep="\t",
            header=True,
            encoding="windows-1251",
        ).alias("df_email")
        df_phone = self.read(
            path="/media/user/SAMSUNG/Databases/index_0086/raw/Westwing.ru_11.2019_3.3M/Phone_Westwing.ru_11.2019_346k.txt",
            sep="\t",
            header=True,
            encoding="windows-1251",
        ).alias("df_phone")

        df_email = (
            df_email.withColumn("first_name", col("Имя"))
            .withColumn("last_name", col("Фамилия"))
            .withColumn("names", name_parts_udf(col("Имя"), col("Фамилия"), lit(None)))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "socials",
                when(
                    col("facebook_id").isNotNull() | col("google_plus_id").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("google_plus_id").isNotNull(),
                                social_udf(
                                    lit("Google Plus"),
                                    col("google_plus_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                            when(
                                col("facebook_id").isNotNull(),
                                social_udf(
                                    lit("Facebook"),
                                    col("facebook_id"),
                                    lit(None),
                                    lit(None),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("updated_at"), col("created_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
        )

        df_users_with_all_info = (
            df_email.join(
                df_phone,
                (
                    (col("df_email.id_customer") == col("df_phone.id_customer_address"))
                    & (col("df_email.Имя") == col("df_phone.first_name"))
                    & (col("df_email.Фамилия") == col("df_phone.last_name"))
                ),
                "inner",
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("postcode"),
                        col("city"),
                        col("address1"),
                        col("address2"),
                    )
                ),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("updated_at"), col("created_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names", "phones", "emails", "address", "sex", "socials", "actuality"
            )
        )

        df_users_with_only_phone_and_address = (
            df_phone.join(df_email, on=["first_name", "last_name"], how="anti")
            .withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(None))
            )
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("postcode"),
                        col("city"),
                        col("address1"),
                        col("address2"),
                    )
                ),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("socials", array())
            .withColumn("actuality", lit(None))
            .select(
                "names", "phones", "emails", "address", "sex", "socials", "actuality"
            )
        )

        df = df_users_with_all_info.unionAll(df_users_with_only_phone_and_address)

        df = df.groupBy(["phones", "names"]).agg(
            array_distinct(flatten(collect_list("socials"))).alias("socials"),
            collect_set("emails").alias("emails"),
            first("sex").alias("sex"),
            collect_set("address").alias("address"),
            max(col("actuality")).alias("actuality"),
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
        )

        df = df.select("names", "phones", "emails", "address", "sex", "socials")

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
