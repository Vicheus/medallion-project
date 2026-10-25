from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    array_distinct,
)
from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    actuality_date_udf,
)
from parsetron.sections.socials.udfs import social_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0542"
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG BACKUP/indexes/index_0542/raw/data.csv",
                sep=",",
                header=True,
            )
            .withColumn("names", name_udf(col("Наименование")))
            .withColumn(
                "phones", phone_udf(col("Телефон"), lit(self.dataset_country_code))
            )
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "socials",
                array_compact(
                    array(
                        when(
                            col("Instagram_WZ (контакт)").isNotNull()
                            & (col("Instagram_WZ (контакт)") != ""),
                            social_udf(
                                lit("Instagram"),
                                lit(None),
                                col("Instagram_WZ (контакт)"),
                                lit(None),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(col("Дата создания"), lit("%d.%m.%Y %H:%M")),
            )
            .select("names", "phones", "emails", "socials", "actuality")
        )

        df.show(n=20, truncate=False)

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
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "socials",
                when(
                    size(array_compact(array_distinct(col("socials")))) > 0,
                    array_compact(array_distinct(col("socials"))),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("socials").isNotNull()
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
