class A:
    def __new__(cls):
        print("Creating instance")
        return super(A,cls).__new__(cls)
    def __init__(self):
        print("Initialising instance")

A()

#when __new__ does not return an instance
class B:
    def __new__(cls):
        print("Creating new instance")
    def __init__(self):
        print("Initialisinf instance")

print(B())

#returning a diff type from __new__
class C:
    def __new__(cls):
        print("Creating new instance")
        return "Hello World"

print(C())

#returning instnace of another class

class GoG:
    def __str__(self):
        return 'GoG instance'
    
class Geek:
    def __new__(cls):
        return GoG()
    def __init__(self):
        print("Inside init")

print(Geek())