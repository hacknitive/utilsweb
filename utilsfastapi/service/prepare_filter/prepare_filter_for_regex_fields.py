def prepare_filter_for_regex_fields(
        fields_names: tuple[str, ...],
        inputs: dict,
        filter_: list,
):
    for field_name in fields_names:
        if inputs[field_name]:
            subfilter = list()
            for i in set(inputs[field_name]):
                subsubfilter = list()
                for j in i.split(" "):
                    subsubfilter.append({field_name: {'$regex': j}})

                if len(subsubfilter) > 1:
                    subfilter.append({'$and': subsubfilter})

                else:
                    subfilter.append(subsubfilter[0])

            filter_.append({'$or': subfilter})

    return filter_

