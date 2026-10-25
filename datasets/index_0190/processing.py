from pyspark import StorageLevel
from pyspark.sql.functions import when, col, array, coalesce

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import email_udf, name_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0190"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0190/raw/smf_members.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("member_name")))
            .withColumn("emails", email_udf(col("email_address")))
            .select("names", "emails")
        )
        df2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0190/raw/tutby_users.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("login")))
            .withColumn("emails", email_udf(col("email")))
            .select("names", "emails")
        )
        df3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0190/raw/user.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("username")))
            .withColumn("emails", email_udf(col("email")))
            .select("names", "emails")
        )
        df4 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0190/raw/users.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("login")))
            .withColumn("emails", email_udf(col("email")))
            .select("names", "emails")
        )
        df5 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0190/raw/users_1.csv",
                sep=":",
                header=True,
            )
            .withColumn("names", name_udf(col("login")))
            .withColumn("emails", email_udf(col("email")))
            .select("names", "emails")
        )
        df6 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0190/raw/vodila_users.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(coalesce(col("nickname"), col("login"))))
            .withColumn("emails", email_udf(col("email")))
            .select("names", "emails")
        )

        df = df1.unionAll(df2).unionAll(df3).unionAll(df4).unionAll(df5).unionAll(df6)

        df = df.drop_duplicates()

        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "emails",
            when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(col("names").isNotNull() & col("emails").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
