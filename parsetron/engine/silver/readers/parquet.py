import os

from pyspark.sql import SparkSession, DataFrame

from parsetron.engine.utils.path import find_date_dir


class ParquetReader:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def read(self, path: str) -> DataFrame:
        return self.spark.read.parquet(path)

    def read_entity(self, base_dir: str, group_id: str, entity: str) -> DataFrame:
        ingest_date_dir = find_date_dir(base_dir)
        if group_id:
            g_id = f"group_id={group_id}"
            path = os.path.join(base_dir, ingest_date_dir, g_id, entity)
        else:
            path = os.path.join(base_dir, ingest_date_dir, entity)

        return self.read(path)
