from pyspark.sql import DataFrame, SparkSession

from parsetron.engine.silver.readers.parquet import ParquetReader


class Reader:
    def __init__(self, spark: SparkSession, in_path: str):
        self.in_path = in_path
        self.reader = ParquetReader(spark)

    def read(self, group_id: str, entity: str) -> DataFrame:
        return self.reader.read_entity(self.in_path, group_id, entity)
