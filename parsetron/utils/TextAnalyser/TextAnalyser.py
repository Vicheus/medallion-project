from natasha import (
    Segmenter,
    NewsEmbedding,
    NewsNERTagger,
    PER,
    ORG,
    Doc,
    AddrExtractor,
    MorphVocab,
)

segmenter = Segmenter()
emb = NewsEmbedding()
ner_tagger = NewsNERTagger(emb)
morph_vocab = MorphVocab()
address_extractor = AddrExtractor(morph_vocab)


class TextAnalyser:
    def __init__(self):
        self.segmenter = Segmenter()
        self.ner_tagger = NewsNERTagger(emb)

    def is_person_or_organisation(text, threshold=0.5):
        doc = Doc(text)
        doc.segment(segmenter)
        doc.tag_ner(ner_tagger)
        person_or_org_spans = [s for s in doc.spans if (s.type == PER or s.type == ORG)]
        if not doc.spans:
            return False
        if (len(doc.spans) > 0) & (
            round(len(person_or_org_spans) / len(doc.spans), 2) > threshold
        ):
            return True

        return False

    def extract_address(text):
        if not text:
            return None
        matches = address_extractor(text)
        if not matches:
            return None
        address = (
            ", ".join(
                f"{match.fact.value}" if match.fact.value is not None else ""
                for match in matches
            )
        ) or None

        return address
