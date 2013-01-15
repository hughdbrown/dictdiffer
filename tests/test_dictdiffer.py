from unittest import TestCase

from src.dictdiffer import DictDiffer


class TestDictDiffer(TestCase):
    def setUp(self):
        a = {'a': 1, 'b': 1, 'c': 0}
        b = {'a': 1, 'b': 2, 'd': 0}
        self.d = DictDiffer(b, a)

    def test_added(self):
        self.assertEqual(self.d.added(), set(['d']))

    def test_removed(self):
        self.assertEqual(self.d.removed(), set(['c']))

    def test_changed(self):
        self.assertEqual(self.d.changed(), set(['b']))

    def test_unchanged(self):
        self.assertEqual(self.d.unchanged(), set(['a']))
