from typing import Optional, Callable

from pyspark.sql import SparkSession, DataFrame, DataFrameReader
from pyspark.sql.types import StructType

from parsetron.engine.bronze.config import BronzeRead
from parsetron.engine.bronze.readers.base import BaseReader
from parsetron.engine.md import InMdData


class CsvReader(BaseReader):
    def __init__(
        self,
        spark: SparkSession,
        md_processor: Optional[InMdData] = None,
        limit: Optional[int] = None,
    ):
        super().__init__(spark, md_processor)
        self.limit = limit

    def read(
        self, config: BronzeRead, schema: Optional[StructType] = None
    ) -> DataFrame:
        reader = self._prepare_reader(config.options, schema)
        func: Callable[[str], DataFrame] = lambda path: (
            reader.csv(path).limit(self.limit) if self.limit else reader.csv(path)
        )
        return self._read(config, func)

    def _prepare_reader(
        self, options: dict, schema: Optional[StructType]
    ) -> DataFrameReader:
        reader: DataFrameReader = self.spark.read
        for k, v in options.items():
            reader = reader.option(k, v)
        option_keys = options.keys()

        if schema:
            reader = reader.schema(schema)
        else:
            if "inferSchema" not in option_keys:
                reader = reader.option("inferSchema", False)
            if "header" not in option_keys:
                reader = reader.option("header", True)
        if "sep" not in option_keys:
            reader = reader.option("sep", ",")
        if "encoding" not in option_keys:
            reader = reader.option("encoding", "UTF-8")
        if "escape" not in option_keys:
            reader = reader.option("escape", '"')
        if "mode" not in option_keys:
            reader = reader.option("mode", "FAILFAST")
        return reader
