"""
Formas de montar uma fatorial -> n!
"""
from functools import reduce
from operator import mul

__all__=['fatorial_1', #1000 loops, best of 5: 62.8 usec per loop
         'fatorial_2', #1000 loops, best of 5: 65.2 usec per loop
         'fatorial_3', #1000 loops, best of 5: 64.6 usec per loop
         'fatorial_4'  #1000 loops, best of 5: 63.2 usec per loop
         ]


fatorial_1 = lambda n: reduce(mul, range(1, n+1, 1), 1)

def fatorial_2(n):
    if not n:
        return 1
    return n * fatorial_2(n-1)

def fatorial_3(n):
    result = 1
    while n:
        result *= n
        n -= 1
    return result

def fatorial_4(n):
    result = 1
    for i in range(1, n+1, 1):
        result *= i
    return result
