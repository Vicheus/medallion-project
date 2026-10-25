from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    array,
    array_compact,
    size,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    names_udf,
    phone_udf,
    email_udf,
    validate_name_is_person_or_organisation_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0344"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0344/raw/клиенты_Infobiz_ru.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names",
                names_udf(
                    validate_name_is_person_or_organisation_udf(
                        array_compact(array(col("Имя")))
                    )
                ),
            )
            .withColumn("emails", email_udf(col("Почта")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .select("names", "emails", "phones")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
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
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
