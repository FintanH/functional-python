__author__ = 'halpenny'
from functor import Functor
from exceptions.exceptions import NotInstanceOfApplicative


class Applicative(Functor):

    def __init__(self):
        pass

    @staticmethod
    def pure(a):
        """a -> f a
        :param a:
        :return:
        """
        raise NotInstanceOfApplicative()
        pass

    @staticmethod
    def apply(f, a):
        """f (a -> b) -> f a -> f b
        Equivalent to Haskell <*>
        :return:
        """
        raise NotInstanceOfApplicative()
        pass