from base64 import b64decode


def validate_base64(value: str | list[str]) -> None:
    if isinstance(value, str):
        try:
            b64decode(value)
        except Exception:
            raise ValueError("فرمت base64 معتبر نیست.")
    else:
        for index, value_i in enumerate(value):
            try:
                b64decode(value_i)
            except Exception as e:
                error_message = f"فرمت base64 برای آیتم {index} معتبر نیست."
                raise ValueError(error_message)

    return None
