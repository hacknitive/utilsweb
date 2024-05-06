from traceback import format_exc

from fastapi.security import APIKeyHeader
from fastapi import Depends, Request, status
from beanie import Document

from src.setting.setting import logger
from fastapi_addons.exception_handling import ProjectBaseException
from fastapi_addons.utility.get_message import get_message

from ...utility.hash_api_key import hash_api_key
from .find_service_authentication import find_service_authentication

X_SERVICE_API_KEY = APIKeyHeader(
    name="Allowed-Secret",
    auto_error=True,
    scheme_name="Allowed-Secret",
)

HTTP_401_UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED


async def authenticate_service(
        request: Request,
        api_key: str = Depends(X_SERVICE_API_KEY),
) -> Document:
    try:
        method = request.scope["method"]
        path = request.scope["route"].path

        hashed_api_key = await hash_api_key(api_key=api_key)

    except Exception:
        logger.error(format_exc())

        error = get_message("unauthorized_service")
        raise ProjectBaseException(
            status_code=HTTP_401_UNAUTHORIZED,
            success=False,
            data=None,
            error=error,
            message=error,
        )

    return await find_service_authentication(
        method_path=f"{method.upper()}:{path}",
        hashed_api_key=hashed_api_key,
    )
