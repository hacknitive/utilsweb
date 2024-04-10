from traceback import format_exc

from fastapi import Request, status

from src.setting.setting import FAST_API_APP, logger, RUN_MODE, enum

from ..utility.custom_orjson_response import ProjectJSONResponse as Response
from ..utility.get_message import get_message
from ..utility.create_traceback import create_traceback

ERROR_TEXT = get_message(
    message_name="internal_server_error",
    message_kwargs=None,
    language="farsi",  # TODO: Hardcode!!!
)


def handler_4_5xx_creator(error: int) -> callable:
    if RUN_MODE == enum.EnumRunMode.production:
        async def handler_4_5xx(
                request: Request,
                exc: Exception
        ) -> Response:
            if getattr(exc, "log_this_exc", True):
                traceback_ = await create_traceback(
                    exc=exc,
                    request=request,
                    traceback_=format_exc(),
                )
                logger.error(msg=traceback_)

            return Response(
                status_code=error,
                success=False,
                data=None,
                error=ERROR_TEXT,
                message=ERROR_TEXT,
            )

    else:
        async def handler_4_5xx(
                request: Request,
                exc: Exception
        ) -> Response:
            traceback_ = await create_traceback(exc=exc,
                                                request=request,
                                                traceback_=format_exc(),
                                                )

            if getattr(exc, "log_this_exc", True):
                logger.error(msg=traceback_)

            return Response(
                status_code=error,
                success=False,
                data=None,
                error=traceback_,
                message=ERROR_TEXT,
            )

    return handler_4_5xx


exceptions = (
    status.HTTP_500_INTERNAL_SERVER_ERROR,
    status.HTTP_501_NOT_IMPLEMENTED,
    status.HTTP_502_BAD_GATEWAY,
    status.HTTP_503_SERVICE_UNAVAILABLE,
    status.HTTP_504_GATEWAY_TIMEOUT,
    status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED,
    status.HTTP_506_VARIANT_ALSO_NEGOTIATES,
    status.HTTP_507_INSUFFICIENT_STORAGE,
    status.HTTP_508_LOOP_DETECTED,
    status.HTTP_510_NOT_EXTENDED,
    status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED,
)

for exception in exceptions:
    FAST_API_APP.exception_handler(exception)(handler_4_5xx_creator(error=exception))
