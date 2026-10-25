from natasha import (
    MorphVocab,
    NamesExtractor,
)

from pullenti_wrapper.langs import set_langs, RU

set_langs([RU])
morph_vocab = MorphVocab()
names_extractor = NamesExtractor(morph_vocab)


class NamesExtractor:
    def extract_name(name_str):
        try:
            matches = names_extractor(name_str)
            if not matches:
                return None

            facts = [match.fact.as_json for match in matches]
            if not facts:
                return None

            max_key_count = max(len(fact) for fact in facts)
            best_facts = [fact for fact in facts if len(fact) == max_key_count]

            if not best_facts:
                return None

            best_fact = best_facts[0]

            first = best_fact.get("first")
            last = best_fact.get("last")
            middle = best_fact.get("middle")

            parts = []
            if last and len(last) >= 3:
                parts.append(last)
            if first and len(first) >= 3:
                parts.append(first)
            if middle and len(middle) >= 3:
                parts.append(middle)

            full_name = " ".join(parts).strip()
            return full_name if full_name else None

        except Exception as e:
            print(f"Error occurred during parsing name with Natasha: {e}")
            return None
