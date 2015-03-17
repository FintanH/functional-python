__author__ = 'halpenny'
from typeclasses.monad import Monad


class Either(Monad):

    def __irshift__(self, other):
        """ Acts as a single bind which can ease syntax in places.
        The reason it can only be used once is because Python thinks you're assigning.
        Cannot use it like:
            m a >>= f >>= g
        but rather accumulate:
            m a >>= f
            m a >>= g
        :param other: a -> m b
        :return: m b
        """
        return bind(other, self)

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

    def __eq__(self, other):
        if isinstance(other, Right):
            return self.get_value() == other.get_value()
        else:
            return False

    def __repr__(self):
        return "Right" + str(self.get_value())

    def get_value(self):
        return self.__value


class Left(Either):

    def __init__(self, b):
        self.__value = b

    def __eq__(self, other):
        if isinstance(other, Left):
            return self.get_value() == other.get_value()
        else:
            return False

    def __repr__(self):
        return "Left" + str(self.get_value())

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