import json
import os
import shutil
import sys
import tempfile
import urllib.request
from functools import reduce
from typing import Optional

import pandas as pd
import requests
from minio import Minio
from minio.error import S3Error
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import (
    col,
    when,
    lit,
    regexp_replace,
    explode,
    size,
    trim,
    expr,
    monotonically_increasing_id,
    first,
    lower,
)
from pyspark.sql.types import StructType, ArrayType

from .settings import (
    APP_NAME,
    DATAFRAME_TEST_LIMIT,
    SPARK_SETTINGS,
    DATA_OUTPUT_DIR,
    DATA_INPUT_DIR,
    DATASETS_DIR,
    DATASET_FILE_NAME,
    MEDIA_OUTPUT_DIR,
    MINIO_HOSTS,
    MINIO_ACCESS_KEY,
    MINIO_SECRET_KEY,
    MINIO_MEDIA_FILES_BUCKET_NAME,
    DATASET_COUNTRY_CODE,
    ANALYZER_API_HOSTS,
    DATE_FORMAT,
    SPARK_DATE_FORMAT,
)
from .utils import (
    JsonSchemaValidator,
    ReadmeGenerator,
    DatasetComparer,
    ColumnCompletenessGenerator,
    ColumnUniquenessGenerator,
)
from .utils.ReadmeGenerator.types import ReadmeDataset


class Parsetron:
    test_mode: bool = False
    forces_mode: bool = False
    compression: Optional[str] = "gzip"
    output_file_count: int = 1
    output_files_url: str = ""
    dataset_code_name: str = None
    data_sample_size: int = 20
    contains_media_files: bool = False
    media_folder_name: str = ""
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.RU
    calc_completeness: bool = True
    validate_invalid_groupping: bool = False
    write_filtered_rows: bool = False
    important_columns_for_filtering: str = ""
    actualize_geo_entity_dictionary: bool = False

    def __init__(self):
        if self.dataset_code_name is None:
            raise ValueError("dataset_code_name must be defined")

        self._entry_point = self._get_entry_point_path()
        self._spark = self._init_spark_session()

        self.schema_raw = []
        self.schema_final = None

        if self.test_mode:
            self.output_file_count = 1
            self.compression = None

    def read(
        self,
        path: Optional[str] = "",
        header: bool = True,
        sep: Optional[str] = ",",
        schema: Optional[StructType] = None,
        encoding: Optional[str] = "UTF-8",
    ) -> DataFrame:
        file_extension = self._get_file_extension(path)
        full_path = ""
        if self.output_files_url != "":
            full_path = path
        else:
            full_path = os.path.join(DATA_INPUT_DIR, path)

        if file_extension in [".csv", ".txt"]:
            df = self._spark.read.csv(
                path=full_path,
                header=header,
                inferSchema=True,
                sep=sep,
                schema=schema,
                encoding=encoding,
                escape='"',
            )
        elif file_extension == ".json":
            df = self._spark.read.json(path=full_path, schema=schema, encoding=encoding)
        elif file_extension == ".parquet":
            df = self._spark.read.format("parquet").load(full_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

        if self.test_mode:
            print(f"""Limit DF to: {DATAFRAME_TEST_LIMIT}""")
            df = df.limit(DATAFRAME_TEST_LIMIT)

        self.schema_raw.append(
            ReadmeDataset(
                code_name=self.dataset_code_name,
                path=path,
                total=df.count(),
                schema=df._jdf.schema().treeString(),
                data_sample=df.limit(self.data_sample_size)
                .toPandas()
                .to_markdown(index=False),
            )
        )

        df = self.clean_columns(df)
        df.show(n=20, truncate=False)

        return df

    def read_file_from_url(
        self, url, file_extension, separator, header, schema, encoding
    ):
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=file_extension)
        urllib.request.urlretrieve(url, tmp_file.name)

        df = self._spark.read.csv(tmp_file.name, header=True, inferSchema=True)
        if file_extension in [".csv", ".txt"]:
            df = self._spark.read.csv(
                path=tmp_file.name,
                header=header,
                inferSchema=True,
                sep=separator,
                schema=schema,
                encoding=encoding,
            )
        elif file_extension == ".json":
            df = self._spark.read.json(
                path=tmp_file.name, schema=schema, encoding=encoding
            )
        return df

    def clean_columns(self, df: DataFrame):
        for col_name in df.columns:
            new_col_name = col_name.replace('"', "").strip()
            df = df.withColumnRenamed(col_name, new_col_name)

        for column in df.columns:
            if isinstance(df.schema[column].dataType, StructType) or isinstance(
                df.schema[column].dataType, ArrayType
            ):
                continue
            df = df.withColumn(
                column,
                when(
                    trim(
                        regexp_replace(col(column), r"^\s*[\'\"]+|\s*[\'\"]+$", "")
                    ).eqNullSafe(""),
                    lit(None),
                ).otherwise(
                    trim(regexp_replace(col(column), r"^\s*[\'\"]+|\s*[\'\"]+$", ""))
                ),
            )

        return df

    def write(self, df: DataFrame, filtered_out_rows_run: bool = False):
        df = df.coalesce(self.output_file_count)
        dataset_code_name = (
            f"{self.dataset_code_name}_filtered_out"
            if filtered_out_rows_run
            else self.dataset_code_name
        )
        if self.output_files_url != "":
            df.write.json(
                path=self.output_files_url,
                mode="overwrite",
                compression=self.compression,
                dateFormat=SPARK_DATE_FORMAT,
            )
        else:
            output_dir = os.path.join(DATA_OUTPUT_DIR, dataset_code_name)
            df.write.json(
                path=output_dir,
                mode="overwrite",
                compression=self.compression,
                dateFormat=SPARK_DATE_FORMAT,
            )

    def write_media(self, df_media: DataFrame):
        """
        Create local files\folder structure for media files of dataset and write them to external file storage
        """
        pandas_df = df_media.toPandas()
        for index, row in pandas_df.iterrows():
            self.move_media_file(row, self.media_folder_name, self.dataset_code_name)
        self.store_media_in_storage(self)

    def parser(self):
        """
        Parser method. Must be implemented in child classes.
        """
        raise NotImplementedError("Parser method must be implemented")

    def link_media_files(self):
        """
        Media files linkage method.
        Method should prepare dataframe with linkage between dataset rows and media files for each row
        Look at Media section in documentation for more info about dataset structure
        Must be implemented in child classes.
        """
        raise NotImplementedError("link_media_files method must be implemented")

    def run(self):
        df = self.parser()
        if self.contains_media_files:
            if not self.media_folder_name:
                print("""media_folder_name property should not be empty""")
            df_media = self.link_media_files(df)
            self.write_media(df_media)
        df.printSchema()
        self._actualize_geo_entity_dictionary(df)

        if self.important_columns_for_filtering:
            if self.write_filtered_rows:
                print(
                    f"CHECK FILTERED OUT ROWS BY COLUMNS {self.important_columns_for_filtering}"
                )
                non_null_sum_expr = reduce(
                    lambda a, b: a + b,
                    [
                        when(col(c).isNotNull(), 1).otherwise(0)
                        for c in self.important_columns_for_filtering.split(",")
                    ],
                )
                df_filtered_out = df.filter(
                    (col("names").isNull()) & (non_null_sum_expr >= 2)
                )
                print(f"FILTERED OUT COUNT: {df_filtered_out.count()}")
                self.write(df_filtered_out, filtered_out_rows_run=True)

            columns = [
                col_name.strip()
                for col_name in self.important_columns_for_filtering.split(",")
                if col_name.strip()
            ]
            or_condition = reduce(
                lambda a, b: a | b, [col(c).isNotNull() for c in columns]
            )
            final_condition = col("names").isNotNull() & or_condition
            df = df.filter(final_condition)

        df.show(n=100, truncate=False)

        self.write(df)

        completeness_stats, df_size = (
            self._calculate_dataset_columns_completeness(df)
            if self.calc_completeness
            else (None, None)
        )

        if self.test_mode:
            self._validate_json(self.forces_mode)
            self._validate_columns_completeness(completeness_stats)
            self._validate_columns_uniqueness(self, df)

        if self.validate_invalid_groupping:
            self._validate_invalid_groupping_for_columns(df)

        if self.forces_mode:
            return

        if not df_size:
            df_size = df.count()

        df_schema = df._jdf.schema().treeString()
        pandas_df = df.limit(self.data_sample_size).toPandas()
        if "actuality" in pandas_df.columns:
            pandas_df["actuality"] = pd.to_datetime(pandas_df["actuality"])
            pandas_df["actuality"] = pandas_df["actuality"].dt.strftime(DATE_FORMAT)
            pandas_df["actuality"] = pandas_df["actuality"].fillna("")

        schema_final = ReadmeDataset(
            total=df_size,
            schema=df_schema,
            columns_completeness=self._beautify_dataset_columns_completeness_stats(
                completeness_stats
            ),
            data_sample=pandas_df.to_markdown(index=False),
        )

        readme_generator = ReadmeGenerator(dataset_code_name=self.dataset_code_name)
        readme_generator.generate_git_readme(
            schema_raw=self.schema_raw, schema_final=schema_final
        )
        readme_generator.generate_ds_documentation_readme(
            schema_raw=self.schema_raw, schema_final=schema_final
        )

        self._copy_entry_point_file()

    def compare_dataset_uniqueness(
        self, df, fields_to_check_mapping, percent_of_data_to_check, compare_to_datasets
    ):
        dataset_comparer = DatasetComparer()
        dataset_comparer.compare_df_uniqueness(
            df, fields_to_check_mapping, percent_of_data_to_check, compare_to_datasets
        )

    def show_dataset_columns_completeness(self, df):
        print("Columns completeness:")
        completeness_stats, _ = self._calculate_dataset_columns_completeness(df)
        print(self._beautify_dataset_columns_completeness_stats(completeness_stats))

    def show_dataset_columns_uniqueness(self, df):
        print("Columns uniqueness:")
        uniqueness_stats = self._calculate_dataset_columns_uniqueness(df)
        print(self._beautify_dataset_columns_uniqueness_stats(uniqueness_stats))

    def _actualize_geo_entity_dictionary(self, df):
        """
        Actualize geo entity values in dictionary, if address column presented in processed dataset
        Method explode normalize_address column and create map like: geo_entity_type(street,city,...):geo_entity_name(New York, Preston street, ...)
        If geo_entity not in dictionary yet, method store it
        """

        if ("normalized_address" in df.columns) & self.actualize_geo_entity_dictionary:
            df = df.repartition(200)
            df_address_keys_values = df.withColumn(
                "key_value_pairs",
                expr("""
                    transform(normalized_address, x -> 
                        map(
                            'region_value', x.location.region_value, 'region_type', x.location.region_type, 
                            'settlement_region_value', x.location.settlement_region_value, 'settlement_region_type', x.location.settlement_region_type, 
                            'settlement_value', x.location.settlement_value, 'settlement_type', x.location.settlement_type, 
                            'street_value', x.location.street_value, 'street_type', x.location.street_type
                        )
                    )
                """),
            )

            df_address_keys_values = df_address_keys_values.withColumn(
                "key_value", explode(col("key_value_pairs"))
            ).withColumn("id", monotonically_increasing_id())
            df_address_keys_values = df_address_keys_values.select(
                "id", explode(col("key_value")).alias("key", "value")
            )

            df_regions = df_address_keys_values.filter(
                col("key").isin("region_value", "region_type")
            )
            df_regions = df_regions.groupBy("id").pivot("key").agg(first("value"))
            df_regions = df_regions.withColumnRenamed(
                "region_value", "name"
            ).withColumnRenamed("region_type", "type")

            df_settlement_regions = df_address_keys_values.filter(
                col("key").isin("settlement_region_value", "settlement_region_type")
            )
            df_settlement_regions = (
                df_settlement_regions.groupBy("id").pivot("key").agg(first("value"))
            )
            df_settlement_regions = df_settlement_regions.withColumnRenamed(
                "settlement_region_value", "name"
            ).withColumnRenamed("settlement_region_type", "type")

            df_settlements = df_address_keys_values.filter(
                col("key").isin("settlement_value", "settlement_type")
            )
            df_settlements = (
                df_settlements.groupBy("id").pivot("key").agg(first("value"))
            )
            df_settlements = df_settlements.withColumnRenamed(
                "settlement_value", "name"
            ).withColumnRenamed("settlement_type", "type")

            df_streets = df_address_keys_values.filter(
                col("key").isin("street_value", "street_type")
            )
            df_streets = df_streets.groupBy("id").pivot("key").agg(first("value"))
            df_streets = df_streets.withColumnRenamed(
                "street_value", "name"
            ).withColumnRenamed("street_type", "type")

            df_address_keys_values = (
                df_regions.unionAll(df_settlement_regions)
                .unionAll(df_settlements)
                .unionAll(df_streets)
            )

            df_address_keys_values = df_address_keys_values.filter(
                col("name").isNotNull()
            ).withColumn("name", lower(col("name")))

            def chunk_data(data, chunk_size=1000):
                for i in range(0, len(data), chunk_size):
                    yield data[i : i + chunk_size]

            def send_bulk_create_request(data):
                headers = {
                    "Content-Type": "application/json",
                }
                payload = {"data": data}
                print(payload)
                api_url = f"{ANALYZER_API_HOSTS}api/addressEntries/bulk-create/"

                response = requests.post(
                    api_url, headers=headers, data=json.dumps(payload)
                )

                if response.status_code == 201:
                    print(f"Successfully created {len(data)} records.")
                else:
                    print(
                        f"Failed to create records. Status Code: {response.status_code}"
                    )
                    print(response.json())

            data = [
                {"name": row["name"], "type": row["type"]}
                for row in df_address_keys_values.collect()
            ]
            for chunk in chunk_data(data, chunk_size=1000):
                print("""Send chunk""")
                send_bulk_create_request(chunk)

            print(
                f"geo entities df prepared, number of pairs: {df_address_keys_values.count()} writing..."
            )

            # drop normalized_address column, because string representation of normalized_address already in address column
            df.drop("normalized_address")
        else:
            print("column normalized_address not in columns list")

    def _copy_entry_point_file(self):
        """
        Copies the main file to the dataset directory.
        """
        source_file = os.path.abspath(sys.modules["__main__"].__file__)
        shutil.copy(source_file, self._entry_point)

    def _get_entry_point_path(self):
        """
        Returns the path to the dataset file.
        """
        return os.path.join(DATASETS_DIR, self.dataset_code_name, DATASET_FILE_NAME)

    @staticmethod
    def _init_spark_session():
        """
        Initializes the Spark session with spark cluster settings.
        """
        builder = SparkSession.builder.appName(APP_NAME)

        for key, value in SPARK_SETTINGS.items():
            builder = builder.config(key, value)

        return builder.getOrCreate()

    @staticmethod
    def _validate_json(forces_mode):
        """
        Validates JSON using JsonSchemaValidator.
        """
        validator = JsonSchemaValidator(use_forces_schema=forces_mode)
        validator.validate()

    @staticmethod
    def _validate_columns_completeness(completeness_stats):
        """
        Validates Columns completeness using ColumnCompletenessGenerator.
        """
        if not completeness_stats:
            return
        min_completeness_for_column = 0.05
        for key, value in completeness_stats.items():
            if value < min_completeness_for_column:
                print(f"""{key} column completeness is lower then threshold: {value}""")

    @staticmethod
    def _calculate_dataset_columns_completeness(df) -> tuple[dict[str, str], int]:
        completeness_stats_generator = ColumnCompletenessGenerator()
        completeness_stats = (
            completeness_stats_generator.generate_columns_completeness_stats(df)
        )

        return completeness_stats

    @staticmethod
    def _beautify_dataset_columns_completeness_stats(
        dataset_columns_completeness_stats,
    ):
        if not dataset_columns_completeness_stats:
            return None
        columns_completeness_beautified = {
            key: round(value * 100, 2) if isinstance(value, (int, float)) else value
            for key, value in dataset_columns_completeness_stats.items()
        }
        return columns_completeness_beautified

    @staticmethod
    def _validate_columns_uniqueness(self, df):
        """
        Validates Columns uniqueness using ColumnUniquenessGenerator.
        """
        min_uniqueness_for_column = 0.05
        uniqueness_stats = self._calculate_dataset_columns_uniqueness(df)
        for key, value in uniqueness_stats.items():
            if value < min_uniqueness_for_column:
                print(f"""{key} column uniqueness is lower then threshold: {value}""")

    @staticmethod
    def _calculate_dataset_columns_uniqueness(df):
        generator = ColumnUniquenessGenerator()
        uniqueness_stats = generator.generate_columns_uniqueness_stats(df)

        return uniqueness_stats

    @staticmethod
    def _validate_invalid_groupping_for_columns(df, threshold=10):
        """
        Check array fields in df, if some field contains more than 10 entries in array - show warning
        """
        array_columns = [
            f.name for f in df.schema.fields if isinstance(f.dataType, ArrayType)
        ]

        for array_col in array_columns:
            oversized_df = df.filter(size(col(array_col)) > threshold).select(
                "names", size(col(array_col)).alias("count")
            )

            oversized = oversized_df.collect()
            for row in oversized:
                print(
                    f"⚠️ Warning: Field '{array_col}' has {row['count']} entries for names = {row['names']}"
                )

    @staticmethod
    def _beautify_dataset_columns_uniqueness_stats(dataset_columns_uniqueness_stats):
        columns_uniqueness_beautified = {
            key: round(value * 100, 2) if isinstance(value, (int, float)) else value
            for key, value in dataset_columns_uniqueness_stats.items()
        }
        return json.dumps(columns_uniqueness_beautified, indent=4)

    @staticmethod
    def _get_file_extension(path: str) -> str:
        """
        Gets the file extension.
        """
        if ".gz" in path:
            path = path.replace(".gz", "")
        _, file_extension = os.path.splitext(path)
        return file_extension

    @staticmethod
    def move_media_file(row, folder_name, dataset_code_name):
        """
        Create media files folders structure.
        Result structure is following:
        1.Main folder with name = dataset_code_name
        2.Nested folder with name = ds_internal_id per each dataset row
        3.Each row folder contains all media files for this row
        """
        raw_filename = row["raw_file_name"]
        new_filename = row["file_name"]
        document_id = row["ds_internal_id"]
        if not raw_filename:
            return

        raw_file_path = os.path.join(folder_name, raw_filename)
        new_folder_path = os.path.join(
            MEDIA_OUTPUT_DIR, folder_name, dataset_code_name, f"""{document_id}"""
        )

        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        new_file_path = os.path.join(new_folder_path, new_filename)

        if os.path.exists(raw_file_path):
            shutil.move(raw_file_path, new_file_path)
        else:
            print(f"""Not found raw_file at {raw_file_path}""")

    @staticmethod
    def store_media_in_storage(self):
        """
        Store media files inside external file storage.
        """
        minio_client = Minio(
            MINIO_HOSTS,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=False,
        )

        bucket_name = MINIO_MEDIA_FILES_BUCKET_NAME

        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)

        path = os.path.join(self.media_folder_name, self.dataset_code_name)

        uploaded_files_count = 0
        for root, dirs, files in os.walk(path):
            relative_path = os.path.relpath(root, path)

            for filename in files:
                file_path = os.path.join(root, filename)

                if relative_path == ".":
                    object_name = filename
                else:
                    object_name = os.path.join(
                        self.dataset_code_name, relative_path, filename
                    )

                try:
                    minio_client.fput_object(bucket_name, object_name, file_path)
                    uploaded_files_count = uploaded_files_count + 1
                except S3Error as e:
                    print(f"Error uploading {file_path}: {e}")
        print(
            f"Uploaded {uploaded_files_count} media files to {bucket_name}/{self.dataset_code_name}."
        )
