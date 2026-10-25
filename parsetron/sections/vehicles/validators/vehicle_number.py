from parsetron.sections.base.validators.base import base_validation


def validate_number(number):
    number = base_validation(number)
    if not number:
        return None

    if (len(number) < 4) | (len(number) > 10):
        return None

    return number
