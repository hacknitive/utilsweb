from typing import Callable
from datetime import datetime
from csv import DictReader, DictWriter
from io import (
    TextIOWrapper,
    StringIO,
    BytesIO,
)

from fastapi import (
    UploadFile,
    status,
)
from pydantic import BaseModel
from utilscommon.exception import ProjectBaseException


async def create_by_file(
        file: UploadFile,
        core_func: Callable,
        request_model: type[BaseModel],
        response_model: type[BaseModel],
        unacceptable_file_format_exception: type[Exception] | Exception,
) -> dict:
    if file.content_type == 'text/csv':
        media_type = 'application/csv'
        now = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
        file_name = file.filename.rsplit('.', 1)[0] + f"-Result-{now}.csv"

        reader = DictReader(TextIOWrapper(
            file.file,
            encoding='utf-8-sig',
        ))

        in_memory_file = StringIO()

        writer = DictWriter(
            in_memory_file,
            fieldnames=(
                *(i for i in request_model.__fields__.keys()),
                *(i for i in response_model.__fields__.keys()),
                'error',
            ),
        )
        writer.writeheader()

        try:
            for line in reader:

                try:
                    model = request_model(**line)
                    result = await core_func(model=model)
                    prepared_result = response_model(**result).model_dump()
                except Exception as e:
                    error = getattr(e, 'error', None) or e

                    prepared_result = {
                        **line,
                        'error': str(error).replace("\n", " #NEWLINE "),
                    }

                writer.writerow(prepared_result)

        except Exception as e:
            error = getattr(e, 'error', None) or e
            error = str(error).replace("\n", " #NEWLINE ")

            raise ProjectBaseException(
                status_code=status.HTTP_400_BAD_REQUEST,
                success=False,
                data=None,
                error=error,
                message=error,
            )

        file_in_string = in_memory_file.getvalue()
        file_in_bytes = bytes(
            file_in_string,
            encoding='utf-8',
        )
        file_in_bytesio = BytesIO(file_in_bytes)

    elif file.content_type == 'application/json':
        media_type = 'application/json'
        now = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
        file_name = file.filename.rsplit('.', 1)[0] + f"-Result-{now}.json"

        data = load(file.file)

        results = list()

        for data_i in data:
            try:
                model = RequestModel(**data_i)
                result = await create(model=model)
                result = result.data.model_dump()

            except Exception as e:
                error = getattr(e, 'error', None) or e
                result = {
                    **data_i,
                    'error': str(error).replace("\n", " #NEWLINE "),
                }

            results.append(result)

        results = jsonable_encoder(results)
        file_in_string = dumps(results)
        file_in_bytes = bytes(
            file_in_string,
            encoding='utf-8',
        )
        file_in_bytesio = BytesIO(file_in_bytes)
    else:
        raise unacceptable_file_format_exception

    return {
        'media_type': media_type,
        'content': file_in_bytesio,
        'status_code': status.HTTP_200_OK,
        'headers': {"Content-Disposition": f"attachment; filename={file_name}"},
    }
