import logging
from typing import Optional, Callable

from pyspark.sql import SparkSession

_DEFAULT_SPARK_PARAMS = {
    "spark.master": "local[6]",
    "spark.driver.memory": "10g",
    "spark.driver.maxResultSize": "16g",
    "spark.memory.fraction": "0.5",
    "spark.memory.storageFraction": "0.3",
    "spark.local.dir": "/tmp/spark-temp",
    "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
    "spark.executor.extraJavaOptions": "-XX:+UseG1GC",
    "spark.driver.extraJavaOptions": "-XX:+UseG1GC",
}


def create_spark_session(
    app_name: str, params: Optional[dict[str, str]] = None
) -> SparkSession:
    builder = SparkSession.builder.appName(app_name)
    if params:
        for key, value in params.items():
            builder.config(key, value)
        for key, value in _DEFAULT_SPARK_PARAMS.items():
            if key not in params:
                builder.config(key, value)
    else:
        for key, value in _DEFAULT_SPARK_PARAMS.items():
            builder.config(key, value)

    return builder.getOrCreate()


def run_spark_app(
    logger: logging.Logger, app_name: str, func: Callable[[SparkSession], None]
) -> None:
    spark_session: Optional[SparkSession] = None
    try:
        spark_session: SparkSession = create_spark_session(app_name)
        func(spark_session)
    except Exception as err:
        logger.error(f"{type(err)}: {err}")
        raise err
    finally:
        if spark_session:
            spark_session.stop()
            logger.debug("Spark session has been closed")
