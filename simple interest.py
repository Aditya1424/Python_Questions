p=input("enter principal amt: ")
r=input("enter rate of interest: ")
t=input("enter time: ")
p=float(p)
r=float(r)
t=float(t)
SI=(p*r*t)/100
print("interest is=",SI)
amt= SI+p
print("amount is=",amt)