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
        class MessageClass:
            cache = None
            def __init__(
                    self,
                    language=cls._default_language,
                    **kwargs,
            ):

                self.language = language
                self.kwargs = kwargs

            def __str__(self):
                if self.cache:
                    return self.cache

                message_dict = getattr(cls, item)
                message_text = message_dict[self.language]

                formatted_message = string.Formatter().vformat(message_text, [], SafeFormat(**self.kwargs))

                self.cache = clean_message(
                    substitution_pattern=cls._substitution_pattern,
                    string_=formatted_message,
                )

                return self.cache

            def __repr__(self):
                return self.__str__()

        return MessageClass
