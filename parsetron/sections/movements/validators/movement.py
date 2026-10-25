from typing import Optional, Dict, Union
from airportsdata import load
from transliterate import translit
from parsetron.sections.base.validators.base import base_validation, base_raw_validation


def movement(
    from_datetime: str = None,
    from_country: str = None,
    from_city: str = None,
    from_code: str = None,
    to_datetime: str = None,
    to_country: str = None,
    to_city: str = None,
    to_code: str = None,
    code_type: str = None,
    ticket_order_datetime: str = None,
    fixation_datetime: str = None,
    seat: str = None,
    ticket_number: str = None,
    trip_number: str = None,
    class_: str = None,
    type_: int = None,
    comment: str = None,
    ticket_issuer: str = None,
    transport_company_name: str = None,
    transport_company_code: str = None,
) -> Optional[Dict[str, Union[int, str]]]:

    if (not from_city) & (not from_code) & (not from_country):
        return
    if (not to_country) & (not to_city) & (not to_code):
        return

    return {
        "from": {
            "datetime": from_datetime,
            "country": from_country,
            "city": from_city,
            "code": from_code,
        },
        "to": {
            "datetime": to_datetime,
            "country": to_country,
            "city": to_city,
            "code": to_code,
        },
        "code_type": code_type,
        "ticket_order_datetime": ticket_order_datetime,
        "fixation_datetime": fixation_datetime,
        "seat": seat,
        "ticket_number": ticket_number,
        "trip_number": trip_number,
        "class": class_,
        "type": type_,
        "comment": comment,
        "ticket_issuer": base_validation(ticket_issuer),
        "transport_company_name": base_raw_validation(transport_company_name),
        "transport_company_code": base_validation(transport_company_code),
    }


# Function to get airport code by name
def get_airport_code_by_name(name):
    if not name:
        return None
    name_stopwords = ["Кыргызстан", "Россия"]
    airports = load("IATA")  # Use "ICAO" if you need ICAO codes
    name_parts = name.split(" ")
    for code, info in airports.items():
        print(info)
        for name_part in name_parts:

            if name_part in name_stopwords:
                continue
            if translit(name_part, "ru", reversed=True).lower() in info["name"].lower():
                print(
                    f"""Code: {code}, Info: {info["name"]}, Name part: {translit(name_part, 'ru', reversed=True)}, Name: {name}"""
                )
                return code
    return None
