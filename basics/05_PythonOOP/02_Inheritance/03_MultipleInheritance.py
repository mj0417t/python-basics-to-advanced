# Base Class 1
class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)

#Base class 2
class Father:
    fathername=""
    def father(self):
        print(self.fathername)

#Derived Class
class Son(Mother, Father):
    def parents(self):
        print("father : ", self.fathername)
        print("Mother: ", self.mothername)

s1=Son()
s1.fathername="Ram"
s1.mothername="Sita"
s1.parents()

#diamond problem
class A:
    def m(self):
        print("In class A")

class B(A):
    def m(self):
        print('In class B')
        super().m()

class C(A):
    def m(self):
        print('In class C')
        super().m()

class D(B,C):
    def m(self):
        print('In class D')
        super().m()

# print(D.mro())
# print(D.__mro__)

obj =D()
obj.m()

class H:
    def m(self):
        print('In class H')
class F(H):
    def m(self):
        print('In class F')
        H.m(self)
class G(H):
    def m(self):
        print('In class G')
class E(F,G):
    pass

obj2=E()
obj2.m()

