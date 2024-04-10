from datetime import datetime
from pytz import UTC

from jwt import decode
from beanie import PydanticObjectId

from src.setting.setting import CONFIG

key = CONFIG.ACCESS_TOKEN.secret_key
algorithm = CONFIG.ACCESS_TOKEN.algorithm


async def decode_token(token: str) -> dict:
    payload = decode(
        jwt=token,
        algorithms=algorithm,
        key=key
    )

    payload['user_authentication_id'] = PydanticObjectId(payload['user_authentication_id'])
    payload['user_id'] = PydanticObjectId(payload['user_id'])
    payload['iat'] = datetime.fromtimestamp(payload['iat'], tz=UTC)

    return payload
