__author__ = 'fintan'
import unittest

from monad.maybe import Just, Nothing, bind, ret


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
        self.a = 1
        self.f = lambda x: Just(x + 1)
        self.g = lambda x: Just(x + 2)

    def test_left_identity(self):
        # Nothing case does not apply as this law relies on an 'a'
        # Test Just case
        self.assertTrue(self.f(self.a) == bind(self.f, ret(self.a)))

    def test_right_identity(self):
        # Test Just case
        m = Just(self.a)
        self.assertTrue(self.right_identity(m))

        # Test Nothing case
        m = Nothing()
        self.assertTrue(self.right_identity(m))

    def right_identity(self, m):
        return bind(ret, m) == m

    def test_associativity(self):
        # Test Just case
        m = Just(self.a)
        self.assertTrue(self.associativity(m))

        # Test Nothing case
        m = Nothing()
        self.assertTrue(self.associativity(m))

    def associativity(self, m):
        left = bind(self.g, bind(self.f, m))
        right = bind(self.f, bind(self.g, m))
        return left == right

if __name__ == '__main__':
    unittest.main()