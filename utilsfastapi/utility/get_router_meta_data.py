from src.dto.const_and_enum.router_details import ROUTER_DETAILS


def get_router_meta_data(name: str):
    default = {
        "name": name,
        "summary": "Summary is not set!",
        "description": "Description is not set!",
        "response_description": "Successful Response",
        "openapi_extra": None,
    }

    return ROUTER_DETAILS.get(name, default)
