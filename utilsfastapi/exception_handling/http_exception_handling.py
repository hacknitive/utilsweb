from traceback import format_exc

from fastapi import Request
from fastapi.exceptions import HTTPException
from starlette.exceptions import HTTPException as Starlette_exc

from src.setting.setting import FAST_API_APP, logger

from ..utility.custom_orjson_response import ProjectJSONResponse as Response
from ..utility.create_traceback import create_traceback
from ..utility.get_message import get_message


async def handler_4_http_exception(
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
        message=get_message(
            message_name="failure_message",
            message_kwargs=None,
            language="farsi",  # TODO: Hardcode!!!
        )
    )


FAST_API_APP.exception_handler(HTTPException)(handler_4_http_exception)
FAST_API_APP.exception_handler(Starlette_exc)(handler_4_http_exception)
