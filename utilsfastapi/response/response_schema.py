from typing import Optional

from pydantic import BaseModel


class ResponseSchema(BaseModel):
    status_code: int = 200
    success: bool = True
    message: str
    error: Optional[str] = None
    # data: Optional[]  # Should be overridden


class PaginatedSchema(BaseModel):
    current_page: int = 1
    page_size: int = 1000
    total: int


class PaginatedDataSchema(BaseModel):
    pagination: PaginatedSchema
    # data: list = list()  # Should be overridden
