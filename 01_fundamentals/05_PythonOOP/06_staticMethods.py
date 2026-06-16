class Calc:
    @staticmethod
    def add(a,b):
        return a+b
res=Calc.add(2,3)
print(res)


class Check:
    @staticmethod
    def is_even(n):
        return n%2==0
print(Check.is_even(7))
print(Check.is_even(10))

class Temp:
    @staticmethod
    def to_fahrenheit(c):
        return (c*9/5)+32
print(Temp.to_fahrenheit(25))

class Person:
    @staticmethod
    def is_adult(age):
        return age>=18
print(Person.is_adult(15))
print(Person.is_adult(21))