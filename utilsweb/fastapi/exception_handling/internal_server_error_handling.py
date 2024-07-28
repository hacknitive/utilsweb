from logging import Logger
from traceback import format_exc

from fastapi import (
    Request,
    status,
    FastAPI,
)

try:
    from utilscommon.utilscommon.setting import EnumRunMode
except ImportError:
    from utilscommon.utilscommon.setting import EnumRunMode

from ..response.custom_orjson_response import ProjectJSONResponse as Response
from .create_traceback import create_traceback


def prepare_handler_for_5xx_creator_function(
        fast_api_app: FastAPI,
        logger: Logger,
        run_mode: EnumRunMode,
        error_text: str,
):
    def prepare_handler_for_5xx(error: int) -> callable:
        if run_mode == EnumRunMode.production:
            async def handler_for_internal_server_error(
                    request: Request,
                    exc: Exception
            ) -> Response:
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

                return Response(
                    status_code=error,
                    success=False,
                    data=None,
                    error=error_text,
                    message=error_text,
                )

        else:
            async def handler_for_internal_server_error(
                    request: Request,
                    exc: Exception
            ) -> Response:
                traceback_ = await create_traceback(
                    exc=exc,
                    request=request,
                    traceback_=format_exc(),
                )

                if getattr(
                        exc,
                        "log_this_exc",
                        True,
                ):
                    logger.error(msg=traceback_)

                return Response(
                    status_code=error,
                    success=False,
                    data=None,
                    error=traceback_,
                    message=error_text,
                )

        return handler_for_internal_server_error

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
        fast_api_app.exception_handler(exception)(prepare_handler_for_5xx(error=exception))
