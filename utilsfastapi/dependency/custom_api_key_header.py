from typing import Optional

from fastapi import Request
from fastapi.security.api_key import APIKeyBase
from fastapi.openapi.models import (
    APIKey,
    APIKeyIn,
)


class CustomAPIKeyHeader(APIKeyBase):
    def __init__(
            self,
            *,
            name: str,
            scheme_name: Optional[str] = None,
            description: Optional[str] = None,
            auto_error: bool = True,
            exception: Exception = Exception
    ):
        self.model: APIKey = APIKey(
            **{"in": APIKeyIn.header},  # type: ignore[arg-type]
            name=name,
            description=description,
        )
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error
        self.exception = exception

    async def __call__(
            self,
            request: Request,
    ) -> Optional[str]:
        api_key = request.headers.get(self.model.name)
        if not api_key:
            if self.auto_error:
                raise self.exception

            else:
                return None
        return api_key
