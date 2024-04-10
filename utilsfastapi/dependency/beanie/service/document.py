from typing import List

from beanie import (
    Document,
    Indexed,
)


class ServiceAuthenticationDocument(Document):
    class Settings:
        name = "service_authentication"

    service_name: Indexed(str, unique=True)
    hashed_api_key: Indexed(str, unique=True)
    allowed_method_path: List[str]
    is_locked: bool = False
    realm: List[str] = list()
