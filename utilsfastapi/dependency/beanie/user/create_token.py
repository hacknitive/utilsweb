from datetime import datetime

from beanie import PydanticObjectId

from .create_user_authentication import create_user_authentication
from ...utility.encode_token import encode_token


async def create_token(user_id: PydanticObjectId) -> str:
    now = datetime.utcnow()

    obj = await create_user_authentication(
        user_id=user_id,
        last_login=now,
    )

    return await encode_token(
        user_authentication_id=obj.id,
        user_id=user_id,
        iat=now,
    )
