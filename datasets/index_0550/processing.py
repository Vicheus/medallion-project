from pyspark.sql.functions import (
    when,
    col,
    array,
    expr,
    explode,
    lit,
    struct,
    max,
    array_distinct,
    array_compact,
    flatten,
    collect_set,
    size,
)
from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.main.udfs import (
    name_udf,
    name_parts_udf,
    phone_udf,
    email_udf,
    address_from_parts_udf,
    actuality_date_udf,
    raw_metadata_udf,
)
from pyspark import StorageLevel


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0550"
    calc_completeness: bool = False
    output_file_count: int = 50

    def parser(self):
        df = self.read(
            path="/media/user/T7 Shield/4_megamarket.ru_1m_12.08.2024-30.07.2024.json",
            header=False,
            sep="\n",
        )

        product_meta = []

        max_len_products = df.select(max(size("products"))).collect()[0][0]
        if max_len_products > 10:
            max_len_products = 10

        for i in range(max_len_products):
            idx = i + 1
            name_col = f"product_{idx}_name"
            inn_col = f"product_{idx}_supplier_INN"
            supplier_col = f"product_{idx}_supplier_name"

            df = df.withColumn(name_col, expr(f"try_element_at(products, {idx}).name"))
            df = df.withColumn(
                inn_col, expr(f"try_element_at(products, {idx}).supplier_INN")
            )
            df = df.withColumn(
                supplier_col, expr(f"try_element_at(products, {idx}).supplier_name")
            )

            product_meta.extend(
                [
                    (lit(name_col), col(name_col)),
                    (lit(inn_col), col(inn_col)),
                    (lit(supplier_col), col(supplier_col)),
                ]
            )

        df = (
            df.withColumn("delivered_at", col("delivered_at"))
            .withColumn(
                "departure_shipping_method_name",
                col("departure")["shipping_method"]["name"],
            )
            .withColumn(
                "departure_shipping_method_comment",
                col("departure")["shipping_method"]["comment"],
            )
            .withColumn("departure_address_email", col("departure")["address"]["email"])
            .withColumn("departure_address_phone", col("departure")["address"]["phone"])
            .withColumn(
                "departure_address_country_code",
                col("departure")["address"]["country_code"],
            )
            .withColumn(
                "departure_address_administrative_area",
                col("departure")["address"]["administrative_area"],
            )
            .withColumn(
                "departure_address_settlement",
                col("departure")["address"]["settlement"],
            )
            .withColumn(
                "departure_address_address_line_1",
                col("departure")["address"]["address_line_1"],
            )
            .withColumn("departure_address_name", col("departure")["address"]["name"])
            .withColumn(
                "departure_address_surname", col("departure")["address"]["surname"]
            )
            .withColumn(
                "departure_address_patronymic",
                col("departure")["address"]["patronymic"],
            )
            .withColumn(
                "departure_address_postal_code",
                col("departure")["address"]["postal_code"],
            )
            .withColumn(
                "departure_address_street", col("departure")["address"]["street"]
            )
            .withColumn("departure_address_house", col("departure")["address"]["house"])
            .withColumn(
                "departure_address_apartment", col("departure")["address"]["apartment"]
            )
            .withColumn("departure_address_floor", col("departure")["address"]["floor"])
            .withColumn(
                "departure_address_company_name",
                col("departure")["address"]["company_name"],
            )
            .withColumn(
                "departure_address_company_inn",
                col("departure")["address"]["company_inn"],
            )
            .withColumn("departure_comment", col("departure")["comment"])
            .withColumn(
                "actuality",
                actuality_date_udf(col("created_at"), lit("%Y-%m-%d %H:%M:%S")),
            )
        )
        df = df.drop(
            "additional_service",
            "archived_at",
            "checkpoints",
            "cod",
            "cod_received_legal_type",
            "cost",
            "cost_readable",
            "created_at",
            "current_status",
            "customer_number",
            "declared_cost",
            "delayed_delivery_at",
            "delivered_at       ",
            "delivery_time",
            "departure",
            "external_id",
            "external_tracking_number",
            "height",
            "history",
            "id",
            "is_unlimited_storage",
            "label_url",
            "length",
            "method",
            "no_gather",
            "orders",
            "package_sending",
            "paid",
            "photo",
            "pick_up",
            "postamat_load_code",
            "postamat_load_code_valid_till",
            "previous_id",
            "problems",
            "products",
            "qr_payment_url_sberbank_delivery",
            "return",
            "sberbank_payment_qr_url",
            "seller_name",
            "sent_at",
            "services",
            "shipment",
            "small_label_url",
            "status",
            "stock",
            "storage",
            "tracking_number",
            "type",
            "weight",
            "width",
        )

        base_meta = [
            (lit("delivered_at"), col("delivered_at")),
            (
                lit("departure_shipping_method_name"),
                col("departure_shipping_method_name"),
            ),
            (
                lit("departure_shipping_method_comment"),
                col("departure_shipping_method_comment"),
            ),
            (lit("departure_comment"), col("departure_comment")),
        ]

        all_metadata = base_meta + product_meta
        metadata_args = []
        for k, v in all_metadata:
            metadata_args.append(k)
            metadata_args.append(v)

        df_persons = (
            df.withColumn(
                "names",
                name_parts_udf(
                    col("departure_address_name"),
                    col("departure_address_surname"),
                    col("departure_address_patronymic"),
                ),
            )
            .withColumn("phones", phone_udf(col("departure_address_phone")))
            .withColumn("emails", email_udf(col("departure_address_email")))
            .withColumn(
                "addresses",
                address_from_parts_udf(
                    lit(2),
                    col("departure_address_postal_code"),
                    col("departure_address_country_code"),
                    col("departure_address_administrative_area"),
                    col("departure_address_settlement"),
                    col("departure_address_street"),
                    col("departure_address_house"),
                    col("departure_address_floor"),
                    col("departure_address_apartment"),
                    lit(None),
                    lit(None),
                ),
            )
            .withColumn("address", col("addresses")["address"])
            .withColumn("documents", array())
            .withColumn("raw_metadata", raw_metadata_udf(*metadata_args))
            .withColumn("actuality", col("actuality"))
            .select(
                "names",
                "phones",
                "emails",
                "addresses",
                "address",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        product_structs = []

        for i in range(1, max_len_products + 1):
            name_col = f"product_{i}_supplier_name"
            inn_col = f"product_{i}_supplier_INN"

            product_structs.append(
                struct(
                    col(name_col).alias("supplier_name"),
                    col(inn_col).alias("supplier_INN"),
                )
            )

        df_persons = (
            df_persons.groupBy(["names", "phones"])
            .agg(
                array_distinct(array_compact(collect_set(col("emails")))).alias(
                    "emails"
                ),
                array_distinct(array_compact(collect_set(col("addresses")))).alias(
                    "addresses"
                ),
                array_distinct(array_compact(collect_set(col("address")))).alias(
                    "address"
                ),
                array_distinct(array_compact(collect_set(col("raw_metadata")))).alias(
                    "raw_metadata"
                ),
                array_distinct(
                    array_compact(flatten(collect_set(col("documents"))))
                ).alias("documents"),
                max(col("actuality")).alias("actuality"),
            )
            .select(
                "names",
                "phones",
                "emails",
                "addresses",
                "address",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df_products_exploded = df.select(
            explode(array(*product_structs)).alias("supplier"), col("actuality")
        )

        df_suppliers = (
            df_products_exploded.select(
                "supplier.supplier_name",
                "supplier.supplier_INN",
                "actuality",
            )
            .filter(col("supplier_name").isNotNull())
            .drop_duplicates(["supplier_INN"])
        )

        df_suppliers = (
            df_suppliers.withColumn("names", name_udf(col("supplier_name")))
            .withColumn("phones", lit(None))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("supplier_INN").isNotNull(),
                            document_udf(
                                lit("инн"),
                                col("supplier_INN"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn("emails", array())
            .withColumn("address", array())
            .withColumn("addresses", array())
            .withColumn("raw_metadata", array())
            .select(
                "names",
                "phones",
                "emails",
                "addresses",
                "address",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )

        df_suppliers.show(n=20, truncate=False)

        df_companies = (
            df.filter(
                col("departure_address_company_name").isNotNull()
                & col("departure_address_company_inn").isNotNull()
            )
            .withColumn("names", name_udf(col("departure_address_company_name")))
            .withColumn(
                "documents",
                array_compact(
                    array(
                        when(
                            col("departure_address_company_inn").isNotNull(),
                            document_udf(
                                lit("инн"),
                                col("departure_address_company_inn"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("yyyy-MM-dd"),
                            ),
                        ).otherwise(None)
                    )
                ),
            )
            .withColumn("phones", lit(None))
            .withColumn("emails", array())
            .withColumn("address", array())
            .withColumn("addresses", array())
            .withColumn("raw_metadata", lit(None))
            .distinct()
            .select(
                "names",
                "phones",
                "emails",
                "addresses",
                "address",
                "documents",
                "raw_metadata",
                "actuality",
            )
        )
        df_companies.show(n=20, truncate=False)

        df = df_persons.unionAll(df_companies).unionAll(df_suppliers)

        df = (
            df.withColumn(
                "names",
                when(
                    col("names").isNotNull(),
                    array_compact(array_distinct(array(col("names")))),
                ).otherwise(None),
            )
            .withColumn(
                "phones",
                when(
                    col("phones").isNotNull(),
                    array_compact(array_distinct(array(col("phones")))),
                ).otherwise(None),
            )
            .withColumn(
                "emails", when(size(col("emails")) > 0, col("emails")).otherwise(None)
            )
            .withColumn(
                "address",
                when(size(col("address")) > 0, col("address")).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(size(col("raw_metadata")) > 0, col("raw_metadata")).otherwise(
                    None
                ),
            )
            .withColumn(
                "documents",
                when(size(col("documents")) > 0, col("documents")).otherwise(None),
            )
            .withColumn("raw_metadata", expr("slice(raw_metadata, 1, 15)"))
        )

        df = df.repartition(self.output_file_count)
        df.persist(StorageLevel.DISK_ONLY).count()

        df = df.filter(
            col("names").isNotNull()
            & (
                col("phones").isNotNull()
                | col("emails").isNotNull()
                | col("documents").isNotNull()
                | col("address").isNotNull()
            )
        )
        df = df.select(
            "names",
            "phones",
            "emails",
            "addresses",
            "address",
            "documents",
            "raw_metadata",
            "actuality",
        )
        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
