__author__ = 'halpenny'
from monad import Monad


class Maybe(Monad):

    def __init__(self):
        pass

    def ret(self, a):
        return Just(a)

    def bind(self, f):

        if is_nothing(self):
            return self
        else:
            a = self.get_value()
            b = f(a)
            return Just(b)

    def fail(self):
        return Nothing()

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

    def __repr__(self):
        return "Just " + str(self.__value)

    def get_value(self):
        return self.__value


class Nothing(Maybe):

    def __init__(self):
        pass

    def __repr__(self):
        return "Nothing"

"""Expose functions for importing"""
maybe = Maybe.maybe
is_just = Maybe.is_just
is_nothing = Maybe.is_nothing
from_just = Maybe.from_just
from_maybe = Maybe.from_maybe
list_to_maybe = Maybe.list_to_maybe
maybe_to_list = Maybe.maybe_to_list
cat_maybes = Maybe.cat_maybes
map_maybe = Maybe.map_maybe

