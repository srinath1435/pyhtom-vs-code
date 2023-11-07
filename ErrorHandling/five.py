try:
    fp=open('rajini.txt','r')
    data=fp.read()
    print(data)
    
except ValueError as err:
    pass
except NameError as err:
    pass
except FileNotFoundError as err:
    print("Bro! File Not Found")
    fp=open('def.txt','r')
    data =fp.read()
    print(data)
except:
    pass