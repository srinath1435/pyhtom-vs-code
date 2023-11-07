class Account:

    def open_account(self):
        print('account opened successfully')
    
    def deposit_amount(self):
        print("Amount deposited")
    
    def withdrawl(self):
        print("Insufficent Bal")
    
    def get_bal(self):
        return 0
a1=Account()
#print(Account.__doc__)
# print(a1)
# print(a1.__dict__)
# print(a1.open_account().__doc__)
# print(a1.deposit_amount().__doc__)

a2=Account()
a2.open_account()
a2.deposit_amount()
a2.withdrawl()
print(a2.get_bal())