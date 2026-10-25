import json
import argparse
from parsetron import Parsetron
from parsetron.settings import JSON_FORCES_SCHEMA_VALIDATOR_PATH

from parsetron.utils.ForcesProcessor import ForcesProcessor


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    calc_completeness: bool = False
    dataset_code_name: str = 'forces_20241014'

    def parser(self):
        date_format = '%m/%d/%Y'
        with open(self.mapping_filepath, "r") as f:
            mapping = json.load(f)
        with open(JSON_FORCES_SCHEMA_VALIDATOR_PATH, "r") as f:
            schema = json.load(f)

        df = self.read(path=self.input_filepath, sep=self.delimiter)

        processor = ForcesProcessor(mapping, schema, date_format)

        df_transformed = processor.build_df(df, self.props_to_aggregate, self.props_to_group_by)
        df_transformed.show(truncate=False)

        return df_transformed

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run ProjectParsetron parser.")
    parser.add_argument('--input_filepath', type=str, required=True, help='Input file path')
    parser.add_argument('--mapping_filepath', type=str, required=True, help='Mapping file path')
    parser.add_argument('--delimiter', type=str, required=True, help='Delimiter')
    parser.add_argument('--props_to_group_by', type=str, required=False, help='Delimiter')
    parser.add_argument('--props_to_aggregate', type=str, required=False, help='Delimiter')

    args = parser.parse_args()

    parsetron = ProjectParsetron()

    parsetron.input_filepath = args.input_filepath
    parsetron.mapping_filepath = args.mapping_filepath
    parsetron.delimiter = args.delimiter
    parsetron.props_to_aggregate = args.props_to_aggregate
    parsetron.props_to_group_by = args.props_to_group_by

    parsetron.run()
