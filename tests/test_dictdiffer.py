from unittest import TestCase

from src.dictdiffer import DictDiffer


class TestDictDiffer(TestCase):
    def setUp(self):
        a = {'a': 1, 'b': 1, 'c': 0}
        b = {'a': 1, 'b': 2, 'd': 0}
        self.d = DictDiffer(b, a)

    def testAdded(self):
        assert self.d.added() == set(['d'])

    def testRemoved(self):
        assert self.d.removed() == set(['c'])

    def testChanged(self):
        assert self.d.changed() == set(['b'])

    def testUnchanged(self):
        assert self.d.unchanged() == set(['a'])
