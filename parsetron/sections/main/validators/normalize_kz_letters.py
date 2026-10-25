def normalize_kz_letters(s):
    if s is None:
        return None
    replacements = {
        "Ә": "А",
        "ә": "а",
        "Ғ": "Г",
        "ғ": "г",
        "Қ": "К",
        "қ": "к",
        "Ң": "Н",
        "ң": "н",
        "Ө": "О",
        "ө": "о",
        "Ұ": "У",
        "ұ": "у",
        "Ү": "У",
        "ү": "у",
        "І": "И",
        "і": "и",
        "Һ": "Х",
        "һ": "х",
    }

    table = str.maketrans(replacements)

    return s.translate(table)
