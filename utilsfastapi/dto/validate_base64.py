from base64 import b64decode


def validate_base64(value: str | list[str]) -> None:
    if value:
        if isinstance(value, str):
            try:
                new_value = value.split(",", 1)[1]
                b64decode(new_value)
            except Exception:
                raise ValueError("فرمت base64 معتبر نیست.")
        else:
            for index, value_i in enumerate(value):
                try:
                    new_value = value_i.split(",", 1)[1]
                    b64decode(new_value)
                except Exception as e:
                    error_message = f"فرمت base64 برای آیتم {index} معتبر نیست."
                    raise ValueError(error_message)

    return None
