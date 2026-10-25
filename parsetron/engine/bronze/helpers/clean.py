import logging

from pyspark.sql import DataFrame
from pyspark.sql.functions import trim, col, when, regexp_replace

from parsetron.engine.bronze.config import BronzeRead
from parsetron.engine.registry.resolver import resolve

logger = logging.getLogger(__name__)


def _trim(df: DataFrame, trim_values: bool | str, path: str) -> DataFrame:
    if trim_values:
        if isinstance(trim_values, bool):
            for column in df.columns:
                df = df.withColumn(column, trim(col(column)))
        else:
            pattern = f"^[{trim_values}]+|[{trim_values}]+$"
            for column in df.columns:
                df = df.withColumn(column, regexp_replace(col(column), pattern, ""))
        logger.info(f"DF values have been trimmed for {path}")
    return df


def _replace(df: DataFrame, values: list[str], path: str) -> DataFrame:
    if values:
        logger.info(f"DF {values} will be replaced with `None` for {path}")
        df = df.replace(values, None)
    return df


def _replace_regex(df: DataFrame, patterns: list[str], path: str) -> DataFrame:
    if patterns:
        logger.info(f"DF {patterns} will be regex replaced with `None` for {path}")
        for pattern in patterns:
            for column in df.columns:
                df = df.withColumn(
                    column, when(~col(column).rlike(pattern), col(column))
                )
    return df


def clean_headers(df: DataFrame, path: str) -> DataFrame:
    columns = df.columns
    stripped_columns = []
    for column in columns:
        if "." in column:
            stripped_column = column.replace(".", "_").strip()
            df = df.withColumnRenamed(column, stripped_column)
        else:
            stripped_column = column.strip()
        stripped_columns.append(stripped_column)
    df = df.toDF(*stripped_columns)
    if columns != stripped_columns:
        logger.warning(f"DF headers have been trimmed for {path}")

    return df


def clean_values(config: BronzeRead, df: DataFrame) -> DataFrame:
    df = _trim(df, config.trim_values, config.path)
    if config.replace_regex_patrial:
        logger.info(
            f"DF {config.replace_regex_patrial} will be regex replaced with `` for {config.path}"
        )
        for column, pattern in config.replace_regex_patrial.items():
            stripped_column = column.replace(".", "_").strip()
            df = df.withColumn(
                stripped_column, regexp_replace(col(stripped_column), pattern, "")
            )
    df = _replace(df, config.replace_with_none, config.path)
    df = _replace_regex(df, config.replace_regex_with_none, config.path)
    if config.filter:
        df = df.filter(resolve(config.filter))
    return df
