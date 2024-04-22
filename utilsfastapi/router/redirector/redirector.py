from fastapi.responses import RedirectResponse

from .router import router


@router.get(
    path="/",
    include_in_schema=False,
    response_class=RedirectResponse,
    status_code=308,
)
async def docs_redirect() -> RedirectResponse:
    return RedirectResponse(
        url='/docs',
        status_code=308,
    )
