def prepare_filter_for_boolean_fields(
        field_names: tuple[str],
        kwargs: dict,
        filter_: list,
):
    for field_name in field_names:
        if kwargs[field_name] is not None:
            filter_.append({field_name: kwargs[field_name]})

    return filter_
