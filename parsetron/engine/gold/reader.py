import os
from pathlib import Path

from pyspark.sql import SparkSession, DataFrame

from parsetron.engine.utils.path import find_date_dir


class Reader:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def read_all(self, path: str) -> dict[str, DataFrame]:
        datasets = {}
        ingest_date_dir = find_date_dir(path)
        in_path = Path(os.path.join(path, ingest_date_dir))

        if not in_path.exists():
            raise FileNotFoundError(f"Input path not found: {path}")

        for entity_dir in in_path.iterdir():
            if not entity_dir.is_dir():
                continue
            datasets[entity_dir.name] = self.spark.read.parquet(str(entity_dir))

        return datasets

    def read_all_groups(self, path: str) -> dict[str, dict[str, DataFrame]]:
        datasets = {}
        ingest_date_dir = find_date_dir(path)
        in_path = Path(os.path.join(path, ingest_date_dir))

        if not in_path.exists():
            raise FileNotFoundError(f"Input path not found: {path}")

        for entity_dir in in_path.iterdir():
            if not entity_dir.is_dir():
                continue
            if entity_dir.name.startswith("group_id="):
                datasets[entity_dir.name[9:]] = {}
                for nested_dir in entity_dir.iterdir():
                    if not entity_dir.is_dir():
                        continue
                    datasets[entity_dir.name[9:]][nested_dir.name] = (
                        self.spark.read.parquet(str(nested_dir))
                    )

        return datasets
