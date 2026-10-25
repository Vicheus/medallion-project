from pyspark import StorageLevel
from pyspark.sql.functions import col, array, concat_ws, when
from pyspark.sql.types import StringType, StructType

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, address_udf, email_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0121"

    def parser(self):
        schema = (
            StructType()
            .add("name", StringType(), True)
            .add("email", StringType(), True)
            .add("phone", StringType(), True)
            .add("city", StringType(), True)
            .add("address1", StringType(), True)
            .add("address2", StringType(), True)
            .add("address3", StringType(), True)
            .add("address4", StringType(), True)
            .add("address5", StringType(), True)
        )
        df = self.read(
            path="/media/user/TRANSCEND/Databases/index_0121/raw/onona_ru_2022.csv",
            sep=",",
            header=False,
            schema=schema,
        )

        df = (
            df.filter(~col("phone").startswith("38"))
            .replace("NULL", None)
            .replace("-", None)
            .withColumn("names", name_udf(col("name")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        " ",
                        col("city"),
                        col("address1"),
                        col("address2"),
                        col("address3"),
                        col("address4"),
                        col("address5"),
                    )
                ),
            )
            .select("names", "phones", "emails", "address")
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
