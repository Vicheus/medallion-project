from pyspark.sql.functions import pandas_udf
from pyspark.sql.functions import udf

from .schemas import (
    name_schema,
    sex_schema,
    address_schema,
    addresses_schema,
    extract_address_schema,
    normalized_address_schema,
    normalized_addresses_schema,
    birth_date_schema,
    email_schema,
    phone_schema,
    children_schema,
    names_schema,
    phones_schema,
    emails_schema,
    validate_name_is_person_or_organisation_schema,
    relations_schema,
    address_with_type_schema,
    addresses_with_type_schema,
    actuality_date_schema,
    relationship_schema,
    raw_metadata_schema,
    normalize_kz_letters_schema,
    death_date_schema,
    multiple_date_formats_schema,
)
from .validators.actuality_date import actuality_date, latest_actuality_date
from .validators.address import (
    address,
    addresses,
    extract_address,
    normalize_address_batch,
    address_with_type,
    addresses_with_type,
    address_from_parts,
)
from .validators.birth_date import birth_date
from .validators.children import children
from .validators.death_date import death_date
from .validators.email import email, emails
from .validators.multiple_dates import multiple_date_formats
from .validators.name import (
    name,
    names,
    name_parts,
    validate_name_is_person_or_organisation,
    extract_name,
    name_parts_ordered,
)
from .validators.normalize_kz_letters import normalize_kz_letters
from .validators.phone import phone, phones
from .validators.raw_metadata import raw_metadata
from .validators.relation import relation
from .validators.relationship import relationship
from .validators.sex import sex

name_udf = udf(name, name_schema)
names_udf = udf(names, names_schema)
name_parts_udf = udf(name_parts, name_schema)
name_parts_ordered_udf = udf(name_parts_ordered, name_schema)
validate_name_is_person_or_organisation_udf = udf(
    validate_name_is_person_or_organisation,
    validate_name_is_person_or_organisation_schema,
)
normalize_kz_letters_udf = udf(normalize_kz_letters, normalize_kz_letters_schema)
sex_udf = udf(sex, sex_schema)
address_udf = udf(address, address_schema)
addresses_udf = udf(addresses, addresses_schema)
address_from_parts_udf = udf(address_from_parts, normalized_address_schema)
address_with_type_udf = udf(address_with_type, address_with_type_schema)
addresses_with_type_udf = udf(addresses_with_type, addresses_with_type_schema)
birth_date_udf = udf(birth_date, birth_date_schema)
death_date_udf = udf(death_date, death_date_schema)
multiple_date_formats_udf = udf(multiple_date_formats, multiple_date_formats_schema)
email_udf = udf(email, email_schema)
emails_udf = udf(emails, emails_schema)
phone_udf = udf(phone, phone_schema)
phones_udf = udf(phones, phones_schema)
children_udf = udf(children, children_schema)
extract_address_udf = udf(extract_address, extract_address_schema)
relations_udf = udf(relation, relations_schema)
normalize_address_batch_udf = pandas_udf(
    normalize_address_batch, normalized_addresses_schema
)
actuality_date_udf = udf(actuality_date, actuality_date_schema)
latest_actuality_date_udf = udf(latest_actuality_date, actuality_date_schema)
relationship_udf = udf(relationship, relationship_schema)
extract_name_udf = udf(extract_name, name_schema)
raw_metadata_udf = udf(raw_metadata, raw_metadata_schema)
