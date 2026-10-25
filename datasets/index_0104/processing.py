from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, array, array_compact, size, concat_ws

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.main.udfs import (
    name_parts_udf,
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    relations_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0104"

    def parser(self):
        df_child_parent = self.read(
            path="/media/user/SAMSUNG/Databases/index_0104/raw/child-747820.json",
            sep="\n",
            header=False,
        ).filter((col("_source.citizenship.title") == "Россия"))
        df_users = self.read(
            path="/media/user/SAMSUNG/Databases/index_0104/raw/user-755799.json",
            sep="\t",
            header=True,
        )

        df_child = (
            df_child_parent.filter((col("_source.citizenship.title") == "Россия"))
            .withColumn("id", col("_id"))
            .withColumn("address", col("_source.address.addressString"))
            .withColumn("birthDate", col("_source.birthDate"))
            .withColumn("citizenship", col("_source.citizenship.title"))
            .withColumn("email", col("_source.email"))
            .withColumn("phone", col("_source.phone"))
            .withColumn("firstName", col("_source.firstName"))
            .withColumn("middleName", col("_source.email"))
            .withColumn("lastName", col("_source.lastName"))
            .withColumn("gender", col("_source.gender"))
            .withColumn("passport", col("_source.passport"))
            .withColumn("passportDate", col("_source.passportDate"))
            .withColumn("parentEmail", col("_source.parentEmail"))
            .withColumn("parentPhone", col("_source.parentPhone"))
            .withColumn("parentFIO", col("_source.parentFIO"))
            .withColumn("snils", col("_source.snils"))
            .withColumn("school", concat_ws(" ", col("_source.school.title")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("clothesSize"),
                    col("_source.clothesSize.title"),
                    lit("disabilityGroup"),
                    col("_source.disabilityGroup.title"),
                    lit("healthGroup"),
                    col("_source.healthGroup.title"),
                    lit("otherOrgInfo"),
                    col("_source.otherOrgInfo"),
                    lit("youngArmyInfo"),
                    col("_source.youngArmyInfo"),
                    lit("hobby"),
                    col("_source.hobby"),
                ),
            )
            .select(
                "id",
                "address",
                "birthDate",
                "citizenship",
                "email",
                "phone",
                "firstName",
                "lastName",
                "middleName",
                "gender",
                "passport",
                "passportDate",
                "parentFIO",
                "parentEmail",
                "parentPhone",
                "snils",
                "school",
                "raw_metadata",
            )
        )

        df_child = (
            df_child.withColumn(
                "names", name_parts_udf(col("firstName"), col("lastName"), lit(None))
            )
            .withColumn("address", address_udf(col("address")))
            .withColumn(
                "birth_date", birth_date_udf(col("birthDate"), lit("%Y-%m-%dT%H:%M:%S"))
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("sex", sex_udf(col("gender")))
            .withColumn(
                "relations",
                when(
                    col("parentFIO").isNotNull(),
                    array(
                        relations_udf(
                            concat_ws(
                                " ",
                                col("parentFIO"),
                                col("parentEmail"),
                                col("parentPhone"),
                                lit("Родитель"),
                            )
                        )
                    ),
                ).otherwise(array()),
            )
            .withColumn(
                "documents",
                when(
                    col("passport").isNotNull() | col("snils").isNotNull(),
                    array_compact(
                        array(
                            when(
                                col("passport").isNotNull(),
                                document_udf(
                                    lit(None),
                                    col("passport"),
                                    col("passportDate"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                            when(
                                col("snils").isNotNull(),
                                document_udf(
                                    lit("снилс"),
                                    col("snils"),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit(None),
                                    lit("yyyy-MM-dd"),
                                ),
                            ).otherwise(None),
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "educations",
                when(
                    col("school").isNotNull() & (col("school") != ""),
                    array_compact(
                        array(
                            education_udf(
                                col("school"),
                                lit("Среднее"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                            )
                        )
                    ),
                ),
            )
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "relations",
                "birth_date",
                "documents",
                "educations",
                "raw_metadata",
            )
        )

        df_parent = (
            df_child_parent.filter(
                (col("_source.citizenship.title") == "Россия")
                & col("_source.parentFIO").isNotNull()
            )
            .withColumn("birthDate", col("_source.birthDate"))
            .withColumn("email", col("_source.email"))
            .withColumn("firstName", col("_source.firstName"))
            .withColumn("middleName", col("_source.email"))
            .withColumn("lastName", col("_source.lastName"))
            .withColumn("parentEmail", col("_source.parentEmail"))
            .withColumn("parentPhone", col("_source.parentPhone"))
            .withColumn("parentFIO", col("_source.parentFIO"))
            .withColumn("phone", col("_source.phone"))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("clothesSize"),
                    col("_source.clothesSize.title"),
                    lit("disabilityGroup"),
                    col("_source.disabilityGroup.title"),
                    lit("healthGroup"),
                    col("_source.healthGroup.title"),
                    lit("otherOrgInfo"),
                    col("_source.otherOrgInfo"),
                    lit("youngArmyInfo"),
                    col("_source.youngArmyInfo"),
                    lit("hobby"),
                    col("_source.hobby"),
                ),
            )
            .select(
                "birthDate",
                "email",
                "phone",
                "firstName",
                "lastName",
                "middleName",
                "parentFIO",
                "parentEmail",
                "parentPhone",
                "raw_metadata",
            )
        )

        df_parent = (
            df_parent.withColumn("names", name_udf(col("parentFIO")))
            .withColumn(
                "child_birth_date",
                birth_date_udf(col("birthDate"), lit("%Y-%m-%dT%H:%M:%S")),
            )
            .withColumn("child_email", email_udf(col("email")))
            .withColumn("child_phone", phone_udf(col("phone")))
            .withColumn(
                "child_name",
                name_parts_udf(col("firstName"), col("lastName"), lit(None)),
            )
            .withColumn("names", name_udf(col("parentFIO")))
            .withColumn("emails", email_udf(col("parentEmail")))
            .withColumn("phones", phone_udf(col("parentPhone")))
            .withColumn(
                "relations",
                when(
                    col("child_name").isNotNull(),
                    array(
                        relations_udf(
                            concat_ws(
                                " ",
                                col("child_name"),
                                col("child_birth_date"),
                                col("child_email"),
                                col("child_phone"),
                                lit("Ребенок"),
                            )
                        )
                    ),
                ).otherwise(array()),
            )
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("address", lit(None))
            .withColumn("documents", array())
            .withColumn("educations", array())
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "relations",
                "birth_date",
                "documents",
                "educations",
                "raw_metadata",
            )
        )

        df_users = (
            df_users.withColumn(
                "names",
                name_parts_udf(
                    col("_source.firstName"),
                    col("_source.lastName"),
                    col("_source.middleName"),
                ),
            )
            .withColumn("address", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", email_udf(col("_source.email")))
            .withColumn("phones", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("relations", lit(None))
            .withColumn("documents", array())
            .withColumn("educations", array())
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "emails",
                "phones",
                "address",
                "sex",
                "relations",
                "birth_date",
                "documents",
                "educations",
                "raw_metadata",
            )
        )

        df = df_child.unionAll(df_parent).unionAll(df_users)

        df = (
            df.withColumn(
                "educations",
                when(
                    size(array_compact(col("educations"))) > 0,
                    array_compact(col("educations")),
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
            .withColumn(
                "relations",
                when(
                    size(array_compact(col("relations"))) > 0,
                    array_compact(col("relations")),
                ).otherwise(None),
            )
            .withColumn(
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
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
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
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
            )
        )
        df = df.select(
            "names",
            "emails",
            "phones",
            "address",
            "sex",
            "relations",
            "birth_date",
            "documents",
            "educations",
            "raw_metadata",
        )
        df.show(n=100, truncate=False)

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
