from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, struct, concat_ws

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    address_udf,
    phone_udf,
    actuality_date_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    output_file_count: 1
    dataset_code_name: str = "index_0016"

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0016/raw/Pochta.ru_2022_10kk/pochta_orders1.csv",
            sep="\t",
        )

        df_sndr = df.select(
            "rpo_sndr_name", "rpo_inn_ccode", "accept_local_dts"
        ).filter(col("rpo_inn_ccode").isNotNull() & col("rpo_sndr_name").isNotNull())

        df_sndr = (
            df_sndr.withColumn("names", name_udf(col("rpo_sndr_name")))
            .withColumn(
                "documents",
                when(
                    col("rpo_inn_ccode").isNotNull(),
                    array(
                        struct(
                            lit(1).alias("type"),
                            lit("RUS").alias("country"),
                            col("rpo_inn_ccode").alias("serial"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("phones", lit(None))
            .withColumn("address", lit(None))
        ).withColumn(
            "actuality",
            actuality_date_udf(col("accept_local_dts"), lit("%Y-%m-%d %H:%M:%S.%f")),
        )

        df_sndr = df_sndr.select(
            "names", "phones", "address", "documents", "actuality"
        ).filter(col("names").isNotNull() & col("documents").isNotNull())
        df_sndr.show(n=20, truncate=False)

        df_sndr.persist(StorageLevel.DISK_ONLY).count()

        df_rcpn = (
            df.withColumn("names", name_udf(col("rpo_rcpn_name")))
            .withColumn("phones", phone_udf(col("rpo_rcpn_phone_ccode")))
            .withColumn(
                "address",
                address_udf(
                    concat_ws(
                        ", ",
                        when(
                            col("index_to_ccode").isNotNull(), col("index_to_ccode")
                        ).otherwise(None),
                        when(
                            col("settlement_to_name").isNotNull(),
                            col("settlement_to_name"),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn("documents", lit(None))
        ).withColumn(
            "actuality",
            actuality_date_udf(col("accept_local_dts"), lit("%Y-%m-%d %H:%M:%S.%f")),
        )

        df_rcpn = df_rcpn.select(
            "names", "phones", "address", "documents", "actuality"
        ).filter(col("names").isNotNull() & col("phones").isNotNull())
        df_rcpn = df_rcpn.dropDuplicates(["phones"])
        df_rcpn.show(n=20, truncate=False)

        df_rcpn.persist(StorageLevel.DISK_ONLY).count()

        df = df_sndr.union(df_rcpn)
        df = (
            df.withColumn("names", array(col("names")))
            .withColumn("phones", array(col("phones")))
            .withColumn("address", array(col("address")))
        )
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
