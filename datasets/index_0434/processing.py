from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    array_distinct,
    transform,
    from_json,
    concat,
    size,
    split,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    address_udf,
    phones_udf,
    email_udf,
    actuality_date_udf,
)
from pyspark.sql.types import ArrayType, StructType, StructField, StringType


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0434"
    calc_completeness: bool = False

    def parser(self):
        add_phones_schema = ArrayType(
            StructType(
                [
                    StructField("phone", StringType(), True),
                    StructField("additional_number", StringType(), True),
                    StructField("name", StringType(), True),
                ]
            )
        )
        df_clients = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0434/raw/pm.ru - @StormBaseAdapter/pm.ru/clients.csv",
            sep=";",
        )

        df_clients = (
            df_clients.withColumn(
                "names",
                name_udf(col("title")),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "add_phones",
                transform(
                    from_json(col("additional_phones"), add_phones_schema),
                    lambda x: x.phone,
                ),
            )
            .withColumn(
                "phones", phones_udf(concat(array(col("phone")), col("add_phones")))
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("registration_date"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn("address", array())
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "actuality",
            )
        )

        df_orders = self.read(
            path="/media/user/SAMSUNG BACKUP/indexes/index_0434/raw/pm.ru - @StormBaseAdapter/pm.ru/orders.csv",
            sep=";",
        )

        df_orders = (
            df_orders.withColumn(
                "names",
                name_udf(col("name")),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phones_udf(split(col("phone"), ",")))
            .withColumn("actuality", lit(None))
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("raw_address")),
                            address_udf(col("raw_address")),
                        )
                    )
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "actuality",
            )
        )

        df = df_clients.unionAll(df_orders)

        df = df.drop_duplicates(["phones", "emails"])

        df_clients = (
            df_clients.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(), array_compact(array(col("emails")))
                ).otherwise(None),
            )
        )

        df_clients = df_clients.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df_clients.persist(StorageLevel.DISK_ONLY).count()

        return df_clients


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
