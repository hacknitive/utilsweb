from typing import Callable
from traceback import format_exc
from logging import Logger

from fastapi import (
    Request,
    FastAPI,
)
from utilsconfigloader.utilsconfigloader.utils.enum import EnumRunMode
from utilscommon.utilscommon.exception import ProjectBaseException

from ..response.custom_orjson_response import ProjectJSONResponse as Response
from .create_traceback import create_traceback


def prepare_handler_for_project_base_exception_function(
        fast_api_app: FastAPI,
        logger: Logger,
        run_mode: EnumRunMode,
        get_message_func: Callable,
        error_lang: str = 'english',
):
    error_text = get_message_func(
        message_name="failure_message",
        message_kwargs=None,
        language=error_lang,
    )

    async def handler_for_project_base_exception(
            request: Request,
            exc: ProjectBaseException
    ) -> Response:
        if exc.status_code >= 500:
            if getattr(
                    exc,
                    "log_this_exc",
                    True,
            ):
                traceback_ = await create_traceback(
                    exc=exc,
                    request=request,
                    traceback_=format_exc(),
                )
                logger.error(msg=traceback_)

            status_code = exc.status_code
            success = False
            data = None
            message = error_text

            if run_mode == EnumRunMode.production:
                error = error_text
            else:
                error = exc.error

        else:
            status_code = exc.status_code
            success = exc.success
            data = exc.data
            error = exc.error
            message = exc.message

        return Response(
            status_code=status_code,
            success=success,
            data=data,
            error=error,
            message=message
        )

    fast_api_app.exception_handler(ProjectBaseException)(handler_for_project_base_exception)
