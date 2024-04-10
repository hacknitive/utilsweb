from datetime import datetime

from beanie import (
    PydanticObjectId,
    Document,
)


class UserAuthenticationDocument(Document):
    class Settings:
        name = "user_authentication"

    last_login: datetime
    user_id: PydanticObjectId

