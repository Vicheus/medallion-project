from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_distinct,
    array_compact,
    struct,
    size,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    email_udf,
    phone_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0102"

    def parser(self):
        df_clients = self.read(
            path="/media/user/TRANSCEND/Databases/index_0102/raw/MEDCENTR-SITIMED.RU - @bereza_bd/Citymed_Klienty.csv",
            sep="\t",
            header=True,
        )
        df_contragents = self.read(
            path="/media/user/TRANSCEND/Databases/index_0102/raw/MEDCENTR-SITIMED.RU - @bereza_bd/Citymed_Kontragenty.csv",
            sep=";",
            header=True,
        )
        df_users = self.read(
            path="/media/user/TRANSCEND/Databases/index_0102/raw/MEDCENTR-SITIMED.RU - @bereza_bd/Citymed_Polzovateli.csv",
            sep=";",
            header=True,
        )

        df_clients = (
            df_clients.withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%M.%Y"))
            )
            .withColumn("emails", email_udf(col("Email")))
            .withColumn(
                "phones",
                array_compact(array_distinct(array(phone_udf(col("Телефон"))))),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(col("Адрес проживания")),
                            address_udf(col("Адрес регистрации")),
                        )
                    )
                ),
            )
            .withColumn("passport", col("Документ"))
            .withColumn(
                "works",
                when(
                    (col("Организация").isNotNull() | col("Должность").isNotNull()),
                    array(
                        work_udf(
                            col("Должность"),
                            lit(None),
                            lit(None),
                            col("Организация"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "documents",
                when(
                    col("СНИЛС").isNotNull() | col("passport").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("СНИЛС").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("СНИЛС"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ),
                            when(
                                col("passport").isNotNull(),
                                document_udf(
                                    lit("паспорт гражданина рф"),
                                    col("passport"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("accounts", array())
            .select(
                "names",
                "phones",
                "emails",
                "birth_date",
                "address",
                "accounts",
                "works",
                "documents",
            )
        )

        df_contragents = (
            df_contragents.withColumn("names", name_udf(col("Название")))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", lit(None))
            .withColumn("phones", array())
            .withColumn("address", array())
            .withColumn("works", array())
            .withColumn(
                "documents",
                when(
                    col("ИНН").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("ИНН").isNotNull(),
                                document_udf(
                                    lit("инн"),
                                    col("ИНН"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn("accounts", array())
            .select(
                "names",
                "phones",
                "emails",
                "birth_date",
                "address",
                "accounts",
                "works",
                "documents",
            )
        )

        df_users = (
            df_users.withColumn("names", name_udf(col("ФИО")))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", array_compact(array(phone_udf("Телефон"))))
            .withColumn("address", array())
            .withColumn(
                "works",
                when(
                    (col("Должность").isNotNull()),
                    array(
                        work_udf(
                            col("Должность"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn("documents", array())
            .withColumn(
                "accounts",
                when(
                    col("Логин").isNotNull(),
                    array(
                        struct(
                            lit("Медцентр Ситимед").alias("title"),
                            lit("http://medcentr-sitimed.ru").alias("link"),
                            col("Логин").alias("login"),
                        )
                    ),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "birth_date",
                "address",
                "accounts",
                "works",
                "documents",
            )
        )

        df = (
            df_clients.unionAll(df_contragents)
            .unionAll(df_users)
            .select(
                "names",
                "phones",
                "emails",
                "birth_date",
                "address",
                "accounts",
                "works",
                "documents",
            )
        )

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
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(size(col("accounts")) > 0, col("accounts")).otherwise(None),
            )
            .withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
        )

        df = df.select(
            "names",
            "phones",
            "emails",
            "birth_date",
            "address",
            "accounts",
            "works",
            "documents",
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
