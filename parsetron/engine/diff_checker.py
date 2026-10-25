import logging
import os
from argparse import Namespace, ArgumentParser
from pathlib import Path

from pyspark import StorageLevel
from pyspark.sql import SparkSession, DataFrame

from parsetron.engine.constants import ColumnTypes, JoinTypes
from parsetron.engine.utils.spark import run_spark_app
from parsetron.engine.utils.track import track_execution_time
from parsetron.log import setup_logger

logger = logging.getLogger(__name__)


def _find_latest_date_dir(base_dir: str):
    basedir = Path(base_dir)
    if basedir.exists():
        dirs = [
            d
            for d in basedir.iterdir()
            if d.is_dir() and d.name.startswith("ingest_date=")
        ]
        if dirs:
            if len(dirs) > 1:
                return sorted(dirs, reverse=True)[0].name
            return dirs[0].name
    raise ValueError(f"There is no directory to get data in {basedir}")


class Reader:
    def __init__(self, spark: SparkSession, index_path: str):
        self.spark = spark
        self.path = index_path

    def read_bronze(self) -> list[DataFrame]:
        base_path = self.path + "/bronze"
        path = os.path.join(base_path, _find_latest_date_dir(base_path))
        dfs = []
        for d in Path(path).iterdir():
            dfs.append(self.spark.read.parquet(str(d)))
        return dfs

    def read_gold(self) -> DataFrame:
        reader = (
            self.spark.read.option("inferSchema", False)
            .option("header", True)
            .option("sep", ",")
            .option("encoding", "UTF-8")
            .option("escape", '"')
            .option("mode", "FAILFAST")
        )
        base_path = self.path + "/gold"
        path: str = os.path.join(base_path, _find_latest_date_dir(base_path), "upload")
        logger.info(f"Started reading from {path}")
        return reader.json(path)


class DiffChecker:
    def __init__(self, spark: SparkSession, index_path: str, out_dir: str = ""):
        self.reader = Reader(spark, index_path)
        self.out_dir = out_dir

    def check(self) -> None:
        initial_dfs = self.reader.read_bronze()
        final_data = self.reader.read_gold().select(ColumnTypes.SOURCE_ENTITY_ID.value)

        initial_data = initial_dfs[0]
        if len(initial_dfs) > 1:
            for entity in initial_dfs[1:]:
                initial_data = initial_data.join(
                    entity,
                    on=ColumnTypes.SOURCE_ENTITY_ID.value,
                    how=JoinTypes.OUTER.value,
                )
        initial_data = initial_data.persist(StorageLevel.DISK_ONLY)
        missed_ids = initial_data.join(
            final_data,
            on=ColumnTypes.SOURCE_ENTITY_ID.value,
            how=JoinTypes.LEFT_ANTI.value,
        ).orderBy(ColumnTypes.SOURCE_ENTITY_ID.value)
        missed_ids.coalesce(1).write.csv(
            path=self.out_dir, mode="overwrite", header=True
        )


def collect_arguments() -> Namespace:
    parser = ArgumentParser(description="Diff Checker")
    parser.add_argument("index_path", type=str, help="Path to index")
    parser.add_argument("--output-dir", type=str, help="Path to save diff result")
    return parser.parse_args()


@track_execution_time(logger, "Diff Checker")
def main():
    args = collect_arguments()
    setup_logger()

    app_run_func = lambda spark: DiffChecker(
        spark, args.index_path, args.output_dir
    ).check()
    run_spark_app(logger, "Diff Checker", app_run_func)

    logger.info("Diff Checker finished successfully")


if __name__ == "__main__":
    main()
