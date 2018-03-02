#coding=utf-8
"""
A dictionary difference calculator
Originally posted as:
http://stackoverflow.com/questions/1165352/fast-comparison-between-two-python-dictionary/1165552#1165552
"""


class DictDiffer(object):
    """
    Calculate the difference between two dictionaries as:
    (1) items added
    (2) items removed
    (3) keys same in both but changed values
    (4) keys same in both and unchanged values
    """
    def __init__(self, current_dict, past_dict):
        self.current_dict, self.past_dict = current_dict, past_dict
        self.current_keys, self.past_keys = set(current_dict.keys()), set(past_dict.keys())
        self.intersect = self.current_keys.intersection(self.past_keys)

    def added(self):
        """ Find keys that have been added """
        return self.current_keys - self.intersect

    def removed(self):
        """ Find keys that have been removed """
        return self.past_keys - self.intersect

    def changed(self):
        """ Find keys that have been changed """
        return set(o for o in self.intersect
                   if self.past_dict[o] != self.current_dict[o])

    def unchanged(self):
        """ Find keys that are unchanged """
        return set(o for o in self.intersect
                   if self.past_dict[o] == self.current_dict[o])

    def new_or_changed(self):
        """ Find keys that are new or changed """
        return set(k for k, v in self.current_dict.items()
                   if k not in self.past_keys or v != self.past_dict[k])
