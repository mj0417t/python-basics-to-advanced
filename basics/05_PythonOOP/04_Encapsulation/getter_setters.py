class Employee:
    def __init__(self):
        self.__salary=50000 #private attr
    def get_salary(self): #getter meth
        return self.__salary
    
    def set_salary(self,amt): #setter meth
        if amt>0:
            self.__salary=amt
        else:
            print("Invalid Salary amount!")

emp=Employee()
print(emp.get_salary()) #access salary using getter
emp.set_salary(60000) #update salary using setter
print(emp.get_salary())
        