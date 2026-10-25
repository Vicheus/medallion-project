import logging
from functools import singledispatchmethod
from typing import Optional

from pyspark.sql import DataFrame
from pyspark.sql.types import StructType, StringType

from parsetron.engine.bronze.config import BronzeJoin, BronzeRead, BronzeUnion
from parsetron.engine.bronze.helpers.clean import clean_values, clean_headers
from parsetron.engine.bronze.readers.base import BaseReader
from parsetron.engine.bronze.readers.factory import ReaderFactory
from parsetron.engine.md import InMdData

logger = logging.getLogger(__name__)


def _prepare_schema(schema: list[str]) -> Optional[StructType]:
    if not schema:
        return None
    header = StructType()
    for value in schema:
        header.add(value, StringType(), True)
    return header


class Reader:
    def __init__(
        self,
        spark,
        md_processor: Optional[InMdData],
        limit: Optional[int] = None,
    ):
        self.spark = spark
        self.md_processor = md_processor
        self.readers: dict[str, BaseReader] = {}
        self.limit = limit

    def read(self, config: BronzeRead) -> DataFrame:
        df = self._read(config)
        df = self._append(df, config.append)
        return df

    def _read(self, config: BronzeRead) -> DataFrame:
        reader = self.readers.setdefault(
            config.format,
            ReaderFactory.create(
                self.spark, config.format, self.md_processor, self.limit
            ),
        )
        header = _prepare_schema(config.header)
        df = reader.read(config, header)
        if self.limit:
            logger.info(f"Limit `{self.limit}` will be applied to {config.path}")

        df = clean_headers(df, config.path)
        if config.aliases:
            df = df.withColumnsRenamed(config.aliases)
        df = clean_values(config, df)
        return df

    def _append(
        self, df: DataFrame, append: list[BronzeJoin | BronzeUnion]
    ) -> DataFrame:
        for append_type in append:
            df = self._base_append(append_type, df)
        return df

    @singledispatchmethod
    def _base_append(self, config: BronzeJoin, df: DataFrame) -> DataFrame:
        join_df = self._read(config.read)
        if config.rename_suffix:
            join_df = join_df.toDF(
                *(
                    (
                        column
                        if column in config.ids
                        else f"{column}{config.rename_suffix}"
                    )
                    for column in join_df.columns
                )
            )
        df = df.join(join_df, config.ids, config.how)
        return self._append(df, config.append)

    @_base_append.register
    def _(self, config: BronzeUnion, df: DataFrame) -> DataFrame:
        union_df = self._read(config.read)
        df = df.unionByName(union_df, config.allow_missing_columns)
        return self._append(df, config.append)


class OnlyReader:
    def __init__(
        self,
        spark,
        md_processor: Optional[InMdData],
        limit: Optional[int] = None,
    ):
        self.spark = spark
        self.md_processor = md_processor
        self.readers: dict[str, BaseReader] = {}
        self.limit = limit

    def read(self, config: BronzeRead) -> DataFrame:
        df = self._read(config)
        if self.limit:
            logger.info(f"Limit `{self.limit}` will be applied to {config.path}")
        self._read_nested(config.append)
        return df

    def _read(self, config: BronzeRead) -> DataFrame:
        reader = self.readers.setdefault(
            config.format,
            ReaderFactory.create(
                self.spark, config.format, self.md_processor, self.limit
            ),
        )
        header = _prepare_schema(config.header)
        return reader.read(config, header)

    def _read_nested(self, append_config: list[BronzeJoin | BronzeUnion]) -> None:
        for config in append_config:
            self._read(config.read)
            if config.append:
                self._read_nested(config.append)
