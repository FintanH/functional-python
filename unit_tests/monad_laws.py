__author__ = 'halpenny'

import unittest

import adt.maybe as maybe
from adt.maybe import Just, Nothing
import adt.either as either
from adt.either import Right, Left


############
# Monad Laws
############
"""
    Left identity:
    return a >>= f === f a

    Right identity:
    m >>= return === m

    Associativity:
    (m >>= f) >>= g ===	m >>= (\\x -> f x >>= g)
"""""


############
# Maybe
############
class TestMaybe(unittest.TestCase):

    def setUp(self):
        self.a = 1
        self.f = lambda x: Just(x + 1)
        self.g = lambda x: Just(x + 2)

    def test_left_identity(self):
        # Nothing case does not apply as this law relies on an 'a'
        # Test Just case
        self.assertTrue(self.f(self.a) == maybe.bind(self.f, maybe.ret(self.a)))

    def test_right_identity(self):
        # Test Just case
        m = Just(self.a)
        self.assertTrue(self.right_identity(m))

        # Test Nothing case
        m = Nothing()
        self.assertTrue(self.right_identity(m))

    def right_identity(self, m):
        return maybe.bind(maybe.ret, m) == m

    def test_associativity(self):
        # Test Just case
        m = Just(self.a)
        self.assertTrue(self.associativity(m))

        # Test Nothing case
        m = Nothing()
        self.assertTrue(self.associativity(m))

    def associativity(self, m):
        left = maybe.bind(self.g, maybe.bind(self.f, m))
        right = maybe.bind(self.f, maybe.bind(self.g, m))
        return left == right


############
# Either
############
class TestEither(unittest.TestCase):

    def setUp(self):
        self.a = "error"
        self.b = 1
        self.f = lambda x: Right(x + 1)
        self.g = lambda x: Right(x + 2)

    def test_left_identity(self):
        # Left case does not apply as ret only returns (Right a)
        #  Test Right case
        self.assertTrue(self.f(self.b) == either.bind(self.f, either.ret(self.b)))

    def test_right_identity(self):
        # Test Right case
        m = Right(self.b)
        self.assertTrue(self.right_identity(m))

        # Test Left case
        m = Left(self.a)
        self.assertTrue(self.right_identity(m))

    def right_identity(self, m):
        return either.bind(either.ret, m) == m

    def test_associativity(self):
        # Test Right case
        m = Right(self.b)
        self.assertTrue(self.associativity(m))

        # Test Left case
        m = Left(self.b)
        self.assertTrue(self.associativity(m))

    def associativity(self, m):
        left = either.bind(self.g, either.bind(self.f, m))
        right = either.bind(self.f, either.bind(self.g, m))
        return left == right


if __name__ == '__main__':
    unittest.main()