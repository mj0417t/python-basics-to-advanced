#asssigning a function to a variable
def myfun(a,b):
    print("addition of a and b is: ",a+b)
f=myfun
f(2,3)  

def msg(name):
    return f"hello, {name}!"
f=msg
print(f("Alice"))  # Output: hello, Alice!

#passing fn as argument to another fn

def greet(func, name):
    return func(name)

print(greet(msg, "Rohana"))

#returning func from another func
def func1(msg):
    def func2():
        return f"Message is: {msg}"
    return func2
f=func1("Hello, World!")
print(f())  


#storing functions in data structures

def add(a,b):
    return a+b;
def subtract(a,b):
    return b-a
def multiply(a,b):
    return a*b
def divide(a,b):    
    return a/b

operations = {"add":add, "subtract":subtract, "multiply":multiply, "divide":divide}

for op_name, op_func in operations.items():
    print(f"{op_name}: {operations[op_name](10,15)}")