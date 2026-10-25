from transliterate import translit
from pyspark.sql.functions import udf
from pyspark.sql.functions import StringType


def transliterate(value, language_code="ru", reversed=False, strict=False):
    if not value:
        return
    transliterated = translit(value, language_code, reversed, strict)
    return transliterated


transliterate_udf = udf(transliterate, StringType())
