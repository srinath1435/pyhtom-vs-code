# class Account:
#     def __init__(self):
#         print("construcotr is spcial method")
        
# Account()
# Account()
# Account()
# Account()

class Account:
    def __init__(self,id,name):
        self.acc_id=id
        self.acc_name=name
        
a1=Account(101,"Srinath")
print(a1.__dict__)

a2=Account(102,"Arjun")
print(a2.__dict__)