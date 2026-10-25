from typing import Literal

from pyspark.sql import DataFrame

from parsetron.engine.registry.functions.base import BaseAction
from parsetron.engine.registry.resolver import resolve_expr
from parsetron.engine.registry.transformations.base import BaseOperation, BaseOpCols


class FilterOp(BaseOperation):
    op: Literal["filter"]
    function: BaseAction

    def apply(self, df: DataFrame) -> DataFrame:
        return df.filter(resolve_expr(self.function))


class DistinctOp(BaseOperation, BaseOpCols):
    op: Literal["distinct"]

    def apply(self, df: DataFrame) -> DataFrame:
        if self.columns:
            return df.drop_duplicates(self.columns)
        return df.distinct()


class WithColumnOp(BaseOperation):
    op: Literal["withColumn"]
    column: str
    function: BaseAction

    def apply(self, df: DataFrame) -> DataFrame:
        return df.withColumn(self.column, resolve_expr(self.function))


class DropColumnsOp(BaseOperation, BaseOpCols):
    op: Literal["dropColumns"]

    def apply(self, df: DataFrame) -> DataFrame:
        return df.drop(*self.columns)
