from traceback import format_exc

from fastapi import status
from beanie.odm.operators.find.comparison import In

from src.setting.setting import logger
from fastapi_addons.exception_handling import ProjectBaseException
from fastapi_addons.utility.get_message import get_message
from .document import ServiceAuthenticationDocument as Document

HTTP_401_UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED


async def find_service_authentication(
        method_path: str,
        hashed_api_key: str,
) -> Document:
    try:
        obj = await Document.find_one(
            Document.hashed_api_key == hashed_api_key,
            Document.is_locked == False,
            In(Document.allowed_method_path, [method_path, "*"]),
        )

        if obj is not None:
            return obj

    except Exception:
        logger.error(format_exc())

    logger.error(f"Unauthorized access")

    error = get_message("unauthorized_service")

    raise ProjectBaseException(
        status_code=HTTP_401_UNAUTHORIZED,
        success=False,
        data=None,
        error=error,
        message=error,
    )
