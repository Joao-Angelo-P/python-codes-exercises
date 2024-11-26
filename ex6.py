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
a.items += [x + 1 for x in range(10)]

b = B()
b.items += [x + 1 for x in range(10)]

c = A()
d = B()

