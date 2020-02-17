from decimal import Decimal
from numbers import Number


def no_decimal(obj):
    _replace_obj(obj, float)


def no_float(obj):
    _replace_obj(obj, lambda x: Decimal(str(x)))


def no_empty_string(obj):
    for k in list(obj.keys()):
        v = obj[k]

        if isinstance(v, dict):
            no_empty_string(v)

        if v == '':
            del obj[k]


def _replace_obj(obj, replace):
    if isinstance(obj, bool):
        return obj

    elif isinstance(obj, Number):
        return _replace_number(obj, replace)

    elif isinstance(obj, dict):
        return _replace_dict(obj, replace)

    elif isinstance(obj, list):
        return _replace_list(obj, replace)

    else:
        return obj


def _replace_number(n, replace):
    return replace(n) if n % 1 else int(n)


def _replace_dict(d, replace):
    for k, v in d.items():
        d[k] = _replace_obj(v, replace)

    return d


def _replace_list(l, replace):
    for i in range(len(l)):
        l[i] = _replace_obj(l[i], replace)

    return l

