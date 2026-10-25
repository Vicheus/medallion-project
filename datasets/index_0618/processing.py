from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    concat_ws,
    count_distinct,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0618"

    def parser(self):
        df = self.read(
            path="/media/user/T7/datasets/index_0618/raw/Finself.ru_370k_users.csv",
            sep=",",
            header=True,
        )
        df = (
            df.withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("birth_date", birth_date_udf(col("birthdate"), lit("%Y-%m-%d")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address", address_udf(concat_ws(" ", col("address1"), col("address2")))
            )
            .select("names", "birth_date", "sex", "phones", "address")
        )

        valid_df = df.filter(col("phones").isNotNull() & col("names").isNotNull())

        bad_phones = (
            valid_df.groupBy("phones")
            .agg(count_distinct("names").alias("name_cnt"))
            .filter(col("name_cnt") > 1)
            .select("phones")
        )

        df = df.join(bad_phones, on="phones", how="left_anti")

        df.persist(StorageLevel.DISK_ONLY).count()
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
