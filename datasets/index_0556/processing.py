from pyspark import StorageLevel
from functools import reduce
from pyspark.sql.functions import (
    col,
    lit,
    array,
    concat,
    array_remove,
    size,
    create_map,
    split,
    regexp_extract,
    concat_ws,
    when,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    address_udf,
    raw_metadata_udf,
)
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.educations.udfs import education_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0556"

    def parser(self):
        months = {
            "Январь": "01",
            "Февраль": "02",
            "Март": "03",
            "Апрель": "04",
            "Май": "05",
            "Июнь": "06",
            "Июль": "07",
            "Август": "08",
            "Сентябрь": "09",
            "Октябрь": "10",
            "Ноябрь": "11",
            "Декабрь": "12",
        }

        mapping_expr = create_map([lit(x) for kv in months.items() for x in kv])

        def parse_period_column(df, col_name):
            start_part = regexp_extract(col_name, r"^([А-Яа-я]+ \d{4})", 1)
            end_part = regexp_extract(col_name, r"— ([А-Яа-я]+ \d{4}|н\.в\.)", 1)

            start_month = split(start_part, " ").getItem(0)
            start_year = split(start_part, " ").getItem(1)

            end_month = split(end_part, " ").getItem(0)
            end_year = split(end_part, " ").getItem(1)

            start_date = when(
                mapping_expr[start_month].isNotNull(),
                concat_ws(".", lit("01"), mapping_expr[start_month], start_year),
            )

            end_date = when(end_part == "н.в.", lit(None)).when(
                mapping_expr[end_month].isNotNull(),
                concat_ws(".", lit("01"), mapping_expr[end_month], end_year),
            )

            df = df.withColumn(f"{col_name}_start", start_date).withColumn(
                f"{col_name}_end", end_date
            )

            return df

        def build_works_array(df, work_udf, max_n=10):
            works = []

            for i in range(1, max_n + 1):

                works.append(
                    work_udf(
                        col(f"work_exp_position_{i}"),
                        col(f"work_exp_term_{i}_start"),
                        col(f"work_exp_term_{i}_end"),
                        col(f"work_exp_place_{i}"),
                        lit(None),
                        col(f"work_exp_desc_{i}"),
                    )
                )

            condition = reduce(
                lambda a, b: a | b,
                [
                    col(f"work_exp_position_{i}").isNotNull()
                    | col(f"work_exp_place_{i}").isNotNull()
                    for i in range(1, max_n + 1)
                ],
            )

            df = df.withColumn("works", when(condition, array(*works)))

            return df

        def build_educations_array_udf(df, education_udf, max_n=10):
            educations = []

            for i in range(1, max_n + 1):
                edu_date = when(
                    col(f"education_term_{i}").isNotNull(),
                    concat(lit("31.12."), col(f"education_term_{i}")),
                )
                educations.append(
                    when(
                        col(f"education_place_{i}").isNotNull(),
                        education_udf(
                            lit(None),
                            col(f"education_place_{i}"),
                            lit(None),
                            edu_date,
                            lit(None),
                            lit(None),
                        ),
                    )
                )

            educations_array = array_remove(array(*educations), None)

            df = df.withColumn(
                "educations", when(size(educations_array) > 0, educations_array)
            )

            return df

        df = self.read(
            path="/home/user/Documents/data/index_0556/raw/rabota_by/resume_info.csv",
            sep=",",
            header=True,
        )

        for i in range(1, 11):
            df = parse_period_column(df, f"work_exp_term_{i}")
        df = build_works_array(df, work_udf)
        df = build_educations_array_udf(df, education_udf)

        df.show(n=5, truncate=False)

        df = (
            df.withColumn("names", name_udf(col("name")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
            .withColumn("address", address_udf(col("city")))
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("description"),
                    col("description"),
                    lit("languages"),
                    col("languages"),
                    lit("info"),
                    col("info"),
                ),
            )
            .select(
                "names", "birth_date", "address", "educations", "works", "raw_metadata"
            )
        )
        #
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
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & col("birth_date").isNotNull())

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
