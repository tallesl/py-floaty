# floaty

![](https://badge.fury.io/py/floaty.svg)

Bandages for boto3 floating-point wounds. [*](https://github.com/boto/boto3/issues/665)

```py
no_float(some_obj)  # replaces all floats with ints and Decimals
no_decimal(some_obj)  # replaces all Decimals with ints and floats

read_item(query_return)  # reads up 'Item' from the dictionary and calls no_decimal on it
read_items(query_return)  # reads up 'Items' from the dictionary and calls no_decimal on each element of it
```
