import logging

from pyspark.sql import DataFrame, Window
from pyspark.sql.functions import count, col, lit, count_distinct

from parsetron.engine.constants import ColumnTypes, TempColumnNames

logger = logging.getLogger(__name__)


def check_hash_collisions(df: DataFrame, ignore_hash_error: bool = False) -> None:
    """
    Validates the DataFrame for hash collisions and identity inconsistencies.

    If anomalies are found, it prints them to stdout and raises a ValueError.
    If no anomalies are found, it completes silently.

    Args:
        df: The input DataFrame to validate.
        ignore_hash_error: Mark to throw exception if hash collision detected

    Raises:
        ValueError: If any hash collisions or identity inconsistencies are detected.
    """
    if df.isEmpty():
        logger.warning("Input DataFrame is empty, nothing to validate")
        return

    hash_col = ColumnTypes.SOURCE_ENTITY_ID.value
    issue_type_col = TempColumnNames.ISSUE_TYPE.value
    identity_cols = [c for c in df.columns if c != hash_col]

    window_hash = Window.partitionBy(hash_col)
    collisions1 = (
        df.withColumn(
            TempColumnNames.HASH_OCCURRENCE.value, count("*").over(window_hash)
        )
        .filter(col(TempColumnNames.HASH_OCCURRENCE.value) > 1)
        .withColumn(issue_type_col, lit("Same Hash, Diff Content"))
    )

    anomalies2 = (
        df.groupBy(identity_cols)
        .agg(count_distinct(hash_col).alias(TempColumnNames.HASH_OCCURRENCE.value))
        .filter(col(TempColumnNames.HASH_OCCURRENCE.value) > 1)
    )
    collisions2 = df.join(anomalies2, on=identity_cols, how="inner").withColumn(
        issue_type_col, lit("Same Content, Diff Hash")
    )
    output_cols = [issue_type_col, hash_col] + identity_cols
    all_collisions = collisions1.select(output_cols).union(
        collisions2.select(output_cols)
    )

    anomaly_count = all_collisions.count()
    if anomaly_count > 0:
        error_msg = f"Detected {anomaly_count} hash collisions"
        logger.warning(error_msg)
        all_collisions.orderBy(issue_type_col, hash_col).show(10, truncate=False)
        if not ignore_hash_error:
            raise ValueError(error_msg)
    else:
        logger.info("Hash collision check passed successfully")
