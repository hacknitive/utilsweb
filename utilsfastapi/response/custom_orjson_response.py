from typing import Optional
from copy import deepcopy

from pydantic import BaseModel
from starlette.responses import Response
from starlette.background import BackgroundTask
from orjson import dumps
from fastapi.encoders import jsonable_encoder


class ProjectJSONResponse(Response):
    media_type = "application/json"

    def __init__(  # noqa
            self,
            status_code: int,
            success: bool,
            message: str = None,
            data: None | dict | list | BaseModel = None,
            error: str | dict | list | None = None,

            headers: Optional[dict[str, str]] = None,
            media_type: Optional[str] = None,
            background: Optional[BackgroundTask] = None,
    ):
        self.status_code = status_code
        self.success = success
        self.message = message
        self.data = data
        self.error = error

        if media_type is not None:
            self.media_type = media_type
        self.background = background
        self.body = self.render()
        self.init_headers(headers)

    def render(self, content=None) -> bytes:
        return dumps(self.prepare_content())

    def prepare_content(self):
        return jsonable_encoder({
            "code": self.status_code,
            "message": self.message,
            "success": self.success,
            "data": self.data,
            "error": self.error
        })

    def deep_copy(self):
        return deepcopy(self)
