__author__ = 'fintan'
from instance_exceptions.method_exceptions import NotInstanceOfFunctor


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