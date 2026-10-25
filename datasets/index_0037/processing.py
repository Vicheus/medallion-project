from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    size,
    array_compact,
    from_json,
    concat_ws,
    concat,
    array_distinct,
    coalesce,
)
from pyspark.sql.types import StructType, StructField, StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0037"
    write_filtered_rows: bool = True
    important_columns_for_filtering: str = "phones,emails,address"

    def parser(self):

        df_profiles = self.read(
            path="/media/user/SAMSUNG/Databases/index_0037/raw/auchan/profiles.csv",
            sep="\t",
            header=True,
        )

        df_customers = self.read(
            path="/media/user/SAMSUNG/Databases/index_0037/raw/auchan/customers.csv",
            sep="\t",
            header=True,
        ).replace("NULL", None)

        df_customer_addresses = self.read(
            path="/media/user/SAMSUNG/Databases/index_0037/raw/auchan/customer_addresses.csv",
            sep="\t",
            header=True,
        )
        address_json_schema = StructType(
            [
                StructField("area", StringType(), True),
                StructField("city", StringType(), True),
                StructField("flat", StringType(), True),
                StructField("block", StringType(), True),
                StructField("floor", StringType(), True),
                StructField("house", StringType(), True),
                StructField("porch", StringType(), True),
                StructField("region", StringType(), True),
                StructField("street", StringType(), True),
                StructField("comment", StringType(), True),
                StructField("geo_lat", StringType(), True),
                StructField("geo_lon", StringType(), True),
                StructField("intercom", StringType(), True),
                StructField("area_guid", StringType(), True),
                StructField("city_guid", StringType(), True),
                StructField("post_index", StringType(), True),
                StructField("region_guid", StringType(), True),
                StructField("country_code", StringType(), True),
                StructField("address_string", StringType(), True),
            ]
        )

        df_customer_addresses = df_customer_addresses.withColumn(
            "address", from_json(col("address"), address_json_schema)
        )
        df_customer_addresses = df_customer_addresses.withColumn(
            "address",
            when(
                col("address.address_string").isNotNull(),
                address_udf(col("address.address_string")),
            ).otherwise(
                address_udf(
                    concat_ws(
                        ", ",
                        when(
                            col("address.city").isNotNull(), col("address.city")
                        ).otherwise(None),
                        when(
                            col("address.street").isNotNull(), col("address.street")
                        ).otherwise(None),
                        when(
                            col("address.house").isNotNull(),
                            concat(lit("д. "), col("address.house")),
                        ).otherwise(None),
                        when(
                            col("address.porch").isNotNull(),
                            concat(lit("под. "), col("address.porch")),
                        ).otherwise(None),
                        when(
                            col("address.floor").isNotNull(),
                            concat(lit("эт. "), col("address.floor")),
                        ).otherwise(None),
                        when(
                            col("address.flat").isNotNull(),
                            concat(lit("кв. "), col("address.flat")),
                        ).otherwise(None),
                    )
                )
            ),
        )

        df_profiles = (
            df_profiles.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("middle_name"), col("last_name")),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("updated_at"), col("created_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select("user_id", "names", "emails", "phones", "actuality")
        )

        df_customers = (
            df_customers.withColumn("sex", sex_udf(col("gender")))
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%Y-%m-%d")))
            .withColumn(
                "company_address", address_udf(col("legal_info_company_address"))
            )
            .withColumn(
                "accounts",
                when(
                    col("id").isNotNull(),
                    array(
                        struct(
                            lit("Ашан").alias("title"),
                            lit("https://www.auchan.ru").alias("link"),
                            col("id").alias("id"),
                            col("loyalty_number").alias("client_card_number"),
                        )
                    ),
                ),
            )
            .select("id", "user_id", "sex", "birth_date", "company_address", "accounts")
        )

        df = df_profiles.join(df_customers, "user_id", "left").join(
            df_customer_addresses,
            df_customer_addresses.customer_id == df_customers.id,
            "left",
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
                "address",
                when(
                    size(
                        array_distinct(
                            array_compact(array(col("address"), col("company_address")))
                        )
                    )
                    > 0,
                    array_distinct(
                        array_compact(array(col("address"), col("company_address")))
                    ),
                ).otherwise(None),
            )
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "sex",
            "birth_date",
            "address",
            "accounts",
            "actuality",
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
