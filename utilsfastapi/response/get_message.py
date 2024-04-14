from re import subn
import string

SUBSTITUTION_PATTERN = r"\{[^\{\}]+\}"


def prepare_get_message_function(
        messages_dict: dict,
        substitution_pattern: str = SUBSTITUTION_PATTERN,
):
    def get_message(
            message_name,
            message_kwargs: dict | None = None,
            language: str = "farsi",
    ) -> str:
        message_kwargs = message_kwargs or dict()
        message = messages_dict[language]

        formatted_message = string.Formatter().vformat(message[message_name], [], _SafeFormat(**message_kwargs))

        return _clean_message(
            substitution_pattern=substitution_pattern,
            string_=formatted_message,
        )

    return get_message


class _SafeFormat(object):
    def __init__(self, **kw):
        self.__dict = kw

    def __getitem__(self, name):
        return self.__dict.get(name, '{%s}' % name)


def _clean_message(
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
