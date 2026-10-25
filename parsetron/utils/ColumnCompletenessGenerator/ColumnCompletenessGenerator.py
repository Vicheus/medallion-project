from pyspark.sql import DataFrame
from pyspark.sql.functions import when, count, col


class ColumnCompletenessGenerator:
    """
    Generates statistics about completeness of each spark dataframe column in Dictionary format.
    Analyzes dataframe and provides statistics about amount of filled rows for each column.
    E.g. email - 0.8, phone - 0.63, which means that email column filled in 80% of rows, phone column filled in 63% of rows.

    Key functionalities of the class include:
    - Create completeness chart based on DF.
    - Provide column completeness in dictionary format.
    """

    def generate_columns_completeness_stats(
        self, df: DataFrame
    ) -> tuple[dict[str, float], int]:
        total_rows = df.count()

        if total_rows == 0:
            return {}, 0

        non_null_counts = df.select(
            [count(when(col(c).isNotNull(), c)).alias(c) for c in df.columns]
        )
        completeness_percentage = non_null_counts.select(
            [(col(c) / total_rows).alias(c) for c in non_null_counts.columns]
        )

        completeness_map = {
            c: completeness_percentage.select(c).first()[0]
            for c in completeness_percentage.columns
        }
        completeness_dict = {key: value for key, value in completeness_map.items()}

        return completeness_dict, total_rows
