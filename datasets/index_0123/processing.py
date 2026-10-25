from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    struct,
    array_compact,
    concat,
    size,
    concat_ws,
    array_distinct,
    regexp_replace,
)

from parsetron import Parsetron
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    name_udf,
    address_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0123"

    def parser(self):
        df_1 = self.read(
            path="/media/user/TRANSCEND/Databases/index_0123/raw/user_info_1_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_2 = self.read(
            path="/media/user/TRANSCEND/Databases/index_0123/raw/user_info_2_preprocessed.csv",
            sep=";",
            header=True,
        )
        df_3 = self.read(
            path="/media/user/TRANSCEND/Databases/index_0123/raw/user_info_3_preprocessed.csv",
            sep=";",
            header=True,
        )

        df = (
            df_2.join(df_1, on="USER_ID", how="left")
            .join(df_3, on="USER_ID", how="left")
            .replace("-Не Указано-", "")
            .replace("Не Указано", "")
        )
        df = (
            df.withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf(
                                col("first_name"), col("last_name"), col("middle_name")
                            ),
                            name_udf(col("name2")),
                        )
                    )
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(col("username")),
                            phone_udf(col("phone")),
                            phone_udf(col("phone2")),
                            phone_udf(col("phone3")),
                            phone_udf(col("phone4")),
                        )
                    )
                ),
            )
            .withColumn(
                "emails",
                array_compact(
                    array_distinct(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%M-%d"))
            )
            .withColumn(
                "accounts",
                array(
                    struct(
                        lit("Аптека Невис").alias("title"),
                        lit("https://aptekanevis.ru/").alias("link"),
                        regexp_replace(col("username"), "\\+", "").alias("login"),
                        col("password_hash").alias("password_hash"),
                        col("client_card_number").alias("client_card_number"),
                    )
                ),
            )
            .withColumn(
                "educations",
                when(
                    col("education").isNotNull(),
                    array_compact(
                        array(
                            education_udf(
                                lit(None),
                                col("education"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    (col("job").isNotNull()),
                    array_compact(
                        array(
                            work_udf(
                                col("job"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "coordinates",
                when(
                    (
                        col("address_longitude").isNotNull()
                        & (col("address_longitude") != 0.0)
                        & col("address_latitude").isNotNull()
                        & (col("address_latitude") != 0.0)
                    ),
                    array(
                        array(
                            col("address_longitude").cast("float"),
                            col("address_latitude").cast("float"),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                when(
                                    col("address").isNotNull(),
                                    concat_ws(
                                        ", ",
                                        col("address"),
                                        when(
                                            col("flat") != "",
                                            concat(lit("кв. "), col("flat")),
                                        ).otherwise(None),
                                    ),
                                ).otherwise(None)
                            ),
                        )
                    )
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "birth_date",
                "works",
                "educations",
                "accounts",
                "coordinates",
            )
        )

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    size(array_compact(col("emails"))) > 0, array_compact(col("emails"))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
                ).otherwise(None),
            )
            .withColumn(
                "educations",
                when(
                    size(array_compact(col("educations"))) > 0,
                    array_compact(col("educations")),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    size(array_compact(col("accounts"))) > 0,
                    array_compact(col("accounts")),
                ).otherwise(None),
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df = df.select(
            "names",
            "emails",
            "phones",
            "address",
            "sex",
            "birth_date",
            "works",
            "educations",
            "accounts",
            "coordinates",
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
