from re import subn
import string

from src.dto.const_and_enum.message import MESSAGES

SUBSTITUTION_PATTERN = r"\{[^\{\}]+\}"

SUPPORTED_LANGUAGES = ("english", "farsi")


def get_message(
        message_name,
        message_kwargs: dict | None = None,
        language: str = "farsi",
) -> str:
    message_kwargs = message_kwargs or dict()
    message = MESSAGES[language]

    formatted_message = string.Formatter().vformat(message[message_name], [], SafeFormat(**message_kwargs))

    return clean_message(string_=formatted_message)


class SafeFormat(object):
    def __init__(self, **kw):
        self.__dict = kw

    def __getitem__(self, name):
        return self.__dict.get(name, '{%s}' % name)


def clean_message(string_):
    string_, count = subn(
        pattern=SUBSTITUTION_PATTERN,
        repl="",
        string=string_,
    )

    for i in range(count):
        string_ = string_.replace("  ", " ").replace("''", "").replace('""', "")
        string_ = string_.replace("  ", " ").replace("''", "").replace('""', "")

    return string_
