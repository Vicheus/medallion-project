from pyspark.sql.functions import (
    col,
    lit,
    array,
    regexp_replace,
    array_compact,
    when,
    size,
    array_distinct,
)
from pyspark.sql.types import StructType, StringType

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    birth_date_udf,
    email_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0064"

    def parser(self):
        schema_1 = (
            StructType()
            .add("birth_date", StringType(), True)
            .add("email", StringType(), True)
            .add("first_name", StringType(), True)
            .add("last_name", StringType(), True)
            .add("city", StringType(), True)
            .add("phone", StringType(), True)
            .add("additional_phone", StringType(), True)
        )
        df_1 = self.read(
            path="KupiVIP/KupiVIP.ru 4.2kk.txt", sep=":", header=False, schema=schema_1
        )
        df_1 = (
            df_1.replace("NULL", None)
            .withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(""))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array(phone_udf(col("phone")), phone_udf(col("additional_phone"))),
            )
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn("address", address_udf(col("city")))
            .select("names", "phones", "emails", "birth_date", "address")
        )

        schema_2 = (
            StructType()
            .add("id", StringType(), True)
            .add("birth_date", StringType(), True)
            .add("email", StringType(), True)
            .add("first_name", StringType(), True)
            .add("unknown_field_1", StringType(), True)
            .add("last_name", StringType(), True)
            .add("city", StringType(), True)
            .add("phone", StringType(), True)
            .add("additional_phone", StringType(), True)
            .add("unknown_field_2", StringType(), True)
        )
        df_2 = self.read(
            path="KupiVIP/kupi_vip_*.csv", sep=",", header=False, schema=schema_2
        )
        df_2 = (
            df_2.replace("NULL", None)
            .withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(""))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones",
                array_compact(
                    array(phone_udf(col("phone")), phone_udf(col("additional_phone")))
                ),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(regexp_replace(col("birth_date"), "(')", "")),
            )
            .withColumn("address", address_udf(col("city")))
            .select("names", "phones", "emails", "birth_date", "address")
        )

        df = df_1.unionAll(df_2)
        df.drop_duplicates(["names", "phones", "emails"])
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(array_distinct(col("phones")))) > 0,
                    array_compact(array_distinct(col("phones"))),
                ).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
