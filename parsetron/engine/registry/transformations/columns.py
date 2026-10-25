from typing import Literal

from pydantic import field_validator, Field
from pyspark.sql import DataFrame, Window
from pyspark.sql.functions import (
    col,
    concat_ws,
    array_remove,
    collect_set,
    array_sort,
    explode_outer,
    lit,
    when,
    coalesce,
    count,
)

from parsetron.engine.constants import ColumnTypes
from parsetron.engine.registry.base import ActionType
from parsetron.engine.registry.resolver import resolve
from parsetron.engine.registry.transformations.base import BaseOperation, ActionOpCols


def _concat_columns_with_null_check(df: DataFrame, column_names: list[ActionType]):
    transformed_cols = []
    for column in column_names:
        transformed_cols.append(resolve(column).cast("string"))
    return df.withColumn("__concatenated", concat_ws(" ", *transformed_cols))


class RelationsOp(BaseOperation, ActionOpCols):
    op: Literal["relations"]
    column: str = ColumnTypes.RELATIONS.value
    ids: list[str] = Field(min_length=1)
    columns: list[ActionType] = Field(min_length=1)

    @field_validator("ids", "columns", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]

    def apply(self, df: DataFrame) -> DataFrame:
        full_df = df.filter(coalesce(*self.ids).isNotNull())
        null_df = df.filter(coalesce(*self.ids).isNull())
        full_df = _concat_columns_with_null_check(full_df, self.columns)
        window_spec = Window.partitionBy(*self.ids)
        return (
            full_df.withColumn(
                self.column, collect_set("__concatenated").over(window_spec)
            )
            .withColumn(
                self.column,
                array_sort(array_remove(col(self.column), col("__concatenated"))),
            )
            .drop("__concatenated")
            .unionByName(null_df, allowMissingColumns=True)
        )


class NullifyDocsByTypesOp(BaseOperation):
    op: Literal["nullifyDocsByTypes"]
    column: str = ColumnTypes.DOCUMENTS.value
    ids: list[str] = Field(min_length=1)
    not_in_types: list[str] = Field(alias="notInTypes", min_length=1)

    @field_validator("ids", "not_in_types", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]

    def apply(self, df: DataFrame) -> DataFrame:
        valid_ids = (
            df.select(explode_outer(self.column).alias("__document"), *self.ids)
            .filter(
                (col("__document.type").isNotNull())
                & ~(col("__document.type").isin(*self.not_in_types))
            )
            .select(*self.ids)
            .withColumn("__has_valid_type", lit(True))
        )

        return (
            df.join(valid_ids, on=self.ids, how="left")
            .withColumn(
                self.column,
                when(col("__has_valid_type") == True, col(self.column)).otherwise(
                    lit(None)
                ),
            )
            .drop("__has_valid_type")
        )


class NullifyColByOccurrenceOp(BaseOperation):
    op: Literal["nullifyColByOccurrence"]
    column: str
    occurrence_column: str = Field(alias="occurrenceColumn")

    def apply(self, df: DataFrame) -> DataFrame:
        window_spec = Window.partitionBy(self.occurrence_column)
        return (
            df.withColumn(
                "__occurrence_count", count(self.occurrence_column).over(window_spec)
            )
            .withColumn(
                self.occurrence_column,
                when(col("__occurrence_count") > 1, None).otherwise(
                    col(self.occurrence_column)
                ),
            )
            .drop("__occurrence_count")
        )
