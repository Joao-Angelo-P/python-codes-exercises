"""
Work with any Iterable or Iterator
"""
from typing import Iterable, Tuple, Any, Generator

def cenumerate(iterable: Iterable) -> Generator[Tuple[int, Any], None, None]:
    i = 0
    for item in iterable:
        yield i, item
        i += 1
