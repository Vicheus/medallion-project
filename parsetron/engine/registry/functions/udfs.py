from typing import Literal, Optional

from pydantic import model_validator, Field, field_validator
from pydantic_core.core_schema import ValidationInfo
from pyspark.sql import Column
from pyspark.sql.functions import lit, array

from parsetron.engine.registry.base import (
    ActionLitType,
    ActionType,
    BaseCol,
    BaseCols,
    ColLiteral,
)
from parsetron.engine.registry.functions.base import BaseAction
from parsetron.engine.registry.resolver import resolve
from parsetron.sections.device.udfs import device_date_udf
from parsetron.sections.document.udfs import document_udf
from parsetron.sections.educations.udfs import education_udf
from parsetron.sections.financials.udfs import financial_udf, financial_date_expire_udf
from parsetron.sections.forces.udfs import force_udf
from parsetron.sections.ips.udfs import ip_address_udf, ip_udf
from parsetron.sections.links.udfs import link_udf
from parsetron.sections.main.udfs import (
    actuality_date_udf,
    address_udf,
    address_with_type_udf,
    birth_date_udf,
    children_udf,
    death_date_udf,
    email_udf,
    emails_udf,
    latest_actuality_date_udf,
    name_parts_ordered_udf,
    name_udf,
    names_udf,
    normalize_address_batch_udf,
    phone_udf,
    phones_udf,
    raw_metadata_udf,
    relationship_udf,
    sex_udf,
    multiple_date_formats_udf,
    relations_udf,
    addresses_udf,
    normalize_kz_letters_udf,
)
from parsetron.sections.movements.udfs import movement_udf, movement_datetime_udf
from parsetron.sections.socials.udfs import social_udf
from parsetron.sections.utils.udfs import (
    regexp_replace_all_udf,
    base_raw_validation_udf,
)
from parsetron.sections.vehicles.udfs import vehicle_udf
from parsetron.sections.work.udfs import work_date_udf
from parsetron.sections.work.udfs import work_with_docs_udf
from parsetron.settings import DATE_FORMAT


class ActualityDateUdf(BaseAction, BaseCol):
    fn: Literal["actuality_date_udf"]
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d %H:%M:%S")

    def apply(self) -> Column:
        return actuality_date_udf(resolve(self.column), resolve(self.date_format))


class LatestActualityDateUdf(BaseAction, BaseCols):
    fn: Literal["latest_actuality_date_udf"]
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d %H:%M:%S")

    def apply(self) -> Column:
        values = (resolve(column) for column in self.columns)
        return latest_actuality_date_udf(*values, date_format=resolve(self.date_format))


class NamePartsOrderedUdf(BaseAction, BaseCols):
    fn: Literal["name_parts_ordered_udf"]
    columns: list[ActionType] = Field(min_length=1, max_length=3)

    def apply(self) -> Column:
        values = (resolve(column) for column in self.columns)
        return name_parts_ordered_udf(*values)


class NamesUdf(BaseAction, BaseCol):
    fn: Literal["names_udf"]

    def apply(self) -> Column:
        return names_udf(resolve(self.column))


class NameUdf(BaseAction, BaseCol):
    fn: Literal["name_udf"]

    def apply(self) -> Column:
        return name_udf(resolve(self.column))


class BirthDateUdf(BaseAction, BaseCol):
    fn: Literal["birth_date_udf"]
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d")

    def apply(self) -> Column:
        if self.date_format:
            return birth_date_udf(resolve(self.column), resolve(self.date_format))
        return birth_date_udf(resolve(self.column))


class DeathDateUdf(BaseAction, BaseCol):
    fn: Literal["death_date_udf"]
    birth_date: Optional[ActionLitType] = None
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d")

    def apply(self) -> Column:
        if self.date_format:
            return death_date_udf(
                resolve(self.column),
                resolve(self.birth_date),
                resolve(self.date_format),
            )
        return death_date_udf(resolve(self.column), resolve(self.birth_date))


class SexUdf(BaseAction, BaseCol):
    fn: Literal["sex_udf"]

    def apply(self) -> Column:
        return sex_udf(resolve(self.column))


class PhonesUdf(BaseAction, BaseCol):
    fn: Literal["phones_udf"]
    country_code: Optional[ColLiteral] = Field(None, alias="countryCode")

    def apply(self) -> Column:
        if self.country_code:
            return phones_udf(resolve(self.column), resolve(self.country_code))
        return phones_udf(resolve(self.column))

    @model_validator(mode="after")
    def find_country_code(self, info: ValidationInfo):
        if (
            not self.country_code
            and info
            and info.context
            and info.context.get("country_code")
        ):
            self.country_code = ColLiteral(lit=info.context.get("country_code"))
        return self


class PhoneUdf(BaseAction, BaseCol):
    fn: Literal["phone_udf"]
    country_code: Optional[ColLiteral] = None

    def apply(self) -> Column:
        if self.country_code:
            return phone_udf(resolve(self.column), resolve(self.country_code))
        return phone_udf(resolve(self.column))

    @model_validator(mode="after")
    def find_country_code(self, info: ValidationInfo):
        if (
            not self.country_code
            and info
            and info.context
            and info.context.get("country_code")
        ):
            self.country_code = ColLiteral(lit=info.context.get("country_code"))
        return self


class EmailsUdf(BaseAction, BaseCol):
    fn: Literal["emails_udf"]

    def apply(self) -> Column:
        return emails_udf(resolve(self.column))


class EmailUdf(BaseAction, BaseCol):
    fn: Literal["email_udf"]

    def apply(self) -> Column:
        return email_udf(resolve(self.column))


class AddressesUdf(BaseAction, BaseCol):
    fn: Literal["addresses_udf"]

    def apply(self) -> Column:
        return addresses_udf(resolve(self.column))


class AddressUdf(BaseAction, BaseCol):
    fn: Literal["address_udf"]

    def apply(self) -> Column:
        return address_udf(resolve(self.column))


class IpAddressUdf(BaseAction, BaseCol):
    fn: Literal["ip_address_udf"]

    def apply(self) -> Column:
        return ip_address_udf(resolve(self.column))


class IpUdf(BaseAction):
    fn: Literal["ip_udf"]
    ip: Optional[ActionLitType] = None
    date: Optional[ActionLitType] = None
    comment: Optional[ActionLitType] = None
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d")

    def apply(self) -> Column:
        return ip_udf(
            ip=resolve(self.ip),
            date=resolve(self.date),
            comment=resolve(self.comment),
            date_format=resolve(self.date_format),
        )


class WorkUdf(BaseAction):
    fn: Literal["work_udf"]
    post: Optional[ActionLitType] = None
    date_start: Optional[ActionLitType] = None
    date_end: Optional[ActionLitType] = None
    company: Optional[ActionLitType] = None
    company_ru_inn: Optional[ActionLitType] = None
    company_ru_ogrn: Optional[ActionLitType] = None
    company_address: Optional[ActionLitType] = None
    comment: Optional[ActionLitType] = None

    def apply(self) -> Column:
        return work_with_docs_udf(
            post=resolve(self.post),
            date_start=resolve(self.date_start),
            date_end=resolve(self.date_end),
            company=resolve(self.company),
            ru_inn=resolve(self.company_ru_inn),
            ru_ogrn=resolve(self.company_ru_ogrn),
            company_address=resolve(self.company_address),
            comment=resolve(self.comment),
        )


class WorkDateUdf(BaseAction, BaseCol):
    fn: Literal["work_date_udf"]
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d")

    def apply(self) -> Column:
        return work_date_udf(
            string=resolve(self.column), date_format=resolve(self.date_format)
        )


class DocumentUdf(BaseAction):
    fn: Literal["document_udf"]
    type: Optional[ActionLitType] = None
    serial: ActionLitType
    date_issue: Optional[ActionLitType] = None
    date_expire: Optional[ActionLitType] = None
    authority: Optional[ActionLitType] = None
    authority_code: Optional[ActionLitType] = None
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d")
    country_code: Optional[ColLiteral] = None

    def apply(self) -> Column:
        return document_udf(
            document_type=resolve(self.type),
            serial=resolve(self.serial),
            date_issue=resolve(self.date_issue),
            date_expire=resolve(self.date_expire),
            authority=resolve(self.authority),
            authority_code=resolve(self.authority_code),
            date_format=resolve(self.date_format),
            country_code=resolve(
                self.country_code if self.country_code else ColLiteral(lit="RU")
            ),
        )

    @model_validator(mode="after")
    def find_country_code(self, info: ValidationInfo):
        if (
            not self.country_code
            and info
            and info.context
            and info.context.get("country_code")
        ):
            self.country_code = ColLiteral(lit=info.context.get("country_code"))
        return self


class ForceUdf(BaseAction):
    fn: Literal["force_udf"]
    tag_number: Optional[ActionLitType] = None
    unit_code: Optional[ActionLitType] = None
    unit_name: Optional[ActionLitType] = None
    callsign: Optional[ActionLitType] = None
    rank: Optional[ActionLitType] = None
    position: Optional[ActionLitType] = None
    mos_code: Optional[ActionLitType] = None
    category: Optional[ActionLitType] = None
    date_start: Optional[ActionLitType] = None
    date_end: Optional[ActionLitType] = None
    comment: Optional[ActionLitType] = None
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d")

    def apply(self) -> Column:
        return force_udf(
            tag_number=resolve(self.tag_number),
            unit_code=resolve(self.unit_code),
            unit_name=resolve(self.unit_name),
            callsign=resolve(self.callsign),
            rank=resolve(self.rank),
            position=resolve(self.position),
            mos_code=resolve(self.mos_code),
            category=resolve(self.category),
            date_start=resolve(self.date_start),
            date_end=resolve(self.date_end),
            comment=resolve(self.comment),
            date_format=resolve(self.date_format),
        )


class EducationUdf(BaseAction):
    fn: Literal["education_udf"]
    title: Optional[ActionLitType] = None
    level: Optional[ActionLitType] = None
    country: Optional[ActionLitType] = None
    date_start: Optional[ActionLitType] = None
    date_end: Optional[ActionLitType] = None
    comment: Optional[ActionLitType] = None
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d")

    def apply(self) -> Column:
        return education_udf(
            title=resolve(self.title),
            level=resolve(self.level),
            country=resolve(self.country),
            date_start=resolve(self.date_start),
            date_end=resolve(self.date_end),
            comment=resolve(self.comment),
            date_format=resolve(self.date_format),
        )


class RawMetadataUdf(BaseAction):
    fn: Literal["raw_metadata_udf"]
    values: dict[str, ActionLitType]

    def apply(self) -> Column:
        values = []
        for k, v in self.values.items():
            values.append(lit(k))
            values.append(resolve(v))
        return raw_metadata_udf(*values)

    @model_validator(mode="before")
    @classmethod
    def parse_items(cls, values: dict, info: ValidationInfo):
        itms = values.get("values")
        if isinstance(itms, dict):
            itm = {}
            for key, value in itms.items():
                if isinstance(value, dict) and not (
                    len(value.keys()) == 1 and "lit" in value.keys()
                ):
                    itm[key] = BaseAction.from_dict(value, info)
                else:
                    itm[key] = value
            values["values"] = itm
        return values


class BaseRawValidationUdf(BaseAction, BaseCol):
    fn: Literal["base_raw_validation_udf"]

    def apply(self) -> Column:
        return base_raw_validation_udf(resolve(self.column))


class VehicleUdf(BaseAction):
    fn: Literal["vehicle_udf"]
    type: ActionLitType
    model: Optional[ActionLitType] = None
    year: Optional[ActionLitType] = None
    color: Optional[ActionLitType] = None
    number: Optional[ActionLitType] = None
    vin: Optional[ActionLitType] = None
    comment: Optional[ActionLitType] = None

    def apply(self) -> Column:
        return vehicle_udf(
            type=resolve(self.type),
            model=resolve(self.model),
            year=resolve(self.year),
            color=resolve(self.color),
            number=resolve(self.number),
            vin=resolve(self.vin),
            comment=resolve(self.comment),
        )


class AddressWithTypeUdf(BaseAction, BaseCol):
    fn: Literal["address_with_type_udf"]
    type: ActionLitType

    def apply(self) -> Column:
        return address_with_type_udf(resolve(self.column), resolve(self.type))


class NormalizeAddressBatchUdf(BaseAction, BaseCol):
    fn: Literal["normalize_address_batch_udf"]

    def apply(self) -> Column:
        return normalize_address_batch_udf(resolve(self.column))


class ChildrenUdf(BaseAction, BaseCol):
    fn: Literal["children_udf"]

    def apply(self) -> Column:
        return children_udf(resolve(self.column))


class DeviceDateUdf(BaseAction, BaseCol):
    fn: Literal["device_date_udf"]
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d")

    def apply(self) -> Column:
        return device_date_udf(resolve(self.column), resolve(self.date_format))


class MultipleDateFormatsUdf(BaseAction, BaseCol):
    fn: Literal["multiple_date_formats_udf"]
    date_formats: list[ColLiteral] = [ColLiteral(lit="%Y-%m-%d")]
    max_years_from: ColLiteral = ColLiteral(lit=50)
    max_years_to: ColLiteral = ColLiteral(lit=0)
    result_date_format: ColLiteral = ColLiteral(lit=DATE_FORMAT)

    def apply(self) -> Column:
        date_formats = [resolve(date_format) for date_format in self.date_formats]
        return multiple_date_formats_udf(
            value=resolve(self.column),
            date_formats=array(*date_formats),
            max_years_from=resolve(self.max_years_from),
            max_years_to=resolve(self.max_years_to),
            result_date_format=resolve(self.result_date_format),
        )

    @field_validator("date_formats", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]


class RelationshipUdf(BaseAction, BaseCol):
    fn: Literal["relationship_udf"]

    def apply(self) -> Column:
        return relationship_udf(resolve(self.column))


class RelationsUdf(BaseAction, BaseCol):
    fn: Literal["relations_udf"]

    def apply(self) -> Column:
        return relations_udf(resolve(self.column))


class MovementUdf(BaseAction):
    fn: Literal["movement_udf"]
    from_datetime: Optional[ActionLitType] = None
    from_country: Optional[ActionLitType] = None
    from_city: Optional[ActionLitType] = None
    from_code: Optional[ActionLitType] = None
    to_datetime: Optional[ActionLitType] = None
    to_country: Optional[ActionLitType] = None
    to_city: Optional[ActionLitType] = None
    to_code: Optional[ActionLitType] = None
    code_type: Optional[ActionLitType] = None
    ticket_order_datetime: Optional[ActionLitType] = None
    fixation_datetime: Optional[ActionLitType] = None
    seat: Optional[ActionLitType] = None
    ticket_number: Optional[ActionLitType] = None
    trip_number: Optional[ActionLitType] = None
    class_: Optional[ActionLitType] = None
    type: Optional[ActionLitType] = None
    comment: Optional[ActionLitType] = None
    ticket_issuer: Optional[ActionLitType] = None
    transport_company_name: Optional[ActionLitType] = None
    transport_company_code: Optional[ActionLitType] = None

    def apply(self) -> Column:
        return movement_udf(
            from_datetime=resolve(self.from_datetime),
            from_country=resolve(self.from_country),
            from_city=resolve(self.from_city),
            from_code=resolve(self.from_code),
            to_datetime=resolve(self.to_datetime),
            to_country=resolve(self.to_country),
            to_city=resolve(self.to_city),
            to_code=resolve(self.to_code),
            code_type=resolve(self.code_type),
            ticket_order_datetime=resolve(self.ticket_order_datetime),
            fixation_datetime=resolve(self.fixation_datetime),
            seat=resolve(self.seat),
            ticket_number=resolve(self.ticket_number),
            trip_number=resolve(self.trip_number),
            class_=resolve(self.class_),
            type_=resolve(self.type),
            comment=resolve(self.comment),
            ticket_issuer=resolve(self.ticket_issuer),
            transport_company_name=resolve(self.transport_company_name),
            transport_company_code=resolve(self.transport_company_code),
        )


class MovementDateTimeUdf(BaseAction, BaseCol):
    fn: Literal["movement_datetime_udf"]
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d %H:%M:%S")

    def apply(self) -> Column:
        return movement_datetime_udf(
            string=resolve(self.column), date_format=resolve(self.date_format)
        )


class SocialUdf(BaseAction):
    fn: Literal["social_udf"]
    title: Optional[ActionLitType] = None
    id: Optional[ActionLitType] = None
    link: Optional[ActionLitType] = None
    comment: Optional[ActionLitType] = None

    def apply(self) -> Column:
        return social_udf(
            title=resolve(self.title),
            id=resolve(self.id),
            link=resolve(self.link),
            comment=resolve(self.comment),
        )


class FinancialUdf(BaseAction):
    fn: Literal["financial_udf"]
    title: Optional[ActionLitType] = None
    card_number: Optional[ActionLitType] = None
    invoice_number: Optional[ActionLitType] = None
    date_issue: Optional[ActionLitType] = None
    date_expire: Optional[ActionLitType] = None
    comment: Optional[ActionLitType] = None
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d")

    def apply(self) -> Column:
        return financial_udf(
            title=resolve(self.title),
            card_number=resolve(self.card_number),
            invoice_number=resolve(self.invoice_number),
            date_issue=resolve(self.date_issue),
            date_expire=resolve(self.date_expire),
            comment=resolve(self.comment),
            date_format=resolve(self.date_format),
        )


class FinancialDateExpireUdf(BaseAction, BaseCol):
    fn: Literal["financial_date_expire_udf"]
    date_format: ColLiteral = ColLiteral(lit="%Y-%m-%d")

    def apply(self) -> Column:
        if self.date_format:
            return financial_date_expire_udf(
                resolve(self.column), resolve(self.date_format)
            )
        return financial_date_expire_udf(resolve(self.column))


class LinkUdf(BaseAction):
    fn: Literal["link_udf"]
    title: ActionLitType
    link: ActionLitType
    comment: Optional[ActionLitType] = None

    def apply(self) -> Column:
        return link_udf(
            title=resolve(self.title),
            link=resolve(self.link),
            comment=resolve(self.comment),
        )


class RegexpReplaceAllUdf(BaseAction, BaseCol):
    fn: Literal["regexp_replace_all_udf"]
    values: dict[str, str]

    def apply(self) -> Column:
        return regexp_replace_all_udf(self.values)(resolve(self.column))


class NormalizeKZLettersUdf(BaseAction, BaseCol):
    fn: Literal["normalize_kz_letters_udf"]

    def apply(self) -> Column:
        return normalize_kz_letters_udf(resolve(self.column))
