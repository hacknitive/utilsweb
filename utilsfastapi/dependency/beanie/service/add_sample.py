from traceback import format_exc

from pymongo.errors import DuplicateKeyError

from src.setting.setting import logger
from .document import ServiceAuthenticationDocument as Document


async def add_sample(
        service_name: str = "foo_bar",
        hashed_api_key: str = "hashed_api_key",
        allowed_method_path: list[str] = None,
        is_locked: bool = False,
        realm: list[str] = None,
) -> None:
    allowed_method_path = allowed_method_path or ["CREATE:api/v1/user", "GET:api/v1/user", ]
    realm = realm or ["realm_1", "realm_2"]

    try:
        obj = Document(
            service_name=service_name,
            hashed_api_key=hashed_api_key,
            allowed_method_path=allowed_method_path,
            is_locked=is_locked,
            realm=realm,
        )

        await obj.create()
    except DuplicateKeyError:
        pass

    except Exception:
        logger.error(format_exc())
