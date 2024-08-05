from json import dumps
from datetime import datetime
from io import BytesIO

from fastapi import status
from fastapi.encoders import jsonable_encoder

MEDIA_TYPE = 'application/json'


def generate_json(
        file_name: str,
        data: dict,
) -> dict:
    now = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
    file_name = f"{file_name}-Result-{now}.json"

    file_in_string = dumps(
        jsonable_encoder(data),
        sort_keys=True,
        indent=4,
    )

    file_in_bytes = bytes(
        file_in_string,
        encoding='utf-8',
    )
    file_in_bytesio = BytesIO(file_in_bytes)

    return {
        'media_type': MEDIA_TYPE,
        'content': file_in_bytesio,
        'status_code': status.HTTP_200_OK,
        'headers': {"Content-Disposition": f"attachment; filename={file_name}"},
    }
