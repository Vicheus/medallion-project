from pyspark import StorageLevel
from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    array,
    size,
    array_distinct,
    array_compact,
    collect_list,
    flatten,
    lit,
    coalesce,
    max,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0099"

    def read_yapdomik_df(self, path, city_name):
        df = self.read(path=path, sep=",", header=True)
        df = (
            df.withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "address",
                array_distinct(
                    array_compact(
                        array(
                            when(
                                col("address").isNotNull() & (col("address") != ""),
                                address_udf(
                                    concat_ws(" ", lit(city_name), col("address"))
                                ),
                            ).otherwise(None),
                            when(
                                col("address_pickup").isNotNull()
                                & (col("address_pickup") != ""),
                                address_udf(
                                    concat_ws(
                                        " ", lit(city_name), col("address_pickup")
                                    )
                                ),
                            ).otherwise(None),
                        )
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("price"),
                    df["price"],
                    lit("date_delivery"),
                    df["date_delivery"],
                    lit("comment"),
                    df["comment"],
                    lit("count_person"),
                    df["count_person"],
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("date_add"), col("date_complete")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
        )

        df = df.groupBy(["phones", "names"]).agg(
            array_distinct(flatten(collect_list("address"))).alias("address"),
            collect_set("raw_metadata").alias("raw_metadata"),
            max("actuality").alias("actuality"),
        )

        df = (
            df.withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
        )

        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        return df

    def parser(self):
        df1 = self.read_yapdomik_df(
            "/media/user/SAMSUNG/Databases/index_0099/raw/Yapdomik.ru_2022_986k_Cleaned/Yapdomik.ru_Achinsk_2022_63k.csv",
            "Ачинск",
        )
        df2 = self.read_yapdomik_df(
            "/media/user/SAMSUNG/Databases/index_0099/raw/Yapdomik.ru_2022_986k_Cleaned/Yapdomik.ru_Berdsk_2022_54k.csv",
            "Бердск",
        )
        df3 = self.read_yapdomik_df(
            "/media/user/SAMSUNG/Databases/index_0099/raw/Yapdomik.ru_2022_986k_Cleaned/Yapdomik.ru_Krasnoyarsk_2022_187k.csv",
            "Красноярск",
        )
        df4 = self.read_yapdomik_df(
            "/media/user/SAMSUNG/Databases/index_0099/raw/Yapdomik.ru_2022_986k_Cleaned/Yapdomik.ru_Novosibirsk_2022_94k.csv",
            "Новосибирск",
        )
        df5 = self.read_yapdomik_df(
            "/media/user/SAMSUNG/Databases/index_0099/raw/Yapdomik.ru_2022_986k_Cleaned/Yapdomik.ru_Omsk_2022_588k.csv",
            "Омск",
        )

        df = df1.unionAll(df2).unionAll(df3).unionAll(df4).unionAll(df5)

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
