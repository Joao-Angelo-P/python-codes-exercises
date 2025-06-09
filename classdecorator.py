# Fazer decorator com classe


class A:
    d = {}

    def __init__(self, nome: str = ""):
        self.nome = nome

    def __call__(self, func):
        def _wrap(*args, **kw):
            self.d[self.nome] = [func.__name__, args, kw]
            return func(*args, **kw)

        return _wrap

class B:
    __slots__ = ("d", "nome")

    def __init__(self, nome: str = ""):
        self.nome = nome
        self.d = {}

    def __call__(self, func):
        def _wrap(*args, **kw):
            self.d[self.nome] = [func.__name__, args, kw]
            print(self.d)
            return func(*args, **kw)

        return _wrap


@A("funcao1")
def func1(*args, **kw):
    print("funcao -> 1")


func1(*range(10), **{"a": 0, "b": 1, "c": "1"})
print(A.d)
