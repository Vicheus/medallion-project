from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array_compact,
    size,
    array,
    concat_ws,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0544"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        df_users = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0544/raw/rdsshop/users*.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", array_compact(array(name_udf("Имя"))))
            .withColumn("address", array())
            .withColumn("emails", array_compact(array(email_udf(col("Email")))))
            .withColumn("phones", array_compact(array(phone_udf(col("Телефон")))))
            .withColumn("actuality", lit(None))
            .select("names", "address", "emails", "phones", "actuality")
        )

        df_orders = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0544/raw/rdsshop/order*.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", array_compact(array(name_udf("client_name"))))
            .withColumn(
                "address",
                array(address_udf(concat_ws(" ", col("town"), col("delivery")))),
            )
            .withColumn("emails", array())
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .withColumn("actuality", actuality_date_udf(col("date"), lit("%d.%m.%Y")))
            .select("names", "address", "emails", "phones", "actuality")
        )

        df = df_users.unionAll(df_orders)
        df = df.drop_duplicates(["phones"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names",
                when(size(col("names")) > 0, col("names")).otherwise(None),
            )
            .withColumn(
                "emails",
                when(size(col("emails")) > 0, col("emails")).otherwise(None),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(size(col("phones")) > 0, col("phones")).otherwise(None),
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
