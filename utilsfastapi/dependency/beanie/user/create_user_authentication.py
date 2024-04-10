from datetime import datetime

from beanie import PydanticObjectId

from .document import UserAuthenticationDocument as Document


async def create_user_authentication(
        user_id: PydanticObjectId,
        last_login: datetime,
) -> Document:
    obj = Document(
        last_login=last_login,
        user_id=user_id,
    )

    await obj.create()
    return obj
