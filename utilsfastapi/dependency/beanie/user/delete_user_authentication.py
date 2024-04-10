from .document import UserAuthenticationDocument as Document


async def delete_user_authentication(obj: Document) -> None:
    await obj.delete()
    return None
