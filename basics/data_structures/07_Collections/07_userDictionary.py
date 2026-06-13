from collections import UserDict

d={'a':1,'b':2, 'c':3}
ud=UserDict(d)

print(ud.data)  # Output: {'a': 1, 'b': 2, 'c': 3}

ud['d']=4
print(ud.data)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(ud['a'])  # Output: 1

ud=UserDict({'x': 10, 'y': 20})
print(ud.data)  # Output: {'x': 10, 'y': 20}

emptyUd=UserDict()
print(emptyUd.data)  # Output: {}

#Let's create a class inheriting from UserDict to implement a customized dictionary.
#creating a dictionary where deletion is not allowed

class MyDict(UserDict):
    def __del__(self):
        raise TypeError("Deletion is not allowed")
    def pop(self, key, default=None):
        raise TypeError("Deletion is not allowed")
    def popitem(self):
        raise TypeError("Deletion is not allowed")
    
# Driver's code
d = MyDict({'a':1,
    'b': 2,
    'c': 3})

print("Original Dictionary")
print(d)

d.pop(1)