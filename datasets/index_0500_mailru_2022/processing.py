from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    email_udf,
    phone_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0500_mailru_2022"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/home/user/Downloads/Sharing/mail.ru - @StormBaseAdapter/xaa.csv",
            sep=",",
        )

        df = (
            df.withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf((col("phone"))))
            .select(
                "emails",
                "phones",
            )
        )

        df = df.drop_duplicates(["emails", "phones"])

        df = df.withColumn(
            "phones",
            when(
                col("phones").isNotNull(), array_compact(array(col("phones")))
            ).otherwise(None),
        ).withColumn(
            "emails",
            when(
                col("emails").isNotNull(), array_compact(array(col("emails")))
            ).otherwise(None),
        )

        df = df.filter(col("phones").isNotNull() & col("emails").isNotNull())

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
