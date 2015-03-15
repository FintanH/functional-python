__author__ = 'halpenny'


class Monad:

    def __init__(self):
        pass

    def ret(self, a):
        """ a -> m a
        :param a:
        :return:
        """
        pass

    def bind(self, f, a):
        """ (a -> m b) -> m a -> m b
        :param f:
        :param a:
        :return:
        """
        pass

    def fail(self):
        """ m a
        :return:
        """
        pass