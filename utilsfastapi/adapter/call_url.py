from typing import Any
from traceback import format_exc
from json import dumps

from aiohttp import ClientSession
from fastapi import status
from utilscommon.utilscommon.setting import EnumRunMode

from .exception import (
    Service503Exception,
    UpperThan300Exception,
)

HTTP_503_SERVICE_UNAVAILABLE = status.HTTP_503_SERVICE_UNAVAILABLE


async def call_url(
        method: str,
        url: str,
        headers: dict | None = None,
        json: dict | None = None,
        raise_: bool = True,
        error_message: str = None,
        run_mode: EnumRunMode = None,
) -> Any:
    try:
        async with ClientSession() as session:
            async with session.request(
                    method=method,
                    url=url,
                    json=json,
                    headers=headers
            ) as response:
                result = await response.json()

    except Exception:
        if run_mode == EnumRunMode.production:
            error = error_message
        else:
            error = format_exc()

        raise Service503Exception(
            status_code=HTTP_503_SERVICE_UNAVAILABLE,
            success=False,
            data=None,
            error=error,
            message=error_message,
            log_this_exc=True,
        )

    if raise_:
        if response.status >= 300:
            if run_mode == EnumRunMode.production:
                error = error_message
            else:
                error = await response.text()

            raise UpperThan300Exception(
                status_code=result.get("status_code") or response.status,
                success=False,
                data=result.get("data"),
                error=error,
                message=error,
            )

    return result
