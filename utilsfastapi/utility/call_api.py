from typing import Any
from traceback import format_exc

from aiohttp import ClientSession
from fastapi import status

from src.setting.setting import RUN_MODE, enum

from ..exception_handling import ProjectBaseException
from ..utility.get_message import get_message

HTTP_503_SERVICE_UNAVAILABLE = status.HTTP_503_SERVICE_UNAVAILABLE
ERROR_TEXT = get_message("internal_server_error")


async def call_api(
        method: str,
        url: str,
        headers: dict | None = None,
        data: dict | None = None,
        raise_: bool = True,
) -> Any:
    try:
        async with ClientSession() as session:
            async with session.request(
                    method=method,
                    url=url,
                    json=data,
                    headers=headers
            ) as response:
                result = await response.json()

    except Exception:
        if RUN_MODE == enum.EnumRunMode.production:
            error = ERROR_TEXT
        else:
            error = format_exc()

        raise ProjectBaseException(
            code=HTTP_503_SERVICE_UNAVAILABLE,
            success=False,
            data=None,
            error=error,
            message=ERROR_TEXT,
            log_this_exc=True,
        )

    if raise_:
        if response.status >= 300:
            raise ProjectBaseException(
                code=result.get("code") or response.status,
                success=False,
                data=result.get("data"),
                error=result.get("message"),
                message=result.get("message"),
            )

    return result
