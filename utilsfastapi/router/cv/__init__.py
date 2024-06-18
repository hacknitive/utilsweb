from fastapi import APIRouter

from utilsfastapi.utilsfastapi.response.custom_orjson_response import ProjectJSONResponse as JsonResponse

router = APIRouter(
    prefix='/raghamCv/sWSj4PT38h/gUPBq5DKaC/YGLLlLHax1',
)


@router.get(
    path="",
    include_in_schema=False,
)
async def fetch() -> JsonResponse:
    return JsonResponse(**{
        'status_code': 200,
        'success': True,
        'message': "The operation is done successfully.",
        'error': None,
        'data': {
            'name': "Reza Aghamohammadi (ragham)",
            'email': "re.agha.mo@gmail.com",
            'phone': "+989376478609",
            "project_name": "Data Management System (D.M.S)",
            "role": "Backend Developer",
            "starts_at": "2024-04-13",
        }
    })
