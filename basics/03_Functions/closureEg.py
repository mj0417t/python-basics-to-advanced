def outerfunc(x):
    def innerfunc(y):
        return x+y
    return innerfunc

f=outerfunc(2)
g=outerfunc(5)

print(f(3))  # Output: 5
print(g(4))  # Output: 9


#counter eg
def makecounter():
    count=0
    def counter():
        nonlocal count
        count+=1
        return count
    return counter

counter1=makecounter();
print(counter1())  # Output: 1
print(counter1())  # Output: 2

#string formatting with closure
def pre(p):
    def add(t):
        return p+" "+t
    return add
string=pre("Hello")
print(string("World"))
print(string("Java"))


#MULTIPlier
def make_multiplier(x):
    def multiplier(n):
        return x*n
    return multiplier
multiple=make_multiplier(2)
print(multiple(3))
print(multiple(4))

# Check closure variables
#print(multiple.__closure__[0].cell_contents)  # Output: 2
