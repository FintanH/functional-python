__author__ = 'halpenny'
from adt.maybe import pure, apply, Just, Nothing
from methods import compose
import unittest


class TestLaws(unittest.TestCase):
    """
    Identity:
    pure id <*> v = v
                           
    Composition:
    pure (.) <*> u <*> v <*> w = u <*> (v <*> w)

    Homomorphism:
    pure f <*> pure x = pure (f x)

    Interchange:
    u <*> pure y = pure ($ y) <*> u

    Interchange is not really needed as Python doesn't have lazy semantics
    """""
    def setUp(self):
        self.just_v = Just(1)
        self.nothing = Nothing()

    def test_identity_just(self):
        v = self.just_v
        self.help_identity(v)

    def test_identity_nothing(self):
        v = self.nothing
        self.help_identity(v)

    def test_homomorphism(self):
        f = lambda x: x + 1
        x = 1
        self.assertTrue(apply(pure(f), pure(x)) == pure(f(x)))

    def help_identity(self, v):
        f = pure(self.id_)
        self.assertTrue(apply(f, v) == v)

    def id_(self, a):
        return a
