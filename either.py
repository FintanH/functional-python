__author__ = 'halpenny'
from monad import Monad


class Either(Monad):

    @staticmethod
    def do(value, *args):
        value = ret(value)
        for f in args:
            value = bind(f, value)

        return value

    @staticmethod
    def ret(a):
        return Right(a)

    @staticmethod
    def fail(b):
        return Left(b)

    @staticmethod
    def bind(f, m):
        if is_left(m):
            return m
        else:
            return f(m.get_value())

    @staticmethod
    def is_left(m):
        return isinstance(m, Left)

    @staticmethod
    def is_right(m):
        return isinstance(m, Right)

    @staticmethod
    def either(f, g, m):
        if is_left(m):
            f(m.get_value())
        else:
            g(m.get_value())

    @staticmethod
    def lefts(ms):
        return [m for m in ms if is_left(m)]

    @staticmethod
    def rights(ms):
        return [m for m in ms if is_right(m)]

    @staticmethod
    def partition_eithers(ms):
        left = []
        right = []
        for m in ms:
            if is_left(m):
                left.append(m)
            else:
                right.append(m)

        return left, right


class Right(Either):

    def __init__(self, a):
        self.__value = a

    def get_value(self):
        return self.__value


class Left(Either):

    def __init__(self, b):
        self.__value = b

    def get_value(self):
        return self.__value

do = Either.do
ret = Either.ret
bind = Either.bind
fail = Either.fail
is_left = Either.is_left
is_right = Either.is_right
either = Either.either
lefts = Either.lefts
rights = Either.rights
partition_eithers = Either.partition_eithers