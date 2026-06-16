from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass        #abstract meth, no implementation here

    def make_gesture(self): #concrete meth
        return "Hands clamped together"
    
    @property
    @abstractmethod
    def language(self):  #abstract property
        pass
    

class English(Greet):
    def say_hello(self): # type: ignore
        return "Hello!"
    
    @property
    def language(self): # type: ignore
        return "english"

g=English()
print(g.say_hello())
print(g.make_gesture())
print(g.language)

# h=Greet() #error=can't instantiate, typeError