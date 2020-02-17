# floaty

[![](https://badge.fury.io/py/floaty.svg)](https://pypi.org/project/floaty)

Bandages for boto3 floating-point wounds. [\*](https://github.com/boto/boto3/issues/665)

```py
from floaty import no_float, no_decimal

no_float(some_obj)  # replaces all floats with ints and Decimals
no_decimal(some_obj)  # replaces all Decimals with ints and floats
```
