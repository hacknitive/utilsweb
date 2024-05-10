import string

from .safe_format import SafeFormat
from .clean_message import clean_message
from .substitution_pattern import SUBSTITUTION_PATTERN


class Message:
    _default_language = None
    _substitution_pattern = None

    def __init__(
            self,
            default_language: str,
            substitution_pattern: str = SUBSTITUTION_PATTERN
    ) -> None:
        Message._default_language = default_language
        Message._substitution_pattern = substitution_pattern

    @classmethod
    def __getattribute__(cls, item, *args, **kwargs):
        return cls._wrapper(item)

    @classmethod
    def _wrapper(cls, item):
        def prepare_message(language=cls._default_language, **kwargs):
            message_dict = getattr(cls, item)
            message_text = message_dict[language]

            formatted_message = string.Formatter().vformat(message_text, [], SafeFormat(**kwargs))

            return clean_message(
                substitution_pattern=cls._substitution_pattern,
                string_=formatted_message,
            )

        return prepare_message
