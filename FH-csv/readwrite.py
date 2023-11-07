#read user data from keyboard and write in to csv
import csv

fp=open('user2.csv','w',newline="")
csv_obj=csv.writer(fp)
csv_obj.writerow(['name','email','city'])

no_users=int(input("enter no of users:"))

for x in range(no_users):
    name=input("enter User name")
    email=input("enter user email")
    city=input("enter user city")
    csv_obj.writerow([name,email,city])
    
    
fp.close()