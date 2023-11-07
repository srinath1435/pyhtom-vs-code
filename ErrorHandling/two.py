try:
    num1=int(input("enter the number:"))
except ValueError as err:
    print("the error:",err)
    num1 =0

print("GM")
print(num1)
print("GN")