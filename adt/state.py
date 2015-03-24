__author__ = 'fintan'
from typeclasses.monad import Monad


class State(Monad):

    def __init__(self, s, a):
        self.__run_state = lambda state: (a, state)

    @staticmethod
    def run_state(m, s):
        return m.__runstate(s)

    @staticmethod
    def get(state):
        pass

    @staticmethod
    def put(state, s):
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
        return lambda s: State(s, a)

    @staticmethod
    def bind(f, a):
        current_state = lambda s: State(s, a)
        a, new_s = run_state(current_state)
        return State(f(a), new_s)
        pass

run_state = State.run_state