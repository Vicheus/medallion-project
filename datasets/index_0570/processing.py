from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    size,
    concat_ws,
    collect_list,
    trim,
    lower,
    concat,
    flatten,
    max,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)
from parsetron.settings import DATASET_COUNTRY_CODE


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0570"
    validate_invalid_groupping: bool = True
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

    def parser(self):
        EMAILS_TO_IGNORE = ["info@monochromeyou.ru"]
        df_orders = (
            (
                self.read(
                    path="/home/user/Documents/data/index_0564/raw/MONOCHROME/order*.csv",
                    sep=",",
                    header=True,
                )
            )
            .replace("NULL", None)
            .filter(
                (
                    lower(trim(col("country"))).isin(
                        [
                            "ресрублика беларусь",
                            "республинка беларусь",
                            "республика беларусь",
                            "рб",
                            "беларусь",
                            "by",
                            "belarus",
                        ]
                    )
                    | (
                        col("country").isNull()
                        & (
                            col("phone").startswith("+37")
                            | col("phone").startswith("37")
                        )
                    )
                )
                & ~(col("email").isin(EMAILS_TO_IGNORE))
            )
        )

        df_orders = (
            df_orders.withColumn(
                "names", name_parts_udf(col("name"), col("surname"), lit(None))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "phones", phone_udf(col("phone"), lit(self.dataset_country_code.value))
            )
            .withColumn(
                "address_str",
                when(
                    col("city").isNotNull(),
                    concat_ws(
                        ", ",
                        when(
                            col("postcode") != "",
                            col("postcode"),
                        ).otherwise(None),
                        when(
                            col("country") != "",
                            col("country"),
                        ).otherwise(None),
                        col("city"),
                        when(
                            col("street") != "",
                            concat(lit("ул. "), col("street")),
                        ).otherwise(None),
                        when(
                            col("house") != "",
                            concat(lit("д. "), col("house")),
                        ).otherwise(None),
                        when(
                            col("building") != "", concat(lit("стр. "), col("building"))
                        ).otherwise(None),
                        when(
                            col("building") != "",
                            concat(lit("кв. "), col("building")),
                        ).otherwise(None),
                    ),
                ),
            )
            .withColumn("address", address_udf(col("address_str")))
            .withColumn(
                "actuality",
                actuality_date_udf(col("updated_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("comment_a"),
                    col("comment_a"),
                    lit("comment"),
                    col("comment"),
                ),
            )
            .select(
                "user_id",
                "names",
                "emails",
                "phones",
                "address",
                "raw_metadata",
                "actuality",
            )
        )

        df_orders = (
            df_orders.withColumn("names", array_compact(array(col("names"))))
            .withColumn("emails", array_compact(array(col("emails"))))
            .withColumn("phones", array_compact(array(col("phones"))))
            .withColumn("address", array_compact(array(col("address"))))
            .withColumn("raw_metadata", array_compact(array(col("raw_metadata"))))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_orders

        df = df.filter(
            col("names").isNotNull()
            & (
                (col("phones").isNotNull() & (size(col("phones")) > 0))
                | (col("emails").isNotNull() & (size(col("emails")) > 0))
            )
        )

        df = (
            df.groupBy(["emails", "phones"])
            .agg(
                array_compact(
                    array_distinct(flatten(collect_list(col("names"))))
                ).alias("names"),
                array_compact(
                    array_distinct(flatten(collect_list(col("address"))))
                ).alias("address"),
                array_compact(
                    array_distinct(flatten(collect_list(col("raw_metadata"))))
                ).alias("raw_metadata"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "raw_metadata",
                "actuality",
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "names", when(size(col("names")) > 0, col("names")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
        )

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
