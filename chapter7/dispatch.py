import html
import numbers

from functools import singledispatch
from collections import abc


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace("\n", "<br>\n")
    return "<p>{0}</p>".format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return "<pr>{0} (0x{0:x})</pre>".format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = "</li>\n<li>".join(htmlize(item) for item in seq)
    return "<url>\n<li>" + inner + "</li>\n</ul>"


if __name__ == '__main__':
    print(htmlize(1))
