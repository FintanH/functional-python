__author__ = 'halpenny'
from applicative import Applicative
from instance_exceptions.method_exceptions import NotInstanceOfMonad


class Monad(Applicative):

    @staticmethod
    def ret(a):
        """ a -> m a
        :param a:
        :return:
        """
        raise NotInstanceOfMonad()
        pass

    @staticmethod
    def bind(f, a):
        """ (a -> m b) -> m a -> m b
        :param f:
        :param a:
        :return:
        """
        raise NotInstanceOfMonad()
        pass