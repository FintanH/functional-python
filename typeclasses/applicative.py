__author__ = 'halpenny'
from functor import Functor


class Applicative(Functor):

    def __init__(self):
        pass

    @staticmethod
    def pure(a):
        """a -> f a
        :param a:
        :return:
        """
        pass

    @staticmethod
    def apply(f, a):
        """f (a -> b) -> f a -> f b
        Equivalent to Haskell <*>
        :return:
        """
        pass