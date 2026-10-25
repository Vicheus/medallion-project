import logging
import os
from abc import ABC, abstractmethod
from typing import Optional, Callable

from pyspark.sql import DataFrame
from pyspark.sql.types import StructType

from parsetron.engine.bronze.config import BronzeRead
from parsetron.engine.md import InMdData

logger = logging.getLogger(__name__)


class BaseReader(ABC):
    def __init__(self, spark, md_processor: Optional[InMdData]):
        self.spark = spark
        self.md_processor = md_processor

    @abstractmethod
    def read(
        self, config: BronzeRead, schema: Optional[StructType] = None
    ) -> DataFrame:
        pass

    def _read(self, config: BronzeRead, func: Callable[[str], DataFrame]) -> DataFrame:
        path: str = (
            config.path
            if os.path.isabs(config.path)
            else os.path.join(config.base_path, config.path)
        )
        logger.info(f"Started reading from {path}")
        df = func(path)
        if self.md_processor:
            self.md_processor.find_stat_in(df, path)
        return df
