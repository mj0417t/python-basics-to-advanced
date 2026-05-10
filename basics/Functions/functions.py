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
