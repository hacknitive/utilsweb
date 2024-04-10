from beanie import PydanticObjectId

from src.storage.mongodb import UserDocument as Document


async def find_user(id_: PydanticObjectId) -> Document:
    return await Document.find_one(Document.id == id_)
