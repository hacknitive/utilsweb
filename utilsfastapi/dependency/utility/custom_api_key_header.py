from typing import Optional

from fastapi.security.api_key import APIKeyBase
from fastapi.openapi.models import APIKey, APIKeyIn
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from utilsfastapi.utilsfastapi.response.get_message import get_message
from ...exception_handling import ProjectBaseException


error = get_message("unauthorized_user")


class CustomAPIKeyHeader(APIKeyBase):
    def __init__(
            self,
            *,
            name: str,
            scheme_name: Optional[str] = None,
            description: Optional[str] = None,
            auto_error: bool = True,
    ):
        self.model: APIKey = APIKey(
            **{"in": APIKeyIn.header},  # type: ignore[arg-type]
            name=name,
            description=description,
        )
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error

    async def __call__(self, request: Request) -> Optional[str]:
        api_key = request.headers.get(self.model.name)
        if not api_key:
            if self.auto_error:
                raise ProjectBaseException(
                    code=HTTP_403_FORBIDDEN,
                    success=False,
                    data=None,
                    error=error,
                    message=error,
                )

            else:
                return None
        return api_key
