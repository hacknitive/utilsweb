from datetime import datetime

from .document import UserAuthenticationDocument as Document


async def update_user_authentication(obj: Document) -> None:
    obj.last_login = datetime.utcnow()
    await obj.replace()
    return None
