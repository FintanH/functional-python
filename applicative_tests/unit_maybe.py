__author__ = 'halpenny'
from adt.maybe import pure, apply, Just, Nothing
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
    """""
    def setUp(self):
        self.just_v = Just(1)
        self.nothing = Nothing()

    def test_identity(self):
        v = self.just_v
        f = pure(self.id_)
        self.assertTrue(apply(f, v) == v)

        v = self.nothing
        self.assertTrue(apply(f, v) == v)

    def id_(self, a):
        return a
