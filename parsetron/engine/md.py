import logging
import shutil
from abc import ABC, abstractmethod

import pandas as pd
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, size
from pyspark.sql.types import ArrayType, StructField

from parsetron.settings import DATE_FORMAT
from parsetron.utils import ReadmeGenerator, ColumnCompletenessGenerator

logger = logging.getLogger(__name__)


class InMdData(ABC):
    @abstractmethod
    def find_stat_in(self, df: DataFrame, path: str) -> None:
        pass


class OutMdData(ABC):
    @abstractmethod
    def find_stat_out(self, df: DataFrame, path: str) -> None:
        pass


class MdGenerator(InMdData, OutMdData):
    schema_raw: list[dict[str, int | str]]

    def __init__(
        self,
        dataset_code_name: str,
        calc_completeness: bool = True,
        data_sample_size: int = 20,
        invalid_grouping_threshold: int = 10,
        min_column_completeness_threshold: float = 0.05,
    ):
        self.index = dataset_code_name
        self.schema_raw = []
        self.read_paths = set()
        self.calc_completeness = calc_completeness
        self.data_sample_size = data_sample_size
        self.invalid_grouping_threshold = invalid_grouping_threshold
        self.min_column_completeness_threshold = min_column_completeness_threshold

    def find_stat_in(self, df: DataFrame, path: str) -> None:
        if path in self.read_paths:
            logger.warning(f"Read the same file path: {path}")
            return

        self.read_paths.add(path)
        schema = df.schema.treeString()
        count = df.count()
        sample = df.limit(self.data_sample_size).toPandas().to_markdown(index=False)

        self.schema_raw.append(
            {
                "code_name": self.index,
                "path": path,
                "total": count,
                "schema": schema,
                "data_sample": sample or "",
            }
        )

    def find_stat_out(self, df: DataFrame, path: str) -> None:
        completeness_stats, df_size = (
            self._find_completeness(df)
            if self.calc_completeness
            else (None, df.count())
        )

        self._validate_completeness(completeness_stats)
        self._validate_invalid_grouping(df)

        schema = df.schema.treeString()
        pandas_df = df.limit(self.data_sample_size).toPandas()
        if "actuality" in pandas_df.columns:
            pandas_df["actuality"] = pd.to_datetime(pandas_df["actuality"])
            pandas_df["actuality"] = pandas_df["actuality"].dt.strftime(DATE_FORMAT)
            pandas_df["actuality"] = pandas_df["actuality"].fillna("")

        sample = pandas_df.to_markdown(index=False)
        completeness_stats = self._round_completeness(completeness_stats)
        schema_final = {
            "total": df_size,
            "schema": schema,
            "columns_completeness": completeness_stats,
            "data_sample": sample or "",
        }

        readme_generator = ReadmeGenerator(dataset_code_name=self.index)
        readme_generator.generate_git_readme(
            schema_raw=self.schema_raw, schema_final=schema_final
        )
        readme_generator.generate_ds_documentation_readme(
            schema_raw=self.schema_raw, schema_final=schema_final
        )

    def copy_config_file(self, path: str):
        renamed_path = f"datasets/{self.index}/processing.yaml"
        if path != renamed_path:
            shutil.copy2(path, renamed_path)

    def _validate_completeness(self, completeness_stats: dict[str, float]):
        for key, value in completeness_stats.items():
            if value < self.min_column_completeness_threshold:
                logger.warning(
                    f"{key} column completeness is lower than threshold: {value}"
                )

    @staticmethod
    def _find_completeness(
        df: DataFrame,
    ) -> tuple[dict[str, float], int]:
        generator = ColumnCompletenessGenerator()
        return generator.generate_columns_completeness_stats(df)

    @staticmethod
    def _round_completeness(
        completeness_stats: dict[str, int | float],
    ) -> dict[str, int | float]:
        if not completeness_stats:
            return {}
        return {key: round(value * 100, 2) for key, value in completeness_stats.items()}

    def _validate_invalid_grouping(self, df: DataFrame):
        schema_fields: list[StructField] = df.schema.fields or []
        array_columns = [
            field.name
            for field in schema_fields
            if isinstance(field.dataType, ArrayType)
        ]

        for column in array_columns:
            oversized_df = df.filter(
                size(col(column)) > self.invalid_grouping_threshold
            ).select("names", size(col(column)).alias("count"))

            oversized = oversized_df.orderBy(col("count").desc()).limit(10).collect()
            for i, row in enumerate(oversized):
                logger.warning(
                    f"{i+1}. Field '{column}' has {row['count']} entries for names = {row['names']}"
                )
