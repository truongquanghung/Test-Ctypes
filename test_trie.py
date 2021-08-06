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

sql = f"SELECT {column} from {table}"
cursor = conn.execute(sql)
s = []
for row in cursor:
    s.append(str(row[0]))

start = timeit.default_timer()
for st in s:
    c_s = c_char_p(st.encode('ascii', errors='ignore'))
    #  add string to trie
    c_lib.insert_trie.argtypes = [c_char_p]
    c_lib.insert_trie(c_s)

stop = timeit.default_timer()
print('Time in C++: ', stop - start)  

from trie import Trie
start = timeit.default_timer()
test = Trie()
for st in s:
    test.insert_key(st)
stop = timeit.default_timer()
print('Time in Python: ', stop - start)  

while True:
    s = input()
    if s=="exit":
        break
    c_s = c_char_p(s.encode('ascii', errors='ignore'))
    # get data from trie
    print("--------------------")
    print("Data:")
    start = timeit.default_timer()
    c_lib.get_num_trie.argtypes = [c_char_p]
    size = c_lib.get_num_trie(c_s)

    c_lib.get_size_trie.restype = ctl.ndpointer(dtype=ctypes.c_int, shape=(size,))
    res_size = c_lib.get_size_trie(c_s)

    c_lib.pass_data_trie.argtypes = [c_char_p]
    c_lib.pass_data_trie.restype = POINTER(c_char_p)
    res = c_lib.pass_data_trie(c_s)
    for i in range(0,size):
        print(res[i].decode('ascii', errors='ignore')[0:res_size[i]])
    stop = timeit.default_timer()
    print('Time response in C++: ', stop - start)  
    
    start = timeit.default_timer()
    print(test.get_data(s))
    stop = timeit.default_timer()
    print('Time response in Python: ', stop - start)  

    # start = timeit.default_timer()
    # sql = f"SELECT {column} from {table} WHERE {column} LIKE '%{s}%'"
    # data = conn.execute(sql)
    # for row in data:
    #     print(row[0])
    # stop = timeit.default_timer()
    # print('Time response in raw Query: ', stop - start)  
    print("--------------------")