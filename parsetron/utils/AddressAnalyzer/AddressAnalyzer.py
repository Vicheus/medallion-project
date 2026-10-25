from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    AddrExtractor,
    Doc,
)

import csv
import re
import cachetools
import requests

from pullenti_wrapper.langs import set_langs, RU
from pullenti_wrapper.processor import Processor, GEO, ADDRESS
from pullenti_wrapper.referent import Referent
from parsetron.settings import (
    ADDRESS_ANALYZER_GEO_ENTITY_DICTIONARY_PATH,
    GEO_API_HOSTS,
    ANALYZER_API_HOSTS,
    SEARCH_COORDINATES
)

cache = cachetools.TTLCache(maxsize=128, ttl=60 * 180)

set_langs([RU])
cache = cachetools.TTLCache(maxsize=128, ttl=60 * 180)
processor = Processor([GEO, ADDRESS])
segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)
addr_extractor = AddrExtractor(morph_vocab)

geo_entities = {}


class AddressAnalyzer:
    """
    The AddressAnalyzer class is designed to analyze address strings and normalize it to structured format.
    Adress analyzer works in 4 normalization steps:
    1.Extract LOCATION entities from address string using Pullenti lib, which also do search using ГАР ФИАС
    addresses db
    2.Extract LOCATION entities using Natasha lib and try to find them in already existing geo entities dictionary
    THis allow to enrich address string with correct abbreviations like г. ул. бул. etc for future second parsing
    3.Extract LOCATION entities from enriched address string using Pullenti
    4.Union results from steps 1-3 to prepare as much as possible strict address object

    Key functionalities of the class include:
    - Address string parsing and normalization.
    - Transformation of normalized address object to formatted string.
    """

    def __init__(self):
        self.segmenter = Segmenter()
        self.ner_tagger = NewsNERTagger(emb)
        self.geo_entities = {}  # self._read_and_cache_geo_entity_dictionary()

    def normalize_address(self, raw, address, address_type):
        def validate_normalized_address(normalized_address):
            location = normalized_address.get("location", {})
            required_fields = [
                "region_value",
                "settlement_region_value",
                "settlement_value",
                "street_value",
            ]
            if all(not location.get(field) for field in required_fields):
                return None

            if (
                (normalized_address.get("type") is None)
                or not normalized_address.get("raw")
                or not normalized_address.get("address")
            ):
                return None

            return normalized_address

        if not address:
            return None
        address = self._cleanup_address_string(address)

        # first iteration - parse address string with Pullenti lib
        address_dict_pullenti_first_iter = self._process_address_with_pullenti(
            self, address
        )
        # extract location entities and try to find it in own dictionaries if not found yet
        address = self._enrich_address_using_geo_entity_dictionary(
            self, address, address_dict_pullenti_first_iter
        )
        # second iteration - parse address string with Pullenti lib after enrichment
        address_dict_pullenti_second_iter = self._process_address_with_pullenti(
            self, address
        )
        # third iteration - problematic addresses also try to parse with Natasha lib after enrichment
        address_dict_natasha = self._process_address_with_natasha(self, address)

        normalized_address_dict = (
            address_dict_natasha
            | address_dict_pullenti_second_iter
            | address_dict_pullenti_first_iter
        )

        normalized_address_dict = self._remove_duplicates_with_priority(
            normalized_address_dict,
            ["город", "село", "поселок", "посёлок", "городское поселение"],
        )

        normalized_address_dict = self._remove_duplicates_with_priority(
            normalized_address_dict,
            [
                "улица",
                "проспект",
                "бульвар",
                "набережная",
                "шоссе",
                "переулок",
                "проезд",
                "тупик",
            ],
        )

        normalized_address = self._transform_normalized_address(
            raw, normalized_address_dict, address_type
        )

        if not validate_normalized_address(normalized_address):
            return None

        return normalized_address

    @staticmethod
    def _transform_normalized_address(raw, address_dict, address_type):
        def transform_normalized_address_to_string(input_dict):
            priority_order = [
                "индекс",
                "республика",
                "область",
                "край",
                "город",
                "муниципальный район",
                "городское поселение",
                "деревня",
                "поселок городского типа",
                "посёлок",
                "посeлок",
                "село",
                "район",
                "микрорайон",
                "массив",
                "улица",
                "проезд",
                "переулок",
                "шоссе",
                "проспект",
                "бульвар",
                "тупик",
                "набережная",
                "дом",
                "строение",
                "подъезд",
                "корпус",
                "этаж",
                "квартира",
                "офис",
            ]
            result = []

            for key in priority_order:
                if key in input_dict:
                    result.append(f"{key} {input_dict[key]}")

            return " ".join(result).strip()

        def get_coordinates(address):
            settlement = address.get("settlement_value", "")
            street = address.get("street_value", "")
            house = address.get("house", "")
            if (settlement == "") and (street != ""):
                return None
            if (settlement == "") and (street == "") and (house != ""):
                return None
            if (settlement != "") and (street == "") and (house != ""):
                house = ""
            url = f"{GEO_API_HOSTS}search?city={settlement}&street={street} {house}"
            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    if len(data) == 0:
                        return None
                    location = data[0]
                    if not location:
                        return

                    lat = location.get("lat", "")
                    lon = location.get("lon", "")

                    lat = float(lat) if lat else None
                    lon = float(lon) if lon else None

                    if (not lat) or (not lon):
                        return None

                    coordinates = [lon, lat]

                    return coordinates
                else:
                    return None
            except Exception as e:
                print(f"""Error during Open street map api call: {e}""")
                return None

        def get_coordinates_detail_level(address: dict) -> int:
            if address.get("settlement_region_value") and not any(
                [
                    address.get("settlement_value"),
                    address.get("street_value"),
                    address.get("house"),
                ]
            ):
                return 1

            if address.get("settlement_value") and not any(
                [address.get("street_value"), address.get("house")]
            ):
                return 0

            if address.get("street_value") and not address.get("house"):
                return 2

            if address.get("house"):
                return 3

            return 1

        output_dict = {}
        location = {}

        region_keys = ["область", "край", "муниципальный район", "республика"]
        for key in region_keys:
            if key in address_dict:
                location["region_type"] = key
                location["region_value"] = address_dict[key]
                break

        if "индекс" in address_dict:
            location["zip"] = address_dict["индекс"]

        settlement_region_keys = ["район", "микрорайон"]
        for key in settlement_region_keys:
            if key in address_dict:
                location["settlement_region_type"] = key
                location["settlement_region_value"] = address_dict[key]
                break

        settlement_keys = [
            "город",
            "городское поселение",
            "деревня",
            "поселок городского типа",
            "посёлок",
            "поселок",
            "село",
        ]
        for key in settlement_keys:
            if key in address_dict:
                location["settlement_type"] = key
                location["settlement_value"] = address_dict[key]
                break

        street_keys = [
            "проезд",
            "переулок",
            "шоссе",
            "проспект",
            "бульвар",
            "улица",
            "набережная",
        ]
        for key in street_keys:
            if key in address_dict:
                location["street_type"] = key
                location["street_value"] = address_dict[key]
                break

        if "дом" in address_dict:
            location["house"] = address_dict["дом"]

        if "квартира" in address_dict:
            location["flat"] = address_dict["квартира"]

        if "корпус" in address_dict:
            location["building"] = address_dict["корпус"]

        if "строение" in address_dict:
            location["building"] = address_dict["строение"]

        if "этаж" in address_dict:
            location["floor"] = address_dict["этаж"]

        if "офис" in address_dict:
            location["office"] = address_dict["офис"]

        output_dict["type"] = address_type
        output_dict["raw"] = raw
        output_dict["address"] = transform_normalized_address_to_string(address_dict)
        location["coordinates"] = get_coordinates(location) if SEARCH_COORDINATES else None
        location["coord_detalization_lvl"] = get_coordinates_detail_level(output_dict) if SEARCH_COORDINATES else None
        output_dict["location"] = location

        return output_dict

    @staticmethod
    def _cleanup_address_string(text):
        """
        Format abbreaviations in address and capitalize words after abbreviations.
        Prepare address string for better future entity recognition run
        """

        def capitalize_after_delimiters(text):
            pattern = r"([ ,;.]?)(\w{4,})"

            def capitalize_match(match):
                delimiter = match.group(1)
                word = match.group(2)
                return delimiter + word[0].upper() + word[1:].lower()

            result = re.sub(pattern, capitalize_match, text)

            result = result[0].upper() + result[1:] if result else result

            return result

        text = text.lower()
        text = capitalize_after_delimiters(text)
        text = re.sub(r"(д|ул|дом|улица|кв|квартира),", r"\1 ", text)
        text = re.sub(r"( к.| к | к, | кв. )", "кв", text)
        # replace empty index with empty string
        text = re.sub(r"00000", "", text)

        return text

    @staticmethod
    def _enrich_address_using_geo_entity_dictionary(
        self, address, found_location_spans
    ):

        def clean_location_span(input_string):
            remove_words = [
                "д." "д",
                "кв.",
                "кв",
                "ул.",
                "ул",
                "пос.",
                "пос",
                "г.",
                "г",
                "c",
                "c.",
                "гор",
                "гор.",
            ]
            parts = input_string.split(" ")

            cleaned_parts = [part for part in parts if part not in remove_words]

            cleaned_string = " ".join(cleaned_parts)

            return cleaned_string

        """
        Extract LOCATION entities from address string, also split address string by comma
        Search for LOCATION entities in geo entities dictionary
        Enrich address string with abbreaviations for found locations
        """

        def try_get_geo_entity_type(geo_entity):
            if geo_entity == "":
                return None
            url = f"{ANALYZER_API_HOSTS}api/addressEntries/by-name/?name={geo_entity}"
            try:
                response = requests.get(url)

                if response.status_code == 200:
                    data = response.json()
                    if len(data) == 0:
                        return None
                    entry = data[0]
                    if not entry:
                        return

                    type = entry.get("type", "")

                    if not type:
                        return None

                    print(f"Find type: {type} for geo entity {geo_entity}")

                    return type
                else:
                    return None
            except Exception as e:
                print(f"""Error during Address analyzer api call: {e}""")
                return None

        geo_type_abbreviations = {
            "область": "обл.",
            "муниципальный район": "м.р.",
            "городское поселение": "г.п.",
            "деревня": "д.",
            "поселок городского типа": "п.г.т.",
            "посёлок": "п.",
            "поселок": "п.",
            "район": "р-н",
            "микрорайон": "мкрн.",
            "проезд": "пр.",
            "переулок": "пер.",
            "шоссе": "шоссе",
            "проспект": "пр-т.",
            "бульвар": "бул.",
            "город": "г.",
            "улица": "ул.",
            "набережная": "наб.",
            "село": "с.",
        }
        try:
            doc = Doc(address)
            doc.segment(segmenter)
            doc.tag_morph(morph_tagger)
            doc.parse_syntax(syntax_parser)
            doc.tag_ner(ner_tagger)

            location_spans = [span.text for span in doc.spans if span.type == "LOC"]

            # also try split address string by comma\space and found parts in dictionaries
            address_split_parts = re.split(r"[,\s.]+", address)
            for part in address_split_parts:
                part = re.sub(r"[^а-яА-ЯёЁ\s]+", "", part)
                if len(part) <= 2:
                    continue
                if part not in location_spans:
                    location_spans.append(part)

            for location_span in location_spans:
                if location_span in found_location_spans.values():
                    continue
                location_span_for_search = location_span.strip().lower()
                geo_type = try_get_geo_entity_type(location_span_for_search) if SEARCH_COORDINATES else None
                if geo_type:
                    if geo_type in geo_type_abbreviations:
                        address = address.replace(
                            location_span,
                            f"{geo_type_abbreviations[geo_type]} {clean_location_span(location_span)}",
                        )
        except Exception as e:
            print(
                f"Error occurred during address string enrichment from geo entities dictionary: {e}"
            )

        return address

    @staticmethod
    def _process_address_with_natasha(self, address):
        """
        Address entities extraction using Natasha lib
        """
        natasha_address = {}

        try:
            matches = addr_extractor(address)
            facts = [i.fact.as_json for i in matches]

            for i in range(len(facts)):
                items = facts[i].items()
                data = dict(items)
                fact_type = data.get("type")
                fact_value = data.get("value")

                if (
                    (not fact_type)
                    & (fact_value != "")
                    & (fact_value is not None)
                    & (fact_value.lower() in self.geo_entities)
                ):
                    geo_entity_type = self.geo_entities[fact_value.lower()]
                    fact_type = geo_entity_type

                if (fact_value != "") & (fact_value is not None):
                    if (fact_type != "") & (fact_type is not None):
                        natasha_address[f"{fact_type}"] = f"{fact_value}"

        except Exception as e:
            print(f"Error occurred during parsing with Natasha: {e}")

        return natasha_address

    @staticmethod
    def _process_address_with_pullenti(self, address):
        """
        Address entity extraction using Pullenti lib
        """

        def parse_referent(referent, level=0):
            try:
                token_type_mapping = {
                    "zip": "индекс",
                    "республика": "республика",
                    "область": "область",
                    "муниципальный район": "муниципальный район",
                    "городское поселение": "городское поселение",
                    "деревня": "деревня",
                    "поселок городского типа": "поселок городского типа",
                    "посёлок": "посёлок",
                    "поселок": "посёлок",
                    "район": "район",
                    "микрорайон": "микрорайон",
                    "проезд": "проезд",
                    "переулок": "переулок",
                    "шоссе": "шоссе",
                    "проспект": "проспект",
                    "бульвар": "бульвар",
                    "house": "дом",
                    "flat": "квартира",
                    "corpus": "корпус",
                    "floor": "этаж",
                    "office": "офис",
                    "город": "город",
                    "улица": "улица",
                    "село": "село",
                }
                address_part = {}
                address_token_type = ""
                address_token_value = ""
                for key in referent.__shortcuts__:
                    value = getattr(referent, key)
                    if value in (None, 0, -1):
                        continue
                    if isinstance(value, Referent):
                        parse_referent(value, level + 1)
                    else:
                        if key == "type":
                            address_token_type = value
                        if key == "name":
                            address_token_value = value
                    if key in ["house", "flat", "corpus", "floor", "office", "zip"]:
                        address_token_type = token_type_mapping[key]
                        address_token_value = value
                        address_part[address_token_type] = address_token_value
                if (address_token_type != "") & (address_token_value != ""):
                    address_part[address_token_type] = address_token_value

                address_parts.append(address_part)
            except Exception as e:
                print(f"Error occurred during parsing referent from Pullenti: {e}")

        address_dict = {}
        address_parts = []
        try:
            address_processed = processor(address)

            if len(address_processed.matches) > 0:
                referent = address_processed.matches[0].referent
                parse_referent(referent)

                address_dict = {
                    k: v.lower().capitalize()
                    for d in address_parts
                    for k, v in d.items()
                }
        except Exception as e:
            print(f"Error occurred during parsing with Pullenti: {e}")

        return address_dict

    @staticmethod
    def _read_and_cache_geo_entity_dictionary():
        geo_entities = cache.get("geo_entities") or {}
        if not geo_entities:
            try:
                print("""Read geo_entities and save in RAM""")
                with open(
                    ADDRESS_ANALYZER_GEO_ENTITY_DICTIONARY_PATH,
                    mode="r",
                    newline="",
                    encoding="utf-8",
                ) as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if len(row) == 2:
                            geo_name, geo_type = row
                            geo_entities[geo_name] = geo_type

                cache["geo_entities"] = geo_entities
            except FileNotFoundError:
                print(
                    f"Error: The file {ADDRESS_ANALYZER_GEO_ENTITY_DICTIONARY_PATH} was not found."
                )
            except Exception as e:
                print(f"Error: {e}")

        return geo_entities

    @staticmethod
    def _remove_duplicates_with_priority(input_dict, priority_order):
        seen_values = set()
        result_dict = {}

        for key in priority_order:
            if key in input_dict:
                value = input_dict[key]
                if value not in seen_values:
                    result_dict[key] = value
                    seen_values.add(value)

        for key, value in input_dict.items():
            if key not in result_dict and value not in seen_values:
                result_dict[key] = value
                seen_values.add(value)

        return result_dict
