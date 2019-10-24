from decimal import Decimal
from numbers import Number


def no_decimal(obj):
    _replace_floating_point(obj, float)


def no_float(obj):
    _replace_floating_point(obj, lambda x: Decimal(str(x)))


def read_item(query_return):
    item = query_return['Item'] if 'Item' in query_return else None
    no_decimal(item)

    return item


def read_items(query_return):
    items = query_return['Items'] if 'Items' in query_return else []

    for i in items:
        no_decimal(i)

    return items


def no_empty_string(obj):
    for k in list(obj.keys()):
        v = obj[k]

        if isinstance(v, dict):
            no_empty_string(v)

        if v == '':
            del obj[k]


def _replace_floating_point(obj, replace):
    for k, v in obj.items():

        if isinstance(v, dict):
            _replace_floating_point(v, replace)

        elif isinstance(v, Number):
            obj[k] = replace(v) if v % 1 else int(v)
