import logging
import re
from abc import ABC, abstractmethod
from typing import Optional

from parsetron.utils.AddressAnalyzer.dto import FetchDto


logger = logging.getLogger(__name__)


class AddressPreparationStrategy(ABC):
    RE_PARTS = re.compile(
        r"\b(г\.( |$)|ул\.( |$)|дом|квартира|деревня|область|край|автономный округ|(сельское|городское)? ?поселение|проспект|проезд|територия|а о|поселок( городского типа)?|(муниципальный|жилой)? ?район|республика|село|в/ч|(военная|войсковая)\s*часть|хутор|\.)\b",
        re.IGNORECASE,
    )
    RE_MULTI_SPACE = re.compile(r"\s+")
    RE_CLEAN_PARENTHESIS = re.compile(r"\([^)]*\)")
    RE_KEEP_ALPHANUM = re.compile(r"[^a-zA-Zа-яА-ЯёЁ0-9\s\-/]")
    RE_START_CHARS = re.compile(r"[ЇїІіЄєҐґ]", flags=re.IGNORECASE)

    @abstractmethod
    def prepare_address(self, data: FetchDto) -> str:
        pass

    def _is_ua_symbol(self, text: Optional[str]) -> bool:
        return not text or bool(self.RE_START_CHARS.match(text))

    def _prepare_answer(self, response: dict, address: str) -> dict:
        result = {}
        if self._is_ua_symbol(response.get("display_name")):
            result["error"] = response.get("display_name")
            logger.warning(
                f"Not allowed symbols in address: `{result["error"]}` for `{address}`"
            )
            return result
        response_address = response.get("address", {})
        result["road"] = response_address.get("road")
        result["alternative_road"] = (
            response_address.get("neighbourhood")
            or response_address.get("allotments")
            or response_address.get("quarter")
            or response_address.get("suburb")
        )
        # if not result["road"] and not result["alternative_road"]:
        #     logger.warning(
        #         f"Missed a road in response `{str(response_address)}` for: `{address}`"
        #     )
        result["house_number"] = response_address.get("house_number")
        result["city"] = response_address.get("city")
        result["town"] = response_address.get("town")
        result["village"] = response_address.get("village")
        result["hamlet"] = response_address.get("hamlet")
        result["county"] = response_address.get("county")
        result["city_district"] = response_address.get("city_district")
        result["state"] = response_address.get("state")
        result["postcode"] = response_address.get("postcode")
        result["country"] = response_address.get("country")
        result["lat"] = float(response.get("lat")) if response.get("lat") else None
        result["lon"] = float(response.get("lon")) if response.get("lon") else None
        return result

    def prepare_response(self, address: str, response_json: list) -> Optional[dict]:
        if not address or not response_json:
            return None

        if len(response_json) == 1:
            return self._prepare_answer(response_json[0], address)
        elif len(response_json) > 1:
            index = -1
            response = {}
            response_road = None
            response_city = None
            for i in range(len(response_json)):
                response = self._prepare_answer(response_json[i], address)
                response_road = response["road"] or response["alternative_road"]
                response_city = (
                    response["city"]
                    or response["town"]
                    or response["village"]
                    or response["hamlet"]
                    or response["county"]
                )
                if response_road or response_city:
                    index = i
                    break
            if index == -1 and len(response_json) - 1 > index:
                return response
            lats = {response.get("lat")} if response.get("lat") else set()
            lons = {response.get("lon")} if response.get("lon") else set()
            postcodes = (
                {response.get("postcode")} if response.get("postcode") else set()
            )
            house_numbers = (
                {response.get("house_number")}
                if response.get("house_number")
                else set()
            )

            for i in range(index + 1, len(response_json)):
                next_response = self._prepare_answer(response_json[i], address)
                next_response_road = (
                    next_response["road"] or next_response["alternative_road"]
                )
                next_response_city = (
                    next_response["city"]
                    or next_response["town"]
                    or next_response["village"]
                    or next_response["hamlet"]
                    or next_response["county"]
                )
                if not next_response_road or not next_response_city:
                    continue

                if not response_road and next_response_road:
                    response["road"] = next_response.get("road")
                    response["alternative_road"] = next_response.get("alternative_road")
                elif next_response_road and response_road != next_response_road:
                    road_err = f"Ambiguous road in response from address: {address}. Response 1: `{response}`, Response 2: `{next_response}`"
                    # logger.warning(road_err)
                    return {"error": road_err}
                if not response["city_district"] and next_response["city_district"]:
                    response["city_district"] = next_response["city_district"]
                elif (
                    next_response["city_district"]
                    and response["city_district"] != next_response["city_district"]
                ):
                    city_district_err = f"Ambiguous city_district in response from address: {address}. Response 1: `{response}`, Response 2: `{next_response}`"
                    # logger.warning(city_district_err)
                    return {"error": city_district_err}
                if not response_city and next_response_city:
                    response["city"] = next_response.get("city")
                    response["town"] = next_response.get("town")
                    response["village"] = next_response.get("village")
                    response["hamlet"] = next_response.get("hamlet")
                    response["county"] = next_response.get("county")
                elif next_response_city and response_city != next_response_city:
                    city_err = f"Ambiguous city in response from address: {address}. Response 1: `{response}`, Response 2: `{next_response}`"
                    # logger.warning(city_err)
                    return {"error": city_err}
                if not response["state"] and next_response["state"]:
                    response["state"] = next_response["state"]
                elif (
                    next_response["state"]
                    and response["state"] != next_response["state"]
                ):
                    state_err = f"Ambiguous state in response from address: {address}. Response 1: `{response}`, Response 2: `{next_response}`"
                    # logger.warning(state_err)
                    return {"error": state_err}
                if not response["country"] and next_response["country"]:
                    response["country"] = next_response["country"]
                elif (
                    next_response["country"]
                    and response["country"] != next_response["country"]
                ):
                    country_err = f"Ambiguous country in response from address: {address}. Response 1: `{response}`, Response 2: `{next_response}`"
                    # logger.warning(country_err)
                    return {"error": country_err}

                if next_response["lat"]:
                    lats.add(next_response["lat"])
                if next_response["lon"]:
                    lons.add(next_response["lon"])
                if next_response["postcode"]:
                    postcodes.add(next_response["postcode"])
                if next_response["house_number"]:
                    house_numbers.add(next_response["house_number"])

        result = response
        result["lat"] = list(lats)[0] if len(lats) == 1 else None
        result["lon"] = list(lons)[0] if len(lons) == 1 else None
        result["postcode"] = list(postcodes)[0] if len(postcodes) == 1 else None
        result["house_number"] = (
            list(house_numbers)[0] if len(house_numbers) == 1 else None
        )

        return result


class BaseRawStrategy(AddressPreparationStrategy):
    def prepare_address(self, data: FetchDto) -> str:
        address = ""
        if data.extended_raw and "house_number" in data.prepared_parts:
            address = re.sub(
                rf"(\b{data.prepared_parts["house_number"]}\b).*",
                r"\1",
                data.extended_raw,
                flags=re.DOTALL | re.IGNORECASE,
            )
            address = self.RE_PARTS.sub(" ", address)
            address = self.RE_MULTI_SPACE.sub(" ", address).strip()
        return address


class BasePartsStrategy(AddressPreparationStrategy):
    def prepare_address(self, data: FetchDto) -> str:
        address = ""
        if "road" in data.prepared_parts and "city" not in data.prepared_parts:
            return address
        if "road" in data.prepared_parts:
            address = data.prepared_parts["road"]
        if "house_number" in data.prepared_parts:
            house = data.prepared_parts["house_number"]
            address = f"{address} {house}"
        if "city" in data.prepared_parts:
            city = data.prepared_parts["city"]
            address = f"{city} {address}"
        if "state" in data.prepared_parts:
            city = data.prepared_parts["state"]
            address = f"{city} {address}"
        if "country" in data.prepared_parts:
            address = f"{data.prepared_parts["country"]} {address}"
        if address:
            address = self.RE_PARTS.sub("", address)
            address = self.RE_MULTI_SPACE.sub(" ", address)
        return address.strip()
