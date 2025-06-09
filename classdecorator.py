# Fazer decorator com classe
from functools import wraps


class A:
    d = {}

    def __init__(self, nome: str = ""):
        self.nome = nome

    def __call__(self, func):
        @wraps(func)
        def _wrap(*args, **kw):
            self.d[self.nome] = [func.__name__, args, kw]
            return func(*args, **kw)

        return _wrap


@A("funcao1")
def func1(*args, **kw):
    print("Funcao -> 1")


func1(*range(10), **{"a": 0, "b": 1, "c": "1"})
print(Deco.d)
