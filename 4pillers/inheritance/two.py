class Account:
    def __init__(self, name, email, branch):
        self.acc_name = name
        self.acc_email = email
        self.branch = branch
        print("Account - class constructor")
        
        
class SA(Account):
    def __init__(self, id,name, email,amount):
        super().__init__(name, email,"MarathaHAlli")
        self.acc_id=id
        self.acc_amount=amount
        print("SA- class constructor")
        
        
s1=SA(101,"Srianth",'sri@gmail.com',85000)


print(s1.__dict__)