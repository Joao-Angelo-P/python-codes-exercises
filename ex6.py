#!/usr/bin/env python3

class A(object):
    def __init__(self, items=[]):
        self.items = items

class B(object):
    def __init__(self, items=None):
        if items is None:
            self.items = []

        else:
            self.items = items

a = A()
a.items += [x + 1 for x in range(10)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = B()
b.items += [(x + 1) * (-1) for x in range(10)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = A() # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = B() # []

a.items.append(58)

a.items # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 58]
b.items # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c.items # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 58]
d.items # []
