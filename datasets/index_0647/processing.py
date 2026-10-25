from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    lit,
    array_compact,
    size,
    array_distinct,
    coalesce,
)


from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0647"
    calc_completeness: bool = True

    def parser(self):
        df = (
            self.read(
                path="/home/user/Documents/data/index_0647/raw/Filterix - @StormBaseAdapter.csv",
                sep="\t",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("NAME"), col("LAST_NAME"), lit(None))
            )
            .withColumn("emails", email_udf(col("EMAIL")))
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("PERSONAL_PHONE")),
                            phone_udf(col("PERSONAL_MOBILE")),
                        )
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("LAST_LOGIN"), col("DATE_REGISTER")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select("names", "emails", "phones", "actuality")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
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
                when(
                    size(array_distinct(array_compact(col("phones")))) > 0,
                    array_distinct(array_compact(col("phones"))),
                ).otherwise(None),
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
