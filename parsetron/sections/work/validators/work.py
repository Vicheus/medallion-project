import re
from typing import Optional, Dict, Union

from .work_company import work_company
from .work_post import work_post
from ...base.validators.base import is_ukrainian_symbols
from ...document.validators.serial.document_serial_ru import (
    document_serial_inn,
    document_serial_ogrn,
)
from ...main.validators.address import address


def work(
    post: str = None,
    date_start: str = None,
    date_end: str = None,
    company: str = None,
    company_address: str = None,
    comment: str = None,
) -> Optional[Dict[str, Union[int, str]]]:

    if company:
        company = work_company(company)
    if post:
        post = work_post(post)
    if company_address:
        company_address = address(company_address)

    if (not company) & (not post):
        return

    return {
        "post": post,
        "date_start": date_start,
        "date_end": date_end,
        "company": company,
        "address": company_address,
        "comment": comment,
    }


def work_with_docs(
    post: str = None,
    date_start: str = None,
    date_end: str = None,
    company: str = None,
    ru_inn: str = None,
    ru_ogrn: str = None,
    company_address: str = None,
    comment: str = None,
) -> Optional[Dict[str, Union[int, str]]]:

    if company:
        company = work_company(company)
    if post:
        post = work_post(post)

    if (not company) & (not post):
        return

    if company_address:
        company_address = address(company_address)
    inn = document_serial_inn(ru_inn)
    if not inn and ru_inn and re.search(r"\d{10}", ru_inn):
        inn = ru_inn
    ogrn = document_serial_ogrn(ru_ogrn)

    if not comment or is_ukrainian_symbols(comment):
        comment = None

    return {
        "post": post,
        "date_start": date_start,
        "date_end": date_end,
        "company": company,
        "ru_inn": inn,
        "ru_ogrn": ogrn,
        "address": company_address,
        "comment": comment,
    }
