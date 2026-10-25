import argparse
import logging
from argparse import Namespace
from typing import List

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col, min, max, length, explode, split, lower

from parsetron.engine.utils.spark import run_spark_app

logger = logging.getLogger(__name__)


def setup_logging() -> None:
    handlers = []
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    handlers.append(handler)
    logging.basicConfig(level=logging.INFO, handlers=handlers)


class AnalyzerRegistry:
    def __init__(self):
        self.methods = {
            "top": find_top_values,
            "word_frequency": find_word_frequency,
            "length": find_lengths,
            "stats": find_statistics,
            "chars": find_unique_chars,
        }

    def run(
        self,
        df: DataFrame,
        selected_types: List[str],
        word_frequency: List[str],
        top_limit: int,
    ) -> None:
        col_names = sorted(df.columns)
        if "all" in selected_types or not selected_types:
            selected_types = list(self.methods.keys())

        for col_name in col_names:
            column = col_name
            if "." in col_name:
                cleaned_col_name = col_name.replace(".", "_").strip()
                column = cleaned_col_name
                df = df.withColumnRenamed(col_name, column)
            col_df = df.select(column).persist()
            logger.info(f"\n{'='*60}\nANALYZING COLUMN: {col_name}\n{'='*60}")

            for key in selected_types:
                if key in self.methods:
                    if (
                        key != "word_frequency"
                        or key == "word_frequency"
                        and (word_frequency == "all" or col_name in word_frequency)
                    ):
                        method = self.methods[key]
                        if key in ("top", "word_frequency"):
                            method(col_df, column, top_limit)
                        else:
                            method(col_df, column)
            col_df.unpersist()


def find_top_values(df: DataFrame, col_name: str, limit: int) -> None:
    result = (
        df.groupBy(col_name)
        .count()
        .withColumnRenamed(col_name, "value")
        .orderBy(col("count").desc())
        .limit(limit)
        .collect()
    )
    logger.info(f"Top {limit} values in '{col_name}':")
    for i, row in enumerate(result):
        logger.info(f"  {i+1}. Value: `{row['value']}` | Count: {row['count']}")


def find_word_frequency(df: DataFrame, col_name: str, limit: int) -> None:
    words = "__words"
    word = "__word"
    result = (
        df.withColumn(words, split(col(col_name), "\\s+"))
        .withColumn(word, explode(col(words)))
        .withColumn(word, lower(col(word)))
        .filter((col(word) != "") & (col(word).isNotNull()))
        .groupBy(word)
        .count()
        .orderBy(col("count").desc())
        .limit(limit)
        .collect()
    )
    logger.info(f"Top {limit} words in '{col_name}':")
    for i, row in enumerate(result):
        logger.info(f"  {i+1}. Value: `{row[word]}` | Count: {row['count']}")


def find_lengths(df: DataFrame, col_name: str) -> None:
    res = df.select(
        min(length(col_name)).alias("min"), max(length(col_name)).alias("max")
    ).collect()[0]
    logger.info(f"Length Range [{col_name}]: Min: {res['min']} | Max: {res['max']}")


def find_statistics(df: DataFrame, col_name: str) -> None:
    total = df.count()
    non_null = df.filter(col(col_name).isNotNull()).count()
    not_empty = df.filter(col(col_name).isNotNull() & (col(col_name).cast("string") != "")).count()
    distinct = df.select(col_name).distinct().count()

    uniq_ratio = (distinct / total) if total > 0 else 0
    if 0.9999 < uniq_ratio < 1:
        uniq_ratio = 0.9999
    elif 0 < uniq_ratio < 0.0001:
        uniq_ratio = 0.0001

    logger.info(
        f"Metrics [{col_name}]: Total: {total} | Distinct: {distinct} "
        f"| Non-Null: {non_null} ({non_null/total:.2%}) "
        f"| Empty: {total - not_empty} | Uniqueness: {uniq_ratio:.2%}"
    )


def find_unique_chars(df: DataFrame, col_name: str) -> None:
    chars = (
        df.select(explode(split(col(col_name), "")).alias("c"))
        .filter(length("c") > 0)
        .distinct()
        .orderBy("c")
        .collect()
    )
    unique_str = "".join([row["c"] for row in chars])
    logger.info(f"Unique Characters [{col_name}]: `{unique_str}`")


def load_data(
    spark: SparkSession,
    path: str,
    file_format: str,
    csv_separator: str,
    multiline: str = "false",
) -> DataFrame:
    if not file_format:
        if path.endswith(".csv"):
            file_format = "csv"
        elif path.endswith(".json"):
            file_format = "json"
        else:
            file_format = "parquet"

    logger.info(f"Loading {path} as {file_format}")

    if file_format == "csv":
        reader = (
            spark.read.option("inferSchema", False)
            .option("header", True)
            .option("sep", csv_separator if csv_separator else ",")
            .option("encoding", "UTF-8")
            .option("escape", '"')
            .option("mode", "FAILFAST")
            .option("multiline", multiline)
        )
        return reader.csv(path)
    elif file_format == "json":
        return spark.read.json(path)
    else:
        return spark.read.parquet(path)


def run(spark: SparkSession, args: Namespace, registry: AnalyzerRegistry) -> None:
    df = load_data(spark, args.path, args.file_format, args.csv_separator)
    df_count = df.count()
    multiline_df = load_data(
        spark, args.path, args.file_format, args.csv_separator, multiline="true"
    )
    multiline_df_count = multiline_df.count()
    if df_count == multiline_df_count:
        logger.info(f"{args.path} is NOT MULTILINE")
    else:
        logger.info(f"{args.path} is MULTILINE, rows: {df_count}/{multiline_df_count}")
        df = multiline_df
    selected = args.analysis.split(",") if args.analysis != "all" else []
    word_frequency = (
        args.word_frequency.split(",") if args.word_frequency != "all" else []
    )
    registry.run(df, selected, word_frequency, args.top_limit)


def main() -> None:
    parser = argparse.ArgumentParser(description="PySpark Column Analyzer")

    parser.add_argument("path", help="Path to the input file (CSV/JSON/Parquet)")
    parser.add_argument(
        "--analysis",
        type=str,
        default="all",
        help="Comma-separated: top,length,stats,chars,patterns (default 'all')",
    )
    parser.add_argument(
        "--top-limit",
        type=int,
        default=5,
        help="Limit for count-based results (default 5)",
    )
    parser.add_argument(
        "--file-format",
        type=str,
        default=None,
        help="File format for the input file (default None)",
    )
    parser.add_argument(
        "--csv-separator",
        type=str,
        default=",",
        help="Separator for csv (default ,)",
    )
    parser.add_argument(
        "--word-frequency",
        type=str,
        default="",
        help="Comma-separated columns to calculate word frequency (default 'all')",
    )

    args = parser.parse_args()
    setup_logging()
    registry = AnalyzerRegistry()

    app_run_func = lambda spark: run(spark, args, registry)
    run_spark_app(logger, "Column Analyzer", app_run_func)

    logger.info("Column Analyzer finished successfully")


# python -m parsetron.engine.column_analyzer.py data_path.txt --analysis top,stats --top-limit 10 --csv-separator "\t" --file-format csv --word-frequency col1,col3
if __name__ == "__main__":
    main()
