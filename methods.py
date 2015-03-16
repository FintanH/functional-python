__author__ = 'fintan'
from functools import reduce


def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)