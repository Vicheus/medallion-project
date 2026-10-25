from pyspark import StorageLevel
from pyspark.sql.functions import (
    array,
    array_compact,
    array_distinct,
    col,
    collect_list,
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
    trim,
    udf,
    upper,
    when,
    xxhash64,
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
from parsetron.sections.main.udfs import (
    actuality_date_udf,
    address_udf,
    birth_date_udf,
    name_parts_udf,
    name_udf,
    raw_metadata_udf,
    sex_udf,
)
from parsetron.settings import DATASET_COUNTRY_CODE


def _remove_doc_duplicates(structs):
    if len(structs) == 0:
        return []

    seen_non_empty = set()
    seen_authorities = set()
    result = []

    for struct in structs:
        if struct["date_issue"] or struct["authority"]:
            result.append(struct)
            seen_non_empty.add((struct["type"], struct["serial"]))

    for struct in structs:
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


remove_doc_duplicates_udf = udf(
    _remove_doc_duplicates,
    ArrayType(document_schema, containsNull=False),
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0622"
    validate_invalid_groupping: bool = True
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.BY

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
    ins_schema = StructType(
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
    ins_unique_schema = StructType(
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
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
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
        df_keys.persist(StorageLevel.DISK_ONLY)

        mapping = df.select("row_id").withColumn("group_id", col("row_id"))
        mapping.persist(StorageLevel.MEMORY_AND_DISK)

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
                array_compact(array_distinct(flatten(collect_list("address")))).alias(
                    "address"
                ),
                array_compact(
                    array_distinct(flatten(collect_list("raw_metadata")))
                ).alias("raw_metadata"),
                first(col("sex"), ignorenulls=True).alias("sex"),
                first(col("birth_place"), ignorenulls=True).alias("birth_place"),
                max(col("actuality")).alias("actuality"),
                min(col("id")).alias("id"),
            )
            .unionByName(null_df)
            .drop("group_id", "name")
        )

        return result, prepared_df

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
                "doc_number", upper(trim(concat_ws("", col("doc_ser"), col("doc_num"))))
            )
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("doc_number").rlike("^(АВ|ВМ|НВ|КН|МР|МС|КВ|РР)"),
                            document_udf(
                                lit("паспорт гражданина рб"),
                                col("doc_number"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(self.dataset_country_code.value),
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
            .withColumn("sex", lit(None))
            .withColumn("actuality", lit(None))
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
                "doc_number", upper(trim(concat_ws("", col("doc_ser"), col("doc_num"))))
            )
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("doc_number").rlike("^(АВ|ВМ|НВ|КН|МР|МС|КВ|РР)"),
                            document_udf(
                                lit("паспорт гражданина рб"),
                                col("doc_number"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(self.dataset_country_code.value),
                            ),
                        )
                    )
                ),
            )
            .filter(size(col("documents")) > 0)
            .withColumn(
                "sex",
                sex_udf(when(col("sex") == "2", lit("0")).otherwise(col("sex"))),
            )
            .withColumn("birth_date", birth_date_udf("birthday", lit("%Y-%m-%d")))
            .select("names", "documents", "birth_date", "sex")
            .distinct()
            .withColumn("birth_place", lit(None))
            .withColumn("actuality", lit(None))
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
                col("fam_p_u").alias("lastname_pr"),
                col("im_p_u").alias("firstname_pr"),
                col("ot_p_u").alias("middlename_pr"),
                col("dr_p_u").alias("birthday_pr"),
                col("w_p_u").alias("sex_pr"),
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
            "doc_ser",
            "doc_num",
        ).unionByName(
            df.select(
                "lastname",
                "firstname",
                "middlename",
                "birthday",
                "sex",
                "doc_ser",
                "doc_num",
            ).filter(col("lastname").isNotNull())
        )
        df.persist(StorageLevel.MEMORY_AND_DISK).count()

        return self._process_ree_pack_list(df), df

    def _prepare_ins_data(self, path, schema):
        return (
            self.read(path=path, sep=",", schema=schema, header=True)
            .select(
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
                col("c_oksm_u").alias("country_code"),
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
                "doc_num",
                when(
                    upper(col("doc_serial_num")).startswith("N")
                    & (length(col("doc_num")) == 6),
                    concat_ws("", lit("0"), col("doc_num")),
                ).otherwise(col("doc_num")),
            )
            .withColumn(
                "doc_serial_num",
                when(
                    upper(trim(col("doc_serial_num"))).rlike(
                        "^(АВ|ВМ|НВ|КН|МР|МС|КВ|РР)"
                    )
                    & (col("country_code") == "UZB"),
                    lit(None),
                ).otherwise(col("doc_serial_num")),
            )
            .withColumn(
                "prev_doc_serial_num",
                when(
                    upper(trim(col("prev_doc_serial_num"))).rlike(
                        "^(АВ|ВМ|НВ|КН|МР|МС|КВ|РР)"
                    )
                    & (col("country_code") == "UZB"),
                    lit(None),
                ).otherwise(col("prev_doc_serial_num")),
            )
            .withColumn(
                "i_doc_serial_num",
                when(
                    upper(trim(col("i_doc_serial_num"))).rlike(
                        "^(АВ|ВМ|НВ|КН|МР|МС|КВ|РР)"
                    )
                    & (col("country_code") == "UZB"),
                    lit(None),
                ).otherwise(col("i_doc_serial_num")),
            )
            .withColumn(
                "doc_num",
                when(
                    (col("country_code") == "BLR") & (length(col("doc_num")) == 6),
                    concat_ws("", lit("0"), col("doc_num")),
                ).otherwise(col("doc_num")),
            )
            .withColumn(
                "doc_number",
                upper(trim(concat_ws("", col("doc_serial_num"), col("doc_num")))),
            )
            .withColumn(
                "prev_doc_number",
                upper(
                    trim(concat_ws("", col("prev_doc_serial_num"), col("prev_doc_num")))
                ),
            )
            .withColumn(
                "i_doc_number",
                upper(trim(concat_ws("", col("i_doc_serial_num"), col("i_doc_num")))),
            )
            .withColumn(
                "documents",
                array_compact(
                    array_distinct(
                        array(
                            when(
                                col("doc_number").rlike("^(АВ|ВМ|НВ|КН|МР|МС|КВ|РР)"),
                                document_udf(
                                    lit("паспорт гражданина рб"),
                                    col("doc_number"),
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
                                    lit(self.dataset_country_code.value),
                                ),
                            ),
                            when(
                                col("prev_doc_number").rlike(
                                    "^(АВ|ВМ|НВ|КН|МР|МС|КВ|РР)"
                                )
                                & (col("prev_doc_number") != col("doc_number"))
                                & (
                                    lower(col("prev_doc_authority"))
                                    != lower(col("doc_authority"))
                                ),
                                document_udf(
                                    lit("паспорт гражданина рб"),
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
                                    lit(self.dataset_country_code.value),
                                ),
                            ),
                            when(
                                col("i_doc_number").rlike("^(АВ|ВМ|НВ|КН|МР|МС|КВ|РР)")
                                & (col("i_doc_number") != col("doc_number"))
                                & (
                                    lower(col("i_doc_authority"))
                                    != lower(col("doc_authority"))
                                )
                                & (col("i_doc_number") != col("prev_doc_number"))
                                & (
                                    lower(col("i_doc_authority"))
                                    != lower(col("prev_doc_authority"))
                                ),
                                document_udf(
                                    lit("паспорт гражданина рб"),
                                    col("i_doc_number"),
                                    lit(None),
                                    lit(None),
                                    when(
                                        ~(
                                            lower(col("i_doc_authority")).isin(
                                                self.replace_doc_authorities
                                            )
                                        ),
                                        regexp_replace(
                                            "i_doc_authority", "&quot;", '"'
                                        ),
                                    ),
                                    lit(None),
                                    lit(None),
                                    lit(self.dataset_country_code.value),
                                ),
                            ),
                        )
                    )
                ),
            )
            .filter(size(col("documents")) > 0)
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
                            col("representative").isNotNull(),
                            raw_metadata_udf(
                                lit("fio_pr_u"), col("representative_name")
                            ),
                        )
                    )
                ),
            )
            .withColumn("id", when(col("id") == "0", lit(None)).otherwise(col("id")))
        )

    def _group_ins_data(self, df):
        return df.groupBy(["id", "names", "documents", "sex", "birth_date"]).agg(
            array_compact(array_distinct(flatten(collect_list("address")))).alias(
                "address"
            ),
            array_compact(array_distinct(flatten(collect_list("raw_metadata")))).alias(
                "raw_metadata"
            ),
            first(col("birth_place"), ignorenulls=True).alias("birth_place"),
            max(col("actuality")).alias("actuality"),
        )

    def parser(self):
        itp_df = self._prepare_ins_temp_polis()
        rpl_df, cached_df = self._prepare_ree_pac_list()

        idpr_df = self._prepare_ins_data(
            "ins_data_policy_reception.csv", self.ins_schema
        )
        idu_df = self._prepare_ins_data("ins_data_unique.csv", self.ins_unique_schema)
        combined_id_df = self._group_ins_data(idpr_df.unionByName(idu_df))

        combined_df = (
            itp_df.unionByName(rpl_df)
            .withColumn("id", lit(None))
            .unionByName(combined_id_df)
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
        combined_df.persist(StorageLevel.MEMORY_AND_DISK).count()
        cached_df.unpersist()

        joined_doc_df, cached_df = self._join_by_docs(combined_df)

        df = (
            self._join_by_main_id(joined_doc_df)
            .withColumn("documents", remove_doc_duplicates_udf(col("documents")))
            .withColumn("names", when(size(col("names")) > 0, col("names")))
            .withColumn("documents", when(size(col("documents")) > 0, col("documents")))
            .withColumn("address", when(size(col("address")) > 0, col("address")))
            .withColumn(
                "raw_metadata", when(size(col("raw_metadata")) > 0, col("raw_metadata"))
            )
            .filter(col("names").isNotNull() & col("documents").isNotNull())
        )

        df.persist(StorageLevel.MEMORY_AND_DISK).count()
        combined_df.unpersist()
        cached_df.unpersist()

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
