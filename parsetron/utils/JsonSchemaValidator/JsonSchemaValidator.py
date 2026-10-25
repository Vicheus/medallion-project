import os
import glob
import json
from jsonschema import validate, ValidationError

from parsetron.settings import (
    JSON_SCHEMA_VALIDATOR_PATH,
    JSON_FORCES_SCHEMA_VALIDATOR_PATH,
    DATA_OUTPUT_DIR,
)


class JsonSchemaValidator:
    """
    The JsonSchemaValidator class is designed to validate JSON documents in JSON lines format
    against a specified schema. The schema is loaded from a given file, and all JSON files found
    in a specified directory are checked for compliance with this schema. If a validation error
    occurs, a ValidationError is raised, allowing easy identification of invalid data.

    Key functionalities of the class include:
    - Loading a JSON schema from a file.
    - Searching for all JSON files in a specified directory.
    - Sequentially reading and validating each document.
    """

    def __init__(self, use_forces_schema):
        self._schema = self._read_schema(use_forces_schema)

    def validate(self):
        """
        Validate all JSON documents against the schema.
        """
        file_paths = self._find_json_files()

        for file_path in file_paths:
            documents = self._read_json(file_path)
            for i, document in enumerate(documents):
                try:
                    validate(instance=document, schema=self._schema)
                except ValidationError as e:
                    raise e

        print("Successfully validated")

    @staticmethod
    def _read_schema(use_forces_schema: bool):
        """
        Load and return the JSON schema from a file.
        """
        path = (
            JSON_FORCES_SCHEMA_VALIDATOR_PATH
            if use_forces_schema
            else JSON_SCHEMA_VALIDATOR_PATH
        )
        with open(path, "r") as file:
            return json.load(file)

    @staticmethod
    def _find_json_files():
        """
        Find all JSON files in the specified directory.
        """
        return glob.glob(os.path.join(DATA_OUTPUT_DIR, "*.json"))

    @staticmethod
    def _read_json(file_path: str):
        """
        Read a JSON lines file and yield each document.
        """
        with open(file_path, mode="r") as file:
            for line in file:
                yield json.loads(line)
