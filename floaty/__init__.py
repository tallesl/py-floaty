from decimal import Decimal
from numbers import Number


def no_decimal(obj):
    return _replace_floating_point(obj, float)


def no_float(obj):
    return _replace_floating_point(obj, lambda x: Decimal(str(x)))


def read_item(query_return):
    item = query_return['Item'] if 'Item' in query_return else None
    return no_decimal(item)


def read_items(query_return):
    items = query_return['Items'] if 'Items' in query_return else []
    return [no_decimal(i) for i in items]


def _replace_floating_point(obj, replace):
    if isinstance(obj, bool):
        return obj

    if isinstance(obj, list):
        return [_replace_floating_point(i, replace) for i in obj]

    elif isinstance(obj, dict):
        return {k: _replace_floating_point(v, replace) for k, v in obj.items()}

    elif isinstance(obj, Number) and obj % 1:
        return replace(obj)

    else:
        return obj

