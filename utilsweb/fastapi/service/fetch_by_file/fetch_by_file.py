from typing import Literal

from .generate_csv import generate_csv
from .generate_excel import generate_excel
from .generate_json import generate_json

LITERAL_FILE_FORMAT = Literal['excel', 'csv', 'json']

FILE_FORMAT_GENERATOR_DICT = {
    'excel': generate_excel,
    'csv': generate_csv,
    'json': generate_json,
}

FILE_FORMAT_EXTENSION_DICT = {
    'excel': "xlsx",
    'csv': 'csv',
    'json': 'json',
}


def fetch_by_file(
        file_format: LITERAL_FILE_FORMAT,
        file_name: str,
        data: dict,
        unacceptable_file_format_exception: type[Exception] | Exception,
) -> dict:
    if file_format not in FILE_FORMAT_GENERATOR_DICT:
        raise unacceptable_file_format_exception

    return FILE_FORMAT_GENERATOR_DICT[file_format](
        file_name=file_name,
        data=data,
    )
