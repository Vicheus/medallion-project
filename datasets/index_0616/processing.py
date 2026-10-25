from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    first,
    array,
    array_distinct,
    explode,
    trim,
    regexp_extract,
    array_compact,
    collect_set,
    size,
    split,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    raw_metadata_udf,
)
from parsetron.sections.socials.udfs import social_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0616"
    calc_completeness: bool = True
    validate_invalid_groupping: bool = True

    def parser(self):
        EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        PHONE_REGEX = (
            r"(?:\+7|8)[\s\-\(\)\"]*\d{3}[\s\-\)]*\d{3}[\s\-]*\d{2}[\s\-]*\d{2}"
        )
        SKYPE_REGEX = r"(?i)skype[:\-\s\^]*([a-zA-Z0-9._-]+)"

        df = self.read(
            path="/home/user/Documents/data/index_0616/raw/dns-shop-employers.csv",
            sep=",",
            header=True,
        )
        df = df.withColumn("parts", split(col("Рабочие контакты"), r";"))

        df = df.withColumn("part", explode(col("parts")))
        df = df.withColumn("part", trim(col("part")))

        df = (
            df.withColumn("email2", when(col("part").rlike(EMAIL_REGEX), col("part")))
            .withColumn(
                "phone",
                when(
                    col("part").rlike(PHONE_REGEX),
                    regexp_extract(col("part"), PHONE_REGEX, 0),
                ),
            )
            .withColumn("skype", regexp_extract(col("part"), SKYPE_REGEX, 1))
        )
        df = (
            df.withColumn("names", name_udf(col("ФИО")))
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%Y-%m-%d"))
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "emails",
                array_distinct(
                    array_compact(
                        array(email_udf(col("email")), email_udf(col("email2")))
                    )
                ),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "socials",
                when(
                    col("skype").isNotNull(),
                    social_udf(
                        lit("Skype"),
                        col("skype"),
                        lit(None),
                        lit(None),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Филиал сотрудника полное наименование"),
                    df["Филиал сотрудника полное наименование"],
                    lit("Филиал сотрудника наименование"),
                    df["Филиал сотрудника наименование"],
                ),
            )
            .select(
                "names",
                "birth_date",
                "sex",
                "phones",
                "emails",
                "socials",
                "raw_metadata",
            )
        )

        df = df.groupBy(["names", "birth_date"]).agg(
            first(col("sex"), ignorenulls=True).alias("sex"),
            array_compact(collect_set(col("phones"))).alias("phones"),
            array_compact(flatten(collect_set(col("emails")))).alias("emails"),
            array_compact(collect_set(col("socials"))).alias("socials"),
            array_compact(collect_set(col("raw_metadata"))).alias("raw_metadata"),
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "phones", when(size(col("phones")) > 0, col("phones")).otherwise(None)
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "socials",
                when(size(col("socials")) > 0, col("socials")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
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
