

from numpy import sctypes
np = type("numpytypes", (), dict((i.__name__, i)
                                 for i in set(sum(sctypes.values(), []))))


import array


NT_ARRAY_CODE = 0
NT_ARRAY_NAME = 1
NT_NUMPY_TYPE = 2
NT_PYTHON_TYPE = 3

NUMTYPED_LOOKUP = \
        { # native types
         int: ('q', "uint64", np.uint64, int), # unsigned integer
         float: ('d', "float64", np.float64, int), # floating point
         # array codes
         "b": ('b', "int8", np.int8, int), # signed integer
         "B": ('B', "uint8", np.uint8, int), # unsigned integer
         "h": ('h', "int16", np.int16, int), # signed integer
         "H": ('H', "uint16", np.uint16, int), # unsigned integer
         "i": ('i', "int16", np.int16, int), # signed integer
         "I": ('I', "uint16", np.uint16, int), # unsigned integer
         "l": ('l', "int32", np.int32, int), # signed integer
         "L": ('L', "uint32", np.uint32, int), # unsigned integer
         "q": ('q', "int64", np.int64, int), # signed integer
         "Q": ('Q', "uint64", np.uint64, int), # unsigned integer
         "f": ('f', "float32", np.float32, float), # floating point
         "d": ('d', "float64", np.float64, float), # floating point
         # convenience aliases
         "byte": ('b', "int8", np.int8, int), # signed integer
         "ubyte": ('B', "uint8", np.uint8, int), # unsigned integer
         "short": ('i', "int16", np.int16, int), # signed integer
         "ushort": ('I', "uint16", np.uint16, int), # unsigned integer
         "int": ('l', "int32", np.int32, int), # signed integer
         "uint": ('L', "uint32", np.uint32, int), # unsigned integer
         "long": ('q', "int64", np.int64, int), # signed integer
         "ulong": ('Q', "uint64", np.uint64, int), # unsigned integer
         "float": ('f', "float32", np.float32, int), # floating point
         "double": ('d', "float64", np.float64, int)} # floating point

for (tag, record) in tuple(NUMTYPED_LOOKUP.items()):
    for i in range(len(record)):
        if record[i] not in NUMTYPED_LOOKUP:
            NUMTYPED_LOOKUP[record[i]] = record


numtypes = tuple(NUMTYPED_LOOKUP.keys())


