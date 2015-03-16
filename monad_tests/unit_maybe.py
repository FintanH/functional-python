__author__ = 'fintan'
import unittest
import maybe

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
        self.f = lambda x: maybe.Just(x + 1)
        self.g = lambda x: maybe.Just(x + 2)

    def test_left_identity(self):
        self.assertTrue(self.f(self.a) == maybe.bind(self.f, maybe.ret(self.a)))

    def test_right_identity(self):
        m = maybe.Just(self.a)
        self.assertTrue(maybe.bind(maybe.ret, m) == m)

    def test_associativity(self):
        m = maybe.Just(self.a)
        left = maybe.bind(self.g, maybe.bind(self.f, m))
        right = maybe.bind(self.f, maybe.bind(self.g, m))
        self.assertTrue(left == right)

if __name__ == '__main__':
    unittest.main()