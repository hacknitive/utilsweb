
class ProjectBaseException(Exception):
    def __init__(
            self,
            code: int,
            success: bool = None,
            data: None | dict | list = None,
            error: str | dict | list | None = None,
            message: str | dict | list | None = None,
            log_this_exc: bool = False
    ):
        self.code = code
        self.success = success
        self.data = data
        self.error = error
        self.message = message
        self.log_this_exc = log_this_exc
