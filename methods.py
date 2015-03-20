__author__ = 'fintan'
from functools import reduce, partial


def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)


def curry(f, a):
    return partial(f, a)


