
try:
    from collections.abc import Collection, Iterable, \
            Sequence, MutableSequence, \
            Mapping, MutableMapping
except ImportError:
    from collections import Collection, Iterable, \
            Sequence, MutableSequence, \
            Mapping, MutableMapping


def isncollection(subject, n_items, collectiontype=Collection, itemtype=None):
    return isinstance(subject, collectiontype) and len(subject) == n_items \
            and (itemtype is None or all(isinstance(i, itemtype)
                                         for i in subject))


def isnsequence(subject, n_items, itemtype=None):
    return isncollection(subject, n_items, Sequence, itemtype)


def isntuple(subject, n_items, itemtype=None):
    return isncollection(subject, n_items, tuple, itemtype)

