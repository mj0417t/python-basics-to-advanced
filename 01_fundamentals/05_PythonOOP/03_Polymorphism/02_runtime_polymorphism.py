class Animal:
    def sound(self):
        return "Some generic sound"
class Dog(Animal):
    def sound(self): # type: ignore
        return "Bark"
    
class Cat(Animal):
    def sound(self): # type: ignore
        return "Meow"
    
#Polymorphic behavior
animals=[Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())

#polymorphic built in function
print(len("Hello"))
print(len([1,2,3]))

print(max({1,2,3}))
print(max('a','z','x'))
print(type({1,2,3}))


#duck typing

class Cow:
    def speak(self):
        print("Moos")

class Bird:
    def speak(self):
        print("Chirps")

def make_sound(animal):
    animal.speak()


cow=Cow()
bird=Bird()

make_sound(cow)
make_sound(bird)