import logging
from pathlib import Path


def rename_ingest_date_dir(
    logger: logging.Logger, base_path: str, ingest_date: str
) -> None:
    basedir = Path(base_path)

    if basedir.exists():
        dirs = [
            d
            for d in basedir.iterdir()
            if d.is_dir()
            and d.name.startswith("ingest_date=")
            and not d.name.endswith(ingest_date)
        ]
        if dirs:
            if len(dirs) > 1:
                logger.error(f"{base_path} has ambiguous dirs to rename: {dirs}")
                raise ValueError(f"{base_path} has ambiguous dirs to rename: {dirs}")
            dir_to_rename = dirs[0]
            new_dir = dir_to_rename.parent / f"ingest_date={ingest_date}"
            logger.info(f"{dir_to_rename.name} will be renamed to {new_dir.name}")
            dir_to_rename.rename(new_dir)
            return

    logger.debug(f"{base_path} has no dirs to rename")


def find_date_dir(base_dir: str):
    basedir = Path(base_dir)
    if basedir.exists():
        dirs = [
            d
            for d in basedir.iterdir()
            if d.is_dir() and d.name.startswith("ingest_date=")
        ]
        if dirs:
            if len(dirs) > 1:
                raise ValueError(f"{basedir} has ambiguous dirs to read: {dirs}")
            return dirs[0].name
    raise ValueError(f"There is no directory to get data in {basedir}")
