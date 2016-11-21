#!/usr/bin/env python
# coding: utf-8
#http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Metaprogramming.html

class RegisterClasses(type):
    def __init__(cls, name, bases, atts):
        super(RegisterClasses, cls).__init__(name, bases, atts)
        cls.childrens = set()
        
        for base in bases:
            if hasattr(base,'childrens'):
                base.childrens.add(cls)

    # Metamethods, called on class objects:
    def __iter__(cls):
        return iter(cls.childrens)
    def __str__(cls):
        if len(cls.childrens)>0:
            return cls.__name__ + ": " + ", ".join([child.__name__ for child in cls])
        else:
            return cls.__name__

class Shape(object):
    __metaclass__ = RegisterClasses

class Round(Shape): pass
class Square(Shape): pass
class Triangular(Shape): pass
class Boxy(Shape): pass
print Shape
class Circle(Round): pass
class Ellipse(Round): pass
print Shape

for s in Shape: # Iterate over subclasses
    print s