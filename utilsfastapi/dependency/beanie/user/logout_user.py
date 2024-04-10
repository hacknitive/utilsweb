from traceback import format_exc

from fastapi import Depends

from src.setting.setting import logger
from fastapi_addons.exception_handling import ProjectBaseException
from fastapi_addons.utility.get_message import get_message
from ...utility.decode_token import decode_token
from .find_user_authentication import find_user_authentication
from .delete_user_authentication import delete_user_authentication
from .authenticate_user import X_USER_TOKEN


async def logout_user(token: str = Depends(X_USER_TOKEN)) -> None:
    try:
        decoded_token = await decode_token(token=token)
        user_authentication_obj = await find_user_authentication(id_=decoded_token["user_authentication_id"])

        if user_authentication_obj is not None:
            await delete_user_authentication(obj=user_authentication_obj)

        return None

    except Exception:
        logger.error(format_exc())

        error = get_message("server_error")
        raise ProjectBaseException(
            code=500,
            success=False,
            data=None,
            error=error,
            message=error,
        )
