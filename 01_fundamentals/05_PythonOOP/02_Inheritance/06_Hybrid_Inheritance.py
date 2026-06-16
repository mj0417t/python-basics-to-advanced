class School:
    def fun1(self):
        print("This func is in School.")

class Stud1(School):
    def fun2(self):
        print("This func is in Student 1.")

class Stud2(School):
    def fun3(self):
        print("This func is in Student 2.")

class Stud3(Stud1, School):
    def fun4(self):
        print("This func is in Student 3.")

obj=Stud3()
obj.fun1()
obj.fun2()