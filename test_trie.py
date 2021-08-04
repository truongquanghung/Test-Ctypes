import numpy.ctypeslib as ctl
import ctypes
import pathlib
from ctypes import *

libname = pathlib.Path().absolute() / "trie.so"
c_lib = ctypes.CDLL(str(libname))

# while True:
#     s = input()
#     if s=="exit":
#         break
#     c_s = c_char_p(s.encode())
#     #  add string to trie
#     c_lib.insert_trie.argtypes = [c_char_p]
#     c_lib.insert_trie(c_s)


# while True:
#     s = input()
#     if s=="exit":
#         break
#     c_s = c_char_p(s.encode())
#     # get data from trie
#     print("Data")
#     c_lib.get_data_trie.argtypes = [c_char_p]
#     c_lib.get_data_trie(c_s)
#     print("--------------------")

import sqlite3

conn = sqlite3.connect('./db.sqlite3')

print("Input table name: ")
table = input()

print("Input column name: ")
column = input()

import timeit

start = timeit.default_timer()

sql = f"SELECT {column} from {table}"
cursor = conn.execute(sql)

for row in cursor:
    c_s = c_char_p(str(row[0]).encode('"ascii"', errors='ignore'))
    #  add string to trie
    c_lib.insert_trie.argtypes = [c_char_p]
    c_lib.insert_trie(c_s)

stop = timeit.default_timer()
print('Time: ', stop - start)  

while True:
    s = input()
    if s=="exit":
        break
    c_s = c_char_p(s.encode('ascii', errors='ignore'))
    # get data from trie
    print("--------------------")
    print("Data:")

    c_lib.get_num_trie.argtypes = [c_char_p]
    size = c_lib.get_num_trie(c_s)

    c_lib.get_size_trie.restype = ctl.ndpointer(dtype=ctypes.c_int, shape=(size,))
    res_size = c_lib.get_size_trie(c_s)

    c_lib.pass_data_trie.argtypes = [c_char_p]
    c_lib.pass_data_trie.restype = POINTER(c_char_p)
    res = c_lib.pass_data_trie(c_s)
    for i in range(0,size):
        print(res[i].decode('ascii', errors='ignore')[0:res_size[i]])
    
    print("--------------------")