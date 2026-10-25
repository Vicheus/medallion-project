from pyspark.sql.functions import explode, hash
from pyspark.sql.types import ArrayType
import pprint


class DatasetComparer:
    def try_find_values(self, field, df_field_values, compare_to_dataset):
        print(field)
        compare_to_df_field_values = (
            compare_to_dataset.select(
                explode(compare_to_dataset[field]).alias("values")
            )
            .dropDuplicates()
            .select("values")
            .rdd.flatMap(lambda x: x)
            .collect()
        )

        return set(compare_to_df_field_values).intersection(df_field_values)

    def check_row_uniqueness(self, fields, compare_to_dataset, df):
        df_hashes = df.select(hash(*fields.keys())).rdd.flatMap(lambda x: x).collect()
        compare_to_df_hashes = (
            compare_to_dataset.select(hash(*fields.values()))
            .rdd.flatMap(lambda x: x)
            .collect()
        )

        return len(set(df_hashes).intersection(compare_to_df_hashes))

    def compare_df_uniqueness(
        self, df, fields_to_check_mapping, percent_of_data_to_check, compare_to_datasets
    ):
        number_of_values_to_check = round(df.count() * (percent_of_data_to_check / 100))
        fields_uniqueness = {}

        for field_info in fields_to_check_mapping:
            df_field, compare_to_df_field = field_info

            df_field_values = []
            if isinstance(df.schema[df_field].dataType, ArrayType):
                values_df = df.select(explode(df[df_field]).alias("values"))
            else:
                values_df = df.select(df[df_field].alias("values"))

            df_field_values = (
                values_df.select("values")
                .dropDuplicates()
                .limit(number_of_values_to_check)
                .rdd.flatMap(lambda x: x)
                .collect()
            )

            values_found = []
            for compare_to_dataset in compare_to_datasets:
                values_found.extend(
                    self.try_find_values(
                        compare_to_df_field, df_field_values, compare_to_dataset
                    )
                )

            field_uniqueness_percentage = round(
                (
                    (number_of_values_to_check - len(values_found))
                    / number_of_values_to_check
                )
                * 100,
                2,
            )
            fields_uniqueness[df_field] = {
                "values_found": len(values_found),
                "field_uniqueness_percentage": field_uniqueness_percentage,
                "compared_values_count": len(df_field_values),
            }

        document_rows_uniqueness_hits = self.check_row_uniqueness(
            fields_to_check_mapping, compare_to_dataset, df
        )
        document_uniqueness_percentage = round(
            (df.count() - document_rows_uniqueness_hits) / df.count() * 100, 2
        )
        uniqueness_data = {
            "fields_uniqueness": fields_uniqueness,
            "document_uniqueness_hits": document_rows_uniqueness_hits,
            "document_uniqueness_percentage": document_uniqueness_percentage,
        }

        pprint.pprint(uniqueness_data)
