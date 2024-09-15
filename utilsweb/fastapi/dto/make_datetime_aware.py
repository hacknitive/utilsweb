from datetime import (
    timezone,
    datetime,
)
from typing import Tuple


def make_datetime_aware(
        inputs: dict[str, datetime],
        datetime_field_names: Tuple[str, ...],
        tzinfo=timezone.utc,
):
    for i in datetime_field_names:
        if inputs.get(i):
            inputs[i] = inputs[i].replace(tzinfo=tzinfo)
            inputs[i] = inputs[i].replace(microsecond=0)

    return inputs
