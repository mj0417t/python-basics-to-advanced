class BankAccount:
    def __init__(self):
        self.balance=1000
    def _show_balance(self): #protected method
        print(f"Balance: Rs{self.balance}")
    def __update_balance(self, amount): #private method
        self.balance+=amount

    def deposit(self,amt):
        if amt>0:
            self.__update_balance(amt) #accessing pvt meth
            self._show_balance() #accessing protected meth
        else:
            print("Invalid deposit amount!")
    
acount=BankAccount()
acount._show_balance()
# acount.__update_balance(500) #error-pvt meth
acount.deposit(500) #use both meth internally