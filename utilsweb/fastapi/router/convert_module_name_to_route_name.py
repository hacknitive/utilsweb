def convert_module_name_to_route_name(
        entity_name: str,
        module_name: str,
) -> str:
    return entity_name + ": " + module_name.rsplit(".", 1)[-1].replace("_", " ")
