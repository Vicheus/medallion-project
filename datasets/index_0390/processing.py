from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    array_distinct,
    lit,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0390"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0390/raw/superkopilka.csv",
            sep=";",
            header=True,
        )
        df = (
            df.withColumn(
                "names", name_parts_udf(col("FirstName"), col("LastName"), lit(None))
            )
            .withColumn(
                "emails", array_compact(array_distinct(array(email_udf(col("Email")))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("Phone")))))
            )
            .withColumn("address", address_udf(col("City")))
            .withColumn("birth_date", birth_date_udf(col("BirthDate"), lit("%d.%m.%Y")))
            .withColumn("sex", sex_udf(col("Sex")))
            .select("names", "emails", "phones", "address", "sex", "birth_date")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
