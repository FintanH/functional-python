__author__ = 'fintan'

from adt.maybe import fmap, Just, Nothing
from methods import compose
from functools import partial
import unittest


class TestLaws(unittest.TestCase):
    """
    Identity:
    fmap id      = id

    Composition:
    fmap (p . q) = (fmap p) . (fmap q)
    """""

    def test_id(self):
        self.assertTrue(fmap(self.id_, Just(1)) == Just(1))
        self.assertTrue(fmap(self.id_, Nothing()) == Nothing())

    def id_(self, a):
        return a

    def test_composition(self):
        p = lambda x: x + 1
        q = lambda x: x + 2
        p_dot_q = compose(p, q)

        a = Just(1)

        # Partially apply p . q with fmap
        left = partial(fmap, p_dot_q)

        # Compose the partially applied functions fmap . p and fmap . q
        right = compose(partial(fmap, p), partial(fmap, q))

        # Supply a test Maybe
        val_left = left(a)
        val_right = right(a)

        self.assertTrue(val_left == val_right)

        val_left = left(Nothing())
        val_right = right(Nothing())

        self.assertTrue(val_left == val_right)