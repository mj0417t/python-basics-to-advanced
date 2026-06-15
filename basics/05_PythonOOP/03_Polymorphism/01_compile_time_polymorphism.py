
class Calculator:
    def multiply(self, a=1,b=1,*args):
        result=a*b
        for num in args:
            result*=num
        return result
    
calc=Calculator()

#using default arg
print(calc.multiply())
print(calc.multiply(4))

#using multiple arg
print(calc.multiply(2,3))
print(calc.multiply(2,3,4))