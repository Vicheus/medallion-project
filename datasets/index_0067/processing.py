from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    collect_set,
    first,
    coalesce,
    array_compact,
    size,
    max,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    email_udf,
    phone_udf,
    birth_date_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0067"

    def parser(self):
        df1 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0067/raw/sushi-master.ru/sushi-master.ru_09.2022_(852.062).txt",
            sep="\t",
            header=True,
        )
        df2 = self.read(
            path="/media/user/SAMSUNG/Databases/index_0067/raw/sushi-master.ru/sushi-master.ru_orders_09.2022_(2.684.788).txt",
            sep="\t",
            header=True,
        )

        df1 = (
            df1.withColumn("names", name_udf(col("firstName")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", birth_date_udf(col("birthday"), lit("%d.%m.%Y")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updateTime"), lit("%Y-%m-%d %H:%M:%S.%f")),
            )
        )
        df1 = df1.select("names", "emails", "phones", "birth_date", "actuality")

        df2 = (
            df2.withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("birth_date", lit(None))
            .withColumn("actuality", lit(None))
        )
        df2 = df2.select("names", "emails", "phones", "birth_date", "actuality")

        df = df1.unionAll(df2)

        df = df.dropDuplicates(["names", "emails", "phones"])

        df = df.filter(
            col("names").isNotNull()
            & (col("emails").isNotNull() | col("phones").isNotNull())
        )

        df = df.groupBy(["phones", "names"]).agg(
            array_compact(collect_set("emails")).alias("emails"),
            first(coalesce("birth_date")).alias("birth_date"),
            max("actuality").alias("actuality"),
        )

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
