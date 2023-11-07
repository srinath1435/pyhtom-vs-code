class Parent:
    def __init__(self) :
        print("I am from child class")
    
    
class child(Parent):
    def __init__(self):
        super().__init__()
        print("I am from child class")
    
    
    
child()