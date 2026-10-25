from pyspark import StorageLevel
from pyspark.sql.functions import when, col, lit, collect_list, array, array_distinct, array_compact, size, flatten

from parsetron import Parsetron
from parsetron.settings import DATASET_COUNTRY_CODE
from parsetron.sections.main.udfs import name_udf, phone_udf, email_udf, address_udf
from parsetron.sections.document.udfs import document_udf

class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = 'index_0558'
    dataset_country_code: DATASET_COUNTRY_CODE = DATASET_COUNTRY_CODE.KZ
    validate_invalid_groupping: bool = True

    def parser(self):
        df = self.read(path='/media/user/SAMSUNG BACKUP/indexes/index_0558/raw/еsроrt.gоv.kz - @StormBaseAdapter.csv', sep=',', header=True)\
        .withColumn('names', name_udf(col('full_name')))\
        .withColumn('phones', phone_udf(col('phone'), lit(self.dataset_country_code)))\
        .withColumn('emails', email_udf(col('email')))\
        .withColumn('address', address_udf(col('region_name_ru')))\
        .withColumn(
            "documents",
            array_compact(
                array_distinct(
                    array(
                        when(
                            col("iin").isNotNull(),
                            document_udf(
                                lit("инн"),
                                col("iin"),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit(None),
                                lit("%Y-%m-%d %H:%M:%S"),
                                lit(self.dataset_country_code))
                        ).otherwise(None)
                    )
                )
            )
        )\
        .select('names', 'phones', 'emails', 'address', 'documents')

        df_without_doc = (
            df.filter((size(col("documents")) == 0) | (col("documents")[0]["serial"].isNull()))
            .withColumn("names", array_compact(array_distinct(array(col("names")))))
            .withColumn("phones", array_compact(array_distinct(array(col("phones")))))
            .withColumn("emails", array_compact(array_distinct(array(col("emails")))))
            .withColumn("address", array_compact(array_distinct(array(col("address")))))
            .select('names', 'phones', 'emails', 'address', 'documents')
        )

        df_without_doc.show(n=1000, truncate=False)

        df_with_doc = (
            df.filter((size(col("documents")) > 0) & (col("documents")[0]["serial"].isNotNull()))
            .groupby(col("documents")[0]["serial"])
            .agg(
                array_compact(array_distinct(collect_list("names"))).alias("names"),
                array_compact(array_distinct(collect_list("phones"))).alias("phones"),
                array_compact(array_distinct(collect_list("emails"))).alias("emails"),
                array_compact(array_distinct(collect_list("address"))).alias("address"),
                array_compact(array_distinct(flatten(collect_list("documents")))).alias("documents")
            )
            .select('names', 'phones', 'emails', 'address', 'documents')
        )

        df = df_with_doc.unionAll(df_without_doc)

        df.persist(StorageLevel.DISK_ONLY).count()
        df = df\
            .withColumn('names', when(size(col('names')) > 0, col('names')).otherwise(None))\
            .withColumn('phones', when(size(col('phones')) > 0, col('phones')).otherwise(None))\
            .withColumn('emails', when(size(col('emails')) > 0, col('emails')).otherwise(None))\
            .withColumn('address', when(size(col('address')) > 0, col('address')).otherwise(None))\
            .withColumn('documents', when(size(col('documents')) > 0, col('documents')).otherwise(None))\
        
        df = df.filter(col('names').isNotNull() & (col('phones').isNotNull() | col('emails').isNotNull() | col('documents').isNotNull()))
        
        df.show(n=20, truncate=False)

        return df


if __name__ == '__main__':
    parsetron = ProjectParsetron()
    parsetron.run()
