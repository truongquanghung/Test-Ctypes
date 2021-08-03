import numpy.ctypeslib as ctl
import ctypes
import pathlib
from ctypes import *

libname = pathlib.Path().absolute() / "trie.so"
c_lib = ctypes.CDLL(str(libname))

while True:
    s = input()
    if s=="exit":
        break
    c_s = c_char_p(s.encode())
    #  add string to trie
    c_lib.insert_trie.argtypes = [c_char_p]
    c_lib.insert_trie(c_s)


while True:
    s = input()
    if s=="exit":
        break
    c_s = c_char_p(s.encode())
    # get data from trie
    print("Data")
    c_lib.get_data_trie.argtypes = [c_char_p]
    c_lib.get_data_trie(c_s)
    print("--------------------")