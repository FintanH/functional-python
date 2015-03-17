__author__ = 'halpenny'
from typeclasses.monad import Monad
from typeclasses.functor import Functor


class Maybe(Monad):

    def __irshift__(self, other):
        """ Acts as a single bind which can ease syntax in places
        Cannot use it like:
            a >>= f >>= g
        but rather accumulate:
            a >>= f
            a >>= g
        :param other: a -> m b
        :return: m b
        """
        return bind(other, self)

    @staticmethod
    def do(value, *args):
        value = ret(value)
        for f in args:
            value >>= f

        return value

    @staticmethod
    def ret(a):
        return pure(a)

    @staticmethod
    def bind(f, m):

        if is_nothing(m):
            return m
        else:
            a = m.get_value()
            return f(a)

    @staticmethod
    def fail(_=None):
        return Nothing()

    @staticmethod
    def fmap(f, fa):
        if isinstance(fa, Nothing):
            return fa
        a = fa.get_value()
        b = f(a)
        return ret(b)

    @staticmethod
    def pure(a):
        return Just(a)

    @staticmethod
    def apply(f, a):
        if isinstance(a, Nothing) or isinstance(f, Nothing):
            return Nothing()
        func = f.get_value()
        val = a.get_value()
        return pure(func(val))

    @staticmethod
    def maybe(b, f, m):
        """ b -> (a -> b) -> Maybe a -> b
        The maybe function takes a default value, a function, and a Maybe value.
        If the Maybe value is Nothing, the function returns the default value.
        Otherwise, it applies the function to the value inside the Just and returns the result.
        :param b: Default value
        :param f: Function from a to b
        :param m: Maybe a
        :return: b
        """
        if is_nothing(m):
            return b
        else:
            return f(m.get_value())

    @staticmethod
    def is_just(m):
        """ Maybe a -> Bool
        The isJust function returns True iff its argument is of the form Just _.
        :return: Boolean
        """
        return isinstance(m, Just)

    @staticmethod
    def is_nothing(m):
        """ Maybe a -> Bool
        The isNothing function returns True iff its argument is Nothing.
        :return:
        """
        return isinstance(m, Nothing)

    @staticmethod
    def from_just(m):
        """ Maybe a -> a
        The fromJust function extracts the element out of a Just and throws an error if its argument is Nothing.
        :param m: Maybe a
        :return: a
        """
        if is_nothing(m):
            raise "Nothing Exception"
        else:
            return m.get_value()

    @staticmethod
    def from_maybe(a, m):
        if is_nothing(m):
            return a
        else:
            return m.get_value()

    @staticmethod
    def list_to_maybe(lis):

        if len(lis):
            return Just(lis[0])
        else:
            return Nothing()

    @staticmethod
    def maybe_to_list(m):

        if is_nothing(m):
            return []
        else:
            return [m.get_value()]

    @staticmethod
    def cat_maybes(ms):
        return [m.get_value() for m in ms if is_just(m)]

    @staticmethod
    def map_maybe(f, xs):
        res = []
        for x in xs:
            if is_just(f(x)):
                res.append(f(x).get_value())

        return res


class Just(Maybe):

    def __init__(self, a):
        self.__value = a

    def __eq__(self, other):
        if isinstance(other, Just):
            return self.__value == other.__value
        else:
            return False

    def __repr__(self):
        return "Just " + str(self.__value)

    def get_value(self):
        return self.__value


class Nothing(Maybe):

    def __init__(self):
        pass

    def __eq__(self, other):
        return isinstance(other, Nothing)

    def __repr__(self):
        return "Nothing"

"""Expose functions for importing"""
do = Maybe.do
ret = Maybe.ret
bind = Maybe.bind
fail = Maybe.fail
fmap = Maybe.fmap
pure = Maybe.pure
apply = Maybe.apply
maybe = Maybe.maybe
is_just = Maybe.is_just
is_nothing = Maybe.is_nothing
from_just = Maybe.from_just
from_maybe = Maybe.from_maybe
list_to_maybe = Maybe.list_to_maybe
maybe_to_list = Maybe.maybe_to_list
cat_maybes = Maybe.cat_maybes
map_maybe = Maybe.map_maybe

