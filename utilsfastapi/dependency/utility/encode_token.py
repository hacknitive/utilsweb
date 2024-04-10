from datetime import datetime

from beanie import PydanticObjectId
from jwt import encode

from src.setting.setting import CONFIG

key = CONFIG.ACCESS_TOKEN.secret_key
algorithm = CONFIG.ACCESS_TOKEN.algorithm


async def encode_token(
        user_authentication_id: str | int | PydanticObjectId,
        user_id: str | int | PydanticObjectId,
        iat: datetime,
) -> str:
    payload = {
        "iat": iat,
        "user_authentication_id": str(user_authentication_id),
        "user_id": str(user_id),
    }

    return encode(
        payload=payload,
        key=key,
        algorithm=algorithm
    )
