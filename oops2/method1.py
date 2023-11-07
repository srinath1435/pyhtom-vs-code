class Account:
    min_bal=500
    
    def __init__(self,id,name):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=0
        
    def set_accBal(self,amount):
        self.acc_bal=self.acc_bal+amount
        
    @classmethod  
    def update_minBal(cls):
        cls.min_bal=600
        
    @staticmethod
    def cal_tax():
        return 10
        
a1=Account(101,"Srinath")
print(a1.__dict__)
a2=Account(102,"Amith")
a1.update_minBal()
print(a1.min_bal)
print(a2.min_bal)
# a1.update_minBal(5000)
# print(a1.__dict__)