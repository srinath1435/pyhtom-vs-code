#read csv file data.csv

import csv   
fp=open('data.csv','r')
csv_obj=csv.reader(fp)

print(csv_obj)
print(type(csv_obj))

for line in csv_obj:
    for word in line:
        print(word,end="")
    print()

fp.close