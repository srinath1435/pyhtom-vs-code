from Account import *

class SA(Account):
    min_bal=500     #static variable
    
    def __init__(self,id, name, email, address, amount):
        super().__init__(name,email,address)
        self.acc_id=id
        self.acc_amount=amount
        
        
        
    def cal_bal(self):
        return self.acc_amount- self.min_bal
    
    
    


    
# s1= SA(101,"Srinath","sri@gmail.com","MarathaHalli",80500)

# print(s1.__dict__)
# print(s1.cal_bal())
# s1.open_account()
# s1.set_mobile_no(9550609532)
# print(s1.get_mobile_no())       


# print(s1.__dict__)
      