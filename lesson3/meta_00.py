#!/usr/bin/env python
# coding: utf-8
#http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Metaprogramming.html


# def howdy(self, you):
#     print("Howdy, " + you)
#
# MyList = type('MyList', (list,), dict(x=42, howdy=howdy))
#
# ml = MyList()
# ml.append("Camembert")
# print(ml)
# print(ml.x)
# ml.howdy("John")

class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

