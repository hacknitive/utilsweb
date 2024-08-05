from typing import (
    Callable,
    Type,
)
from zipfile import (
    ZipFile,
    ZIP_DEFLATED,
)
from io import BytesIO
from datetime import datetime

from fastapi import status
from .fetch_by_file import (
    fetch_by_file,
    LITERAL_FILE_FORMAT,
    FILE_FORMAT_EXTENSION_DICT,
)
from utilscommon.exception import ProjectBaseException


async def group_by_by_file_complete(
        file_format: LITERAL_FILE_FORMAT,
        group_by_attributes: list[str],

        fetch_func: Callable,
        unacceptable_file_format_exception: Type[ProjectBaseException] | ProjectBaseException,

        current_page: int,
        page_size: int,
        order_by: dict | None,

        **kwargs,
) -> dict:
    files_to_add = dict()
    extension = FILE_FORMAT_EXTENSION_DICT[file_format]
    for i in group_by_attributes:
        data = await fetch_func(
            inputs=kwargs,
            group_by_on=[i],
            order_by=order_by,
            current_page=current_page,
            page_size=page_size,
        )
        result = fetch_by_file(
            file_format=file_format,
            file_name="Complete",  # Not important
            data=data,
            unacceptable_file_format_exception=unacceptable_file_format_exception
        )

        files_to_add[f"{i}.{extension}"] = result['content']

    return _create_zipfile(files_to_add=files_to_add)


def _create_zipfile(files_to_add: dict[str, BytesIO]):
    now = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
    file_name = f"group-by-complete-{now}.zip"
    folder_name = f"group-by-complete-{now}/"

    zip_stream = BytesIO()
    with ZipFile(zip_stream, "w", ZIP_DEFLATED) as zip_file:
        for filename, content in files_to_add.items():
            zip_file.writestr(f"{folder_name}{filename}", content.getvalue())

    zip_stream.seek(0)

    return {
        'media_type': "application/zip",
        'content': zip_stream,
        'status_code': status.HTTP_200_OK,
        'headers': {"Content-Disposition": f"attachment; filename={file_name}"},
    }
