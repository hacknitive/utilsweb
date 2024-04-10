from traceback import format_exc

from fastapi import Request

from src.setting.setting import FAST_API_APP, logger, RUN_MODE, enum

from .project_base_exception import ProjectBaseException
from ..utility.custom_orjson_response import ProjectJSONResponse as Response
from ..utility.create_traceback import create_traceback
from ..utility.get_message import get_message

ERROR_TEXT = get_message(
    message_name="failure_message",
    message_kwargs=None,
    language="farsi",  # TODO: Hardcode!!!
)


@FAST_API_APP.exception_handler(ProjectBaseException)
async def handler_4_project_base_exception(
        request: Request,
        exc: ProjectBaseException
) -> Response:
    if exc.code >= 500:
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

        status_code = exc.code
        success = False
        data = None
        message = ERROR_TEXT

        if RUN_MODE == enum.EnumRunMode.production:
            error = ERROR_TEXT
        else:
            error = exc.error

    else:
        status_code = exc.code
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
