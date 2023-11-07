from abc import *

class Bank(ABC):
    
    @abstractmethod
    def cal_bal(self):
        pass
    
# b1=Bank()    #  we dont want create object? - abstract class

# print(b1.__dict__)

# we dont want create object? - abstract class
# child class is responsible to provide impl