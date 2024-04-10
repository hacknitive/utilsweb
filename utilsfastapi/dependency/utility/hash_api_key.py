from hashlib import new

from src.setting.setting import CONFIG

hash_salt = CONFIG.SERVICE_AUTHENTICATION.hash_salt
hash_method_name = CONFIG.SERVICE_AUTHENTICATION.hash_method_name


async def hash_api_key(api_key: str) -> str:
    hash_obj = new(hash_method_name)
    salted_api_key = str(api_key) + str(hash_salt)
    salted_api_key_bin = salted_api_key.encode("ascii")
    hash_obj.update(salted_api_key_bin)
    return hash_obj.hexdigest()
