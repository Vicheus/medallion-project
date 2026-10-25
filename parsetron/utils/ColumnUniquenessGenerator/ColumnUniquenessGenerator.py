from splink.exploratory import profile_columns
from splink import DuckDBAPI

import json


class ColumnUniquenessGenerator:
    """
    The ColumnUniquenessGenerator class is designed to generate statistics about uniqueness of each spark dataframe column in Dictionary format.
    Using Splink library class analyze dataframe and provide statistics about abount of distinct rows for each column.
    E.g. email - 0.8, phone - 0.63, which means that email column has 80% of unique values, phone column has 63% of unique values

    Key functionalities of the class include:
    - Create profile columns chart based on DF using Splink.
    - Provide column uniqueness in dictionary format.
    """

    def generate_columns_uniqueness_stats(self, df):
        profile_columns_chart_data = profile_columns(
            df.toPandas(), db_api=DuckDBAPI(), top_n=10, bottom_n=5
        )
        parsed_data = json.loads(profile_columns_chart_data.to_json())

        distinct_percentage = {}
        for section in parsed_data.get("vconcat", []):
            for hconcat_item in section.get("hconcat", []):
                values = hconcat_item["data"].get("values", [])

                for entry in values:
                    distinct_value_count = entry.get("distinct_value_count", 0)
                    total_non_null_rows = entry.get("total_non_null_rows", 0)
                    group_name = entry.get("group_name", "Unknown")

                    if total_non_null_rows > 0:
                        percentage_distinct = distinct_value_count / total_non_null_rows
                    else:
                        percentage_distinct = 0

                    distinct_percentage[group_name] = percentage_distinct

        return distinct_percentage
