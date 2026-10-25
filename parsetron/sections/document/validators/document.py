import importlib
import re
from typing import Optional, Dict, Union

import pandas as pd

from parsetron.utils import DocumentsAnalyzer
from .document_date_expire import document_date_expire
from .document_date_issue import document_date_issue
from ...base.validators.base import is_ukrainian_symbols


def load_config(country_code: str):
    map = {
        "RU": "parsetron.sections.document.settings.settings_ru",
        "BY": "parsetron.sections.document.settings.settings_by",
        "KZ": "parsetron.sections.document.settings.settings_kz",
    }
    module_name = map.get(country_code)
    if module_name:
        settings_module = importlib.import_module(module_name)
        return settings_module.DOCUMENT_CONFIG
    else:
        raise ValueError(f"Unsupported country code: {country_code}")


def _build_document_data(
    document_config,
    serial,
    authority_code,
    date_issue,
    date_expire,
    date_format,
    authority,
):
    serial = document_config["validator"](serial)

    if not serial:
        return None

    if not authority or is_ukrainian_symbols(authority):
        authority = None
    if authority_code:
        authority_code = re.sub(r"\D", "", authority_code)

    return {
        "type": document_config["type"],
        "serial": serial,
        "country": document_config["country"],
        "date_issue": document_date_issue(date_issue, date_format),
        "date_expire": document_date_expire(date_expire, date_format),
        "authority": authority,
        "authority_code": authority_code if authority_code else None,
    }


def document(
    document_type: str,
    serial: str,
    date_issue: str = None,
    date_expire: str = None,
    authority: str = None,
    authority_code: str = None,
    date_format: str = "yyyy-MM-dd",
    country_code: str = "RU",
) -> Optional[Dict[str, Union[int, str]]]:
    DOCUMENT_CONFIG = load_config(country_code)

    if (not document_type) & (not serial):
        return

    if document_type:
        for config in DOCUMENT_CONFIG:
            if document_type.lower() in config["texts"]:
                return _build_document_data(
                    config,
                    serial,
                    authority_code,
                    date_issue,
                    date_expire,
                    date_format,
                    authority,
                )
        return None
    else:
        for config in sorted(DOCUMENT_CONFIG, key=lambda x: x["type"]):
            try:
                if (serial is not None) & (config.get("regex") is not None):
                    serial = serial.strip().replace(" ", "")
                    for pattern in config["regex"]:
                        match = re.search(pattern, serial)
                        if match:
                            extracted_serial = match.group(1)

                            return _build_document_data(
                                config,
                                extracted_serial,
                                authority_code,
                                date_issue,
                                date_expire,
                                date_format,
                                authority,
                            )
            except Exception as e:
                print(f"Error: {e}. For serial: {serial} and {config}")

    return None


def get_document_features_batch(documents_series: pd.Series) -> pd.Series:
    analyzer = DocumentsAnalyzer()
    print(f"Extract features from: {documents_series.items()}")

    documents_features = []

    for idx, documents_arr in documents_series.items():
        documents_dicts = []
        for document_entry in documents_arr:
            print(f"Extract features from: {document_entry}")
            try:
                if not document_entry:
                    documents_dicts.append(None)
                    continue

                document_features = analyzer.identify_document_features(document_entry)

                if isinstance(document_features, dict):
                    documents_dicts.append(document_features)
                else:
                    documents_dicts.append(None)
            except Exception as e:
                print(f"Error processing document at index {idx}: {e}")
                documents_dicts.append(None)

        documents_features.append(documents_dicts)

    return pd.Series(documents_features)


def get_document_features(document_raw):
    analyzer = DocumentsAnalyzer()
    if document_raw == "None":
        return

    try:
        if not document_raw:
            return
        print(f"Extract features from: {document_raw}")

        document_features = analyzer.identify_document_features(document_raw)

        if isinstance(document_features, dict):
            return document_features
        else:
            return
    except Exception as e:
        print(f"Error processing document {document_raw}: {e}")
        return
