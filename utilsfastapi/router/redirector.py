from fastapi.responses import RedirectResponse

from src.setting.setting import FAST_API_APP


@FAST_API_APP.get(
    path="/",
    include_in_schema=False,
)
async def docs_redirect():
    return RedirectResponse(
        url='/docs',
        status_code=308,
    )
