import json
from parsetron.sections.base.validators.base import base_raw_validation


def raw_metadata(*args):
    if len(args) % 2 != 0:
        return None

    try:
        keys = args[::2]
        values = args[1::2]
        result = {}

        for k, v in zip(keys, values):
            if v not in [None, "None", "null", "NULL"]:
                v = base_raw_validation(v)
                if v:
                    result[k] = v

        if not result:
            return None

        return json.dumps(result, ensure_ascii=False)
    except Exception:
        return None
