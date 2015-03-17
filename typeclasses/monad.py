__author__ = 'halpenny'
from functor import Functor
from applicative import Applicative


class Monad(Functor, Applicative):

    def __init__(self):
        pass

    @staticmethod
    def ret(a):
        """ a -> m a
        :param a:
        :return:
        """
        pass

    @staticmethod
    def bind(f, a):
        """ (a -> m b) -> m a -> m b
        :param f:
        :param a:
        :return:
        """
        pass

    @staticmethod
    def fail(string):
        """ String -> m a
        :return:
        """
        pass