class Animal: #parent class
    def __init__(self, name):
        self.name=name
    def info(self):
        print("Animal name: ", self.name)
    def sound(self):
        print(self.name, "Animal sound")


class Dog(Animal): #child class
    def __init__(self, name, breed):
        #calls constructor based on MRO
        super().__init__(name)
        self .breed = breed
    def details(self):
        print(self.name, " is a ", self.breed)
    def sound(self): #method overriding
        print(self.name, "barks")



d=Dog("SanSan", "Golden Retriever")
d.info()
d.details()
d.sound()


class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Emp(Person):
    def __init__(self,name,id):
        super().__init__(name,id)

emp=Emp('Jack',109)
print(emp.name, emp.id)