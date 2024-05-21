from typing import (
    Tuple,
    Dict,
)

# from .prepare_filter_for_boolean_fields import prepare_filter_for_boolean_fields
from .prepare_filter_for_regex_fields import prepare_filter_for_regex_fields
# from .prepare_filter_for_has_value_fields import prepare_filter_for_boolean_fields
from .prepare_filter_for_datetime_fields import prepare_filter_for_datetime_fields
from .prepare_filter_for_in_fields import prepare_filter_for_in_fields


def prepare_filter(
        inputs: Dict,
        fields_names_for_regex: Tuple[str, ...] = tuple(),
        fields_names_for_datetime: Tuple[str, ...] = tuple(),
        fields_names_for_in: Tuple[str, ...] = tuple(),

):
    filter_ = list()

    filter_ = prepare_filter_for_regex_fields(
        fields_names=fields_names_for_regex,
        inputs=inputs,
        filter_=filter_,
    )

    prepare_filter_for_datetime_fields(
        fields_names=fields_names_for_datetime,
        inputs=inputs,
        filter_=filter_,
    )

    prepare_filter_for_in_fields(
        fields_names=fields_names_for_in,
        inputs=inputs,
        filter_=filter_,
    )

    if filter_:
        return {'$and': filter_}
    else:
        return dict()
