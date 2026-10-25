from pyspark.sql.functions import (
    concat_ws,
    when,
    col,
    lit,
    array,
    struct,
    from_json,
    trim,
    array_compact,
)
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType,
    ArrayType,
    BooleanType,
    FloatType,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    email_udf,
    phone_udf,
)
from parsetron.sections.vehicles.udfs import vehicle_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0069"

    def read_df_cars(self):
        schema = StructType(
            [
                StructField("_index", StringType(), True),
                StructField("_type", StringType(), True),
                StructField("_id", StringType(), True),
                StructField("_score", StringType(), True),
                StructField(
                    "_source",
                    StructType(
                        [
                            StructField(
                                "tag",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("tag_en_downcase", StringType(), True),
                            StructField("year", IntegerType(), True),
                            StructField("service_location_id", StringType(), True),
                            StructField("organization_id", StringType(), True),
                            StructField("contractor_id", StringType(), True),
                            StructField(
                                "contractor_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "contractor_phone",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_formatted", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "contractor_discount_card_number",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "contractor_discount_card_number_no_spec_char",
                                StringType(),
                                True,
                            ),
                            StructField(
                                "vin",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("active", StringType(), True),
                            StructField("car_type", StringType(), True),
                            StructField(
                                "car_make_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "car_model_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "car_type_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                        ]
                    ),
                    True,
                ),
            ]
        )
        df = self.read(
            path="Rocketwash.me_02.2023_3,6M/cars-staging_197к.txt",
            sep="\n",
            header=False,
        )

        df = (
            df.replace("NULL", None)
            .replace("(null)", None)
            .withColumn("data", from_json(col("_c0"), schema))
            .withColumn("tag", col("data._source.tag.value"))
            .withColumn("year", col("data._source.year"))
            .withColumn("contractor_id", col("data._source.contractor_id"))
            .withColumn("contractor_name", col("data._source.contractor_name.value"))
            .withColumn("contractor_phone", col("data._source.contractor_phone.value"))
            .withColumn(
                "contractor_discount_card_number",
                col("data._source.contractor_discount_card_number.value"),
            )
            .withColumn("vin", col("data._source.vin.value"))
            .withColumn("car_make_name", col("data._source.car_make_name.value"))
            .withColumn("car_model_name", col("data._source.car_model_name.value"))
            .withColumn("car_type_name", col("data._source.car_type_name.value"))
            .withColumn(
                "car_model_full",
                trim(
                    concat_ws(
                        " ",
                        col("car_make_name"),
                        col("car_model_name"),
                        col("car_type_name"),
                    )
                ),
            )
            .filter(
                (col("contractor_name").isNotNull() & (col("contractor_name") != ""))
                & (
                    (
                        (
                            col("contractor_phone").isNotNull()
                            & (col("contractor_phone") != "")
                        )
                        | ((col("tag").isNotNull() & (col("tag") != "")))
                    )
                )
            )
            .withColumn("names", name_udf(col("contractor_name")))
            .withColumn("phones", phone_udf(col("contractor_phone")))
            .withColumn(
                "vehicles",
                when(
                    (col("tag").isNotNull() & (col("tag") != ""))
                    | (col("vin").isNotNull() & (col("vin") != ""))
                    | col("car_model_full").isNotNull() & (col("car_model_full") != ""),
                    vehicle_udf(
                        lit(1),
                        col("car_model_full"),
                        col("year"),
                        lit(None),
                        col("tag"),
                        col("vin"),
                        lit(None),
                    ),
                ),
            )
            .withColumn(
                "accounts",
                when(
                    col("contractor_discount_card_number").isNotNull()
                    & (col("contractor_discount_card_number") != ""),
                    array(
                        struct(
                            lit("RocketWash").alias("title"),
                            lit("https://www.rocketwash.me").alias("link"),
                            col("contractor_discount_card_number").alias(
                                "client_card_number"
                            ),
                        )
                    ),
                ),
            )
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", lit(None))
            .withColumn("documents", lit(None))
            .withColumn("works", lit(None))
            .withColumn("other", lit(None))
            .select(
                "names",
                "phones",
                "sex",
                "emails",
                "birth_date",
                "documents",
                "works",
                "accounts",
                "vehicles",
                "other",
            )
        )

        return df

    def read_df_financial_centers(self):
        schema = StructType(
            [
                StructField("_index", StringType(), True),
                StructField("_type", StringType(), True),
                StructField("_id", StringType(), True),
                StructField("_score", DoubleType(), True),
                StructField(
                    "_source",
                    StructType(
                        [
                            StructField("id", IntegerType(), True),
                            StructField("record_type", StringType(), True),
                            StructField(
                                "name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "fc_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("payment_types", ArrayType(StringType()), True),
                            StructField("amount", IntegerType(), True),
                            StructField("organization_id", IntegerType(), True),
                            StructField(
                                "organization_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "organization_inn",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("service_location_id", IntegerType(), True),
                            StructField(
                                "effective_service_location_ids",
                                ArrayType(StringType()),
                                True,
                            ),
                            StructField(
                                "service_location_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "service_location_agreement_number",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("legal_entity_id", IntegerType(), True),
                            StructField(
                                "legal_entity_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("user_id", IntegerType(), True),
                            StructField(
                                "user_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "user_full_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "user_phone",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_formatted", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "user_tin",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "user_discount_card_number",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "user_role",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("user_supplier", BooleanType(), True),
                        ]
                    ),
                    True,
                ),
            ]
        )
        df = self.read(
            path="Rocketwash.me_02.2023_3,6M/financial_centers-staging_405k.txt",
            sep="\n",
            header=False,
        )

        df = (
            df.replace("NULL", None)
            .replace("(null)", None)
            .withColumn("data", from_json(col("_c0"), schema))
            .withColumn("user_name", col("data._source.user_name.value"))
            .withColumn("user_phone", col("data._source.user_phone.value"))
            .withColumn("user_tin", col("data._source.user_tin.value"))
            .withColumn(
                "user_discount_card_number",
                col("data._source.user_discount_card_number.value"),
            )
            .filter(
                (col("user_name").isNotNull() & (col("user_name") != ""))
                & (
                    (
                        (col("user_phone").isNotNull() & (col("user_phone") != ""))
                        | ((col("user_tin").isNotNull() & (col("user_tin") != "")))
                    )
                )
            )
            .withColumn("names", name_udf(col("user_name")))
            .withColumn("phones", phone_udf(col("user_phone")))
            .withColumn(
                "documents",
                when(
                    col("user_tin").isNotNull() & (col("user_tin") != ""),
                    document_udf(
                        lit("инн"),
                        col("user_tin"),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("yyyy-MM-dd"),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("user_discount_card_number").isNotNull()
                    & (col("user_discount_card_number") != ""),
                    array(
                        struct(
                            lit("RocketWash").alias("title"),
                            lit("https://www.rocketwash.me").alias("link"),
                            col("user_discount_card_number").alias(
                                "client_card_number"
                            ),
                        )
                    ),
                ),
            )
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", lit(None))
            .withColumn("other", lit(None))
            .withColumn("works", lit(None))
            .withColumn("vehicles", lit(None))
            .select(
                "names",
                "phones",
                "sex",
                "emails",
                "birth_date",
                "documents",
                "works",
                "accounts",
                "vehicles",
                "other",
            )
        )

        return df

    def read_df_users(self):
        schema = StructType(
            [
                StructField("_index", StringType(), True),
                StructField("_type", StringType(), True),
                StructField("_id", StringType(), True),
                StructField("_score", DoubleType(), True),
                StructField(
                    "_source",
                    StructType(
                        [
                            StructField("id", IntegerType(), True),
                            StructField("created_at", StringType(), True),
                            StructField(
                                "tin",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "kpp",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "role",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "email",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "phone",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_formatted", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "user_type",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("superuser", BooleanType(), True),
                            StructField(
                                "sex",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("date_of_birth", StringType(), True),
                            StructField("service_location_id", IntegerType(), True),
                            StructField(
                                "discount_card_number",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("organization_id", IntegerType(), True),
                            StructField(
                                "organization_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "service_location_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "employee_status",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "all_car_tags",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "all_car_tags_similar",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "all_car_make_models",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "user_category_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("balance_bonuses", IntegerType(), True),
                            StructField(
                                "bonuses_percentage",
                                StructType(
                                    [
                                        StructField("value", IntegerType(), True),
                                        StructField("sortable", IntegerType(), True),
                                        StructField("string", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "discount",
                                StructType(
                                    [
                                        StructField("value", IntegerType(), True),
                                        StructField("sortable", IntegerType(), True),
                                        StructField("string", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("balance_money", IntegerType(), True),
                            StructField("balance_salary", IntegerType(), True),
                            StructField(
                                "phone_confirmed",
                                StructType(
                                    [
                                        StructField("value", BooleanType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("last_phone_confirmed_at", StringType(), True),
                            StructField("supplier", BooleanType(), True),
                            StructField("partner_code", StringType(), True),
                            StructField("partner_plan_id", IntegerType(), True),
                            StructField(
                                "can_send_notification",
                                StructType(
                                    [
                                        StructField("value", BooleanType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("tags", ArrayType(StringType()), True),
                            StructField(
                                "latest_location",
                                StructType(
                                    [
                                        StructField("lat", FloatType(), True),
                                        StructField("lon", FloatType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "client_activity_category",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                        ]
                    ),
                    True,
                ),
            ]
        )

        df = self.read(
            path="Rocketwash.me_02.2023_3,6M/rw_stage2-users-staging_198k.txt",
            sep="\n",
            header=False,
        )

        df = (
            df.replace("NULL", None)
            .replace("(null)", None)
            .withColumn("data", from_json(col("_c0"), schema))
            .withColumn("tin", col("data._source.tin.value"))
            .withColumn("name", col("data._source.name.value"))
            .withColumn("email", col("data._source.email.value"))
            .withColumn("phone", col("data._source.phone.value"))
            .withColumn("sex", col("data._source.sex.value"))
            .withColumn("date_of_birth", col("data._source.date_of_birth"))
            .withColumn(
                "organization_name", col("data._source.organization_name.value")
            )
            .withColumn("all_car_tags", col("data._source.all_car_tags.value"))
            .withColumn(
                "all_car_make_models", col("data._source.all_car_make_models.value")
            )
            .withColumn(
                "discount_card_number", col("data._source.discount_card_number.value")
            )
            .withColumn("latest_location_lat", col("data._source.latest_location.lat"))
            .withColumn("latest_location_lon", col("data._source.latest_location.lon"))
            .filter(
                (col("name").isNotNull() & (col("name") != ""))
                & (
                    (
                        (col("phone").isNotNull() & (col("phone") != ""))
                        | ((col("email").isNotNull() & (col("email") != "")))
                        | ((col("tin").isNotNull() & (col("tin") != "")))
                        | (
                            (
                                col("all_car_tags").isNotNull()
                                & (col("all_car_tags") != "")
                            )
                        )
                    )
                )
            )
            .withColumn("names", name_udf(col("name")))
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn("emails", email_udf(col("email")))
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn("birth_date", birth_date_udf(col("date_of_birth")))
            .withColumn(
                "documents",
                when(
                    col("tin").isNotNull() & (col("tin") != ""),
                    document_udf(
                        lit("инн"),
                        col("tin"),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("yyyy-MM-dd"),
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("discount_card_number").isNotNull()
                    & (col("discount_card_number") != ""),
                    array(
                        struct(
                            lit("RocketWash").alias("title"),
                            lit("https://www.rocketwash.me").alias("link"),
                            col("discount_card_number").alias("client_card_number"),
                        )
                    ),
                ),
            )
            .withColumn(
                "works",
                when(
                    col("organization_name").isNotNull()
                    & (col("organization_name") != ""),
                    array(
                        work_udf(
                            lit(None),
                            lit(None),
                            lit(None),
                            col("organization_name").alias("company"),
                            lit(None),
                            lit(None),
                        )
                    ),
                ),
            )
            .withColumn(
                "vehicles",
                when(
                    (col("all_car_tags").isNotNull() & (col("all_car_tags") != ""))
                    | (
                        col("all_car_make_models").isNotNull()
                        & (col("all_car_make_models") != "")
                    ),
                    vehicle_udf(
                        lit(1),
                        col("all_car_make_models"),
                        lit(None),
                        lit(None),
                        col("all_car_tags"),
                        lit(None),
                        lit(None),
                    ),
                ),
            )
            .withColumn(
                "other",
                when(
                    (
                        col("latest_location_lat").isNotNull()
                        & (col("latest_location_lat") != 0.0)
                        & col("latest_location_lon").isNotNull()
                        & (col("latest_location_lon") != 0.0)
                    ),
                    struct(
                        array(
                            array(
                                col("latest_location_lon"), col("latest_location_lat")
                            )
                        ).alias("coordinates")
                    ),
                ),
            )
            .select(
                "names",
                "phones",
                "sex",
                "emails",
                "birth_date",
                "documents",
                "works",
                "accounts",
                "vehicles",
                "other",
            )
        )

        return df

    def read_df_reservations(self):
        schema = StructType(
            [
                StructField("_index", StringType(), True),
                StructField("_type", StringType(), True),
                StructField("_id", StringType(), True),
                StructField("_score", IntegerType(), True),
                StructField(
                    "_source",
                    StructType(
                        [
                            StructField("id", IntegerType(), True),
                            StructField("organization_id", IntegerType(), True),
                            StructField(
                                "taxi_organization_ids", ArrayType(IntegerType()), True
                            ),
                            StructField("service_location_id", IntegerType(), True),
                            StructField(
                                "service_location_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "service_location_phone",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_formatted", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "service_location_lane_id", IntegerType(), True
                            ),
                            StructField(
                                "service_location_lane_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("created_at", StringType(), True),
                            StructField("time_start", StringType(), True),
                            StructField("time_end", StringType(), True),
                            StructField(
                                "status",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "admin_status",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "notes",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("car_id", IntegerType(), True),
                            StructField(
                                "car_tag",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "car_make_model",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "owner_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "owner_phone",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_formatted", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "channel",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "ordinal",
                                StructType(
                                    [
                                        StructField("value", IntegerType(), True),
                                        StructField("sortable", IntegerType(), True),
                                        StructField("string", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("price", IntegerType(), True),
                            StructField("discount", IntegerType(), True),
                            StructField(
                                "discounted_price",
                                StructType(
                                    [
                                        StructField("value", IntegerType(), True),
                                        StructField("sortable", IntegerType(), True),
                                        StructField("string", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "rounded_price",
                                StructType(
                                    [
                                        StructField("value", IntegerType(), True),
                                        StructField("sortable", IntegerType(), True),
                                        StructField("string", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("full_duration", IntegerType(), True),
                            StructField("paid_at", StringType(), True),
                            StructField("fully_paid", BooleanType(), True),
                            StructField(
                                "all_payment_types",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "reservation_payments",
                                ArrayType(
                                    StructType(
                                        [
                                            StructField("id", IntegerType(), True),
                                            StructField("amount", IntegerType(), True),
                                            StructField(
                                                "payment_type_name",
                                                StructType(
                                                    [
                                                        StructField(
                                                            "value", StringType(), True
                                                        ),
                                                        StructField(
                                                            "value_lowercase",
                                                            StringType(),
                                                            True,
                                                        ),
                                                        StructField(
                                                            "sortable",
                                                            StringType(),
                                                            True,
                                                        ),
                                                    ]
                                                ),
                                                True,
                                            ),
                                            StructField(
                                                "payment_type_const", StringType(), True
                                            ),
                                        ]
                                    )
                                ),
                                True,
                            ),
                            StructField("paid_with_bonuses", IntegerType(), True),
                            StructField(
                                "reservation_lifetime",
                                StructType(
                                    [
                                        StructField("id", IntegerType(), True),
                                        StructField(
                                            "saved_associations", BooleanType(), True
                                        ),
                                        StructField(
                                            "save_worklog_done", BooleanType(), True
                                        ),
                                        StructField(
                                            "notify_client_that_reservation_was_finished_done",
                                            BooleanType(),
                                            True,
                                        ),
                                        StructField(
                                            "create_driver_and_contractor_done",
                                            BooleanType(),
                                            True,
                                        ),
                                        StructField(
                                            "move_car_to_service_location_done",
                                            BooleanType(),
                                            True,
                                        ),
                                        StructField(
                                            "update_user_category_done",
                                            BooleanType(),
                                            True,
                                        ),
                                        StructField(
                                            "resave_related_models_to_update_financial_operations_done",
                                            BooleanType(),
                                            True,
                                        ),
                                        StructField(
                                            "add_bonuses_to_user_done",
                                            BooleanType(),
                                            True,
                                        ),
                                        StructField(
                                            "send_sms_to_specified_phone_done",
                                            BooleanType(),
                                            True,
                                        ),
                                        StructField(
                                            "update_organization_balance_done",
                                            BooleanType(),
                                            True,
                                        ),
                                        StructField(
                                            "update_charts_done", BooleanType(), True
                                        ),
                                        StructField(
                                            "send_bonuses_payment_confirmations_done",
                                            BooleanType(),
                                            True,
                                        ),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "reservation_lifetime_all_complete", BooleanType(), True
                            ),
                            StructField("contractor_id", IntegerType(), True),
                            StructField("original_contractor_id", IntegerType(), True),
                            StructField(
                                "created_responsible",
                                StructType(
                                    [
                                        StructField("id", IntegerType(), True),
                                        StructField(
                                            "name",
                                            StructType(
                                                [
                                                    StructField(
                                                        "value", StringType(), True
                                                    ),
                                                    StructField(
                                                        "value_lowercase",
                                                        StringType(),
                                                        True,
                                                    ),
                                                    StructField(
                                                        "sortable", StringType(), True
                                                    ),
                                                ]
                                            ),
                                            True,
                                        ),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "paid_responsible",
                                StructType(
                                    [
                                        StructField("id", IntegerType(), True),
                                        StructField(
                                            "name",
                                            StructType(
                                                [
                                                    StructField(
                                                        "value", StringType(), True
                                                    ),
                                                    StructField(
                                                        "value_lowercase",
                                                        StringType(),
                                                        True,
                                                    ),
                                                    StructField(
                                                        "sortable", StringType(), True
                                                    ),
                                                ]
                                            ),
                                            True,
                                        ),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "completed_responsible",
                                StructType(
                                    [
                                        StructField("id", IntegerType(), True),
                                        StructField(
                                            "name",
                                            StructType(
                                                [
                                                    StructField(
                                                        "value", StringType(), True
                                                    ),
                                                    StructField(
                                                        "value_lowercase",
                                                        StringType(),
                                                        True,
                                                    ),
                                                    StructField(
                                                        "sortable", StringType(), True
                                                    ),
                                                ]
                                            ),
                                            True,
                                        ),
                                    ]
                                ),
                                True,
                            ),
                            StructField("added_bonuses", StringType(), True),
                            StructField("tinkoff_transaction_id", StringType(), True),
                            StructField(
                                "comments",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "tags",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "client_activity_category",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "attached_services",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "contractor",
                                StructType(
                                    [
                                        StructField("id", IntegerType(), True),
                                        StructField("name", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "sl_location",
                                StructType(
                                    [
                                        StructField("lat", FloatType(), True),
                                        StructField("lon", FloatType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "created_from_location",
                                StructType(
                                    [
                                        StructField("lat", FloatType(), True),
                                        StructField("lon", FloatType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "created_from_city",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "taxi_deduction_without_rw", IntegerType(), True
                            ),
                            StructField("taxi_deduction_with_rw", IntegerType(), True),
                        ]
                    ),
                    True,
                ),
            ]
        )
        df = self.read(
            path="Rocketwash.me_02.2023_3,6M/rw_stage-reservations-staging_519k.txt",
            sep="\n",
            header=False,
        )

        df = (
            df.replace("NULL", None)
            .replace("(null)", None)
            .withColumn("data", from_json(col("_c0"), schema))
            .withColumn("owner_name", col("data._source.owner_name.value"))
            .withColumn("owner_phone", col("data._source.owner_phone.value"))
            .withColumn("car_tag", col("data._source.car_tag.value"))
            .withColumn("car_make_model", col("data._source.car_make_model.value"))
            .withColumn("sl_location_lat", col("data._source.sl_location.lat"))
            .withColumn("sl_location_lon", col("data._source.sl_location.lon"))
            .filter(
                (col("owner_name").isNotNull() & (col("owner_name") != ""))
                & (
                    (
                        (col("owner_phone").isNotNull() & (col("owner_phone") != ""))
                        | ((col("car_tag").isNotNull() & (col("car_tag") != "")))
                    )
                )
            )
            .withColumn("names", name_udf(col("owner_name")))
            .withColumn("phones", phone_udf(col("owner_phone")))
            .withColumn(
                "vehicles",
                when(
                    (col("car_tag").isNotNull() & (col("car_tag") != ""))
                    | (
                        col("car_make_model").isNotNull()
                        & (col("car_make_model") != "")
                    ),
                    vehicle_udf(
                        lit(1),
                        col("car_make_model"),
                        lit(None),
                        lit(None),
                        col("car_tag"),
                        lit(None),
                        lit(None),
                    ),
                ),
            )
            .withColumn(
                "other",
                when(
                    (
                        col("sl_location_lat").isNotNull()
                        & (col("sl_location_lat") != 0.0)
                        & col("sl_location_lon").isNotNull()
                        & (col("sl_location_lon") != 0.0)
                    ),
                    struct(
                        array(
                            array(col("sl_location_lon"), col("sl_location_lat"))
                        ).alias("coordinates")
                    ),
                ),
            )
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", lit(None))
            .withColumn("documents", lit(None))
            .withColumn("works", lit(None))
            .withColumn("accounts", lit(None))
            .select(
                "names",
                "phones",
                "sex",
                "emails",
                "birth_date",
                "documents",
                "works",
                "accounts",
                "vehicles",
                "other",
            )
        )

        return df

    def read_df_sms(self):
        schema = StructType(
            [
                StructField("_index", StringType(), True),
                StructField("_type", StringType(), True),
                StructField("_id", StringType(), True),
                StructField("_score", IntegerType(), True),
                StructField(
                    "_source",
                    StructType(
                        [
                            StructField("created_at", StringType(), True),
                            StructField("service_location_id", IntegerType(), True),
                            StructField("organization_id", IntegerType(), True),
                            StructField(
                                "receiver_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "receiver_phone",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_formatted", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "sender_name",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "status",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField("sortable", StringType(), True),
                                        StructField("ru", StringType(), True),
                                        StructField("ru_lowercase", StringType(), True),
                                        StructField("en", StringType(), True),
                                        StructField("en_lowercase", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField(
                                "text",
                                StructType(
                                    [
                                        StructField("value", StringType(), True),
                                        StructField(
                                            "value_lowercase", StringType(), True
                                        ),
                                        StructField("sortable", StringType(), True),
                                    ]
                                ),
                                True,
                            ),
                            StructField("sent_by_superuser", BooleanType(), True),
                            StructField("sensitive", BooleanType(), True),
                        ]
                    ),
                    True,
                ),
            ]
        )
        df = self.read(
            path="Rocketwash.me_02.2023_3,6M/rw_stage-sms-staging_152k.txt",
            sep="\n",
            header=False,
        )

        df = (
            df.replace("NULL", None)
            .replace("(null)", None)
            .withColumn("data", from_json(col("_c0"), schema))
            .withColumn("receiver_name", col("data._source.receiver_name.value"))
            .withColumn("receiver_phone", col("data._source.receiver_phone.value"))
            .filter(
                (col("receiver_name").isNotNull() & (col("receiver_name") != ""))
                & (
                    (
                        (
                            col("receiver_phone").isNotNull()
                            & (col("receiver_phone") != "")
                        )
                    )
                )
            )
            .withColumn("names", name_udf(col("receiver_name")))
            .withColumn("phones", phone_udf(col("receiver_phone")))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("emails", lit(None))
            .withColumn("documents", lit(None))
            .withColumn("works", lit(None))
            .withColumn("accounts", lit(None))
            .withColumn("vehicles", lit(None))
            .withColumn("other", lit(None))
            .select(
                "names",
                "phones",
                "sex",
                "emails",
                "birth_date",
                "documents",
                "works",
                "accounts",
                "vehicles",
                "other",
            )
        )

        return df

    def parser(self):
        df_cars = self.read_df_cars()
        df_financial_centers = self.read_df_financial_centers()
        df_users = self.read_df_users()
        df_reservations = self.read_df_reservations()
        df_sms = self.read_df_sms()

        df = (
            df_sms.unionAll(df_reservations)
            .unionAll(df_users)
            .unionAll(df_financial_centers)
            .unionAll(df_cars)
        )

        df = df.filter(
            col("names").isNotNull()
            & (
                col("emails").isNotNull()
                | col("phones").isNotNull()
                | col("documents").isNotNull()
                | col("vehicles").isNotNull()
            )
        )

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(), array_compact(array(col("names")))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(
                    col("emails").isNotNull(), array_compact(array(col("emails")))
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(), array_compact(array(col("phones")))
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    col("works").isNotNull(), array_compact(array(col("works")))
                ).otherwise(None),
            )
            .withColumn(
                "accounts",
                when(
                    col("accounts").isNotNull(), array_compact(array(col("accounts")))
                ).otherwise(None),
            )
            .withColumn(
                "vehicles",
                when(
                    col("vehicles").isNotNull(), array_compact(array(col("vehicles")))
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    col("documents").isNotNull(), array_compact(array(col("documents")))
                ).otherwise(None),
            )
        )

        df.show(n=1000, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
