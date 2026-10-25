from airportsdata import load
from transliterate import translit
import cachetools
from ..settings import RU_AIRPORTS_SLAVIC_CODES, RU_AIRPORTS_IATA

cache = cachetools.TTLCache(maxsize=128, ttl=60 * 180)


def get_airports(allowed_country_codes):
    airports = cache.get("airports")
    if not airports:
        airports = []
        all_airports = load("IATA")
        for airport in all_airports.items():
            _, info = airport
            if allowed_country_codes and (info["country"] not in allowed_country_codes):
                continue
            airports.append(airport)
        cache["airports"] = airports

    return airports


def get_movement_airport_code_by_name(
    name, name_stopwords, allowed_country_codes, min_words_in_name=1
):
    value = cache.get(name)

    if name not in cache:
        airports = get_airports(allowed_country_codes)

        if (not name) or (not airports):
            return None

        name_parts = name.split(" ")
        if len(name_parts) < min_words_in_name:
            return None

        for code, info in airports:
            if allowed_country_codes and (info["country"] not in allowed_country_codes):
                continue
            for name_part in name_parts:
                if name_stopwords and (name_part in name_stopwords):
                    continue
                if (
                    translit(name_part, "ru", reversed=True).lower()
                    in info["name"].lower()
                ):
                    value = code
    cache[name] = value

    return value


def get_movement_airport_iata_code_by_slavic_code(slavic_code):
    if not slavic_code:
        return None
    airport_data = RU_AIRPORTS_SLAVIC_CODES.get(slavic_code)
    if not airport_data:
        return None
    return airport_data["IATA"]


def get_movement_airport_city_by_slavic_code(slavic_code):
    if not slavic_code:
        return None
    airport_data = RU_AIRPORTS_SLAVIC_CODES.get(slavic_code)
    if not airport_data:
        return None
    return airport_data["City"]


def get_movement_airport_city_by_IATA_code(IATA_code):
    if not IATA_code:
        return None
    airport_data = RU_AIRPORTS_IATA.get(IATA_code)
    if not airport_data:
        # assume that value is city
        if len(IATA_code) > 3:
            return IATA_code
        return None
    return airport_data["City"]
