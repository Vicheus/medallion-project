import asyncio
import logging
import re
from typing import Optional

import aiohttp
import pandas as pd
from environs import env
from pydantic import BaseModel

from parsetron.utils.AddressAnalyzer.geocoder import NominatimGeocoder, FetchDto
from parsetron.utils.AddressAnalyzer.parser import AddressParser, extract_address_parts
from parsetron.utils.AddressAnalyzer.preparation_strategies import (
    BasePartsStrategy,
    BaseRawStrategy,
)

logger = logging.getLogger(__name__)


class AddressAnalyzerDto(BaseModel):
    concurrent_tasks: int
    http_conn_limit: int
    http_conn_timeout: int
    max_retries: int


def split_address(
    text: Optional[str], types: set[str]
) -> tuple[Optional[str], Optional[str]]:
    if not text:
        return None, None

    for t in types:
        pattern = rf"\b{re.escape(t)}\b"
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            start, end = match.span()
            prefix = text[:start].strip()
            suffix = text[end:].strip()
            remaining = f"{prefix} {suffix}".strip()
            return remaining, t

    return text.strip(), None


class AddressAnalyzer:
    RE_BUILDING = re.compile(r"^(?:дом)?\s*(\d\S*|\d[\s-]\S$)", re.IGNORECASE)
    RE_BUILDING_NESTED = re.compile(r"\bдом\s+(\d\S*|\d[\s-]\S$)", re.IGNORECASE)
    RE_FLAT = re.compile(r"\bквартира\s+(\d+)", re.IGNORECASE)
    RE_CORPUS = re.compile(r" к\.?\s*(\d+\S\b|\S\b)", re.IGNORECASE)
    RE_CORPUS_REPLACE = re.compile(r" к\.?\s*(?=(\d+|[a-zA-Zа-яА-ЯёЁ]))", re.IGNORECASE)
    RE_STR_REPLACE = re.compile(r" с\.?\s*(?=(\d+|[a-zA-Zа-яА-ЯёЁ]\b))", re.IGNORECASE)
    RE_CORPUS_DIGIT_REPLACE = re.compile(r" к\.?\s*(?=\d+)", re.IGNORECASE)
    RE_STR_DIGIT_REPLACE = re.compile(r" с\.?\s*(?=\d+)", re.IGNORECASE)
    RE_FLOOR = re.compile(r"\bэтаж\s+(\d+)", re.IGNORECASE)
    RE_OFFICE = re.compile(r"\bофис\s+(\S+)", re.IGNORECASE)

    def __init__(self, dto: AddressAnalyzerDto) -> None:
        self._dto = dto
        self._parser = AddressParser()

        geo_url = env("GEO_API_HOSTS")
        address_preparation_strategies = [BaseRawStrategy(), BasePartsStrategy()]
        self._geocoder = NominatimGeocoder(
            geo_url=geo_url,
            max_retries=self._dto.max_retries,
            strategies=address_preparation_strategies,
        )

    async def _process(self, data: list[FetchDto]) -> tuple[FetchDto]:
        connector = aiohttp.TCPConnector(limit=self._dto.http_conn_limit)
        semaphore = asyncio.Semaphore(self._dto.concurrent_tasks)

        async with aiohttp.ClientSession(
            connector=connector,
            timeout=aiohttp.ClientTimeout(total=self._dto.http_conn_timeout),
        ) as session:
            tasks = [
                self._geocoder.fetch_address(session, addr, semaphore) for addr in data
            ]
            results = await asyncio.gather(*tasks)
        return results

    def _extract_basic_location(self, prepared_parts: dict) -> dict:
        location = {}
        if prepared_parts.get("level"):
            match = self.RE_FLOOR.search(prepared_parts.get("level"))
            if match:
                location["floor"] = match.group(1)
        if prepared_parts.get("unit"):
            unit = prepared_parts["unit"]
            match = self.RE_FLAT.search(unit)
            if match:
                location["flat"] = match.group(1)
            match = self.RE_OFFICE.search(unit)
            if match:
                location["office"] = match.group(1)
        if prepared_parts.get("house_number") and not location.get("house"):
            match = self.RE_CORPUS.search(prepared_parts["house_number"])
            if match:
                location["corpus"] = match.group(1).upper()
            match = self.RE_BUILDING.search(prepared_parts["house_number"])
            if match:
                location["house"] = match.group(1).upper().replace(" ", "")
        elif prepared_parts.get("road") and " дом " in prepared_parts.get("road"):
            match = self.RE_CORPUS.search(prepared_parts["road"])
            if match:
                location["corpus"] = match.group(1).upper()
            match = self.RE_BUILDING_NESTED.search(prepared_parts["road"])
            if match:
                location["house"] = match.group(1).upper().replace(" ", "")
        return location

    def _enrich_location_from_response(
        self, location: dict, address_parts: dict, prepared_parts: dict
    ):
        if not address_parts:
            return

        if (
            address_parts.get("house_number")
            and prepared_parts.get("house_number")
            and address_parts.get("lat")
            and address_parts.get("lon")
        ):
            house_number = (
                prepared_parts.get("house_number")
                .replace("дом", "")
                .replace(".", "")
                .strip()
                .lower()
            )
            response_house_number = (
                address_parts.get("house_number").replace(" ", "").lower()
            )
            location["house_number"] = house_number
            if response_house_number == house_number.replace(" ", ""):
                location["coordinates"] = [address_parts["lon"], address_parts["lat"]]
                match = self.RE_CORPUS.search(address_parts.get("house_number"))
                if match:
                    location["corpus"] = match.group(1).upper()
                match = self.RE_BUILDING.search(address_parts.get("house_number"))
                if match:
                    location["house"] = match.group(1).upper()
                prepared_parts["house_number"] = self.RE_CORPUS_REPLACE.sub(
                    " корпус ",
                    self.RE_STR_REPLACE.sub(
                        " строение ", address_parts.get("house_number")
                    ),
                )
            elif response_house_number == house_number.replace("/", "").replace(
                "-", ""
            ).replace(" ", ""):
                location["coordinates"] = [address_parts["lon"], address_parts["lat"]]
                match = self.RE_CORPUS.search(address_parts.get("house_number"))
                if match:
                    location["corpus"] = match.group(1).upper()
                match = self.RE_BUILDING.search(address_parts.get("house_number"))
                if match:
                    location["house"] = match.group(1).upper()
                prepared_parts["house_number"] = self.RE_CORPUS_REPLACE.sub(
                    " корпус ",
                    self.RE_STR_REPLACE.sub(
                        " строение ", address_parts.get("house_number")
                    ),
                )
            else:
                logger.warning(
                    f"Response house number: `{address_parts.get("house_number")}` does not match with parsed house number: `{prepared_parts.get("house_number")}`"
                )
        if address_parts.get("road"):
            location["street_value"], location["street_type"] = split_address(
                self._parser.clean_processed(address_parts.get("road")),
                {
                    "улица",
                    "проспект",
                    "проезд",
                    "бульвар",
                    "набережная",
                    "переулок",
                    "шоссе",
                    "тупик",
                    "площадь",
                },
            )
        elif address_parts.get("alternative_road"):
            location["street_value"] = self._parser.clean_processed(
                address_parts.get("alternative_road")
            )

        settlement_keys = ["city", "town", "village", "hamlet", "county"]
        for key in settlement_keys:
            if address_parts.get(key):
                if key == "city":
                    location["settlement_value"], location["settlement_type"] = (
                        split_address(
                            self._parser.clean_processed(address_parts["city"]),
                            {"городской округ", "город"},
                        )
                    )
                    if not location["settlement_type"]:
                        location["settlement_type"] = "город"
                elif key == "county":
                    location["settlement_value"], location["settlement_type"] = (
                        split_address(
                            self._parser.clean_processed(address_parts["county"]),
                            {
                                "район",
                                "муниципальный округ",
                                "городской округ",
                                "город",
                            },
                        )
                    )
                    if not location["settlement_type"]:
                        location["settlement_type"] = "город"
                else:
                    location["settlement_value"] = self._parser.clean_processed(
                        address_parts[key]
                    )
                break

        if address_parts.get("city_district"):
            location["settlement_region_value"], location["settlement_region_type"] = (
                split_address(
                    self._parser.clean_processed(address_parts["city_district"]),
                    {"район", "округ", "территориальное управление"},
                )
            )
        if address_parts.get("state"):
            location["region_value"], location["region_type"] = split_address(
                self._parser.clean_processed(address_parts["state"]),
                {
                    "область",
                    "край",
                    "автономный округ",
                    "Автономная Республика",
                    "Республика",
                },
            )
            if (
                location["region_type"]
                and location["region_type"] == "Автономная Республика"
            ):
                location["region_type"] = "Республика"

    def _build_formatted_address(self, location: dict, prepared_parts: dict) -> str:
        order = [
            "region_type",
            "region_value",
            "settlement_type",
            "settlement_value",
            "settlement_region_type",
            "settlement_region_value",
            "street_type",
            "street_value",
        ]

        address_segments = [location[k] for k in order if k in location]
        if prepared_parts.get("house_number"):
            house_number = prepared_parts["house_number"].replace("дом", "").strip()
            if house_number and " " not in house_number:
                house_number = house_number.upper()
            house_number = f"дом {house_number}"
            address_segments.append(house_number)
        if prepared_parts.get("unit"):
            flat_number = prepared_parts["unit"].strip()
            address_segments.append(flat_number)

        return " ".join(filter(None, address_segments))

    def _prepare_result(self, dto: FetchDto) -> dict:
        output_dict = {
            "raw": dto.raw,
            "type": dto.address_type,
            "address": None,
            "location": None,
        }

        location = self._extract_basic_location(dto.prepared_parts)
        address_parts = dto.response or {}

        if address_parts and not address_parts.get("error"):
            self._enrich_location_from_response(
                location, address_parts, dto.prepared_parts
            )
            output_dict["address"] = self._build_formatted_address(
                location, dto.prepared_parts
            )
        elif dto.extended_raw:
            output_dict["address"] = self.RE_CORPUS_DIGIT_REPLACE.sub(
                " корпус ",
                self.RE_STR_DIGIT_REPLACE.sub(
                    " строение ",
                    dto.extended_raw.replace("г.", "город")
                    .replace("ул.", "улица")
                    .replace("к.", "корпус")
                    .replace("с.", "строение"),
                ),
            )
        if location:
            output_dict["location"] = location
        return output_dict

    def _prepare_row(
        self, raw: str, address: str, address_type: int
    ) -> Optional[FetchDto]:
        if not raw:
            return None
        cleaned = self._parser.clean(address)
        if not cleaned:
            return None

        expanded = self._parser.expand(cleaned)
        if not self._parser.is_address_part_present(expanded):
            return FetchDto(
                raw=raw,
                extended_raw=expanded,
                address_type=address_type,
            )

        prepared = extract_address_parts(expanded)
        is_api_call_required = bool(
            "road" in prepared
            and ("city" in prepared or "state" in prepared or "road" in prepared)
        )

        return FetchDto(
            raw=raw,
            extended_raw=expanded,
            prepared_parts=prepared,
            address_type=address_type,
            is_api_call_required=is_api_call_required,
        )

    def geocode(
        self, raw_address: pd.Series, address: pd.Series, address_type: pd.Series
    ) -> pd.Series:
        dtos = [
            self._prepare_row(raw_address[i], address[i], address_type[i])
            for i in range(len(raw_address))
        ]
        tasks_to_run = []
        results_map = {}

        for idx, dto in enumerate(dtos):
            if dto is None:
                results_map[idx] = None
            elif not dto.is_api_call_required:
                results_map[idx] = self._prepare_result(dto)
            else:
                tasks_to_run.append((idx, dto))

        if tasks_to_run:
            batch_dtos = [item[1] for item in tasks_to_run]

            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                api_results = loop.run_until_complete(self._process(batch_dtos))
                loop.close()
                for i, res in enumerate(api_results):
                    results_map[tasks_to_run[i][0]] = self._prepare_result(res)
            except Exception as e:
                logger.error(f"Async batch processing failed: {e}", exc_info=True)
                for idx, _ in tasks_to_run:
                    if idx not in results_map:
                        results_map[idx] = None
        return pd.Series(
            [[results_map[i]] for i in range(len(raw_address))], index=raw_address.index
        )
