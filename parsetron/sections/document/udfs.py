from pyspark.sql.functions import udf
from pyspark.sql.functions import pandas_udf

from .validators.document import (
    document,
    get_document_features_batch,
    get_document_features,
)
from .schemas import (
    document_schema,
    identify_documents_features_schema,
    identify_document_features_schema,
)

document_udf = udf(document, document_schema)
identify_documents_features_batch_udf = pandas_udf(
    get_document_features_batch, identify_documents_features_schema
)
identify_document_features_udf = udf(
    get_document_features, identify_document_features_schema
)
