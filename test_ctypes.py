import numpy.ctypeslib as ctl
import ctypes
import pathlib

libname = pathlib.Path().absolute() / "testlib.so"
c_lib = ctypes.CDLL(str(libname))
print(c_lib.add_one(5))

import numpy as np

py_print_array = c_lib.print_array
py_print_array.argtypes = [ctl.ndpointer(np.float64, flags='aligned, c_contiguous'), ctypes.c_int]
A = np.array([1.4, 2.6, 3.0], dtype=np.float64)
py_print_array(A, 3)

# while True:
#     i = input()
#     c_lib.add(int(i))
#     size = c_lib.num()
#     print("size: ",size)
#     c_lib.out.restype = ctl.ndpointer(dtype=ctypes.c_int, shape=(size,))
#     for x in c_lib.out():
#         print(x)

from ctypes import *

while True:
    s = input()
    print("--------------------------------------------")
    print("Vector")
    c_s = c_char_p(s.encode())
    #  add string to vector
    c_lib.str.argtypes = [c_char_p, c_int]
    c_lib.str(c_s, len(s))

    # get data from vector
    size = c_lib.num_str() # size of vector
    print("size: ",size)
    c_lib.get_size.restype = ctl.ndpointer(dtype=ctypes.c_int, shape=(size,)) # size of each string
    c_lib.out_str.restype = POINTER(c_char_p) # vector
    res = c_lib.out_str()
    array_size = c_lib.get_size()
    for i in range(0,size):
        print(res[i].decode("ascii", errors='ignore')[0:array_size[i]])
    print("-------------------------------------------")