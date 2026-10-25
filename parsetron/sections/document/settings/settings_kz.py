from ..validators.serial.document_serial_base import (
    document_serial_digits,
    document_serial,
)
from ..validators.serial.document_serial_kz import (
    document_serial_passport,
    document_serial_inn,
    document_serial_id_number,
    document_serial_driver_license,
    document_serial_seaman_passport,
)

DOCUMENT_CONFIG = [
    {
        "regex": [r"([Nn]\s?\d{8})(?![0-9])"],
        "texts": ["паспорт гражданина рк", "паспорт гражданина республики казахстан"],
        "type": 0,
        "country": "KZ",
        "validator": document_serial_passport,
    },
    {
        "texts": [
            "инн",
            "индивидуальный номер налогоплательщика",
            "бизнес идентификационный номер",
        ],
        "type": 1,
        "country": "KZ",
        "validator": document_serial_inn,
    },
    {
        "texts": [
            "водительское удостоверение",
        ],
        "type": 3,
        "country": "KZ",
        "validator": document_serial_driver_license,
    },
    {
        "regex": [
            r"^([A-Za-z]{2}\s?№?\s?\d{6,7})$",
            r"^([А-Яа-я]{2}\s?№?\s?\d{6,7,8})$",
            r"([IVXLCDM]+[А-ЯЁ]{2}\d{7})(?![0-9])",
        ],
        "texts": [
            "свидетельство о рождении",
        ],
        "type": 5,
        "country": "KZ",
        "validator": document_serial,
    },
    {
        "regex": [r"(БА\d{6,7})(?![0-9])"],
        "texts": [
            "удостоверение личности военнослужащего",
        ],
        "type": 6,
        "country": "KZ",
        "validator": document_serial,
    },
    {
        "texts": [
            "удостоверение беженца",
        ],
        "type": 7,
        "country": "KZ",
        "validator": document_serial_digits,
    },
    {
        "texts": [
            "вид на жительство",
        ],
        "type": 8,
        "country": "KZ",
        "validator": document_serial_id_number,
    },
    {
        "texts": [
            "Временное удостоверение личн. гражд. рк",
        ],
        "type": 9,
        "country": "KZ",
        "validator": document_serial_digits,
    },
    {
        "texts": [
            "паспорт моряка",
        ],
        "type": 10,
        "country": "KZ",
        "validator": document_serial_seaman_passport,
    },
    {
        "regex": [r"([D]\d{8})(?![0-9])"],
        "texts": [
            "дипломатический паспорт рк",
        ],
        "type": 11,
        "country": "KZ",
        "validator": document_serial,
    },
    {
        "regex": [
            r"([S]\d{8})",
        ],
        "texts": [
            "служебный паспорт рк",
        ],
        "type": 12,
        "country": "KZ",
        "validator": document_serial,
    },
    {
        "texts": [
            "удостоверение личности гражданина казахстана",
            "удостоверение личности рк",
        ],
        "type": 13,
        "country": "KZ",
        "validator": document_serial_id_number,
    },
]
