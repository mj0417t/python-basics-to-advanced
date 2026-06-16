class Dog:
    species = "Canine" #class attribute
    def __init__(self, name, age):
        self.name = name  #instance attribute
        self.age = age    #instance attribute

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def bark(self): #instance method
        return "Woof!"
    
    def get_info(self): #instance method
        return f"{self.name} is a {self.species} and is {self.age} years old"

#creating an object of the Dog class
dog1 = Dog("Rocky",2)

print(dog1.name)  # Output: Rocky
print(dog1.bark())  # Output: Woof!
print(dog1.age)   # Output: 2
print(dog1.species)  # Output: Canine

print(dog1)  # default Output: <__main__.Dog object at 0x7f8b8c9e5d30> (memory address of the object)   
#custom Output: Rocky is 2 years old (because of the __str__ method defined in the Dog class)

class Check:
    def __init__(self):
        print("Address of self: ", id(self))
obj=Check()
print("Address of obj: ", id(obj))


class Counter:
    def __init__(self):
        self.count=0
    def increment(self):
        self.count+=1
    def decrement(self):
        self.count-=1
    def getCount(self):
        return self.count

counter=Counter()
counter.increment()
counter.decrement()
counter.increment()
print(counter.getCount())

del dog1 #deleting obj
