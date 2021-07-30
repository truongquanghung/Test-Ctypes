# Test-Ctypes
Make library in C++ with Ctypes-Python
-
<br>

Build DLL with MinGW-w64 (version 64bit)
```powershell
g++ -shared -o testlib.so -fPIC test.cpp
```

Run Python script
```powershell
py test_ctypes.py
```
