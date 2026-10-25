import re
from parsetron.sections.base.validators.base import base_validation


def validate_vin(vin):
    vin = base_validation(vin)
    if not vin:
        return None
    vin = vin.upper()
    try:
        # Check VIN length and characters
        # VINs must be exactly 17 characters and must not contain I, O, or Q
        if len(vin) != 17 or not re.match(r"^[A-HJ-NPR-Z0-9]{17}$", vin):
            return None

        return vin
    except:  # noqa: E722
        return
