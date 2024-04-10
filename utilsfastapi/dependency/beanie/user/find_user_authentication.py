from beanie import PydanticObjectId

from .document import UserAuthenticationDocument as Document


async def find_user_authentication(id_: PydanticObjectId) -> Document:
    return await Document.find_one(Document.id == id_)
