import os
from environs import Env
from dotenv import load_dotenv
from enum import Enum

env = Env()
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

BASE_DIR = os.getcwd()
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

# Pyspark settings
APP_NAME = "Parsetron"

SPARK_SETTINGS = {
    "spark.master": env("SPARK_MASTER_ENDPOINT", default="local[4]"),
    "spark.driver.cores": "2",
    "spark.driver.memory": "10g",
    "spark.driver.maxResultSize": "16g",
    "spark.executor.cores": "2",
    "spark.executor.memory": "10g",
    "spark.executor.memoryOverhead": "4g",
    "spark.executor.instances": "2",
    "spark.memory.fraction": "0.5",
    "spark.memory.storageFraction": "0.3",
    "spark.local.dir": "/tmp/spark-temp",
    "spark.sql.shuffle.partitions": "200",
    "spark.serializer": "org.apache.spark.serializer.KryoSerializer",
    "spark.kryoserializer.buffer.max": "200m",
    "spark.executor.extraJavaOptions": "-XX:+UseG1GC",
    "spark.driver.extraJavaOptions": "-XX:+UseG1GC",
    "spark.hadoop.fs.s3a.endpoint": env("SPARK_S3A_ENDPOINT", default=""),
    "spark.hadoop.fs.s3a.access.key": env("SPARK_S3A_ACCESS_KEY", default=""),
    "spark.hadoop.fs.s3a.secret.key": env("SPARK_S3A_SECRET_KEY", default=""),
    "spark.hadoop.fs.s3a.path.style.access": "true",
    "spark.hadoop.fs.s3a.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
    "spark.hadoop.fs.s3a.connection.ssl.enabled": "false",
    "spark.executor.extraClassPath": "/opt/spark/jars/*",
}

# Test mode settings
DATAFRAME_TEST_LIMIT = 50

# Date formats
DATE_FORMAT = "%d.%m.%Y"
SPARK_DATE_FORMAT = "dd.MM.yyyy"
TIME_FORMAT = "%H:%M:%S"

# Data directory settings
DATA_INPUT_DIR = os.path.join(BASE_DIR, "data", "input")
DATA_OUTPUT_DIR = os.path.join(BASE_DIR, "data", "output")
MEDIA_OUTPUT_DIR = os.path.join(BASE_DIR, "media", "output")
DATASETS_DIR = os.path.join(BASE_DIR, "datasets")
DATASET_FILE_NAME = "processing.py"


# Json validator settings
JSON_SCHEMA_VALIDATOR_PATH = os.path.join(
    MODULE_DIR, "utils", "JsonSchemaValidator", "schema.json"
)
JSON_FORCES_SCHEMA_VALIDATOR_PATH = os.path.join(
    MODULE_DIR, "utils", "JsonSchemaValidator", "schema_forces.json"
)

# Address analyser settings
ADDRESS_ANALYZER_GEO_ENTITY_DICTIONARY_TEMP_PATH = os.path.join(
    MODULE_DIR, "utils", "AddressAnalyzer", "Dictionaries", "Temp"
)
ADDRESS_ANALYZER_GEO_ENTITY_DICTIONARY_PATH = os.path.join(
    MODULE_DIR, "utils", "AddressAnalyzer", "Dictionaries", "geo_entities.csv"
)
ADDRESS_ANALYZER_GEO_ENTITY_TYPES = [
    "край",
    "область",
    "муниципальный район",
    "городское поселение",
    "деревня",
    "поселок городского типа",
    "город",
    "посёлок",
    "поселок",
    "район",
    "микрорайон",
    "массив",
    "проезд",
    "переулок",
    "шоссе",
    "улица",
    "проспект",
    "бульвар",
    "тупик",
]
GEO_API_HOSTS = env("GEO_API_HOSTS")
ANALYZER_API_HOSTS = env("ANALYZER_API_HOSTS")
SEARCH_COORDINATES = False

# README generator settings
TEMPLATES_DIR = os.path.join(MODULE_DIR, "utils", "ReadmeGenerator", "templates")

# Minio settings
MINIO_HOSTS = env("MINIO_HOSTS", default="")
MINIO_ACCESS_KEY = env("MINIO_ACCESS_KEY", default="")
MINIO_SECRET_KEY = env("MINIO_SECRET_KEY", default="")
MINIO_MEDIA_FILES_BUCKET_NAME = env("MINIO_MEDIA_FILES_BUCKET_NAME", default="")


class DATASET_COUNTRY_CODE(Enum):
    RU = "RU"
    BY = "BY"
    KZ = "KZ"


# Documents analyzer settings
AGENT_HOSTS = env("AGENT_HOSTS", default="")
