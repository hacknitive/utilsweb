def prepare_filter_for_datetime_fields(
        fields_names: tuple[str, ...],
        inputs: dict,
        filter_: list,
):
    for field_name in fields_names:
        from_ = field_name + '_from'
        to = field_name + '_to'

        sub_filter = dict()
        if inputs[from_] is not None:
            sub_filter['$gte'] = inputs[from_]

        if inputs[to] is not None:
            sub_filter['$lte'] = inputs[to]

        if sub_filter:
            filter_.append({field_name: sub_filter})

    return filter_
