"""
Work with any Iterable or Iterator
>>> list(cenumerate('ABC'))
[(0, 'A'), (1, 'B'), (2, 'C')]
>>> list(cenumerate([0, 1, 'AB']))
[(0, 0), (1, 1), (2, 'AB')]
>>> list(cenumerate(range(1, 6, 1)))
[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]"""

from typing import Iterable, Tuple, Any, Generator
def cenumerate(iterable: Iterable) -> Generator[Tuple[int, Any], None, None]:
    i = 0
    for item in iterable:
        yield i, item
        i += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=1)
