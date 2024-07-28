from traceback import format_exc
from re import subn
from logging import Logger

from fastapi import (
    FastAPI,
    Request,
    status,
)
from fastapi.exceptions import RequestValidationError
from utilsfastapi.utilsfastapi.response.custom_orjson_response import ProjectJSONResponse as Response

from ..response.message import PreparedMessage as _PreparedMessage
from .validation_regex_message_dict import VALIDATION_REGEX_MESSAGE_DICT
from .validation_error_message_cache import validation_error_message_cache

HTTP_422_UNPROCESSABLE_ENTITY = status.HTTP_422_UNPROCESSABLE_ENTITY


def prepare_handler_for_validation_errors_function(
        fast_api_app: FastAPI,
        logger: Logger,
        prepared_message: _PreparedMessage = _PreparedMessage,
        error_language: str = 'english',
):
    failure_text = prepared_message.failure_message(language=error_language)

    async def handler_for_validation_error(
            request: Request,
            exc: RequestValidationError,
    ) -> Response:
        exe_error = exc.errors()
        try:
            for i in exe_error:
                i['orginal_msg'] = i['msg']
                i['msg'] = translate(
                    error_msg=i['msg'],
                    error_language=error_language,
                    logger=logger,
                )
        except Exception:
            logger.warning(
                "Exception occurred when translating this error message: %s \n %s",
                exe_error,
                format_exc(),
            )

        return Response(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            success=False,
            data=None,
            error=exe_error,
            message=failure_text,
        )

    fast_api_app.exception_handler(RequestValidationError)(handler_for_validation_error)


def translate(
        error_msg: str,
        logger: Logger,
        error_language: str,
):
    cache_key = f"{error_language}_{error_msg}"
    if cache_key in validation_error_message_cache:
        return validation_error_message_cache[cache_key]

    for key, value in VALIDATION_REGEX_MESSAGE_DICT.items():
        try:
            output_msg, count = subn(
                key,
                value[error_language],
                error_msg,
            )
            if count:
                validation_error_message_cache[cache_key] = output_msg
                return output_msg

        except Exception:
            logger.warning(
                "Exception occurred when translating by this regex: %s \n %s",
                key,
                format_exc(),
            )

    logger.warning("Cannot find translation for this error message: %s", error_msg)

    try:
        with open("cannot_translate.txt", "a", encoding='utf-8') as handler:
            handler.write(f"{error_msg}\n")
    except Exception:
        logger.warning(format_exc())

    return error_msg
