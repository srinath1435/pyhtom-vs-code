class Employee:
    org_name="TCS"                          #class level 
    org_loc="Bangalore"                     #class level 
    def __init__(self,id,name,sal):
        self.acc_id=id                      
        self.acc_name=name
        self.acc_sal=sal 



e1=Employee(101,'Rahul',45000)
e2=Employee(102,'Sonia',55000)
print(e1.__dict__)
print(e2.__dict__)
print(Employee.__dict__)     #it's printed class level varabiles in dict formate