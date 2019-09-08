from decimal import Decimal
from numbers import Number


def no_decimal(obj):
    return _replace_all(obj, Decimal, float)


def no_float(obj):
    return _replace_all(obj, float, lambda x: Decimal(str(x)))


def read_item(query_return):
    item = query_return['Item'] if 'Item' in query_return else None
    return no_decimal(item)


def read_items(query_return):
    items = query_return['Items'] if 'Items' in query_return else []
    return [no_decimal(i) for i in items]


def _replace_all(obj, _type, replace):
    if isinstance(obj, bool):
        return obj

    if isinstance(obj, list):
        return [_replace_all(i, _type, replace) for i in obj]

    elif isinstance(obj, dict):
        return {k: _replace_all(v, _type, replace) for k, v in obj.items()}

    elif isinstance(obj, Number):
        return replace(obj) if obj % 1 else int(obj)

    else:
        return obj

