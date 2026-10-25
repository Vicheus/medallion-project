from typing import Optional, Dict, Union
from datetime import datetime

from parsetron.sections.base.validators.base import base_validation
from .vin import validate_vin
from .vehicle_number import validate_number


def vehicle(
    type: int,
    model: str = None,
    year: int = None,
    color: str = None,
    number: str = None,
    vin: str = None,
    comment: str = None,
) -> Optional[Dict[str, Union[int, str]]]:
    if not type:
        return
    model = base_validation(model)
    number = validate_number(number)
    vin = validate_vin(vin)
    if year is not None:
        if (year < 1800) | (year > datetime.now().year):
            year = None

    if (not model) & (not number) & (not vin):
        return

    return {
        "type": type,
        "model": model,
        "year": year,
        "color": base_validation(color),
        "number": number,
        "vin": vin,
        "comment": base_validation(comment),
    }
