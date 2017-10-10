x = [
    ("Guido", "van", "Rossum"),
    ("Haskel", "Curry"),
    ("John", "Backus")
]

import operator as op
from functools import partial

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(x)
sort_by_last(x)
print(x)

y = ["abc", "cba", "abb"]
sort_by_last(y)
print(y)
