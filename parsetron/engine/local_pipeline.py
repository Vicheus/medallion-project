import logging
from argparse import ArgumentParser, Namespace
from pathlib import Path

from pyspark.sql import SparkSession

from parsetron.engine.bronze.pipeline import run_bronze
from parsetron.engine.config.base import PipelineConfig
from parsetron.engine.config.loader import load_source_config
from parsetron.engine.constants import StageTypes
from parsetron.engine.gold.pipeline import run_gold
from parsetron.engine.md import MdGenerator
from parsetron.engine.silver.pipeline import run_silver
from parsetron.engine.utils.spark import run_spark_app
from parsetron.engine.utils.splitter import split_by
from parsetron.engine.utils.track import track_start_command, track_execution_time
from parsetron.log import setup_logger

logger = logging.getLogger(__name__)


def collect_arguments() -> Namespace:
    parser = ArgumentParser(description="Local MVP pipeline: Bronze -> Silver -> Gold")
    parser.add_argument("source_config", type=str, help="Path to source YAML config")
    parser.add_argument(
        "output_dir", type=str, help="Base path for bronze/silver/gold outputs"
    )
    parser.add_argument(
        "--entities",
        type=str,
        default=None,
        help="Comma-separated list of entities to process",
    )
    parser.add_argument(
        "--group-ids",
        type=str,
        default=None,
        help="Comma-separated list of group ids to process",
    )
    parser.add_argument(
        "--stages",
        type=str,
        default=None,
        help="Comma-separated list of stages to run (bronze,silver,gold)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Integer value to return after reading process",
    )
    return parser.parse_args()


def run_stages(
    args: Namespace,
    spark: SparkSession,
    config: PipelineConfig,
    md_generator: MdGenerator,
):
    base_output = Path(args.output_dir)
    bronze_path = base_output / config.source_id / StageTypes.BRONZE.value
    silver_path = base_output / config.source_id / StageTypes.SILVER.value
    gold_path = base_output / config.source_id / StageTypes.GOLD.value

    bronze_path.mkdir(parents=True, exist_ok=True)
    silver_path.mkdir(parents=True, exist_ok=True)
    gold_path.mkdir(parents=True, exist_ok=True)
    bronze_path = str(bronze_path)
    silver_path = str(silver_path)
    gold_path = str(gold_path)

    if args.stages:
        stages = split_by(args.stages)
        md_generator = md_generator if StageTypes.GOLD.value in stages else None

        if StageTypes.BRONZE.value in stages:
            run_bronze(
                spark,
                config.source_entity_id_hash_type,
                config.bronze,
                bronze_path,
                args.group_ids,
                args.entities,
                md_generator,
                limit=args.limit,
            )
        elif md_generator:
            run_bronze(
                spark,
                "",
                config.bronze,
                "",
                "",
                "",
                md_generator,
                read_only=True,
                limit=args.limit,
            )
        if StageTypes.SILVER.value in stages:
            run_silver(
                spark,
                config.silver,
                bronze_path,
                silver_path,
                args.group_ids,
                args.entities,
            )
        if StageTypes.GOLD.value in stages:
            run_gold(
                spark,
                config.gold,
                config.source_entity_id_hash_type,
                bronze_path,
                silver_path,
                gold_path,
                md_generator,
            )
            md_generator.copy_config_file(args.source_config)
    else:
        run_bronze(
            spark,
            config.source_entity_id_hash_type,
            config.bronze,
            bronze_path,
            args.group_ids,
            args.entities,
            md_generator,
            limit=args.limit,
        )
        run_silver(
            spark,
            config.silver,
            bronze_path,
            silver_path,
            args.group_ids,
            args.entities,
        )
        run_gold(
            spark,
            config.gold,
            config.source_entity_id_hash_type,
            bronze_path,
            silver_path,
            gold_path,
            md_generator,
        )
        md_generator.copy_config_file(args.source_config)


@track_execution_time(logger, "Pipeline")
def main():
    args = collect_arguments()
    config = load_source_config(args.source_config)

    setup_logger(f"{config.source_id}.log")
    track_start_command(logger)

    md_generator = MdGenerator(config.source_id)
    app_run_func = lambda spark: run_stages(args, spark, config, md_generator)
    run_spark_app(logger, "IngestJob", app_run_func)

    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()
