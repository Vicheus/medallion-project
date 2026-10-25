from pyspark.sql.functions import udf

from .utils.financials_utils import (
    brute_force_card,
    extract_invoice_number_for_physical_person,
)
from .validators.financial_card_number import (
    financial_card_number,
    financial_cards_numbers,
)
from .validators.financial_date_expire import financial_date_expire
from .validators.financial_date_issue import financial_date_issue
from .validators.financial_invoice_number import financial_invoice_number
from .validators.yandex_money_number import yandex_money_number
from .validators.financials import financial

from .schemas import (
    card_schema,
    cards_schema,
    date_expire_schema,
    date_issue_schema,
    brute_force_card_schema,
    yandex_money_number_schema,
    invoice_number_schema,
    financials_schema,
)


brute_force_card_udf = udf(brute_force_card, brute_force_card_schema)
financial_card_number_udf = udf(financial_card_number, card_schema)
financial_cards_numbers_udf = udf(financial_cards_numbers, cards_schema)
financial_date_expire_udf = udf(financial_date_expire, date_expire_schema)
financial_date_issue_udf = udf(financial_date_issue, date_issue_schema)
financial_invoice_number_udf = udf(financial_invoice_number, invoice_number_schema)

extract_invoice_number_for_physical_person_udf = udf(
    extract_invoice_number_for_physical_person, invoice_number_schema
)
yandex_money_number_udf = udf(yandex_money_number, yandex_money_number_schema)
financial_udf = udf(financial, financials_schema)
