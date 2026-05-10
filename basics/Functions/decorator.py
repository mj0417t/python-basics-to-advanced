import logging
logging.basicConfig(level=logging.INFO)

def logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger 
def add(a, b):
    return a + b  
#add = logger(add)  
print(add(3,4))

# add(3,4)
#    ↓
# wrapper(3,4)
#    ↓
# log message
#    ↓
# original add(3,4)
#    ↓
# returns 7


def decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@decorator
def greet():
    print("Hello, World!")
#greet = decorator(greet)  # Manually applying the decorator
greet();


#method decorator
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before the method execution.")
        result = func(self, *args, **kwargs)
        print("After the method execution.")
        return result
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello, World!")

obj=MyClass()
obj.say_hello()


#class decorator
def fun(cls):
    cls.class_name=cls.__name__
    return cls

@fun
class Person:
    pass
print(Person.class_name)  # Output: Person

#Built in decorator
class MathOp:
    @staticmethod
    def add(a, b):
        return a + b
res=MathOp.add(3,4)
print(res)

class Employee:
    raise_amount = 1.05
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount   
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)  # Output: 1.10    

class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value
    @property
    def area(self):
        import math
        return math.pi * (self.radius ** 2)
    
c=Circle(5)
print(c.radius)  # Output: 5    
print(c.area)    # Output: 78.53981633974483

c.radius = 10
print(c.area)
    


#chaining decorators

def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner

def decor2(func):
    def inner():
        x=func()
        return 2*x
    return inner

@decor1
@decor2
def num():
    return 10

@decor2
@decor1
def num2():
    return 10

print(num())   # Output: 400
print(num2())  # Output: 200