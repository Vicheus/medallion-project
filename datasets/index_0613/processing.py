from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    split,
    expr,
    regexp_replace,
    array_compact,
    collect_set,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, phone_udf, address_udf
from parsetron.sections.vehicles.udfs import vehicle_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0613"
    calc_completeness: bool = True

    def parser(self):
        df = self.read(
            path="/home/user/Documents/data/index_0613/raw/gaspro.csv",
            sep=",",
            header=True,
        )

        df = (
            df.withColumn("parts", split(col("text"), r"\s*\|\s*"))
            .withColumn("parts", expr("slice(parts, 2, size(parts))"))
            .withColumn("keys", expr("filter(parts, (x, i) -> i % 2 = 0)"))
            .withColumn("values", expr("filter(parts, (x, i) -> i % 2 = 1)"))
            .withColumn(
                "keys", expr("transform(keys, x -> trim(regexp_replace(x, ':$', '')))")
            )
            .withColumn("values", expr("transform(values, x -> trim(x))"))
            .withColumn(
                "kv_map",
                expr(
                    """
                    map_from_arrays(
                        slice(keys, 1, least(size(keys), size(values))),
                        slice(values, 1, least(size(keys), size(values)))
                    )
                """
                ),
            )
        )

        df = df.select(
            col("kv_map")["Марка и модель автомобиля"].alias(
                "Марка и модель автомобиля"
            ),
            regexp_replace(
                col("kv_map")["Год выпуска автомобиля"], r"[^0-9]", ""
            ).alias("Год выпуска автомобиля"),
            col("kv_map")["Объём двигателя"].alias("Объём двигателя"),
            col("kv_map")["Город"].alias("Город"),
            col("kv_map")["Сервис ГБО"].alias("Сервис ГБО"),
            col("kv_map")["Ваше имя"].alias("Ваше имя"),
            col("kv_map")["Номер телефона"].alias("Номер телефона"),
            col("date"),
        )

        df = (
            df.withColumn("names", name_udf(col("Ваше имя")))
            .withColumn("phones", phone_udf(col("Номер телефона")))
            .withColumn("address", address_udf(col("Город")))
            .withColumn(
                "vehicles",
                when(
                    col("Марка и модель автомобиля").isNotNull()
                    & (col("Марка и модель автомобиля") != ""),
                    array(
                        vehicle_udf(
                            lit(1),
                            col("Марка и модель автомобиля"),
                            when(
                                col("Год выпуска автомобиля") != "",
                                col("Год выпуска автомобиля").cast("int"),
                            ),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .select("names", "phones", "address", "vehicles")
        )

        df = (
            df.groupBy(["names", "phones"])
            .agg(
                array_compact(flatten(collect_set(col("vehicles")))).alias("vehicles"),
                array_compact(collect_set(col("address"))).alias("address"),
            )
            .select("names", "phones", "address", "vehicles")
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        df = (
            df.withColumn(
                "vehicles",
                when(size(col("vehicles")) > 0, col("vehicles")).otherwise(None),
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
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
        )
        df = df.filter(col("names").isNotNull() & (col("phones").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
