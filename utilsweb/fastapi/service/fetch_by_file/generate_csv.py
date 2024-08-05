from datetime import datetime
from csv import DictReader, DictWriter
from io import (
    TextIOWrapper,
    StringIO,
    BytesIO,
)

from fastapi import status
from utilscommon import make_flat

MEDIA_TYPE = 'application/csv'


def generate_csv(
        file_name: str,
        data: dict,
) -> dict:
    now = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
    file_name = f"{file_name}-Result-{now}.csv"

    in_memory_file = StringIO()

    flat_data = [
        make_flat(
            data=data['pagination'],
            key="pagination"
        ),
        *[make_flat(i) for i in data['data']]
    ]

    headers = set()
    for i in flat_data:
        headers.update(set(i.keys()))
    headers = list(headers)
    headers.sort()

    writer = DictWriter(
        in_memory_file,
        fieldnames=headers,
    )
    writer.writeheader()

    for i in flat_data:
        writer.writerow(i)

    file_in_string = in_memory_file.getvalue()
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
