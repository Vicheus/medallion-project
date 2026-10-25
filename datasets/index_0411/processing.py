from pyspark.sql.functions import when, col, array, regexp_replace
from parsetron import Parsetron
from parsetron.sections.main.udfs import name_udf, email_udf, phone_udf


class ProjectParsetron(Parsetron):
    test_mode: bool = False
    dataset_code_name: str = "index_0411"
    calc_completeness: bool = False

    def parser(self):
        df = (
            self.read(
                path="/media/user/SAMSUNG/Databases/index_0411/raw/contacts_preprep_tetrika_school_7m_ru_new_full.csv",
                sep=",",
            )
            .filter(
                ~col("Name").contains("контакт по звонку")
                & ~col("Name").contains("Нет имени")
            )
            .withColumn("Name", regexp_replace(col("Name"), r"[РУ]\s", ""))
            .withColumn("names", name_udf(col("Name")))
            .withColumn("phones", phone_udf(col("Phone")))
            .withColumn("emails", email_udf(col("Email")))
            .select("names", "emails", "phones")
        )

        df = df.drop_duplicates(["names", "emails", "phones"])

        df = df.repartition(self.output_file_count)

        df = (
            df.withColumn(
                "names",
                when(col("names").isNotNull(), array(col("names"))).otherwise(None),
            )
            .withColumn(
                "phones",
                when(col("phones").isNotNull(), array(col("phones"))).otherwise(None),
            )
            .withColumn(
                "emails",
                when(col("emails").isNotNull(), array(col("emails"))).otherwise(None),
            )
        )

        df = df.filter(
            col("names").isNotNull()
            & (col("phones").isNotNull() | col("emails").isNotNull())
        )

        df.show(n=100, truncate=False)

        return df


if __name__ == "__main__":
    parsetron = ProjectParsetron()
    parsetron.run()
