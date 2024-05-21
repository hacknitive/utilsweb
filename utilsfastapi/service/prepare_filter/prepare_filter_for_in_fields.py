def prepare_filter_for_in_fields(
        fields_names: tuple[str, ...],
        inputs: dict,
        filter_: list,
):
    for field_name in fields_names:

        if inputs[field_name]:
            filter_.append({field_name: {'$in': set(inputs[field_name])}})

    return filter_
