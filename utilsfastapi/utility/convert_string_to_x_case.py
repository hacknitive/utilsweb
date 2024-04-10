from enum import Enum

SPLIT_CHARS = (
    "-",
    "_",
    " ",
)
REPLACE_CHAR = "@$#"


class EnumCase(str, Enum):
    camel = "camel"
    pascal = "pascal"


def convert_string_to_x_case(
        string: str,
        split_chars: tuple = SPLIT_CHARS,
        replace_char: str = REPLACE_CHAR,
        case: EnumCase = EnumCase.camel,
):
    for i in split_chars:
        string = string.replace(i, replace_char)

    string = string.split(replace_char)

    result = ""
    counter = 1
    for index in range(len(string)):
        current = string[index].strip()
        if current:
            if counter == 1:
                if case == EnumCase.camel:
                    result += current.lower()

                elif case == EnumCase.pascal:
                    result += current.title()
            else:
                result += current.title()
            counter += 1

    return result
