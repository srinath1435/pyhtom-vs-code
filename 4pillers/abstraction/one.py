from abc import *
class Account:
    @abstractmethod(ABC)
    def cal_bal(self):
        pass


a1 = Account()

print(a1)
print(id(a1))