__author__ = 'halpenny'


class Applicative:

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