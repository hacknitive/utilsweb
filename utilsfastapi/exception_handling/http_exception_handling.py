from typing import Callable
from logging import Logger
from traceback import format_exc

from fastapi import (
    Request,
    FastAPI,
)
from fastapi.exceptions import HTTPException
from starlette.exceptions import HTTPException as Starlette_exc

from utilsfastapi.utilsfastapi.response.custom_orjson_response import ProjectJSONResponse as Response
from utilsfastapi.utilsfastapi.exception_handling.create_traceback import create_traceback


def prepare_handler_for_http_exception_function(
        fast_api_app: FastAPI,
        logger: Logger,
        get_message_func: Callable,
        error_lang: str = 'english',
) -> None:
    error_text = get_message_func(
        message_name="failure_message",
        message_kwargs=None,
        language=error_lang,
    )

    async def handler_for_http_exception(
            request: Request,
            exc: HTTPException
    ) -> Response:
        if getattr(
                exc,
                "log_this_exc",
                False
        ):
            traceback_ = await create_traceback(
                exc=exc,
                request=request,
                traceback_=format_exc(),
            )
            logger.error(traceback_)

        return Response(
            status_code=exc.status_code,
            success=False,
            data=None,
            error=exc.detail,
            message=error_text,
        )

    fast_api_app.exception_handler(HTTPException)(handler_for_http_exception)
    fast_api_app.exception_handler(Starlette_exc)(handler_for_http_exception)
