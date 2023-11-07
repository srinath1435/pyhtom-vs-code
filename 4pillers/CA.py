from Account import *

class CA(Account):
    min_bal=2500
    def __init__(self,id, name, email, address, amount):
        super().__init__(name,email,address)
        self.acc_id=id
        self.acc_amount=amount
    
    def cal_bal(self):
        return self.acc_amount - self.min_bal
    

# c1= CA(101,"Srinath","sri@gmail.com","MarathaHalli",80500)

# print(c1.__dict__)
# print(c1.cal_bal())

# c1.open_account()
# c1.set_mobile_no(9550609532)
# print(c1.get_mobile_no())