#recreate FileNotFoundError and FileExistsError


#fp.open('rajini.txt','r')     # here///FileNotFound error
fp=open('emp.txt','x')         #FileExistsError

fp.read()

fp.close()