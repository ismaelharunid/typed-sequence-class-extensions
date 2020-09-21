

from .numtyped import *
from .helpers import *


class NumTypedList(array.array, MutableSequence):
    
    _itemtype = None
    
    @property
    def itemtype(self):
        return self._itemtype
    
    @property
    def dtype(self):
        return NUMTYPED_LOOKUP[self._itemtype][NT_NUMPY_TYPE]
    
    @property
    def ntype(self):
        return NUMTYPED_LOOKUP[self._itemtype][NT_PYTHON_TYPE]
    
    def __new__(cls, *args, itemtype):
        try:
            record = NUMTYPED_LOOKUP[itemtype]
            self = array.array.__new__(cls, record[NT_ARRAY_CODE], *args)
            self._itemtype = record[NT_ARRAY_NAME]
            return self
        except:
            pass
        raise ValueError("Invalid itemtype {:}".format(repr(itemtype)))


class IntList(NumTypedList):

    def __new__(cls, *args):
        return super().__new__(cls, *args, itemtype=int)


class UIntList(NumTypedList):

    def __new__(cls, *args):
        return super().__new__(cls, *args, itemtype="uint64")


class FloatList(NumTypedList):

    def __new__(cls, *args):
        return super().__new__(cls, *args, itemtype=float)

