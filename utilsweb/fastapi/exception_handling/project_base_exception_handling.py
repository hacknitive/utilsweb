from traceback import format_exc
from logging import Logger

from fastapi import (
    Request,
    FastAPI,
)
from utilscommon.setting import EnumRunMode
from utilscommon.exception import ProjectBaseException

from ..response.custom_orjson_response import ProjectJSONResponse as Response
from .create_traceback import create_traceback


def prepare_handler_for_project_base_exception_function(
        fast_api_app: FastAPI,
        logger: Logger,
        run_mode: EnumRunMode,
):
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
            message = str(exc.message) if exc.message else None

            if run_mode == EnumRunMode.production:
                error = message
            else:
                error = str(exc.error) if exc.error else None

        else:
            status_code = exc.status_code
            success = exc.success
            data = exc.data
            error = str(exc.error) if exc.error else None
            message = str(exc.message) if exc.message else None

        return Response(
            status_code=status_code,
            success=success,
            data=data,
            error=error,
            message=message
        )

    fast_api_app.exception_handler(ProjectBaseException)(handler_for_project_base_exception)
