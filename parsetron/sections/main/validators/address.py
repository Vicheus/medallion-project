from typing import Optional, List, Dict, Union, Any

import cachetools
import pandas as pd

from parsetron.sections.base.validators.base import (
    base_validation,
    base_address_validation,
)
from parsetron.utils import TextAnalyser, AddressAnalyzer

cache = cachetools.TTLCache(maxsize=128, ttl=60 * 180)


def address(value: str) -> Optional[str]:
    string = base_address_validation(value)

    if not string:
        return None

    if len(string) <= 2:
        return None

    if string.islower() or string.isupper():
        string = string.title()

    return string


def address_from_parts(
    type: Optional[int],
    index: Optional[str],
    country: Optional[str],
    region: Optional[str],
    settlement: Optional[str],
    street: Optional[str],
    house: Optional[str],
    floor: Optional[str],
    flat: Optional[str],
    office: Optional[str],
    corpus: Optional[str],
) -> Optional[Dict[str, Any]]:
    index = base_validation(index)
    country = base_validation(country)
    region = base_validation(region)
    settlement = base_validation(settlement)
    street = base_address_validation(street)
    house = base_address_validation(house)
    floor = base_validation(floor)
    flat = base_validation(flat)
    office = base_validation(office)
    corpus = base_validation(corpus)

    parts = [
        p
        for p in [
            index,
            country,
            region,
            settlement,
            street,
            house,
            floor,
            flat,
            office,
            corpus,
        ]
        if p
    ]
    if not parts:
        return

    concatenated = ", ".join(parts)

    location = {
        "region_type": None,
        "region_value": region,
        "settlement_region_type": None,
        "settlement_region_value": None,
        "settlement_type": None,
        "settlement_value": settlement,
        "street_type": None,
        "street_value": street,
        "house": house,
        "flat": flat,
        "floor": floor,
        "office": office,
        "corpus": corpus,
        "coordinates": None,
        "coord_detalization_lvl": None,
    }

    location = {k: v for k, v in location.items() if v is not None}

    result = {
        "type": type,
        "raw": concatenated,
        "address": address(concatenated),
        "location": location,
    }

    return result


def address_with_type(
    string: str, address_type: int
) -> Optional[Dict[str, Union[int, str]]]:
    address_info = {"address": string, "address_type": address_type}

    return address_info


def addresses_with_type(
    addresses: List[str], address_type: int
) -> Optional[Dict[str, Union[int, str]]]:
    if not addresses:
        return None

    addresses_with_type = []
    for address_value in addresses:
        address_info = {"address": address_value, "address_type": address_type}
        addresses_with_type.append(address_info)

    return addresses_with_type if len(addresses_with_type) > 0 else None


def addresses(addresses: List[str]) -> Optional[List[str]]:
    if not addresses:
        return None

    formatted_addresses = set()
    for address_value in addresses:
        formatted_address = address(address_value)
        if not formatted_address:
            continue

        formatted_addresses.add(formatted_address)

    return list(formatted_addresses) if len(formatted_addresses) > 0 else None


def extract_address(texts: List[str]) -> Optional[List[str]]:
    if not texts:
        return None
    addresses = set()
    for text in texts:
        found_location = TextAnalyser.extract_address(text)
        if found_location:
            addresses.add(found_location)

    return list(addresses) if len(addresses) > 0 else None


def normalize_address_batch(address_series: pd.Series) -> pd.Series:
    analyzer = AddressAnalyzer()

    normalized_addresses = []

    for idx, address_arr in address_series.items():
        address_dicts = []
        if address_arr is None:
            normalized_addresses.append(address_dicts)
            continue
        for address_entry in address_arr:
            print(f"""Normalize: {address_entry}""")
            try:
                if not address_entry:
                    address_dicts.append(None)
                    continue
                address_str = address_entry.get("address")
                address_type = address_entry.get("address_type")
                if not address_arr.any():
                    continue
                raw_address = address_str
                cleaned_address_str = address(address_str)
                normalized_address = analyzer.normalize_address(
                    raw_address, cleaned_address_str, address_type
                )

                if normalized_address is not None and isinstance(
                    normalized_address, dict
                ):
                    address_dicts.append(normalized_address)
                else:
                    address_dicts.append(None)
            except Exception as e:
                print(f"Error processing address at index {idx}: {e}")
                address_dicts.append(None)

        normalized_addresses.append(address_dicts)

    print(normalized_addresses)

    return pd.Series(normalized_addresses)
