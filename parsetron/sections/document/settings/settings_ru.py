from ..validators.serial.document_serial_base import (
    document_serial_digits,
    document_serial,
)
from ..validators.serial.document_serial_ru import (
    document_serial_passport,
    document_serial_snils,
    document_serial_inn,
    document_serial_kpp,
    document_serial_ogrn,
    document_serial_driver_license,
    document_serial_international_passport,
    document_serial_birth_certificate,
    document_serial_resident_card,
    document_serial_diplomatic_passport,
    document_serial_service_passport,
    document_serial_military_identification_card,
    document_serial_snils_without_control_sum,
)

DOCUMENT_CONFIG = [
    {
        "regex": [
            r"ПС(\d{10})(?![0-9])",
            r"PS(\d{10})(?![0-9])",
            r"ПН(\d{10})(?![0-9])",
            r"^(\d{10})$",
        ],
        "texts": ["паспорт гражданина рф", "паспорт гражданина российской федерации"],
        "type": 0,
        "country": "RUS",
        "validator": document_serial_passport,
    },
    {
        "texts": [
            "инн",
            "индивидуальный номер налогоплательщика",
        ],
        "type": 1,
        "country": "RUS",
        "validator": document_serial_inn,
    },
    {
        "texts": [
            "снилс",
        ],
        "type": 2,
        "country": "RUS",
        "validator": document_serial_snils,
    },
    {
        "texts": [
            "снилс без контрольной суммы",
        ],
        "type": 2,
        "country": "RUS",
        "validator": document_serial_snils_without_control_sum,
    },
    {
        "texts": [
            "водительское удостоверение",
        ],
        "type": 3,
        "country": "RUS",
        "validator": document_serial_driver_license,
    },
    {
        "regex": [
            r"ПСП(\d{9})(?![0-9])",
            r"PSP(\d{9})(?![0-9])",
            r"ЗП(\d{9})(?![0-9])",
            r"^(([5-8][0-9]|9[0-8])\d{7})$",
        ],
        "texts": [
            "заграничный паспорт гражданина рф",
            "загранпаспорт гражданина рф",
        ],
        "type": 4,
        "country": "RUS",
        "validator": document_serial_international_passport,
    },
    {
        "regex": [r"ЗЗ(.+)", r"ZA(.+)", r"ЗА(.+)"],
        "texts": [
            "заграничный паспорт",
        ],
        "type": 4,
        "country": None,
        "validator": document_serial_digits,
    },
    {
        "regex": [
            r"СР((?<![0-9])([2-9]|1+)-?[а-яА-ЯёЁ]{2}\d{6})(?![0-9])",
            r"СР([IVXLCDMivxlcdm]+-?[а-яА-ЯёЁ]{2}\d{6})(?![0-9])",
            r"((?<![0-9])([2-9]|1+)-?[а-яА-ЯёЁ]{2}\d{6})(?![0-9])",
            r"([IVXLCDMivxlcdm]+-?[а-яА-ЯёЁ]{2}\d{6})(?![0-9])",
        ],
        "texts": [
            "свидетельство о рождении",
        ],
        "type": 5,
        "country": "RUS",
        "validator": document_serial_birth_certificate,
    },
    {
        "regex": [
            r"УДЛ(.+)",
            r"ВБ(.+)",
        ],
        "texts": [
            "удостоверение личности военнослужащего",
        ],
        "type": 6,
        "country": "RUS",
        "validator": document_serial_military_identification_card,
    },
    {
        "texts": [
            "удостоверение беженца",
        ],
        "type": 7,
        "country": "RUS",
        "validator": document_serial,
    },
    {
        "regex": [r"ВЖ(.+)"],
        "texts": [
            "вид на жительство",
        ],
        "type": 8,
        "country": "RUS",
        "validator": document_serial_resident_card,
    },
    {
        "regex": [r"СПУ(.+)"],
        "texts": [
            "Временное удостоверение личн. гражд. РФ",
        ],
        "type": 9,
        "country": "RUS",
        "validator": document_serial,
    },
    {
        "regex": [
            r"ПМ(.+)",
        ],
        "texts": [
            "паспорт моряка",
        ],
        "type": 10,
        "country": "RUS",
        "validator": document_serial,
    },
    {
        "regex": [r"ДП(.+)", r"^(10\d{7})$"],
        "texts": [
            "дипломатический паспорт рф",
        ],
        "type": 11,
        "country": "RUS",
        "validator": document_serial_diplomatic_passport,
    },
    {
        "regex": [r"СП(.+)", r"^(20\d{7})$"],
        "texts": ["служебный паспорт рф"],
        "type": 12,
        "country": "RUS",
        "validator": document_serial_service_passport,
    },
    {
        "texts": [
            "кпп",
            "код причины постановки на учет",
        ],
        "type": 14,
        "country": "RUS",
        "validator": document_serial_kpp,
    },
    {
        "texts": [
            "огрн",
            "основной государственный регистрационный номер",
        ],
        "type": 15,
        "country": "RUS",
        "validator": document_serial_ogrn,
    },
    {
        "texts": ["номер страхового полиса"],
        "type": 16,
        "country": "RUS",
        "validator": document_serial,
    },
]
