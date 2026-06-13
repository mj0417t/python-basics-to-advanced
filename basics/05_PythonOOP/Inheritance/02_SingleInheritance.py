#Base class
class Parent:
    def func1(self):
        print("The function is in parent class.")

#Derived Class
class Child(Parent):
    def func2(self):
        print("The function is in child class.")

#Driver Code
obj=Child()
obj.func1()
obj.func2()