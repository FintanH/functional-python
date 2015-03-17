__author__ = 'fintan'
from exceptions.exceptions import NotInstanceOfFunctor


class Functor:

    def __init__(self):
        pass

    @staticmethod
    def fmap(f, fa):
        """ (a -> b) -> f a -> f b
        :param f:
        :param fa:
        :return:
        """
        raise NotInstanceOfFunctor()
        pass