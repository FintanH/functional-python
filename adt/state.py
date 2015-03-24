__author__ = 'fintan'
from typeclasses.monad import Monad


class State(Monad):

    def __init__(self, s, a):
        self.__state = s
        self.__value = a

    def run_state(self, s):
        pass

    def get(self):
        pass

    def put(self, s):
        pass

    @staticmethod
    def fmap(f, fa):
        pass

    @staticmethod
    def pure(a):
        pass

    @staticmethod
    def apply(f, a):
        pass

    @staticmethod
    def ret(a):
        pass

    @staticmethod
    def bind(f, a):
        pass