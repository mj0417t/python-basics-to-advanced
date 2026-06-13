def func():
    print("This is a function.")
func()

def evenOdd(num):
    if num%2==0: 
        print(num,"is even.")
    else:
        print(num,"is odd.")    

evenOdd(10)
evenOdd(15)

#default arguments
def greet(name="Guest"):
    print("Hello",name)
greet()
greet("Alice")  

#keyword arguments

def strudent(name,age):
    print("Name: ",name,"age: ",age)
strudent(name="Alice",age=20)
strudent(age=20,name="Alice")


#positional arguments
def add(a,b):
    return a+b
print(add(5,10))    


#arbitrary arguments
def myFunc(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFunc('helo', 'bacho','love',"physics", name="Alice", age=20,place="new york")

#inner/nested functions
def outer():
    s = 'I love GeeksforGeeks'
    def inner():
        print(s)
        
    inner()
outer()


#pass by reference and pass by value
def modify_list(lst):
    lst.append(4)
    lst[0] = 0   
my_list = [1, 2, 3]
modify_list(my_list)    
print(my_list)  # Output: [0, 2, 3, 4] list is modified because it's mutable


def modify_number(num):
    num += 1                
my_number = 5
modify_number(my_number)
print(my_number)  # Output: 5     number is not modified because it's immutable  

#pass statement
def my_function():
    pass  # This function does nothing
my_function()

#global and local variables

myNum=6
def myFunction():
    global myNum
    print(myNum)
    myNum += 10  # This is a global variable
    print("Inside function, myNum =", myNum)
myFunction()
print("Outside function, myNum =", myNum)


#local & global var with same name
a = 1  # Global variable

def f():
    print("f():", a)  # Uses global a

def g():
    a = 2  # Local shadows global
    print("g():", a)

def h():
    global a
    a = 3  # Modifies global a
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)


#non keyword arguments
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#using args to multiple any number of values
def multiply(*args):
    res=1
    for arg in args:
        res*=arg
    return res
print("3 num multiplication:", multiply(5,2,3))
print("2 num multiplication:", multiply(4,5))

#keyword arguments
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, "=", val)

fun(s1='Python', s2='is', s3='Awesome')

def introduce(**kwargs):
    details = []
    for key,val in kwargs.items():
        details.append(key+"="+str(val))
    return ",".join(details)
print(introduce(name="Alice", age=30, city="New York"))

def student_info(*args, **kwargs):
    print("Subjects:", args)        # Positional arguments
    print("Details:", kwargs)       # Keyword arguments

# Passing subjects as *args and details as **kwargs
student_info("Math", "Science", "English", Name="Alice", Age=20, City="New York")