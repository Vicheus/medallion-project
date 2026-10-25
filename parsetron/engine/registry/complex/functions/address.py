from typing import Literal, Any, Optional

from pyspark import StorageLevel
from pyspark.sql import DataFrame
from pyspark.sql.functions import explode
from pyspark.sql.pandas.functions import pandas_udf

from parsetron.engine.registry.complex.functions.base import BaseBatchAction
from parsetron.engine.registry.resolver import resolve
from parsetron.sections.main.schemas import normalized_addresses_schema
from parsetron.utils.AddressAnalyzer.AddressAnalyzer2 import (
    AddressAnalyzer,
    AddressAnalyzerDto,
)


class StructuredAddressBatchFn(BaseBatchAction):
    batch_fn: Literal["structured_address_udf"]
    raw: str
    address: str
    type: Optional[int] = None
    concurrent_tasks: int = 10
    http_conn_limit: int = 10
    http_conn_timeout: int = 20
    max_retries: int = 7
    _address_analyzer: AddressAnalyzer

    def model_post_init(self, context: Any, /) -> None:
        self._address_analyzer = AddressAnalyzer(
            AddressAnalyzerDto(
                concurrent_tasks=self.concurrent_tasks,
                http_conn_limit=self.http_conn_limit,
                http_conn_timeout=self.http_conn_timeout,
                max_retries=self.max_retries,
            )
        )

    def apply(self, df: DataFrame, target_col: str) -> DataFrame:
        udf = pandas_udf(self._address_analyzer.geocode, normalized_addresses_schema)
        return df.withColumn(
            target_col,
            explode(udf(resolve(self.raw), resolve(self.address), resolve(self.type))),
        ).persist(StorageLevel.DISK_ONLY)
