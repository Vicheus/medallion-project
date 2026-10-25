import os.path
from typing import List, Dict

from jinja2 import Environment, FileSystemLoader

from parsetron.settings import TEMPLATES_DIR, DATASETS_DIR


class ReadmeGenerator:
    def __init__(self, dataset_code_name: str):
        dataset_dir = os.path.join(DATASETS_DIR, dataset_code_name)

        if not os.path.exists(dataset_dir):
            os.makedirs(dataset_dir, exist_ok=True)

        self._readme_path = os.path.join(dataset_dir, "README.md")
        self._documentation_path = os.path.join(dataset_dir, "DOCUMENTATION.md")
        self._env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
        self._template_git_readme = self._env.get_template("README.md")
        self._template_ds_documentation_readme = self._env.get_template(
            "DOCUMENTATION.md"
        )

    def generate_git_readme(
        self,
        schema_raw: List[Dict[str, int | str]],
        schema_final: Dict[str, int | str | dict],
    ):
        content = self._template_git_readme.render(
            schema_raw=schema_raw, schema_final=schema_final
        )
        self._write_file(self._readme_path, content)

    def generate_ds_documentation_readme(
        self,
        schema_raw: List[Dict[str, int | str]],
        schema_final: Dict[str, int | str | dict],
    ):
        content = self._template_ds_documentation_readme.render(
            schema_raw=schema_raw, schema_final=schema_final
        )
        self._write_file(self._documentation_path, content)

    def _write_file(self, path, content: str):
        with open(path, "w") as file:
            file.write(content)
