import os
from ctypes import *
# Connects to C++ .DLL-file
mydll = cdll.LoadLibrary(os.getcwd() + "\\Python_DLL_test_1.dll")
print(mydll.sum(5, 25))
print(mydll.mult(3, 40))
