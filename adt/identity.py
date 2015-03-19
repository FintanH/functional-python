__author__ = 'fintan'
from typeclasses.monad import Monad


class ID(Monad):

    def __init__(self, a):
        self.__value = a

    def get_value(self):
        return self.__value

    def __irshift__(self, other):
        return bind(other, self)

    @staticmethod
    def do(value, *args):
        value = ret(value)
        for f in args:
            value >>= f

        return value

    @staticmethod
    def fmap(f, fa):
        return ID(f(fa.get_value()))

    @staticmethod
    def pure(a):
        return ID(a)

    @staticmethod
    def apply(f, a):
        g = f.get_value()
        a = a.get_value()
        return ID(g(a))

    @staticmethod
    def ret(a):
        return pure(a)

    @staticmethod
    def bind(f, m):
        a = m.get_value()
        return f(a)

fmap = ID.fmap
pure = ID.pure
apply = ID.apply
ret = ID.ret
bind = ID.bind