class Employee:
    def __init__(self, name, age, salary):
        self.name=name       #public attr
        self._age=age        #protected attr
        self.__salary=salary #private attr

    def show_salary(self):
        print('Salary: ', self.__salary)

class SubEmp(Employee):
    def show_age(self):
        print("Age: ", self._age) #accessible in subclass


emp=SubEmp("Fedrick",26,5000)
print(emp.name)  #public accessible 
emp.show_age()   #protected accessed through subclass
emp.show_salary()

#name mangling

class Parent:
    def __init__(self):
        self.__show()
    def show(self):
        print("Parent class")
    __show=show

class Child(Parent):
    def show(self):
        print("Child class")

obj=Child()
# obj.show()