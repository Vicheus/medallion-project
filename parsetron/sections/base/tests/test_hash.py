import pytest
from pyspark.sql import SparkSession, DataFrame

from parsetron.engine.constants import ColumnTypes
from parsetron.engine.utils.hash import check_hash_collisions


@pytest.fixture(scope="session")
def spark() -> SparkSession:
    """Fixture to create a SparkSession for the duration of the test session."""
    return (
        SparkSession.builder.master("local[1]")
        .appName("pytest-pyspark-testing")
        .getOrCreate()
    )


@pytest.fixture
def clean_data(spark: SparkSession) -> DataFrame:
    data = [("hash1", "alpha"), ("hash2", "beta"), ("hash3", "gamma")]
    return spark.createDataFrame(data, [ColumnTypes.SOURCE_ENTITY_ID.value, "content"])


@pytest.fixture
def type1_collision_data(spark: SparkSession) -> DataFrame:
    data = [("hash1", "alpha"), ("hash2", "beta"), ("hash1", "gamma")]
    return spark.createDataFrame(data, [ColumnTypes.SOURCE_ENTITY_ID.value, "content"])


@pytest.fixture
def type2_collision_data(spark: SparkSession) -> DataFrame:
    data = [
        ("hash1", "alpha"),
        ("hash2", "alpha"),
        ("hash3", "beta"),
        ("hash4", "alpha"),
    ]
    return spark.createDataFrame(data, [ColumnTypes.SOURCE_ENTITY_ID.value, "content"])


@pytest.fixture
def empty_data(spark: SparkSession) -> DataFrame:
    return spark.createDataFrame(
        [], f"{ColumnTypes.SOURCE_ENTITY_ID.value}: string, content: string"
    )


def test_check_hash_collisions_success(clean_data: DataFrame):
    try:
        check_hash_collisions(clean_data)
    except ValueError:
        pytest.fail("ValueError was raised unexpectedly on clean data!")


def test_check_hash_collisions_empty(empty_data: DataFrame):
    try:
        check_hash_collisions(empty_data)
    except ValueError:
        pytest.fail("ValueError was raised unexpectedly on empty data!")


def test_check_hash_collisions_type1_fails(type1_collision_data: DataFrame):
    with pytest.raises(ValueError) as exec_info:
        check_hash_collisions(type1_collision_data)
    assert "Detected 2 hash collisions" == str(exec_info.value)


def test_check_hash_collisions_type2_fails(type2_collision_data: DataFrame):
    with pytest.raises(ValueError) as exec_info:
        check_hash_collisions(type2_collision_data)
    assert "Detected 3 hash collisions" == str(exec_info.value)


def test_check_hash_collisions_mixed_fails(spark: SparkSession):
    data = [("h1", "a"), ("h1", "b"), ("h2", "c"), ("h3", "c")]
    df = spark.createDataFrame(data, [ColumnTypes.SOURCE_ENTITY_ID.value, "content"])
    with pytest.raises(ValueError):
        check_hash_collisions(df)
