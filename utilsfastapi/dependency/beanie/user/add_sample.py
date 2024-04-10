from traceback import format_exc
from datetime import datetime

from beanie import PydanticObjectId

from src.setting.setting import logger
from .document import UserAuthenticationDocument as Document


async def add_sample(
        last_login: datetime = datetime.utcnow(),
        user_id: PydanticObjectId = PydanticObjectId(),
) -> None:
    try:
        obj = Document(
            last_login=last_login,
            user_id=user_id,
        )

        await obj.create()

    except Exception:
        logger.error(format_exc())
