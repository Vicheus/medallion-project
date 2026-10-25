import logging
import re
from bisect import bisect_left
from typing import Optional

from postal.parser import parse_address

logger = logging.getLogger(__name__)

PRIORITY_GEO_TYPES = [
    "unit",
    "level",
    "entrance",
    "house_number",
    "road",
    "city",
    "suburb",
    "state_district",
    "state",
    "postcode",
    "country_region",
    "country",
]


def _group_tokens_by_type(
    address_tokens: list[tuple[str, str]],
) -> dict[str, list[int]]:
    type_to_indices = {}
    for idx, (_, field_type) in enumerate(address_tokens):
        if field_type not in type_to_indices:
            type_to_indices[field_type] = []
        type_to_indices[field_type].append(idx)
    return type_to_indices


def _find_closest_index(target_indices: list[int], anchor_idx: int) -> int:
    """
    Performs a radial search to find the index in target_indices closest to anchor_idx. Uses 'Left First' tie-breaking
    """
    pos = bisect_left(target_indices, anchor_idx)
    candidates = []

    if pos < len(target_indices):
        candidates.append((abs(target_indices[pos] - anchor_idx), target_indices[pos]))
    if pos > 0:
        candidates.append(
            (abs(target_indices[pos - 1] - anchor_idx), target_indices[pos - 1])
        )
    return min(candidates)[1]


def _determine_initial_anchor(
    type_to_indices: dict[str, list[int]], priority_order: list[str]
) -> Optional[int]:
    """Finds the best starting index based on proximity to the second priority type."""
    first_key = next((p for p in priority_order if p in type_to_indices), None)
    if not first_key:
        return None

    potential_seeds = type_to_indices[first_key]
    next_relevant_type = next(
        (p for p in priority_order[1:] if p in type_to_indices), None
    )

    if len(potential_seeds) > 1 and next_relevant_type:
        ref_indices = type_to_indices[next_relevant_type]

        def score_seed(seed_idx):
            pos = bisect_left(ref_indices, seed_idx)
            distances = []
            if pos < len(ref_indices):
                distances.append((abs(ref_indices[pos] - seed_idx), ref_indices[pos]))
            if pos > 0:
                distances.append(
                    (abs(ref_indices[pos - 1] - seed_idx), ref_indices[pos - 1])
                )
            return min(distances) if distances else (float("inf"), 0)

        return min(potential_seeds, key=score_seed)

    return potential_seeds[0]


def extract_address_parts(text: Optional[str]) -> dict[str, str]:
    if not text:
        return {}
    address_tokens = parse_address(text)
    if not address_tokens:
        return {}

    type_to_indices = _group_tokens_by_type(address_tokens)
    current_anchor_idx = _determine_initial_anchor(type_to_indices, PRIORITY_GEO_TYPES)
    result_values = {}
    for target_key in PRIORITY_GEO_TYPES:
        if target_key not in type_to_indices:
            continue
        indices = type_to_indices[target_key]

        if current_anchor_idx is None:
            found_idx = indices[0]
        else:
            found_idx = _find_closest_index(indices, current_anchor_idx)

        val, _ = address_tokens[found_idx]
        result_values[target_key] = val
        current_anchor_idx = found_idx

    return result_values


class AddressParser:
    RE_START_CHARS = re.compile(
        r"[ЇїІіЄєҐґ]|^[a-z0-9][a-z0-9_.+-]*@[a-z0-9-]+\.[a-z0-9-.]+$",
        flags=re.IGNORECASE,
    )
    RE_CLEAN_PARENTHESIS = re.compile(r"\([^)]*\)")
    # RE_BACKSLASH_TO_SLASH = re.compile(r"(\d{1,2})\\(?=\d{1,2})")
    RE_KEEP_ALPHANUM = re.compile(r"[^a-zA-Zа-яА-ЯёЁ0-9\s\-/]")
    RE_REMOVE = re.compile(r"\s+/\b|\b/\s+")
    RE_STRIP_SEPARATORS = re.compile(r"[ /\-]+")
    RE_ONLY_DIGITS = re.compile(r"^\d+$")
    RE_START_DIGIT = re.compile(r"^\d")
    RE_6_DIGITS = re.compile(r"^\d{6}$")
    RE_REPEATING_DIGITS = re.compile(r"\b(\d)\1{3,}\b")
    RE_MULTI_SPACE = re.compile(r"\s+")
    RE_BUILDING_FLAT = re.compile(
        r"\b((дом|участок|микрорайон)?\s*\d{1,3}[абвгдАБВГД]?)[\s-]+(\d{1,3})(?:[\s-]+(\d{1,3}))?$"
    )
    RE_STOPWORDS = re.compile(
        r"^(no|test|null|none|тест|нету?|[a-f0-9]{8}\\-[a-f0-9]{4}\\-[a-f0-9]{4}\\-[a-f0-9]{4}\\-[a-f0-9]{12})$"
    )
    ADDRESS_PARTS = {
        "г.",
        "ул.",
        "д.",
        "микрорайон",
        "деревня",
        "область",
        "край",
        "набережная",
        "пгт",
        "переулок",
        "поселение",
        "поселок",
        "проспект",
        "район",
        "республика",
        "село",
        "тупик",
        "шоссе",
        "бульвар",
    }

    def __init__(self):
        _mappings = {
            r"(?<!\d)[ -]*\b(д(ом)?|зд(ание)?|влд)\s*(?=\d)": " дом ",
            r"\b((домо)?владение|двлд)\b": " дом ",
            r"\bс п\b": " сельское поселение ",
            r"(?<!\d)[ -]*\bп\b": " поселение ",
            r"\b(б-р|бульв)\b": " бульвар ",
            r"\b(пос[её]лок гор(одского)? типа|п г т|пгт)\b": " поселок городского типа ",
            r"\bпр-д\b": " проезд ",
            r"\b(пр-к?т|пр(осп)?)\b": " проспект ",
            r"\bг ?п\b": " городское поселение ",
            r"\bр ?п\b": " районное поселение ",
            r"\bг(ор(од)?)?\b": " г. ",
            r"\bдер\b": " деревня ",
            r"\bкв(артира)?\s*(?=\d)": " квартира ",
            r"\bкв-л\b": " квартал ",
            r"\bкор(п(ус)?)?\s*(?=(\d+|[a-zA-Zа-яА-ЯёЁ]))\b": " к. ",
            r"\bм ?р(-н)?\b": " муниципальный район ",
            r"\b(мкрн?|мик-он)\b": " микрорайон ",
            r"\bнаб\b": " набережная ",
            r"\bобл(аст)\b": " область ",
            r"\bпер\b": " переулок ",
            r"\bпос([её]лок)?\b": " поселок ",
            r"\bр-о?н\b": " район ",
            r"\bресп\b": " республика ",
            r"\bс\s+(?=[А-Яа-яЁё]{2,})": " село ",
            r"\bстр(оен(ие)?)?\b": " с. ",
            r"\bтуп\b": " тупик ",
            r"\bул(ица)?\b": " ул. ",
            r"\bхутор\b": " хутор ",
            r"\bш\b": " шоссе ",
            r"\bж/р\b": " жилой район ",
            r"\bст-ца\b": " станица ",
            r"\bпл\b": " площадь ",
            r"\bим\b": " имени ",
            r"\bуч(-к)?\b": " участок ",
            r"\bтер\b": "територия",
            r"\bком(ната)?\s*(?=\d)": " комната ",
            r"\bпомещ\s*(?=\d)": " помещение ",
        }
        self.pattern_to_replacement = {}
        group_patterns = []

        for i, (pattern, replacement) in enumerate(_mappings.items()):
            group_name = f"p{i}"
            self.pattern_to_replacement[group_name] = replacement
            group_patterns.append(f"(?P<{group_name}>{pattern})")
        self.master_regex = re.compile(
            "|".join(group_patterns), flags=re.IGNORECASE | re.MULTILINE
        )

    def clean(self, text: Optional[str]) -> Optional[str]:
        if not text or self.RE_START_CHARS.match(text):
            return None

        cleaned = self.RE_CLEAN_PARENTHESIS.sub(" ", text)
        cleaned = self.RE_KEEP_ALPHANUM.sub(" ", cleaned)
        cleaned = self.RE_REMOVE.sub(" ", cleaned)
        if not cleaned:
            return None

        compacted = self.RE_STRIP_SEPARATORS.sub("", cleaned.lower())
        if len(set(compacted)) < 2 or self.RE_STOPWORDS.match(compacted):
            return None
        if self.RE_ONLY_DIGITS.match(compacted) and not self.RE_6_DIGITS.match(cleaned):
            return None

        cleaned = self.RE_REPEATING_DIGITS.sub(" ", cleaned)
        cleaned = self.RE_MULTI_SPACE.sub(" ", cleaned)
        return cleaned.strip(" /-")

    def clean_processed(self, text: Optional[str]) -> Optional[str]:
        if not text or self.RE_START_CHARS.match(text):
            return None

        cleaned = self.RE_CLEAN_PARENTHESIS.sub(" ", text)
        cleaned = self.RE_KEEP_ALPHANUM.sub(" ", cleaned)
        cleaned = self.RE_MULTI_SPACE.sub(" ", cleaned).strip(" /-")
        return cleaned if cleaned else None

    def expand(self, text: Optional[str]) -> Optional[str]:
        if not text:
            return None

        def _replacement_callback(match):
            return self.pattern_to_replacement[match.lastgroup]

        def _replacement_building_flat(match):
            n1, n2, n3 = match.groups()
            n1 = n1.strip()
            if self.RE_START_DIGIT.match(n1):
                n1 = f"дом {n1}"
            if n3:
                return f"{n1} к{n2} квартира {n3}"
            return f"{n1} квартира {n2}"

        replaced = self.master_regex.sub(_replacement_callback, text).strip()
        cleaned = self.RE_MULTI_SPACE.sub(" ", replaced)
        # if not (" дом " in cleaned or " квартира " in cleaned or " к. " in cleaned or " с. " in cleaned):
        #     cleaned = self.RE_BUILDING_FLAT.sub(_replacement_building_flat, cleaned)
        return cleaned

    def is_address_part_present(self, text: Optional[str]) -> bool:
        if not text:
            return False
        text_words = set(text.split())
        return not self.ADDRESS_PARTS.isdisjoint(text_words)
