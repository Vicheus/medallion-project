from enum import Enum, StrEnum


class StageTypes(StrEnum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"


class EntityTypes(StrEnum):
    PERSONS = "persons"


class ColumnTypes(StrEnum):
    OBJECT_ID = "object_id"
    NAMES = "names"
    AVATAR = "avatar"
    SEX = "sex"
    BIRTH_DATE = "birth_date"
    DEATH_DATE = "death_date"
    BIRTH_PLACE = "birth_place"
    RELATIONSHIP = "relationship"
    CHILDREN = "children"
    PHONES = "phones"
    EMAILS = "emails"
    ADDRESS = "address"
    ADDRESSES = "addresses"
    RELATIONS = "relations"
    ACTUALITY = "actuality"
    SOCIALS = "socials"
    EDUCATIONS = "educations"
    WORKS = "works"
    FORCES = "forces"
    DOCUMENTS = "documents"
    VEHICLES = "vehicles"
    FINANCIALS = "financials"
    OWNERSHIPS = "ownerships"
    LINKS = "links"
    ACCOUNTS = "accounts"
    MOVEMENTS = "movements"
    INCIDENCES = "incidences"
    DEVICES = "devices"
    IPS = "ips"
    MEDIA = "media"
    RAW_METADATA = "raw_metadata"
    COMMENT = "comment"
    SOURCE_ENTITY_ID = "source_entity_id"


class ColumnAggTypes(Enum):
    GENERATED_ID = [ColumnTypes.SOURCE_ENTITY_ID.value]
    ANY = [
        ColumnTypes.AVATAR.value,
        ColumnTypes.BIRTH_DATE.value,
        ColumnTypes.DEATH_DATE.value,
        ColumnTypes.BIRTH_PLACE.value,
        ColumnTypes.CHILDREN.value,
        ColumnTypes.COMMENT.value,
        ColumnTypes.RELATIONSHIP.value,
        ColumnTypes.SEX.value,
    ]
    MAX = [
        ColumnTypes.ACTUALITY.value,
        ColumnTypes.OBJECT_ID.value,
    ]
    SCALARS = [
        ColumnTypes.ACTUALITY.value,
        ColumnTypes.AVATAR.value,
        ColumnTypes.BIRTH_DATE.value,
        ColumnTypes.DEATH_DATE.value,
        ColumnTypes.BIRTH_PLACE.value,
        ColumnTypes.CHILDREN.value,
        ColumnTypes.COMMENT.value,
        ColumnTypes.OBJECT_ID.value,
        ColumnTypes.RELATIONSHIP.value,
        ColumnTypes.SEX.value,
        ColumnTypes.SOURCE_ENTITY_ID.value,
    ]


class SourceIdTypes(StrEnum):
    SORTED_INCREASING_ID = "stable_int"
    NUM_HASH_ID = "hash_int"
    SHA_HASH_ID = "hash_sha224"
    INCREASING_ID = "unstable_int"


class JoinTypes(StrEnum):
    INNER = "inner"
    LEFT = "left"
    RIGHT = "right"
    OUTER = "outer"
    LEFT_ANTI = "left_anti"
    FULL = "full"


class TempColumnNames(StrEnum):
    MAX_STRUCT = "__max_struct"
    SOURCE_ENTITY_ID = "__source_entity_id"
    ISSUE_TYPE = "issue_type"
    HASH_OCCURRENCE = "hash_occurrence"
