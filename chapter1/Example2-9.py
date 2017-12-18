# -*- coding: utf-8 -*-

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.697667))

print(tokyo)
print(tokyo.coordinates)
print(tokyo[1])

