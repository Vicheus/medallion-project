from pyspark import StorageLevel

from pyspark.sql.functions import (
    when,
    col,
    lit,
    array,
    size,
    array_compact,
    from_json,
    explode,
    concat_ws,
    array_distinct,
    coalesce,
)

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE

from parsetron.sections.document.udfs import document_udf
from parsetron.sections.work.udfs import work_udf
from parsetron.sections.main.udfs import (
    birth_date_udf,
    phone_udf,
    sex_udf,
    address_udf,
    name_parts_udf,
    name_udf,
    raw_metadata_udf,
    actuality_date_udf,
    email_udf,
)
from pyspark.sql.types import (
    StructType,
    StructField,
    LongType,
    StringType,
    ArrayType,
    IntegerType,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0420"
    calc_completeness: bool = False
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ

    def parser(self):
        schema = StructType(
            [
                StructField(
                    "phone",
                    StructType([StructField("potential_contract_id", LongType())]),
                ),
                StructField(
                    "photo",
                    StructType(
                        [
                            StructField("status", StringType()),
                            StructField("provider", StringType()),
                            StructField("remote_id", StringType()),
                            StructField(
                                "fromBucket",
                                StructType([StructField("clientImageId", LongType())]),
                            ),
                            StructField(
                                "fromRequest",
                                StructType([StructField("clientImageId", LongType())]),
                            ),
                        ]
                    ),
                ),
                StructField(
                    "contacts",
                    ArrayType(
                        StructType(
                            [
                                StructField("owner_name", StringType()),
                                StructField("owner_type", StringType()),
                                StructField("phone_number", LongType()),
                            ]
                        )
                    ),
                ),
                StructField(
                    "personal",
                    StructType(
                        [
                            StructField("email", StringType()),
                            StructField("last_name", StringType()),
                            StructField("first_name", StringType()),
                            StructField("middle_name", StringType()),
                        ]
                    ),
                ),
                StructField(
                    "employment",
                    StructType(
                        [
                            StructField("income", StringType()),
                            StructField("children", StringType()),
                            StructField("residence", StringType()),
                            StructField("work_phone", LongType()),
                            StructField("ipdl_status", StringType()),
                            StructField("employer_name", StringType()),
                            StructField("present_position", StringType()),
                            StructField("additional_income", StringType()),
                        ]
                    ),
                ),
                StructField(
                    "external_personal",
                    StructType(
                        [
                            StructField("status", StringType()),
                            StructField(
                                "personal",
                                StructType(
                                    [
                                        StructField(
                                            "person",
                                            StructType(
                                                [
                                                    StructField("iin", StringType()),
                                                    StructField("name", StringType()),
                                                    StructField(
                                                        "gender",
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "code",
                                                                    IntegerType(),
                                                                ),
                                                                StructField(
                                                                    "nameKz",
                                                                    StringType(),
                                                                ),
                                                                StructField(
                                                                    "nameRu",
                                                                    StringType(),
                                                                ),
                                                                StructField(
                                                                    "changeDate",
                                                                    StringType(),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    StructField(
                                                        "surname", StringType()
                                                    ),
                                                    StructField(
                                                        "birthDate", StringType()
                                                    ),
                                                    StructField(
                                                        "documents",
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "document",
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "name",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "type",
                                                                                StructType(
                                                                                    [
                                                                                        StructField(
                                                                                            "code",
                                                                                            StringType(),
                                                                                        ),
                                                                                        StructField(
                                                                                            "nameKz",
                                                                                            StringType(),
                                                                                        ),
                                                                                        StructField(
                                                                                            "nameRu",
                                                                                            StringType(),
                                                                                        ),
                                                                                        StructField(
                                                                                            "changeDate",
                                                                                            StringType(),
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                            StructField(
                                                                                "number",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "status",
                                                                                StructType(
                                                                                    [
                                                                                        StructField(
                                                                                            "code",
                                                                                            StringType(),
                                                                                        ),
                                                                                        StructField(
                                                                                            "nameKz",
                                                                                            StringType(),
                                                                                        ),
                                                                                        StructField(
                                                                                            "nameRu",
                                                                                            StringType(),
                                                                                        ),
                                                                                        StructField(
                                                                                            "changeDate",
                                                                                            StringType(),
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                            StructField(
                                                                                "endDate",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "surname",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "beginDate",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "birthDate",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "patronymic",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "issueOrganization",
                                                                                StructType(
                                                                                    [
                                                                                        StructField(
                                                                                            "code",
                                                                                            StringType(),
                                                                                        ),
                                                                                        StructField(
                                                                                            "nameKz",
                                                                                            StringType(),
                                                                                        ),
                                                                                        StructField(
                                                                                            "nameRu",
                                                                                            StringType(),
                                                                                        ),
                                                                                        StructField(
                                                                                            "changeDate",
                                                                                            StringType(),
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                )
                                                            ]
                                                        ),
                                                    ),
                                                    StructField(
                                                        "birthPlace",
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "city", StringType()
                                                                ),
                                                                StructField(
                                                                    "region",
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "code",
                                                                                LongType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameKz",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameRu",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "changeDate",
                                                                                StringType(),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                                StructField(
                                                                    "country",
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "code",
                                                                                LongType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameKz",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameRu",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "changeDate",
                                                                                StringType(),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                                StructField(
                                                                    "district",
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "code",
                                                                                LongType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameKz",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameRu",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "changeDate",
                                                                                StringType(),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    StructField(
                                                        "lifeStatus",
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "code",
                                                                    IntegerType(),
                                                                ),
                                                                StructField(
                                                                    "nameKz",
                                                                    StringType(),
                                                                ),
                                                                StructField(
                                                                    "nameRu",
                                                                    StringType(),
                                                                ),
                                                                StructField(
                                                                    "changeDate",
                                                                    StringType(),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    StructField(
                                                        "patronymic", StringType()
                                                    ),
                                                    StructField(
                                                        "regAddress",
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "city", StringType()
                                                                ),
                                                                StructField(
                                                                    "flat",
                                                                    IntegerType(),
                                                                ),
                                                                StructField(
                                                                    "region",
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "code",
                                                                                LongType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameKz",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameRu",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "changeDate",
                                                                                StringType(),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                                StructField(
                                                                    "street",
                                                                    StringType(),
                                                                ),
                                                                StructField(
                                                                    "country",
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "code",
                                                                                LongType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameKz",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameRu",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "changeDate",
                                                                                StringType(),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                                StructField(
                                                                    "building",
                                                                    IntegerType(),
                                                                ),
                                                                StructField(
                                                                    "district",
                                                                    StructType(
                                                                        [
                                                                            StructField(
                                                                                "code",
                                                                                LongType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameKz",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "nameRu",
                                                                                StringType(),
                                                                            ),
                                                                            StructField(
                                                                                "changeDate",
                                                                                StringType(),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                                StructField(
                                                                    "beginDate",
                                                                    StringType(),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    StructField(
                                                        "citizenship",
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "code", LongType()
                                                                ),
                                                                StructField(
                                                                    "nameKz",
                                                                    StringType(),
                                                                ),
                                                                StructField(
                                                                    "nameRu",
                                                                    StringType(),
                                                                ),
                                                                StructField(
                                                                    "changeDate",
                                                                    StringType(),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    StructField(
                                                        "nationality",
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "code", StringType()
                                                                ),
                                                                StructField(
                                                                    "nameKz",
                                                                    StringType(),
                                                                ),
                                                                StructField(
                                                                    "nameRu",
                                                                    StringType(),
                                                                ),
                                                                StructField(
                                                                    "changeDate",
                                                                    StringType(),
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        )
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
                StructField("kiscPersonalId", LongType()),
                StructField(
                    "client_form_answer",
                    StructType(
                        [
                            StructField("residence", StringType()),
                            StructField("ipdl_status", StringType()),
                        ]
                    ),
                ),
                StructField(
                    "address",
                    StructType(
                        [
                            StructField("same_actual", StringType()),
                            StructField(
                                "registration_address",
                                StructType(
                                    [
                                        StructField(
                                            "city",
                                            StructType(
                                                [
                                                    StructField("id", StringType()),
                                                    StructField("name", StringType()),
                                                    StructField("type", StringType()),
                                                ]
                                            ),
                                        ),
                                        StructField("flat", StringType()),
                                        StructField("corps", StringType()),
                                        StructField("house", StringType()),
                                        StructField(
                                            "street",
                                            StructType(
                                                [
                                                    StructField("id", StringType()),
                                                    StructField("name", StringType()),
                                                ]
                                            ),
                                        ),
                                        StructField("building", StringType()),
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
                StructField(
                    "passport",
                    StructType(
                        [
                            StructField("sex", StringType()),
                            StructField("when", StringType()),
                            StructField("issuer", StringType()),
                            StructField("birthday", StringType()),
                            StructField("id_number", StringType()),
                            StructField("birthplace", StringType()),
                            StructField("country_id", StringType()),
                            StructField("period_validity", StringType()),
                        ]
                    ),
                ),
            ]
        )
        df_potential_clients = self.read(
            path="/media/user/SAMSUNG/Databases/index_0420/raw/kazakhstan zaimer.kz/potential_clients_preprocessed.csv",
            sep=";",
        ).withColumn("json_data", from_json(col("data"), schema))

        contacts_df = df_potential_clients.select(
            explode(col("json_data.contacts")).alias("contact")
        ).select(
            name_udf(col("contact.owner_name")).alias("names"),
            array_compact(
                array(
                    phone_udf(
                        col("contact.phone_number"),
                        lit(self.dataset_country_code.value),
                    )
                )
            ).alias("phones"),
            lit(None).alias("emails"),
            array().alias("address"),
            lit(None).alias("birth_date"),
            lit(None).alias("birth_place"),
            lit(None).alias("sex"),
            array().alias("documents"),
            array().alias("works"),
            lit(None).alias("raw_metadata"),
            lit(None).alias("actuality"),
        )

        df_potential_clients = (
            df_potential_clients.withColumn("phone", col("phone"))
            .withColumn("inn", col("c11"))
            .withColumn("personal_email", col("json_data.personal.email"))
            .withColumn("personal_last_name", col("json_data.personal.last_name"))
            .withColumn("personal_first_name", col("json_data.personal.first_name"))
            .withColumn("personal_middle_name", col("json_data.personal.middle_name"))
            .withColumn("work_phone", col("json_data.employment.work_phone"))
            .withColumn("employer_name", col("json_data.employment.employer_name"))
            .withColumn(
                "present_position", col("json_data.employment.present_position")
            )
            .withColumn(
                "external_personal_person_iin",
                col("json_data.external_personal.personal.person.iin"),
            )
            .withColumn(
                "external_personal_person_name",
                col("json_data.external_personal.personal.person.name"),
            )
            .withColumn(
                "external_personal_person_surname",
                col("json_data.external_personal.personal.person.surname"),
            )
            .withColumn(
                "external_personal_person_patronymic",
                col("json_data.external_personal.personal.person.patronymic"),
            )
            .withColumn(
                "external_personal_person_birthDate",
                col("json_data.external_personal.personal.person.birthDate"),
            )
            .withColumn(
                "external_personal_person_citizenship",
                col("json_data.external_personal.personal.person.citizenship.nameRu"),
            )
            .withColumn(
                "external_personal_person_nationality",
                col("json_data.external_personal.personal.person.nationality.nameRu"),
            )
            .withColumn(
                "external_personal_person_gender",
                col("json_data.external_personal.personal.person.gender.nameRu"),
            )
            .withColumn(
                "external_personal_person_birthPlace_city",
                col("json_data.external_personal.personal.person.birthPlace.city"),
            )
            .withColumn(
                "external_personal_person_birthPlace_region",
                col(
                    "json_data.external_personal.personal.person.birthPlace.region.nameRu"
                ),
            )
            .withColumn(
                "external_personal_person_birthPlace_country",
                col(
                    "json_data.external_personal.personal.person.birthPlace.country.nameRu"
                ),
            )
            .withColumn(
                "external_personal_person_birthPlace_district",
                col(
                    "json_data.external_personal.personal.person.birthPlace.district.nameRu"
                ),
            )
            .withColumn(
                "external_personal_person_regAddress_city",
                col("json_data.external_personal.personal.person.regAddress.city"),
            )
            .withColumn(
                "external_personal_person_regAddress_flat",
                col("json_data.external_personal.personal.person.regAddress.flat"),
            )
            .withColumn(
                "external_personal_person_regAddress_region",
                col(
                    "json_data.external_personal.personal.person.regAddress.region.nameRu"
                ),
            )
            .withColumn(
                "external_personal_person_regAddress_street",
                col("json_data.external_personal.personal.person.regAddress.street"),
            )
            .withColumn(
                "external_personal_person_regAddress_country",
                col(
                    "json_data.external_personal.personal.person.regAddress.country.nameRu"
                ),
            )
            .withColumn(
                "external_personal_person_regAddress_building",
                col("json_data.external_personal.personal.person.regAddress.building"),
            )
            .withColumn(
                "external_personal_person_regAddress_district",
                col(
                    "json_data.external_personal.personal.person.regAddress.district.nameRu"
                ),
            )
            .withColumn(
                "external_personal_person_documents_document_name",
                col(
                    "json_data.external_personal.personal.person.documents.document.name"
                ),
            )
            .withColumn(
                "external_personal_person_documents_document_type",
                col(
                    "json_data.external_personal.personal.person.documents.document.type.nameRu"
                ),
            )
            .withColumn(
                "external_personal_person_documents_document_number",
                col(
                    "json_data.external_personal.personal.person.documents.document.number"
                ),
            )
            .withColumn(
                "external_personal_person_documents_document_beginDate",
                col(
                    "json_data.external_personal.personal.person.documents.document.beginDate"
                ),
            )
            .withColumn(
                "external_personal_person_documents_document_endDate",
                col(
                    "json_data.external_personal.personal.person.documents.document.endDate"
                ),
            )
            .withColumn(
                "external_personal_person_documents_document_issueOrganisation",
                col(
                    "json_data.external_personal.personal.person.documents.document.issueOrganization.nameRu"
                ),
            )
            .withColumn(
                "address_registration_address_city_name",
                col("json_data.address.registration_address.city.name"),
            )
            .withColumn(
                "address_registration_address_flat",
                col("json_data.address.registration_address.flat"),
            )
            .withColumn(
                "address_registration_address_corps",
                col("json_data.address.registration_address.corps"),
            )
            .withColumn(
                "address_registration_address_house",
                col("json_data.address.registration_address.house"),
            )
            .withColumn(
                "address_registration_address_street",
                col("json_data.address.registration_address.street.name"),
            )
            .withColumn(
                "address_registration_address_building",
                col("json_data.address.registration_address.building"),
            )
            .withColumn("passport_sex", col("json_data.passport.sex"))
            .withColumn("passport_when", col("json_data.passport.when"))
            .withColumn("passport_issuer", col("json_data.passport.issuer"))
            .withColumn("passport_birthday", col("json_data.passport.birthday"))
            .withColumn("passport_id_number", col("json_data.passport.id_number"))
            .withColumn("passport_birthplace", col("json_data.passport.birthplace"))
            .withColumn("passport_country_id", col("json_data.passport.country_id"))
            .withColumn(
                "passport_period_validity", col("json_data.passport.period_validity")
            )
            .select(
                "phone",
                "inn",
                col("c9").alias("created_at"),
                col("c10").alias("updated_at"),
                "personal_email",
                "personal_last_name",
                "personal_first_name",
                "personal_middle_name",
                "work_phone",
                "employer_name",
                "present_position",
                "external_personal_person_iin",
                "external_personal_person_name",
                "external_personal_person_surname",
                "external_personal_person_patronymic",
                "external_personal_person_birthDate",
                "external_personal_person_citizenship",
                "external_personal_person_nationality",
                "external_personal_person_gender",
                "external_personal_person_birthPlace_city",
                "external_personal_person_birthPlace_region",
                "external_personal_person_birthPlace_country",
                "external_personal_person_birthPlace_district",
                "external_personal_person_regAddress_city",
                "external_personal_person_regAddress_flat",
                "external_personal_person_regAddress_region",
                "external_personal_person_regAddress_street",
                "external_personal_person_regAddress_country",
                "external_personal_person_regAddress_building",
                "external_personal_person_regAddress_district",
                "external_personal_person_documents_document_name",
                "external_personal_person_documents_document_type",
                "external_personal_person_documents_document_number",
                "external_personal_person_documents_document_beginDate",
                "external_personal_person_documents_document_endDate",
                "external_personal_person_documents_document_issueOrganisation",
                "address_registration_address_city_name",
                "address_registration_address_flat",
                "address_registration_address_corps",
                "address_registration_address_house",
                "address_registration_address_street",
                "address_registration_address_building",
                "passport_sex",
                "passport_when",
                "passport_issuer",
                "passport_birthday",
                "passport_id_number",
                "passport_birthplace",
                "passport_country_id",
                "passport_period_validity",
            )
        )

        df_potential_clients = (
            df_potential_clients.withColumn(
                "names",
                name_parts_udf(
                    col("personal_first_name"),
                    col("personal_last_name"),
                    col("personal_middle_name"),
                ),
            )
            .withColumn(
                "phones",
                array_compact(
                    array_distinct(
                        array(
                            phone_udf(
                                col("phone"), lit(self.dataset_country_code.value)
                            ),
                            phone_udf(
                                col("work_phone"), lit(self.dataset_country_code.value)
                            ),
                        )
                    )
                ),
            )
            .withColumn("emails", email_udf(col("personal_email")))
            .withColumn(
                "birth_date",
                birth_date_udf(
                    col("external_personal_person_birthDate"), lit("%Y-%m-%d")
                ),
            )
            .withColumn(
                "sex",
                sex_udf(
                    coalesce(
                        col("external_personal_person_gender"), col("passport_sex")
                    )
                ),
            )
            .withColumn(
                "birth_place",
                address_udf(
                    concat_ws(
                        " ",
                        col("external_personal_person_birthPlace_country"),
                        col("external_personal_person_birthPlace_district"),
                        col("external_personal_person_birthPlace_region"),
                        col("external_personal_person_birthPlace_city"),
                    )
                ),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                concat_ws(
                                    " ",
                                    col("external_personal_person_regAddress_country"),
                                    col("external_personal_person_regAddress_region"),
                                    col("external_personal_person_regAddress_district"),
                                    col("external_personal_person_regAddress_city"),
                                    col("external_personal_person_regAddress_street"),
                                    col("external_personal_person_regAddress_building"),
                                )
                            ),
                            address_udf(
                                concat_ws(
                                    " ",
                                    col("address_registration_address_city_name"),
                                    col("address_registration_address_street"),
                                    col("address_registration_address_house"),
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("inn").isNotNull(),
                            document_udf(
                                lit("инн"),
                                col("inn"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                                lit(self.dataset_country_code.value),
                            ),
                        ).otherwise(None),
                        when(
                            col("external_personal_person_iin").isNotNull(),
                            document_udf(
                                lit("инн"),
                                col("external_personal_person_iin"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                                lit(self.dataset_country_code.value),
                            ),
                        ).otherwise(None),
                        when(
                            col(
                                "external_personal_person_documents_document_number"
                            ).isNotNull(),
                            document_udf(
                                lit(None),
                                col(
                                    "external_personal_person_documents_document_number"
                                ),
                                col(
                                    "external_personal_person_documents_document_beginDate"
                                ),
                                col(
                                    "external_personal_person_documents_document_endDate"
                                ),
                                col(
                                    "external_personal_person_documents_document_issueOrganisation"
                                ),
                                lit(None),
                                lit("yyyy-MM-dd"),
                                lit(self.dataset_country_code.value),
                            ),
                        ).otherwise(None),
                        when(
                            col("passport_id_number").isNotNull(),
                            document_udf(
                                lit(None),
                                col("passport_id_number"),
                                col("passport_when"),
                                col("passport_period_validity"),
                                col("passport_issuer"),
                                lit(None),
                                lit("yyyy-MM-dd"),
                                lit(self.dataset_country_code.value),
                            ),
                        ).otherwise(None),
                    )
                ),
            )
            .withColumn(
                "works",
                when(
                    col("employer_name").isNotNull(),
                    array_compact(
                        array_distinct(
                            array(
                                work_udf(
                                    col("present_position"),
                                    lit(None),
                                    lit(None),
                                    col("employer_name"),
                                    lit(None),
                                    lit(None),
                                )
                            )
                        )
                    ),
                ),
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("external_personal_person_citizenship"),
                    col("external_personal_person_citizenship"),
                    lit("external_personal_person_nationality"),
                    col("external_personal_person_nationality"),
                ),
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("updated_at"), col("created_at")),
                    lit("%Y-%m-%d %H:%M:%S"),
                ),
            )
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "birth_date",
                "birth_place",
                "sex",
                "documents",
                "works",
                "raw_metadata",
                "actuality",
            )
        )

        df_clients = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0420/raw/kazakhstan zaimer.kz/clients_preprocessed.csv",
                sep=",",
            )
            .withColumn("client_id", col("id"))
            .withColumn(
                "names",
                name_parts_udf(col("first_name"), col("last_name"), col("middle_name")),
            )
            .withColumn("sex", sex_udf(col("sex")))
            .withColumn(
                "phones",
                array(phone_udf(col("phone"), lit(self.dataset_country_code.value))),
            )
            .withColumn("emails", email_udf(col("email")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    coalesce(col("c7"), col("c6")), lit("%Y-%m-%d %H:%M:%S")
                ),
            )
            .select("client_id", "names", "phones", "emails", "sex", "actuality")
        )

        df_passport = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0420/raw/kazakhstan zaimer.kz/passports_preprocessed.csv",
                sep=",",
            )
            .withColumn("client_id", col("id1"))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("inn").isNotNull(),
                            document_udf(
                                lit("инн"),
                                col("inn"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                                lit(self.dataset_country_code.value),
                            ),
                        ).otherwise(None),
                        when(
                            col("passport_num").isNotNull(),
                            document_udf(
                                lit(None),
                                col("passport_num"),
                                col("passport_valid_from"),
                                col("passport_valid_to"),
                                concat_ws(" ", col("issued_by1"), col("issued_by2")),
                                lit(None),
                                lit("yyyy-MM-dd"),
                                lit(self.dataset_country_code.value),
                            ),
                        ).otherwise(None),
                    )
                ),
            )
            .select("client_id", "birth_date", "documents")
        )

        df_clients = (
            df_clients.join(df_passport, "client_id", "left")
            .withColumn("birth_place", lit(None))
            .withColumn("address", array())
            .withColumn("works", array())
            .withColumn("raw_metadata", lit(None))
            .select(
                "names",
                "phones",
                "emails",
                "address",
                "birth_date",
                "birth_place",
                "sex",
                "documents",
                "works",
                "raw_metadata",
                "actuality",
            )
        )

        df = df_potential_clients.unionAll(contacts_df).unionAll(df_clients)

        df = df.select(
            "names",
            "phones",
            "emails",
            "address",
            "birth_date",
            "birth_place",
            "sex",
            "documents",
            "works",
            "raw_metadata",
            "actuality",
        )

        df = (
            df.withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    size(array_compact(col("phones"))) > 0, array_compact(col("phones"))
                ).otherwise(None),
            )
            .withColumn(
                "address",
                when(
                    size(array_compact(col("address"))) > 0,
                    array_compact(col("address")),
                ).otherwise(None),
            )
            .withColumn(
                "works",
                when(
                    size(array_compact(col("works"))) > 0, array_compact(col("works"))
                ).otherwise(None),
            )
            .withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    col("raw_metadata").isNotNull(), array(col("raw_metadata"))
                ).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )
        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("address").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()

        df.show(n=20, truncate=False)
        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
