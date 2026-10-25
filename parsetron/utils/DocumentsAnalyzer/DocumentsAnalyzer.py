import re
import json

# from ollama import Client


class DocumentsAnalyzer:
    """ """

    def __init__(self):
        # self._client = Client(
        #    host=AGENT_HOSTS
        # )
        return

    def identify_document_features(self, document_raw):
        prompt = self._get_extract_document_features_prompt(document_raw)
        response = self._client.chat(
            model="aya-expanse:32b",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )

        data = self._create_json(response.message.content)

        return data

    def _get_extract_document_features_prompt(self, document_raw):
        prompt = f"""
    You - agent, which should read user input about some document and extract from this user input strict document features
    Your task - extract from user input document features and return them as json object with following fields:

    {{
    "document_series": "",           // Document number
    "document_issued_at": "",        // Document issue date
    "document_issued_by": "",        // Document issue organisation
    "document_issued_by_code": ""    // Document issue organisation code
    }}

    Example:
    4514 952807 09.12.2014 отделением УФМС России по городу Москве по району Крюково -> {{"document_series": "4514 952807", "document_issued_at": "09.12.2014", "document_issued_by": "отделением УФМС России по городу Москве по району Крюково", "document_issued_by_code": "" }}
    4515 170413 -> {{"document_series": "4515 170413", "document_issued_at": "", "document_issued_by": "", "document_issued_by_code": "" }}
    4513115766 Москва ОВДАлексеевский -> {{"document_series": "4513115766", "document_issued_at": "", "document_issued_by": "Москва ОВДАлексеевский", "document_issued_by_code": "" }}
    III-МЮ № 749978 05.09.2007 Перовский отд. ЗАГС Управления ЗАГС г. Москвы -> {{"document_series": "III-МЮ749978", "document_issued_at": "05.09.2007", "document_issued_by": "Перовский отд. ЗАГС Управления ЗАГС г. Москвы", "document_issued_by_code": "" }}
    45 11 416974, 06.02.2012, 770-042 -> {{"document_series": "45 11 416974", "document_issued_at": "06.02.2012", "document_issued_by": "", "document_issued_by_code": "770-042" }}

    Text for analysis:

    <<<
    {document_raw}
    >>>

    In response include ONLY json object, no other text or explanation. If you'll find more than one feature of some type - include them most relevant
    """
        return prompt

    def _create_json(self, content):
        cleaned = re.sub(r"```(?:json)?\s*(.*?)\s*```", r"\1", content, flags=re.DOTALL)
        content = cleaned.strip()
        try:
            data = json.loads(content)
            return data
        except json.JSONDecodeError:
            return {}
