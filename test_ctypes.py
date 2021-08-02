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

while True:
    i = input()
    c_lib.add(int(i))
    size = c_lib.num()
    print("size: ",size)
    c_lib.out.restype = ctl.ndpointer(dtype=ctypes.c_int, shape=(size,))
    for x in c_lib.out():
        print(x)

# libname = 'testlib.so'
# libdir = './'
# lib=ctl.load_library(libname, libdir)

# py_add_one = lib.add_one
# py_add_one.argtypes = [ctypes.c_int]
# value = 5
# results = py_add_one(value)
# print(results)