from re import subn


def clean_message(
        substitution_pattern,
        string_,
):
    string_, count = subn(
        pattern=substitution_pattern,
        repl="",
        string=string_,
    )

    for i in range(count):
        string_ = string_.replace("  ", " ").replace("''", "").replace('""', "")
        string_ = string_.replace("  ", " ").replace("''", "").replace('""', "")

    return string_
