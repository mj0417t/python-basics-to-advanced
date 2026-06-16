class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child1 class.")

class Child2(Parent):
    def func3(self):
        print("This function is in child2 class.")

ob1 =Child1()
ob2=Child2()

ob1.func1()
ob1.func2()
ob2.func1()
ob2.func3()
