from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pyspark.sql.functions import udf
from pyspark.sql.functions import ArrayType, StringType


def cosine_similarity_strings(str1, str2):
    try:
        vectors = TfidfVectorizer().fit_transform([str1, str2])
        return cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    except ValueError:
        return 0


def get_distinct_elements_based_on_cosine_similarity(arr):
    distinct_elements = []
    if not arr:
        return distinct_elements

    for i, item in enumerate(arr):
        is_distinct = True
        for distinct_item in distinct_elements:
            if cosine_similarity_strings(item, distinct_item) >= 1:
                is_distinct = False
                break
        if is_distinct:
            distinct_elements.append(item)

    return distinct_elements


array_distinct_cosine_similarity_udf = udf(
    get_distinct_elements_based_on_cosine_similarity, ArrayType(StringType())
)
