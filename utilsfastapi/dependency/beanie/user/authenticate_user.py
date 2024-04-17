from traceback import format_exc
from datetime import datetime, timedelta


from fastapi import Depends, status
from beanie import Document
from jwt.exceptions import DecodeError

from src.setting.setting import logger, CONFIG

from fastapi_addons.exception_handling import ProjectBaseException
from fastapi_addons.utility.get_message import get_message
from ...utility.decode_token import decode_token
from .find_user_authentication import find_user_authentication
from .delete_user_authentication import delete_user_authentication
from .find_user import find_user
from .update_user_authentication import update_user_authentication
from dms.auth.dependency.custom_api_key_header import CustomAPIKeyHeader

X_USER_TOKEN = CustomAPIKeyHeader(
    name="X-USER-TOKEN",
    auto_error=True,
    scheme_name="X-USER-TOKEN",
)

TIME_DELTA = timedelta(days=CONFIG.ACCESS_TOKEN.validity_period_in_days)

error = get_message("unauthorized_user")
project_base_exception = ProjectBaseException(
    code=status.HTTP_401_UNAUTHORIZED,
    success=False,
    data=None,
    error=error,
    message=error,
)


async def authenticate_user(token: str = Depends(X_USER_TOKEN)) -> Document:
    try:
        decoded_token = await decode_token(token=token)
        user_authentication_obj = await find_user_authentication(id_=decoded_token["user_authentication_id"])

        if user_authentication_obj is None:
            raise project_base_exception

        token_expiration_time = user_authentication_obj.last_login + TIME_DELTA
        if datetime.utcnow() > token_expiration_time:
            await delete_user_authentication(obj=user_authentication_obj)
            raise project_base_exception

        user_obj = await find_user(id_=decoded_token["user_id"])
        if user_obj is None:
            await delete_user_authentication(obj=user_authentication_obj)
            raise project_base_exception

        await update_user_authentication(obj=user_authentication_obj)

        return user_obj

    except ProjectBaseException:
        raise

    except DecodeError:
        raise project_base_exception

    except Exception:
        logger.error(format_exc())

        raise project_base_exception
