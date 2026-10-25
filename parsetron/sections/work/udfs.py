from pyspark.sql.functions import udf

from .validators.work import work, work_with_docs
from .validators.work_date import work_date
from .validators.work_post import work_post
from .validators.work_company import work_company
from .schemas import (
    work_company_schema,
    work_post_schema,
    work_date_schema,
    work_schema,
    work_with_docs_schema,
)

work_date_udf = udf(work_date, work_date_schema)
work_post_udf = udf(work_post, work_post_schema)
work_company_udf = udf(work_company, work_company_schema)
work_udf = udf(work, work_schema)
work_with_docs_udf = udf(work_with_docs, work_with_docs_schema)
