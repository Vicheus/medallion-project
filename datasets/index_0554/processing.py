from pyspark import StorageLevel
from pyspark.sql.functions import (
    array,
    array_compact,
    array_distinct,
    col,
    collect_list,
    concat,
    concat_ws,
    explode,
    expr,
    first,
    flatten,
    from_unixtime,
    length,
    lit,
    lower,
    max,
    min,
    monotonically_increasing_id,
    regexp_replace,
    size,
    split,
    trim,
    udf,
    upper,
    when,
    xxhash64,
    broadcast,
)
from pyspark.sql.types import (
    ArrayType,
    StringType,
    StructType,
    StructField,
    IntegerType,
)

from parsetron import Parsetron
from parsetron.sections.document.schemas import document_schema
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.schemas import raw_metadata_schema
from parsetron.sections.main.udfs import (
    actuality_date_udf,
    address_udf,
    birth_date_udf,
    name_parts_udf,
    name_udf,
    phone_udf,
    raw_metadata_udf,
    relations_udf,
    sex_udf,
)


def _remove_doc_duplicates(structs):
    if len(structs) == 0:
        return []

    seen_non_empty = set()
    seen_authorities = set()
    result = []

    for struct in structs:
        if struct["type"] == 16:
            result.append(struct)
            continue
        if struct["date_issue"] or struct["authority"]:
            result.append(struct)
            seen_non_empty.add((struct["type"], struct["serial"]))

    for struct in structs:
        if struct["type"] == 16:
            continue
        if (not struct["date_issue"] or not struct["authority"]) and (
            struct["type"],
            struct["serial"],
        ) not in seen_non_empty:
            result.append(struct)

    final_result = []
    for struct in result:
        if not struct["authority"]:
            final_result.append(struct)
            continue

        normalized_name = f"{struct["type"]}{struct["serial"]}{struct["date_issue"]}{struct["authority"].lower()}"
        if normalized_name not in seen_authorities:
            final_result.append(struct)
            seen_authorities.add(normalized_name)

    return final_result


def _remove_raw_duplicates(structs: list[str]):
    if len(structs) == 0:
        return []

    result: list[str] = []
    names = []
    phones = []

    for struct in structs:
        if '"fio_pr_u"' in struct and '"mob_phone"' in struct:
            result.append(struct)
        elif '"fio_pr_u"' in struct:
            names.append(struct)
        elif '"mob_phone"' in struct:
            phones.append(struct)

    if len(result) == 0:
        for name in names:
            result.append(name)
        for phone in phones:
            result.append(phone)
        return result

    for name in names:
        start_value = name[:-1]
        for value in result:
            if not value.startswith(start_value):
                result.append(name)
    for phone in phones:
        end_value = phone[1:]
        for value in result:
            if not value.endswith(end_value):
                result.append(phone)

    return result


remove_doc_duplicates_udf = udf(
    _remove_doc_duplicates,
    ArrayType(document_schema, containsNull=False),
)
remove_raw_duplicates_udf = udf(_remove_raw_duplicates, ArrayType(raw_metadata_schema))


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0554"
    validate_invalid_groupping: bool = True

    ignored_polis_vals = [
        "4294967295",
        "4294967296",
        "4294967297",
        "4294967298",
        "4294967299",
    ]
    ignored_polis_part_vals = ["\\.", "I", "/"]
    ignored_polis_part_vals_pattern = "|".join(ignored_polis_part_vals)
    replace_med_names_stops = ["нет", "-"]
    replace_med_names_stops_pattern = "|".join(replace_med_names_stops)
    filter_med_prefixes = [
        "─",
        "└",
        "├",
        "┬",
        "┴",
        "┼",
        "═",
        "╒",
        "╓",
        "╘",
        "╙",
        "╚",
        "╞",
        "╟",
        "╠",
        "╤",
        "╥",
        "╦",
        "╧",
        "╨",
        "╩",
        "╪",
        "╫",
        "╬",
        "▀",
        "▐",
        "▌",
        "•",
        "џ",
        "”",
        "’",
        "љ",
        "“",
        "ћ",
    ]
    filter_med_prefixes_pattern = r"^(" + "|".join(filter_med_prefixes) + r")"
    replace_med_fam_stops = ["умер", "уволена", "уволен", "удалить", "студент"]
    replace_med_fam_stops_pattern = "|".join(replace_med_fam_stops)
    replace_med_fam_suffix_stops = [
        "-п",
        "-пенсионер",
        "-пенсионер-ветеран труда",
        " ь",
    ]
    replace_med_fam_suffix_stops_pattern = (
        r"(" + "|".join(replace_med_fam_suffix_stops) + r")$"
    )
    replace_address_stops = [
        "нет",
        "НЕТ",
        "Нет",
        "д. 0",
        "кв. -",
        "- --0",
        "0",
        "6700000000000",
        "к. - -,",
        "корп. - -,",
        ",- -",
        "- -",
        "--",
        ", .,",
        ", .",
        "кв. общ",
        "кв. ОБЩ",
    ]
    replace_doc_authorities = [
        "ytn",
        "бюро загс",
        "нет",
        "отдел загс",
        "отдел",
        " ",
        "мвд",
        "мид",
        "министерство юстиции",
        "министерством юстиции",
    ]
    replace_address_stops_pattern = "|".join(replace_address_stops)
    replace_name_stops = ["нет", "-"]
    replace_name_stops_pattern = "|".join(replace_name_stops)
    replace_middlename_stops = ["нет", "-", "нет отч", "нет отчеств", "нет отчества"]
    replace_middlename_stops_pattern = "|".join(replace_middlename_stops)
    birth_cert_format_prefix_pattern = "^([2-9]|1+|[ivx]+)[ -]?[а-яё]"
    replace_birth_cert_format_prefix_pattern = "^([2-9]|1+|[ivx]+)[ -]?(но|чо|вн|ед|ро|лю|бп|жг|тп|ал|ою|жс|ки|вл|ег|ид|бк|кг|ап|фп|жд|ке|фм)"
    replace_trailing_dot_pattern = r"(?<=\s|^)\.(\S)"
    replace_street_stops_pattern = (
        "\\b(\\.НЕТ|Нет ул\\.|Нет ул|НЕТ УЛ|нет|Нет|НЕТ|--)\\b"
    )
    replace_house_stops_pattern = (
        "\\b(нет|Нет|НЕТ|0|общ|общ\\.|ОБЩ|СОГБУ|СОГУ ГЦ|дом|ДОМ|СОГБУГЦ|СОГУ|--)\\b"
    )
    replace_room_stops_pattern = (
        "\\b(нет|Нет|НЕТ|0|кв\\.|КВ\\.|кв|КВ|общ|общ\\.|ОБЩ|инт|ВСРФ|всрф|--)\\b"
    )
    med_schema = StructType(
        [
            StructField("id", StringType(), True),
            StructField("num", StringType(), True),
            StructField("person_data", StringType(), True),
            StructField("polis_ser", StringType(), True),
            StructField("polis_num", StringType(), True),
            StructField("card_number", StringType(), True),
            StructField("disease_code", StringType(), True),
            StructField("birthday", StringType(), True),
            StructField("service_date", StringType(), True),
            StructField("service_code", StringType(), True),
            StructField("service_quantity", StringType(), True),
            StructField("service_cost", StringType(), True),
            StructField("reason_payment_reduction", StringType(), True),
            StructField("payment_reduction", StringType(), True),
            StructField("infringement_point_of_the_list", StringType(), True),
            StructField("size_reduction_tarif", StringType(), True),
            StructField("tarif", StringType(), True),
            StructField("sum_reduction_payment", StringType(), True),
            StructField("size_financial_sanctions", StringType(), True),
            StructField("sum_financial_sanctions", StringType(), True),
            StructField("date_add", StringType(), True),
            StructField("date_remove", StringType(), True),
            StructField("is_deleted", StringType(), True),
            StructField("act_id", StringType(), True),
            StructField("tpe_code", StringType(), True),
            StructField("analyze_period", StringType(), True),
            StructField("person_address", StringType(), True),
            StructField("is_blocked", StringType(), True),
            StructField("is_finished", StringType(), True),
            StructField("tab_id", StringType(), True),
            StructField("act_id_o", StringType(), True),
            StructField("pac_id_o", StringType(), True),
            StructField("sluch_id_o", StringType(), True),
            StructField("serv_id_o", StringType(), True),
            StructField("md", StringType(), True),
            StructField("sluch_h", StringType(), True),
            StructField("w", StringType(), True),
            StructField("service_beg_date", StringType(), True),
            StructField("user_id", StringType(), True),
            StructField("dkk1_u", StringType(), True),
        ]
    )
    med_tabs_schema = StructType(
        [
            StructField("id", StringType(), True),
            StructField("num", StringType(), True),
            StructField("person_data", StringType(), True),
            StructField("polis_ser", StringType(), True),
            StructField("polis_num", StringType(), True),
            StructField("card_number", StringType(), True),
            StructField("disease_code", StringType(), True),
            StructField("birthday", StringType(), True),
            StructField("service_date", StringType(), True),
            StructField("service_code", StringType(), True),
            StructField("service_quantity", StringType(), True),
            StructField("service_cost", StringType(), True),
            StructField("reason_payment_reduction", StringType(), True),
            StructField("payment_reduction", StringType(), True),
            StructField("infringement_point_of_the_list", StringType(), True),
            StructField("size_reduction_tarif", StringType(), True),
            StructField("tarif", StringType(), True),
            StructField("sum_reduction_payment", StringType(), True),
            StructField("size_financial_sanctions", StringType(), True),
            StructField("sum_financial_sanctions", StringType(), True),
            StructField("date_add", StringType(), True),
            StructField("date_remove", StringType(), True),
            StructField("is_deleted", StringType(), True),
            StructField("act_id", StringType(), True),
            StructField("tab_id", StringType(), True),
            StructField("tpe_code", StringType(), True),
            StructField("person_address", StringType(), True),
            StructField("is_blocked", StringType(), True),
            StructField("is_finished", StringType(), True),
            StructField("analyze_period", StringType(), True),
            StructField("mec_id", StringType(), True),
            StructField("exp_inc_stat", StringType(), True),
            StructField("exp_rezult", StringType(), True),
            StructField("exp_oper_name", StringType(), True),
            StructField("exp_oper_date", StringType(), True),
            StructField("exp_diag_o", StringType(), True),
            StructField("exp_diag_tr", StringType(), True),
            StructField("exp_diag_accomp", StringType(), True),
            StructField("exp_pdiag", StringType(), True),
            StructField("exp_pdiag_tr", StringType(), True),
            StructField("exp_pdiag_accomp", StringType(), True),
            StructField("exp_inf_collect", StringType(), True),
            StructField("exp_inf_coll_err", StringType(), True),
            StructField("exp_inf_diag", StringType(), True),
            StructField("exp_inf_diag_tr", StringType(), True),
            StructField("exp_inf_diag_accomp", StringType(), True),
            StructField("exp_inf_diag_err", StringType(), True),
            StructField("exp_inf_treat", StringType(), True),
            StructField("exp_inf_treat_err", StringType(), True),
            StructField("exp_inf_contin", StringType(), True),
            StructField("exp_inf_contin_err", StringType(), True),
            StructField("exp_inf_conclus", StringType(), True),
            StructField("exp_g_err", StringType(), True),
            StructField("act_id_o", StringType(), True),
            StructField("pac_id_o", StringType(), True),
            StructField("sluch_id_o", StringType(), True),
            StructField("serv_id_o", StringType(), True),
            StructField("md", StringType(), True),
            StructField("sluch_h", StringType(), True),
            StructField("mee_tab", StringType(), True),
            StructField("w", StringType(), True),
            StructField("service_beg_date", StringType(), True),
            StructField("user_id", StringType(), True),
            StructField("dkk1_u", StringType(), True),
        ]
    )

    def _join_by_main_id(self, df):
        null_df = df.filter(col("id").isNull() | col("birth_date").isNull())
        full_df = df.filter(col("id").isNotNull() & col("birth_date").isNotNull())

        return (
            full_df.groupBy(["id", "birth_date"])
            .agg(
                array_compact(array_distinct(flatten(collect_list("names")))).alias(
                    "names"
                ),
                array_compact(array_distinct(flatten(collect_list("documents")))).alias(
                    "documents"
                ),
                array_compact(array_distinct(flatten(collect_list("phones")))).alias(
                    "phones"
                ),
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_list("relations")))).alias(
                    "relations"
                ),
                array_compact(
                    array_distinct(flatten(collect_list("raw_metadata")))
                ).alias("raw_metadata"),
                first(col("sex"), ignorenulls=True).alias("sex"),
                first(col("birth_place"), ignorenulls=True).alias("birth_place"),
                max(col("actuality")).alias("actuality"),
            )
            .unionByName(null_df)
            .drop("id")
        )

    def _join_by_id(self, df):
        return (
            df.groupBy("join_id")
            .agg(
                array_compact(array_distinct(flatten(collect_list("names")))).alias(
                    "names"
                ),
                array_compact(array_distinct(flatten(collect_list("documents")))).alias(
                    "documents"
                ),
                array_compact(array_distinct(flatten(collect_list("phones")))).alias(
                    "phones"
                ),
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_list("relations")))).alias(
                    "relations"
                ),
                array_compact(
                    array_distinct(flatten(collect_list("raw_metadata")))
                ).alias("raw_metadata"),
                first(col("sex"), ignorenulls=True).alias("sex"),
                first(col("birth_date"), ignorenulls=True).alias("birth_date"),
                first(col("birth_place"), ignorenulls=True).alias("birth_place"),
                max(col("actuality")).alias("actuality"),
                min(col("id")).alias("min_id"),
                max(col("id")).alias("max_id"),
            )
            .withColumn("id", when(col("min_id") == col("max_id"), col("min_id")))
            .drop("join_id", "min_id", "max_id")
        )

    def _join_by_docs(self, df):
        df_keys = (
            df.select(
                "row_id",
                "name",
                "birth_date",
                explode(col("documents.serial")).alias("key"),
            )
            .filter(
                col("key").isNotNull()
                & col("birth_date").isNotNull()
                & col("name").isNotNull()
            )
            .withColumn("hashed_key", xxhash64("name", "birth_date", "key"))
        )
        df_keys.persist(StorageLevel.DISK_ONLY).count()

        mapping = df.select("row_id").withColumn("group_id", col("row_id"))
        mapping.persist(StorageLevel.DISK_ONLY).count()

        changed = True
        iteration = 0

        while changed:
            iteration += 1
            key_groups = df_keys.join(mapping, "row_id")
            min_groups = key_groups.groupBy("hashed_key").agg(
                min("group_id").alias("min_group_id")
            )
            new_mapping = (
                df_keys.join(min_groups, "hashed_key")
                .groupBy("row_id")
                .agg(min("min_group_id").alias("new_group_id"))
            )
            check_df = mapping.join(new_mapping, "row_id")
            diff_df = check_df.filter(col("group_id") != col("new_group_id"))

            if diff_df.isEmpty():
                changed = False
            else:
                old_mapping = mapping
                next_mapping = new_mapping.select(
                    "row_id", col("new_group_id").alias("group_id")
                )
                mapping = next_mapping.persist(StorageLevel.MEMORY_AND_DISK)
                old_mapping.unpersist()

        prepared_df = df.join(mapping, "row_id", "left")
        prepared_df.persist(StorageLevel.DISK_ONLY)
        mapping.unpersist()
        df_keys.unpersist()

        null_df = prepared_df.filter(col("group_id").isNull()).drop("row_id")
        full_df = prepared_df.filter(col("group_id").isNotNull())

        result = (
            full_df.groupBy(["group_id", "name", "birth_date"])
            .agg(
                array_compact(array_distinct(flatten(collect_list("names")))).alias(
                    "names"
                ),
                array_compact(array_distinct(flatten(collect_list("documents")))).alias(
                    "documents"
                ),
                array_compact(array_distinct(flatten(collect_list("phones")))).alias(
                    "phones"
                ),
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_list("relations")))).alias(
                    "relations"
                ),
                array_compact(
                    array_distinct(flatten(collect_list("raw_metadata")))
                ).alias("raw_metadata"),
                first(col("sex"), ignorenulls=True).alias("sex"),
                first(col("birth_place"), ignorenulls=True).alias("birth_place"),
                max(col("actuality")).alias("actuality"),
                min(col("join_id")).alias("join_id"),
                min(col("id")).alias("min_id"),
                max(col("id")).alias("max_id"),
            )
            .withColumn("id", when(col("min_id") == col("max_id"), col("min_id")))
            .drop("min_id", "max_id")
            .unionByName(null_df)
            .drop("group_id", "name")
        )

        return result, prepared_df

    def _prepare_med(self):
        return (
            self.read(path="ree_md.csv", sep=",", header=True)
            .select("fam", "im", "ot", "w", "dr", "code")
            .filter(~col("fam").rlike(self.filter_med_prefixes_pattern))
            .withColumn(
                "fam", split(lower(col("fam")), r"\s*(бывшая|бывший| и |бавшая)\s*")
            )
            .withColumn("fam", explode(col("fam")))
            .withColumn(
                "fam",
                regexp_replace(
                    col("fam"), self.replace_med_fam_suffix_stops_pattern, ""
                ),
            )
            .withColumn(
                "fam",
                regexp_replace(
                    lower(col("fam")),
                    f"\\b({self.replace_med_fam_stops_pattern})\\b",
                    "",
                ),
            )
            .withColumn(
                "ot",
                regexp_replace(
                    lower(col("ot")),
                    f"\\b({self.replace_med_names_stops_pattern})\\b",
                    "",
                ),
            )
            .withColumn("names", name_parts_udf("im", "fam", "ot"))
            .filter(col("names").isNotNull())
            .withColumn(
                "documents",
                document_udf(
                    when(
                        length(col("code")) == 11,
                        lit("снилс без контрольной суммы"),
                    ).otherwise(lit("снилс")),
                    col("code"),
                ),
            )
            .filter(col("documents").isNotNull())
            .withColumn("birth_date", birth_date_udf("dr", lit("%Y-%m-%d")))
            .withColumn("names", col("names"))
            .withColumn("snils", col("documents.serial"))
            .select(
                col("names").alias("md_name"),
                col("snils").alias("md_snils"),
                col("birth_date").alias("md_birth_date"),
                col("code").alias("md"),
            )
            .filter(col("md_name").isNotNull() & col("md_snils").isNotNull())
            .distinct()
        )

    def _prepare_services_doubles_result(self):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("polis", StringType(), True),
                StructField("soname", StringType(), True),
                StructField("birthday", StringType(), True),
                StructField("code_service", StringType(), True),
                StructField("date_service", StringType(), True),
                StructField("count_day_treatment", StringType(), True),
                StructField("cervice_cost", StringType(), True),
                StructField("removed_payment", StringType(), True),
                StructField("id_act", StringType(), True),
                StructField("code_tpe", StringType(), True),
                StructField("date_add", StringType(), True),
                StructField("date_deleted", StringType(), True),
                StructField("is_deleted", StringType(), True),
                StructField("type_double", StringType(), True),
                StructField("tab_id", StringType(), True),
                StructField("cross_rec", StringType(), True),
                StructField("date_receipt", StringType(), True),
                StructField("type_service", StringType(), True),
                StructField("handle", StringType(), True),
                StructField("err", StringType(), True),
                StructField("num", StringType(), True),
                StructField("description", StringType(), True),
                StructField("removed_sum", StringType(), True),
                StructField("diagnosis", StringType(), True),
            ]
        )
        return (
            self.read(
                path="services_doubles_result.csv", sep=",", schema=schema, header=True
            )
            .select(col("soname").alias("name"), "polis", "birthday", "date_service")
            .filter(length(regexp_replace(col("polis"), " ", "")) > 8)
            .withColumn("names", name_udf("name"))
            .filter(col("names").isNotNull())
            .withColumn(
                "documents",
                when(
                    ~col("polis").contains("/"),
                    document_udf(lit("номер страхового полиса"), col("polis")),
                ),
            )
            .filter(col("documents").isNotNull())
            .withColumn("names", array(col("names")))
            .withColumn("documents", array(col("documents")))
            .withColumn("birth_date", birth_date_udf("birthday", lit("%Y-%m-%d")))
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("date_service"), "yyyy-MM-dd"),
                    lit("%Y-%m-%d"),
                ),
            )
            .groupBy(["names", "documents", "birth_date"])
            .agg(max(col("actuality")).alias("actuality"))
            .withColumn("sex", lit(None))
            .withColumn("address", array())
            .withColumn("relations", array())
        )

    def _prepare_relax_persons_raw_data(self, md_df):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("person_data", StringType(), True),
                StructField("birthday", StringType(), True),
                StructField("polis_num", StringType(), True),
                StructField("polis_ser", StringType(), True),
                StructField("person_address", StringType(), True),
                StructField("tpe", StringType(), True),
                StructField("department", StringType(), True),
                StructField("card_number", StringType(), True),
                StructField("disease_code", StringType(), True),
                StructField("treatment_outcome", StringType(), True),
                StructField("service_code", StringType(), True),
                StructField("service_date", StringType(), True),
                StructField("service_quantity", StringType(), True),
                StructField("service_cost", StringType(), True),
                StructField("date_add", StringType(), True),
                StructField("is_deleted", StringType(), True),
                StructField("analyze_period", StringType(), True),
                StructField("act_id", StringType(), True),
                StructField("pac_id", StringType(), True),
                StructField("sluch_id", StringType(), True),
                StructField("serv_id", StringType(), True),
                StructField("tab_id", StringType(), True),
                StructField("tarif", StringType(), True),
                StructField("sluch_h", StringType(), True),
                StructField("md", StringType(), True),
                StructField("w", StringType(), True),
                StructField("service_beg_date", StringType(), True),
                StructField("user_id", StringType(), True),
                StructField("dkk1_u", StringType(), True),
            ]
        )
        return (
            self.read(
                path="relax_persons_raw_data.csv", sep=",", schema=schema, header=True
            )
            .select(
                col("person_data").alias("name"),
                "polis_num",
                "polis_ser",
                "birthday",
                "service_date",
                "person_address",
                "md",
            )
            .filter(
                ~(
                    col("polis_num").isin(self.ignored_polis_vals)
                    | col("polis_num").rlike(
                        f"({self.ignored_polis_part_vals_pattern})"
                    )
                )
            )
            .withColumn("polis", upper(concat_ws("", "polis_ser", "polis_num")))
            .filter(length(col("polis")) > 8)
            .withColumn("names", name_udf("name"))
            .filter(col("names").isNotNull())
            .withColumn(
                "documents",
                document_udf(lit("номер страхового полиса"), col("polis")),
            )
            .filter(col("documents").isNotNull())
            .withColumn(
                "person_address", regexp_replace(col("person_address"), ", -, -", "")
            )
            .withColumn(
                "person_address",
                regexp_replace(
                    col("person_address"),
                    f"\\b({self.replace_address_stops_pattern})\\b",
                    "",
                ),
            )
            .withColumn("names", array(col("names")))
            .withColumn("documents", array(col("documents")))
            .withColumn(
                "birth_date", birth_date_udf("birthday", lit("%Y-%m-%d %H:%M:%S.%f"))
            )
            .withColumn(
                "actuality",
                actuality_date_udf(
                    from_unixtime(col("service_date"), "yyyy-MM-dd"),
                    lit("%Y-%m-%d"),
                ),
            )
            .withColumn(
                "address", array_compact(array(address_udf(col("person_address"))))
            )
            .join(broadcast(md_df), on="md", how="left")
            .withColumn(
                "relations",
                when(
                    col("md_name").isNotNull(),
                    array_compact(
                        array(
                            relations_udf(
                                concat_ws(
                                    " ",
                                    "md_name",
                                    "md_birth_date",
                                    "md_snils",
                                    lit("Врач"),
                                )
                            )
                        )
                    ),
                ),
            )
            .groupBy(["names", "documents", "birth_date"])
            .agg(
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_list("relations")))).alias(
                    "relations"
                ),
                max(col("actuality")).alias("actuality"),
            )
            .withColumn("sex", lit(None))
        )

    def _prepare_mediko_economic_certificate(self, path, schema):
        return (
            self.read(path=path, sep=",", schema=schema, header=True)
            .select(
                col("person_data").alias("name"),
                "polis_num",
                "polis_ser",
                "birthday",
                "service_date",
                "person_address",
                "md",
                "w",
                "id",
            )
            .filter(
                col("id").rlike("^\\d+$")
                & (col("polis_ser").isNull() | ~lower(col("polis_ser")).rlike("н|ц|г"))
            )
            .filter(
                ~(
                    col("polis_num").isin(self.ignored_polis_vals)
                    | col("polis_num").rlike(
                        f"({self.ignored_polis_part_vals_pattern})"
                    )
                )
            )
            .withColumn("polis", upper(concat_ws("", "polis_ser", "polis_num")))
            .filter(length(col("polis")) > 8)
            .withColumn("names", name_udf("name"))
            .filter(col("names").isNotNull())
            .withColumn(
                "documents",
                document_udf(lit("номер страхового полиса"), col("polis")),
            )
            .filter(col("documents").isNotNull())
            .withColumn(
                "person_address", regexp_replace(col("person_address"), ", -, -", "")
            )
            .withColumn(
                "person_address",
                regexp_replace(
                    col("person_address"),
                    f"\\b({self.replace_address_stops_pattern})\\b",
                    "",
                ),
            )
            .withColumn("names", array(col("names")))
            .withColumn("documents", array(col("documents")))
            .withColumn("birth_date", birth_date_udf("birthday", lit("%Y-%m-%d")))
            .withColumn(
                "sex",
                sex_udf(when(col("w") == "2", lit("0")).otherwise(col("w"))),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("service_date"), lit("%Y-%m-%d"))
            )
            .withColumn(
                "address", array_compact(array(address_udf(col("person_address"))))
            )
        )

    def _group_mediko_economic_certificate(self, df, md_df):
        return (
            df.join(broadcast(md_df), on="md", how="left")
            .withColumn(
                "relations",
                when(
                    col("md_name").isNotNull(),
                    array_compact(
                        array(
                            relations_udf(
                                concat_ws(
                                    " ",
                                    "md_name",
                                    "md_birth_date",
                                    "md_snils",
                                    lit("Врач"),
                                )
                            )
                        )
                    ),
                ),
            )
            .groupBy(["names", "documents", "birth_date", "sex"])
            .agg(
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_list("relations")))).alias(
                    "relations"
                ),
                max(col("actuality")).alias("actuality"),
            )
        )

    def _prepare_ins_temp_polis(self):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("foms_id_o", StringType(), True),
                StructField("fam_o", StringType(), True),
                StructField("im_o", StringType(), True),
                StructField("ot_o", StringType(), True),
                StructField("dr_o", StringType(), True),
                StructField("mr_o", StringType(), True),
                StructField("enp_u", StringType(), True),
                StructField("v_polic_o", StringType(), True),
                StructField("s_polic_u", StringType(), True),
                StructField("n_polic_o", StringType(), True),
                StructField("doc_num_o", StringType(), True),
                StructField("doc_ser_u", StringType(), True),
                StructField("date_add", StringType(), True),
                StructField("date_delete", StringType(), True),
                StructField("is_deleted", StringType(), True),
                StructField("d_beg_u", StringType(), True),
                StructField("q", StringType(), True),
            ]
        )

        return (
            self.read(path="ins_temp_polis.csv", sep=",", schema=schema, header=True)
            .select(
                col("fam_o").alias("lastname"),
                col("im_o").alias("firstname"),
                col("ot_o").alias("middlename"),
                col("dr_o").alias("birthday"),
                col("mr_o").alias("birth_place"),
                col("enp_u").alias("enp"),
                col("s_polic_u").alias("polic_ser"),
                col("n_polic_o").alias("polic_num"),
                col("doc_ser_u").alias("doc_ser"),
                col("doc_num_o").alias("doc_num"),
            )
            .replace("", None)
            .withColumn(
                "lastname",
                regexp_replace(
                    trim(lower(col("lastname"))),
                    f"^({self.replace_name_stops_pattern})$",
                    "",
                ),
            )
            .withColumn(
                "firstname",
                regexp_replace(
                    trim(lower(col("firstname"))),
                    f"^({self.replace_name_stops_pattern})$",
                    "",
                ),
            )
            .withColumn(
                "middlename",
                regexp_replace(
                    trim(lower(col("middlename"))),
                    f"^({self.replace_middlename_stops_pattern})$",
                    "",
                ),
            )
            .withColumn("names", name_parts_udf("firstname", "lastname", "middlename"))
            .filter(col("names").isNotNull())
            .withColumn("names", array(col("names")))
            .withColumn(
                "doc_type",
                when(
                    upper(col("doc_ser")).rlike("(ВУ|СБ|РФ)")
                    & (length(col("doc_num")) > 6),
                    lit("удостоверение беженца"),
                )
                .when(
                    col("doc_ser").isin(["80", "81", "82", "90"])
                    & ((length(col("doc_num")) == 6) | (length(col("doc_num")) == 7)),
                    lit("вид на жительство"),
                )
                .when(
                    col("doc_ser").isin(["820", "821", "900"])
                    & (length(col("doc_num")) == 6),
                    lit("вид на жительство"),
                )
                .when(
                    col("doc_ser").isin(["8214", "82N02"])
                    & (length(col("doc_num")) == 5),
                    lit("вид на жительство"),
                )
                .when(
                    (col("doc_ser") == "82N") & (length(col("doc_num")) == 7),
                    lit("вид на жительство"),
                ),
            )
            .withColumn(
                "doc_ser",
                when(
                    col("doc_type") == "вид на жительство",
                    regexp_replace(col("doc_ser"), r"N", ""),
                ).otherwise(col("doc_ser")),
            )
            .withColumn(
                "doc_number", upper(trim(concat_ws("", col("doc_ser"), col("doc_num"))))
            )
            .withColumn(
                "doc_number",
                when(
                    lower(col("doc_number")).rlike(
                        self.replace_birth_cert_format_prefix_pattern
                    ),
                    lit(None),
                )
                .when(
                    lower(col("doc_number")).rlike(
                        self.birth_cert_format_prefix_pattern
                    )
                    & ~(
                        col("birthday").startswith("20")
                        | col("birthday").startswith("199")
                    ),
                    lit(None),
                )
                .otherwise(col("doc_number")),
            )
            .withColumn(
                "polis_num",
                upper(trim(concat_ws("", col("polic_ser"), col("polic_num")))),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            document_udf(col("doc_type"), col("doc_number")),
                            document_udf(lit("номер страхового полиса"), col("enp")),
                            document_udf(
                                lit("номер страхового полиса"),
                                when(
                                    length(col("polic_num")) == 16, col("polic_num")
                                ).otherwise(col("polis_num")),
                            ),
                        )
                    )
                ),
            )
            .filter(size(col("documents")) > 0)
            .withColumn("birth_date", birth_date_udf("birthday", lit("%Y-%m-%d")))
            .withColumn("birth_place", address_udf(col("birth_place")))
            .groupBy(["names", "documents", "birth_date"])
            .agg(first("birth_place", ignorenulls=True).alias("birth_place"))
            .withColumn("id", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("actuality", lit(None))
            .withColumn("phones", array())
            .withColumn("relations", array())
            .withColumn("address", array())
            .withColumn("raw_metadata", array())
        )

    def _process_ree_pack_list(self, df):
        return (
            df.withColumn(
                "lastname",
                regexp_replace(
                    trim(lower(col("lastname"))),
                    f"^({self.replace_name_stops_pattern})$",
                    "",
                ),
            )
            .withColumn(
                "firstname",
                regexp_replace(
                    trim(lower(col("firstname"))),
                    f"^({self.replace_name_stops_pattern})$",
                    "",
                ),
            )
            .withColumn(
                "middlename",
                regexp_replace(
                    trim(lower(col("middlename"))),
                    f"^({self.replace_middlename_stops_pattern})$",
                    "",
                ),
            )
            .withColumn("names", name_parts_udf("firstname", "lastname", "middlename"))
            .filter(col("names").isNotNull())
            .withColumn("names", array(col("names")))
            .withColumn(
                "doc_type",
                when(
                    upper(col("doc_ser")).rlike("(ВУ|СБ|РФ)")
                    & (length(col("doc_num")) > 6),
                    lit("удостоверение беженца"),
                )
                .when(
                    col("doc_ser").isin(["80", "81", "82", "90"])
                    & ((length(col("doc_num")) == 6) | (length(col("doc_num")) == 7)),
                    lit("вид на жительство"),
                )
                .when(
                    col("doc_ser").isin(["820", "821", "900"])
                    & (length(col("doc_num")) == 6),
                    lit("вид на жительство"),
                )
                .when(
                    col("doc_ser").isin(["8214", "8202"])
                    & (length(col("doc_num")) == 5),
                    lit("вид на жительство"),
                )
                .when(
                    (col("doc_ser").isin(["82N", "82 N"]))
                    & (length(col("doc_num")) == 7),
                    lit("вид на жительство"),
                )
                .when(
                    (col("doc_ser").startswith("82-")) & (length(col("doc_num")) == 6),
                    lit("паспорт гражданина рф"),
                )
                .when(
                    (col("doc_type") == "4")
                    & (
                        upper(col("doc_ser")).startswith("СМЛ")
                        | col("doc_ser").startswith("ФПС")
                        | col("doc_num").startswith("СМЛ")
                        | col("doc_num").startswith("ФПС")
                    ),
                    lit("удостоверение личности военнослужащего"),
                )
                .when(
                    col("doc_type") == "7",
                    lit("удостоверение личности военнослужащего"),
                ),
            )
            .withColumn(
                "doc_ser",
                when(
                    col("doc_type") == "вид на жительство",
                    regexp_replace(col("doc_ser"), r"N", ""),
                ).otherwise(col("doc_ser")),
            )
            .withColumn(
                "doc_number", upper(trim(concat_ws("", col("doc_ser"), col("doc_num"))))
            )
            .withColumn(
                "doc_number",
                when(
                    col("doc_type") == "удостоверение личности военнослужащего",
                    regexp_replace(col("doc_number"), r"МВД|ПЧ-14|ЯО 100/1", ""),
                ).otherwise(col("doc_number")),
            )
            .withColumn(
                "doc_number",
                when(
                    lower(col("doc_number")).rlike(
                        self.replace_birth_cert_format_prefix_pattern
                    ),
                    lit(None),
                )
                .when(
                    lower(col("doc_number")).rlike(
                        self.birth_cert_format_prefix_pattern
                    )
                    & ~(
                        col("birthday").startswith("20")
                        | col("birthday").startswith("199")
                    ),
                    lit(None),
                )
                .otherwise(col("doc_number")),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            document_udf(col("doc_type"), col("doc_number")),
                            when(
                                col("snils").rlike("^\\d{3}-\\d{3}-\\d{3} \\d{2}$"),
                                document_udf(lit("снилс"), col("snils")),
                            ),
                        )
                    )
                ),
            )
            .filter(size(col("documents")) > 0)
            .withColumn("phones", array_compact(array(phone_udf(col("phone")))))
            .withColumn(
                "sex",
                sex_udf(when(col("sex") == "2", lit("0")).otherwise(col("sex"))),
            )
            .withColumn("birth_date", birth_date_udf("birthday", lit("%Y-%m-%d")))
            .select("names", "documents", "birth_date", "sex", "phones")
            .distinct()
            .withColumn("id", lit(None))
            .withColumn("birth_place", lit(None))
            .withColumn("actuality", lit(None))
            .withColumn("relations", array())
            .withColumn("address", array())
            .withColumn("raw_metadata", array())
        )

    def _prepare_ree_pac_list(self):
        schema = StructType(
            [
                StructField("id", StringType(), True),
                StructField("id_pac_o", StringType(), True),
                StructField("fam_o", StringType(), True),
                StructField("im_o", StringType(), True),
                StructField("ot_o", StringType(), True),
                StructField("w_o", StringType(), True),
                StructField("dr_o", StringType(), True),
                StructField("fam_p_u", StringType(), True),
                StructField("im_p_u", StringType(), True),
                StructField("ot_p_u", StringType(), True),
                StructField("w_p_u", StringType(), True),
                StructField("dr_p_u", StringType(), True),
                StructField("mr_u", StringType(), True),
                StructField("doctype_u", StringType(), True),
                StructField("docser_u", StringType(), True),
                StructField("docnum_u", StringType(), True),
                StructField("snils_u", StringType(), True),
                StructField("okatog_u", StringType(), True),
                StructField("okatop_u", StringType(), True),
                StructField("comentp_u", StringType(), True),
                StructField("date_add", StringType(), True),
                StructField("date_delete", StringType(), True),
                StructField("is_deleted", StringType(), True),
                StructField("act_id", StringType(), True),
                StructField("address", StringType(), True),
                StructField("err", StringType(), True),
                StructField("id_pac_mo", StringType(), True),
                StructField("dost_u", StringType(), True),
                StructField("dost_p_u", StringType(), True),
                StructField("operator_u", StringType(), True),
                StructField("tel_u", StringType(), True),
            ]
        )
        df = (
            self.read(path="ree_pac_list.csv", sep=",", schema=schema, header=True)
            .select(
                col("fam_o").alias("lastname"),
                col("im_o").alias("firstname"),
                col("ot_o").alias("middlename"),
                col("dr_o").alias("birthday"),
                col("w_o").alias("sex"),
                col("tel_u").alias("phone"),
                col("fam_p_u").alias("lastname_pr"),
                col("im_p_u").alias("firstname_pr"),
                col("ot_p_u").alias("middlename_pr"),
                col("dr_p_u").alias("birthday_pr"),
                col("w_p_u").alias("sex_pr"),
                col("snils_u").alias("snils"),
                col("doctype_u").alias("doc_type"),
                col("docser_u").alias("doc_ser"),
                col("docnum_u").alias("doc_num"),
            )
            .replace("", None)
        )
        df = df.select(
            col("lastname_pr").alias("lastname"),
            col("firstname_pr").alias("firstname"),
            col("middlename_pr").alias("middlename"),
            col("birthday_pr").alias("birthday"),
            col("sex_pr").alias("sex"),
            "snils",
            "doc_ser",
            "doc_num",
            "phone",
            "doc_type",
        ).unionByName(
            df.select(
                "lastname",
                "firstname",
                "middlename",
                "birthday",
                "sex",
                "snils",
                "doc_ser",
                "doc_num",
                "phone",
                "doc_type",
            ).filter(col("lastname").isNotNull())
        )
        df.persist(StorageLevel.DISK_ONLY).count()

        return self._process_ree_pack_list(df.repartition(200)), df

    def _read_ins_data_policy_reception(self):
        schema = StructType(
            [
                StructField("id_o", StringType(), True),
                StructField("foms_id_u", IntegerType(), True),
                StructField("tip_op_o", StringType(), True),
                StructField("fam_o", StringType(), True),
                StructField("im_o", StringType(), True),
                StructField("ot_o", StringType(), True),
                StructField("w_o", StringType(), True),
                StructField("dr_o", StringType(), True),
                StructField("true_dr_o", StringType(), True),
                StructField("c_oksm_u", StringType(), True),
                StructField("ss_u", StringType(), True),
                StructField("phone_u", StringType(), True),
                StructField("email_u", StringType(), True),
                StructField("fio_pr_u", StringType(), True),
                StructField("contackt_u", StringType(), True),
                StructField("ddeath_u", StringType(), True),
                StructField("doc_type_o", StringType(), True),
                StructField("doc_ser_u", StringType(), True),
                StructField("doc_num_o", StringType(), True),
                StructField("doc_date_o", StringType(), True),
                StructField("name_vp_u", StringType(), True),
                StructField("mr_o", StringType(), True),
                StructField("o_fam_u", StringType(), True),
                StructField("o_im_u", StringType(), True),
                StructField("o_ot_u", StringType(), True),
                StructField("o_w_u", StringType(), True),
                StructField("o_dr_u", StringType(), True),
                StructField("o_old_enp_u", StringType(), True),
                StructField("o_doc_type_u", StringType(), True),
                StructField("o_doc_ser_u", StringType(), True),
                StructField("o_doc_num_u", StringType(), True),
                StructField("o_doc_date_u", StringType(), True),
                StructField("o_name_vp_u", StringType(), True),
                StructField("o_mr_u", StringType(), True),
                StructField("bomg_o", StringType(), True),
                StructField("subj_u", StringType(), True),
                StructField("indx_u", StringType(), True),
                StructField("okato_u", StringType(), True),
                StructField("rn_name_u", StringType(), True),
                StructField("np_name_u", StringType(), True),
                StructField("ul_u", StringType(), True),
                StructField("dom_u", StringType(), True),
                StructField("korp_u", StringType(), True),
                StructField("kv_u", StringType(), True),
                StructField("dreg_u", StringType(), True),
                StructField("p_subj_u", StringType(), True),
                StructField("p_indx_u", StringType(), True),
                StructField("p_okato_u", StringType(), True),
                StructField("p_rn_name_u", StringType(), True),
                StructField("p_np_name_u", StringType(), True),
                StructField("p_ul_u", StringType(), True),
                StructField("p_dom_u", StringType(), True),
                StructField("p_korp_u", StringType(), True),
                StructField("p_kv_u", StringType(), True),
                StructField("d_vizit_o", StringType(), True),
                StructField("method_o", StringType(), True),
                StructField("petition_o", StringType(), True),
                StructField("rsmo_u", StringType(), True),
                StructField("rpolic_u", StringType(), True),
                StructField("fpolic_o", StringType(), True),
                StructField("ter_st_u", StringType(), True),
                StructField("enp_u", StringType(), True),
                StructField("ogrn_smo_u", StringType(), True),
                StructField("v_polic_o", StringType(), True),
                StructField("n_polic_o", StringType(), True),
                StructField("s_polic_u", StringType(), True),
                StructField("d_beg_u", StringType(), True),
                StructField("d_end_u", StringType(), True),
                StructField("d_stop_u", StringType(), True),
                StructField("erp_o", StringType(), True),
                StructField("n_order_o", StringType(), True),
                StructField("d_order_o", StringType(), True),
                StructField("p_type_u", StringType(), True),
                StructField("photo_u", StringType(), True),
                StructField("signature_u", StringType(), True),
                StructField("date_add", StringType(), True),
                StructField("date_delete", StringType(), True),
                StructField("is_deleted", StringType(), True),
                StructField("is_blocked", StringType(), True),
                StructField("is_activ", StringType(), True),
                StructField("record_state", StringType(), True),
                StructField("err", StringType(), True),
                StructField("mob_phone", StringType(), True),
                StructField("mob_phone_pr", StringType(), True),
                StructField("delete_reason", StringType(), True),
                StructField("mark", StringType(), True),
                StructField("operator", StringType(), True),
                StructField("type_record", StringType(), True),
                StructField("id_p", StringType(), True),
                StructField("prz_cod", StringType(), True),
                StructField("count_export", StringType(), True),
                StructField("who_pr", StringType(), True),
                StructField("doc_type_pr", StringType(), True),
                StructField("doc_num_pr", StringType(), True),
                StructField("doc_ser_pr", StringType(), True),
                StructField("doc_date_pr", StringType(), True),
                StructField("cod_type_p", StringType(), True),
                StructField("doc_num_p", StringType(), True),
                StructField("doc_ser_p", StringType(), True),
                StructField("doc_date_p", StringType(), True),
                StructField("name_vp_p", StringType(), True),
                StructField("vid_beg", StringType(), True),
                StructField("vid_end", StringType(), True),
                StructField("date_export", StringType(), True),
                StructField("birth_oksm_u", StringType(), True),
                StructField("kateg_o", StringType(), True),
                StructField("docexp_1", StringType(), True),
                StructField("docexp_3", StringType(), True),
                StructField("idoc_type_u", StringType(), True),
                StructField("idoc_ser_u", StringType(), True),
                StructField("idoc_num_u", StringType(), True),
                StructField("iname_vp_u", StringType(), True),
                StructField("imr_u", StringType(), True),
            ]
        )
        return self.read(
            path="ins_data_policy_reception.csv", sep=",", schema=schema, header=True
        ).select(
            col("foms_id_u").alias("id"),
            col("fam_o").alias("lastname"),
            col("im_o").alias("firstname"),
            col("ot_o").alias("middlename"),
            col("o_fam_u").alias("prev_lastname"),
            col("o_im_u").alias("prev_firstname"),
            col("o_ot_u").alias("prev_middlename"),
            col("w_o").alias("sex"),
            col("dr_o").alias("birth"),
            col("fio_pr_u").alias("representative_name"),
            col("ss_u").alias("snils"),
            col("doc_type_o").alias("doc_type_num"),
            col("doc_ser_u").alias("doc_serial_num"),
            col("doc_num_o").alias("doc_num"),
            col("doc_date_o").alias("doc_issue_date"),
            col("name_vp_u").alias("doc_authority"),
            col("o_doc_type_u").alias("prev_doc_type_num"),
            col("o_doc_ser_u").alias("prev_doc_serial_num"),
            col("o_doc_num_u").alias("prev_doc_num"),
            col("o_doc_date_u").alias("prev_doc_issue_date"),
            col("o_name_vp_u").alias("prev_doc_authority"),
            col("mr_o").alias("birth_place"),
            col("idoc_ser_u").alias("i_doc_serial_num"),
            col("idoc_num_u").alias("i_doc_num"),
            col("iname_vp_u").alias("i_doc_authority"),
            col("mob_phone").alias("phone"),
            col("enp_u").alias("current_enp"),
            col("o_old_enp_u").alias("prev_enp"),
            col("d_vizit_o").alias("last_visit"),
            col("indx_u").alias("registered_index"),
            col("rn_name_u").alias("registered_area"),
            col("np_name_u").alias("registered_city"),
            col("ul_u").alias("registered_street"),
            col("dom_u").alias("registered_house"),
            col("kv_u").alias("registered_room"),
            col("p_indx_u").alias("index"),
            col("p_rn_name_u").alias("area"),
            col("p_np_name_u").alias("city"),
            col("p_ul_u").alias("street"),
            col("p_dom_u").alias("house"),
            col("p_kv_u").alias("room"),
            col("doc_ser_pr"),
            col("doc_num_pr"),
            col("doc_date_pr"),
            col("s_polic_u").alias("polic_ser"),
            col("n_polic_o").alias("polic_num"),
        )

    def _read_ins_data_unique(self):
        schema = StructType(
            [
                StructField("id_o", StringType(), True),
                StructField("foms_id_u", IntegerType(), True),
                StructField("tip_op_o", StringType(), True),
                StructField("fam_o", StringType(), True),
                StructField("im_o", StringType(), True),
                StructField("ot_o", StringType(), True),
                StructField("w_o", StringType(), True),
                StructField("dr_o", StringType(), True),
                StructField("true_dr_o", StringType(), True),
                StructField("c_oksm_u", StringType(), True),
                StructField("ss_u", StringType(), True),
                StructField("phone_u", StringType(), True),
                StructField("email_u", StringType(), True),
                StructField("fio_pr_u", StringType(), True),
                StructField("contackt_u", StringType(), True),
                StructField("ddeath_u", StringType(), True),
                StructField("doc_type_o", StringType(), True),
                StructField("doc_ser_u", StringType(), True),
                StructField("doc_num_o", StringType(), True),
                StructField("doc_date_o", StringType(), True),
                StructField("name_vp_u", StringType(), True),
                StructField("mr_o", StringType(), True),
                StructField("o_fam_u", StringType(), True),
                StructField("o_im_u", StringType(), True),
                StructField("o_ot_u", StringType(), True),
                StructField("o_w_u", StringType(), True),
                StructField("o_dr_u", StringType(), True),
                StructField("o_old_enp_u", StringType(), True),
                StructField("o_doc_type_u", StringType(), True),
                StructField("o_doc_ser_u", StringType(), True),
                StructField("o_doc_num_u", StringType(), True),
                StructField("o_doc_date_u", StringType(), True),
                StructField("o_name_vp_u", StringType(), True),
                StructField("o_mr_u", StringType(), True),
                StructField("bomg_o", StringType(), True),
                StructField("subj_u", StringType(), True),
                StructField("indx_u", StringType(), True),
                StructField("okato_u", StringType(), True),
                StructField("rn_name_u", StringType(), True),
                StructField("np_name_u", StringType(), True),
                StructField("ul_u", StringType(), True),
                StructField("dom_u", StringType(), True),
                StructField("korp_u", StringType(), True),
                StructField("kv_u", StringType(), True),
                StructField("dreg_u", StringType(), True),
                StructField("p_subj_u", StringType(), True),
                StructField("p_indx_u", StringType(), True),
                StructField("p_okato_u", StringType(), True),
                StructField("p_rn_name_u", StringType(), True),
                StructField("p_np_name_u", StringType(), True),
                StructField("p_ul_u", StringType(), True),
                StructField("p_dom_u", StringType(), True),
                StructField("p_korp_u", StringType(), True),
                StructField("p_kv_u", StringType(), True),
                StructField("d_vizit_o", StringType(), True),
                StructField("method_o", StringType(), True),
                StructField("petition_o", StringType(), True),
                StructField("rsmo_u", StringType(), True),
                StructField("rpolic_u", StringType(), True),
                StructField("fpolic_o", StringType(), True),
                StructField("ter_st_u", StringType(), True),
                StructField("enp_u", StringType(), True),
                StructField("ogrn_smo_u", StringType(), True),
                StructField("v_polic_o", StringType(), True),
                StructField("n_polic_o", StringType(), True),
                StructField("s_polic_u", StringType(), True),
                StructField("d_beg_u", StringType(), True),
                StructField("d_end_u", StringType(), True),
                StructField("d_stop_u", StringType(), True),
                StructField("erp_o", StringType(), True),
                StructField("n_order_o", StringType(), True),
                StructField("d_order_o", StringType(), True),
                StructField("p_type_u", StringType(), True),
                StructField("photo_u", StringType(), True),
                StructField("signature_u", StringType(), True),
                StructField("date_add", StringType(), True),
                StructField("date_delete", StringType(), True),
                StructField("is_deleted", StringType(), True),
                StructField("is_blocked", StringType(), True),
                StructField("is_activ", StringType(), True),
                StructField("record_state", StringType(), True),
                StructField("err", StringType(), True),
                StructField("mob_phone", StringType(), True),
                StructField("mob_phone_pr", StringType(), True),
                StructField("delete_reason", StringType(), True),
                StructField("mark", StringType(), True),
                StructField("operator", StringType(), True),
                StructField("type_record", StringType(), True),
                StructField("id_p", StringType(), True),
                StructField("prz_cod", StringType(), True),
                StructField("count_export", StringType(), True),
                StructField("who_pr", StringType(), True),
                StructField("doc_type_pr", StringType(), True),
                StructField("doc_num_pr", StringType(), True),
                StructField("doc_ser_pr", StringType(), True),
                StructField("doc_date_pr", StringType(), True),
                StructField("cod_type_p", StringType(), True),
                StructField("doc_num_p", StringType(), True),
                StructField("doc_ser_p", StringType(), True),
                StructField("doc_date_p", StringType(), True),
                StructField("name_vp_p", StringType(), True),
                StructField("vid_beg", StringType(), True),
                StructField("vid_end", StringType(), True),
                StructField("date_export", StringType(), True),
                StructField("birth_oksm_u", StringType(), True),
                StructField("kateg_o", StringType(), True),
                StructField("docexp_1", StringType(), True),
                StructField("docexp_3", StringType(), True),
                StructField("idoc_type_u", StringType(), True),
                StructField("idoc_ser_u", StringType(), True),
                StructField("idoc_num_u", StringType(), True),
                StructField("iname_vp_u", StringType(), True),
                StructField("imr_u", StringType(), True),
                StructField("date_edit", StringType(), True),
                StructField("date_mo_attach", StringType(), True),
                StructField("date_mo_detachment", StringType(), True),
                StructField("mo", StringType(), True),
                StructField("attachment_type", StringType(), True),
                StructField("street_num", StringType(), True),
                StructField("action", StringType(), True),
                StructField("code_division", StringType(), True),
                StructField("SNILS_doctor", StringType(), True),
                StructField("date_upload", StringType(), True),
            ]
        )
        return self.read(
            path="ins_data_unique.csv", sep=",", schema=schema, header=True
        ).select(
            col("foms_id_u").alias("id"),
            col("fam_o").alias("lastname"),
            col("im_o").alias("firstname"),
            col("ot_o").alias("middlename"),
            col("o_fam_u").alias("prev_lastname"),
            col("o_im_u").alias("prev_firstname"),
            col("o_ot_u").alias("prev_middlename"),
            col("w_o").alias("sex"),
            col("dr_o").alias("birth"),
            col("fio_pr_u").alias("representative_name"),
            col("ss_u").alias("snils"),
            col("doc_type_o").alias("doc_type_num"),
            col("doc_ser_u").alias("doc_serial_num"),
            col("doc_num_o").alias("doc_num"),
            col("doc_date_o").alias("doc_issue_date"),
            col("name_vp_u").alias("doc_authority"),
            col("o_doc_type_u").alias("prev_doc_type_num"),
            col("o_doc_ser_u").alias("prev_doc_serial_num"),
            col("o_doc_num_u").alias("prev_doc_num"),
            col("o_doc_date_u").alias("prev_doc_issue_date"),
            col("o_name_vp_u").alias("prev_doc_authority"),
            col("mr_o").alias("birth_place"),
            col("idoc_ser_u").alias("i_doc_serial_num"),
            col("idoc_num_u").alias("i_doc_num"),
            col("iname_vp_u").alias("i_doc_authority"),
            col("mob_phone").alias("phone"),
            col("enp_u").alias("current_enp"),
            col("o_old_enp_u").alias("prev_enp"),
            col("d_vizit_o").alias("last_visit"),
            col("indx_u").alias("registered_index"),
            col("rn_name_u").alias("registered_area"),
            col("np_name_u").alias("registered_city"),
            col("ul_u").alias("registered_street"),
            col("dom_u").alias("registered_house"),
            col("kv_u").alias("registered_room"),
            col("p_indx_u").alias("index"),
            col("p_rn_name_u").alias("area"),
            col("p_np_name_u").alias("city"),
            col("p_ul_u").alias("street"),
            col("p_dom_u").alias("house"),
            col("p_kv_u").alias("room"),
            col("doc_ser_pr"),
            col("doc_num_pr"),
            col("doc_date_pr"),
            col("s_polic_u").alias("polic_ser"),
            col("n_polic_o").alias("polic_num"),
            col("SNILS_doctor").alias("md_snils"),
        )

    def _add_ins_data_unique_relations(self, df, md_df):
        return (
            df.join(broadcast(md_df), on="md_snils", how="left")
            .withColumn(
                "relations",
                when(
                    col("md_name").isNotNull(),
                    concat(
                        col("relations"),
                        array_compact(
                            array(
                                relations_udf(
                                    concat_ws(
                                        " ",
                                        "md_name",
                                        "md_birth_date",
                                        "md_snils",
                                        lit("Врач"),
                                    )
                                )
                            )
                        ),
                    ),
                ).otherwise(col("relations")),
            )
            .drop("md", "md_name", "md_birth_date", "md_snils")
        )

    def _add_required_ins_data(self, df):
        return (
            df.replace("", None)
            .withColumn(
                "lastname",
                regexp_replace(
                    trim(lower(col("lastname"))),
                    f"^({self.replace_name_stops_pattern})$",
                    "",
                ),
            )
            .withColumn(
                "firstname",
                regexp_replace(
                    trim(lower(col("firstname"))),
                    f"^({self.replace_name_stops_pattern})$",
                    "",
                ),
            )
            .withColumn(
                "middlename",
                regexp_replace(
                    trim(lower(col("middlename"))),
                    f"^({self.replace_middlename_stops_pattern})$",
                    "",
                ),
            )
            .withColumn(
                "prev_lastname",
                regexp_replace(
                    trim(lower(col("prev_lastname"))),
                    f"^({self.replace_name_stops_pattern})$",
                    "",
                ),
            )
            .withColumn(
                "prev_firstname",
                regexp_replace(
                    trim(lower(col("prev_firstname"))),
                    f"^({self.replace_name_stops_pattern})$",
                    "",
                ),
            )
            .withColumn(
                "prev_middlename",
                regexp_replace(
                    trim(lower(col("prev_middlename"))),
                    f"^({self.replace_middlename_stops_pattern})$",
                    "",
                ),
            )
            .withColumn("name", name_parts_udf("firstname", "lastname", "middlename"))
            .withColumn(
                "names",
                array_compact(
                    array_distinct(
                        array(
                            name_parts_udf("firstname", "lastname", "middlename"),
                            when(
                                col("prev_lastname").isNotNull()
                                | col("prev_firstname").isNotNull()
                                | col("prev_middlename").isNotNull(),
                                name_parts_udf(
                                    when(
                                        col("prev_firstname").isNotNull(),
                                        col("prev_firstname"),
                                    ).otherwise(col("firstname")),
                                    when(
                                        col("prev_lastname").isNotNull(),
                                        col("prev_lastname"),
                                    ).otherwise(col("lastname")),
                                    when(
                                        col("prev_middlename").isNotNull(),
                                        col("prev_middlename"),
                                    ).otherwise(col("middlename")),
                                ),
                            ),
                        ),
                    )
                ),
            )
            .filter(size(col("names")) > 0)
            .withColumn(
                "sex",
                sex_udf(when(col("sex") == "2", lit("0")).otherwise(col("sex"))),
            )
            .withColumn("birth_date", birth_date_udf("birth", lit("%Y-%m-%d")))
            .withColumn("birth_place", address_udf(col("birth_place")))
            .withColumn(
                "actuality",
                when(
                    col("last_visit").isNotNull() & (col("last_visit") > 900_000_000),
                    actuality_date_udf(
                        from_unixtime(col("last_visit"), "yyyy-MM-dd HH:mm:ss"),
                        lit("%Y-%m-%d %H:%M:%S"),
                    ),
                ),
            )
            .withColumn("representative", name_udf(col("representative_name")))
            .withColumn(
                "representative_doc",
                when(
                    col("doc_num_pr").isNotNull(),
                    document_udf(
                        when(col("doc_ser_pr") == "82", lit("вид на жительство"))
                        .when(col("doc_ser_pr") == "ВУ", lit("удостоверение беженца"))
                        .otherwise(lit("паспорт гражданина рф")),
                        concat_ws("", "doc_ser_pr", "doc_num_pr"),
                        col("doc_date_pr"),
                        lit(None),
                        lit(None),
                        lit(None),
                        lit("%Y-%m-%d"),
                    ),
                ),
            )
            .withColumn(
                "relations",
                array_compact(
                    array(
                        when(
                            col("representative").isNotNull()
                            & col("representative_doc").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    col("representative"),
                                    col("representative_doc.serial"),
                                    lit("Представитель"),
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "representative_relations",
                array_compact(
                    array(
                        when(
                            col("representative").isNotNull()
                            & col("representative_doc").isNotNull()
                            & col("birth_date").isNotNull(),
                            relations_udf(
                                concat_ws(
                                    " ",
                                    col("name"),
                                    col("birth_date"),
                                    lit("Представляемый"),
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn("phones", phone_udf(col("phone")))
            .withColumn(
                "doc_type",
                when(col("doc_type_num") == "5", lit("паспорт гражданина рф"))
                .when(
                    (col("doc_type_num") == "3")
                    & (col("birth").startswith("20") | col("birth").startswith("199")),
                    lit("свидетельство о рождении"),
                )
                .when(
                    (col("doc_type_num") == "1")
                    & col("doc_issue_date").startswith("20"),
                    lit("свидетельство о рождении"),
                )
                .when(
                    col("doc_type_num") == "7",
                    lit("удостоверение личности военнослужащего"),
                )
                .when(
                    col("doc_type_num").isin(["8", "22"]),
                    lit("вид на жительство"),
                )
                .when(
                    col("doc_type_num") == "9",
                    when(
                        col("doc_serial_num").isin(["80", "82", "82 00"]),
                        lit("вид на жительство"),
                    ),
                )
                .when(
                    col("doc_type_num") == "10",
                    when(col("doc_serial_num") == "80", lit("вид на жительство"))
                    .when(
                        col("doc_serial_num").rlike("^[0-9]{4}$"),
                        lit("паспорт гражданина рф"),
                    )
                    .when(
                        col("doc_serial_num").startswith("I"),
                        lit("свидетельство о рождении"),
                    )
                    .when(
                        lower(col("doc_serial_num")).rlike("(ВУ|СБ|РФ|СС)")
                        & (length(col("doc_num")) > 5),
                        lit("удостоверение беженца"),
                    ),
                )
                .when(
                    col("doc_type_num") == "11",
                    when(
                        col("doc_serial_num").startswith("66"),
                        lit("паспорт гражданина рф"),
                    ).otherwise(lit("вид на жительство")),
                )
                .when(
                    col("doc_type_num") == "12",
                    when(col("doc_serial_num") == "82", lit("вид на жительство"))
                    .when(
                        col("doc_serial_num").startswith("66"),
                        lit("паспорт гражданина рф"),
                    )
                    .when(
                        lower(col("doc_serial_num")).rlike("(ВУ|СБ|РФ|СС)")
                        & (length(col("doc_num")) > 5),
                        lit("удостоверение беженца"),
                    ),
                )
                .when(
                    col("doc_type_num") == "13",
                    when(col("doc_serial_num") == "82", lit("вид на жительство"))
                    .when(
                        col("doc_serial_num").startswith("66"),
                        lit("паспорт гражданина рф"),
                    )
                    .when(
                        col("doc_serial_num").startswith("51")
                        | col("doc_serial_num").startswith("64"),
                        lit("заграничный паспорт гражданина рф"),
                    ),
                )
                .when(
                    col("doc_type_num") == "14",
                    when(
                        col("prev_doc_serial_num").isin(["80", "82"]),
                        lit("вид на жительство"),
                    ),
                )
                .when(
                    col("doc_type_num") == "15",
                    when(
                        col("doc_serial_num") == "82", lit("вид на жительство")
                    ).otherwise(lit("заграничный паспорт гражданина рф")),
                )
                .when(
                    col("doc_type_num") == "18",
                    when(col("doc_serial_num") == "82", lit("вид на жительство")),
                )
                .when(
                    col("doc_type_num") == "21",
                    when(
                        col("doc_serial_num").isin(["82", "820", "821", "8214", "900"]),
                        lit("вид на жительство"),
                    ).otherwise(lit("свидетельство о рождении")),
                )
                .when(col("doc_type_num") == "24", lit("свидетельство о рождении"))
                .when(
                    col("doc_type_num").isin(["23", "25", "28"]),
                    when(col("doc_serial_num") == "82", lit("вид на жительство")).when(
                        lower(col("doc_serial_num")).rlike("(ВУ|СБ|РФ|СС|Е|ВТ|БУ|BY)")
                        & (length(col("doc_num")) > 5),
                        lit("удостоверение беженца"),
                    ),
                ),
            )
            .withColumn(
                "prev_doc_type",
                when(col("prev_doc_type_num") == "3", lit("свидетельство о рождении"))
                .when(
                    (col("prev_doc_type_num") == "9")
                    & col("prev_doc_serial_num").isin(["80", "82"]),
                    lit("вид на жительство"),
                )
                .when(
                    (col("prev_doc_type_num") == "10")
                    & col("prev_doc_serial_num").isNotNull(),
                    lit("удостоверение беженца"),
                )
                .when(col("prev_doc_type_num") == "11", lit("вид на жительство"))
                .when(
                    col("prev_doc_type_num") == "12",
                    when(
                        col("prev_doc_serial_num") == "82",
                        lit("вид на жительство"),
                    ).otherwise(lit("удостоверение беженца")),
                )
                .when(
                    col("prev_doc_type_num") == "13",
                    when(
                        col("prev_doc_serial_num") == "80",
                        lit("вид на жительство"),
                    ),
                )
                .when(
                    col("prev_doc_type_num") == "14",
                    when(
                        col("prev_doc_serial_num") == "82",
                        lit("вид на жительство"),
                    ).otherwise("паспорт гражданина рф"),
                )
                .when(
                    (col("prev_doc_type_num") == "21")
                    & (col("prev_doc_serial_num") == "82"),
                    lit("вид на жительство"),
                )
                .when(
                    (col("prev_doc_type_num") == "22")
                    & (col("prev_doc_serial_num") == "90"),
                    lit("вид на жительство"),
                )
                .when(
                    col("prev_doc_type_num").isin(["23", "25", "28"])
                    & upper(col("prev_doc_serial_num")).rlike("(ВУ|СА|ЕК)"),
                    lit("удостоверение беженца"),
                ),
            )
            .withColumn(
                "doc_serial_num",
                when(
                    col("doc_type").isin(
                        ["вид на жительство", "заграничный паспорт гражданина рф"]
                    ),
                    regexp_replace("doc_serial_num", r" 00|N", ""),
                ).otherwise(col("doc_serial_num")),
            )
            .withColumn(
                "document_number", trim(concat_ws("", "doc_serial_num", "doc_num"))
            )
            .withColumn(
                "prev_doc_number",
                trim(concat_ws("", "prev_doc_serial_num", "prev_doc_num")),
            )
        )

    def _enrich_ins_data(self, df):
        return (
            df.withColumn(
                "document_number",
                when(
                    lower(col("document_number")).rlike(
                        self.replace_birth_cert_format_prefix_pattern
                    ),
                    lit(None),
                )
                .when(
                    lower(col("document_number")).rlike(
                        self.birth_cert_format_prefix_pattern
                    )
                    & ~(col("birth").startswith("20") | col("birth").startswith("199")),
                    lit(None),
                )
                .otherwise(col("document_number")),
            )
            .withColumn(
                "prev_doc_number",
                when(
                    lower(col("prev_doc_number")).rlike(
                        self.replace_birth_cert_format_prefix_pattern
                    ),
                    lit(None),
                )
                .when(
                    lower(col("prev_doc_number")).rlike(
                        self.birth_cert_format_prefix_pattern
                    )
                    & ~(col("birth").startswith("20") | col("birth").startswith("199")),
                    lit(None),
                )
                .otherwise(col("prev_doc_number")),
            )
            .withColumn(
                "polis_num", concat_ws("", upper(col("polic_ser")), col("polic_num"))
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("document_number").isNotNull(),
                                document_udf(
                                    col("doc_type"),
                                    col("document_number"),
                                    when(
                                        col("doc_issue_date") != lit("1970-01-01"),
                                        col("doc_issue_date"),
                                    ),
                                    lit(None),
                                    when(
                                        ~(
                                            lower(col("doc_authority")).isin(
                                                self.replace_doc_authorities
                                            )
                                        ),
                                        regexp_replace("doc_authority", "&quot;", '"'),
                                    ),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ),
                            when(
                                col("prev_doc_number").isNotNull(),
                                document_udf(
                                    col("prev_doc_type"),
                                    col("prev_doc_number"),
                                    when(
                                        col("prev_doc_issue_date") != lit("1970-01-01"),
                                        col("prev_doc_issue_date"),
                                    ),
                                    lit(None),
                                    when(
                                        ~(
                                            lower(col("prev_doc_authority")).isin(
                                                self.replace_doc_authorities
                                            )
                                        ),
                                        regexp_replace(
                                            "prev_doc_authority", "&quot;", '"'
                                        ),
                                    ),
                                    lit(None),
                                    lit("%Y-%m-%d"),
                                ),
                            ),
                            when(
                                col("snils").isNotNull(),
                                document_udf(lit("снилс"), col("snils")),
                            ),
                            document_udf(
                                lit("вид на жительство"),
                                concat_ws("", "i_doc_serial_num", "i_doc_num"),
                                lit(None),
                                lit(None),
                                col("i_doc_authority"),
                            ),
                            when(
                                col("current_enp").isNotNull()
                                & (length(col("current_enp")) > 8)
                                & (length(col("current_enp")) < 17),
                                document_udf(
                                    lit("номер страхового полиса"), col("current_enp")
                                ),
                            ),
                            when(
                                col("prev_enp").isNotNull()
                                & (length(col("current_enp")) > 8)
                                & (length(col("current_enp")) < 17),
                                document_udf(
                                    lit("номер страхового полиса"), col("prev_enp")
                                ),
                            ),
                            when(
                                col("polic_num").isNotNull()
                                & (length(col("polis_num")) > 8),
                                when(
                                    length(col("polic_num")) == 16,
                                    document_udf(
                                        lit("номер страхового полиса"),
                                        col("polic_num"),
                                    ),
                                ).when(
                                    length(col("polic_num")) < 17,
                                    document_udf(
                                        lit("номер страхового полиса"),
                                        col("polis_num"),
                                    ),
                                ),
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "registered_street",
                regexp_replace(
                    col("registered_street"), self.replace_trailing_dot_pattern, r"\1"
                ),
            )
            .withColumn(
                "street",
                regexp_replace(col("street"), self.replace_trailing_dot_pattern, r"\1"),
            )
            .withColumn(
                "registered_house",
                regexp_replace(
                    col("registered_house"), self.replace_trailing_dot_pattern, r"\1"
                ),
            )
            .withColumn(
                "registered_room",
                regexp_replace(
                    col("registered_room"), self.replace_trailing_dot_pattern, r"\1"
                ),
            )
            .withColumn(
                "house",
                regexp_replace(col("house"), self.replace_trailing_dot_pattern, r"\1"),
            )
            .withColumn(
                "room",
                regexp_replace(col("room"), self.replace_trailing_dot_pattern, r"\1"),
            )
            .withColumn(
                "registered_street",
                trim(
                    regexp_replace(
                        col("registered_street"), self.replace_street_stops_pattern, ""
                    )
                ),
            )
            .withColumn(
                "street",
                trim(
                    regexp_replace(col("street"), self.replace_street_stops_pattern, "")
                ),
            )
            .withColumn(
                "registered_house",
                trim(
                    regexp_replace(
                        col("registered_house"), self.replace_house_stops_pattern, ""
                    )
                ),
            )
            .withColumn(
                "house",
                trim(
                    regexp_replace(col("house"), self.replace_house_stops_pattern, "")
                ),
            )
            .withColumn(
                "registered_room",
                trim(
                    regexp_replace(
                        col("registered_room"), self.replace_room_stops_pattern, ""
                    )
                ),
            )
            .withColumn(
                "room",
                trim(regexp_replace(col("room"), self.replace_room_stops_pattern, "")),
            )
            .withColumn(
                "address",
                array_compact(
                    array_distinct(
                        array(
                            address_udf(
                                concat_ws(
                                    " ",
                                    when(
                                        length(trim(col("registered_index"))) == 6,
                                        col("registered_index"),
                                    ),
                                    when(
                                        length(trim(col("registered_area"))) > 2,
                                        trim(col("registered_area")),
                                    ),
                                    when(
                                        length(trim(col("registered_city"))) > 2,
                                        trim(col("registered_city")),
                                    ),
                                    when(
                                        length(col("registered_street")) > 2,
                                        col("registered_street"),
                                    ),
                                    when(
                                        col("registered_house").isNotNull()
                                        & (col("registered_house") != "")
                                        & (col("registered_house") != "-"),
                                        concat_ws(
                                            " ", lit("д"), col("registered_house")
                                        ),
                                    ),
                                    when(
                                        col("registered_room").isNotNull()
                                        & (col("registered_room") != "")
                                        & (col("registered_room") != "-"),
                                        concat_ws(
                                            " ", lit("кв"), col("registered_room")
                                        ),
                                    ),
                                )
                            ),
                            address_udf(
                                concat_ws(
                                    " ",
                                    when(length(trim(col("index"))) == 6, col("index")),
                                    when(
                                        length(trim(col("area"))) > 2, trim(col("area"))
                                    ),
                                    when(
                                        length(trim(col("city"))) > 2, trim(col("city"))
                                    ),
                                    when(length(col("street")) > 2, col("street")),
                                    when(
                                        col("house").isNotNull()
                                        & (col("house") != "")
                                        & (col("house") != "-"),
                                        concat_ws(" ", lit("д"), col("house")),
                                    ),
                                    when(
                                        col("room").isNotNull()
                                        & (col("room") != "")
                                        & (col("room") != "-"),
                                        concat_ws(" ", lit("кв"), col("room")),
                                    ),
                                )
                            ),
                        )
                    )
                ),
            )
            .withColumn(
                "raw_metadata",
                array_compact(
                    array(
                        when(
                            col("representative").isNotNull()
                            & col("representative_doc").isNull()
                            & col("phones").isNotNull(),
                            raw_metadata_udf(
                                lit("fio_pr_u"),
                                col("representative_name"),
                                lit("mob_phone"),
                                col("phone"),
                            ),
                        )
                        .when(
                            col("representative").isNotNull()
                            & col("representative_doc").isNull()
                            & col("phones").isNull(),
                            raw_metadata_udf(
                                lit("fio_pr_u"), col("representative_name")
                            ),
                        )
                        .when(
                            col("representative").isNull() & col("phones").isNotNull(),
                            raw_metadata_udf(lit("mob_phone"), col("phone")),
                        )
                    )
                ),
            )
            .withColumn("id", when(col("id") == "0", lit(None)).otherwise(col("id")))
            .select(
                "id",
                "names",
                "documents",
                "address",
                "relations",
                "sex",
                "birth_date",
                "birth_place",
                "actuality",
                "raw_metadata",
                "representative",
                "representative_doc",
                "representative_relations",
            )
        )

    def _group_ins_data(self, df):
        return (
            df.repartition(200)
            .groupBy(
                [
                    "id",
                    "names",
                    "documents",
                    "sex",
                    "birth_date",
                    "representative",
                    "representative_doc",
                    "representative_relations",
                ]
            )
            .agg(
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
                ),
                array_compact(array_distinct(flatten(collect_list("relations")))).alias(
                    "relations"
                ),
                array_compact(
                    array_distinct(flatten(collect_list("raw_metadata")))
                ).alias("raw_metadata"),
                first(col("birth_place"), ignorenulls=True).alias("birth_place"),
                max(col("actuality")).alias("actuality"),
            )
            .withColumn("phones", array())
        )

    def _extract_representatives(self, df):
        return (
            df.select(
                col("representative").alias("names"),
                col("representative_doc").alias("documents"),
                col("representative_relations").alias("relations"),
            )
            .filter(col("names").isNotNull() & col("documents").isNotNull())
            .withColumn("names", array(col("names")))
            .withColumn("documents", array(col("documents")))
            .withColumn("id", lit(None))
            .withColumn("sex", lit(None))
            .withColumn("birth_date", lit(None))
            .withColumn("birth_place", lit(None))
            .withColumn("actuality", lit(None))
            .withColumn("address", array())
            .withColumn("phones", array())
            .withColumn("raw_metadata", array())
        ).unionByName(
            df.drop("representative", "representative_doc", "representative_relations")
        )

    def parser(self):
        md_df = self._prepare_med()
        md_df.persist(StorageLevel.MEMORY_AND_DISK).count()

        idpr_df = self._add_required_ins_data(self._read_ins_data_policy_reception())
        idu_df = self._add_required_ins_data(self._read_ins_data_unique())
        idu_df = self._add_ins_data_unique_relations(idu_df, md_df)
        combined_id_df = idpr_df.unionByName(idu_df)
        enriched_id_df = self._enrich_ins_data(combined_id_df)
        grouped_ins_df = self._group_ins_data(enriched_id_df)
        grouped_ins_repr_df = self._extract_representatives(grouped_ins_df)
        grouped_ins_repr_df.persist(StorageLevel.DISK_ONLY)

        itp_df = self._prepare_ins_temp_polis()
        rpl_df, cached_df = self._prepare_ree_pac_list()
        side_df = itp_df.unionByName(rpl_df)
        side_df.persist(StorageLevel.DISK_ONLY)

        sdr_df = self._prepare_services_doubles_result()
        rprd_df = self._prepare_relax_persons_raw_data(md_df)
        med_df = self._prepare_mediko_economic_certificate(
            "mediko_economic_certificate.csv", self.med_schema
        )
        mect_df = self._prepare_mediko_economic_certificate(
            "mediko_economic_certificate_tabs.csv", self.med_tabs_schema
        )
        med_df = self._group_mediko_economic_certificate(
            med_df.unionByName(mect_df), md_df
        )

        combined_df = (
            sdr_df.unionByName(rprd_df)
            .unionByName(med_df)
            .withColumn("phones", array())
            .withColumn("raw_metadata", array())
            .withColumn("birth_place", lit(None))
            .withColumn("id", lit(None))
            .unionByName(grouped_ins_repr_df)
            .unionByName(side_df)
            .withColumn("join_id", monotonically_increasing_id())
            .withColumn("name", explode(col("names")))
            .withColumn(
                "name",
                concat_ws(
                    " ",
                    expr("""
                        transform(
                            split(name, '[ \\.]+'),
                            (x, i) -> case
                                when i = 0 then x
                                else substring(x, 1, 1)
                            end
                        )
                    """),
                ),
            )
            .withColumn("row_id", monotonically_increasing_id())
        )
        combined_df.persist(StorageLevel.DISK_ONLY).count()
        md_df.unpersist()
        grouped_ins_repr_df.unpersist()
        side_df.unpersist()
        cached_df.unpersist()

        joined_doc_df, cached_df = self._join_by_docs(combined_df.repartition(40))
        joined_doc_df.localCheckpoint(storageLevel=StorageLevel.DISK_ONLY)

        joined_id_df = self._join_by_id(joined_doc_df)

        df = (
            self._join_by_main_id(joined_id_df)
            .withColumn("documents", remove_doc_duplicates_udf(col("documents")))
            .withColumn(
                "raw_metadata",
                remove_raw_duplicates_udf(col("raw_metadata")),
            )
            .withColumn("names", when(size(col("names")) > 0, col("names")))
            .withColumn("documents", when(size(col("documents")) > 0, col("documents")))
            .withColumn("phones", when(size(col("phones")) > 0, col("phones")))
            .withColumn("address", when(size(col("address")) > 0, col("address")))
            .withColumn("relations", when(size(col("relations")) > 0, col("relations")))
            .withColumn(
                "raw_metadata", when(size(col("raw_metadata")) > 0, col("raw_metadata"))
            )
            .filter(
                col("names").isNotNull()
                & (col("documents").isNotNull() | col("phones").isNotNull())
            )
        )

        df.persist(StorageLevel.DISK_ONLY).count()
        combined_df.unpersist()
        cached_df.unpersist()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
