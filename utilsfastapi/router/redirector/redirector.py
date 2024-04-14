from fastapi.responses import RedirectResponse

from .router import router


@router.get(
    path="/",
    include_in_schema=False,
)
async def docs_redirect():
    return RedirectResponse(
        url='/docs',
        status_code=308,
    )
