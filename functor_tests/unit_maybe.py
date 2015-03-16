__author__ = 'fintan'

from adt.maybe import fmap, Just, Nothing
import unittest


class TestLaws(unittest.TestCase):
    """
    fmap id      = id

    Harder to test this without any functional composition
    fmap (p . q) = (fmap p) . (fmap q)
    """""

    def test_id(self):
        self.assertTrue(fmap(self.id_, Just(1)) == Just(1))
        self.assertTrue(fmap(self.id_, Nothing()) == Nothing())

    def id_(self, a):
        return a