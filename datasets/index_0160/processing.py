from pyspark import StorageLevel
from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    array_compact,
    concat,
    regexp_replace,
    first,
    collect_set,
    size,
    flatten,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import name_udf, sex_udf, birth_date_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0160"

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0160/raw/edu.govvrn.ru/edu.govvrn.ru- @BDump/*.csv",
                sep=",",
                header=True,
            )
            .withColumn("name", regexp_replace("textBox1", r"[^a-zA-Zа-яА-Я\s-]", ""))
            .withColumn("names", name_udf(col("name")))
            .withColumn("birth_date", birth_date_udf(col("textBox6"), lit("%d.%m.%Y")))
            .withColumn("sex", sex_udf(col("textBox14")))
            .withColumn(
                "doc_num",
                regexp_replace(
                    regexp_replace(
                        regexp_replace(
                            concat(col("textBox13"), col("textBox15")), r"\s*-\s*", ""
                        ),
                        r"^(II|III)",
                        "I",
                    ),
                    " ",
                    "",
                ),
            )
            .withColumn(
                "documents",
                array(
                    when(
                        col("doc_num").isNotNull(),
                        document_udf(
                            lit(None),
                            col("doc_num"),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit(None),
                            lit("yyyy-MM-dd"),
                        ),
                    ).otherwise(None)
                ),
            )
            .select("names", "birth_date", "sex", "documents")
        )

        df = (
            df.groupBy(
                [
                    "names",
                    "birth_date",
                    col("documents")[0]["serial"],
                    col("documents")[0]["type"],
                ]
            )
            .agg(
                first("sex").alias("sex"),
                array_compact(flatten(collect_set("documents"))).alias("documents"),
            )
            .select("names", "birth_date", "sex", "documents")
        )

        df = df.withColumn(
            "names", when(col("names").isNotNull(), array(col("names"))).otherwise(None)
        ).withColumn(
            "documents",
            when(size(col("documents")) > 0, col("documents")).otherwise(None),
        )
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(col("names").isNotNull() & (col("documents").isNotNull()))

        df.show(n=20, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
