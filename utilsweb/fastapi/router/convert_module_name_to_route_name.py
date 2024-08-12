from os import sep

def convert_module_name_to_route_name(
        entity_name: str,
        module_name: str,
) -> str:
    FILE_NAME = module_name.rstrip(".py").rsplit(sep, 1)[-1]
    return f"{entity_name}:{FILE_NAME}"

