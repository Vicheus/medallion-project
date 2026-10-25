from pyspark.sql.functions import (
    from_json,
    when,
    col,
    lit,
    array,
    explode_outer,
    array_distinct,
    size,
    concat_ws,
    array_compact,
    max,
    regexp_replace,
    flatten,
    collect_set,
    first,
)
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    LongType,
    ArrayType,
    BooleanType,
    IntegerType,
    DoubleType,
)

from parsetron import Parsetron
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.movements.udfs import (
    movement_udf,
    ticket_order_datetime_udf,
    movement_date_udf,
)
from parsetron.sections.main.udfs import (
    name_udf,
    birth_date_udf,
    sex_udf,
    actuality_date_udf,
    raw_metadata_udf,
)


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0092"

    def parser(self):
        schema = StructType(
            [
                StructField("result", StringType(), True),
                StructField("saleOrderId", LongType(), True),
                StructField(
                    "orders",
                    ArrayType(
                        StructType(
                            [
                                StructField("orderId", LongType(), True),
                                StructField("created", StringType(), True),
                                StructField("dirName", StringType(), True),
                                StructField("code0", LongType(), True),
                                StructField("station0", StringType(), True),
                                StructField("code1", LongType(), True),
                                StructField("station1", StringType(), True),
                                StructField("timeInfo", StringType(), True),
                                StructField("cost", DoubleType(), True),
                                StructField("date0", StringType(), True),
                                StructField("time0", StringType(), True),
                                StructField("route0", StringType(), True),
                                StructField("route1", StringType(), True),
                                StructField("number", StringType(), True),
                                StructField("number2", StringType(), True),
                                StructField("terminal", StringType(), True),
                                StructField("gate", StringType(), True),
                                StructField("date1", StringType(), True),
                                StructField("time1", StringType(), True),
                                StructField("cnumber", StringType(), True),
                                StructField("addSigns", StringType(), True),
                                StructField("clsType", StringType(), True),
                                StructField("type", StringType(), True),
                                StructField("ctype", IntegerType(), True),
                                StructField("carrier", StringType(), True),
                                StructField("carrier_full", StringType(), True),
                                StructField("carrier_inn", StringType(), True),
                                StructField("blank_info", StringType(), True),
                                StructField("agent", StringType(), True),
                                StructField("seatNums", StringType(), True),
                                StructField(
                                    "tickets",
                                    ArrayType(
                                        StructType(
                                            [
                                                StructField(
                                                    "ticketId", LongType(), True
                                                ),
                                                StructField(
                                                    "seats", StringType(), True
                                                ),
                                                StructField(
                                                    "cost", IntegerType(), True
                                                ),
                                                StructField(
                                                    "tariff", StringType(), True
                                                ),
                                                StructField(
                                                    "tariffName", StringType(), True
                                                ),
                                                StructField(
                                                    "seatsType", StringType(), True
                                                ),
                                                StructField(
                                                    "Teema", BooleanType(), True
                                                ),
                                                StructField(
                                                    "pass",
                                                    ArrayType(
                                                        StructType(
                                                            [
                                                                StructField(
                                                                    "lastName",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "firstName",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "midName",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "docType",
                                                                    IntegerType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "docTypeName",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "docNumber",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "birthDate",
                                                                    StringType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "genderId",
                                                                    IntegerType(),
                                                                    True,
                                                                ),
                                                                StructField(
                                                                    "insurance",
                                                                    IntegerType(),
                                                                    True,
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    True,
                                                ),
                                            ]
                                        )
                                    ),
                                    True,
                                ),
                            ]
                        )
                    ),
                    True,
                ),
                StructField("totalSum", DoubleType(), True),
            ]
        )
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0092/raw/rzd_orders_preprocessed.csv",
                sep="~~",
                header=True,
            )
            .withColumn("response", regexp_replace("response", r'""', '"'))
            .withColumn("response", from_json(col("response"), schema=schema))
            .withColumn("orders", col("response.orders"))
        )
        df = (
            df.withColumn("order", explode_outer(col("orders")))
            .withColumn("ticket", explode_outer(col("order.tickets")))
            .withColumn("pass", explode_outer(col("ticket.pass")))
            .select(
                col("id"),
                col("sale_order_id").alias("sale_order_id"),
                col("order.orderId").alias("order_id"),
                col("order.number").alias("order_num"),
                col("order.agent").alias("agent"),
                col("order.created").alias("order_date"),
                col("order.cost").alias("cost"),
                col("order.dirName").alias("direction"),
                col("order.code0"),
                col("order.code1"),
                col("order.station0"),
                col("order.station1"),
                col("order.date0").alias("date0"),
                col("order.date1").alias("date1"),
                col("order.time0").alias("time0"),
                col("order.time1").alias("time1"),
                col("order.timeInfo").alias("timeInfo"),
                col("order.route0").alias("route0"),
                col("order.route1").alias("route1"),
                col("order.number").alias("train_number"),
                col("order.number2").alias("train_number2"),
                col("order.terminal").alias("terminal"),
                col("order.gate").alias("gate"),
                col("order.cnumber").alias("car_number"),
                col("order.type").alias("car_type"),
                col("order.clsType").alias("car_class"),
                col("order.addSigns").alias("add_signs"),
                col("order.seatNums").alias("seat_nums"),
                col("order.carrier").alias("carrier"),
                col("order.carrier_full").alias("carrier_full"),
                col("order.carrier_inn").alias("carrier_inn"),
                col("order.blank_info").alias("blank_info"),
                col("ticket.ticketId").alias("ticketId"),
                col("ticket.seats").alias("seats"),
                col("ticket.cost").alias("ticketCost"),
                col("ticket.tariff").alias("tariff"),
                col("pass.lastName").alias("last_name"),
                col("pass.firstName").alias("first_name"),
                col("pass.midName").alias("mid_name"),
                concat_ws(
                    " ",
                    col("pass.lastName"),
                    col("pass.firstName"),
                    col("pass.midName"),
                ).alias("names"),
                col("pass.docType").alias("doc_type"),
                col("pass.docTypeName").alias("doc_type_name"),
                col("pass.docNumber").alias("doc_number"),
                col("pass.birthDate").alias("birth_date"),
                col("pass.genderId").alias("gender_id"),
                col("pass.insurance"),
            )
            .withColumn("names", name_udf(col("names")))
            .withColumn(
                "birth_date", birth_date_udf(col("birth_date"), lit("%d.%m.%Y"))
            )
            .withColumn("sex", sex_udf(col("gender_id")))
            .withColumn(
                "documents",
                when(
                    col("doc_number").isNotNull(),
                    array_distinct(
                        array_compact(
                            array(
                                when(
                                    col("doc_number").isNotNull(),
                                    document_udf(
                                        lit(None),
                                        col("doc_number"),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit(None),
                                        lit("yyyy-MM-dd"),
                                    ),
                                ).otherwise(None)
                            )
                        )
                    ),
                ).otherwise(None),
            )
            .withColumn(
                "movements",
                array_distinct(
                    array_compact(
                        array(
                            movement_udf(
                                movement_date_udf(col("date0"), lit("%d.%m.%Y")),
                                lit(None),
                                lit(None),
                                col("station0"),
                                movement_date_udf(col("date1"), lit("%d.%m.%Y")),
                                lit(None),
                                lit(None),
                                col("station1"),
                                lit(None),
                                ticket_order_datetime_udf(
                                    col("order_date"), lit("%d.%m.%Y")
                                ),
                                lit(None),
                                col("ticketId"),
                                col("train_number"),
                                lit(None),
                                lit(4),
                                lit(None),
                                col("agent"),
                                lit(None),
                                lit(None),
                            )
                        )
                    )
                ),
            )
            .withColumn(
                "actuality", actuality_date_udf(col("order_date"), lit("%d.%m.%Y"))
            )
            .withColumn(
                "raw_metadata",
                raw_metadata_udf(
                    lit("carrier"),
                    col("carrier"),
                    lit("carrier_full"),
                    col("carrier_full"),
                    lit("carrier_inn"),
                    col("carrier_inn"),
                    lit("blank_info"),
                    col("blank_info"),
                    lit("terminal"),
                    col("terminal"),
                    lit("gate"),
                    col("gate"),
                    lit("car_number"),
                    col("car_number"),
                ),
            )
        )
        # all records should be with document based on data checks
        df = (
            df.filter(
                col("documents").isNotNull() & (col("documents")[0]["serial"] != "")
            )
            .groupby(col("documents")[0]["serial"])
            .agg(
                collect_set("names").alias("names"),
                flatten(collect_set("documents")).alias("documents"),
                flatten(collect_set("movements")).alias("movements"),
                first("sex").alias("sex"),
                first("birth_date").alias("birth_date"),
                max("actuality").alias("actuality"),
                collect_set("raw_metadata").alias("raw_metadata"),
            )
        )

        df = (
            df.withColumn(
                "names",
                when(
                    size(array_compact(col("names"))) > 0, array_compact(col("names"))
                ).otherwise(None),
            )
            .withColumn(
                "documents",
                when(
                    size(array_compact(col("documents"))) > 0,
                    array_compact(col("documents")),
                ).otherwise(None),
            )
            .withColumn(
                "movements",
                when(
                    size(array_compact(col("movements"))) > 0,
                    array_compact(col("movements")),
                ).otherwise(None),
            )
            .withColumn(
                "raw_metadata",
                when(
                    size(array_compact(col("raw_metadata"))) > 0,
                    array_compact(col("raw_metadata")),
                ).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("documents").isNotNull() | col("movements").isNotNull())
        )

        df = df.select(
            "names", "documents", "movements", "sex", "birth_date", "actuality"
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
