__author__ = 'halpenny'
from functor import Functor
from instance_exceptions.method_exceptions import NotInstanceOfApplicative


class Applicative(Functor):

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