import builtins

exceptions = [
    name for name, obj in vars(builtins).items()
    if isinstance(obj, type) and issubclass(obj, BaseException)
]
i=1
print("List of Built in Exceptions in Python")
for item in exceptions:
    print(i,item)
    i+=1

#eg of BaseException  class
try:
    raise BaseException("This is a Base exception")
except BaseException as e:
    print(e)


#eg of Exception class
try:
    raise Exception("This is a generic exception")
except Exception as e:
    print(e)

#eg of ArithmeticError class
try:
    raise ArithmeticError("Arithmetic Error occured")
except ArithmeticError as e:
    print(e)

#eg of OverflowError class
import math
try:
    res=math.exp(1000)
except OverflowError as e:
    print(e)

import numpy as np
np.seterr(all='raise')

try:
    np.divide(1,0)
except FloatingPointError as e:
    print('FloatingPointError caught:',e)

try:
    assert 1==2, "Assertion failed"
except AssertionError as e:
    print(e)

class A:
    pass
obj=A()
try:
    obj.some_Attr # type: ignore
except AttributeError as e:
    print(e)

li=[1,2,3]
try:
    elem=li[5]
except IndexError as e:
    print(e)

d={'key':'value'}
try:
    val=d['key1']
except KeyError as e:
    print(e)
try: 
    li=[2]*(10**10)
except MemoryError as e:
    print(e)

try:
    open("non_existent_file.txt")  # File does not exist
except FileNotFoundError as e:     # More specific
    print("FileNotFoundError caught:", e)
except OSError as e:               # General OS-related error
    print("OSError caught:", e)
    