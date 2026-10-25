from ..validators.serial.document_serial_base import (
    document_serial_digits,
    document_serial,
)
from ..validators.serial.document_serial_by import (
    document_serial_passport,
    document_serial_id_number,
    document_serial_inn,
    document_serial_unp,
    document_serial_diplomatic_passport,
)

DOCUMENT_CONFIG = [
    {
        "regex": [
            r"^((АВ|ВМ|НВ|КН|МР|МС|КВ|РР|ав|вм|нв|кн|мр|мс|кв|рр)\s?\d{7})(?![0-9])",
        ],
        "texts": ["паспорт гражданина рб", "паспорт гражданина республики беларусь"],
        "type": 0,
        "country": "BLR",
        "validator": document_serial_passport,
    },
    {
        "regex": [
            r"^((DP|SP|dp|sp)\s?\d{7})(?![0-9])",
        ],
        "texts": [
            "дипломатический паспорт рб",
        ],
        "type": 11,
        "country": "BLR",
        "validator": document_serial_diplomatic_passport,
    },
    {
        "texts": [
            "инн рб",
            "индивидуальный номер налогоплательщика рб",
        ],
        "type": 1,
        "country": "BLR",
        "validator": document_serial_inn,
    },
    {
        "texts": [
            "водительское удостоверение",
        ],
        "type": 3,
        "country": "BLR",
        "validator": document_serial_digits,
    },
    {
        "regex": [
            r"СР(\d[А-ЯЁ]{2}\d{6})(?![0-9])",
            r"СР([IVXLCDM]+[А-ЯЁ]{2}\d{7})(?![0-9])",
            r"(\d[А-ЯЁ]{2}\d{6})(?![0-9])",
            r"([IVXLCDM]+[А-ЯЁ]{2}\d{7})(?![0-9])",
        ],
        "texts": [
            "свидетельство о рождении",
        ],
        "type": 5,
        "country": "BLR",
        "validator": document_serial,
    },
    {
        "regex": [r"(\d[А-ЯЁ]{2}\d{7})(?![0-9])"],
        "texts": [
            "удостоверение личности военнослужащего",
        ],
        "type": 6,
        "country": "BLR",
        "validator": document_serial,
    },
    {
        "texts": [
            "удостоверение беженца",
        ],
        "type": 7,
        "country": "BLR",
        "validator": document_serial_digits,
    },
    {
        "texts": [
            "вид на жительство",
        ],
        "type": 8,
        "country": "RUS",
        "validator": document_serial_digits,
    },
    {
        "texts": [
            "идентификационный номер гражданина рб",
        ],
        "type": 13,
        "country": "BLR",
        "validator": document_serial_id_number,
    },
    {
        "texts": [
            "унп",
            "учетный номер плательщика",
        ],
        "type": 14,
        "country": "BLR",
        "validator": document_serial_unp,
    },
    {
        "texts": ["номер страхового полиса"],
        "type": 16,
        "country": "RUS",
        "validator": document_serial_digits,
    },
]
