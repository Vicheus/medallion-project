import inspect
from typing import Dict, Any, List, get_type_hints

from pyspark.sql.functions import (
    col,
    lit,
    array,
    struct,
    expr,
    when,
    size,
    array_compact,
    flatten,
    collect_set,
    array_distinct,
    concat_ws,
)
from functools import reduce
from pyspark.sql.types import ArrayType, StructType
from pyspark.sql import DataFrame

from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    address_udf,
    address_with_type_udf,
    normalize_address_batch_udf,
    email_udf,
    phone_udf,
    actuality_date_udf,
)

from parsetron.sections.forces.udfs import forces_udf
from parsetron.sections.forces.validators.forces import forces

from parsetron.sections.medicals.udfs import medicals_udf
from parsetron.sections.medicals.validators.medicals import medicals

from parsetron.sections.awards.udfs import award_udf
from parsetron.sections.awards.validators.award import award

from parsetron.sections.conflicts.udfs import conflict_udf
from parsetron.sections.conflicts.validators.conflicts import conflict

from parsetron.sections.device.udfs import device_udf
from parsetron.sections.device.validators.device import device

from parsetron.sections.document.udfs import document_udf
from parsetron.sections.document.validators.document import document

from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.educations.validators.education import education

from parsetron.sections.financials.udfs import financial_udf
from parsetron.sections.financials.validators.financials import financial

from parsetron.sections.incidences.udfs import incidence_udf
from parsetron.sections.incidences.validators.incidence import incidence

from parsetron.sections.ips.udfs import ip_udf
from parsetron.sections.ips.validators.ip import ip

from parsetron.sections.movements.udfs import movement_udf
from parsetron.sections.movements.validators.movement import movement

from parsetron.sections.ownerships.udfs import ownership_udf
from parsetron.sections.ownerships.validators.ownership import ownership

from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.vehicles.validators.vehicle import vehicle

from parsetron.sections.violations.udfs import violation_udf
from parsetron.sections.violations.validators.violation import violation

from parsetron.sections.work.udfs import work_udf
from parsetron.sections.work.validators.work import work

"""
Processor class for building df based on provided mappings, schema, fields for groupping and filtering etc.
"""


class ForcesProcessor:

    def __init__(self, mapping, schema, date_format):
        self.mapping = mapping
        self.schema = schema
        self.date_format = date_format
        print(f"""Passed date format: {date_format}""")

        return

    """
    Dynamically build dataframe using provided mapping and result schema
    Automatically apply udf's
    Automatically apply groupping and filtering
    """

    def build_df(self, df: DataFrame, props_to_aggregate: str, props_to_group_by: str):
        result_fields = [
            self._build_column(df, field, spec)
            for field, spec in self.schema["properties"].items()
        ]

        df_transformed = df.select(*result_fields)
        df_transformed = self._clean_dataframe(df_transformed)

        if bool(props_to_aggregate and props_to_aggregate.strip()) and bool(
            props_to_group_by and props_to_group_by.strip()
        ):
            df_transformed = self._apply_groupping(
                df_transformed, props_to_group_by, props_to_aggregate
            )

        other_cols = [
            "phones",
            "emails",
            "relations",
            "address",
            "educations",
            "works",
            "documents",
            "vehicles",
            "financials",
            "ownerships",
            "links",
            "accounts",
            "movements",
            "devices",
            "ips",
            "awards",
            "conflicts",
            "forces",
            "violations",
            "medicals",
        ]
        existing_cols = [c for c in other_cols if c in df.columns]
        if existing_cols:
            condition = col("names").isNotNull() & (
                reduce(lambda a, b: a | b, [col(c).isNotNull() for c in existing_cols])
            )
        else:
            condition = col("names").isNotNull()

        df_transformed = df_transformed.filter(condition)
        df_transformed.show(truncate=False)

        return df_transformed

    def _build_column(self, df: DataFrame, field: str, spec: Dict[str, Any]):
        print(f"""build column {field}""")

        def get_function_defaults(func):
            sig = inspect.signature(func)
            defaults = {
                k: v.default
                for k, v in sig.parameters.items()
                if v.default is not inspect.Parameter.empty
            }
            return defaults

        def build_struct_from_schema(
            prefix: str, schema_obj: Dict[str, Any]
        ) -> List[Any]:
            fields = []
            for key, spec in schema_obj["properties"].items():
                full_path = f"{prefix}.{key}"
                print(f"FIELD: {full_path}")
                if spec["type"] == "object":
                    nested_fields = build_struct_from_schema(full_path, spec)
                    fields.append(struct(*nested_fields).alias(key))
                elif spec["type"] == "array" and spec["items"].get("type") == "object":
                    item_fields = build_struct_from_schema(full_path, spec["items"])
                    fields.append(array(struct(*item_fields)).alias(key))
                else:
                    fields.append(
                        self._extract_mapped_column(
                            df, full_path, key, spec["type"]
                        ).alias(key)
                    )
            return fields

        def get_param_type_map(func):
            sig = inspect.signature(func)
            hints = get_type_hints(func)

            param_map = {}
            for name in sig.parameters:
                annotation = hints.get(name, str)
                param_map[name] = {
                    int: "int",
                    float: "double",
                    bool: "boolean",
                }.get(annotation, "string")
            return param_map

        udf_registry = {
            "forces": (forces_udf, forces),
            "medicals": (medicals_udf, medicals),
            "awards": (award_udf, award),
            "conflicts": (conflict_udf, conflict),
            "device": (device_udf, device),
            "documents": (document_udf, document),
            "educations": (education_udf, education),
            "financials": (financial_udf, financial),
            "incidences": (incidence_udf, incidence),
            "ips": (ip_udf, ip),
            "movements": (movement_udf, movement),
            "ownerships": (ownership_udf, ownership),
            "vehicles": (vehicle_udf, vehicle),
            "violations": (violation_udf, violation),
            "work": (work_udf, work),
        }

        if spec["type"] == "object":
            return struct(*build_struct_from_schema(field, spec)).alias(field)

        if spec["type"] == "array" and spec.get("items", {}).get("type") == "object":
            if field in udf_registry:
                if field == "documents":
                    print("""Working with documents""")
                udf_func, validator_func = udf_registry[field]
                param_map = get_param_type_map(validator_func)

                max_parts = 1
                field_param_lists = {param: [] for param in param_map}

                for param in param_map:
                    map_key = f"{field}.{param}"
                    raw_column = self.mapping.get(map_key, "")
                    column_names = [
                        c.strip() for c in raw_column.split(",") if c.strip()
                    ]
                    max_parts = max(max_parts, len(column_names))
                    field_param_lists[param] = column_names

                function_defaults = get_function_defaults(validator_func)
                if "date_format" in function_defaults:
                    function_defaults["date_format"] = self.date_format
                udf_calls = []
                for i in range(max_parts):
                    args = []
                    for param, spark_type in param_map.items():
                        columns = field_param_lists.get(param, [])
                        if i < len(columns) and columns[i] in df.columns:
                            args.append(col(columns[i]))
                        elif param in function_defaults:
                            args.append(lit(function_defaults[param]))
                        else:
                            args.append(self._default_value_for_type(spark_type))
                    udf_calls.append(udf_func(*args))

                return array(*udf_calls).alias(field)

        return self._extract_mapped_column(df, field, field, spec["type"]).alias(field)

    def _default_value_for_type(self, t: str):
        return {
            "string": lit(None).cast("string"),
            "number": lit(None).cast("double"),
            "integer": lit(None).cast("int"),
            "boolean": lit(None).cast("boolean"),
            "array": array().cast("array<string>"),
            "object": lit(None).cast("struct<>"),
        }.get(t, lit(None).cast("string"))

    def _extract_mapped_column(
        self, df: DataFrame, field_path: str, result_field: str, field_type: str
    ):
        def apply_udf_to_columns(udf_func, cols):
            udf_arrays = [array(udf_func(c)) for c in cols]
            return flatten(array_compact(array_distinct((array(*udf_arrays)))))

        raw_column = self.mapping.get(field_path)
        if raw_column:
            column_names = [col_name.strip() for col_name in raw_column.split(",")]
            valid_columns = [col(name) for name in column_names if name in df.columns]
            if not valid_columns:
                return self._default_value_for_type(field_type)
            if result_field == "names":
                return array(name_udf(valid_columns[0]))
            elif result_field == "birth_date":
                birth_date = birth_date_udf(valid_columns[0], lit(self.date_format))
                print(f"""{birth_date}""")
                return birth_date
            elif result_field == "sex":
                return sex_udf(valid_columns[0])
            elif result_field == "phones":
                return apply_udf_to_columns(phone_udf, valid_columns)
            elif result_field == "emails":
                return apply_udf_to_columns(email_udf, valid_columns)
            elif result_field == "addresses":
                if len(valid_columns) == 1:
                    return array_compact(
                        array_distinct(
                            normalize_address_batch_udf(
                                array(
                                    address_with_type_udf(
                                        address_udf(valid_columns[0]), lit(1)
                                    )
                                )
                            )
                        )
                    )
                else:
                    concatenated = concat_ws(" ", *valid_columns)
                    return array_compact(
                        array_distinct(
                            normalize_address_batch_udf(
                                array(
                                    address_with_type_udf(
                                        address_udf(concatenated), lit(1)
                                    )
                                )
                            )
                        )
                    )
            elif result_field == "actuality_date":
                return actuality_date_udf(valid_columns[0], lit(self.date_format))
            else:
                return valid_columns[0]

        return self._default_value_for_type(field_type)

    def _clean_dataframe(self, df: DataFrame):
        def clean_column(c, data_type):
            if isinstance(data_type, ArrayType):
                element_type = data_type.elementType
                if isinstance(element_type, StructType):
                    fields = element_type.fields
                    conditions = []
                    for f in fields:
                        f_name = f.name
                        f_type = f.dataType
                        if isinstance(f_type, ArrayType):
                            conditions.append(
                                f"(x.{f_name} IS NULL OR size(x.{f_name}) = 0)"
                            )
                        else:
                            conditions.append(f"(x.{f_name} IS NULL)")
                    struct_empty_condition = " AND ".join(conditions)

                    filtered = expr(
                        f"filter({c._jc.toString()}, x -> NOT ({struct_empty_condition}))"
                    )

                    return when(size(filtered) == 0, lit(None)).otherwise(filtered)

                else:
                    filtered = expr(
                        f"filter({c._jc.toString()}, x -> x IS NOT NULL AND x != '')"
                    )
                    return when(size(filtered) == 0, lit(None)).otherwise(filtered)
            else:
                return when(c == "", lit(None)).otherwise(c)

        schema = df.schema
        cleaned_cols = []
        for field in schema.fields:
            cleaned_col = clean_column(col(field.name), field.dataType).alias(
                field.name
            )
            cleaned_cols.append(cleaned_col)
        df = df.select(*cleaned_cols)
        df = df.drop_duplicates()

        return df

    def _apply_groupping(self, df: DataFrame, group_by_str: str, agg_str: str):
        group_by_cols = [col.strip() for col in group_by_str.split(",")]
        agg_cols = [col.strip() for col in agg_str.split(",")]

        agg_exprs = [
            array_compact(flatten(collect_set(col))).alias(col) for col in agg_cols
        ]

        result_df = df.groupBy(*group_by_cols).agg(*agg_exprs)

        return result_df
