import json

fp=open('emp.json','r')
emp_obj=json.load(fp)

print(emp_obj)

fp.close()