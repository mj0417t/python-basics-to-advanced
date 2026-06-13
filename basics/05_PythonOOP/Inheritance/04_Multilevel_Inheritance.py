#Base class
class GrandFather:
    def __init__(self, grandfathername):
        self.grandfathername=grandfathername

#intermediate class
class Father(GrandFather):
    def __init__(self,fathername, grandfathername):
        self.fathername=fathername
        super().__init__(grandfathername)

# Derived class
class Son(Father):
    def __init__(self,sonName, fathername, grandfathername):
        self.sonName=sonName
        super().__init__(fathername,grandfathername)

    def print_name(self):
        print('Grandfather name: ', self.grandfathername)
        print('Father name: ', self.fathername)
        print('Son name: ', self.sonName)



son=Son('Zayn Ali Warsi', 'Imran Ali', 'Mujibur Rahman')
print(son.grandfathername)
print(son.print_name())
