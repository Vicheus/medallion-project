from datetime import datetime

from pyspark import StorageLevel
from pyspark.sql.functions import (
    col,
    array,
    lower,
    regexp_replace,
    lit,
    when,
    size,
    array_distinct,
    length,
    flatten,
    collect_list,
    explode,
    split,
    array_compact,
    upper,
    substring,
    concat,
    udf,
)
from pyspark.sql.types import ArrayType

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import name_parts_udf, birth_date_udf, sex_udf
from parsetron.sections.work.schemas import work_schema
from parsetron.sections.work.udfs import work_udf, work_date_udf
from parsetron.sections.work.validators.work import work


def _optimize_works(works):
    if works is None:
        return None

    result = {}

    def _parse_date(dt: str):
        try:
            return datetime.strptime(dt, "%d.%m.%Y") if ds else None
        except:
            return None

    for x in works:
        if x is None:
            continue

        post = x["post"]
        ds = x["date_start"]
        de = x["date_end"]

        if not post:
            continue
        ds_dt = _parse_date(ds)
        de_dt = _parse_date(de)

        if post not in result:
            result[post] = (ds_dt, de_dt)
        else:
            old_fd, old_sd = result[post]
            new_fd = min(filter(None, [old_fd, ds_dt]), default=None)
            new_sd = max(filter(None, [old_sd, de_dt]), default=None)
            result[post] = (new_fd, new_sd)

    output = []
    for post, (ds_dt, de_dt) in result.items():
        output.append(
            work(
                post,
                ds_dt.strftime("%d.%m.%Y") if ds_dt else None,
                de_dt.strftime("%d.%m.%Y") if de_dt else None,
            )
        )

    return output


optimize_works_udf = udf(_optimize_works, ArrayType(work_schema, containsNull=False))


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0621"
    validate_invalid_groupping: bool = True

    replace_names_stops = ["нет", "-"]
    replace_names_stops_pattern = "|".join(replace_names_stops)
    filter_prefixes = [
        "─",
        "└",
        "├",
        "┬",
        "┴",
        "┼",
        "═",
        "╒",
        "╓",
        "╘",
        "╙",
        "╚",
        "╞",
        "╟",
        "╠",
        "╤",
        "╥",
        "╦",
        "╧",
        "╨",
        "╩",
        "╪",
        "╫",
        "╬",
        "▀",
        "▐",
        "▌",
        "•",
        "џ",
        "”",
        "’",
        "љ",
        "“",
        "ћ",
    ]
    filter_prefixes_pattern = r"^(" + "|".join(filter_prefixes) + r")"
    replace_fam_stops = ["умер", "уволена", "уволен", "удалить", "студент"]
    replace_fam_stops_pattern = "|".join(replace_fam_stops)
    replace_fam_suffix_stops = ["-п", "-пенсионер", "-пенсионер-ветеран труда", " ь"]
    replace_fam_suffix_stops_pattern = r"(" + "|".join(replace_fam_suffix_stops) + r")$"

    def _read_med_spec_data(self):
        return (
            self.read(path="ree_md_s.csv", sep=",", header=True)
            .select("code", "name_s", "beg_s", "end_s")
            .withColumn("name_s", lower(col("name_s")))
            .filter(~col("name_s").rlike(self.filter_prefixes_pattern))
            .withColumn(
                "name_s",
                split(lower(col("name_s")), r"\s*(\.|/)\s*"),
            )
            .withColumn("name_s", explode(col("name_s")))
            .filter(~col("name_s").startswith("среднее медиц"))
            .withColumn(
                "name_s",
                regexp_replace(lower(col("name_s")), r"( - |   s| в педиатрии)", ""),
            )
            .withColumn(
                "name_s",
                regexp_replace(
                    lower(col("name_s")), "урологияандрология", "урология-андрология"
                ),
            )
            .withColumn(
                "name_s",
                concat(
                    upper(substring(lower(col("name_s")), 1, 1)),
                    substring(col("name_s"), 2, length(col("name_s")) - 1),
                ),
            )
        )

    def parser(self):
        df = (
            self.read(path="ree_md.csv", sep=",", header=True)
            .select("fam", "im", "ot", "w", "dr", "code")
            .filter(~col("fam").rlike(self.filter_prefixes_pattern))
            .withColumn(
                "fam", split(lower(col("fam")), r"\s*(бывшая|бывший| и |бавшая)\s*")
            )
            .withColumn("fam", explode(col("fam")))
            .withColumn(
                "fam",
                regexp_replace(col("fam"), self.replace_fam_suffix_stops_pattern, ""),
            )
            .withColumn(
                "fam",
                regexp_replace(
                    lower(col("fam")),
                    f"\\b({self.replace_fam_stops_pattern})\\b",
                    "",
                ),
            )
            .withColumn(
                "ot",
                regexp_replace(
                    lower(col("ot")),
                    f"\\b({self.replace_names_stops_pattern})\\b",
                    "",
                ),
            )
            .withColumn("names", name_parts_udf("im", "fam", "ot"))
            .filter(col("names").isNotNull())
            .withColumn(
                "documents",
                document_udf(
                    when(
                        length(col("code")) == 11,
                        lit("снилс без контрольной суммы"),
                    ).otherwise(lit("снилс")),
                    col("code"),
                ),
            )
            .filter(col("documents").isNotNull())
            .withColumn(
                "sex",
                sex_udf(when(col("w") == "2", lit("0")).otherwise(col("w"))),
            )
            .withColumn("birth_date", birth_date_udf("dr", lit("%Y-%m-%d")))
            .withColumn("names", array(col("names")))
            .withColumn("documents", array(col("documents")))
            .select("names", "documents", "sex", "birth_date", "code")
            .join(self._read_med_spec_data(), on="code", how="left")
            .withColumn(
                "works",
                array_compact(
                    array(
                        work_udf(
                            col("name_s"),
                            work_date_udf(col("beg_s"), lit("%Y-%m-%d")),
                            work_date_udf(col("end_s"), lit("%Y-%m-%d")),
                        )
                    )
                ),
            )
            .groupBy(["documents", "sex", "birth_date"])
            .agg(
                array_distinct(flatten(collect_list("names"))).alias("names"),
                array_distinct(flatten(collect_list("works"))).alias("works"),
            )
            .withColumn("works", optimize_works_udf(col("works")))
            .withColumn("names", when(size(col("names")) > 0, col("names")))
            .withColumn("documents", when(size(col("documents")) > 0, col("documents")))
            .withColumn("works", when(size(col("works")) > 0, col("works")))
            .filter(col("names").isNotNull() & col("documents").isNotNull())
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
