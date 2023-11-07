fp=open('data.txt',"r")

#here we have read entiry file

#data1=fp.read() 
#print(data1)


#here we read particular no_of lines beacuase we gives the some value on the parameters

#data2=fp.read(85)
#print(data2)


# here we have read only 1st line only

#data3=fp.readline()
#print(data3)




# here the entiry file comes from list formate
data4=fp.readlines()
print(data4)

#itareting the data using for loop
for data in data4:
    print(data)

fp.close()