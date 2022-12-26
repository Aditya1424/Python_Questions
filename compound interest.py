p=float(input("enter principal: "))
r=float(input("enter interest: "))
n=int(input("enter time: "))
CI= p*((1+(r/100))**n)-p
print(CI)