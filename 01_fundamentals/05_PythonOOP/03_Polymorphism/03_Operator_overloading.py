print(1+2)
print('Geeks'+' for')
print(3*4)
print("Geeks"*4)


#user defined type
class A:
    def __init__(self, value):
        self.value=value

    def __add__(self, other):
        return self.value+other.value
    
obj1=A(1)
obj2=A(2)

print(obj1+obj2)
print(A.__add__(obj1,obj2))
print(obj1.__add__(obj2))


#addition of complex num

class Complex:
    def __init__(self, real,img):
        self.real=real
        self.img=img

    def __add__(self, other):
        return self.real+other.real , self.img+other.img

c1=Complex(1,2)
c2=Complex(2,3)
print(c1+c2)


#overloading <,>,== operator

class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self, other):
        return self.a > other.a
    
    def __lt__(self, other):
        return "ob1 is less than ob2" if self.a < other.a else "ob2 is less than ob1"
    def __eq__(self,other): # type: ignore
        return "Both are equal" if self.a==other.a else "Not equal"
    def __and__(self,other):
        return A(self.a and other.a)
    
ob1=A(2)
ob2=A(3)

if ob1 > ob2:
    print("ob1 is greater than ob2")
if ob1<ob2:
    print("ob2 is greater than ob1")
print(ob1==ob2)

a=A(True)
b=A(False)
c=a&b
print(c.a)

