from typing import Any

from beanie import Link
from bson import DBRef


def prepare_pydantic_object_id(
        pydantic_class_input: dict,
        fields: list | tuple,
) -> dict:
    if "_id" in fields:
        if "_id" in pydantic_class_input:
            pydantic_class_input["id"] = pydantic_class_input["_id"]
            del pydantic_class_input["_id"]

        fields.remove("_id")

    for field in fields:
        if field in pydantic_class_input:
            value_for_this_field = pydantic_class_input[field]

            if isinstance(value_for_this_field, list):
                prepared_field = list()
                for i in value_for_this_field:
                    result = convert_2_pydantic_object_id(value=i)
                    prepared_field.append(result)

                pydantic_class_input[field] = prepared_field

            else:
                pydantic_class_input[field] = convert_2_pydantic_object_id(value=value_for_this_field)

    return pydantic_class_input


def convert_2_pydantic_object_id(value: Any):
    if isinstance(value, Link):
        return value.ref.id

    elif isinstance(value, DBRef):
        return value.id

    elif isinstance(value, dict):

        try:
            return str(value["id"])
        except Exception:
            return str(value["_id"])

    return value
