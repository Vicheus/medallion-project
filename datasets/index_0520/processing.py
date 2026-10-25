from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    from_json,
    expr,
)
from pyspark.sql.types import ArrayType

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_parts_udf,
    phone_udf,
    email_udf,
    sex_udf,
    birth_date_udf,
    address_udf,
    address_from_parts_udf,
    raw_metadata_udf,
    children_udf,
)
from parsetron.sections.work.schemas import work_schema
from parsetron.sections.educations.schemas import education_schema


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0520"

    def parser(self):
        df_1 = (
            self.read(
                path="/media/user/T7 Shield/Databases/index_0520/raw/output_final.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date",
                birth_date_udf(col("Дата рождения"), lit("%Y-%m-%dT%H:%M:%S")),
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "relationship",
                when(col("Семейное положение").isin("Женат", "Замужем"), 0)
                .when(col("Семейное положение").isin("Разведен", "Разведена"), 3)
                .when(col("Семейное положение").isin("Вдовец", "Вдова"), 2)
                .otherwise(None),
            )
            .withColumn(
                "children_mapped",
                when(col("Наличие детей").isin("Есть"), "1")
                .when(col("Наличие детей").isin("Нет"), "0")
                .otherwise(None),
            )
            .withColumn("children", children_udf(col("children_mapped")))
            .withColumn("emails", email_udf(col("Email")))
            .withColumn("phones", phone_udf(col("Телефон")))
            .withColumn("address", address_udf(col("Город")))
            .withColumn(
                "addresses",
                address_from_parts_udf(
                    lit(1),
                    lit(None).alias("index"),
                    lit(None).alias("country"),
                    lit(None).alias("region"),
                    col("Город").alias("settlement"),
                    lit(None).alias("street"),
                    lit(None).alias("house"),
                    lit(None).alias("floor"),
                    lit(None).alias("flat"),
                    lit(None).alias("office"),
                    lit(None).alias("corpus"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Желаемая должность"),
                    col("Желаемая должность"),
                    lit("Желаемая зарплата"),
                    col("Желаемая зарплата"),
                ),
            )
            .withColumn(
                "works",
                from_json(col("work_experience_parsed"), ArrayType(work_schema)),
            )
            .withColumn(
                "works",
                expr(
                    """
                    transform(
                        filter(works, x -> (x.post is not null and x.post != '') 
                                        or (x.company is not null and x.company != '')),
                        x -> struct(
                            x.post as post,
                            -- Force all dates to 01-01-Y
                            date_format(
                                to_date(
                                    case
                                        when x.date_start rlike '^[0-9]{4}$' then concat('01-01-', x.date_start)
                                        when x.date_start rlike '^[0-9]{2}-[0-9]{2}-[0-9]{4}$' then concat('01-01-', split(x.date_start, "-")[2])
                                        else null
                                    end,
                                    'dd-MM-yyyy'
                                ),
                                'dd.MM.yyyy'
                            ) as date_start,
                            date_format(
                                to_date(
                                    case
                                        when x.date_end rlike '^[0-9]{4}$' then concat('01-01-', x.date_end)
                                        when x.date_end rlike '^[0-9]{2}-[0-9]{2}-[0-9]{4}$' then concat('01-01-', split(x.date_end, "-")[2])
                                        else null
                                    end,
                                    'dd-MM-yyyy'
                                ),
                                'dd.MM.yyyy'
                            ) as date_end,
                            x.company as company,
                            x.address as address,
                            x.comment as comment
                        )
                    )
                """
                ),
            )
            .withColumn("educations", array())
            .select(
                "names",
                "sex",
                "birth_date",
                "relationship",
                "children",
                "address",
                "addresses",
                "emails",
                "phones",
                "raw_metadata",
                "works",
                "educations",
            )
        )

        df_2 = (
            self.read(
                path="/media/user/T7 Shield/Databases/index_0520/raw/output_final_1_1.csv",
                sep=",",
                header=True,
            )
            .withColumn(
                "names", name_parts_udf(col("Имя"), col("Фамилия"), col("Отчество"))
            )
            .withColumn(
                "birth_date", birth_date_udf(col("Дата рождения"), lit("%d.%m.%Y"))
            )
            .withColumn("sex", sex_udf(col("Пол")))
            .withColumn(
                "relationship",
                when(col("Семейное положение").isin("Женат", "Замужем"), 0)
                .when(col("Семейное положение").isin("Разведен", "Разведена"), 3)
                .when(col("Семейное положение").isin("Вдовец", "Вдова"), 2)
                .otherwise(None),
            )
            .withColumn(
                "children_mapped",
                when(col("Наличие несовершеннолетних детей").isin("Есть"), "1")
                .when(col("Наличие несовершеннолетних детей").isin("Нет"), "0")
                .otherwise(None),
            )
            .withColumn("children", children_udf(col("children_mapped")))
            .withColumn("emails", email_udf(col("E-mail")))
            .withColumn("phones", phone_udf(col("Телефон (нормализованное)")))
            .withColumn("address", address_udf(col("Место жительства")))
            .withColumn(
                "addresses",
                address_from_parts_udf(
                    lit(1),
                    lit(None).alias("index"),
                    lit(None).alias("country"),
                    lit(None).alias("region"),
                    col("Место жительства").alias("settlement"),
                    lit(None).alias("street"),
                    lit(None).alias("house"),
                    lit(None).alias("floor"),
                    lit(None).alias("flat"),
                    lit(None).alias("office"),
                    lit(None).alias("corpus"),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("Увлечения, интересы"),
                    col("Увлечения, интересы"),
                    lit("Цель карьеры"),
                    col("Цель карьеры"),
                    lit("Причина смены работы"),
                    col("Причина смены работы"),
                    lit("Знание иностранных языков"),
                    col("Знание иностранных языков"),
                    lit("Знание персонального компьютера"),
                    col("Знание персонального компьютера"),
                    lit("Умеет ли водить машину"),
                    col("Умеет ли водить машину"),
                    lit("Наличие персонального автомобиля"),
                    col("Наличие персонального автомобиля"),
                    lit("Владеет ли навыками машинописи"),
                    col("Владеет ли навыками машинописи"),
                    lit("Приемлема ли 6-ти дневная рабочая неделя"),
                    col("Приемлема ли 6-ти дневная рабочая неделя"),
                    lit("Приемлем ли ненормированный рабочий день"),
                    col("Приемлем ли ненормированный рабочий день"),
                    lit("Приемлемы ли командировки"),
                    col("Приемлемы ли командировки"),
                    lit("Допустим ли переезд в другой город"),
                    col("Допустим ли переезд в другой город"),
                ),
            )
            .withColumn(
                "works",
                from_json(col("work_experience_parsed"), ArrayType(work_schema)),
            )
            .withColumn(
                "works",
                expr(
                    """
                    transform(
                        filter(works, x -> (x.post is not null and x.post != '') 
                                        or (x.company is not null and x.company != '')),
                        x -> struct(
                            x.post as post,
                            -- Force all dates to 01-01-Y
                            date_format(
                                to_date(
                                    case
                                        when x.date_start rlike '^[0-9]{4}$' then concat('01-01-', x.date_start)
                                        when x.date_start rlike '^[0-9]{2}-[0-9]{2}-[0-9]{4}$' then concat('01-01-', split(x.date_start, "-")[2])
                                        else null
                                    end,
                                    'dd-MM-yyyy'
                                ),
                                'dd.MM.yyyy'
                            ) as date_start,
                            date_format(
                                to_date(
                                    case
                                        when x.date_end rlike '^[0-9]{4}$' then concat('01-01-', x.date_end)
                                        when x.date_end rlike '^[0-9]{2}-[0-9]{2}-[0-9]{4}$' then concat('01-01-', split(x.date_end, "-")[2])
                                        else null
                                    end,
                                    'dd-MM-yyyy'
                                ),
                                'dd.MM.yyyy'
                            ) as date_end,
                            x.company as company,
                            x.address as address,
                            x.comment as comment
                        )
                    )
                """
                ),
            )
            .withColumn(
                "educations",
                array(from_json(col("education_parsed"), education_schema)),
            )
            .withColumn(
                "educations",
                expr(
                    """
                    transform(
                        filter(educations, x -> x.title is not null and x.title != ''),
                        x -> struct(
                            x.title as title,
                            x.level as level,
                            -- Force all dates to 01-01-Y
                            date_format(
                                to_date(
                                    case
                                        when x.date_start rlike '^[0-9]{4}$' then concat('01-01-', x.date_start)
                                        when x.date_start rlike '^[0-9]{2}-[0-9]{2}-[0-9]{4}$' then concat('01-01-', split(x.date_start, "-")[2])
                                        else null
                                    end,
                                    'dd-MM-yyyy'
                                ),
                                'dd.MM.yyyy'
                            ) as date_start,
                            date_format(
                                to_date(
                                    case
                                        when x.date_end rlike '^[0-9]{4}$' then concat('01-01-', x.date_end)
                                        when x.date_end rlike '^[0-9]{2}-[0-9]{2}-[0-9]{4}$' then concat('01-01-', split(x.date_end, "-")[2])
                                        else null
                                    end,
                                    'dd-MM-yyyy'
                                ),
                                'dd.MM.yyyy'
                            ) as date_end,
                            x.country as country,
                            x.comment as comment
                        )
                    )
                """
                ),
            )
            .select(
                "names",
                "sex",
                "birth_date",
                "relationship",
                "children",
                "address",
                "addresses",
                "emails",
                "phones",
                "raw_metadata",
                "works",
                "educations",
            )
        )

        df = df_1.unionAll(df_2)

        df = df.drop_duplicates(["names", "birth_date"])

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "works", when(size(col("works")) > 0, col("works")).otherwise(None)
            )
            .withColumn(
                "educations",
                when(size(col("educations")) > 0, col("educations")).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "address",
                when(col("address").isNotNull(), array(col("address"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "addresses",
                when(col("addresses").isNotNull(), array(col("addresses"))).otherwise(
                    None
                ),
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
