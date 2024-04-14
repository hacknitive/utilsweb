from fastapi import Request, status
from fastapi.exceptions import RequestValidationError

from src.setting.setting import FAST_API_APP

from utilsfastapi.utilsfastapi.response.custom_orjson_response import ProjectJSONResponse as Response
from utilsfastapi.utilsfastapi.response.get_message import get_message

HTTP_422_UNPROCESSABLE_ENTITY = status.HTTP_422_UNPROCESSABLE_ENTITY


@FAST_API_APP.exception_handler(RequestValidationError)
async def handler_4_validation_error(
        request: Request,
        exc: RequestValidationError,
) -> Response:
    error = list()
    exe_error = exc.errors()
    for i in exe_error:
        field_name = i["loc"][-1]

        if isinstance(field_name, int):
            field_name = str(i["loc"][0])

        error_message = await get_equivalent_error_message(
            message_name=i["msg"],
            message_kwargs=None,
            language="farsi",  # TODO: Hardcode!!!
        )

        error.append({field_name: error_message})

    return Response(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        success=False,
        data=None,
        error=error,
        message=get_message(
            message_name="failure_message",
            message_kwargs=None,
            language="farsi",  # TODO: Hardcode!!!
        )
    )


async def get_equivalent_error_message(
        message_name,
        message_kwargs: dict | None = None,
        language: str = "farsi",
) -> str:
    if language == "english":
        return message_name

    try:
        return get_message(
            message_name=message_name,
            message_kwargs=message_kwargs,
            language=language,
        )

    except Exception:
        return message_name
