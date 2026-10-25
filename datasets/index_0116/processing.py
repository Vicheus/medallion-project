from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    size,
    concat_ws,
    array_distinct,
    coalesce,
    from_unixtime,
    greatest,
)

from parsetron import Parsetron
from parsetron.sections.ips.udfs import ip_address_udf, ip_date_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    birth_date_udf,
    address_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0116"
    calc_completeness: bool = False

    def parser(self):
        df = self.read(
            path="/media/user/SAMSUNG/Databases/index_0116/raw/wineStyle_2.csv",
            sep=",",
            header=True,
        ).select(
            "orddate",
            "ordbillfirstname",
            "ordbilllastname",
            "ordbillmiddlename",
            "ordbillbirthday",
            "ordbillstreet1",
            "ordbillstreet2",
            "ordbillstate",
            "ordbillzip",
            "ordbillcountry",
            "ordbillphone",
            "ordbillemail",
            "ordshipfirstname",
            "ordshiplastname",
            "ordshipmiddlename",
            "ordshipbirthday",
            "ordshipstreet1",
            "ordshipstreet2",
            "ordshipstate",
            "ordshipzip",
            "ordshipcountry",
            "ordshipphone",
            "ordshipemail",
            "ordipaddress",
            "ordbyphone",
            "orderid",
            "ordtotalamount",
            "ordbillcompany",
            "dateclientlastorder",
        )

        df = (
            df.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("ordbillfirstname"),
                                col("ordbilllastname"),
                                col("ordbillmiddlename"),
                            ),
                            name_parts_udf(
                                col("ordshipfirstname"),
                                col("ordshiplastname"),
                                col("ordshipmiddlename"),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("ordbillphone")),
                            phone_udf(col("ordshipphone")),
                            phone_udf(col("ordbyphone")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(
                            email_udf(col("ordshipemail")),
                            email_udf(col("ordbillemail")),
                        )
                    )
                ),
            )
            .withColumn(
                "birth_date",
                birth_date_udf(
                    coalesce(col("ordbillbirthday"), col("ordshipbirthday")),
                    lit("%Y-%M-%d"),
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("ordbillstreet1").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        when(
                                            col("ordbillcountry") != "",
                                            col("ordbillcountry"),
                                        ).otherwise(None),
                                        when(
                                            col("ordbillzip") != "", col("ordbillzip")
                                        ).otherwise(None),
                                        col("ordbillstreet1"),
                                        col("ordbillstreet2"),
                                    ),
                                ).otherwise(None)
                            ),
                            address_udf(
                                when(
                                    col("ordshipstreet1").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        when(
                                            col("ordshipcountry") != "",
                                            col("ordshipcountry"),
                                        ).otherwise(None),
                                        when(
                                            col("ordshipzip") != "", col("ordshipzip")
                                        ).otherwise(None),
                                        col("ordshipstreet1"),
                                        col("ordshipstreet2"),
                                    ),
                                ).otherwise(None)
                            ),
                        )
                    )
                ),
            )
            .withColumn("ip_address", ip_address_udf(col("ordipaddress")))
            .withColumn(
                "ips",
                when(
                    col("ip_address").isNotNull(),
                    array(
                        struct(
                            col("ip_address").alias("ip"),
                            ip_date_udf(
                                from_unixtime(col("orddate")), lit("%Y-%m-%d %H:%M:%S")
                            ).alias("date"),
                        )
                    ),
                ).otherwise(array()),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    greatest(
                        from_unixtime(col("orddate")),
                        lit("%Y-%m-%d %H:%M:%S"),
                        from_unixtime(col("dateclientlastorder")),
                        lit("%Y-%m-%d %H:%M:%S"),
                    ),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("orderid"),
                    col("orderid"),
                    lit("ordtotalamount"),
                    col("ordtotalamount"),
                    lit("ordbillcompany"),
                    col("ordbillcompany"),
                ),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(array_distinct(col("names")))) > 0,
                    array_compact(array_distinct(col("names"))),
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(array_distinct(col("emails")))) > 0,
                    array_compact(array_distinct(col("emails"))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(array_distinct(col("phones")))) > 0,
                    array_compact(array_distinct(col("phones"))),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(array_distinct(col("address")))) > 0,
                    array_compact(array_distinct(col("address"))),
                ).otherwise(None),
            )
            .withColumn(
                "ips",
                when(
                    size(array_compact(array_distinct(col("ips")))) > 0,
                    array_compact(array_distinct(col("ips"))),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select(
            "names",
            "birth_date",
            "emails",
            "phones",
            "ips",
            "address",
            "actuality",
            "raw_metadata",
        )

        df.show(n=10, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
