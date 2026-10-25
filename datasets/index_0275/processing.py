from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    max,
    array,
    array_distinct,
    array_compact,
    size,
    from_unixtime,
    regexp_replace,
    split,
    flatten,
    collect_set,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    address_udf,
    actuality_date_udf,
    phones_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0275"

    def parser(self):
        df_customers_1 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0275/raw/www.electronpribor.ru/www.electronpribor.ru /preprocessed/customers_1_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "emails", array_distinct(array_compact(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones", array_distinct(array_compact(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("date_add"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("company").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                work_udf(
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    regexp_replace(col("company"), "&quot;", ""),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn("address", array())
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "works",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_customers_2 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0275/raw/www.electronpribor.ru/www.electronpribor.ru /preprocessed/customers_2_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "emails", array_distinct(array_compact(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf(col("contacts")))
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("date_add"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn("works", array())
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("address"))))),
            )
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "works",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_customers_3 = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0275/raw/www.electronpribor.ru/www.electronpribor.ru /preprocessed/orders_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "emails", array_distinct(array_compact(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(phone_udf(col("phone")), phone_udf(col("contacts")))
                    )
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("date_add"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn("works", array())
            .withColumn(
                "address",
                array_compact(array_distinct(array(address_udf(col("address"))))),
            )
            .withColumn(
                "raw_metadata", raw_metadata_udf(lit("comment"), col("comment"))
            )
            .select(
                "names",
                "emails",
                "phones",
                "works",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_users = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0275/raw/www.electronpribor.ru/www.electronpribor.ru /preprocessed/users_preprocessed.csv",
                sep=";",
                header=True,
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "emails", array_distinct(array_compact(array(email_udf(col("email")))))
            )
            .withColumn(
                "phones", array_compact(array_distinct(array(phone_udf(col("phone")))))
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("date_add"), "yyyy-MM-dd HH:mm:ss"),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("name_organization").isNotNull(),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            regexp_replace(col("name_organization"), "&quot;", ""),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("address")),
                            address_udf(col("post_address")),
                        )
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("admin_comment"),
                    col("admin_comment"),
                    lit("requisites"),
                    col("requisites"),
                    lit("yandex_id"),
                    col("yandex_id"),
                    lit("inn_organization"),
                    col("inn_organization"),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "works",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_suppliers = self.read(
            path="/media/user/SAMSUNG/Databases/index_0275/raw/www.electronpribor.ru/www.electronpribor.ru /preprocessed/suppliers_preprocessed.csv",
            sep=";",
            header=True,
        ).filter(
            ~(col("country") == "Украина")
            & ~(col("address").contains("Украина"))
            & ~(col("address2").contains("Украина"))
        )

        df_suppliers_contacts = self.read(
            path="/media/user/SAMSUNG/Databases/index_0275/raw/www.electronpribor.ru/www.electronpribor.ru /preprocessed/suppliers_contacts_preprocessed.csv",
            sep=";",
            header=True,
        )

        df_suppliers_contacts = (
            df_suppliers_contacts.join(
                df_suppliers,
                df_suppliers["id"] == df_suppliers_contacts["supplier_id"],
                "left",
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn(
                "emails",
                array_distinct(
                    array_compact(array(email_udf(df_suppliers_contacts["email"])))
                ),
            )
            .withColumn(
                "phones",
                array_distinct(
                    array_compact(array(phone_udf(df_suppliers_contacts["phone"])))
                ),
            )
            .withColumn(
                "works",
                when(
                    df_suppliers["title_full"].isNotNull(),
                    array(
                        work_udf(
                            df_suppliers_contacts["post"],
                            lit(None),
                            lit(None),
                            regexp_replace(df_suppliers["title_full"], "&quot;", ""),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("address", array())
            .withColumn("actuality", lit(None))
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "works",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_suppliers_as_entities = (
            df_suppliers.withColumn(
                "names",
                name_udf(regexp_replace(df_suppliers["title_full"], "&quot;", "")),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn(
                "phones",
                array_distinct(array_compact(phones_udf(split(col("phones"), ",")))),
            )
            .withColumn("works", array())
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(address_udf(col("address")), address_udf(col("address2")))
                    )
                ),
            )
            .withColumn("actuality", lit(None))
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "works",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df_customers = (
            df_customers_1.unionAll(df_customers_2)
            .unionAll(df_customers_3)
            .unionAll(df_suppliers_contacts)
            .unionAll(df_users)
            .groupBy(["names", "phones", "emails"])
            .agg(
                array_compact(array_distinct(flatten(collect_set(col("works"))))).alias(
                    "works"
                ),
                array_compact(
                    array_distinct(flatten(collect_set(col("address"))))
                ).alias("address"),
                max(col("actuality")).alias("actuality"),
                collect_set(col("raw_metadata")).alias("raw_metadata"),
            )
            .select(
                "names",
                "emails",
                "phones",
                "works",
                "address",
                "actuality",
                "raw_metadata",
            )
        )

        df = df_customers.unionAll(df_suppliers_as_entities)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
