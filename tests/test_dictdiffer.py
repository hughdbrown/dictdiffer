from unittest import TestCase

from src.dictdiffer import DictDiffer


class TestDictDiffer(TestCase):
    # Calculate the difference between two dictionaries as:
    # (1) items added
    # (2) items removed
    # (3) keys same in both but changed values
    # (4) keys same in both and unchanged values
    """
    >>> a = {'a': 1, 'b': 1, 'c': 0}
    >>> b = {'a': 1, 'b': 2, 'd': 0}
    >>> d = DictDiffer(b, a)
    >>> print "Added:", d.added()
    Added: set(['d'])
    >>> print "Removed:", d.removed()
    Removed: set(['c'])
    >>> print "Changed:", d.changed()
    Changed: set(['b'])
    >>> print "Unchanged:", d.unchanged()
    Unchanged: set(['a'])
    """
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
