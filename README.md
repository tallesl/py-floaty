# floaty

[![](https://badge.fury.io/py/floaty.svg)](https://pypi.org/project/floaty)

Bandages for boto3 floating-point wounds. [\*](https://github.com/boto/boto3/issues/665)

```py
from floaty import *

no_float(some_obj)  # replaces all floats with ints and Decimals
no_decimal(some_obj)  # replaces all Decimals with ints and floats

read_item(query_return)  # reads up 'Item' from the dictionary, calls no_decimal on it, and returns it
read_items(query_return)  # reads up 'Items' from the dictionary, calls no_decimal on each element of it, and returns it
```
