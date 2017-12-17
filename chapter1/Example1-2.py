# -*- coding: utf-8 -*-
"""
    Example1-2.py
    ~~~~~~~~~~~~~
    Example 1-2 is a Vector class implementing the operations just described, through the use of the
    special methods __repr__, __abs__, __add__, and __mul__.

"""
#: Example 1-2. A simple two-dimensional vector class
from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #: string formatting operations
    #: %s uses the str function
    #: %r uses the repr function
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    #: hypot: 平方和的平方根
    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    #: scalar: 标量
    def __mul__(self, scalar):
        return Vector(self.x*scalar, self.y*scalar)





