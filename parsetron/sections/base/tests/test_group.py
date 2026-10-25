import pytest
from pyspark.sql import SparkSession, DataFrame

from parsetron.engine.constants import ColumnTypes
from parsetron.engine.registry.transformations.group import ActualityGroupByOp


class DataFrameComparator:
    """
    A utility class for asserting equality between two PySpark DataFrames,
    including schema validation and detailed error reporting.
    """

    @staticmethod
    def assert_df_equal(actual_df: DataFrame, expected_df: DataFrame):
        actual_schema = actual_df.schema
        expected_schema = expected_df.schema

        if actual_schema != expected_schema:
            actual_cols = [(f.name, f.dataType) for f in actual_schema]
            expected_cols = [(f.name, f.dataType) for f in expected_schema]
            raise AssertionError(
                f"Schema mismatch!\n"
                f"Expected: {expected_cols}\n"
                f"Actual:   {actual_cols}"
            )

        sort_columns = actual_df.columns
        actual_sorted = actual_df.orderBy(sort_columns).collect()
        expected_sorted = expected_df.orderBy(sort_columns).collect()

        if actual_sorted != expected_sorted:
            actual_set = set(actual_sorted)
            expected_set = set(expected_sorted)
            diff_in_actual = actual_set - expected_set
            diff_in_expected = expected_set - actual_set

            error_msg = "DataFrame content mismatch!\n"
            if diff_in_actual:
                error_msg += (
                    f"Rows found in ACTUAL but missing in EXPECTED: {diff_in_actual}\n"
                )
            if diff_in_expected:
                error_msg += f"Rows found in EXPECTED but missing in ACTUAL: {diff_in_expected}\n"

            raise AssertionError(error_msg)


@pytest.fixture(scope="session")
def spark():
    """Fixture to create a SparkSession for the duration of the test session."""
    return (
        SparkSession.builder.master("local[1]")
        .appName("RegistryGroupTest")
        .getOrCreate()
    )


@pytest.fixture
def transformer():
    return ActualityGroupByOp(op="actualityGroupBy")


def test_apply(spark, transformer):
    expected_data = [("1", "2023-05-01", "A"), ("2", "2023-01-01", "C")]
    expected_schema = [
        "id",
        ColumnTypes.ACTUALITY.value,
        ColumnTypes.SOURCE_ENTITY_ID.value,
    ]
    expected_df = spark.createDataFrame(expected_data, expected_schema)

    data = [
        ("1", "2023-01-01", "B"),
        ("1", "2023-05-01", "A"),
        ("2", "2023-01-01", "C"),
    ]
    schema = ["id", ColumnTypes.ACTUALITY.value, ColumnTypes.SOURCE_ENTITY_ID.value]
    df = spark.createDataFrame(data, schema)

    actual_df = transformer.apply(df, ["id"])
    DataFrameComparator.assert_df_equal(actual_df, expected_df)


def test_apply_multiple_grouping_columns(spark, transformer):
    expected_data = [("1", "A", "2023-01-02", "A"), ("1", "B", "2023-01-01", "C")]
    expected_schema = [
        "id",
        "category",
        ColumnTypes.ACTUALITY.value,
        ColumnTypes.SOURCE_ENTITY_ID.value,
    ]
    expected_df = spark.createDataFrame(expected_data, expected_schema)

    data = [
        ("1", "A", "2023-01-01", "B"),
        ("1", "A", "2023-01-02", "A"),
        ("1", "A", None, "D"),
        ("1", "B", "2023-01-01", "C"),
    ]
    schema = [
        "id",
        "category",
        ColumnTypes.ACTUALITY.value,
        ColumnTypes.SOURCE_ENTITY_ID.value,
    ]
    df = spark.createDataFrame(data, schema)

    actual_df = transformer.apply(df, ["id", "category"])
    DataFrameComparator.assert_df_equal(actual_df, expected_df)
