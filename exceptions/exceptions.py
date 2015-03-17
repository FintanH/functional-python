__author__ = 'halpenny'


class NotInstanceOfFunctor(BaseException):
    def __init__(self):
        self.message = "Not an instance of Functor"


class NotInstanceOfApplicative(BaseException):
    def __init__(self):
        self.message = "Not an instance of Applicative"


class NotInstanceOfMonad(BaseException):
    def __init__(self):
        self.message = "Not an instance of Monad"