__author__ = 'fintan'

import unittest

from adt.either import Right, Left, ret, bind


############
# Monad Laws
############


class TestLaws(unittest.TestCase):
    """
    Left identity:
    return a >>= f === f a

    Right identity:
    m >>= return === m

    Associativity:
    (m >>= f) >>= g ===	m >>= (\\x -> f x >>= g)
    """""

    def setUp(self):
        self.a = "error"
        self.b = 1
        self.f = lambda x: Right(x + 1)
        self.g = lambda x: Right(x + 2)

    def test_left_identity(self):
        # Left case does not apply as ret only returns (Right a)
        #  Test Right case
        self.assertTrue(self.f(self.b) == bind(self.f, ret(self.b)))

    def test_right_identity(self):
        # Test Right case
        m = Right(self.b)
        self.assertTrue(self.right_identity(m))

        # Test Left case
        m = Left(self.a)
        self.assertTrue(self.right_identity(m))

    def right_identity(self, m):
        return bind(ret, m) == m

    def test_associativity(self):
        # Test Right case
        m = Right(self.b)
        self.assertTrue(self.associativity(m))

        # Test Left case
        m = Left(self.b)
        self.assertTrue(self.associativity(m))

    def associativity(self, m):
        left = bind(self.g, bind(self.f, m))
        right = bind(self.f, bind(self.g, m))
        return left == right

if __name__ == '__main__':
    unittest.main()