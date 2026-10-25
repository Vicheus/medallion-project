from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    struct,
    array,
    array_distinct,
    size,
    flatten,
    collect_set,
)
from pyspark.sql.types import StringType, StructField, StructType

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0208"

    def parser(self):
        users_schema = StructType(
            [
                StructField("user_id", StringType(), True),
                StructField("username", StringType(), True),
                StructField("first_name", StringType(), True),
                StructField("last_name", StringType(), True),
            ]
        )
        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0208/raw/Mirtesen.ru/Mirtesen.csv",
                sep=",",
                header=False,
                schema=users_schema,
            )
            .replace("NULL", None)
            .select("user_id", "first_name", "last_name")
        )

        ip_schema = StructType(
            [
                StructField("user_id", StringType(), True),
                StructField("ip", StringType(), True),
            ]
        )
        df_ips = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0208/raw/Mirtesen.ru/MT.ips.csv",
                sep="\t",
                header=False,
                schema=ip_schema,
            )
            .replace("NULL", None)
            .select("user_id", "ip")
        )

        df_phones = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0208/raw/Mirtesen.ru/MT.phone_verification.csv",
                sep="\t",
                header=True,
            )
            .replace("NULL", None)
            .select("obj_person_obj_id", "person_phone_number")
        )

        df = (
            df_users.join(
                df_phones,
                df_users["user_id"] == df_phones["obj_person_obj_id"],
                "inner",
            )
            .join(df_ips, df_users["user_id"] == df_ips["user_id"], "left")
            .select("first_name", "last_name", "person_phone_number", "ip")
        )

        df = (
            df.withColumn(
                "names", name_parts_udf(col("first_name"), col("last_name"), lit(None))
            )
            .withColumn("phones", phone_udf(col("person_phone_number")))
            .withColumn("ip_address", ip_address_udf(col("ip")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(struct(col("ip_address").alias("ip"))),
                ),
            )
            .select("names", "phones", "ips")
        )

        df = df.groupBy(["phones", "names"]).agg(
            array_distinct(flatten(collect_set("ips"))).alias("ips")
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
            .withColumn("ips", when(size(col("ips")) > 0, col("ips")).otherwise(None))
        )

        df = df.filter(col("names").isNotNull() & col("phones").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
